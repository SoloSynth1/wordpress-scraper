from legacy.crawler import crawler
import os

url = "https://threatpost.com/"
output_dir = os.path.join('.', 'data', 'threatpost')
headers = {
        'Accept':'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding':'*',
        'Accept-Language':'zh-CN,zh;q=0.8',
        'Cookie': '_ga=GA1.2.908572152.1540264737; __gads=ID=b803df93913bd567:T=1540264741:S=ALNI_MaUpeM35RC42f9YZMJE4x8eKpPo-Q; _gid=GA1.2.1096157912.1540537307; _gat_UA-35676203-21=1; _fbp=fb.1.1540537307445.696691226; _gat_gtag_UA_109681207_2=1',
        'Host': 'threatpost.com',
        'Connection':'keep-alive',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        'X-Requested-With':'XMLHttpRequest'
        }

if __name__ == "__main__":
    from legacy import common_crawl
    wpc = crawler.WordPressCrawler(url, headers, output_dir)
    common_crawl(wpc)
