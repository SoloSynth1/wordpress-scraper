import os

from urllib.parse import urlparse

from . import crawler


class BasicJSONCrawlerManager:

    def __init__(self, url, output_dir, crawl_rate=25):
        self.url = url
        self.output_dir = output_dir
        self.domain = urlparse(url).netloc
        self.crawl_rate = crawl_rate
        self.headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding': '*',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Host': self.domain,
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'
        }

    def crawl(self):
        wpc = crawler.WordPressCrawler(self.url, self.headers, self.crawl_rate)
        wpc.get_tags(os.path.join('{}'.format(self.output_dir), 'tags.json'))
        wpc.get_categories(os.path.join('{}'.format(self.output_dir), 'cats.json'))
        wpc.get_posts(os.path.join('{}'.format(self.output_dir), 'posts.json'))
