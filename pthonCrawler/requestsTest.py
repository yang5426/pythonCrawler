import requests
import re


# r = requests.get('https://static1.scrape.cuiqingcai.com/')
# print(r.text)

data = {'name': 'wang', 'age': '28'}
r = requests.get('http://httpbin.org/get', params=data)
print(r.json())

r1 = requests.get('https://static1.scrape.cuiqingcai.com/')
pattern = re.compile('<h2.*?>(.*?)</h2>', re.S)
titles = re.findall(pattern, r1.text)
print(titles)

# 二进制文件的爬取
# r2 = requests.get('https://github.com/favicon.ico')
# with open('favicon.ico', 'wb') as f:
#     f.write(r2.content)


headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/52.0.2743.116 Safari/537.36 '
}
r3 = requests.get('https://static1.scrape.cuiqingcai.com/', headers=headers)
# print(r3.text)


# post
data = {'name': 'lisi', 'age': "25"}
r4 = requests.post('http://httpbin.org/post', data=data)
print(r4.text)

# 状态码、响应头、Cookies
r5 = requests.get('https://static1.scrape.cuiqingcai.com/')
print(type(r5.status_code), r5.status_code)
print(type(r5.headers), r5.headers)
print(type(r5.cookies), r5.cookies)
print(type(r5.url), r5.url)
print(type(r5.history), r5.history)
exit() if not r5.status_code == requests.codes.ok else print('Request Successfully')

# 上传文件
files = {'file': open('favicon.ico', 'rb')}
r6 = requests.post('http://httpbin.org/post', files=files)
print(r6.text)

# 获取cookies
print('获取cookies')
r7 = requests.get('http://www.baidu.com')
print(r7.cookies)
for k, v in r7.cookies.items():
    print(k + ' = ' + v)

headers = {
    'Cookies': 'BIDUPSID=9623A74408150E24EE4F01F276EB5B9E; PSTM=1561351472; PANWEB=1; BAIDUID=9910865EB2FE70AC179685E7F62B3C3A:SL=0:NR=10:FG=1; BDUSS=RsdUc0MHBMdGVxbTYxYUVVVVpBUUhrcGRiRnNpb1M0dFdoSmx5czVLUFJ-VVJlRUFBQUFBJCQAAAAAAAAAAAEAAACek75VY2xlYXJsb3Zl0e4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANFwHV7RcB1eUj; MCITY=-%3A; BDUSS_BFESS=RsdUc0MHBMdGVxbTYxYUVVVVpBUUhrcGRiRnNpb1M0dFdoSmx5czVLUFJ-VVJlRUFBQUFBJCQAAAAAAAAAAAEAAACek75VY2xlYXJsb3Zl0e4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANFwHV7RcB1eUj; delPer=0; PSINO=2; BDRCVFR[mkUqnUt8juD]=mk3SLVN4HKm; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BCLID=11476471668160658379; BDSFRCVID=a1tOJexroG3oQSnrEESfhyJy3eKKvV3TDYLE20jjwZdURp-VJeC6EG0Pts1-dEu-EHtdogKK0gOTH6KF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=tR32Wn7a5TrDHJTg5DTjhPrM-HQJWMT-MTryKKOOLxO_ql5H0Pjs2fI-DUoiBb5ptanRhlRNtDJ8j43LbhoCKKuZyxomtfQxtNRJQKDE5p5hKq5S5-OobUPUDMJ9LUkqW2cdot5yBbc8eIna5hjkbfJBQttjQn3hfIkj2CKLK-oj-D-9j60B3e; __xsptplusUT_861=1; _ga=GA1.2.635191149.1598930069; _gid=GA1.2.1741125174.1598930069; _gat_gtag_UA_138572523_1=1; __xsptplus861=861.1.1598930069.1598930069.1%234%7C%7C%7C%7C%7C%23%2303NSFQn-NKSsVDz-QUkjvnvsSpbJvKaV%23; H_PS_PSSID=32645_32606_1454_32693_32533_32046_32677_32117_32691_32583; STOKEN=3ca1ffc12e9bffae9dfaa55ef259d95e932cadd36d63b0ce2d5fcc60f62d57c0; SCRC=13520447a2926d58e749a6561318c72a; Hm_lvt_7a3960b6f067eb0085b7f96ff5e660b0=1598930086; Hm_lpvt_7a3960b6f067eb0085b7f96ff5e660b0=1598930094; PANPSC=11644747187183998937%3ACU2JWesajwChyyrcwBHywus60cmUHWkV2mX9vbaObO%2B6iCFng%2B%2BNns%2FNbbUaC9LQwoXDdbD%2Bmr6%2BWsCeXwhiLlTtHO07XYA0sO6vrVCIuBe4uxZbPN8RdkVqH25aAQJnWDN81yfxsC8tg73W9Mr3XaL5jVfu52v0baC532AuNi2mq8HS1A%2Bd%2BW1xB75uDARpMKjxtxPUcwo%3D',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/52.0.2743.116 Safari/537.36 '
}
url = 'https://pan.baidu.com/disk/home'
# r8 = requests.get(url, headers=headers)
# print(r8.text)

