import requests
import logging
import time
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

TOTAL_NUMBER = 100
BASE_URL = 'https://static4.scrape.cuiqingcai.com/detail/{id}'
# start_time = time.time()
# for id in range(1, TOTAL_NUMBER + 1):
#     url = BASE_URL.format(id=id)
#     logging.info('scraping %s', url)
#     respose = requests.get(url)
# end_time = time.time()
# logging.info('total time %s seconds', end_time - start_time)


# 阻塞和非阻塞、同步和异步、多进程和协程。

# 阻塞状态指程序未得到所需计算资源时被挂起的状态。程序在等待某个操作完成期间，自身无法继续处理其他的事情，则称该程序在该操作上是阻塞的。
# 常见的阻塞形式有：网络 I/O 阻塞、磁盘 I/O 阻塞、用户输入阻塞等。阻塞是无处不在的，包括 CPU 切换上下文时，所有的进程都无法真正处理事情，它们也会被阻塞。如果是多核 CPU 则正在执行上下文切换操作的核不可被利用。

# 非阻塞  程序在等待某操作过程中，自身不被阻塞，可以继续处理其他的事情，则称该程序在该操作上是非阻塞的。
# 非阻塞并不是在任何程序级别、任何情况下都可以存在的。仅当程序封装的级别可以囊括独立的子程序单元时，它才可能存在非阻塞状态。
# 非阻塞的存在是因为阻塞存在，正因为某个操作阻塞导致的耗时与效率低下，我们才要把它变成非阻塞的。

# 同步 不同程序单元为了完成某个任务，在执行过程中需靠某种通信方式以协调一致，我们称这些程序单元是同步执行的。
# 例如购物系统中更新商品库存，需要用“行锁”作为通信信号，让不同的更新请求强制排队顺序执行，那更新库存的操作是同步的。
# 简言之，同步意味着有序。

# 异步 为完成某个任务，不同程序单元之间过程中无需通信协调，也能完成任务的方式，不相关的程序单元之间可以是异步的。
# 例如，爬虫下载网页。调度程序调用下载程序后，即可调度其他任务，而无需与该下载任务保持通信以协调行为。不同网页的下载、保存等操作都是无关的，也无需相互通知协调。这些异步操作的完成时刻并不确定。
# 简言之，异步意味着无序

# 多进程
# 多进程就是利用 CPU 的多核优势，在同一时间并行地执行多个任务，可以大大提高执行效率。

# 协程 协程，英文叫作 Coroutine，又称微线程、纤程，协程是一种用户态的轻量级线程。
# 协程拥有自己的寄存器上下文和栈。协程调度切换时，将寄存器上下文和栈保存到其他地方，在切回来的时候，恢复先前保存的寄存器上下文和栈。
# 因此协程能保留上一次调用时的状态，即所有局部状态的一个特定组合，每次过程重入时，就相当于进入上一次调用的状态。
# 协程本质上是个单进程，协程相对于多进程来说，无需线程上下文切换的开销，无需原子操作锁定及同步的开销，编程模型也非常简单。



# 我们可以使用协程来实现异步操作，比如在网络爬虫场景下，我们发出一个请求之后，需要等待一定的时间才能得到响应，但其实在这个等待过程中，
# 程序可以干许多其他的事情，等到响应得到之后才切换回来继续处理，这样可以充分利用 CPU 和其他资源，这就是协程的优势。
# Python 中使用协程最常用的库莫过于 asyncio，所以本文会以 asyncio 为基础来介绍协程的使用。
#
# 首先我们需要了解下面几个概念。
#
# event_loop：事件循环，相当于一个无限循环，我们可以把一些函数注册到这个事件循环上，当满足条件发生的时候，就会调用对应的处理方法。
# coroutine：中文翻译叫协程，在 Python 中常指代为协程对象类型，我们可以将协程对象注册到时间循环中，它会被事件循环调用。我们可以使用 async 关键字来定义一个方法，这个方法在调用时不会立即被执行，而是返回一个协程对象。
# task：任务，它是对协程对象的进一步封装，包含了任务的各个状态。
# future：代表将来执行或没有执行的任务的结果，实际上和 task 没有本质区别。
# 另外我们还需要了解 async/await 关键字，它是从 Python 3.5 才出现的，专门用于定义协程。其中，async 定义一个协程，await 用来挂起阻塞方法的执行。


