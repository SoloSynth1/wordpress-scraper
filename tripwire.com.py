from crawler import crawler
import os

url = "https://www.tripwire.com/state-of-security"
output_dir = os.path.join('.', 'data', 'tripwire.com')
headers = {
        'Accept':'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding':'*',
        'Accept-Language':'zh-CN,zh;q=0.8',
        'Cookie': '_ga=GA1.2.119094175.1540799721; _gid=GA1.2.675558396.1540799721; _mkto_trk=id:314-IAH-785&token:_mch-tripwire.com-1540799721524-69889; _omappvp=EUydrVi0KyoqV6kQYYfr9SAWeJ75OsHJzvDtRBCMHHgDmiG0IlZyjDXvOVgLR8Qwg3nVS6y8OKwf27Qlbb6R72A3osyOirxY; Set_Me=949470104.1.1933538064.1457756320; ASP.NET_SessionID=o0mhp3nnm2o2anb25azmuzfx; SnapABugRef=https%3A%2F%2Fwww.tripwire.com%2F%20; SnapABugHistory=1#; SnapABugVisit=1#1540802097; SC_ANALYTICS_GLOBAL_COOKIE=405d761fe5044375a0106c170d9c6a38|True; _ceir=1; _ceg.s=phcqid; _ceg.u=phcqid; __atuvc=2%7C44; __atuvs=5bd6c6351ed52630000; _gat_omTrackerkmdrxrz6bmslide=1',
        'Connection':'keep-alive',
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/70.0.3538.67 Chrome/70.0.3538.67 Safari/537.36',
        'X-Requested-With':'XMLHttpRequest'
        }

if __name__ == "__main__":
    wpc = crawler.WordPressCrawler(url, headers)
    wpc.get_tags(os.path.join('{}'.format(output_dir), 'tags.json'))
    wpc.get_categories(os.path.join('{}'.format(output_dir), 'cats.json'))
    wpc.get_posts(os.path.join('{}'.format(output_dir), 'posts.json'))