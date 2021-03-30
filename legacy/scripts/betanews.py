from legacy.crawler import crawler
import os

url = "https://betanews.com"
output_dir = os.path.join('.', 'data', 'betanews.com')
headers = {
        'Accept':'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding':'*',
        'Accept-Language':'zh-CN,zh;q=0.8',
        'Cookie': '_ga=GA1.2.529771702.1541147410; __gads=ID=cddffd965b59ec5f:T=1541147412:S=ALNI_MYQm3Vphovvte59_MWZctfuIFxpmg; zdbb_swap_krux_id=1; _gid=GA1.2.1535543751.1541383876; geoCC=HK',
        'Host': 'betanews.com',
        'Connection':'keep-alive',
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/70.0.3538.67 Chrome/70.0.3538.67 Safari/537.36',
        'X-Requested-With':'XMLHttpRequest'
        }

if __name__ == "__main__":
    from legacy import common_crawl
    wpc = crawler.WordPressCrawler(url, headers, output_dir, crawl_rate=100)
    common_crawl(wpc)
