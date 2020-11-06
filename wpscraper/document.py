import json
from typing import Any
from abc import ABC, abstractmethod


class Document(ABC):
    @abstractmethod
    def __init__(self, raw_data: Any):
        pass

    @abstractmethod
    def process_raw_data(self):
        pass


class JSONDocument(Document):
    def __init__(self, raw_data: str):
        super().__init__(raw_data)
        self.raw_data = raw_data
        self.data = None
        self.process_raw_data()

    def process_raw_data(self):
        self.data = json.loads(self.raw_data)

    def __repr__(self):
        return self.data
