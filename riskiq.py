from crawler import crawler

url = "https://www.riskiq.com"
output_dir = ".\\data\\riskiq"

headers = {
        'Accept':'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding':'gzip, deflate, sdch, br',
        'Accept-Language':'zh-CN,zh;q=0.8',
        'Connection':'keep-alive',
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36',
        'X-Requested-With':'XMLHttpRequest'
        }

if __name__ == "__main__":
    wpc = crawler.WordPressCrawler(url, headers)
    wpc.get_tags("{}\\tags.json".format(output_dir))
    wpc.get_categories("{}\\cats.json".format(output_dir))
    wpc.get_posts("{}\\posts.json".format(output_dir))