#encoding=utf-8
import cx_Oracle
import time
import traceback
import xlsxwriter
import xlwt  # 操作excel模块
# 从文件所在目录中导入Log.py文件中所有内容
from Action.Log import *
from Config.VarConfig import *
from Config.Budid import *
from Config.Orgcode import *
import base64
import re


# #测试数据
# budid1=[
#     "A005001010101",
#     "A005001010102"]
#     # "A005001010103",
#     # "8001010401"]

# #测试数据
# orgcode1=[
#     "CRH0000",
#     "SUPORG"]
#     # "RFZH000",
#     # "RFNM000",
#     # "HBGT000"]

print("开始时间：",time.strftime("%Y-%m-%d %H:%M:%S"))

# 读取预占报文的内容
with open(parentDirPath + '/Util/YZ/' + 'YZ.txt', encoding='utf-8') as fp:
    body1 = fp.read()

#print(type(body1))

# 读取实占报文的内容
with open(parentDirPath + '/Util/SZ/' + 'SZ.txt', encoding='utf-8') as fp:
    body3 = fp.read()

#print(type(body3))

#删除YZ_Encode.bat
try:
    os.remove(parentDirPath + '/Util/YZ/' +'YZ_Encode.bat')
    print("YZ_Encode.bat,删除完毕")
except(FileNotFoundError):
    print("YZ_Encode.bat,不存在")

#删除SZ_Encode.bat
try:
    os.remove(parentDirPath + '/Util/SZ/' +'SZ_Encode.bat')
    print("SZ_Encode.bat,删除完毕")
except(FileNotFoundError):
    print("SZ_Encode.bat,不存在")

#在目录下生成预占的bat文件:YZ_Encode.bat
YZ_Encode = open(parentDirPath + '/Util/YZ/' +'YZ_Encode.bat', 'w')

#在目录下生成实占的bat文件:SZ_Encode.bat
SZ_Encode = open(parentDirPath + '/Util/SZ/' +'SZ_Encode.bat', 'w')

#用来：给ID拼接唯一性和计数
i=1

#遍历budid
for budid2 in budid:

    for orgcode2 in orgcode:
        temp = time.strftime("%Y%m%d%H%M%S")
        patt1 =r'ID'
        id='YC'+str(temp)+str(i)
        body2 = re.sub(patt1,id,body1)
        body4 = re.sub(patt1,id,body3)

        patt2 = r'ORG'
        body2 = re.sub(patt2, orgcode2, body2)
        body4 = re.sub(patt2, orgcode2, body4)

        patt3 = r'BUD'
        body2 = re.sub(patt3, budid2, body2)

        #print('预占报文：',body2)
        #print(type(body2))
        str1 = base64.b64encode(bytes(body2,'utf-8'))
        print(str1, file=YZ_Encode)

        #print('实占报文：',body4)
        str2 = base64.b64encode(bytes(body4, 'utf-8'))
        print(str2, file=SZ_Encode)

        print('第%s对,生成成功！' %i)
        i += 1

YZ_Encode.close()
SZ_Encode.close()


#打开读取YZ_Encode.bat中内容
with open(parentDirPath + '/Util/YZ/' + 'YZ_Encode.bat', encoding='utf-8') as fp:
    YZ_Encode2 = fp.read()
#把文件中‘b'’去掉
patt = "b'"
YZ_Encode2 = re.sub(patt, "", YZ_Encode2)
#把文件中‘'’去掉
patt = "'"
YZ_Encode2 = re.sub(patt, "", YZ_Encode2)

#print(YZ_Encode2)

#把替换好的内容，保存到YZ_Encode.bat中
with open(parentDirPath + '/Util/YZ/' + 'YZ_Encode.bat', 'w', encoding="utf-8") as fp:
    fp.write(YZ_Encode2)



#打开读取SZ_Encode.bat中内容
with open(parentDirPath + '/Util/SZ/' + 'SZ_Encode.bat', encoding='utf-8') as fp:
    SZ_Encode2 = fp.read()
#把文件中‘b'’去掉
patt = "b'"
SZ_Encode2 = re.sub(patt, "", SZ_Encode2)
#把文件中‘'’去掉
patt = "'"
SZ_Encode2 = re.sub(patt, "", SZ_Encode2)

#print(SZ_Encode2)

#把替换好的内容，保存到SZ_Encode.bat中
with open(parentDirPath + '/Util/SZ/' + 'SZ_Encode.bat', 'w', encoding="utf-8") as fp:
    fp.write(SZ_Encode2)


print("结束时间：", time.strftime("%Y-%m-%d %H:%M:%S"))