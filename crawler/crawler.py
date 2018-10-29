import requests
import json
import time
from crawler import utils

class WordPressCrawler:
    def __init__(self,url, headers):
        self.api = url+'/wp-json/wp/v2'
        self.headers = headers

    def _abstract_get(self, path, output_file):
        json_output = self._crawl_jsons(self.api + path)
        if output_file:
            utils.dump_json(json_output, output_file)
        return json_output

    def get_categories(self, output_file=None):
        return self._abstract_get('/categories', output_file)

    def get_tags(self, output_file=None):
        return self._abstract_get('/tags', output_file)

    def get_posts(self, output_file=None):
        return self._abstract_get('/posts', output_file)

    def _isjsonarray(self, json):
        return json and isinstance(json, list)

    def _crawl_jsons(self, url):
        output = []
        i = 1
        while True:
            json_repsonse = self._get_json_response('{}?per_page=100&page={}'.format(url,i))
            if self._isjsonarray(json_repsonse):
                output += json_repsonse
                i += 1
            else:
                break
        return output

    def _get_json_response(self, url):
        while True:
            try:
                response = requests.get(url, headers=self.headers, timeout=15)   # 10 seconds
                print('subpath: {}'.format(url))
                print('response code: {}'.format(response.status_code))
                print('response head: {}'.format(response.text[:300]))
                if response.status_code == 200 or response.status_code == 400:
                    return json.loads(response.text)
                else:
                    print("status code returned {}, waiting 30 seconds".format(response.status_code))
                    time.sleep(30)
            except requests.Timeout:
                print("Timed out.")
                continue
            except Exception as e:
                print("Exception occurred: {}".format(e))
                continue
