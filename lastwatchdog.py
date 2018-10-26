from crawler import crawler

url = "https://www.lastwatchdog.com"
output_dir = ".\\data\\lastwatchdog"
headers = {
        'Accept':'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding':'*',
        'Accept-Language':'zh-CN,zh;q=0.8',
        'cookie':'__cfduid=dfea0ee9fe9b8670fdd8222535adb9ec21540527308; __unam=c02b1ec-166acddd608-734d3c03-1',
        'Connection':'keep-alive',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        'X-Requested-With':'XMLHttpRequest'
        }

if __name__ == "__main__":
    wpc = crawler.WordPressCrawler(url, headers)
    wpc.get_tags("{}\\tags.json".format(output_dir))
    wpc.get_categories("{}\\cats.json".format(output_dir))
    wpc.get_posts("{}\\posts.json".format(output_dir))