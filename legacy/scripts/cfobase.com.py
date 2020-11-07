from legacy.crawler import crawler
import os

url = "https://cfobase.com/"
output_dir = os.path.join('../..', 'data', 'cfobase.com')
headers = {
        'Accept':'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding':'*',
        'Accept-Language':'zh-CN,zh;q=0.8',
        'Host': 'cfobase.com',
        'Connection':'keep-alive',
        'Cookie': '_mkto_trk=id:497-ITQ-712&token:_mch-bromium.com-1545360431008-12984; _biz_sid=919162; _ga=GA1.2.1945164141.1545360432; _gid=GA1.2.949409536.1545360432; _biz_uid=a18ee78fd1664b1ecb82da38af7ca704; _biz_flagsA=%7B%22Version%22%3A1%2C%22Mkto%22%3A%221%22%2C%22XDomain%22%3A%221%22%7D; _biz_nA=4; _biz_pendingA=%5B%5D',
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36',
        'X-Requested-With':'XMLHttpRequest'
        }

if __name__ == "__main__":
    wpc = crawler.WordPressCrawler(url, headers)
    wpc.get_tags(os.path.join('{}'.format(output_dir), 'tags.json'))
    wpc.get_categories(os.path.join('{}'.format(output_dir), 'cats.json'))
    wpc.get_posts(os.path.join('{}'.format(output_dir), 'posts.json'))