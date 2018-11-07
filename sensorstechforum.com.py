from crawler import crawler
import os

url = "https://sensorstechforum.com"
output_dir = os.path.join('.', 'data', 'sensorstechforum.com')
headers = {
        'Accept':'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding':'*',
        'Accept-Language':'zh-CN,zh;q=0.8',
        'Cookie': '__cfduid=d6e8d60c5ed6e3694722eda50a248c54a1541577018; PHPSESSID=824147b5f2c890a2dc93bfbaccf9e157; cookiescriptaccept=visit',
        'Connection':'keep-alive',
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/70.0.3538.67 Chrome/70.0.3538.67 Safari/537.36',
        'X-Requested-With':'XMLHttpRequest'
        }

if __name__ == "__main__":
    wpc = crawler.WordPressCrawler(url, headers, crawl_rate=100)
    wpc.get_tags(os.path.join('{}'.format(output_dir), 'tags.json'))
    wpc.get_categories(os.path.join('{}'.format(output_dir), 'cats.json'))
    wpc.get_posts(os.path.join('{}'.format(output_dir), 'posts.json'))