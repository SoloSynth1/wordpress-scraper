from legacy.crawler import crawler
import os

url = "https://securityaffairs.co/wordpress"
output_dir = os.path.join('.', 'data', 'securityaffairs.co-wordpress')

headers = {
        'Accept':'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding':'gzip, deflate, sdch, br',
        'Accept-Language':'zh-CN,zh;q=0.8',
        'Connection':'keep-alive',
        'cookie':'__sharethis_cookie_test__=1; __unam=6f69f6a-166b1935d01-3a484fa3-3',
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36',
        'X-Requested-With':'XMLHttpRequest'
        }

if __name__ == "__main__":
    from legacy import common_crawl
    wpc = crawler.WordPressCrawler(url, headers, output_dir)
    common_crawl(wpc)
