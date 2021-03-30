from legacy.crawler import crawler
import os

url = "https://www.scmagazine.com"
output_dir = os.path.join('.', 'data', 'www.scmagazine.com')

headers = {
        'Accept':'application/json, text/javascript, */*; q=0.01',
        'Accept-Language':'zh-CN,zh;q=0.8',
        'Connection':'keep-alive',
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36',
        'X-Requested-With':'XMLHttpRequest'
        }

if __name__ == "__main__":
    from legacy import common_crawl
    wpc = crawler.WordPressCrawler(url, headers, output_dir)
    common_crawl(wpc)