import asyncio
async def execute(x):
    print('Number:', x)
coroutine = execute(1)
print('Coroutine:', coroutine)
print('After calling execute')
loop = asyncio.get_event_loop()
loop.run_until_complete(coroutine)  # 当我们将 coroutine 对象传递给 run_until_complete 方法的时候，实际上它进行了一个操作就是将 coroutine 封装成了 task 对象
print('After calling loop')


# 显式地进行声明
async def execute(x):
    print('Number:', x)
    return x
coroutine = execute(1)
print('Coroutine:', coroutine)
print('After calling execute')
loop = asyncio.get_event_loop()
task = loop.create_task(coroutine)
print('Task:', task)
loop.run_until_complete(task)
print('Task:', task)
print('After calling loop')

# 没有声明 loop 也可以提前定义好 task 对象
async def execute(x):
    print('Number:', x)
    return x
coroutine = execute(1)
print('Coroutine:', coroutine)
print('After calling execute')
task = asyncio.ensure_future(coroutine)
print('Task:', task)
loop = asyncio.get_event_loop()
loop.run_until_complete(task)
print('Task:', task)
print('After calling loop')

# 绑定回调 为某个 task 绑定一个回调方法
import requests
async def request():
    url = 'https://www.baidu.com'
    status = requests.get(url)
    return status
def callback(task):
    print('Status:', task.result())
coroutine = request()
task = asyncio.ensure_future(coroutine)
task.add_done_callback(callback)
print('Task:', task)
loop = asyncio.get_event_loop()
loop.run_until_complete(task)
print('Task:', task)

print()
#  多任务协程
async def request():
    url = 'https://www.baidu.com'
    status = requests.get(url)
    return status
tasks = [asyncio.ensure_future(request()) for _ in range(5)]
print('Tasks:', tasks)
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
for task in tasks:
    print('Task Result:', task.result())


# 协程实现
# 错误
# start = time.time()
#
# async def request():
#     url = 'https://static4.scrape.cuiqingcai.com/'
#     print('Waiting for', url)
#     response = requests.get(url)
#     print('Get response from', url, 'response', response)
#
# tasks = [asyncio.ensure_future(request()) for _ in range(10)]
# loop = asyncio.get_event_loop()
# loop.run_until_complete(asyncio.wait(tasks))
# end = time.time()
# print('Cost time:', end - start)


# 使用 aiohttp
# aiohttp 是一个支持异步请求的库，利用它和 asyncio 配合我们可以非常方便地实现异步请求操作。
import aiohttp
# async def get(url):
#     session = aiohttp.ClientSession()
#     response = await session.get(url)
#     await response.text()
#     await session.close()
#     return response
# async def request():
#     url = 'https://static4.scrape.cuiqingcai.com/'
#     print('Waiting for', url)
#     response = await get(url)
#     print('Get response from ', url, 'response', response)
#
# start = time.time()
# tasks = [asyncio.ensure_future(request()) for _ in range(10)]
# loop = asyncio.get_event_loop()
# loop.run_until_complete(asyncio.wait(tasks))
# end = time.time()
# print('Cost time:', end - start)



def test(number):
    start = time.time()

    async def get(url):
        session = aiohttp.ClientSession()
        response = await session.get(url)
        await response.text()
        await session.close()
        return response

    async def request():
        url = 'https://www.baidu.com/'
        await get(url)

    tasks = [asyncio.ensure_future(request()) for _ in range(number)]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    end = time.time()
    print('Number:', number, 'Cost time:', end - start)

for number in [1, 3, 5, 10, 15, 30, 50, 75, 100, 200, 500]:
    test(number)