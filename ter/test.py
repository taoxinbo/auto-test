# encoding=utf-8
# @Time : 2020/8/14 14:49
# @Author : Mindy
# 此文件是测试资金结算模块，包括基础设置、备案信息管理
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Action.keyword_action import *
# 从文件所在目录中导入Log.py文件中所有内容
from Action.Log import *
from Config.VarConfig import *
from selenium.common.exceptions import WebDriverException
import traceback
import time
from datetime import datetime, date, timedelta
from Action.dir_opration import make_current_date_dir, make_current_hour_dir
from Action.send_mail import *
import random
use=str(random.randint(1000, 10000))
sql="update t_se_payments set paystate = '4' where purpose = '"+use+"'"
print(sql)

ran=random.randint(1000, 10000)
p="测试拆分"+str(ran)
sql = "update t_se_payments set NOTECODE = 'ZJFK_001010_202010_00009999'  where purpose = '"+p +"'"
print(type(sql))

#update t_se_payments set NOTECODE = 'ZJFK_001010_202010_00009999'  where purpose = '测试拆分'

zzg = "zzg"

temp1 = time.strftime("%H%M%S")
PJH="YFPJ"+str(temp1)
print(PJH)
# print("开始时间：",time.strftime("%Y%m%d%H%M%S"))

code = time.strftime("%Y%m%d%S")
name="JGJG"+str(time.strftime("%H%M%S"))

today = date.today()
we=str(today)+" "+"08:30:00"
print(12223)
print(we)

print(timedelta(days=720))
expireddate = today + timedelta(days=720)
print(expireddate)

temp = time.strftime("%Y%m%d%H%M%S")
print(type(temp))
print(2)

for i in range(1,4):
	print(i)


today = date.today()
today1 = today + timedelta(days=730)
print(str(today1))
	

				
				
			
				
			
				
				
				
			
				

	
		


if __name__ == '__main__':
	#  启动单元测试
	unittest.main(verbosity=2)
