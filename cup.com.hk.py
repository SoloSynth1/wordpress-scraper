from crawler import crawler
import os

url = "https://www.cup.com.hk"
output_dir = os.path.join('.', 'data', 'cup.com.hk')
headers = {
        'Accept':'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding':'*',
        'Accept-Language':'zh-CN,zh;q=0.8',
        'Cookie': '__cfduid=d0c4282dcdb115dbcd08edfba7e0e8e721560849079',
        'Connection':'keep-alive',
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/70.0.3538.67 Chrome/70.0.3538.67 Safari/537.36',
        'X-Requested-With':'XMLHttpRequest'
        }

if __name__ == "__main__":
    wpc = crawler.WordPressCrawler(url, headers, crawl_rate=100)
    wpc.get_tags(os.path.join('{}'.format(output_dir), 'tags.json'))
    wpc.get_categories(os.path.join('{}'.format(output_dir), 'cats.json'))
    wpc.get_posts(os.path.join('{}'.format(output_dir), 'posts.json'))