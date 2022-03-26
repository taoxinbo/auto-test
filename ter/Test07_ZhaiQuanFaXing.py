# encoding=utf-8
# @Time : 2020/10/28 13:30
# @Author : zzg
# 此文件是测试债券发行管理模块，包含基础设置，注册登记，发行登记，注册登记查看，发行登记查看，债券兑付申请，还款计划查看
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
# print("开始时间：",time.strftime("%Y-%m-%d %H:%M:%S"))

driver = ""


class Test_Zqfx(unittest.TestCase):
	
	# 启动浏览器
	def setUp(self):
		# 启动浏览器的另外一个方法：通过封装启动浏览器的驱动，启动不同浏览器
		self.driver = get("chrome")
	
	# 登陆系统、对系统设置进行操作
	def test_trade(self):
		#login(G_Mys_Url, mindy, Password, "亚唐科技")
		login(G_Mys_Url, mindy, Password, "亚唐科技")
		
		logging.info("开始测试债券发行管理的页面功能")
		# 将页面的滚动条滑动到‘债券发行管理’页面的地方
		js_gd("xpath", "//span[contains(text(),'债券发行管理')]")
		# 用JS的方法点击债券发行管理菜单按钮
		js_click("xpath", "//span[contains(text(),'债券发行管理')]")
		sleep(1)

		
		#测试监管机构💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
		try:
			logger.info("开始测试->债券发行管理->基础设置，监管机构")
			# 点击基础设置菜单
			click("xpath", "//li[@f_value='bondissuancesetting']/descendant-or-self::*[5]")
			sleep(1)
			# 点击监管机构菜单
			click("xpath", "//li[@f_value='bondregisterorg']/descendant-or-self::*[5]")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			
			for i in range(1,3):
				# 切入监管机构的iframe窗体
				switch_to("xpath", "//iframe[@id='bondregisterorg-tab-iframe']")
				# 用JS的方法点击新增按钮
				js_click("xpath", "//span[text()='新增']")
				sleep(1)
				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='addWin-iframe']")
				sleep(1)
				
				# 输入代码
				TestReg=time.strftime("%H%M%S")
				input("xpath", "//input[@name='code']", TestReg)
				sleep(2)
				
				# 输入的名称
				name="JGJG"+str(time.strftime("%H%M%S"))
				input("xpath", "//input[@id='name']", name)
				sleep(1)
				
				# 描述框中填入值
				input("xpath", "//textarea[@id='description']", "测试")
				sleep(1)
				
				# 点击保存按钮
				click("xpath", "//span[text()='保存']")
				
				# 退出所有iframe窗体
				switch_default()
				
				# 用隐式等待方法等页面出现新增成功的提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				if i==2:
					print("监管机构，新增成功！")
				time.sleep(3)
			
			#测试删除功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入监管机构的iframe窗体
			switch_to("xpath", "//iframe[@id='bondregisterorg-tab-iframe']")
			# 刷新勾选数据
			click("xpath",'//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
			sleep(1)
			
			# 点击删除按钮
			click("xpath", "//span[text()='删除']")
			sleep(1)
			# 点击弹出框的OK键
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'成功删除')]")
			print("监管机构，删除成功！")
			time.sleep(3)
			
			# 测试修改功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入监管机构的iframe窗体
			switch_to("xpath", "//iframe[@id='bondregisterorg-tab-iframe']")
			# 刷新勾选数据
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
			sleep(1)
			
			# 点击修改按钮
			click("xpath", "//span[text()='修改']")
			sleep(1)
			# 切入修改的iframe窗体
			switch_to("xpath", "//iframe[@id='modWin-iframe']")
			# 修改描述框中的内容
			clear("xpath","//textarea[@id='description']")
			sleep(1)
			input("xpath", "//textarea[@id='description']", "自动化测试修改")
			sleep(2)
			
			# 点击保存按钮
			click("xpath", "//span[text()='保存']")
			
			# 退出所有iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("监管机构，修改成功！")
			time.sleep(3)
			
			# 测试失效功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入监管机构的iframe窗体
			switch_to("xpath", "//iframe[@id='bondregisterorg-tab-iframe']")
			# 刷新勾选数据
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
			sleep(1)
			
			# 点击失效按钮
			click("xpath", "//span[text()='失效']")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'失效成功！')]")
			print("监管机构，点击失效成功！")
			time.sleep(3)
			
			# 测试生效功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入监管机构的iframe窗体
			switch_to("xpath", "//iframe[@id='bondregisterorg-tab-iframe']")
			# 刷新勾选数据
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
			sleep(1)
			
			# 点击生效按钮
			click("xpath", "//span[text()='生效']")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'生效成功！')]")
			print("监管机构，点击生效成功！")
			
			#点击基础设置回归原样
			click("xpath", "//li[@f_value='bondissuancesetting']/descendant-or-self::*[5]")
			time.sleep(3)
			
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("监管机构失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
			
		#测试评级机构💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
		try:
			logger.info("开始测试->债券发行管理->基础设置，评级机构")
			# 点击基础设置菜单
			click("xpath", "//li[@f_value='bondissuancesetting']/descendant-or-self::*[5]")
			sleep(1)
			# 点击评级机构菜单
			click("xpath", "//span[text()='评级机构']")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			
			for i in range(1, 3):
				# 切入评级机构的iframe窗体
				switch_to("xpath", "//iframe[@id='bondratingagency-tab-iframe']")
				# 用JS的方法点击新增按钮
				js_click("xpath", "//span[text()='新增']")
				sleep(1)
				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='addWin-iframe']")
				sleep(1)
				# 输入代码
				TestReg = time.strftime("%Y%d%S")
				input("xpath", "//input[@name='code']", TestReg)
				sleep(1)
				
				# 输入的名称
				name = "PJJG"+str(time.strftime("%H%M%S"))
				input("xpath", "//input[@id='name']", name)
				sleep(2)
				
				# 描述框中填入值
				input("xpath", "//textarea[@id='description']", "自动化测试评级机构描述框")
				sleep(2)
				
				# 点击保存按钮
				click("xpath", "//span[text()='保存']")
				sleep(1)
				# 退出所有iframe窗体
				switch_default()
				
				# 用隐式等待方法等页面出现提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				if i ==2 :
					print("评级机构，保存成功！")
				time.sleep(3)
				
			# 测试删除功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入评级机构的iframe窗体
			switch_to("xpath", "//iframe[@id='bondratingagency-tab-iframe']")
			# 刷新勾选数据
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
			sleep(1)
			
			# 点击删除按钮
			click("xpath", "//span[text()='删除']")
			sleep(1)
			# 点击弹出框的OK键
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'成功删除')]")
			print("评级机构，删除成功！")
			time.sleep(3)
			# 测试修改功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入评级机构的iframe窗体
			switch_to("xpath", "//iframe[@id='bondratingagency-tab-iframe']")
			# 刷新勾选数据
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
			sleep(1)
			
			# 点击修改按钮
			click("xpath", "//span[text()='修改']")
			sleep(1)
			# 切入修改的iframe窗体
			switch_to("xpath", "//iframe[@id='modWin-iframe']")
			# 修改描述框中的内容
			clear("xpath", "//textarea[@id='description']")
			sleep(1)
			input("xpath", "//textarea[@id='description']", "自动化测试修改")
			sleep(2)
			
			# 点击保存按钮
			click("xpath", "//span[text()='保存']")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("评级机构，修改成功！")
			time.sleep(3)
			
			# 测试失效功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入评级机构的iframe窗体
			switch_to("xpath", "//iframe[@id='bondratingagency-tab-iframe']")
			# 刷新勾选数据
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
			sleep(1)
			
			# 点击失效按钮
			click("xpath", "//span[text()='失效']")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'失效成功！')]")
			print("评级机构，点击失效成功！")
			time.sleep(3)
			
			# 测试生效功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入评级机构的iframe窗体
			switch_to("xpath", "//iframe[@id='bondratingagency-tab-iframe']")
			# 刷新勾选数据
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
			sleep(1)
			
			# 点击生效按钮
			click("xpath", "//span[text()='生效']")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'生效成功！')]")
			print("评级机构，点击生效成功！")
			
			# 点击基础设置菜单
			click("xpath", "//li[@f_value='bondissuancesetting']/descendant-or-self::*[5]")
			time.sleep(3)
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("评级机构失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		
		
		# 测试注册品种💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
		try:
			logger.info("开始测试->债券发行管理->基础设置，注册品种")
			# 点击基础设置菜单
			click("xpath", "//li[@f_value='bondissuancesetting']/descendant-or-self::*[5]")
			sleep(1)
			# 点击注册品种菜单
			click("xpath", "//span[text()='注册品种']")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			
			for i in range(1, 3):
				# 切入注册品种的iframe窗体
				switch_to("xpath", "//iframe[@id='bondregistervariety-tab-iframe']")
				# 用JS的方法点击新增按钮
				js_click("xpath", "//span[text()='新增']")
				sleep(1)
				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='addWin-iframe']")
				# 输入代码
				TestReg = time.strftime("%Y%H%S")
				input("xpath", "//input[@name='code']", TestReg)
				sleep(1)
				
				# 输入的名称
				name = "ZCPZ" + str(time.strftime("%H%M%S"))
				input("xpath", "//input[@id='name']", name)
				sleep(1)
				# 点击保存按钮
				click("xpath", "//span[text()='保存']")
				sleep(1)
				# 退出所有iframe窗体
				switch_default()
				# 用隐式等待方法等页面出现提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				if i ==2 :
					print("注册品种，新增成功！")
				time.sleep(3)
			
			# 测试删除功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入注册品种的iframe窗体
			switch_to("xpath", "//iframe[@id='bondregistervariety-tab-iframe']")
			# 刷新勾选数据
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
			sleep(1)
			
			# 点击删除按钮
			click("xpath", "//span[text()='删除']")
			sleep(1)
			# 点击弹出框的OK键
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'成功删除')]")
			print("注册品种，删除成功！")
			time.sleep(3)
			# 测试修改功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入注册品种的iframe窗体
			switch_to("xpath", "//iframe[@id='bondregistervariety-tab-iframe']")
			# 刷新勾选数据
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
			sleep(1)
			
			# 点击修改按钮
			click("xpath", "//span[text()='修改']")
			sleep(1)
			# 切入修改的iframe窗体
			switch_to("xpath", "//iframe[@id='modWin-iframe']")
			# 修改描述框中的内容
			clear("xpath", "//textarea[@id='description']")
			sleep(1)
			input("xpath", "//textarea[@id='description']", "自动化测试修改")
			sleep(2)
			
			# 点击保存按钮
			click("xpath", "//span[text()='保存']")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("注册品种，修改成功！")
			time.sleep(3)
			
			# 测试失效功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入注册品种的iframe窗体
			switch_to("xpath", "//iframe[@id='bondregistervariety-tab-iframe']")
			# 刷新勾选数据
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
			sleep(1)
			
			# 点击失效按钮
			click("xpath", "//span[text()='失效']")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'失效成功！')]")
			print("注册品种，点击失效成功！")
			time.sleep(3)
			
			# 测试生效功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入注册品种的iframe窗体
			switch_to("xpath", "//iframe[@id='bondregistervariety-tab-iframe']")
			# 刷新勾选数据
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
			sleep(1)
			
			# 点击生效按钮
			click("xpath", "//span[text()='生效']")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'生效成功！')]")
			print("评级机构，点击生效成功！")
			
			# 点击基础设置菜单
			click("xpath", "//li[@f_value='bondissuancesetting']/descendant-or-self::*[5]")
			time.sleep(3)
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("注册品种失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		
		
		# 测试法律顾问💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
		try:
			logger.info("开始测试->债券发行管理->基础设置，法律顾问")
			# 点击基础设置菜单
			click("xpath", "//li[@f_value='bondissuancesetting']/descendant-or-self::*[5]")
			sleep(1)
			# 点击注册品种菜单
			click("xpath", "//span[text()='法律顾问']")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			
			for i in range(1, 3):
				# 切入‘法律顾问’的iframe窗体
				switch_to("xpath", "//iframe[@id='bondlegaladviser-tab-iframe']")
				# 用JS的方法点击新增按钮
				js_click("xpath", "//span[text()='新增']")
				sleep(1)
				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='addWin-iframe']")
				sleep(1)
				
				# 输入代码
				TestReg = time.strftime("%Y%H%S")
				input("xpath", "//input[@name='code']", TestReg)
				sleep(1)
				
				# 输入的名称
				name = "FLGW" + str(time.strftime("%H%M%S"))
				input("xpath", "//input[@id='name']", name)
				sleep(1)
				
				# 描述框中填入值
				input("xpath", "//textarea[@id='description']", "大法师")
				sleep(1)
				
				# 点击保存按钮
				click("xpath", "//span[text()='保存']")
				sleep(1)
				# 退出所有iframe窗体
				switch_default()
				
				# 用隐式等待方法等页面出现提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				if i ==2 :
					print("法律顾问，保存成功！")
				time.sleep(3)
			
			# 测试删除功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入‘法律顾问’的iframe窗体
			switch_to("xpath", "//iframe[@id='bondlegaladviser-tab-iframe']")
			# 刷新勾选数据
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
			sleep(1)
			
			# 点击删除按钮
			click("xpath", "//span[text()='删除']")
			sleep(1)
			# 点击弹出框的OK键
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'成功删除')]")
			print("法律顾问，删除成功！")
			time.sleep(3)
			# 测试修改功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入‘法律顾问’的iframe窗体
			switch_to("xpath", "//iframe[@id='bondlegaladviser-tab-iframe']")
			# 刷新勾选数据
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
			sleep(1)
			
			# 点击修改按钮
			click("xpath", "//span[text()='修改']")
			sleep(1)
			# 切入修改的iframe窗体
			switch_to("xpath", "//iframe[@id='modWin-iframe']")
			# 修改描述框中的内容
			clear("xpath", "//textarea[@id='description']")
			sleep(1)
			input("xpath", "//textarea[@id='description']", "小法师")
			sleep(2)
			
			# 点击保存按钮
			click("xpath", "//span[text()='保存']")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("注册品种，修改成功！")
			time.sleep(3)
			
			# 测试失效功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入‘法律顾问’的iframe窗体
			switch_to("xpath", "//iframe[@id='bondlegaladviser-tab-iframe']")
			# 刷新勾选数据
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
			sleep(1)
			
			# 点击失效按钮
			click("xpath", "//span[text()='失效']")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'失效成功！')]")
			print("法律顾问，失效成功！")
			time.sleep(3)
			
			# 测试生效功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入‘法律顾问’的iframe窗体
			switch_to("xpath", "//iframe[@id='bondlegaladviser-tab-iframe']")
			# 刷新勾选数据
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
			sleep(1)
			
			# 点击生效按钮
			click("xpath", "//span[text()='生效']")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'生效成功！')]")
			print("法律顾问，生效成功！")
			
			# 点击基础设置菜单
			click("xpath", "//li[@f_value='bondissuancesetting']/descendant-or-self::*[5]")
			time.sleep(3)
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("注册品种失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		
		
		# 测试资金用途💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
		try:
			logger.info("开始测试->债券发行管理->基础设置，资金用途")
			# 点击基础设置菜单
			click("xpath", "//li[@f_value='bondissuancesetting']/descendant-or-self::*[5]")
			sleep(1)
			# 点击注册品种菜单
			click("xpath", "//span[text()='资金用途']")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			
			for i in range(1, 3):
				# 切入‘资金用途’的iframe窗体
				switch_to("xpath", "//iframe[@id='bondpurpose-tab-iframe']")
				# 用JS的方法点击新增按钮
				js_click("xpath", "//span[text()='新增']")
				sleep(1)
				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='addWin-iframe']")
				# 输入代码
				TestReg = time.strftime("%Y%m%d%S")
				input("xpath", "//input[@name='code']", TestReg)
				sleep(1)
				
				# 输入的名称
				name = "JGJG" + str(time.strftime("%H%M%S"))
				input("xpath", "//input[@id='name']", name)
				sleep(1)
				
				# 描述框中填入值
				input("xpath", "//textarea[@id='description']", "资金用途描述框")
				sleep(1)
				
				# 点击保存按钮
				click("xpath", "//span[text()='保存']")
				sleep(1)
				# 退出所有iframe窗体
				switch_default()
				
				# 用隐式等待方法等页面出现提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				if i ==2:
					print("资金用途，保存成功！")
				time.sleep(3)
			
			# 测试删除功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入‘资金用途’的iframe窗体
			switch_to("xpath", "//iframe[@id='bondpurpose-tab-iframe']")
			# 刷新勾选数据
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
			sleep(1)
			
			# 点击删除按钮
			click("xpath", "//span[text()='删除']")
			sleep(1)
			# 点击弹出框的OK键
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'成功删除1条记录！')]")
			print("资金用途，删除成功！")
			time.sleep(3)
			# 测试修改功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入‘资金用途’的iframe窗体
			switch_to("xpath", "//iframe[@id='bondpurpose-tab-iframe']")
			# 刷新勾选数据
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
			sleep(1)
			
			# 点击修改按钮
			click("xpath", "//span[text()='修改']")
			sleep(1)
			# 切入修改的iframe窗体
			switch_to("xpath", "//iframe[@id='modWin-iframe']")
			# 修改描述框中的内容
			clear("xpath", "//textarea[@id='description']")
			sleep(1)
			input("xpath", "//textarea[@id='description']", "资金用途修改")
			sleep(2)
			
			# 点击保存按钮
			click("xpath", "//span[text()='保存']")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("资金用途，修改成功！")
			time.sleep(3)
			
			# 测试失效功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入‘资金用途’的iframe窗体
			switch_to("xpath", "//iframe[@id='bondpurpose-tab-iframe']")
			# 刷新勾选数据
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
			sleep(1)
			
			# 点击失效按钮
			click("xpath", "//span[text()='失效']")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'失效成功！')]")
			print("资金用途，失效成功！")
			time.sleep(3)
			
			# 测试生效功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入‘资金用途’的iframe窗体
			switch_to("xpath", "//iframe[@id='bondpurpose-tab-iframe']")
			# 刷新勾选数据
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
			sleep(1)
			
			# 点击生效按钮
			click("xpath", "//span[text()='生效']")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'生效成功！')]")
			print("资金用途，生效成功！")
			
			# 点击基础设置菜单
			click("xpath", "//li[@f_value='bondissuancesetting']/descendant-or-self::*[5]")
			time.sleep(3)
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("资金用途失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		
		
		# 测试主承销商💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
		try:
			logger.info("开始测试->债券发行管理->基础设置，资金用途")
			# 点击基础设置菜单
			click("xpath", "//li[@f_value='bondissuancesetting']/descendant-or-self::*[5]")
			sleep(1)
			# 点击注册品种菜单
			click("xpath", "//span[text()='主承销商']")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			
			for i in range(1, 3):
				# 切入‘主承销商’的iframe窗体
				switch_to("xpath", "//iframe[@id='bondconsignee-tab-iframe']")
				# 用JS的方法点击新增按钮
				js_click("xpath", "//span[text()='新增']")
				sleep(1)
				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='addWin-iframe']")
				sleep(1)
				
				# 输入代码
				TestReg = time.strftime("%Y%m%d%S")
				input("xpath", "//input[@name='code']", TestReg)
				sleep(1)
				
				# 输入的名称
				name = "CXS" + str(time.strftime("%H%M%S"))
				input("xpath", "//input[@id='name']", name)
				sleep(1)
				
				# 描述框中填入值
				input("xpath", "//textarea[@id='description']", "主承销商描述框")
				sleep(1)
				
				# 点击保存按钮
				click("xpath", "//span[text()='保存']")
				sleep(1)
				# 退出所有iframe窗体
				switch_default()
				# 用隐式等待方法等页面出现提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				if i == 2 :
					print("主承销商，新增成功！")
				time.sleep(3)
			
			# 测试删除功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入‘主承销商’的iframe窗体
			switch_to("xpath", "//iframe[@id='bondconsignee-tab-iframe']")
			# 刷新勾选数据
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
			sleep(1)
			
			# 点击删除按钮
			click("xpath", "//span[text()='删除']")
			sleep(1)
			# 点击弹出框的OK键
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("主承销商，删除成功！")
			time.sleep(3)
			# 测试修改功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入‘主承销商’的iframe窗体
			switch_to("xpath", "//iframe[@id='bondconsignee-tab-iframe']")
			# 刷新勾选数据
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
			sleep(1)
			
			# 点击修改按钮
			click("xpath", "//span[text()='修改']")
			sleep(1)
			# 切入修改的iframe窗体
			switch_to("xpath", "//iframe[@id='modWin-iframe']")
			# 修改描述框中的内容
			clear("xpath", "//textarea[@id='description']")
			sleep(1)
			input("xpath", "//textarea[@id='description']", "资金用途修改")
			sleep(2)
			
			# 点击保存按钮
			click("xpath", "//span[text()='保存']")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("主承销商，修改成功！")
			time.sleep(3)
			
			# 测试失效功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入‘主承销商’的iframe窗体
			switch_to("xpath", "//iframe[@id='bondconsignee-tab-iframe']")
			# 刷新勾选数据
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
			sleep(1)
			
			# 点击失效按钮
			click("xpath", "//span[text()='失效']")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'失效成功！')]")
			print("资金用途，失效成功！")
			time.sleep(3)
			
			# 测试生效功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入‘主承销商’的iframe窗体
			switch_to("xpath", "//iframe[@id='bondconsignee-tab-iframe']")
			# 刷新勾选数据
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
			sleep(1)
			
			# 点击生效按钮
			click("xpath", "//span[text()='生效']")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'生效成功！')]")
			print("主承销商，生效成功！")
			
			# 点击基础设置菜单
			click("xpath", "//li[@f_value='bondissuancesetting']/descendant-or-self::*[5]")
			time.sleep(3)
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("资金用途失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
			
		
		# 测试注册登记💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
		try:
			logger.info("开始测试->债券发行管理->注册登记")
			# 点击注册登记
			click("xpath", "//span[text()='注册登记']")
			# 退出所有iframe窗体
			switch_default()
			#测试新增功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			for i in range(1,4):
				# 切入‘注册登记’的iframe窗体
				switch_to("xpath", "//iframe[@id='bondregister-tab-iframe']")
				# 用JS的方法点击新增按钮
				js_click("xpath", "//span[text()='新增']")
				sleep(1)
				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='addWin-iframe']")
	
				# 输入注册编码
				BM=str(time.strftime("%Y%m%d%H%M%S"))+"ZCBM"
				input("xpath", "//input[@name='code']",BM)
				sleep(2)
				
				#境内外
				input("xpath", "//input[@id='combobox-input-consigneetype']", "境内")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-consigneetype']")
				input_enter("xpath", "//input[@id='combobox-input-consigneetype']")
				sleep(1)
				
				# 选择监管机构
				click("xpath", "//input[@id='combobox-input-registerorg']")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-registerorg']")
				input_enter("xpath", "//input[@id='combobox-input-registerorg']")
				sleep(1)
				
				#公募私募
				click("xpath", "//input[@id='combobox-input-issuetype']")
				sleep(1)
				click("xpath",'//*[@id="f-combo-issuetype-list-0"]/div[1]')
				sleep(1)
				click("xpath", "//input[@id='combobox-input-issuetype']")
				sleep(1)
				
				# 注册品种
				click("xpath", "//input[@id='combobox-input-varietys']")
				sleep(1)
				click("xpath",'//*[@id="varietys-combogrid-body-table"]/tbody/tr[1]/td[2]/div/button')
				sleep(1)
				click("xpath", "//input[@id='combobox-input-varietys']")
				sleep(1)
				
				#注册额度
				clear("xpath", "//input[@id='amount-input']")
				sleep(1)
				input("xpath", "//input[@id='amount-input']", "5000")
				sleep(1)
				
				#注册币种
				input("xpath", "//input[@id='combobox-input-currencyid']", "CNY-人民币")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-currencyid']")
				input_enter("xpath", "//input[@id='combobox-input-currencyid']")
				sleep(1)
				
				#批文文号
				PWWH = time.strftime("%Y%m%d%H%M%S")
				input("xpath", "//input[@id='registerapproval']", str(PWWH))
				sleep(1)
				
				# 输入批文下发日
				today = date.today()
				input("xpath", "//input[@id='approvaldate-input']", str(today))
				# 模拟回车键
				
				
				# 输入额度生效日
				click("xpath", "//input[@id='begindate-input']")
				sleep(1)
				input("xpath", "//input[@id='begindate-input']", str(today))
				sleep(1)
				# 模拟回车键
				
				
				# 输入额度到期日
				today2 = today + timedelta(days=730)
				click("xpath", "//input[@id='enddate-input']")
				sleep(1)
				input("xpath", "//input[@id='enddate-input']", str(today2))
				sleep(1)
				
				
				
				# 点击保存按钮
				click("xpath", "//span[text()='保存']")
				sleep(1)
				# 退出所有iframe窗体
				switch_default()
				
				# 用隐式等待方法等页面出现提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				if i ==3 :
					print("注册登记，新增成功")
				time.sleep(2)
				
			#测试修改功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入‘注册登记’的iframe窗体
			switch_to("xpath", "//iframe[@id='bondregister-tab-iframe']")
			#刷新勾选数据
			click("xpath",'//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath",'//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
			sleep(1)
			
			# 点击修改按钮
			click("xpath", "//span[text()='修改']")
			sleep(1)
			# 切入修改的iframe窗体
			switch_to("xpath", "//iframe[@id='modWin-iframe']")
			
			# 增信措施输入新内容
			input("xpath", "//textarea[@id='addcreditmeasures']", "个人信用")
			sleep(1)
			# 点击保存按钮
			click("xpath", "//span[text()='保存']")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("注册登记，修改成功！")
			time.sleep(3)
			
			# 测试删除功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入‘注册登记’的iframe窗体
			switch_to("xpath", "//iframe[@id='bondregister-tab-iframe']")
			# 刷新勾选数据
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
			sleep(1)
			
			# 点击删除按钮
			click("xpath", "//span[text()='删除']")
			sleep(1)
			# 点击弹出框的OK键
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'删除债券注册合同成功')]")
			print("注册登记，删除成功！")
			time.sleep(3)
			
			# 测试作废功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入‘注册登记’的iframe窗体
			switch_to("xpath", "//iframe[@id='bondregister-tab-iframe']")
			# 刷新勾选数据
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
			sleep(1)
			
			# 点击作废按钮
			click("xpath", "//span[text()='作废']")
			sleep(1)
			# 点击弹出框的OK键
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'作废债券注册合同成功')]")
			print("注册登记，作废成功！")
			time.sleep(3)
			
			# 测试审核、取消审核功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入‘注册登记’的iframe窗体
			switch_to("xpath", "//iframe[@id='bondregister-tab-iframe']")
			# 刷新勾选数据
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
			sleep(1)
			
			# 点击审核按钮
			click("xpath", "//span[text()='审核']")
			sleep(1)
			# 点击弹出框的OK键
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'审批债券注册合同成功')]")
			print("注册登记，审核成功！")
			time.sleep(3)
			
			#撤销审核
			# 切入‘注册登记’的iframe窗体
			switch_to("xpath", "//iframe[@id='bondregister-tab-iframe']")
			# 刷新勾选数据
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
			sleep(1)
			
			# 用JS方便点击‘审核’按钮旁边的倒三角形
			js_click("xpath", "//span[text()='审核']/parent::*/following-sibling::*/child::*")
			sleep(1)
			
			# 点击取消审核按钮
			js_click("xpath", "//a[contains(text(),'取消审核')]")
			sleep(1)
			
			# 点击弹出框的OK键
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'取消审核债券注册合同成功')]")
			print("注册登记，取消审核成功！")
			time.sleep(3)
			
			# 测试变更功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入‘注册登记’的iframe窗体
			switch_to("xpath", "//iframe[@id='bondregister-tab-iframe']")
			# 刷新勾选数据
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
			sleep(1)
			
			# 点击审核按钮
			click("xpath", "//span[text()='审核']")
			sleep(1)
			# 点击弹出框的OK键
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现的提示框
			implici_wait("xpath", "//span[contains(text(),'审批债券注册合同成功')]")
			time.sleep(3)
			
			# 切入‘注册登记’的iframe窗体
			switch_to("xpath", "//iframe[@id='bondregister-tab-iframe']")
			# 刷新勾选数据
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
			sleep(1)
			
			# 点击变更按钮
			click("xpath", "//span[text()='变更']")
			
			# 切入修改的iframe窗体
			switch_to("xpath", "//iframe[@id='modWin-iframe']")
			sleep(1)
			
			# 增信措施输入新内容
			input("xpath", "//textarea[@id='addcreditmeasures']", "诚实小郎君")
			sleep(1)
			
			# 点击保存按钮
			click("xpath", "//span[text()='保存']")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("注册登记，变更成功！")
			time.sleep(3)
			
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("注册登记失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
			
		
		
		#配置自定义字段，以及利率方案💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
		#  系统设置里面设置自定义字段
		try:
			logger.info("开始配置自定义字段")
			# 点击系统设置
			click("xpath", "//div[@class='sysconfigset']")
			sleep(1)
			# 点击进入系统设置页面
			switch_to("xpath", "//iframe[@id='systemconfig-tab-iframe']")
			# 将页面的滚动条滑动到‘自定义字段’页面的地方
			js_gd("xpath", "//span[contains(text(),'自定义字段')]")
			# 用JS的方法点击自定义字段菜单按钮
			js_click("xpath", "//span[contains(text(),'自定义字段')]")
			sleep(1)
			switch_default()
			switch_to("xpath", "//iframe[@id='custom-tab-iframe']")
			# 切入自定义字段的iframe窗体
			switch_to("xpath", "//iframe[@id='subTabOne-iframe']")
			sleep(1)
			# 点击查看
			# 用JS的方法点击放大镜
			js_click("xpath", "//span[@class='f-contrac-close']")
			sleep(1)
			# 输入内容
			input("xpath", "//input[@id='tablecomment']", "债券发行登记扩展表")
			sleep(1)
			# 点击查询
			click("xpath", "//span[text()='查询']")
			sleep(1)
			# 点击选择
			click("xpath", "//div[@title='扩展表说明:债券发行登记扩展表']/parent::*[1]/preceding-sibling::*[2]/descendant::*[2]")
			sleep(1)
			
			click("xpath", "//span[text()='配置']")
			sleep(1)
			
			# 进入iframe 窗体
			switch_to("xpath", "//iframe[@id='modWin-iframe']")
			# 点击新增行
			click("xpath", "//span[text()='新增行']")
			sleep(1)
			
			# 输入排序号
			input("xpath", "//input[@id='customformfieldconfig-displayorder-0-input']", "1")
			sleep(1)
			
			# 选择字段名称
			click("xpath", "//input[@id='combobox-input-customformfieldconfig-fieldname-0']")
			sleep(1)
			input_down("xpath",'//*[@id="combobox-input-customformfieldconfig-fieldname-0"]')
			input_enter("xpath",'//*[@id="combobox-input-customformfieldconfig-fieldname-0"]')
			sleep(1)
			
			# 选择字段类型
			click("xpath", "//input[@id='combobox-input-customformfieldconfig-fieldtype-0']")
			sleep(1)
			click("xpath", "//div[@title='文本']")
			sleep(1)
			# 输入字段显示名称
			input("xpath", "//input[@id='customformfieldconfig-fieldcomment-0']", "债券发行人")
			sleep(1)
			
			# 是否必填
			click("xpath", "//input[@id='combobox-input-customformfieldconfig-isrequired-0']")
			sleep(1)
			# 选择必填
			click("xpath", "//div[@title='×']")
			sleep(1)
			click("xpath", "//span[text()='保存']")
			sleep(1)
			switch_default()
			
			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功')]")
			print("债券发行登记拓展表，新增成功！")
			time.sleep(3)
			
			#----------创建债券发行利率方案----------
			# 点击系统设置
			logging.info("开始创建债券发行->利率方案")
			click("xpath", "//div[@class='sysconfigset']")
			sleep(1)
			# 点击进入系统设置页面
			switch_to("xpath", "//iframe[@id='systemconfig-tab-iframe']")
			# 将页面的滚动条滑动到‘利率方案’页面的地方
			js_gd("xpath", "//span[contains(text(),'利率方案')]")
			# 用JS的方法利率方案字段菜单按钮
			js_click("xpath", "//span[contains(text(),'利率方案')]")
			sleep(1)
			switch_default()
			switch_to("xpath", "//iframe[@id='interestRateSchemes-tab-iframe']")
			# 用JS的方法点击新增按钮
			js_click("xpath", "//span[text()='新增']")
			sleep(1)
			# 切入新增的iframe窗体
			switch_to("xpath", "//iframe[@id='addWin-iframe']")
			sleep(1)
			
			# 输入代码
			DM="LV"+str(random.randint(1,100))
			input("xpath", "//input[@name='code']", DM)
			sleep(1)
			
			# 输入名称
			LV_name="债券发行"+str(random.randint(1,100))
			input("xpath", "//input[@id='name']", LV_name)
			sleep(1)
			# 单据对象
			click("xpath", "//input[@id='combobox-input-noteobjectid']")
			sleep(1)
			input("xpath", "//input[@id='combobox-input-noteobjectid']", "ZQFX-债券发行")
			sleep(1)
			input_enter("xpath", "//input[@id='combobox-input-noteobjectid']")
			sleep(1)
			input_down("xpath", "//input[@id='combobox-input-noteobjectid']")
			sleep(1)
			input_enter("xpath", "//input[@id='combobox-input-noteobjectid']")
			sleep(1)
			# 利率类型
			click("xpath", "//input[@id='combobox-input-interestratetypeid']")
			sleep(1)
			input("xpath", "//input[@id='combobox-input-interestratetypeid']", "固定利率")
			sleep(1)
			input_enter("xpath", "//input[@id='combobox-input-interestratetypeid']")
			sleep(1)
			input_down("xpath", "//input[@id='combobox-input-interestratetypeid']")
			sleep(1)
			input_enter("xpath", "//input[@id='combobox-input-interestratetypeid']")
			sleep(1)
			
			# 共享模式combobox-input-includemode
			click("xpath", "//input[@id='combobox-input-includemode']")
			sleep(1)
			input("xpath", "//input[@id='combobox-input-includemode']", "下属组织共享")
			sleep(1)
			input_enter("xpath", "//input[@id='combobox-input-includemode']")
			sleep(1)
			input_down("xpath", "//input[@id='combobox-input-includemode']")
			sleep(1)
			input_enter("xpath", "//input[@id='combobox-input-includemode']")
			sleep(1)
			
			# 点击保存按钮
			click("xpath", "//span[text()='保存']")
			
			# 退出所有iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("利率方案，保存成功！")
			time.sleep(3)
			
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("自定义字段+利率方案,失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)

		# 测试发行登记💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
		try:
			logger.info("开始测试->债券发行管理->发行登记")
			# 点击发行登记
			click("xpath", "//span[text()='发行登记']")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			

			#测试新增功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			for i in range(1, 6):
				# 切入‘发行登记’的iframe窗体
				switch_to("xpath", "//iframe[@id='bondissuance-tab-iframe']")
				
				# 用JS的方法点击新增按钮
				js_click("xpath", "//span[text()='新增']")
				sleep(1)
				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='addWin-iframe']")
				
				# 选择注册编码
				# 点击‘注册编码’框
				click("xpath", "//input[@id='combobox-input-bondregisterid']")
				sleep(1)
				click("xpath",'//*[@id="bondregisterid-combogrid-body-table"]/tbody/tr[1]/td[2]/div')
				sleep(1)
				
				
				# 输入债券代码
				ZQDM = time.strftime("%Y%m%d%H%M%S")
				input("xpath", "//input[@id='code']", "Test" + str(ZQDM))
				sleep(2)
				
				# 输入债券全称
				name = "中国债券"+str(time.strftime("%H%M%S"))
				input("xpath", "//input[@id='name']", name)
				sleep(1)
				
				# 输入债券简称
				name2 = "国券" + str(time.strftime("%H%M%S"))
				input("xpath", "//input[@id='simplename']", name2)
				time.sleep(1)
				
				#输入发行日期
				RQ=str(date.today())
				input("xpath",'//*[@id="issuancedate-input"]' ,RQ)
				sleep(1)
				
				
				#输入起息日
				click("xpath",'//*[@id="initintereststartdate-input"]')
				sleep(1)
				input("xpath", '//*[@id="initintereststartdate-input"]', RQ)
				sleep(1)
				
				
				#本次行权日
				click("xpath", '//*[@id="enddate-input"]')
				sleep(1)
				input("xpath", '//*[@id="enddate-input"]', RQ)
				sleep(1)
				
				
				#法定到期日
				click("xpath",'//*[@id="legalenddate-input"]')
				sleep(1)
				DQR=str(date.today() + timedelta(days=60))
				input("xpath",'//*[@id="legalenddate-input"]',DQR)
				sleep(1)
				
				#发行期限
				clear("xpath",'//*[@id="termday-input"]')
				sleep(1)
				input("xpath",'//*[@id="termday-input"]','60')
				
				
				
				#发行金额
				input("xpath",'//*[@id="amount-input"]',"500")
				sleep(2)
				
				#计息方式-------------
				js_gd("xpath", "//span[contains(text(),'计息方式')]")
				#click("xpath", "//span[contains(text(),'计息方式')]")
				sleep(1)
				
				click("xpath",'//*[@id="memo"]')
				sleep(1)
				#还本方式
				click("xpath",'//*[@id="combobox-input-repaymode"]')
				sleep(1)
				click("xpath",'//*[@id="f-combo-repaymode-list-0"]')
				sleep(1)
				#还息方式
				click("xpath",'//*[@id="combobox-input-interestmode"]')
				sleep(1)
				click("xpath",'//*[@id="f-combo-interestmode-list-0"]')
				sleep(1)
				#利率方案
				click("xpath",'//*[@id="combobox-input-interestrateschemeid"]')
				sleep(1)
				input_down("xpath",'//*[@id="combobox-input-interestrateschemeid"]')
				sleep(1)
				input_enter("xpath",'//*[@id="combobox-input-interestrateschemeid"]')
				sleep(1)
				
				# 点击保存按钮
				click("xpath", "//span[text()='保存']")
				sleep(1)
				# 退出所有iframe窗体
				switch_default()
				# 用隐式等待方法等页面出现提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				if i ==4 :
					print("发行登记，新增成功")
				time.sleep(3)
			
			
			#测试修改功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入‘发行登记’的iframe窗体
			switch_to("xpath", "//iframe[@id='bondissuance-tab-iframe']")
			
			#刷新
			click("xpath",'//*[@id="gridbar-page-refresh"]')
			sleep(1)
			#点击单据号使其按照做些最新顺序排列
			span_click("单据号")
			sleep(1)
			#勾选按钮
			click("xpath",'//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			#点击修改按钮
			span_click("修改")
			sleep(1)
			#切入窗体
			switch_to("xpath",'//*[@id="modWin-iframe"]')
			input("xpath",'//*[@id="addcreditmeasures"]','中国信用')
			sleep(2)
			#点击保存
			span_click("保存")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("发行登记，修改成功！")
			time.sleep(3)
			
			# 测试删除功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入‘发行登记’的iframe窗体
			switch_to("xpath", "//iframe[@id='bondissuance-tab-iframe']")
			# 刷新
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			# 勾选按钮
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			# 点击删除按钮
			click("xpath", "//span[text()='删除']")
			sleep(1)
			# 点击弹出框的OK键
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'成功删除1条记录！')]")
			print("发行登记，删除成功！")
			logging.info("发行登记，删除成功！")
			time.sleep(3)
			
			
			# 测试审核、撤销审核功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入‘发行登记’的iframe窗体
			switch_to("xpath", "//iframe[@id='bondissuance-tab-iframe']")
			# 刷新
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			
			# 勾选按钮
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			# 点击审核按钮
			click("xpath", "//span[text()='审核']")
			sleep(1)
			# 点击弹出框的OK键
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'成功审核1条记录')]")
			print("发行登记，审核成功！")
			time.sleep(3)
			
			# 取消审核
			# 切入‘发行登记’的iframe窗体
			switch_to("xpath", "//iframe[@id='bondissuance-tab-iframe']")
			# 刷新
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			# 勾选按钮
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			# 用JS方便点击‘审核’按钮旁边的倒三角形
			js_click("xpath", "//span[text()='审核']/parent::*/following-sibling::*/child::*")
			sleep(1)
			# 点击取消审核按钮
			js_click("xpath", "//a[contains(text(),'取消审核')]")
			sleep(1)
			# 点击弹出框的OK键
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'成功取消审核:1条')]")
			print("发行登记，取消审核成功！")
			time.sleep(3)
			
			# 测试变更功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入‘发行登记’的iframe窗体
			switch_to("xpath", "//iframe[@id='bondissuance-tab-iframe']")
			# 刷新
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			# 勾选按钮
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			# 点击审核按钮
			click("xpath", "//span[text()='审核']")
			sleep(1)
			# 点击弹出框的OK键
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
			sleep(3)
			
			# 刷新
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			# 勾选按钮
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			# 点击变更按钮
			click("xpath", "//span[text()='变更']")
			sleep(1)
			#切入窗体
			switch_to("xpath",'//*[@id="modWin-iframe"]')
			input("xpath",'//*[@id="addcreditmeasures"]','中国增信')
			sleep(2)
			span_click("保存")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("发行登记，变更成功！")
			time.sleep(3)
			
			# 测试作废功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入‘发行登记’的iframe窗体
			switch_to("xpath", "//iframe[@id='bondissuance-tab-iframe']")
			# 刷新
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			# 勾选按钮
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			# 点击作废按钮
			click("xpath", "//span[text()='作废']")
			sleep(1)
			# 点击弹出框的OK键
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'成功作废1条记录！')]")
			print("发行登记，作废成功！")
			time.sleep(3)
			
			# 测试资金到账功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入‘发行登记’的iframe窗体
			switch_to("xpath", "//iframe[@id='bondissuance-tab-iframe']")
			# 刷新
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			# 勾选按钮
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			# 点击审核按钮
			click("xpath", "//span[text()='审核']")
			sleep(1)
			# 点击弹出框的OK键
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
			sleep(3)
			
			#资金到账
			# 刷新#,勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			#点击资金到账
			span_click("资金到账")
			sleep(1)
			switch_to("xpath",'//*[@id="accountWin-iframe"]')
			#输入到账金额
			input("xpath",'//*[@id="amount-input"]','100')
			sleep(2)
			span_click("保存")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("发行登记，资金到账成功！")
			time.sleep(3)
			
			# 测试取消到账功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入‘发行登记’的iframe窗体
			switch_to("xpath", "//iframe[@id='bondissuance-tab-iframe']")
			# 刷新
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			# 勾选按钮
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			# 用JS方便点击‘资金到账’按钮旁边的倒三角形
			js_click("xpath", "//span[text()='资金到账']/parent::*/following-sibling::*/child::*")
			sleep(1)
			# 点击取消到账按钮
			js_click("xpath", "//a[contains(text(),'取消到账')]")
			sleep(1)
			
			# 切入取消到账的窗体页面
			switch_to("xpath", "//iframe[@id='cancelAccountWin-iframe']")
			# 点击勾选当前资金到账的数据
			click("xpath", '//*[@id="loanlend-body-table"]/tbody/tr/td[2]/div/button')
			sleep(1)
			# 点击取消到账
			click("xpath", "//span[text()='取消到账']")
			sleep(1)
			# 点击弹出框的OK键
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'成功取消:1条记录！')]")
			print("发行登记，取消到账成功！")
			sleep(3)
			#退出
			# 切入资金到账的iframe窗体
			switch_to("xpath", "//iframe[@id='bondissuance-tab-iframe']")
			sleep(1)
			# 点击关闭取消到账的关闭按钮
			click("xpath", "//span[text()='到账取消']/preceding-sibling::*[1]")
			sleep(1)
			switch_default()
			
			# 测试生成到账交易单功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入‘发行登记’的iframe窗体
			switch_to("xpath", "//iframe[@id='bondissuance-tab-iframe']")
			# 刷新
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			# 勾选按钮
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			# 资金到账
			# 刷新#,勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			# 点击资金到账
			span_click("资金到账")
			sleep(1)
			switch_to("xpath", '//*[@id="accountWin-iframe"]')
			# 输入到账金额
			input("xpath", '//*[@id="amount-input"]', '100')
			sleep(2)
			span_click("保存")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			
			
			#生成到账交易单===============
			# 切入‘发行登记’的iframe窗体
			switch_to("xpath", "//iframe[@id='bondissuance-tab-iframe']")
			
			# 刷新
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			# 勾选按钮
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			# 用JS方便点击‘资金到账’按钮旁边的倒三角形
			js_click("xpath", "//span[text()='资金到账']/parent::*/following-sibling::*/child::*")
			sleep(1)
			# 点击生成到账交易单
			js_click("xpath", "//a[contains(text(),'生成到账交易单')]")
			sleep(1)
			#切入生成到账交易单窗体
			switch_to("xpath",'//*[@id="genRecWin-iframe"]')
			
			#勾选记录
			click("xpath",'//*[@id="loanlend-body-table"]/tbody/tr/td[2]/div/button')
			sleep(1)
			#点击下一步
			span_click("下一步")
			sleep(1)
			switch_parent()
			#切入三层窗体
			switch_to("xpath",'//*[@id="addRecWin-iframe"]')
			#交易类型
			input("xpath",'//*[@id="combobox-input-paytypeid"]','201-外部收款')
			sleep(2)
			click("xpath",'//*[@id="paytypeid-combogrid-body-table"]/tbody/tr/td[2]/div')
			sleep(1)
			
			#收方账户
			click("xpath",'//*[@id="combobox-input-ourbankaccountid"]')
			sleep(1)
			input_down("xpath",'//*[@id="combobox-input-ourbankaccountid"]')
			input_enter("xpath",'//*[@id="combobox-input-ourbankaccountid"]')
			sleep(1)
			
			#复方名称
			input("xpath",'//*[@id="combobox-input-oppcounterpartyid"]','浙江华语科技')
			sleep(2)
			double_click("xpath",'//*[@id="combobox-input-oppcardtype"]')
			sleep(1)
			
			#付方账户
			input("xpath", '//*[@id="combobox-input-oppcounterpartyaccountid"]', '200848782767819')
			sleep(2)
			double_click("xpath", '//*[@id="combobox-input-oppcardtype"]')
			sleep(1)
			
			
			#用途，便于修改数据库
			input("xpath", '//*[@id="combobox-input-purpose"]', '发行登记交易单')
			sleep(2)
			
			#保存
			span_click("保存")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("发行登记，生成到账交易单成功！")
			time.sleep(3)
			
			#到收款处理页面进行收款💨💨💨💨💨💨💨💨💨
			js_click("xpath", "//span[contains(text(),'债券发行管理')]")
			sleep(1)
			js_gd("xpath", "//span[contains(text(),'资金结算管理')]")
			# 用JS的方法点击资金结算管理菜单按钮
			js_click("xpath", "//span[contains(text(),'资金结算管理')]")
			sleep(1)
			# 点击'资金系统收付'菜单
			click("xpath", "//span[text()='资金系统收付']")
			sleep(1)
			# 点击收款处理菜单
			click("xpath", "//span[text()='收款处理']")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			#确认收款💨💨💨💨💨💨💨💨💨
			# 切入‘银行账户收款’的iframe窗体
			switch_to("xpath", "//iframe[@id='generalRecment-tab-iframe']")
			# 进入银行账户收款的iframe窗体
			switch_to("xpath", "//iframe[@id='subTabEight-iframe']")
			# 刷新，勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
			sleep(1)
			# 点击确认收款按钮
			click("xpath", "//span[text()='确认收款']")
			sleep(1)
			# 点击确定
			click("xpath", "//span[text()='确定']")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			time.sleep(3)
			#回到债券发行页面💨💨💨💨💨💨💨💨💨
			js_gd("xpath", "//span[contains(text(),'债券发行管理')]")
			# 用JS的方法点击债券发行管理菜单按钮
			js_click("xpath", "//span[contains(text(),'债券发行管理')]")
			sleep(1)
			span_click("发行登记")
			sleep(1)
			

			#承兑功能测试开始===============
			# 切入‘发行登记’的iframe窗体
			switch_to("xpath", "//iframe[@id='bondissuance-tab-iframe']")
			# 刷新
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			# 点击单据号使其按照做些最新顺序排列
			span_click("单据号")
			sleep(1)
			# 勾选按钮
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			#点击兑付按钮
			span_click("兑付")
			sleep(1)
			#切入到兑付窗体
			switch_to("xpath",'//*[@id="bondredeemsWin-iframe"]')
			#兑付本金
			clear("xpath",'//*[@id="capital-input"]')
			sleep(1)
			input("xpath",'//*[@id="capital-input"]','10')
			sleep(2)
			span_click("保存")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("发行管理，承兑成功")
			sleep(3)
			
			# 测试付息功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入‘发行登记’的iframe窗体
			switch_to("xpath", "//iframe[@id='bondissuance-tab-iframe']")
			# 刷新
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			# 勾选按钮
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			#点击兑付旁边三角
			click("xpath","//span[text()='兑付']/parent::*/following-sibling::*/child::*")
			sleep(1)
			js_click("xpath", "//a[contains(text(),'付息')]")
			sleep(1)
			#切入付息窗体
			switch_to("xpath",'//*[@id="bondredeemsWin-iframe"]')
			sleep(1)
			#兑付利息
			clear("xpath",'//*[@id="interest-input"]')
			sleep(2)
			input("xpath",'//*[@id="interest-input"]','1')
			sleep(2)
			span_click("保存")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("发行管理，付息成功")
			sleep(3)
			
			# 测试重新生成还本付息功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入‘发行登记’的iframe窗体
			switch_to("xpath", "//iframe[@id='bondissuance-tab-iframe']")
			# 刷新
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			# 勾选按钮
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			#点击还本付息
			span_click("重新生成还本付息")
			sleep(1)
			#点击ok
			click("xpath",'//*[@id="f-message-webgen-0-okBnt"]')
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'成功重新计息:1条！')]")
			print("发行管理，重新生成还本付息成功")
			sleep(3)
			
			
			# 测试债券替换功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入‘发行登记’的iframe窗体
			switch_to("xpath", "//iframe[@id='bondissuance-tab-iframe']")
			
			# 刷新
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			# 勾选按钮
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[2]/td[2]/div/button')
			sleep(1)
			
			# 点击审核按钮
			click("xpath", "//span[text()='审核']")
			sleep(1)
			# 点击弹出框的OK键
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
			sleep(3)
			
			# 刷新
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			# 勾选按钮
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[2]/td[2]/div/button')
			sleep(1)
			
			# 转股之前进行资金到账
			# 点击资金到账
			span_click("资金到账")
			sleep(1)
			switch_to("xpath", '//*[@id="accountWin-iframe"]')
			# 输入到账金额
			input("xpath", '//*[@id="amount-input"]', '100')
			sleep(2)
			span_click("保存")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			time.sleep(3)
			
			# 切入‘发行登记’的iframe窗体
			switch_to("xpath", "//iframe[@id='bondissuance-tab-iframe']")
			# 刷新
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			# 勾选按钮
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[2]/td[2]/div/button')
			sleep(1)
			span_click("债券替换")
			sleep(1)
			#切入窗体
			switch_to("xpath",'//*[@id="modWin-iframe"]')
			#债券代码
			THCD=str(time.strftime("%Y%m%d%H%M%S"))
			input("xpath",'//*[@id="code"]',THCD)
			sleep(2)
			
			#债券全称
			input("xpath",'//*[@id="name"]','替换债券')
			sleep(1)
			
			#债券简称
			input("xpath",'//*[@id="simplename"]','替换简称')
			sleep(1)
			
			#发行金额
			clear("xpath",'//*[@id="amount-input"]')
			sleep(1)
			input("xpath",'//*[@id="amount-input"]','500')
			sleep(2)
			#保存
			span_click("保存")
			sleep(1)
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("发行管理，债券替换成功")
			sleep(3)
			
			# 测试债券转股功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入‘发行登记’的iframe窗体
			switch_to("xpath", "//iframe[@id='bondissuance-tab-iframe']")
			# 刷新
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			
			# 勾选按钮
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[4]/td[2]/div/button')
			sleep(1)
			
			# 点击审核按钮
			click("xpath", "//span[text()='审核']")
			sleep(1)
			# 点击弹出框的OK键
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
			sleep(3)
			
			# 刷新
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			# 勾选按钮
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[4]/td[2]/div/button')
			sleep(1)
			
			#转股之前进行资金到账
			# 点击资金到账
			span_click("资金到账")
			sleep(1)
			switch_to("xpath", '//*[@id="accountWin-iframe"]')
			# 输入到账金额
			input("xpath", '//*[@id="amount-input"]', '100')
			sleep(2)
			span_click("保存")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			time.sleep(3)
			
			# 切入‘发行登记’的iframe窗体
			switch_to("xpath", "//iframe[@id='bondissuance-tab-iframe']")
			# 刷新
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			# 勾选按钮
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[4]/td[2]/div/button')
			sleep(1)
			#点击债券转股
			span_click("债券转股")
			sleep(1)
			click("xpath",'//*[@id="f-message-webgen-0-okBnt"]')
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'成功转股:1条！')]")
			print("发行登记，转股成功")
			time.sleep(3)
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("发行登记失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		
		
		# 测试注册登记查看💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
		try:
			logger.info("开始测试->债券发行管理->注册登记查看")
			# 点击基础设置菜单
			click("xpath", "//span[text()='注册登记查看']")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			
			#切入查看窗体
			switch_to("xpath",'//*[@id="bondregisterview-tab-iframe"]')
			js_click("xpath",'//*[@id="north"]/div[2]/span')
			sleep(1)
			span_click("查询")
			switch_default()
			print("注册登记查看成功")
			sleep(3)
		
			
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("注册登记查看失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
			
		
		# 测试发行登记查看💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
		try:
			logger.info("开始测试->债券发行管理->注册登记查看")
			# 点击基础设置菜单
			click("xpath", "//span[text()='发行登记查看']")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			
			# 切入查看窗体
			switch_to("xpath", '//*[@id="bondissuanceview-tab-iframe"]')
			js_click("xpath", '//*[@id="north"]/div[2]/span')
			sleep(1)
			span_click("查询")
			print("发行登记查看成功")
			switch_default()
			sleep(3)
		
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("发行登记查看失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		
		
		# 测试债券兑付申请💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
		try:
			logger.info("开始测试->债券发行管理->债券兑付申请")
			# 点击基础设置菜单
			click("xpath", "//span[text()='债券兑付申请']")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			
			# 测试新增功能===========================================================
			for i in range(1,2):
				# 切入债券兑付申请窗体
				switch_to("xpath", '//*[@id="bondredeemsapply-tab-iframe"]')
				span_click("新增")
				sleep(1)
				# 切入新增窗体
				switch_to("xpath", '//*[@id="modWin-iframe"]')
				
				# 债券代码
				click("xpath", '//*[@id="combobox-input-bondissuancesid"]')
				sleep(1)
				input_down("xpath", '//*[@id="combobox-input-bondissuancesid"]')
				sleep(1)
				input_enter("xpath", '//*[@id="combobox-input-bondissuancesid"]')
				sleep(1)
				
				# 兑付分类
				click("xpath", '//*[@id="combobox-input-redeemtypeid"]')
				sleep(1)
				input_enter("xpath", '//*[@id="combobox-input-redeemtypeid"]')
				sleep(1)
				
				span_click("下一步")
				sleep(1)
				
				# 切入窗体
				switch_to("xpath", '//*[@id="bondredeemsWin-iframe"]')
				#金额
				clear("xpath", '//*[@id="capital-input"]')
				sleep(1)
				input("xpath", '//*[@id="capital-input"]', '5')
				sleep(1)
				
				#其他费用

				input("xpath", '//*[@id="title"]', '风')
				sleep(1)
				
				span_click("保存")
				sleep(1)
				# 退出所有iframe窗体
				switch_default()
				# 用隐式等待方法等页面出现新增成功的提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				if i ==3:
					print("债券发行管理，新增成功")
				time.sleep(3)
			
			# 测试修改功能===========================================================
			# 切入债券兑付申请窗体
			switch_to("xpath", '//*[@id="bondredeemsapply-tab-iframe"]')
			#刷新，勾选按钮
			click("xpath",'//*[@id="gridbar-page-refresh"]')
			sleep(1)
			span_click("标题")
			sleep(1)
			span_click("标题")
			sleep(1)
			click("xpath",'//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			#点击修改
			span_click("修改")
			sleep(1)
			switch_to("xpath",'//*[@id="modWin-iframe"]')
			input("xpath",'//*[@id="description"]','测试修改')
			sleep(1)
			span_click("保存")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("债券发行管理，修改成功")
			time.sleep(3)
			
			# 测试删除功能===========================================================
			# 切入债券兑付申请窗体
			switch_to("xpath", '//*[@id="bondredeemsapply-tab-iframe"]')
			# 刷新，勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			# 点击删除
			span_click("删除")
			sleep(1)
			#点击ok
			click("xpath",'//*[@id="f-message-webgen-0-okBnt"]')
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'债券发行兑付成功删除:1条！')]")
			print("债券发行管理，删除成功")
			time.sleep(3)
			
			# 测试送审、撤销送审功能===========================================================
			# 切入债券兑付申请窗体
			switch_to("xpath", '//*[@id="bondredeemsapply-tab-iframe"]')
			# 刷新，勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			#点击送审
			span_click("送审")
			sleep(1)
			#点击ok
			click("xpath",'//*[@id="f-message-webgen-0-okBnt"]')
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'送审成功！')]")
			print("债券发行管理，送审成功")
			time.sleep(3)
			
			#测试撤销送审===============
			# 切入债券兑付申请窗体
			switch_to("xpath", '//*[@id="bondredeemsapply-tab-iframe"]')
			# 刷新，勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			triangle_cick("送审")
			sleep(1)
			js_click("xpath", "//a[contains(text(),'撤销送审')]")
			sleep(1)
			# 点击ok
			click("xpath", '//*[@id="f-message-webgen-0-okBnt"]')
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'撤销送审成功！')]")
			print("债券发行管理，撤销送审成功")
			time.sleep(3)
			
			# 测试变更功能===========================================================
			# 切入债券兑付申请窗体
			switch_to("xpath", '//*[@id="bondredeemsapply-tab-iframe"]')
			# 刷新，勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			# 点击送审
			span_click("送审")
			sleep(1)
			# 点击ok
			click("xpath", '//*[@id="f-message-webgen-0-okBnt"]')
			sleep(1)
			time.sleep(3)
			#二审
			double_click("xpath",'//*[@id="grid-body-table"]/tbody/tr[1]/td[3]/div')
			sleep(1)
			switch_to("xpath",'//*[@id="wf_taskProcessing_win-iframe"]')
			span_click("同意")
			sleep(3)
			switch_parent()
			
			#三审
			double_click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[3]/div')
			sleep(1)
			switch_to("xpath", '//*[@id="wf_taskProcessing_win-iframe"]')
			span_click("同意")
			sleep(3)
			switch_parent()
			
			# 刷新，勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("变更")
			sleep(1)
			switch_to("xpath",'//*[@id="modWin-iframe"]')
			input("xpath",'//*[@id="description"]','张中国')
			sleep(1)
			span_click("保存")
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("债券发行管理，变更成功")
			time.sleep(3)
			
			# 测试生成交易单功能===========================================================
			# 切入债券兑付申请窗体
			switch_to("xpath", '//*[@id="bondredeemsapply-tab-iframe"]')
			# 刷新，勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("生成交易单")
			sleep(1)
			# 切入生成到账交易单窗体
			switch_to("xpath", '//*[@id="genRecWin-iframe"]')
			
			# 勾选记录
			click("xpath", '//*[@id="loanlend-body-table"]/tbody/tr/td[2]/div/button')
			sleep(1)
			# 点击下一步
			span_click("下一步")
			sleep(1)
			switch_parent()
			# 切入三层窗体
			switch_to("xpath", '//*[@id="addRecWin-iframe"]')
			# 交易类型
			input("xpath", '//*[@id="combobox-input-paytypeid"]', '103-对外付款')
			sleep(2)
			click("xpath", '//*[@id="paytypeid-combogrid-body-table"]/tbody/tr/td[2]/div')
			sleep(1)
			
			# 结算方式
			input("xpath", '//*[@id="combobox-input-settlementmodeid"]', '601-其他支付')
			sleep(2)
			click("xpath", '//*[@id="settlementmodeid-combogrid-body-table"]/tbody/tr/td[2]/div')
			sleep(1)
			
			# 收方账户
			click("xpath", '//*[@id="combobox-input-ourbankaccountid"]')
			sleep(1)
			input_down("xpath", '//*[@id="combobox-input-ourbankaccountid"]')
			input_enter("xpath", '//*[@id="combobox-input-ourbankaccountid"]')
			sleep(1)
			
			# 复方名称
			input("xpath", '//*[@id="combobox-input-oppcounterpartyid"]', '浙江华语科技')
			sleep(2)
			double_click("xpath", '//*[@id="combobox-input-oppcardtype"]')
			sleep(1)
			
			# 付方账户
			input("xpath", '//*[@id="combobox-input-oppcounterpartyaccountid"]', '200848782767819')
			sleep(2)
			double_click("xpath", '//*[@id="combobox-input-oppcardtype"]')
			sleep(1)
			
			# 用途，便于修改数据库
			input("xpath", '//*[@id="combobox-input-purpose"]', '发行登记交易单')
			sleep(2)
			
			# 保存
			span_click("保存")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("发行登记，生成到账交易单成功！")
			time.sleep(3)
			
			# 测试作废功能===========================================================
			# 切入债券兑付申请窗体
			switch_to("xpath", '//*[@id="bondredeemsapply-tab-iframe"]')
			# 刷新，勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[2]/td[2]/div/button')
			sleep(1)
			
			# 点击送审
			span_click("送审")
			sleep(1)
			# 点击ok
			click("xpath", '//*[@id="f-message-webgen-0-okBnt"]')
			sleep(1)
			time.sleep(3)
			# 二审
			double_click("xpath", '//*[@id="grid-body-table"]/tbody/tr[2]/td[3]/div')
			sleep(1)
			switch_to("xpath", '//*[@id="wf_taskProcessing_win-iframe"]')
			span_click("同意")
			sleep(3)
			switch_parent()
			
			# 三审
			double_click("xpath", '//*[@id="grid-body-table"]/tbody/tr[2]/td[3]/div')
			sleep(1)
			switch_to("xpath", '//*[@id="wf_taskProcessing_win-iframe"]')
			span_click("同意")
			sleep(3)
			switch_parent()
			
			# 刷新，勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[2]/td[2]/div/button')
			sleep(1)
			
			span_click("作废")
			sleep(1)
			click("xpath",'//*[@id="f-message-webgen-0-okBnt"]')
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'作废成功！')]")
			print("债券发行管理，作废成功")
			time.sleep(3)
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("债券兑付申请失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)

if __name__ == '__main__':
	#  启动单元测试
	unittest.main(verbosity=2)