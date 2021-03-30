from legacy.crawler import crawler
import os

url = "https://www.tripwire.com/state-of-security"
output_dir = os.path.join('.', 'data', 'tripwire.com')
headers = {
        'Accept':'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding':'*',
        'Accept-Language':'zh-CN,zh;q=0.8',
        'Cookie': 'ASP.NET_SessionID=rno4pepppbkdh2f1bn5nc2kj; SC_ANALYTICS_GLOBAL_COOKIE=f9c357b4f7124f7890bd980c59b97db4|False; active=yes; Set_Me=3415655320.1.1933537720.2330721216; SnapABugRef=https%3A%2F%2Fwww.tripwire.com%2F%20; SnapABugHistory=1#; SnapABugVisit=1#1541675065',
        'Connection':'keep-alive',
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/70.0.3538.67 Chrome/70.0.3538.67 Safari/537.36',
        'X-Requested-With':'XMLHttpRequest'
        }

if __name__ == "__main__":
    from legacy import common_crawl
    wpc = crawler.WordPressCrawler(url, headers, output_dir, crawl_rate=25)
    common_crawl(wpc)
