from uuid import uuid4
from typing import List

from urllib.parse import urlparse

from wpscraper.connector import FileSystemConnector
from wpscraper.crawler import WordPressCrawler
from wpscraper.header import Header, DefaultHeader


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
    def __init__(self, url: str, paths_to_crawl: List[str], session_name: str = str(uuid4()), header: Header = None, crawl_rate: int = 25, verify_ssl: bool = True):
        self.name = session_name
        self.url = url
        self.domain = urlparse(self.url).netloc
        self.header = header
        if not self.header:
            self.header = DefaultHeader(self.domain)
        self.paths = validate_paths(paths_to_crawl)
        self.crawler = WordPressCrawler(headers=header, crawl_rate=crawl_rate, verify_ssl=verify_ssl)
        self.connectors = [FileSystemConnector(folder="./data/{}".format(self.domain), save_as_individual_files=False)]

    def execute(self):
        for path in self.paths:
            products = self.crawler.
