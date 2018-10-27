from crawler import crawler
import os

url = "https://www.lookingglasscyber.com"
output_dir = os.path.join('.', 'data', 'lookingglasscyber')
headers = {
        'Accept':'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding':'*',
        'Accept-Language':'zh-CN,zh;q=0.8',
        'Connection':'keep-alive',
        'Cookie':'__cfduid=d8bd3b5ad23455ce8b26bcbb869ff80c31540451497',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        'X-Requested-With':'XMLHttpRequest'
        }

if __name__ == "__main__":
    if __name__ == "__main__":
        wpc = crawler.WordPressCrawler(url, headers)
        wpc.get_tags(os.path.join('{}'.format(output_dir), 'tags.json'))
        wpc.get_categories(os.path.join('{}'.format(output_dir), 'cats.json'))
        wpc.get_posts(os.path.join('{}'.format(output_dir), 'posts.json'))