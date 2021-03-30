from legacy.crawler import crawler
import os

url = "https://www.comparitech.com"
output_dir = os.path.join('.', 'data', 'www.comparitech.com')
headers = {
        'Accept':'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding':'*',
        'Accept-Language':'zh-CN,zh;q=0.8',
        'Cookie': '_conv_r=s:heimdalsecurity.com*m:referral*t:*c:; _ga=GA1.2.235624317.1541147443; PHPSESSID=4865b95b6bd5a85c6e071c1e2f47497f; _gid=GA1.2.595733218.1541383875; _conv_v=vi:1*sc:4*cs:1541383837*fs:1541147440*pv:5*exp:{}*ps:1541221464; _conv_s=si:4*sh:1541383837127-0.002642356216356223*pv:2; _ceg.s=php9gm; _ceg.u=php9gm',
        'Connection':'keep-alive',
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/70.0.3538.67 Chrome/70.0.3538.67 Safari/537.36',
        'X-Requested-With':'XMLHttpRequest'
        }

if __name__ == "__main__":
    from legacy import common_crawl
    wpc = crawler.WordPressCrawler(url, headers, output_dir)
    common_crawl(wpc)
