from legacy.crawler import crawler
import os

url = "https://securelist.com"
output_dir = os.path.join('.', 'data', 'securelist.com')
headers = {
        'Accept':'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding':'*',
        'Accept-Language':'zh-CN,zh;q=0.8',
        'Cookie': '_ga=GA1.2.1769368666.1545970795; _hjIncludedInSample=1; _gid=GA1.2.240454939.1546227015; _fbp=fb.1.1546227015921.374506551; PHPSESSID=a856739d604f1496cd355f2dc35f3371',
        'Connection':'keep-alive',
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/70.0.3538.67 Chrome/70.0.3538.67 Safari/537.36',
        'X-Requested-With':'XMLHttpRequest'
        }

if __name__ == "__main__":
    from legacy import common_crawl
    wpc = crawler.WordPressCrawler(url, headers, output_dir, crawl_rate=100)
    common_crawl(wpc)
