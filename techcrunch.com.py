from crawler import crawler
import os

url = "https://techcrunch.com"
output_dir = os.path.join('.', 'data', 'techcrunch.com')
headers = {
        'Accept':'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding':'*',
        'Accept-Language':'zh-CN,zh;q=0.8',
        'Cookie': 'GUCS=AZbgFVVR; BX=dh9q691dto2nb&b=3&s=pa; GUC=AQEBAQFb3VFcqEIeDwRg&s=AQAAAHrL6bS1&g=W9wK9Q; rxx=1igbwm2xq2h.1b7gr4g0&v=1; __pcvc={}; _parsely_session={%22sid%22:1%2C%22surl%22:%22https://techcrunch.com/tag/security/%22%2C%22sref%22:%22https://heimdalsecurity.com/blog/best-internet-security-blogs/%22%2C%22sts%22:1541147372572%2C%22slts%22:0}; _ga=GA1.2.1478942211.1541147373; _gid=GA1.2.641246751.1541147373; _fbp=fb.1.1541147372697.1423203867; _parsely_visitor={%22id%22:%22pid=ec7dcbdb884243adc40612940d2620db%22%2C%22session_count%22:1%2C%22last_session_ts%22:1541147372572}; __tbc=%7Bjzx%7DjGAToaZMxJYLoS7N4KRjDSIBQx5XEUgUJ2gvwnLO_mQfpRr8AZeO09jGk7-hTUyQLRad9Q5Lm3MJbSMChjRhiKNoGVtYYENGn5Vzh_MxqnGS8ho0EJnccNxVf1vgcsspOzaeIILFhlSTw5lulLLvTw; __pat=-14400000; __pvi=%7B%22id%22%3A%22v-2018-11-02-16-29-33-940-6TjxfdUCVZ3f1YuQ-2f3e0384dd8f3212b5d9c2020699090e%22%2C%22domain%22%3A%22.techcrunch.com%22%2C%22time%22%3A1541147374314%7D; xbc=%7Bjzx%7D_e5BhmMRjtsjUjGbrtX0c7h7R3xM4VwABoRuGqnXs1Ch_5rnoQguNFJyyQn8ud-iL8IqeSU80X8vYQUgLUhfHjuT7rlXqV_haFtcBrb8yuIRISMjwJMKlsrJHHm5uxsQSNVe4coFP2tX0siiAgGZ0F02N2xHWSErhk02CjXpVfgMydpMnNyxptMGZ-xXMB5A; __adblocker=false',
        'Connection':'keep-alive',
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/70.0.3538.67 Chrome/70.0.3538.67 Safari/537.36',
        'X-Requested-With':'XMLHttpRequest'
        }

if __name__ == "__main__":
    wpc = crawler.WordPressCrawler(url, headers)
    wpc.get_tags(os.path.join('{}'.format(output_dir), 'tags.json'))
    wpc.get_categories(os.path.join('{}'.format(output_dir), 'cats.json'))
    wpc.get_posts(os.path.join('{}'.format(output_dir), 'posts.json'))