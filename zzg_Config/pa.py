# encoding=utf-8
# coding:utf-8

from bs4 import BeautifulSoup
import requests

url = 'http://python123.io/ws/demo.html'
r = requests.get(url)
demo = r.text  # 服务器返回响应

soup = BeautifulSoup(demo, "html.parser")
"""
demo 表示被解析的html格式的内容
html.parser表示解析用的解析器
"""
print(soup)  # 输出响应的html对象
print(soup.prettify())  # 使用prettify()格式化显示输出