from abc import ABC, abstractmethod


class Header(ABC):
    @abstractmethod
    def __init__(self):
        self.headers = None

    def __repr__(self):
        return str(self.headers)


class DefaultHeader(Header):
    def __init__(self, domain):
        self.headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding': '*',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Host': domain,
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'
        }