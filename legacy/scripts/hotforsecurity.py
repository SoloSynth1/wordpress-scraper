from legacy.crawler import crawler
import os

url = "https://hotforsecurity.bitdefender.com"
output_dir = os.path.join('.', 'data', 'hotforsecurity.bitdefender.com')
headers = {
        'Accept':'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding':'*',
        'Accept-Language':'zh-CN,zh;q=0.8',
        'Cookie': '__cfduid=d168be0b4533032d20c2aa278ecb62fe31541147413; check=true; _ga=GA1.2.130067401.1541147420; _gid=GA1.2.1176639717.1541147420; bd112=Xc5BCsIwEAXQu2ThShICEbES3Lj1BEYkbadNoE3CZGoV8e622enqD58H869vNuHAKuaIUmWEEfM889pTCx2EFpA3cTQiewIjLtYHI3oIgHY4%2B97TEpbsKWkjNnZMR9KrvLs4QrI9lK4dNIRyOe0iqQwNx%2FrJ48P9PApAReVVdREXN6Gn1%2F%2BaggBRsy0jP0KmpWCV3Ckp1V7Jw%2Bf2BQ%3D%3D; AMCVS_0E920C0F53DA9E9B0A490D45%40AdobeOrg=1; AMCV_0E920C0F53DA9E9B0A490D45%40AdobeOrg=2035320058%7CMCIDTS%7C17838%7CMCMID%7C26407325438182498473478927876586191970%7CMCAAMLH-1541752221%7C11%7CMCAAMB-1541752221%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1541154621s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C3.3.0; mbox=session#8b43bd7f0847437182a44000418828d2#1541149284|PC#8b43bd7f0847437182a44000418828d2.22_35#1604392224; s_cc=true; aam_uuid=26426712967223226083480932539320192677; s_ht=1541147427592; s_hc=1%7C0%7C0%7C0%7C0; s_ppvl=h4s%253Ahome%2C29%2C29%2C1009%2C1920%2C1009%2C1920%2C1080%2C1%2CP; s_ppn=h4s%3Ahome; s_ppv=h4s%253Ahome%2C84%2C29%2C2946%2C1920%2C1009%2C1920%2C1080%2C1%2CP',
        'Connection':'keep-alive',
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/70.0.3538.67 Chrome/70.0.3538.67 Safari/537.36',
        'X-Requested-With':'XMLHttpRequest'
        }

if __name__ == "__main__":
    from legacy import common_crawl
    wpc = crawler.WordPressCrawler(url, headers, output_dir)
    common_crawl(wpc)
