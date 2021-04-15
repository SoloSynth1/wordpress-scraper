from legacy.crawler import crawler
import os

url = "https://securityboulevard.com"
output_dir = os.path.join('.', 'data', 'securityboulevard.com')
headers = {
        'Accept':'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding':'*',
        'Accept-Language':'zh-CN,zh;q=0.8',
        'Cookie': '_ga=GA1.2.1760483183.1541147404; _gid=GA1.2.41433513.1541147405; __gads=ID=3a20452a115478a6:T=1541147404:S=ALNI_MaHaXvYr-7YP-IKnSWpWY3gtGaYzg; __auc=e6a83ec6166d38b319d60ec7ce4; __hstc=90482629.5a8f2b35b9b387e938400552b20b5008.1541147409765.1541147409765.1541147409765.1; __hssrc=1; hubspotutk=5a8f2b35b9b387e938400552b20b5008',
        'Connection':'keep-alive',
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/70.0.3538.67 Chrome/70.0.3538.67 Safari/537.36',
        'X-Requested-With':'XMLHttpRequest'
        }

if __name__ == "__main__":
    from legacy import common_crawl
    wpc = crawler.WordPressCrawler(url, headers, output_dir, crawl_rate=5)
    common_crawl(wpc)
