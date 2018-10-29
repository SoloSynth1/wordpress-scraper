from crawler import crawler
import os

url = "https://securityledger.com"
output_dir = os.path.join('.', 'data', 'securityledger.com')
headers = {
        'Accept':'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding':'*',
        'Accept-Language':'zh-CN,zh;q=0.8',
        'Cookie': '__cfduid=df69a10a216bf3a67efa57115a197bbda1540799737; __sharethis_cookie_test__=1; __unam=7639673-166bed22de8-519e7a93-1; __qca=P0-1129919385-1540799738659; _ga=GA1.2.963329934.1540799739; _gid=GA1.2.1250730364.1540799739',
        'Connection':'keep-alive',
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/70.0.3538.67 Chrome/70.0.3538.67 Safari/537.36',
        'X-Requested-With':'XMLHttpRequest'
        }

if __name__ == "__main__":
    wpc = crawler.WordPressCrawler(url, headers)
    wpc.get_tags(os.path.join('{}'.format(output_dir), 'tags.json'))
    wpc.get_categories(os.path.join('{}'.format(output_dir), 'cats.json'))
    wpc.get_posts(os.path.join('{}'.format(output_dir), 'posts.json'))