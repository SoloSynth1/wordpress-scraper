from uuid import uuid4
from typing import List

from urllib.parse import urlparse

from wpscraper.connector import Connector, FileSystemConnector
from wpscraper.crawler import Crawler, WordPressCrawler

VALID_PATHS = [
    'posts',
    'tags',
    'categories'
]

def validate_paths(paths_to_crawl: List[str]):
    for path in paths_to_crawl:
        if path not in VALID_PATHS:
            raise NameError('path "{}" is not a valid path.'.format(path))

class CrawlSession:
    def __init__(self, url: str, paths_to_crawl: List[str], session_name: str = str(uuid4())):
        self.name = session_name
        self.url = url
        self.domain = urlparse(self.url).netloc
        self.paths = validate_paths(paths_to_crawl)
        self.crawler = None
        self.connectors = []

    def set_crawler(self, crawler: Crawler):
        self.crawler = crawler

    def add_connector(self, connector: Connector):
        self.connectors.append(connector)

    def execute(self):
        if not (self.crawler and self.connectors):
            raise AssertionError("No crawler and/or connector is specified.")
        for path in self.paths:
            products = self.crawler.

class DefaultCrawlSession(CrawlSession):
    def __init__(self, url: str, paths_to_crawl: List[str], session_name: str = str(uuid4())):
        super().__init__(url, paths_to_crawl, session_name)
        self.crawler = WordPressCrawler()
        self.connectors = [FileSystemConnector(folder='./data/{}'.format(self.domain), save_as_individual_files=False)]