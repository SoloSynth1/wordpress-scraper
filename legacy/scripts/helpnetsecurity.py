from legacy.crawler import crawler
import os

url = "https://www.helpnetsecurity.com"
output_dir = os.path.join('.', 'data', 'helpnetsecurity.com')
headers = {
        'Accept':'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding':'*',
        'Accept-Language':'zh-CN,zh;q=0.8',
        'Cookie': '_ga=GA1.2.910557633.1540266945; _gid=GA1.2.1879377337.1541147383',
        'Host': 'www.helpnetsecurity.com',
        'Connection':'keep-alive',
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/70.0.3538.67 Chrome/70.0.3538.67 Safari/537.36',
        'X-Requested-With':'XMLHttpRequest'
        }

if __name__ == "__main__":
    from legacy import common_crawl
    wpc = crawler.WordPressCrawler(url, headers, output_dir)
    common_crawl(wpc)
