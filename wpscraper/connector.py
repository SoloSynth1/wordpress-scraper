import os
from abc import ABC, abstractmethod
import hashlib
import json

import pymongo

from wpscraper.document import Document


def create_directory(directory):
    directory = os.path.dirname(os.path.realpath(directory))
    parent_directory = os.path.dirname(directory)
    if not os.path.exists(parent_directory):
        create_directory(parent_directory)
    if not os.path.exists(directory):
        os.makedirs(directory)


class Connector(ABC):
    @abstractmethod
    def process_document(self, document: Document, *args, **kwargs):
        pass


class FileSystemConnector(Connector):
    def __init__(self, folder: str, save_as_individual_files: bool = False):
        self.folder = folder
        self.save_as_individual_files = save_as_individual_files
        create_directory(self.folder)

    def process_document(self, document: Document, resource: str):
        json_string = json.dumps(document.data)
        if self.save_as_individual_files:
            self._generate_individual_document(json_string)
        else:
            self._append_resource_document(resource, json_string)

    def _generate_individual_document(self, json_string: str):
        filename = hashlib.sha256(json_string.encode('utf-8')).hexdigest()
        file_to_write = os.path.join(self.folder, "{}.json".format(filename))
        with open(file_to_write, 'w') as f:
            f.write(json_string)

    def _append_resource_document(self, resource: str, json_string: str):
        file_to_write = os.path.join(self.folder, "{}.json".format(resource))
        with open(file_to_write, 'a') as f:
            f.write(json_string)


class MongoDBConnector(Connector):
    def __init__(self, connection_string: str, collection_name: str):
        self.connection_string = connection_string
        self.collection_name = collection_name

    def process_document(self, document: Document, resource: str):
        # TODO: Implement actual process to upload document to MongoDB
        pass