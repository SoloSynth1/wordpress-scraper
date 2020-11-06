import json
import time
import os
import re

import requests


class WordPressCrawler:
    def __init__(self, url, headers, crawl_rate, verify_ssl):
        self.api = url+'/wp-json/wp/v2'
        self.headers = headers
        self.crawl_rate = crawl_rate
        self.verify_ssl = verify_ssl
        # self.session = HTMLSession()

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
            json_repsonse = self._get_json_response('{}?per_page={}&page={}'.format(url, self.crawl_rate, i))
            if self._isjsonarray(json_repsonse):
                output += json_repsonse
                i += 1
            else:
                break
        return output

    def _get_json_response(self, url, max_retries=5, retry_standoff_time=30):
        retries = 0
        while True:
            try:
                # response = self.session.get(url, headers=self.headers, timeout=30)
                # # response.html.render()
                response = requests.get(url, headers=self.headers, timeout=30, verify=self.verify_ssl)   # 30 seconds
                print('subpath: {}'.format(url))
                print('response code: {}'.format(response.status_code))
                print('response head: {}'.format(response.text[:300]))
                if response.status_code == 200 or response.status_code == 400:
                    return json.loads(next(response.iter_lines()))
                else:
                    print("status code returned {}".format(response.status_code))
                    retries += 1
                    if retries < max_retries:
                        print("waiting for {} seconds...".format(retry_standoff_time))
                        time.sleep(retry_standoff_time)
                        print("retrying... (attempt {} of {})".format(retries, max_retries))
                    else:
                        print("max no. of retries reached. exiting...")
                        break
            except requests.Timeout:
                print("Timed out.")
                continue
            except Exception as e:
                print("Exception occurred: {}".format(e))
                continue


def ensure_file_directory(file):
    inception(os.path.dirname(os.path.realpath(file)))


def inception(directory):
    parent_directory = os.path.dirname(directory)
    if not os.path.exists(parent_directory):
        inception(parent_directory)
    if not os.path.exists(directory):
        os.makedirs(directory)


def dump_json(json_object,output_file):
    ensure_file_directory(output_file)
    with open(output_file, 'w') as f:
        f.write(json.dumps(json_object))


def remove_leading_scripts(response_text):
    cleaned_text = re.search(r'(\[.*)', response_text)
    return cleaned_text.group(1)
