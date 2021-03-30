from legacy.crawler import crawler
import os

url = "https://blog.sucuri.net"
output_dir = os.path.join('.', 'data', 'blog.sucuri.net')
headers = {
        'Accept':'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding':'*',
        'Accept-Language':'zh-CN,zh;q=0.8',
        'Cookie': '_ga=GA1.2.1452495584.1541147436; IR_gbd=sucuri.net; _gid=GA1.2.959211258.1541383890; IR_3713=1541559256293%7C0%7C1541559256293; IR_PI=3df49081-c233-9d54-c728-932176615ccd%7C1541645656293',
        'Connection':'keep-alive',
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/70.0.3538.67 Chrome/70.0.3538.67 Safari/537.36',
        'X-Requested-With':'XMLHttpRequest'
        }

if __name__ == "__main__":
    from legacy import common_crawl
    wpc = crawler.WordPressCrawler(url, headers, output_dir, crawl_rate=100)
    common_crawl(wpc)
