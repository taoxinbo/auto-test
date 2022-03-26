import requests, codecs, re, urllib, os, random, math
from PIL import Image
import numpy as np
import cv2 as cv

txtpath = 'C:/Users/11037/Desktop/test/qqfriends.txt'  # 你从QQ邮箱中粘贴的文件
savepath = 'C:/Users/11037/Desktop/touxiang/'  # 头像存储位置

resultSavePath = 'C:/Users/11037/Desktop/result2.png'  # 结果存储位置
modePath = 'C:/Users/11037/Desktop/leno.jpg'  # 模板存储位置

friends_count = 0  # 好友数量
all_mean_rgbs = []  # 存储计算出的所有平均rgb值


def meanrbg(img):  # 计算图片平均rgb
	rgb = np.array(img)
	r = int(round(np.mean(rgb[:, :, 0])))
	g = int(round(np.mean(rgb[:, :, 1])))
	b = int(round(np.mean(rgb[:, :, 2])))
	return (r, g, b)


def gettouxiang(txtpath):  # 输入你的txt文件存储位置
	file = codecs.open(txtpath, 'rb', 'utf-8')
	s = file.read()
	pattern = re.compile(r'\d+@qq.com')
	all_mail = pattern.findall(s)  # 正则表达式匹配所有的qq号
	all_link = []  # 用于存储需要访问的链接
	url = 'http://qlogo.store.qq.com/qzone/'
	for mail in all_mail:
		qq = mail.replace('@qq.com', '')
		l = url + qq + '/' + qq + '/100'
		all_link.append(l)
	i = 1
	for link in all_link:  # 遍历链接，下载头像
		saveurl = savepath + str(i) + '.png'
		savaImg(link, saveurl)
		i += 1
		print('已下载', i)
	friends_count = len(all_link)  # 获取朋友头像数量
	return True


def savaImg(picurl, saveurl):  # 存储图片函数，picurl是图片的URL，saveurl是本地存储位置
	try:
		bytes = urllib.request.urlopen(picurl)
		file = open(saveurl, 'wb')
		file.write(bytes.read())
		file.flush()
		file.close()
		return True
	except:
		print('worry')
		savaImg(picurl, saveurl)


def simple_split(filepackage, size, littlesize):  # 简单拼接，参数为图片文件名，每行每列的size，小头像图片的大小
	row = size[0]
	col = size[1]
	bigimg = Image.new('RGBA', (littlesize * row, littlesize * col))
	number = 0
	for i in range(row):
		for j in range(col):
			randpic = random.randint(1, friends_count)
			img = Image.open(filepackage + str(randpic) + '.png').convert('RGBA')
			img = img.resize((littlesize, littlesize))
			loc = (i * littlesize, j * littlesize, (i + 1) * littlesize, (j + 1) * littlesize)
			print(loc, number)
			number += 1
			bigimg.paste(img, loc)
	bigimg.save(resultSavePath)


def mode_split(filepackage, modepath, bigsize, littlesize):  # 以模板存储头像
	row = bigsize[0]  # 大图每行多少个小头像
	col = bigsize[1]  # 每列
	suitSize = (littlesize * row, littlesize * col)  # 大图最终的像素size
	bigImg = Image.open(modepath)
	bigImg = bigImg.resize(suitSize)
	resultImg = Image.new('RGBA', suitSize)
	
	for i in range(row):
		for j in range(col):
			cutbox = (i * littlesize, j * littlesize, (i + 1) * littlesize, (j + 1) * littlesize)  # 模板剪切用于对比的某个区域
			cutImg = bigImg.crop(cutbox)  # 复制到cutImg中
			tmprgb = meanrbg(cutImg)
			suitOne = mostSuitImg(tmprgb) + 1  # 对比出最合适的头像
			
			img = Image.open(filepackage + str(suitOne) + '.png').convert('RGBA')
			img = img.resize((littlesize, littlesize))
			resultImg.paste(img, cutbox)
			print('已粘贴', cutbox)
	resultImg.save(resultSavePath)  # 存储


def mostSuitImg(tmprgb):  # 进行对比，找出最合适的头像
	global all_mean_rgbs
	minRange = 200000
	id = 0
	for rgb in all_mean_rgbs:
		tmp = (rgb[1][0] - tmprgb[2]) ** 2 + (rgb[1][1] - tmprgb[1]) ** 2 + (rgb[1][2] - tmprgb[1]) ** 2
		if tmp < minRange:
			minRange = tmp
			id = rgb[0]
	return id


if __name__ == '__main__':
	# gettouxiang(txtpath)   #获取头像，如果已经获取就可以给注释掉了
	# simple_split(savepath,(20,20),30)   #简单拼接
	
	# 模板拼接
	for i in range(1, friends_count + 1):
		img = cv.imread(savepath + str(i) + '.png')
		rgb = meanrbg(img)
		all_mean_rgbs.append(rgb)
	all_mean_rgbs = list(enumerate(all_mean_rgbs))  # 给列表增加一个索引
	
	mode_split(savepath, modePath, (50, 80), 20)  # 模板拼接