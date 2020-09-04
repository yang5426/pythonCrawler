import re

# match
content = 'Hello 123 4567 World_This is a Regex Demo'
print(len(content))
result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}', content)
print(result)
print(result.group())
print(result.span())

content = 'Hello 1234567 World_This is a Regex Demo'

result = re.match('^Hello\s(\d+)\sWorld', content)
print(result)
print(result.group())
print(result.group(1))
print(result.span())

# 通用匹配  .*  . 可以匹配任意字符（除换行符）  * 代表匹配前面的字符无限次 组合在一起就可以匹配任意字符
result = re.match('^Hello.*Demo$', content)
print(result)
print(result.group())
print(result.span())

# 贪婪与非贪婪
# 贪婪匹配是尽可能匹配多的字符，非贪婪匹配就是尽可能匹配少的字符
content = 'Hello 1234567 World_This is a Regex Demo'
result = re.match('^He.*(\d+).*Demo$', content)
print(result)
print(result.group(1))  # 正则表达式中 .* 后面是 \d+，也就是至少一个数字，并没有指定具体多少个数字，因此，.* 就尽可能匹配多的字符，这里就把 123456 匹配了，给 \d+ 留下一个可满足条件的数字 7，最后得到的内容就只有数字 7 了。
result = re.match('^He.*?(\d+).*Demo$', content)
print(result.group(1))




# 修饰符
content = '''Hello 1234567 World_This
is a Regex Demo
'''
result = re.match('^He.*?(\d+).*?Demo$', content, re.S)
print(result.group())
print(result.group(1))


# 转义匹配
content1 = '(百度) www.1234567baidu.com'
result1 = re.match('\(百度\) www\..*?(d+).*?\.com', content1)
print(result1)


# search
content = 'Extra stings Hello 1234567 World_This is a Regex Demo Extra stings'
result = re.search('Hello.*?(\d+).*?Demo', content)
print(result.group())


html = '''<div id="songs-list">
<h2 class="title">经典老歌</h2>
<p class="introduction">
经典老歌列表
</p>
<ul id="list" class="list-group">
<li data-view="2">一路上有你</li>
<li data-view="7">
<a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
</li>
<li data-view="4" class="active">
<a href="/3.mp3" singer="齐秦">往事随风</a>
</li>
<li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
<li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
<li data-view="5">
<a href="/6.mp3" singer="邓丽君">但愿人长久</a>
</li>
</ul>
</div>'''
# result = re.search('<li.*?active.*?singer="(.*?)">(.*?)</a>', html, re.S)
result = re.search('<li.*?singer="(.*?)">(.*?)</a>', html, re.S)
if result:
    print(result.group(1), result.group(2))


# findall
results = re.findall('<li.*?href="(.*?)".*?singer="(.*?)">(.*?)</a>', html, re.S)
print(results)
print(type(results))
for result in results:
    print(result)
    print(result[0], result[1], result[2])



# sub 想要把一串文本中的所有数字都去掉
content = '54aK54yr5oiR54ix5L2g'
content = re.sub('\d+', '', content)
print(content)


result = re.findall('<li.*?>\s*?(<a.*?>)?(\w+)(</a>)?\s*?</li>', html, re.S)
for result in results:
    print(result[2])

html = re.sub('<a.*?>|</a>', '', html)
print(html)
results = re.findall('<li.*?>(.*?)</li>', html, re.S)
for result in results:
    print(result.strip())



# compile 这个方法可以将正则字符串编译成正则表达式对象，以便在后面的匹配中复用
content1 = '2019-12-15 12:00'
content2 = '2019-12-17 12:55'
content3 = '2019-12-22 13:21'
pattern = re.compile('\d{2}:\d{2}', re.S)
result1 = re.sub(pattern, '', content1)
result2 = re.sub(pattern, '', content2)
result3 = re.sub(pattern, '', content3)
print(result1, result2, result3)




