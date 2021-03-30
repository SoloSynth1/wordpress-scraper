from legacy.crawler import crawler
import os

url = "https://www.social-engineer.org"
output_dir = os.path.join('.', 'data', 'social-engineer.org')
headers = {
        'Accept':'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding':'*',
        'Accept-Language':'zh-CN,zh;q=0.8',
        'Cookie': 'PHPSESSID=66j0js30oq2j43o59fa278pti1; wordpress_test_cookie=WP+Cookie+check; __unam=fea26eb-166bed13d3b-2f1cc5de-1; _ga=GA1.2.1491302686.1540799678; _gid=GA1.2.157321464.1540799678',
        'Host': 'www.social-engineer.org',
        'Connection':'keep-alive',
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/70.0.3538.67 Chrome/70.0.3538.67 Safari/537.36',
        'X-Requested-With':'XMLHttpRequest'
        }

if __name__ == "__main__":
    from legacy import common_crawl
    wpc = crawler.WordPressCrawler(url, headers, output_dir)
    common_crawl(wpc)
