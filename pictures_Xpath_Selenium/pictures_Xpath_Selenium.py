# coding:utf-8

'''
	 豆瓣电影爬取沈腾的海报以及电影名 —— selenium + Xpath
'''

from selenium import webdriver
from lxml import etree
import requests
import json
import os
import time

query = '沈腾'

os.chdir("D:/stFiles") 

def download(src, id):
	dir = './' + str(id) + '.webp'
	try:
		pic = requests.get(src, timeout=30)        #获取连接，并且等待 30 秒，防止出现 http 请求错误
		fp = open(dir, 'wb')
		fp.write(pic.content)
		fp.close()
	except requests.exceptions.ConnectionError:
		print("图片无法下载")


browser = webdriver.Chrome('D:/chromedriver.exe')  #这里的地址填写你的 chromedriver.exe 路径

for i in range(0, 46, 15):
	url = 'https://movie.douban.com/subject_search?search_text='+ query +'&cat=1002' + '&start=' + str(i)
	browser.get(url)
	time.sleep(5)

	html = etree.HTML(browser.page_source)         #etree整个文档获取页面内容
	#图片和电影名 Xpath 地址
	src_xpath = "//*[@class='item-root']/a/img/@src"
	title_xpath = "//*[@class='item-root']/div[@class='detail']/div[@class='title']/a[@class='title-text']"

	#Xpath 解析
	srcs = html.xpath(src_xpath)
	titles = html.xpath(title_xpath)

	for src, title in zip(srcs, titles):
		download(src, title.text)
		time.sleep(5)
browser.quit()