# import requests
#
# proxy = '121.232.148.67:9000'
# proxies = {
#     'http': 'http://' + proxy,
#     'https': 'https://' + proxy,
# }
# try:
#     response = requests.get('https://httpbin.org/get', proxies=proxies)
#     print(response.text)
# except requests.exceptions.ConnectionError as e:
#     print('Error', e.args)

# from selenium import webdriver
# proxy = '121.232.148.67:9000'
# options = webdriver.ChromeOptions()
# options.add_argument('--proxy-server=http://' + proxy)
# browser = webdriver.Chrome(options=options)
# browser.get('https://httpbin.org/get')
# print(browser.page_source)
# browser.close()


import requests

PROXY_POOL_URL = 'http://localhost:5555/random'


# def get_proxy():
#     try:
#         response = requests.get(PROXY_POOL_URL)
#         if response.status_code == 200:
#             return response.text
#     except ConnectionError:
#         return None
# #
# # print(get_proxy())
#
# import requests
#
# proxy = get_proxy()
# print(proxy)

proxy = '85.14.5.57:80'

proxies = {
    'http': 'http://' + proxy,
    'https': 'https://' + proxy,
}
try:
    response = requests.get('http://httpbin.org/get', proxies=proxies)
    print(response.text)
except requests.exceptions.ConnectionError as e:
    print('Error', e.args)

