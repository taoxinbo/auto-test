# encoding=utf-8
# @Time : 2020/9/4 15:37
# @Author : TaoXB
# 此文件是读取当前文件夹下的所有文件名称和读取某一行内容，放入excel中
import os
import xlwt  # 操作excel模块
import sys

file_path = sys.path[0] + '\\filenamelist.xls'  # sys.path[0]为要获取当前路径，filenamelist为要写入的文件
f = xlwt.Workbook(encoding='utf-8', style_compression=0)  # 新建一个excel
sheet = f.add_sheet('sheet1')  # 新建一个sheet
pathDir = os.listdir(sys.path[0])  # 文件放置在当前文件夹中，用来获取当前文件夹内所有文件目录
sheet.write(0, 0, '文件名')  # A1格子里写入汉字‘文件名’
sheet.write(0, 1, '文件说明')  # B1格子里写入汉字‘文件说明’
sheet.write(0, 2, '备注')  # C1格子里写入汉字‘备注’

i = 1  # 将文件列表写入test.xls
j = 0 # 统计文件数量
for s in pathDir:
    file = os.path.splitext(s) #把文件进行切割，分为文件名和文件类型
    filename, type = file #filename赋值为文件名，type赋值为文件类型
    #print(filename)
    #print(type)
    if filename in ('__init__', '__pycache__') or type in ('.xls','.txt'): #过滤掉文件名为‘__init__’和文件类型为‘.xls、.txt’
        continue
    else:
        sheet.write(i, 0, s)  # 参数i,0,s分别代表行，列，写入值
        fp = open(s, "r", encoding="utf-8")
        fp.seek(0, 0)
        lines = fp.readlines()
        print(s + "：第4行内容为：" + lines[3])
        sheet.write(i, 1, lines[3]) #和文件名对应的一行，写入文件说明
        i= i+1
        j = j + 1

print(file_path)
print(j)  # 显示文件名数量
f.save(file_path)
