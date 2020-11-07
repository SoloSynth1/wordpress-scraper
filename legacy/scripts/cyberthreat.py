from legacy.crawler import crawler

url = "http://cyberthreat.blog"
output_dir = ".\\data\\cyberthreat"
headers = {
        'Accept':'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding':'*',
        'Accept-Language':'zh-CN,zh;q=0.8',
        'Connection':'keep-alive',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        'X-Requested-With':'XMLHttpRequest'
        }

if __name__ == "__main__":
    wpc = crawler.WordPressCrawler(url, headers)
    wpc.get_tags("{}\\tags.json".format(output_dir))
    wpc.get_categories("{}\\cats.json".format(output_dir))
    wpc.get_posts("{}\\posts.json".format(output_dir))