# session
# requests.get('http://httpbin.org/cookies/set/number/123456789')
# r9 = requests.get('http://httpbin.org/cookies')
# print(r9.text)

s10 = requests.Session()
s10.get('http://httpbin.org/cookies/set/number/123456789')
r10 = s10.get('http://httpbin.org/cookies')
print(r10.text)


# ssl证书验证 使用 verify 参数控制是否验证证书，如果将其设置为 False
# from requests.packages import urllib3
# # urllib3.disable_warnings()
import logging
logging.captureWarnings(True)
respose = requests.get('https://static2.scrape.cuiqingcai.com/', verify=False)
print(respose.status_code)

# 指定一个本地证书用作客户端证书
# 我们需要有 crt 和 key 文件，并且指定它们的路径。另外注意，本地私有证书的 key 必须是解密状态，加密状态的 key 是不支持的。
# response = requests.get('https://static2.scrape.cuiqingcai.com/', cert=('/path/server.crt', '/path/server.key'))



# 超时设置 连接（connect）和读取（read） 永久等待，可以直接将 timeout 设置为 None，或者不设置直接留空
r = requests.get('https://httpbin.org/get', timeout=(1, 2))
print(r.status_code)


# 身份认证
from requests.auth import HTTPBasicAuth

# r = requests.get('https://static3.scrape.cuiqingcai.com/', auth=HTTPBasicAuth('admin', 'admin'))
# r = requests.get('https://static3.scrape.cuiqingcai.com/', auth=('admin', 'admin'))
# print(r.status_code)

# OAuth1 认证
# from requests_oauthlib import OAuth1
# url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
# auth = OAuth1('YOUR_APP_KEY', 'YOUR_APP_SECRET',
#               'USER_OAUTH_TOKEN', 'USER_OAUTH_TOKEN_SECRET')
# requests.get(url, auth=auth)




# 代理设置
# 某些网站在测试的时候请求几次，能正常获取内容。但是对于大规模且频繁的请求，网站可能会弹出验证码，或者跳转到登录认证页面，更甚者可能会直接封禁客户端的 IP，导致一定时间段内无法访问。
# proxies = {
#   'http': 'http://10.10.10.10:1080',
#   'https': 'http://10.10.10.10:1080',
# }
# requests.get('https://httpbin.org/get', proxies=proxies)

# 若代理需要使用上文所述的身份认证，可以使用类似 http://user:password@host:port 这样的语法来设置代理，示例如下：
# proxies = {'https': 'http://user:password@10.10.10.10:1080/'}
# requests.get('https://httpbin.org/get', proxies=proxies)


# SOCKS协议代理
# proxies = {
#     'http': 'socks5://user:password@host:port',
#     'https': 'socks5://user:password@host:port'
# }
# requests.get('https://httpbin.org/get', proxies=proxies)



# Prepared Request
from requests import Request, Session
url = 'http://httpbin.org/post'
data = {'name': 'germey'}
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
}
s = Session()
req = Request('POST', url, data=data, headers=headers)
prepped = s.prepare_request(req)
r = s.send(prepped)
print(r.text)