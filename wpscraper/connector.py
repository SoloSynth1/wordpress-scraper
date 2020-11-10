import os
from abc import ABC, abstractmethod
import hashlib
import json

from pymongo import MongoClient

from wpscraper.document import Document


def create_directory(directory):
    parent_directory = os.path.dirname(os.path.realpath(directory))
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
            f.write("\n")   # add linebreak at the end


class MongoDBConnector(Connector):
    def __init__(self, db_host: str, db_port: int, db_database: str, db_collection: str,
                 username: str, password: str, auth_source: str = "admin", auth_mechanism: str = "SCRAM-SHA-256"):
        self.db_host = db_host
        self.db_port = db_port
        self.db_database = db_database
        self.db_collection = db_collection
        self.username = username
        self.password = password
        self.auth_source = auth_source
        self.auth_mechanism = auth_mechanism
        self.client = MongoClient(host=self.db_host, port=self.db_port, username=self.username, password=self.password,
                             authSource=self.auth_source, authMechanism=self.auth_mechanism)

    def process_document(self, document: Document, resource: str):
        doc_id = self.client[self.db_database][self.db_collection].insert_one(document=document.data).inserted_id
        if not doc_id:
            raise ConnectionError("Couldn't insert document into MongoDB.")
