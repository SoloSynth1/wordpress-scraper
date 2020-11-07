from uuid import uuid4
from typing import List
import datetime

from urllib.parse import urlparse

from wpscraper.connector import Connector, FileSystemConnector
from wpscraper.crawler import Crawler, SimpleRequestsCrawler
from wpscraper.headers import DefaultHeaders
from wpscraper.document import JSONDocument

VALID_PATHS = [
    'posts',
    'tags',
    'categories'
]


def validate_paths(resources: List[str]):
    for path in resources:
        if path not in VALID_PATHS:
            raise NameError('path "{}" is not a valid path.'.format(path))
    return resources


class CrawlSession:
    def __init__(self, url: str, resources: List[str], session_id: str = str(uuid4())):
        self.session_id = session_id
        self.url = url
        self.domain = urlparse(self.url).netloc
        self.resources = validate_paths(resources)
        self.crawler = None
        self.connectors = []

    def set_crawler(self, crawler: Crawler):
        self.crawler = crawler

    def add_connector(self, connector: Connector):
        self.connectors.append(connector)

    def execute(self):
        if not (self.crawler and self.connectors):
            raise AssertionError("No crawler and/or connector is specified.")
        for resource in self.resources:
            while True:
                raw_documents = self.crawler.crawl(resource=resource)
                if not raw_documents:
                    break
                current_timestamp = datetime.datetime.utcnow().isoformat()
                documents = [JSONDocument(document, resource_type=resource, session_id=self.session_id,
                                          crawledtime=current_timestamp) for document in raw_documents]
                for document in documents:
                    for connector in self.connectors:
                        connector.process_document(resource=resource, document=document)


class DefaultCrawlSession(CrawlSession):
    def __init__(self, url: str, session_id: str = str(uuid4())):
        resources = ['posts', 'tags', 'categories']
        super().__init__(url, resources=resources, session_id=session_id)
        headers = DefaultHeaders(self.domain)
        self.crawler = SimpleRequestsCrawler(url=self.url, headers=headers)
        self.connectors = [FileSystemConnector(folder='./data/{}'.format(self.domain), save_as_individual_files=True)]

