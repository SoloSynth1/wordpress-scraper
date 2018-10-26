import requests
import json
import time
from crawler import utils

class WordPressCrawler:
    def __init__(self,url, headers):
        self.api = url+'/wp-json/wp/v2'
        self.headers = headers

    def get_categories(self, output_file=None):
        categories = self._crawl_jsons(self.api + '/categories')
        if output_file:
            utils.ensure_file_directory(output_file)
            with open(output_file, 'w') as f:
                f.write(json.dumps(categories))
        return categories

    def get_tags(self, output_file=None):
        tags = self._crawl_jsons(self.api + '/tags')
        if output_file:
            utils.ensure_file_directory(output_file)
            with open(output_file, 'w') as f:
                f.write(json.dumps(tags))
        return tags

    def get_posts(self, output_file=None):
        posts = self._crawl_jsons(self.api+'/posts')
        if output_file:
            utils.ensure_file_directory(output_file)
            with open(output_file, 'w') as f:
                f.write(json.dumps(posts))
        return posts

    def _isjsonarray(self, json):
        return json and isinstance(json, list)

    def _crawl_jsons(self, url, param='page'):
        output = []
        i = 1
        while True:
            json_repsonse = self._get_json_response('{}?{}={}'.format(url,param,i))
            if self._isjsonarray(json_repsonse):
                output += json_repsonse
                i += 1
            else:
                break
        return output

    def _get_json_response(self, url):
        while True:
            try:
                response = requests.get(url, headers=self.headers, timeout=5)   # 5 seconds
                print('subpath: {}'.format(url))
                print('response code: {}'.format(response.status_code))
                print('response: {}'.format(response.text))
                if response.status_code == 200 or response.status_code == 400:
                    return json.loads(response.text)
                else:
                    print("status code returned {}, waiting 30 seconds".format(response.status_code))
                    time.sleep(30)
            except requests.Timeout:
                print("Timed out.")
                continue
