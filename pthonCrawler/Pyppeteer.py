import asyncio
from pyppeteer import launch
from pyquery import PyQuery as pq

url = 'https://dynamic2.scrape.cuiqingcai.com/'

width, height = 1366, 768


# evaluate 方法执行了 JavaScript，并获取到了对应的结果。另外其还有 exposeFunction、evaluateOnNewDocument、evaluateHandle 方法可以做了解。


# async def main():
#     browser = await launch()
#     page = await browser.newPage()
#     await page.setViewport({'width': width, 'height': height})
#     await page.goto(url)
#     await page.waitForSelector('.item .name')
#     await asyncio.sleep(2)
#     await page.screenshot(path='example.png')
#
#     # doc = pq(await page.content())
#     # names = [item.text() for item in doc('.item .name').items()]
#     # print('Names:', names)
#
#     dimensions = await page.evaluate('''() => {
#         return {
#             width: document.documentElement.clientWidth,
#             height: document.documentElement.clientHeight,
#             deviceScaleFactor: window.devicePixelRatio,
#         }
#     }''')
#     print(dimensions)
#     await browser.close()



# async def main():
#     await launch(headless=False)
#     await asyncio.sleep(100)

# async def main():
#     browser = await launch(headless=False, userDataDir='./userdata', args=['--disable-infobars', f'--window-size={width},{height}'])
#     page = await browser.newPage()
#     await page.setViewport({'width': width, 'height': height})
#     await page.evaluateOnNewDocument('Object.defineProperty(navigator, "webdriver", {get: () => undefined})')
#     await page.goto('https://www.taobao.com')
#     await asyncio.sleep(100)



# import asyncio
# from pyppeteer import launch
# from pyquery import PyQuery as pq
#  
# async def main():
#    browser = await launch()
#    page = await browser.newPage()
#    await page.goto('https://dynamic2.scrape.cuiqingcai.com/')
#    await page.waitForSelector('.item .name')
#    j_result1 = await page.J('.item .name')
#    j_result2 = await page.querySelector('.item .name')
#    jj_result1 = await page.JJ('.item .name')
#    jj_result2 = await page.querySelectorAll('.item .name')
#    print('J Result1:', j_result1)
#    print('J Result2:', j_result2)
#    print('JJ Result1:', jj_result1)
#    print('JJ Result2:', jj_result2)
#    await browser.close()
#  
# asyncio.get_event_loop().run_until_complete(main())


# async def main():
#     browser = await launch(headless=False)
#     page = await browser.newPage()
#     await page.goto('https://www.baidu.com')
#     page = await browser.newPage()
#     await page.goto('https://www.bing.com')
#     pages = await browser.pages()
#     print('Pages:', pages)
#     page1 = pages[1]
#     await page1.bringToFront()
#     await asyncio.sleep(100)
#
#
# asyncio.get_event_loop().run_until_complete(main())


import asyncio
from pyppeteer import launch
from pyquery import PyQuery as pq

# async def main():
#     browser = await launch(headless=True)
#     page = await browser.newPage()
#     await page.goto('https://dynamic1.scrape.cuiqingcai.com/')
#     await page.goto('https://dynamic2.scrape.cuiqingcai.com/')
#     # 后退
#     await page.goBack()
#     # 前进
#     await page.goForward()
#     # 刷新
#     await page.reload()
#     # 保存 PDF
#     await page.pdf()  # 无头模式才可以使用
#     # 截图
#     await page.screenshot()
#     # 设置页面 HTML
#     await page.setContent('<h2>Hello World</h2>')
#     # 设置 User-Agent
#     await page.setUserAgent('Python')
#     # 设置 Headers
#     await page.setExtraHTTPHeaders(headers={})
#     # 关闭
#     await page.close()
#     await browser.close()
#
#
# asyncio.get_event_loop().run_until_complete(main())



# 点击
# import asyncio
# from pyppeteer import launch
# from pyquery import PyQuery as pq
#
#
# async def main():
#     browser = await launch(headless=False)
#     page = await browser.newPage()
#     await page.goto('https://dynamic2.scrape.cuiqingcai.com/')
#     await page.waitForSelector('.item .name')
#     await page.click('.item .name', options={
#         'button': 'right',
#         'clickCount': 1,  # 1 or 2
#         'delay': 3000,  # 毫秒
#     })
#     await browser.close()
#
#
# asyncio.get_event_loop().run_until_complete(main())

# import asyncio
# from pyppeteer import launch
# from pyquery import PyQuery as pq
#
#
# async def main():
#     browser = await launch(headless=False)
#     page = await browser.newPage()
#     await page.goto('https://www.taobao.com')
#     # 后退
#     await page.type('#q', 'iPad')
#     # 关闭
#     await asyncio.sleep(10)
#     await browser.close()
#
#
# asyncio.get_event_loop().run_until_complete(main())


# 获取信息
import asyncio
from pyppeteer import launch
from pyquery import PyQuery as pq


async def main():
    browser = await launch(headless=False)
    page = await browser.newPage()
    await page.goto('https://dynamic2.scrape.cuiqingcai.com/')
    print('HTML:', await page.content())
    print('Cookies:', await page.cookies())
    await browser.close()


asyncio.get_event_loop().run_until_complete(main())



# 延时等待
# 除了 waitForSelector 方法，还有很多其他的等待方法，介绍如下。
# waitForFunction：等待某个 JavaScript 方法执行完毕或返回结果。
# waitForNavigation：等待页面跳转，如果没加载出来就会报错。
# waitForRequest：等待某个特定的请求被发出。
# waitForResponse：等待某个特定的请求收到了回应。
# waitFor：通用的等待方法。
# waitForSelector：等待符合选择器的节点加载出来。
# waitForXPath：等待符合 XPath 的节点加载出来。

