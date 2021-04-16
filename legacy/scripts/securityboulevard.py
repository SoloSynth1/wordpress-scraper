from legacy.crawler import improved_crawler
import os

url = "https://securityboulevard.com"
output_dir = os.path.join('.', 'data', 'securityboulevard.com')
headers = {
    'Accept':'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding':'*',
    'Accept-Language':'en-US,en;q=0.9,zh-CN,zh;q=0.8',
    'Cache-control': 'max-age=0',
    'Cookie': 'timer=3; lastvisit=1618499885',
    'Dnt': '1',
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
}

if __name__ == "__main__":
    from legacy import common_crawl
    wpc = improved_crawler.MultiThreadedCrawler(url, headers, output_dir, crawl_rate=1, retry_standoff=60, max_retries=20)
    common_crawl(wpc)
