import os
from abc import ABC, abstractmethod

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
    def process_document(self, document: Document):
        pass


class FileSystemConnector(Connector):
    def __init__(self, folder: str, save_as_individual_files: bool = False):
        self.folder = folder
        self.save_as_individual_files = save_as_individual_files
        create_directory(self.folder)

    def process_document(self, document: Document):
        pass


class MongoDBConnector(Connector):
    def __init__(self, connection_string: str, collection_name: str):
        self.connection_string = connection_string
        self.collection_name = collection_name

    def process_document(self, document: Document):
        pass