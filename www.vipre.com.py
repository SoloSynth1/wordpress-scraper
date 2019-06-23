from crawler import crawler
import os

url = "https://www.vipre.com"
output_dir = os.path.join('.', 'data', 'www.vipre.com')
headers = {
        'Accept':'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding':'*',
        'Accept-Language':'zh-CN,zh;q=0.8',
        'Cookie': '_ga=GA1.2.1644535100.1541147443; __adroll_fpc=3a119bf44db7ee75d21bdc4bd8006d25; __idcontext=eyJjb29raWVJRCI6IjZFM0I3VUNSNDVOWVZHT1o3WTJGSDZOT1dXRUtFMkM0TlhKNUdBVDdIVkdRPT09PSIsImRldmljZUlEIjoiNkUzQjdVQ1I0QjNKRlg2WFZZSVdMNjcyU1M0SllNU0dKTEc1T0FDR0c0RUE9PT09IiwiaXYiOiI1SVdKNlpMUlBKN0lNNlcyVkpWMjZQRzJKST09PT09PSIsInYiOjF9; _gid=GA1.2.1952222110.1541383857; _gcl_au=1.1.535369970.1541532633; __ar_v4=R5EX2LAD7FAOVD6PWNPH6O%3A20181102%3A10%7CN7AGIAEPRZDM5FMAGV2QUY%3A20181102%3A10%7C53FLNYE57ZE4ZDAHOYANNY%3A20181102%3A10',
        'Host': 'www.vipre.com',
        'Connection':'keep-alive',
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/70.0.3538.67 Chrome/70.0.3538.67 Safari/537.36',
        'X-Requested-With':'XMLHttpRequest'
        }

if __name__ == "__main__":
    wpc = crawler.WordPressCrawler(url, headers, crawl_rate=100)
    wpc.get_tags(os.path.join('{}'.format(output_dir), 'tags.json'))
    wpc.get_categories(os.path.join('{}'.format(output_dir), 'cats.json'))
    wpc.get_posts(os.path.join('{}'.format(output_dir), 'posts.json'))