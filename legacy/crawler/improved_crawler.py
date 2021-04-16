import json
import time
import os
from multiprocessing import Pool

import requests

from legacy.crawler import utils


class MultiThreadedCrawler:
    def __init__(self, url, headers, output_dir, crawl_rate=25, verify_ssl=True, timeout=30, retry_standoff=30,
                 max_retries=5):
        self.api = url + '/wp-json/wp/v2'
        self.headers = headers
        self.crawl_rate = crawl_rate
        self.verify_ssl = verify_ssl
        self.output_dir = output_dir
        self.timeout = timeout
        self.retry_standoff = retry_standoff
        self.max_retries = max_retries
        self.result_dump = []

    def _get(self, path, output_file):
        json_output = self._crawl_jsons(self.api + path)
        if output_file:
            utils.dump_json(json_output, output_file)
        return json_output

    def get_categories(self, output_file=None):
        if not output_file:
            output_file = os.path.join(self.output_dir, "cats.json")
        return self._get('/categories', output_file)

    def get_tags(self, output_file=None):
        if not output_file:
            output_file = os.path.join(self.output_dir, "tags.json")
        return self._get('/tags', output_file)

    def get_posts(self, output_file=None):
        if not output_file:
            output_file = os.path.join(self.output_dir, "posts.json")
        return self._get('/posts', output_file)

    def _isjsonarray(self, json):
        return json and isinstance(json, list)

    def set_output_dir(self, output_dir):
        self.output_dir = output_dir

    def _crawl_jsons(self, url):
        output = []
        i = 1
        while True:
            urls = ['{}?per_page={}&page={}'.format(url, 1, x) for x in range(i, i+self.crawl_rate, 1)]
            with Pool(self.crawl_rate) as p:
                json_responses = p.map(self._get_json_response, urls)
            json_responses = list(filter(None, json_responses))
            if self._isjsonarray(json_responses):
                output += json_responses
                i += self.crawl_rate
            else:
                break
        return output

    def _get_json_response(self, url):
        retries = 1
        while retries <= self.max_retries:
            print("attempt #{} of {} - {}".format(retries, self.max_retries, url))
            try:
                response = requests.get(url, headers=self.headers, timeout=self.timeout,
                                        verify=self.verify_ssl)  # 30 seconds
                print('response code: {}'.format(response.status_code))
                print('response head: {}'.format(response.text[:300]))
                # some API return valid response despite code 400 (weird I know)
                if response.status_code <= 400:
                    return json.loads(response.content.decode('utf-8').strip('\n').strip(' '))[0]
                else:
                    print("status code returned {}".format(response.status_code))
            except requests.Timeout:
                print("Timed out.")
            except Exception as e:
                print("Exception occurred:\nError Type: {}\nDetails: {}".format(type(e), str(e)))
            retries += 1
            print("waiting for {} seconds...".format(self.retry_standoff))
            time.sleep(self.retry_standoff)
        print("max no. of retries reached. exiting...")
        return None
