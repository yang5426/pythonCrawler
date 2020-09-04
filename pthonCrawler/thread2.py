import threading
import time


class MyThread(threading.Thread):
    def __init__(self, second):
        threading.Thread.__init__(self)
        self.second = second

    def run(self):
        print(f'Threading {threading.current_thread().name} is running')
        print(f'Threading {threading.current_thread().name} sleep {self.second}s')
        time.sleep(self.second)
        print(f'Threading {threading.current_thread().name} is ended')

print(f'Threading {threading.current_thread().name} is running')
# threads = []
# for i in [1, 5]:
#     thread = MyThread(i)
#     threads.append(thread)
#     thread.start()
# for thread in threads:
#     thread.join()

# t1 = MyThread(2)
# t1.start()
# t2 = MyThread(5)
# t2.setDaemon(True)  # 在这里我们通过 setDaemon 方法将 t2 设置为了守护线程，这样主线程在运行完毕时，t2 线程会随着线程的结束而结束。
# t2.start()   # 不过细心的你可能会发现，这里并没有调用 join 方法，如果我们让 t1 和 t2 都调用 join 方法，主线程就会仍然等待各个子线程执行完毕再退出，不论其是否是守护线程

count = 0
# 互斥锁
class MyThread2(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global count
        lock.acquire()
        temp = count + 1
        time.sleep(0.001)
        count = temp
        lock.release()


lock = threading.Lock()
threads = []
for _ in range(1000):
    thread = MyThread2()
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()
print(f'Final count: {count}')
print(f'Threading {threading.current_thread().name} is ended')





















