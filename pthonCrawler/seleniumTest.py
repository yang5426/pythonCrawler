from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
# browser = webdriver.Chrome()
import time

# try:
#     browser.get('https://www.baidu.com')
#     input = browser.find_element_by_id('kw')
#     input.send_keys('Python')
#     input.send_keys(Keys.ENTER)
#     wait = WebDriverWait(browser, 10)
#     wait.until(EC.presence_of_element_located((By.ID, 'content_left')))
#     print(browser.current_url)
#     print(browser.get_cookies())
#     print(browser.page_source)
# finally:
#     browser.close()

# browser.get('https://www.taobao.com')
# print(browser.page_source)
# find_element_by_id 
# find_element_by_name 
# find_element_by_xpath 
# find_element_by_link_text 
# find_element_by_partial_link_text 
# find_element_by_tag_name 
# find_element_by_class_name 
# find_element_by_css_selector
# input_first = browser.find_element_by_id('q')
# input_second = browser.find_element_by_css_selector('#q')
# input_third = browser.find_element_by_xpath('//*[@id="q"]')
# print(input_first, input_second, input_third)
#
# input_first = browser.find_element(By.ID, 'q')
# print(input_first)


# 多个节点
# lis = browser.find_elements_by_css_selector('.service-bd li')
# print(lis)
# lis = browser.find_elements(By.CSS_SELECTOR, '.service-bd li')
# print(lis)


# 节点交互
# input = browser.find_element_by_id('q')
# input.send_keys('iPhone')
# time.sleep(1)
# input.clear()
# input.send_keys('iPad')
# button = browser.find_element_by_class_name('btn-search')
# button.click()
#
# time.sleep(5)


# 还有另外一些操作，它们没有特定的执行对象，比如鼠标拖拽、键盘按键等，这些动作用另一种方式来执行，那就是动作链。


# from selenium.webdriver import ActionChains
# url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
# browser.get(url)
# browser.switch_to_frame('iframeResult')
# source = browser.find_element_by_css_selector('#draggable')
# target = browser.find_element_by_css_selector('#droppable')
# actions = ActionChains(browser)
# actions.drag_and_drop(source, target)
# actions.perform()


# 执行 JavaScript
# browser.get('https://www.zhihu.com/explore')
# browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
# browser.execute_script('alert("To Bottom")')


# 获取节点信息
# url = 'https://dynamic2.scrape.cuiqingcai.com/'
# browser.get(url)
# logo = browser.find_element_by_class_name('logo-image')
# print(logo)
# print(logo.get_attribute('src'))

# 获取文本值
# input = browser.find_element_by_class_name('logo-title')
# print(input.text)

# 获取 ID、位置、标签名、大小
# print(input.id)
# print(input.location)
# print(input.tag_name)
# print(input.size)
# browser.close()
# 切换 Frame
# from selenium.common.exceptions import NoSuchElementException
# browser = webdriver.Chrome()
# url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
# browser.get(url)
# browser.switch_to.frame('iframeResult')
# try:
#     logo = browser.find_element_by_class_name('logo')
# except NoSuchElementException:
#     print('NO LOGO')
# browser.switch_to.parent_frame()
# logo = browser.find_element_by_class_name('logo')
# print(logo)
# print(logo.text)
#
# browser.close()

# 延时等待
# 隐式等待 如果 Selenium 没有在 DOM 中找到节点，将继续等待，超出设定时间后，则抛出找不到节点的异常。
# 换句话说，隐式等待可以在我们查找节点而节点并没有立即出现的时候，等待一段时间再查找 DOM，默认的时间是 0
# browser = webdriver.Chrome()
# browser.implicitly_wait(10)
# browser.get('https://dynamic2.scrape.cuiqingcai.com/')
# input = browser.find_element_by_class_name('logo-image')
# print(input)
# browser.close()

# 这里还有一种更合适的显式等待方法，它指定要查找的节点，然后指定一个最长等待时间。
# 如果在规定时间内加载出来了这个节点，就返回查找的节点；如果到了规定时间依然没有加载出该节点，则抛出超时异常
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# browser = webdriver.Chrome()
# browser.get('https://www.taobao.com/')
# wait = WebDriverWait(browser, 10)
# input = wait.until(EC.presence_of_element_located((By.ID, 'q')))
# button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-search')))
# print(input, button)


# 前进后退
# import time
# from selenium import webdriver
# browser = webdriver.Chrome()
# browser.get('https://www.baidu.com/')
# browser.get('https://www.taobao.com/')
# # browser.get('https://www.python.org/')
# browser.back()
# time.sleep(1)
# browser.forward()
# browser.close()

# Cookies
# 对 Cookies 进行操作，例如获取、添加、删除 Cookies 等
# from selenium import webdriver
# browser = webdriver.Chrome()
# browser.get('https://www.zhihu.com/explore')
# print(browser.get_cookies())
# browser.add_cookie({'name': 'name', 'domain': 'www.zhihu.com', 'value': 'germey'})
# print(browser.get_cookies())
# browser.delete_all_cookies()
# print(browser.get_cookies())

# 选项卡管理
# import time
# from selenium import webdriver
# browser = webdriver.Chrome()
# browser.get('https://www.baidu.com')
# browser.execute_script('window.open()')
# print(browser.window_handles)
# browser.switch_to.window(browser.window_handles[1])
# browser.get('https://www.taobao.com')
# time.sleep(1)
# browser.switch_to.window(browser.window_handles[0])
# browser.get('https://python.org')

# 异常处理
from selenium import webdriver
from selenium.common.exceptions import TimeoutException,NoSuchElementException
# browser = webdriver.Chrome()
# try:
#     browser.get('https://www.baidu.com')
# except TimeoutException:
#     print('Time out')
# try:
#     browser.find_element_by_id('hello')
# except NoSuchElementException:
#     print('No Element')
# finally:
#     browser.close()


# 反屏蔽
# 使用 CDP（即 Chrome Devtools-Protocol，Chrome 开发工具协议）来解决这个问题
# from selenium import webdriver
# from selenium.webdriver import ChromeOptions
# option = ChromeOptions()
# option.add_experimental_option('excludeSwitches', ['enable-automation'])
# option.add_experimental_option('useAutomationExtension', False)
# browser = webdriver.Chrome(options=option)
# browser.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {'source': 'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'})
# browser.get('https://antispider1.scrape.cuiqingcai.com/')


# 无头模式
from selenium import webdriver
from selenium.webdriver import ChromeOptions
option = ChromeOptions()
option.add_argument('--headless')
browser = webdriver.Chrome(options=option)
browser.set_window_size(1366, 768)
browser.get('https://www.baidu.com')
browser.get_screenshot_as_file('preview.png')