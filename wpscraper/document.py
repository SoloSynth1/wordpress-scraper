from typing import Any
from abc import ABC, abstractmethod


class Document(ABC):
    def __init__(self, raw_data: Any):
        self.raw_data = raw_data
        self.data = None

    @abstractmethod
    def process_raw_data(self, *args, **kwargs):
        pass

    def __repr__(self):
        return self.data


class JSONDocument(Document):
    # receive and process raw JSON document from WP-JSON API
    def __init__(self, raw_data: dict, **kwargs):
        super().__init__(raw_data)
        self.process_raw_data(kwargs)

    def process_raw_data(self, kwargs: dict):
        self.data = {"data": self.raw_data}
        self.data.update(kwargs)


class RawDocument(Document):
    def __init__(self, raw_data: dict):
        super().__init__(raw_data)
        self.process_raw_data()

    def process_raw_data(self):
        self.data = self.raw_data
