# coding:utf-8

'''
	 豆瓣爬取沈腾的海报 —— json数据下载
'''

import requests
import json
import os


#指定文件路径
os.chdir("D:/stPictures")
#查询的关键字
query = "沈腾"

#下载图片
def download(src, id):
	dir = './' + str(id) + '.jpg'
	try:
		pic = requests.get(src, timeout=30) #获取连接，并且等待30秒，防止出现http请求错误
		fp = open(dir, 'wb')
		fp.write(pic.content)
		fp.close()
	except requests.exceptions.ConnectionError:
		print("图片无法下载")

# for循环请求全部的url
for i in range(0, 40, 20):
	url = 'https://www.douban.com/j/search_photo?q=' + query + '&limit=20&start=' + str(i)
	html = requests.get(url).text
	
	#将json数据转换成Python对象
	response = json.loads(html, encoding='utf-8')
	for image in response["images"]:          #选择返回回来的images的键对应的值
		print(image['src'])                   #查看当前图片对应的网址
		download(image['src'], image['id'])   #调用函数



