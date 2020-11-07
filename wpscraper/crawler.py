import json
import time
from abc import ABC, abstractmethod

from wpscraper.headers import Headers

import requests


class Crawler(ABC):
    def __init__(self, url, headers: Headers, verify_ssl: bool, timeout: int, max_retries: int):
        self.api_path = url + '/wp-json/wp/v2/'
        self.headers = headers
        self.verify_ssl = verify_ssl
        self.timeout = timeout
        self.max_retries = max_retries

    @abstractmethod
    def crawl(self, resource: str, *args, **kwargs):
        pass


class SimpleRequestsCrawler(Crawler):
    def __init__(self, url, headers: Headers = None, crawl_rate: int = 25, verify_ssl: bool = True, timeout: int = 30,
                 max_retries: int = 5, constant_retry_standoff: int = 30):
        super().__init__(url=url, headers=headers, verify_ssl=verify_ssl, timeout=timeout, max_retries=max_retries)
        self.crawled_resource_count = {}
        self.crawl_rate = crawl_rate
        self.constant_retry_standoff = constant_retry_standoff

    def crawl(self, resource: str):
        documents = []
        if resource in self.crawled_resource_count.keys():
            self.crawled_resource_count[resource] = 0
        objs = self._get_json_response(
            self.api_path+resource+'?per_page={}&page={}'.format(self.crawl_rate, self.crawled_resource_count[resource])
        )
        if objs and isinstance(objs, list):
            documents = objs
            self.crawled_resource_count[resource] += 1
        else:
            print("No documents are crawled.")
        return documents

    def _get_json_response(self, url):
        attempt_count = 1
        while attempt_count < self.max_retries:
            try:
                response = requests.get(url, headers=self.headers, timeout=self.timeout, verify=self.verify_ssl)
                print('subpath: {}'.format(url))
                print('response code: {}'.format(response.status_code))
                print('response head: {}'.format(response.text[:300]))
                if response.status_code == 200 or response.status_code == 400:
                    return json.loads(next(response.iter_lines()))
                else:
                    print("status code returned {}".format(response.status_code))
            except requests.Timeout:
                print("Timed out.")
                continue
            except Exception as e:
                print("Exception occurred: {}".format(e))
                continue
            finally:
                attempt_count += 1
                print("waiting for {} seconds...".format(self.constant_retry_standoff))
                time.sleep(self.constant_retry_standoff)
                print("retrying... (attempt {} of {})".format(attempt_count, self.max_retries))
        print("max no. of retries reached. exiting...")
        return None

    def get_crawled_stat(self):
        return self.crawled_resource_count

