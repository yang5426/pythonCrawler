print("abc", "yyy", "aaa", 100 + 200)
print(r'''11111 \n
222222222
333333333
''')  # 多行输出中 前面加r 里面的内容转义符不起作用

a = 'abc'
b = a
a = 'XYT'
print(b, a)

# 常量
PI = 3.14159265

# 除法 和 地板除 和 取余
print(10 / 3)
print(10 // 3)
print(10 % 3)

# 字符串和编码
# 一字节 byte = 8 比特 bit   最大 11111111 = 255 , 二字节 = 65535 ， 4字节 = 4294967295
# UTF-8编码把一个Unicode字符根据不同的数字大小编码成1-6个字节，常用的英文字母被编码成1个字节，汉字通常是3个字节，只有很生僻的字符才会被编码成4-6个字节。
# 在计算机内存中，统一使用Unicode编码，当需要保存到硬盘或者需要传输的时候，就转换为UTF-8编码。

# 对于单个字符的编码，Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符：
print(ord('王'), ord('A'))
print(chr(23011))

# Python对bytes类型的数据用带b前缀的单引号或双引号表示：
x = b"ABC"
# 纯英文的str可以用ASCII编码为bytes，内容是一样的，含有中文的str可以用UTF-8编码为bytes。含有中文的str无法用ASCII编码，因为中文编码的范围超过了ASCII编码的范围
print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))
# print('中文'.encode('ascii'))

# 反过来，如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用decode()方法
print(b'ABC'.decode('ascii'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
# 如果bytes中只有一小部分无效的字节，可以传入errors='ignore'忽略错误的字节：
print(b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore'))
print(len('usgdhajsifbsdajkfhahidosafhaoidfhsadiofhdsaifj'))

# tuple一旦初始化就不能修改 只有1个元素的tuple定义时必须加一个逗号,，来消除和 小括号() 歧义
classmates = ('Michael', 'Bob', 'Tracy')
print(classmates[0], classmates[-1])
t = (1,)
print(t[0])

# 条件判断
age = 5
if age > 18:
    print("your age is ", age)
    print("adult")
else:
    print("teenager")

# 循环
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)
list1 = list(range(100))
sum = 0
for num in list1:
    sum += num
print(sum)
n = 1
while n <= 100:
    if n > 10:
        break
    print(n)
    n = n + 1
print('END')
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:
        continue
    print(n)
print('END')

s = set([1, 2, 3, 3])
print(s)
s.remove(1)
print(s)


def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x


print(my_abs(-100))

import math


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


x, y = move(100, 100, 60, math.pi / 6)
print(x, y)
r = move(100, 100, 60, math.pi / 6)
print(r)


# 定义默认参数要牢记一点：默认参数必须指向不变对象！ 默认参数定义为list这种每次调用都会改变默认参数的值 L = None

# *nums表示把nums这个list的所有元素作为可变参数传进去。这种写法相当有用，而且很常见。

# 关键字参数 **kw , 调用函数时可以只传必选参数 也可以传入任意个数的关键字参数
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


for i, value in enumerate(names):
    print(i, value)

# 列表生成式
l1 = [x * x for x in range(1, 11)]
print(l1)
l2 = [x * x for x in range(1, 11) if x % 2 == 0]
print(l2)

import os

print([d for d in os.listdir('.')])

print([s.lower() for s in ['Hello', 'World', 'IBM', 'Apple']])

# 如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？这样就不必创建完整的list，
# 从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator。
g = (x * x for x in range(10))
for n in g:
    print(n)

from collections.abc import Iterator

# 迭代器 iterable (list、dict、str) 和 iterator (iter()函数可以变成iterator)
# 而生成器不但可以作用于for循环，还可以被next()函数不断调用并返回下一个值，直到最后抛出StopIteration错误表示无法继续返回下一个值了。
print(isinstance(iter([]), Iterator))
print(isinstance([], Iterator))

# Python的for循环本质上就是通过不断调用next()函数实现的
for x in [1, 2, 3, 4, 5]:
    pass
# ==>
it = iter([1, 2, 3, 4, 5])
while True:
    try:
        x = next(it)
        print(x)
    except StopIteration:
        break


# 函数式编程的一个特点就是，允许把函数本身作为参数传入另一个函数，还允许返回一个函数！

# map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
def f1(x):
    return x * x


r1 = map(f1, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(r1))
print(list(map(str, (1, 2))))

# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
from functools import reduce


def add(x, y):
    return x + y


print(reduce(add, [1, 5, 6]))

# 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。

# 匿名函数lambda x: x * x
lam = lambda x: x * x
print(lam(2))

# 代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
import functools


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper


# 简单总结functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。
int2 = functools.partial(int, base=2)
print(int2('100000'))
