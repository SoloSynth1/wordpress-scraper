from legacy.crawler import crawler
import os

url = "https://www.infosecblog.org"
output_dir = os.path.join('.', 'data', 'infosecblog.org')
headers = {
        'Accept':'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding':'*',
        'Accept-Language':'zh-CN,zh;q=0.8',
        'Cookie': '__cfduid=dfc1c22a9bb42efd57b3c2231d0c43d2a1540799668; _ga=GA1.2.958394734.1540799670; _gid=GA1.2.1380839925.1540799670',
        'Connection':'keep-alive',
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/70.0.3538.67 Chrome/70.0.3538.67 Safari/537.36',
        'X-Requested-With':'XMLHttpRequest'
        }

if __name__ == "__main__":
    from legacy import common_crawl
    wpc = crawler.WordPressCrawler(url, headers, output_dir)
    common_crawl(wpc)
