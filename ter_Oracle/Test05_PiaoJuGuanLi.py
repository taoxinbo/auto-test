# encoding=utf-8
# @Time : 2020/11/02 08:30
# @Author : zzg
# 此文件是测试Oracle版本票据管理，包含基础设置，支票管理，承兑汇票管理，信用证管理，保函管理
import unittest, pytest
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


@pytest.mark.flaky(reruns=pytest_flaky, reruns_delay=10)
class Test36_WaiBiShouFuJieSuan_JNWBHK_QTZF(unittest.TestCase):
	
	# 启动浏览器
	def setUp(self):
		# 启动浏览器的另外一个方法：通过封装启动浏览器的驱动，启动不同浏览器
		self.driver = get("chrome")
	
	# 登陆系统、对系统设置进行操作
	def test_trade(self):
		
		# login(G_Ora_Url, mindy, Password, "亚唐科技")
		login(G_Ora_Url, mindy, Password, "亚唐科技")
		
		logging.info("开始测试票据管理")
		# 将页面的滚动条滑动到‘资金结算管理’页面的地方
		js_gd("xpath", "//span[contains(text(),'票据管理')]")
		# 用JS的方法点击资金结算管理菜单按钮
		js_click("xpath", "//span[contains(text(),'票据管理')]")
		sleep(1)
		# 退出所有iframe窗体
		switch_default()
		
		
		
		#测试票据管理-基础设置-支票用途💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
		try:
			logger.info("测试票据管理-基础设置-支票用途")
			#点击基础设置
			click("xpath", "//li[@f_value='billSetting']/descendant-or-self::*[5]")
			sleep(1)
			#点击支票用途
			span_click("支票用途")
			sleep(1)
			#退出所有窗口
			switch_default()


			#测试新增💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			for i in range(1,3):
				# 切入支票用途窗体
				switch_to("xpath", '//*[@id="chequePurpose-tab-iframe"]')
				#点击新增
				span_click("新增")
				sleep(1)
				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='addWin-iframe']")
				# 输入用途代码
				code = time.strftime("%Y%m%d%S")
				input("xpath", "//input[@name='code']", code)
				sleep(1)
				# 输入的支票用途
				name = "ZPYT" + str(time.strftime("%H%M%S"))
				input("xpath", "//input[@id='name']", name)
				sleep(1)
				# 点击保存按钮
				click("xpath", "//span[text()='保存']")
				sleep(1)
				# 退出所有iframe窗体
				switch_default()
				# 用隐式等待方法等页面出现新增成功的提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				print("支票用途，新增成功！")
				time.sleep(3)
				
			#测试修改💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入支票用途窗体
			switch_to("xpath", '//*[@id="chequePurpose-tab-iframe"]')
			#刷新勾选那妞
			click("xpath",'//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath",'//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
			sleep(1)
			
			span_click("修改")
			sleep(1)
			# 切入修改的iframe窗体
			switch_to("xpath", "//iframe[@id='modWin-iframe']")
			# 修改描述框中的内容
			input("xpath", "//textarea[@id='description']", "测试修改")
			sleep(1)
			# 点击保存按钮
			click("xpath", "//span[text()='保存']")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("支票用途，修改成功！")
			time.sleep(3)
			
			# 测试删除💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入支票用途窗体
			switch_to("xpath", '//*[@id="chequePurpose-tab-iframe"]')
			# 刷新勾选那妞
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
			implici_wait("xpath", "//span[contains(text(),'操作成功')]")
			print("支票用途，删除成功！")
			time.sleep(3)
			
			# 点击基础设置，回归初始页面
			click("xpath", "//li[@f_value='billSetting']/descendant-or-self::*[5]")
			sleep(1)
			
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("支票用途失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
			
			# def tearDown(self):
			#     self.driver.quit()
			print("结束时间：", time.strftime("%Y-%m-%d %H:%M:%S"))
			
		
		# 测试票据管理-基础设置-支票作废原因💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
		try:
			logger.info("测试票据管理-基础设置-支票作废原因")
			# 点击基础设置
			click("xpath", "//li[@f_value='billSetting']/descendant-or-self::*[5]")
			sleep(1)
			# 点击支票用途
			span_click("支票作废原因")
			sleep(1)
			# 退出所有窗口
			switch_default()
			
			# 测试新增💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			for i in range(1, 3):
				# 切入支票作废原因窗体
				switch_to("xpath", "//iframe[@id='chequeInvalidReason-tab-iframe']")
				# 点击新增
				span_click("新增")
				sleep(1)
				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='addWin-iframe']")
				# 输入作废代码
				code = time.strftime("%Y%m%d%S")
				input("xpath", "//input[@name='code']", code)
				sleep(1)
				
				# 输入作废原因名称
				name = "ZPZFYY" + str(time.strftime("%H%M%S"))
				input("xpath", "//input[@id='name']", name)
				sleep(1)
				# 点击保存按钮
				click("xpath", "//span[text()='保存']")
				sleep(1)
				# 退出所有iframe窗体
				switch_default()
				# 用隐式等待方法等页面出现新增成功的提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				if i == 2:
					print("支票作废原因，新增成功！")
				time.sleep(3)
			
			# 测试修改💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入‘支票作废原因’的iframe窗体
			switch_to("xpath", "//iframe[@id='chequeInvalidReason-tab-iframe']")
			# 刷新勾选那妞
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
			sleep(1)
			
			span_click("修改")
			sleep(1)
			# 切入修改的iframe窗体
			switch_to("xpath", "//iframe[@id='modWin-iframe']")
			# 修改描述框中的内容
			input("xpath", "//textarea[@id='description']", "测试修改")
			sleep(1)
			# 点击保存按钮
			click("xpath", "//span[text()='保存']")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("支票作废原因，修改成功！")
			time.sleep(3)
			
			# 测试删除💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入支票作废原因的iframe窗体
			switch_to("xpath", "//iframe[@id='chequeInvalidReason-tab-iframe']")
			# 刷新勾选那妞
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
			implici_wait("xpath", "//span[contains(text(),'操作成功')]")
			print("支票作废原因，删除成功！")
			time.sleep(3)
			
			# 点击基础设置，回归初始页面
			click("xpath", "//li[@f_value='billSetting']/descendant-or-self::*[5]")
			sleep(1)
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("支票用途失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
			
			# def tearDown(self):
			#     self.driver.quit()
			print("结束时间：", time.strftime("%Y-%m-%d %H:%M:%S"))
		
		
		# 测试票据管理-基础设置-承兑银行信息💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
		try:
			logger.info("测试票据管理-基础设置-承兑银行信息")
			# 点击基础设置
			click("xpath", "//li[@f_value='billSetting']/descendant-or-self::*[5]")
			sleep(1)
			# 点击承兑银行信息
			span_click("承兑银行信息")
			sleep(1)
			# 退出所有窗口
			switch_default()
			
			# 测试新增💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			for i in range(1, 3):
				switch_to("xpath", "//iframe[@id='acceptancebankinfos-tab-iframe']")
				# 用JS的方法点击新增按钮
				js_click("xpath", "//span[text()='新增']")
				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='addacceptanceBankInfosWin-iframe']")
				# 输入银行名称，通过模糊匹配搜索
				if i ==1 :
					input("xpath", "//span[@title='银行']/parent::*/following-sibling::*/descendant::*[3]", "中国银行")
					sleep(1)
					up_enter_click('//*[@id="combobox-input-bankid"]')
					sleep(1)
				if i ==2 :
					input("xpath", "//span[@title='银行']/parent::*/following-sibling::*/descendant::*[3]", "农业银行")
					sleep(1)
					up_enter_click('//*[@id="combobox-input-bankid"]')
					sleep(1)

				# 输入可收票额度
				input("xpath", "//input[@id='draftamount-input']", "5000")
				sleep(1)
				
				# 输入贴息率(%)
				input("xpath", "//input[@id='rate-input']", "5")
				sleep(1)
				
				# 点击保存按钮
				click("xpath", "//span[text()='保存']")
				sleep(1)
				# 退出所有iframe窗体
				switch_default()
				# 用隐式等待方法等页面出现提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				if i ==2 :
					print("承兑银行信息，保存成功！")
				time.sleep(3)
			
			# 测试修改💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入承兑银行信息的iframe窗体
			switch_to("xpath", "//iframe[@id='acceptancebankinfos-tab-iframe']")
			# 刷新勾选那妞
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
			sleep(1)
			
			span_click("修改")
			sleep(1)
			# 切入修改的iframe窗体
			switch_to("xpath", "//iframe[@id='modWin-iframe']")
			# 因为是金额，所以先清空，再修改描述框中的内容
			clear("xpath", "//input[@id='draftamount-input']")
			sleep(1)
			input("xpath", "//input[@id='draftamount-input']", "8000")
			# 点击保存按钮
			click("xpath", "//span[text()='保存']")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("承兑银行信息，修改成功！")
			time.sleep(3)
			
			# 测试删除💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入承兑银行信息的iframe窗体
			switch_to("xpath", "//iframe[@id='acceptancebankinfos-tab-iframe']")
			# 刷新勾选那妞
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
			implici_wait("xpath", "//span[contains(text(),'操作成功')]")
			print("承兑银行信息，删除成功！")
			time.sleep(3)
			
			# 点击基础设置，回归初始页面
			click("xpath", "//li[@f_value='billSetting']/descendant-or-self::*[5]")
			sleep(1)
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("承兑银行信息失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
			
			# def tearDown(self):
			#     self.driver.quit()
			print("结束时间：", time.strftime("%Y-%m-%d %H:%M:%S"))
			
		
		# 测试票据管理-基础设置-电票操作类别💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
		try:
			logger.info("测试票据管理-基础设置-电票操作类别")
			# 点击基础设置
			click("xpath", "//li[@f_value='billSetting']/descendant-or-self::*[5]")
			sleep(1)
			# 点击承兑银行信息
			span_click("电票操作类别")
			sleep(1)
			# 退出所有窗口
			switch_default()
			
			# 测试新增💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			for i in range(1, 3):
				# 切入电票操作类别的iframe窗体
				switch_to("xpath", "//iframe[@id='operationfincation-tab-iframe']")
				# 用JS的方法点击新增按钮
				js_click("xpath", "//span[text()='新增']")
				sleep(1)
				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='addWin-iframe']")
				# 输入代码
				code = time.strftime("%Y%m%d%S")
				input("xpath", "//input[@name='code']",code)
				sleep(1)
				
				# 输入的名称
				name = "DPCZLB" + str(time.strftime("%H%M%S"))
				input("xpath", "//input[@id='name']", name)
				sleep(1)
				
				# 点击保存按钮
				click("xpath", "//span[text()='保存']")
				sleep(1)
				# 退出所有iframe窗体
				switch_default()
				
				# 用隐式等待方法等页面出现新增成功的提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				if i ==2 :
					print("电票操作类别，保存成功！")
				time.sleep(3)
			
			# 测试修改💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入‘电票操作类别’的iframe窗体
			switch_to("xpath", "//iframe[@id='operationfincation-tab-iframe']")
			# 刷新勾选那妞
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
			sleep(1)
			span_click("修改")
			sleep(1)
			
			# 切入修改的iframe窗体
			switch_to("xpath", "//iframe[@id='modWin-iframe']")
			sleep(1)
			# 修改描述框中的内容
			input("xpath", "//textarea[@id='description']", "自动化测试修改")
			sleep(1)
			# 点击保存按钮
			click("xpath", "//span[text()='保存']")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("电票操作类别，修改成功！")
			time.sleep(3)
			
			# 测试删除💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入‘电票操作类别’的iframe窗体
			switch_to("xpath", "//iframe[@id='operationfincation-tab-iframe']")
			# 刷新勾选那妞
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
			implici_wait("xpath", "//span[contains(text(),'操作成功')]")
			print("电票操作类别用途，删除成功！")
			time.sleep(3)
			
			# 点击基础设置，回归初始页面
			click("xpath", "//li[@f_value='billSetting']/descendant-or-self::*[5]")
			sleep(1)
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("电票操作类别失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
			
			# def tearDown(self):
			#     self.driver.quit()
			print("结束时间：", time.strftime("%Y-%m-%d %H:%M:%S"))
			
		
		# 测试票据管理-基础设置-电票经办网点💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
		try:
			logger.info("测试票据管理-基础设置-电票经办网点")
			# 点击基础设置
			click("xpath", "//li[@f_value='billSetting']/descendant-or-self::*[5]")
			sleep(1)
			# 点击承兑银行信息
			span_click("电票经办网点")
			sleep(1)
			# 退出所有窗口
			switch_default()
			
			# 测试新增💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			for i in range(1, 3):
				# 切入电票经办网点的iframe窗体
				switch_to("xpath", "//iframe[@id='eledraftnetwork-tab-iframe']")
				# 用JS的方法点击新增按钮
				js_click("xpath", "//span[text()='新增']")
				sleep(1)
				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='addWin-iframe']")
				# 输入账号
				if i ==1 :
					click("xpath",'//*[@id="combobox-input-accountid"]')
					sleep(1)
					up_enter_click('//*[@id="combobox-input-accountid"]')
				if i ==2 :
					click("xpath",'//*[@id="combobox-input-accountid"]')
					sleep(1)
					click("xpath",'//*[@id="accountid-combogrid-body-table"]/tbody/tr[2]/td[2]/div')
					sleep(1)
				
				# 点击保存按钮
				click("xpath", "//span[text()='保存']")
				sleep(1)
				# 退出所有iframe窗体
				switch_default()
				
				# 用隐式等待方法等页面出现新增成功的提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				if i == 2:
					print("电票经办网点，新增成功！")
				time.sleep(3)
			
			# 测试修改💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入‘电票经办网点’的iframe窗体
			switch_to("xpath", "//iframe[@id='eledraftnetwork-tab-iframe']")
			# 刷新勾选那妞
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
			sleep(1)
			span_click("修改")
			sleep(1)
			
			# 切入修改的iframe窗体
			switch_to("xpath", "//iframe[@id='modWin-iframe']")
			sleep(1)
			click("xpath", "//span[text()='保存']")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("电票操作类别，修改成功！")
			time.sleep(3)
			
			# 测试删除💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入电票经办网点的iframe窗体
			switch_to("xpath", "//iframe[@id='eledraftnetwork-tab-iframe']")
			# 刷新勾选那妞
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
			implici_wait("xpath", "//span[contains(text(),'操作成功')]")
			print("电票经办网点，删除成功！")
			time.sleep(3)
			
			# 点击基础设置，回归初始页面
			click("xpath", "//li[@f_value='billSetting']/descendant-or-self::*[5]")
			sleep(1)
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("电票经办网点失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
			
			# def tearDown(self):
			#     self.driver.quit()
			print("结束时间：", time.strftime("%Y-%m-%d %H:%M:%S"))

		'''
		# 创建票据管理需要的数据💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
		try:
			#点击票据管理，收回窗体
			js_click("xpath", "//span[contains(text(),'票据管理')]")
			sleep(1)
			
			# 创建直联单笔收款账户
			js_gd("xpath", "//span[contains(text(),'账户资金监控')]")
			# 用JS的方法点击票据管理菜单按钮
			js_click("xpath", "//span[contains(text(),'账户资金监控')]")
			sleep(1)
			click("xpath", "//span[contains(text(),'账户生命周期')]")
			sleep(1)
			# 点击账户维户
			click("xpath", "//span[text()='账户维护']")
			sleep(1)
			switch_default()
			
			# 切入单币种账户窗体
			switch_to("xpath", '//*[@id="bankAccounts-tab-iframe"]')
			sleep(1)
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			click("xpath", "//span[text()='新增']")
			switch_to("xpath", '//*[@id="addWin-iframe"]')
			sleep(1)
			click("xpath", "//input[@id='combobox-input-bankid']")
			# 模糊匹配报错，因此选择直接点击
			click("xpath", "//div[@title='代码-名称:BOC-中国银行']")
			sleep(1)
			
			# 选择开户行
			click("xpath", "//input[@id='combobox-input-banklocationid']")
			input("xpath", "//input[@id='combobox-input-banklocationid']", "大连泡崖")
			sleep(1)
			click("xpath", "//div[@title='联行号-开户行名:104222000965-中国银行股份有限公司大连泡崖街支行']")
			sleep(1)
			
			# 选择币种
			click("xpath", "//input[@id='combobox-input-currencyid']")
			# 输入开户行大连泡崖街支行名称，模糊查询
			input("xpath", "//input[@id='combobox-input-currencyid']", "CNY")
			sleep(1)
			input_down("xpath", "//input[@id='combobox-input-currencyid']")
			input_enter("xpath", "//input[@id='combobox-input-currencyid']")
			time.sleep(1)
			
			# 选择账户性质
			click("xpath", "//input[@id='combobox-input-accounttypeid']")
			# 输入开户行大连泡崖街支行名称，模糊查询
			input("xpath", "//input[@id='combobox-input-accounttypeid']", "基本户")
			sleep(1)
			input_down("xpath", "//input[@id='combobox-input-accounttypeid']")
			input_enter("xpath", "//input[@id='combobox-input-accounttypeid']")
			time.sleep(1)
			
			# # 选择银企直联户isbankdirect
			click("xpath", "//input[@id='isbankdirect']")
			sleep(1)
			
			# 境内外
			# 输入开户行大连泡崖街支行名称，模糊查询
			input("xpath", "//input[@id='combobox-input-inorout']", "境内")
			sleep(1)
			input_down("xpath", "//input[@id='combobox-input-inorout']")
			input_enter("xpath", "//input[@id='combobox-input-inorout']")
			# 输入银行账号
			input("xpath", '//*[@id="accountnumber"]', '20211005')
			sleep(1)
			input("xpath", '//*[@id="accountname"]', '中国银行直联通用账户')
			
			# 点击保存按钮
			click("xpath", "//span[text()='保存']")
			# 退出所有iframe窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			
			sleep(1)
			# 切入窗体
			switch_to("xpath", '//*[@id="bankAccounts-tab-iframe"]')
			sleep(1)
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			
			# 点击查看
			js_click("xpath", "//span[@class='f-contrac-close']")
			sleep(1)
			
			input("xpath", '//*[@id="accountnumber"]', '20211005')
			sleep(1)
			# 点击查询
			click("xpath", "//span[text()='查询']")
			sleep(1)
			
			# 勾选数据
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
			sleep(1)
			click("xpath", '/html/body/div[1]/div[3]/div[1]/div[1]/a/em')
			click("xpath", '/html/body/div[1]/div[3]/div[1]/div[2]/ul/li[1]/a')
			click("xpath", "//input[@id='openeddatewin-input']")
			sleep(2)
			
			today = date.today()
			open_date = today - timedelta(days=20)
			click("xpath", "//input[@id='openeddatewin-input']")
			sleep(1)
			clear("xpath", "//input[@id='openeddatewin-input']")
			sleep(1)
			input("xpath", "//input[@id='openeddatewin-input']", str(open_date))
			time.sleep(1)
			click("xpath", '//*[@id="journalbalance-input"]')
			sleep(1)
			clear("xpath", '//*[@id="journalbalance-input"]')
			sleep(1)
			input("xpath", '//*[@id="journalbalance-input"]', "50000")
			sleep(1)
			click("xpath", "//span[text()='确定']")
			sleep(1)
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("中国银行直联通用账户创建成功")
			
			# 点击账户资金监控，收回窗体，并返回票据管理页面
			js_click("xpath", "//span[contains(text(),'账户资金监控')]")
			sleep(1)
			
			#融资管理--授信协议做数据
			js_gd("xpath", "//span[contains(text(),'融资管理')]")
			# 用JS的方法点击资金结算管理菜单按钮
			js_click("xpath", "//span[contains(text(),'融资管理')]")
			sleep(1)
			
			#点击融资授信
			click("xpath", "//span[contains(text(),'融资授信')]")
			sleep(1)
			span_click("授信协议")
			
			#切入授信协议窗体
			switch_to("xpath",'//*[@id="credits-tab-iframe"]')
			span_click("新增")
			
			switch_to("xpath",'//*[@id="addWin-iframe"]')
			
			#协议号
			input("xpath",'//*[@id="contractcode"]','XYH5555')
			sleep(1)
			
			#融资机构类型
			input("xpath",'//*[@id="combobox-input-financialinstitutiontype"]','银行')
			sleep(1)
			up_enter_click('//*[@id="combobox-input-financialinstitutiontype"]')
			
			#融资机构
			input("xpath",'//*[@id="combobox-input-bankid"]','BOC-中国银行')
			sleep(1)
			up_enter_click('//*[@id="combobox-input-bankid"]')
			
			#授信额度
			double_click("xpath",'//*[@id="creditamount-input"]')
			sleep(1)
			input("xpath",'//*[@id="creditamount-input"]','5000000')
			sleep(1)
			
			#协议截止日期
			clear("xpath",'//*[@id="enddate-input"]')
			today = date.today()
			JZRQ = today + timedelta(days=730)
			input("xpath",'//*[@id="enddate-input"]',str(JZRQ))
			sleep(1)
			
			#适用组织
			click("xpath",'//*[@id="combobox-input-applicableorgrange"]')
			sleep(1)
			click("xpath",'//*[@id="applicableorgrange-combogrid-body-table"]/tbody/tr[1]/td[2]/div')
			sleep(1)
			click("xpath", '//*[@id="combobox-input-applicableorgrange"]')
			sleep(1)
			
			#使用模式
			input("xpath",'//*[@id="combobox-input-usemode"]','下属组织共享')
			sleep(1)
			up_enter_click('//*[@id="combobox-input-usemode"]')
			
			span_click("授信产品")
			
			#新增行（承兑保贴）
			click("xpath",'//*[@id="gridbar"]/div/div[1]/table/tbody/tr/td[1]')
			sleep(1)
			
			#授信产品
			input("xpath",'//*[@id="combobox-input-creditbusinessgrid-financeproductid-0"]','CDBT-承兑保贴')
			sleep(1)
			up_enter_click('//*[@id="combobox-input-creditbusinessgrid-financeproductid-0"]')
			
			#额度
			double_click("xpath",'//*[@id="creditbusinessgrid-creditamount-0-input"]')
			sleep(1)
			input("xpath",'//*[@id="creditbusinessgrid-creditamount-0-input"]','50000')
			sleep(1)
			
			# 新增行（109-银行承兑汇票）
			click("xpath", '//*[@id="gridbar"]/div/div[1]/table/tbody/tr/td[1]')
			sleep(1)
			
			# 授信产品
			input("xpath", '//*[@id="combobox-input-creditbusinessgrid-financeproductid-1"]', '109-银行承兑汇票')
			sleep(1)
			up_enter_click('//*[@id="combobox-input-creditbusinessgrid-financeproductid-1"]')
			
			# 额度
			double_click("xpath", '//*[@id="creditbusinessgrid-creditamount-1-input"]')
			sleep(1)
			input("xpath", '//*[@id="creditbusinessgrid-creditamount-1-input"]', '50000')
			sleep(1)
			
			# 新增行（105-信用证开证）
			click("xpath", '//*[@id="gridbar"]/div/div[1]/table/tbody/tr/td[1]')
			sleep(1)
			
			# 授信产品
			input("xpath", '//*[@id="combobox-input-creditbusinessgrid-financeproductid-2"]', '信用证开证')
			sleep(1)
			up_enter_click('//*[@id="combobox-input-creditbusinessgrid-financeproductid-2"]')
			
			# 额度
			double_click("xpath", '//*[@id="creditbusinessgrid-creditamount-2-input"]')
			sleep(1)
			input("xpath", '//*[@id="creditbusinessgrid-creditamount-2-input"]', '50000')
			sleep(1)
			
			span_click("保存")
			sleep(3)
			switch_default()
			
			# 对新增数据进行审核
			# 切入授信协议窗体
			switch_to("xpath", '//*[@id="credits-tab-iframe"]')
			
			# 勾选数据、审核
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			span_click("审核")
			ok_click()
			sleep(3)
			
			# 勾选数据、生效
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			span_click("生效")
			sleep(3)
			switch_default()
			
			# 收回融资管理窗体
			click("xpath", "//span[contains(text(),'融资授信')]")
			sleep(1)
			js_click("xpath", "//span[contains(text(),'融资管理')]")
			sleep(1)
			#-----
			js_gd("xpath", "//span[contains(text(),'票据管理')]")
			# 用JS的方法点击资金结算管理菜单按钮
			js_click("xpath", "//span[contains(text(),'票据管理')]")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("数据创建失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		'''
		
		
		# 支票管理--应付支票登记功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
		try:
			logging.info("开始测试票据管理-支票管理-应付支票登记")
			click("xpath", "//span[@title='支票管理']")
			sleep(1)
			# 点击应付支票登记菜单
			click("xpath", "//span[@title='应付支票登记']")
			sleep(1)
			# 退出所有的iframe窗体
			switch_default()
			#测试新增功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			global startCode
			global endCode
			for i in range(1, 3):
				# 切入应付支票登记iframe窗体
				switch_to("xpath", "//iframe[@id='chequeStorage-tab-iframe']")
				# 用JS的方法点击新增按钮
				js_click("xpath", "//span[text()='新增']")
				sleep(1)
				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='addWin-iframe']")
				sleep(1)
				
				#支票类型
				input("xpath",'//*[@id="combobox-input-booktype"]','现金/转账')
				sleep(1)
				up_enter_click('//*[@id="combobox-input-booktype"]')
				
				#起始码,终止码
				if i ==1 :
					startCode = random.randint(1000,10000)
					endCode   = startCode +1
					#起始码
					input("xpath",'//*[@id="codefrom"]',startCode)
					sleep(1)
					#终止码
					input("xpath",'//*[@id="codeto"]',endCode)
					sleep(1)
				if i ==2 :
					startCode2 = random.randint(1000,10000)
					endCode2  = startCode2 +1
					#起始码
					input("xpath",'//*[@id="codefrom"]',startCode2)
					sleep(1)
					#终止码
					input("xpath",'//*[@id="codeto"]',endCode2)
					sleep(1)
			
				# 银行账号
				input("xpath", '//*[@id="combobox-input-accountid"]', '20211005')
				sleep(1)
				up_enter_click('//*[@id="combobox-input-accountid"]')
			
				span_click("保存")
				sleep(1)
			
				# 点击弹出框的OK键
				click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
				sleep(1)
			
				# 退出所有iframe窗体
				switch_default()
			
				# 用隐式等待方法等页面出现提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				if i == 2:
					print("应付支票登记,新增成功")
				time.sleep(3)
			
			# 测试修改功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入应付支票登记iframe窗体
			switch_to("xpath", "//iframe[@id='chequeStorage-tab-iframe']")
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div')
			sleep(1)
			
			# 点击修改
			span_click("修改")
			sleep(1)
			
			# 切入修改的iframe窗体
			switch_to("xpath", "//iframe[@id='modWin-iframe']")
			# 修改备注框中值
			input("xpath", "//textarea[@id='description']", "测试修改")
			sleep(1)
			
			# 点击保存按钮
			click("xpath", "//span[text()='保存']")
			sleep(1)
			# 点击弹出框的OK键
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
			sleep(1)
			
			# 退出所有iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("应付支票登记，修改成功！")
			time.sleep(3)
			
			# 测试删除功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入应付支票登记iframe窗体
			switch_to("xpath", "//iframe[@id='chequeStorage-tab-iframe']")
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div')
			sleep(1)
			
			# 点击删除按钮
			click("xpath", "//span[text()='删除']")
			sleep(1)
			# 点击弹出框的OK键
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
			sleep(1)
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("应付支票登记，删除成功！")
			time.sleep(3)
			#点击支票管理收回窗体
			click("xpath", "//span[@title='支票管理']")
			sleep(1)
	
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("应付支票登记！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		
		
		
		# 支票管理--应付支票领用功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
		try:
			logging.info("开始测试票据管理-支票管理-应付支票领用")
			click("xpath", "//span[@title='支票管理']")
			sleep(1)
			# 点击应付支票登记菜单
			click("xpath", "//span[@title='应付支票领用']")
			sleep(1)
			# 退出所有的iframe窗体
			switch_default()
			
			#测试支票领用功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入‘应付支票领用’的iframe窗体
			switch_to("xpath", "//iframe[@id='chequeRecipients-tab-iframe']")
			
			#查询出相应数据
			# 用JS的方法点击放大镜
			js_click("xpath", "//span[@class='f-contrac-close']")
			sleep(1)
			#银行账号
			input("xpath",'//*[@id="combobox-input-accountid"]','20211005')
			sleep(1)
			click("xpath",'//*[@id="accountid-combogrid-body-table"]/tbody/tr/td[2]/div/button')
			sleep(1)
			#查询
			span_click("查询")
			sleep(1)
			
			#刷新、勾选按钮
			click("xpath",'//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath",'//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("支票领用")
			sleep(1)
			
			#切入领用窗体
			switch_to("xpath",'//*[@id="applyWin-iframe"]')
			#领用人
			input("xpath",'//*[@id="username"]','张中国')
			sleep(1)
			# 输入收款人名称
			input("xpath", "//input[@id='receiever']", "浙江彩旗科技")
			sleep(1)
			
			# 输入支票用途，通过模糊匹配搜索
			input("xpath", "//input[@id='combobox-input-chequepurposeid']", "ZPYT")
			sleep(1)
			up_enter_click("//input[@id='combobox-input-chequepurposeid']")
			
			# 金额中填入值
			clear("xpath", "//input[@id='useamount-input']")
			input("xpath", "//input[@id='useamount-input']", "500")
			sleep(1)
			
			# 点击领用按钮
			click("xpath", "//span[text()='领用']")
			sleep(1)
			# 显示等待3秒，首先页面不退出，继续点击该页面的审核按钮
			print("应付支票领用成功！")
			span_click("返回")
			switch_default()
			sleep(3)
			
			# 测试领用取消功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入‘应付支票领用’的iframe窗体
			switch_to("xpath", "//iframe[@id='chequeRecipients-tab-iframe']")
			
			# 查询出相应数据
			# 用JS的方法点击放大镜
			js_click("xpath", "//span[@class='f-contrac-close']")
			sleep(1)
			# 银行账号
			input("xpath", '//*[@id="combobox-input-accountid"]', '20211005')
			sleep(1)
			click("xpath", '//*[@id="accountid-combogrid-body-table"]/tbody/tr/td[2]/div/button')
			sleep(1)
			# 查询
			span_click("查询")
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("领用取消")
			sleep(1)
			ok_click()
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'领用取消成功！')]")
			print("应付支票领用，领用取消成功！")
			time.sleep(3)
			
			# 测试领用审核功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入‘应付支票领用’的iframe窗体
			switch_to("xpath", "//iframe[@id='chequeRecipients-tab-iframe']")
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("支票领用")
			sleep(1)
			
			# 切入领用窗体
			switch_to("xpath", '//*[@id="applyWin-iframe"]')
			# 领用人
			input("xpath", '//*[@id="username"]', '张中国')
			sleep(1)
			# 输入收款人名称
			input("xpath", "//input[@id='receiever']", "浙江彩旗科技")
			sleep(1)
			
			# 输入支票用途，通过模糊匹配搜索
			input("xpath", "//input[@id='combobox-input-chequepurposeid']", "ZPYT")
			sleep(1)
			up_enter_click("//input[@id='combobox-input-chequepurposeid']")
			
			# 金额中填入值
			clear("xpath", "//input[@id='useamount-input']")
			input("xpath", "//input[@id='useamount-input']", "500")
			sleep(1)
			
			# 点击领用按钮
			click("xpath", "//span[text()='领用']")
			sleep(1)
			# 显示等待3秒，首先页面不退出，继续点击该页面的审核按钮
			span_click("返回")
			switch_default()
			sleep(3)
			
			#领用审核==============================
			# 切入‘应付支票领用’的iframe窗体
			switch_to("xpath", "//iframe[@id='chequeRecipients-tab-iframe']")
			
			# 查询出相应数据
			# 用JS的方法点击放大镜
			js_click("xpath", "//span[@class='f-contrac-close']")
			sleep(1)
			# 银行账号
			input("xpath", '//*[@id="combobox-input-accountid"]', '20211005')
			sleep(1)
			click("xpath", '//*[@id="accountid-combogrid-body-table"]/tbody/tr/td[2]/div/button')
			sleep(1)
			# 查询
			span_click("查询")
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("领用审核")
			sleep(1)
			ok_click()
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'领用审核成功！')]")
			print("应付支票领用，领用审核成功！")
			time.sleep(3)
			
			# 测试打印功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入‘应付支票领用’的iframe窗体
			switch_to("xpath", "//iframe[@id='chequeRecipients-tab-iframe']")
			
			
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("打印")
			sleep(1)
			switch_to("xpath",'//*[@id="printWin-iframe"]')
			implici_wait("xpath", "//td[contains(text(),'浙江')]")
			print("应付支票领用，打印成功！")
			
			switch_parent()
			click("xpath",'//*[@id="f-win-title-printWin"]/div[1]/div')
			sleep(1)
			
			switch_default()
			
			# 测试取消审核功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入‘应付支票领用’的iframe窗体
			switch_to("xpath", "//iframe[@id='chequeRecipients-tab-iframe']")
			
			
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("取消审核")
			sleep(1)
			ok_click()
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'领用审核取消成功！')]")
			print("应付支票领用，领用审核取消成功！")
			time.sleep(3)
			
			#点击支票管理收回窗体
			click("xpath", "//span[@title='支票管理']")
			sleep(1)
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("应付支票领用失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		
		
		
		# 测试应付支票作废💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
		try:
			
			# 点击支票管理菜单
			click("xpath", "//span[@title='支票管理']")
			sleep(1)
			# 点击应付支票作废菜单
			click("xpath", "//span[@title='应付支票作废']")
			sleep(1)
			# 退出所有的iframe窗体
			switch_default()
		
			#测试支票作废功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入‘应付支票作废’的iframe窗体
			switch_to("xpath", "//iframe[@id='chequeInvalid-tab-iframe']")
			
			#查询
			# 用JS的方法点击放大镜
			js_click("xpath", "//span[@class='f-contrac-close']")
			sleep(1)
			
			# 输入银行账号
			input("xpath",'//*[@id="combobox-input-accountid"]','20211005')
			sleep(1)
			click("xpath",'//*[@id="accountid-combogrid-body-table"]/tbody/tr/td[2]/div/button')
			sleep(1)
			
			# 点击查询
			click("xpath", "//span[text()='查询']")
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			# 用JS的方法点击支票作废按钮
			js_click("xpath", "//span[text()='支票作废']")
			sleep(1)
			# 切入支票领用的iframe窗体
			switch_to("xpath", "//iframe[@id='applyWin-iframe']")
			sleep(1)
			
			#作废原因
			click("xpath", "//input[@id='combobox-input-chequecancelreasonid']")
			sleep(1)
			up_enter_click('//*[@id="combobox-input-chequecancelreasonid"]')
			
			click("xpath", "//span[text()='保存']")
			sleep(1)
			#退出所有窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功')]")
			print("应付支票作废,作废成功！")
			time.sleep(3)
			
			
			# 测试取消作废功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入应付支票领用窗体
			switch_to("xpath", "//iframe[@id='chequeInvalid-tab-iframe']")
			
			# 用JS的方法点击支票领用按钮
			js_click("xpath", "//span[text()='高级查询']")
			sleep(1)
			# 已作废
			input("xpath", '//*[@id="combobox-input-value_0"]', '20211005')
			sleep(1)
			click("xpath",'//*[@id="value_0-combogrid-body-table"]/tbody/tr/td[2]/div/button')
			sleep(1)
			#去除下拉框
			click("xpath",'//*[@id="f-win-title-advQueryWin"]/div[2]/div[1]/div/div/label')
			sleep(1)
			
			#作废状态
			clear("xpath",'//*[@id="combobox-input-property_1"]')
			sleep(1)
			input("xpath",'//*[@id="combobox-input-property_1"]','作废状态')
			sleep(1)
			up_enter_click('//*[@id="combobox-input-property_1"]')
			#条件
			clear("xpath",'//*[@id="combobox-input-condition_1"]')
			input("xpath",'//*[@id="combobox-input-condition_1"]','等于')
			sleep(1)
			keyDown("enter")
			#已作废
			input("xpath", '//*[@id="combobox-input-value_1"]', '已作废')
			sleep(1)
			up_enter_click('//*[@id="combobox-input-value_1"]')
			#查询
			click("xpath", "//div[contains(text(),'查询')]")
			sleep(1)
			click("xpath",'//*[@id="f-win-title-advQueryWin"]/div[1]/div')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			click("xpath", "//span[text()='作废取消']")
			# 点击弹出框的OK键
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
			sleep(1)
			# 退出所有窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'取消作废成功！')]")
			print("应付支票作废，取消作废成功！")
			time.sleep(3)
			
			# 点击支票管理收回窗体
			click("xpath", "//span[@title='支票管理']")
			sleep(1)
			
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("应付支票作废失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		
		
		# 测试应付支票查看💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
		try:
			# 点击支票管理菜单
			click("xpath", "//span[@title='支票管理']")
			# 点击应付支票作废菜单
			click("xpath", "//span[@title='应付支票查看']")
			# 退出所有的iframe窗体
			switch_default()
			
			# 切入‘应付支票作废’的iframe窗体
			switch_to("xpath", "//iframe[@id='chequeView-tab-iframe']")
			# 用JS的方法点击放大镜
			js_click("xpath", "//span[@class='f-contrac-close']")
			sleep(1)
			
			#银行账号
			input("xpath",'//*[@id="combobox-input-accountid"]','20211005')
			sleep(1)
			click("xpath",'//*[@id="accountid-combogrid-body-table"]/tbody/tr/td[2]/div/button')
			sleep(1)
			
			# 点击查询
			click("xpath", "//span[text()='查询']")
			sleep(1)
			
			double_click("xpath",'//*[@id="grid-body-table"]/tbody/tr[1]/td[3]/div')
			sleep(1)
			switch_to("xpath",'//*[@id="detailWin-iframe"]')
			# 用隐式等待方法等页面出现预期数据：复核人:mindy
			implici_wait("xpath", '//*[@id="uncanceluserid"]')
			sleep(3)
			print("应付支票查看，查看成功！")
			span_click("返回")
			sleep(1)
			switch_default()
			time.sleep(3)
			# 点击支票管理收回窗体
			click("xpath", "//span[@title='支票管理']")
			sleep(1)
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("应付支票作废失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		
		
		# 测试应收支票管理💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
		try:
			# 点击支票管理菜单
			click("xpath", "//span[@title='支票管理']")
			sleep(1)
			# 点击应付支票登记菜单
			click("xpath", "//span[@title='应收支票管理']")
			sleep(1)
			# 退出所有的iframe窗体
			switch_default()
			
			#测试新增功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			for i in range(1,3):
				# 切入‘应收支票管理’的iframe窗体
				switch_to("xpath", "//iframe[@id='collectChequeManage-tab-iframe']")
				# 用JS的方法点击新增按钮
				js_click("xpath", "//span[text()='新增']")
				sleep(1)
				
				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='addWin-iframe']")
				sleep(1)
				
				
				# 输入支票号
				number =random.randint(1000,10000)
				input("xpath", "//input[@id='chequecode']",number)
				sleep(1)
				
				# 输入票面金额
				clear("xpath", "//input[@id='amount-input']")
				sleep(1)
				# 输入金额
				input("xpath", "//input[@id='amount-input']", "500")
				sleep(1)
				
				# 输入到期日期
				clear("xpath",'//*[@id="expiredate-input"]')
				sleep(1)
				input("xpath",'//*[@id="expiredate-input"]',"2021-12-21")
				sleep(1)
				keyDown("enter")
				
				#签发银行
				input("xpath",'//*[@id="combobox-input-issuebankid"]','中国银行')
				sleep(1)
				up_enter_click('//*[@id="combobox-input-issuebankid"]')
				
				#付票单位
				input("xpath",'//*[@id="combobox-input-oppcounterpartyid"]','浙江彩旗科技')
				sleep(1)
				double_click("xpath",'//*[@id="orgname"]')
				sleep(1)
				
				#保存
				span_click("保存")
				# 退出所有iframe窗体
				switch_default()
				
				# 用隐式等待方法等页面出现提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				if i == 2 :
					print("应收支票管理,新增成功")
				time.sleep(3)
			
			# 测试修改功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入‘应收支票管理’的iframe窗体
			switch_to("xpath", "//iframe[@id='collectChequeManage-tab-iframe']")
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			# 点击修改按钮
			click("xpath", "//span[text()='修改']")
			sleep(1)
			# 切入修改的iframe窗体
			switch_to("xpath", "//iframe[@id='modWin-iframe']")
			# 备注框中输入新内容
			input("xpath", "//textarea[@id='memo']", "修改备注内容")
			sleep(1)
			
			# 点击保存按钮
			click("xpath", "//span[text()='保存']")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("应收支票管理，修改成功！")
			time.sleep(3)
			
			# 测试删除功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入‘应收支票管理’的iframe窗体
			switch_to("xpath", "//iframe[@id='collectChequeManage-tab-iframe']")
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
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
			print("应收支票管理，删除成功！")
			logging.info("应收支票管理，删除成功！")
			time.sleep(3)
			
			# 测试审核、撤销审核功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入‘应收支票管理’的iframe窗体
			switch_to("xpath", "//iframe[@id='collectChequeManage-tab-iframe']")
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
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
			implici_wait("xpath", "//span[contains(text(),'成功审核1条!')]")
			print("应收支票管理，审核成功！")
			logging.info("应收支票管理，第一次审核成功！")
			time.sleep(3)
			
			# 测试撤销审核功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入‘应收支票管理’的iframe窗体
			switch_to("xpath", "//iframe[@id='collectChequeManage-tab-iframe']")
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
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
			implici_wait("xpath", "//span[contains(text(),'成功取消审核1条！')]")
			print("应收支票管理，取消审核成功！")
			time.sleep(3)
			
			# 测试托收功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入‘应收支票管理’的iframe窗体
			switch_to("xpath", "//iframe[@id='collectChequeManage-tab-iframe']")
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
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
			implici_wait("xpath", "//span[contains(text(),'成功审核1条!')]")
			time.sleep(3)
			
			#托收
			#切入‘应收支票管理’的iframe窗体
			switch_to("xpath", "//iframe[@id='collectChequeManage-tab-iframe']")
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			#点击托收
			span_click("托收")
			sleep(1)
			#托收银行
			input("xpath",'//*[@id="combobox-input-collectionbankid"]','中国银行')
			sleep(1)
			#托收银行
			click("xpath",'//*[@id="collectionbankid-combogrid-body-table"]/tbody/tr[1]/td[2]/div')
			sleep(1)
			span_click("确定")
			# 退出所有iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'成功托收1条！')]")
			print("应收支票登记，托收成功！")
			sleep(3)
			
			# 测试托收到账功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入‘应收支票管理’的iframe窗体
			switch_to("xpath", "//iframe[@id='collectChequeManage-tab-iframe']")
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("托收到账")
			sleep(1)
			switch_to("xpath",'//*[@id="impawneWin-iframe"]')
			span_click("确定")
			sleep(1)
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'成功到账1条！')]")
			print("应收支票管理，托收到账成功！")
			time.sleep(3)
			
			# 点击支票管理菜单，收回菜单
			click("xpath", "//span[@title='支票管理']")
			
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("应收支票管理失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		
		
		# 测试应收票据查看💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
		try:
			logger.info("开始测试票据管理-支票管理-应收支票查看")
			# 点击支票管理菜单
			click("xpath", "//span[@title='支票管理']")
			sleep(1)
			# 点击应付支票登记菜单
			click("xpath", "//span[@title='应收支票查看']")
			sleep(1)
			# 退出所有的iframe窗体
			switch_default()
			
			# 切入‘应收支票查看’的iframe窗体
			switch_to("xpath", "//iframe[@id='chequeManageView-tab-iframe']")
			double_click("xpath",'//*[@id="grid-body-table"]/tbody/tr[1]/td[3]/div')
			sleep(1)
			switch_to("xpath",'//*[@id="detailWin-iframe"]')
			# 用隐式等待方法等页面出现数据
			implici_wait("xpath", '//*[@id="createdby"]')
			sleep(3)
			span_click("返回")
			sleep(1)
			switch_default()
			
			# 点击支票管理菜单，收回菜单
			click("xpath", "//span[@title='支票管理']")
			sleep(1)
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("应收支票管理失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		
		
		
		
		# 测试应收票据管理💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
		try:
			logger.info("开始测试票据管理-承兑汇票管理-应收票据管理")
			# 点击承兑汇票管理
			click("xpath", "//span[@title='承兑汇票管理']")
			sleep(1)
			# 点击应付支票登记菜单
			click("xpath", "//span[@title='应收票据管理']")
			sleep(1)
			# 退出所有的iframe窗体
			switch_default()
			global PJH1
			global PJH2
			global PJH3
			global PJH4
			
			#测试新增功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			for i in range(1, 5):
				# 切入应收票据管理窗体
				switch_to("xpath", "//iframe[@id='recDraftManage-tab-iframe']")
				# 用JS的方法点击新增按钮
				js_click("xpath", "//span[text()='新增']")
				sleep(1)
				switch_to("xpath", '//*[@id="addWin-iframe"]')
				
				# 票据类型
				input("xpath", '//*[@id="combobox-input-drafttype"]', '109-银行承兑汇票')
				sleep(1)
				click("xpath", '//*[@id="drafttype-combogrid-body-table"]/tbody/tr/td[2]/div')
				sleep(1)
				
				# 票据号
				if i ==1 :
					PJH1 = time.strftime("%Y%m%d%H%M%S")
					input("xpath", '//*[@id="draftcode"]', PJH1)
					sleep(1)
				if i ==2 :
					PJH2 = time.strftime("%Y%m%d%H%M%S")
					input("xpath", '//*[@id="draftcode"]', PJH2)
					sleep(1)
				if i ==3 :
					PJH3 = time.strftime("%Y%m%d%H%M%S")
					input("xpath", '//*[@id="draftcode"]', PJH3)
					sleep(1)
				if i ==4 :
					PJH4 = time.strftime("%Y%m%d%H%M%S")
					input("xpath", '//*[@id="draftcode"]', PJH4)
					sleep(1)
				
				# 到期期限
				clear("xpath", '//*[@id="terms-input"]')
				sleep(1)
				input("xpath", '//*[@id="terms-input"]', "60")
				sleep(1)
				
				# 票面金额
				clear("xpath", '//*[@id="draftamount-input"]')
				sleep(1)
				input("xpath", '//*[@id="draftamount-input"]', "100")
				sleep(1)
				
				# 外部给票单位
				input("xpath", '//*[@id="combobox-input-endorsecounterpartyid"]', '浙江华语科技')
				sleep(2)
				# 双击清楚下拉框
				double_click("xpath", '//*[@id="recaccountinfo"]')
				sleep(1)
				
				# 承兑银行
				input("xpath", '//*[@id="combobox-input-paybankid"]', "BOC-中国银行")
				sleep(2)
				click("xpath", '//*[@id="paybankid-combogrid-body-table"]/tbody/tr[1]/td[2]/div')
				sleep(1)
				
				# 保存
				span_click("保存")
				sleep(1)
				# 退出所有iframe窗体
				switch_default()
				
				# 用隐式等待方法等页面出现提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				print("应收票据管理，新增成功！")
				sleep(3)
				
			
			# 测试修改功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入应收票据管理窗体
			switch_to("xpath", "//iframe[@id='recDraftManage-tab-iframe']")
			#刷新，勾选按钮
			click("xpath",'//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath",'//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			# 点击修改按钮
			click("xpath", "//span[text()='修改']")
			sleep(1)
			# 切入修改的iframe窗体
			switch_to("xpath", "//iframe[@id='editRecDraftWin-iframe']")
			input("xpath",'//*[@id="description"]','测试修改')
			sleep(1)
			span_click("保存")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("应收票据管理，修改成功！")
			time.sleep(3)
			
			# 测试删除功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入应收票据管理窗体
			switch_to("xpath", "//iframe[@id='recDraftManage-tab-iframe']")
			# 刷新，勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
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
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("应收票据管理，删除成功！")
			time.sleep(3)
			
			# 测试审核、撤销审核功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入应收票据管理窗体
			switch_to("xpath", "//iframe[@id='recDraftManage-tab-iframe']")
			# 刷新，勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
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
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("应收票据管理，审核成功！")
			time.sleep(3)
			
			# 撤销审核功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入应收票据管理窗体
			switch_to("xpath", "//iframe[@id='recDraftManage-tab-iframe']")
			# 刷新，勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
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
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("应收票据管理，取消审核成功！")
			time.sleep(3)
			
			
			# 测试背书功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入应收票据管理窗体
			switch_to("xpath", "//iframe[@id='recDraftManage-tab-iframe']")
			# 刷新，勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
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
			#票据操作-背书
			# 切入应收票据管理窗体
			switch_to("xpath", "//iframe[@id='recDraftManage-tab-iframe']")
			# 刷新，勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			triangle_cick("票据操作")
			sleep(1)
			js_click("xpath", "//a[contains(text(),'票据背书')]")
			sleep(1)
			#切入背书窗体
			switch_to("xpath",'//*[@id="endorseWin-iframe"]')
			#被背书对象类型
			input("xpath",'//*[@id="combobox-input-endorsetype"]','交易对手')
			sleep(1)
			up_enter_click('//*[@id="combobox-input-endorsetype"]')
			
			#被背书交易对手
			input("xpath", '//*[@id="combobox-input-endorsecounterpartyid"]', '张中国')
			sleep(1)
			
			# 被背书账户
			click("xpath",'//*[@id="combobox-input-endorseaccountnumber"]')
			sleep(1)
			input("xpath", '//*[@id="combobox-input-endorseaccountnumber"]', '200818199619')
			sleep(1)
			
			#被背书开户银行
			click("xpath",'//*[@id="combobox-input-endorsebanklocationid"]')
			sleep(1)
			up_enter_click('//*[@id="combobox-input-endorsebanklocationid"]')
			
			span_click("背书")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("应收票据管理，票据背书成功！")
			time.sleep(3)
			
			#取消背书💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入应收票据管理窗体
			switch_to("xpath", "//iframe[@id='recDraftManage-tab-iframe']")
			# 刷新，勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			triangle_cick("票据操作")
			sleep(1)
			js_click("xpath", "//a[contains(text(),'取消背书')]")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("应收票据管理，取消背书成功！")
			time.sleep(3)
			
			# 票据贴现💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入应收票据管理窗体
			switch_to("xpath", "//iframe[@id='recDraftManage-tab-iframe']")
			# 刷新，勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			triangle_cick("票据操作")
			sleep(1)
			js_click("xpath", "//a[contains(text(),'票据贴现')]")
			sleep(1)
			
			#切入贴现窗体
			switch_to("xpath",'//*[@id="discountWin-iframe"]')
			#贴现收款账户
			input("xpath",'//*[@id="combobox-input-bankaccountid"]','20211005')
			sleep(1)
			up_enter_click('//*[@id="combobox-input-bankaccountid"]')
			
			#贴现利率
			input("xpath",'//*[@id="editgrid-discountrate-0-input"]','5')
			sleep(1)
			span_click("贴现")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("应收票据管理，贴现成功！")
			time.sleep(3)
			
			# 取消贴现💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入应收票据管理窗体
			switch_to("xpath", "//iframe[@id='recDraftManage-tab-iframe']")
			# 刷新，勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			triangle_cick("票据操作")
			sleep(1)
			js_click("xpath", "//a[contains(text(),'取消贴现')]")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("应收票据管理，取消贴现成功！")
			time.sleep(3)
			
			# 票据托收💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入应收票据管理窗体
			switch_to("xpath", "//iframe[@id='recDraftManage-tab-iframe']")
			# 刷新，勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			triangle_cick("票据操作")
			sleep(1)
			js_click("xpath", "//a[contains(text(),'票据托收')]")
			sleep(1)
			
			switch_to("xpath",'//*[@id="endorseWin-iframe"]')
			#托收收款账户
			input("xpath",'//*[@id="combobox-input-bankaccountid"]','20211005')
			sleep(1)
			up_enter_click('//*[@id="combobox-input-bankaccountid"]')
			span_click("托收")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("应收票据管理，票据托收成功！")
			time.sleep(3)
			
			# 取消托收💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入应收票据管理窗体
			switch_to("xpath", "//iframe[@id='recDraftManage-tab-iframe']")
			# 刷新，勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			triangle_cick("票据操作")
			sleep(1)
			js_click("xpath", "//a[contains(text(),'取消托收')]")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("应收票据管理，取消托收成功！")
			time.sleep(3)
			
			# 票据质押💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入应收票据管理窗体
			switch_to("xpath", "//iframe[@id='recDraftManage-tab-iframe']")
			# 刷新，勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			triangle_cick("票据操作")
			sleep(1)
			js_click("xpath", "//a[contains(text(),'票据质押')]")
			sleep(1)
			
			switch_to("xpath",'//*[@id="impawneWin-iframe"]')
			span_click("保存")
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("应收票据管理，票据质押成功！")
			time.sleep(3)
			
			# 取消质押💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入应收票据管理窗体
			switch_to("xpath", "//iframe[@id='recDraftManage-tab-iframe']")
			# 刷新，勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			triangle_cick("票据操作")
			sleep(1)
			js_click("xpath", "//a[contains(text(),'取消质押')]")
			sleep(1)

			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("应收票据管理，取消质押成功！")
			time.sleep(3)
			
			# 质押到期托收💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入应收票据管理窗体
			switch_to("xpath", "//iframe[@id='recDraftManage-tab-iframe']")
			# 刷新，勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			triangle_cick("票据操作")
			sleep(1)
			js_click("xpath", "//a[contains(text(),'票据质押')]")
			sleep(1)
			
			switch_to("xpath", '//*[@id="impawneWin-iframe"]')
			span_click("保存")
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			time.sleep(3)
			#质押到期托收
			# 切入应收票据管理窗体
			switch_to("xpath", "//iframe[@id='recDraftManage-tab-iframe']")
			# 刷新，勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			triangle_cick("票据操作")
			sleep(1)
			js_click("xpath", "//a[contains(text(),'质押到期托收')]")
			sleep(1)
			switch_to("xpath",'//*[@id="impawneCollectionWin-iframe"]')
			#托收收款账户
			input("xpath",'//*[@id="combobox-input-bankaccountid"]','20211005')
			sleep(1)
			up_enter_click('//*[@id="combobox-input-bankaccountid"]')
			
			span_click("质押到期托收")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("应收票据管理，质押到期托收成功！")
			time.sleep(3)
			
			# 取消质押托收💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入应收票据管理窗体
			switch_to("xpath", "//iframe[@id='recDraftManage-tab-iframe']")
			# 刷新，勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			triangle_cick("票据操作")
			sleep(1)
			js_click("xpath", "//a[contains(text(),'取消质押托收')]")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("应收票据管理，取消质押托收成功！")
			time.sleep(3)
			
			# 测试坏票功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入应收票据管理窗体
			switch_to("xpath", "//iframe[@id='recDraftManage-tab-iframe']")
			# 刷新，勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[2]/td[2]/div/button')
			sleep(1)
			# 点击审核按钮
			click("xpath", "//span[text()='审核']")
			sleep(1)
			# 点击弹出框的OK键
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			# 票据操作-坏票
			# 切入应收票据管理窗体
			switch_to("xpath", "//iframe[@id='recDraftManage-tab-iframe']")
			# 刷新，勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[2]/td[2]/div/button')
			sleep(1)
			
			triangle_cick("票据操作")
			sleep(1)
			js_click("xpath", "//a[contains(text(),'坏票')]")
			sleep(1)
			switch_to("xpath",'//*[@id="badBillWin-iframe"]')
			span_click("保存")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("应收票据管理，坏票成功！")
			time.sleep(3)
			
			#取消坏票💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入应收票据管理窗体
			switch_to("xpath", "//iframe[@id='recDraftManage-tab-iframe']")
			# 刷新，勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[2]/td[2]/div/button')
			sleep(1)
			
			triangle_cick("票据操作")
			sleep(1)
			js_click("xpath", "//a[contains(text(),'取消坏票')]")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("应收票据管理，取消质押托收成功！")
			time.sleep(3)
			
			
			# 测试退票功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 票据操作-背书
			# 切入应收票据管理窗体
			switch_to("xpath", "//iframe[@id='recDraftManage-tab-iframe']")
			# 刷新，勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[2]/td[2]/div/button')
			sleep(1)
			
			triangle_cick("票据操作")
			sleep(1)
			js_click("xpath", "//a[contains(text(),'票据背书')]")
			sleep(1)
			# 切入背书窗体
			switch_to("xpath", '//*[@id="endorseWin-iframe"]')
			# 被背书对象类型
			input("xpath", '//*[@id="combobox-input-endorsetype"]', '交易对手')
			sleep(1)
			up_enter_click('//*[@id="combobox-input-endorsetype"]')
			
			# 被背书交易对手
			input("xpath", '//*[@id="combobox-input-endorsecounterpartyid"]', '张中国')
			sleep(1)
			
			# 被背书账户
			click("xpath",'//*[@id="combobox-input-endorseaccountnumber"]')
			sleep(1)
			input("xpath", '//*[@id="combobox-input-endorseaccountnumber"]', '200818199619')
			sleep(1)
			
			# 被背书开户银行
			click("xpath", '//*[@id="combobox-input-endorsebanklocationid"]')
			sleep(1)
			up_enter_click('//*[@id="combobox-input-endorsebanklocationid"]')
			
			span_click("背书")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			time.sleep(3)
			#退票操作
			# 切入应收票据管理窗体
			switch_to("xpath", "//iframe[@id='recDraftManage-tab-iframe']")
			# 刷新，勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[2]/td[2]/div/button')
			sleep(1)
			
			triangle_cick("票据操作")
			sleep(1)
			js_click("xpath", "//a[contains(text(),'退票')]")
			switch_to("xpath",'//*[@id="returnedBillWin-iframe"]')
			sleep(1)
			span_click("保存")
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("应收票据管理，退票成功！")
			time.sleep(3)
			
			# 测试票据托管功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入应收票据管理窗体
			switch_to("xpath", "//iframe[@id='recDraftManage-tab-iframe']")
			# 刷新，勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[2]/td[2]/div/button')
			sleep(1)
			
			triangle_cick("票据操作")
			sleep(1)
			js_click("xpath", "//a[contains(text(),'票据托管')]")
			sleep(1)
			switch_to("xpath",'//*[@id="trusteeshipWin-iframe"]')
			today = date.today()
			input("xpath",'//*[@id="trusteeshipdate-input"]',str(today))
			sleep(1)
			span_click("托管")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("应收票据管理，托管成功！")
			time.sleep(3)
			
			# 测试取消托管功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入应收票据管理窗体
			switch_to("xpath", "//iframe[@id='recDraftManage-tab-iframe']")
			# 刷新，勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[2]/td[2]/div/button')
			sleep(1)
			
			triangle_cick("票据操作")
			sleep(1)
			js_click("xpath", "//a[contains(text(),'取消托管')]")
			sleep(1)
			ok_click()
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("应收票据管理，取消托管成功！")
			time.sleep(3)
			
			# 测试贴息功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入应收票据管理窗体
			switch_to("xpath", "//iframe[@id='recDraftManage-tab-iframe']")
			# 刷新，勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[2]/td[2]/div/button')
			sleep(1)
			
			triangle_cick("票据操作")
			sleep(1)
			js_click("xpath", "//a[contains(text(),'贴息')]")
			sleep(1)
			
			switch_to("xpath",'//*[@id="subsidiesWin-iframe"]')
			#贴息日期
			today2 = date.today()
			input("xpath",'//*[@id="operatedate-input"]',str(today2))
			sleep(1)
			keyDown("enter")
			sleep(1)
			
			#贴息率
			input("xpath",'//*[@id="discountrate-input"]','5')
			sleep(1)
			
			#贴息收款账户
			input('xpath','//*[@id="combobox-input-bankaccountid"]','20211005')
			sleep(1)
			up_enter_click('//*[@id="combobox-input-bankaccountid"]')
			
			span_click("贴息")
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("应收票据管理，贴息成功！")
			time.sleep(3)
			
			
			
			# 测试操作记录查看、换票💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			#审核第三笔数据
			# 切入应收票据管理窗体
			switch_to("xpath", "//iframe[@id='recDraftManage-tab-iframe']")
			# 刷新，勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[3]/td[2]/div/button')
			sleep(1)
			span_click("审核")
			ok_click()
			switch_default()
			time.sleep(3)
			
			# 切入应收票据管理窗体
			switch_to("xpath", "//iframe[@id='recDraftManage-tab-iframe']")
			# 刷新，勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[2]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("票据操作",'票据背书')
			# 切入背书窗体
			switch_to("xpath", '//*[@id="endorseWin-iframe"]')
			# 被背书对象类型
			input("xpath", '//*[@id="combobox-input-endorsetype"]', '交易对手')
			sleep(1)
			up_enter_click('//*[@id="combobox-input-endorsetype"]')
			
			# 被背书交易对手
			input("xpath", '//*[@id="combobox-input-endorsecounterpartyid"]', '张中国')
			sleep(1)
			
			# 被背书账户
			click("xpath", '//*[@id="combobox-input-endorseaccountnumber"]')
			sleep(1)
			input("xpath", '//*[@id="combobox-input-endorseaccountnumber"]', '200818199619')
			sleep(1)
			
			# 被背书开户银行
			click("xpath", '//*[@id="combobox-input-endorsebanklocationid"]')
			sleep(1)
			up_enter_click('//*[@id="combobox-input-endorsebanklocationid"]')
			
			span_click("背书")
			# 退出所有iframe窗体
			switch_default()
			time.sleep(3)
			
			# 测试操作记录查看💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入应收票据管理窗体
			switch_to("xpath", "//iframe[@id='recDraftManage-tab-iframe']")
			# 刷新，勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[2]/td[2]/div/button')
			sleep(1)
			
			span_click("操作记录查看")
			switch_to("xpath",'//*[@id="operationWin-iframe"]')
			click("xpath",'//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			span_click("生成交易单")
			sleep(1)
			switch_parent()
			switch_to("xpath",'//*[@id="recmentsWin-iframe"]')
			sleep(1)
			#结算方式
			click("xpath",'//*[@id="combobox-input-settlementmodeid"]')
			sleep(1)
			up_enter_click('//*[@id="combobox-input-settlementmodeid"]')
			
			span_click("保存")
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("应收票据管理，操作记录查看！")
			time.sleep(3)
			
			# 换票💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入应收票据管理窗体
			switch_to("xpath", "//iframe[@id='recDraftManage-tab-iframe']")
			# 刷新，勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[2]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("票据操作",'换票')
			switch_to("xpath",'//*[@id="replaceWin-iframe"]')
			click("xpath",'//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			span_click("确定")
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("应收票据管理，换票成功！")
			time.sleep(3)
			
			# 收票生成交易单💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入应收票据管理窗体
			switch_to("xpath", "//iframe[@id='recDraftManage-tab-iframe']")
			# 刷新，勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[2]/td[2]/div/button')
			sleep(1)
			span_click("收票生成交易单")
			switch_to("xpath", '//*[@id="receiveGenRecmentWin-iframe"]')
			sleep(1)
			span_click("确认")
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("应收票据管理，收票生成交易单成功！")
			time.sleep(3)
			
			# 入账💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入应收票据管理窗体
			switch_to("xpath", "//iframe[@id='recDraftManage-tab-iframe']")
			# 刷新，勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[2]/td[2]/div/button')
			sleep(1)
			
			span_click("入账")
			
			switch_to("xpath",'//*[@id="entryaccountWin-iframe"]')
			click("xpath",'//*[@id="grid-body-table"]/tbody/tr/td[2]')
			sleep(1)
			span_click("入账")
			
			switch_to("xpath", "//iframe[@id='entryaccountWin-iframe']")
			sleep(1)
			#业务员
			input("xpath", "//input[@id='salesman']", "张中国")
			sleep(1)
			#收款银行账号
			input("xpath",'//*[@id="combobox-input-bankaccountid"]','20211005')
			sleep(1)
			up_enter_click('//*[@id="combobox-input-bankaccountid"]')
			
			span_click("保存")
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("应收票据管理，入账成功！")
			span_click("应收票据管理")
			time.sleep(3)
			
			# 批量筛选票据💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入应收票据管理窗体
			switch_to("xpath", "//iframe[@id='recDraftManage-tab-iframe']")
			span_click("批量筛选票据")
			#票据号
			input("xpath",'//*[@id="selectdraftcodes"]','20')
			sleep(1)
			span_click("确定")
			sleep(3)
			print("应收票据管理，批量筛选票据成功！")
			
			# 点击承兑汇票管理，收回菜单
			switch_default()
			click("xpath", "//span[@title='承兑汇票管理']")
			sleep(1)
			
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("承兑汇票管理失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		 
		
		# 测试应付票据管理💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
		try:
			logger.info("开始测试票据管理-承兑汇票管理-应付票据管理")
			# 点击承兑汇票管理
			click("xpath", "//span[@title='承兑汇票管理']")
			sleep(1)
			# 点击应付支票登记菜单
			click("xpath", "//span[@title='应付票据管理']")
			
			sleep(1)
			# 退出所有的iframe窗体
			switch_default()
			
			# 测试新增功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			for i in range (1,5):
				switch_to("xpath",'//*[@id="payDraftManage-tab-iframe"]')
				span_click("新增")
				
				#切入新增窗体
				switch_to("xpath",'//*[@id="addWin-iframe"]')
				
				#票据类型
				input("xpath",'//*[@id="combobox-input-drafttype"]','109-银行承兑汇票')
				sleep(1)
				up_enter_click('//*[@id="combobox-input-drafttype"]')
				
				#票据号
				YFPJH = time.strftime("%Y%m%d%H%M%S")
				input("xpath",'//*[@id="draftcode"]',YFPJH)
				sleep(1)
				
				#承兑银行
				input("xpath",'//*[@id="combobox-input-paybankid"]','BOC-中国银行')
				sleep(1)
				up_enter_click('//*[@id="combobox-input-paybankid"]')
				
				#外部收款单位
				input('xpath','//*[@id="combobox-input-reccounterpartyid"]','浙江华语科技')
				sleep(1)
				
				#付款期限
				double_click("xpath",'//*[@id="terms-input"]')
				sleep(1)
				input("xpath",'//*[@id="terms-input"]','60')
				sleep(1)
				
				#票面金额
				money =random.randint(100,300)
				double_click("xpath",'//*[@id="draftamount-input"]')
				sleep(1)
				input("xpath",'//*[@id="draftamount-input"]',str(money))
				sleep(1)
				
				if i == 1 :
					# 保证金担保方式
					input("xpath", '//*[@id="combobox-input-bailtype"]', '一定比例保证金')
					sleep(1)
					up_enter_click('//*[@id="combobox-input-bailtype"]')
					
					#授信协议
					input("xpath",'//*[@id="combobox-input-creditid"]','XYH5555')
					sleep(1)
					up_enter_click('//*[@id="combobox-input-creditid"]')
				else :
					# 保证金担保方式
					input("xpath", '//*[@id="combobox-input-bailtype"]', '票据质押保证')
					sleep(1)
					up_enter_click('//*[@id="combobox-input-bailtype"]')
				
				if i ==3 :
					print("应付票据管理，新增成功")
				span_click("保存")
				switch_default()
				sleep(3)

			# 测试修改功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="payDraftManage-tab-iframe"]')
			#刷新、勾选按钮
			click("xpath",'//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[3]/td[2]/div/button')
			sleep(1)
			
			span_click("修改")
			
			switch_to("xpath",'//*[@id="modWin-iframe"]')
			clear("xpath",'//*[@id="combobox-input-drafttype"]')
			sleep(1)
			input("xpath",'//*[@id="combobox-input-drafttype"]','205-商业承兑汇票')
			sleep(1)
			up_enter_click('//*[@id="combobox-input-drafttype"]')
			
			span_click("保存")
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("应付票据管理，修改成功！")
			time.sleep(3)
			
			# 测试删除功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="payDraftManage-tab-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("删除")
			ok_click()
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("应付票据管理，删除成功！")
			time.sleep(3)
			

			# 测试审核、取消审核功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="payDraftManage-tab-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("审核")
			ok_click()
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("应付票据管理，审核成功！")
			time.sleep(3)
			
			# 测取消审核功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="payDraftManage-tab-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("审核",'取消审核')
			ok_click()
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("应付票据管理，取消审核成功！")
			time.sleep(3)
			
			# 再次审核做数据💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="payDraftManage-tab-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("审核")
			ok_click()
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			time.sleep(3)
			
			switch_to("xpath", '//*[@id="payDraftManage-tab-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[2]/td[2]/div/button')
			sleep(1)
			
			span_click("审核")
			ok_click()
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			time.sleep(3)
			
			# 测试票据出票💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="payDraftManage-tab-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("票据操作",'票据出票')
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("应付票据管理，票据出票成功！")
			time.sleep(3)
			
			# 测试取消出票💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="payDraftManage-tab-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("票据操作", '取消出票')
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("应付票据管理，取消出票成功！")
			time.sleep(3)
			
			# 测试保证贴现💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="payDraftManage-tab-iframe"]')
			
			# 刷新、勾选按钮（对数据出票）
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[2]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("票据操作", '票据出票')
			sleep(3)
			
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[2]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("票据操作", '保证贴现')
			switch_to("xpath",'//*[@id="ensureDiscountWin-iframe"]')
			#授信协议
			input("xpath",'//*[@id="combobox-input-creditid"]','XYH5555')
			sleep(1)
			up_enter_click('//*[@id="combobox-input-creditid"]')
			
			span_click("保存")
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("应付票据管理，保证贴现成功！")
			time.sleep(3)
			
			# 测试取消保贴💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="payDraftManage-tab-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[2]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("票据操作", '取消保贴')
			ok_click()
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'票据取消保贴成功！')]")
			print("应付票据管理，取消保贴成功！")
			time.sleep(3)
			
			# 测试到期付款💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="payDraftManage-tab-iframe"]')
			# 刷新、勾选按钮（对数据进行出票）
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("票据操作", '票据出票')
			sleep(3)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("票据操作", '到期付款')
			span_click("确定")
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("应付票据管理，到期付款成功！")
			time.sleep(3)
			
			# 测试取消付款💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="payDraftManage-tab-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("票据操作", '取消付款')
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("应付票据管理，取消付款成功！")
			time.sleep(3)
			
			# 测试退票💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="payDraftManage-tab-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("票据操作", '退票')
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("应付票据管理，退票成功！")
			time.sleep(3)
			
			# 测试取消退票💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="payDraftManage-tab-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("票据操作", '取消退票')
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("应付票据管理，取消退票成功！")
			time.sleep(3)
			
			# 测试操作记录查看、生成交易单💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="payDraftManage-tab-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("票据操作", '到期付款')
			span_click("确定")
			sleep(3)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("操作记录查看")
			switch_to("xpath",'//*[@id="operationWin-iframe"]')
			#勾选数据
			click("xpath",'//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			span_click("生成交易单")
			
			switch_parent()
			switch_to("xpath",'//*[@id="otherPayWin-iframe"]')
			sleep(1)
			
			#交易类型
			input("xpath",'//*[@id="combobox-input-paytypeid"]','103-对外付款')
			sleep(1)
			up_enter_click('//*[@id="combobox-input-paytypeid"]')
			
			# 结算方式
			input("xpath", '//*[@id="combobox-input-settlementmodeid"]', '601-其他支付')
			sleep(1)
			up_enter_click('//*[@id="combobox-input-settlementmodeid"]')
			
			#付方账户
			click("xpath",'//*[@id="combobox-input-ourbankaccountid"]')
			sleep(1)
			up_enter_click('//*[@id="combobox-input-ourbankaccountid"]')
			
			span_click("保存")
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("应付票据管理，操作记录查看、生成交易单成功！")
			time.sleep(3)
			
			# 测试保证金登记💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="payDraftManage-tab-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[3]/td[2]/div/button')
			sleep(1)
			
			span_click("审核")
			ok_click()
			sleep(3)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[3]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("票据操作",'票据出票')
			sleep(3)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[3]/td[2]/div/button')
			sleep(1)
			
			span_click("保证金登记")
			switch_to("xpath",'//*[@id="registerBailsWin-iframe"]')
			span_click("保证金登记")
		
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("应付票据管理，保证金登记成功")
			time.sleep(3)
			
			# 点击承兑汇票管理，收回菜单
			click("xpath", "//span[@title='承兑汇票管理']")
			sleep(1)
			
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("应付票据管理失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		
		
		# 测试应收票据查看💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
		try:
			logger.info("开始测试票据管理-承兑汇票管理-应收票据查看")
			# 点击承兑汇票管理
			click("xpath", "//span[@title='承兑汇票管理']")
			sleep(1)
			# 点击应付支票登记菜单
			click("xpath", "//span[@title='应收票据查看']")
			sleep(1)
			# 退出所有的iframe窗体
			switch_default()
			
			# 票据信息查看💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath",'//*[@id="recDraftView-tab-iframe"]')
			switch_to("xpath",'//*[@id="subTabOne-iframe"]')
			implici_wait("xpath","//div[text()='浙江华语科技']")
			switch_default()
			print("应收票据查看，票据信息查看成功")
			sleep(3)
			# 票据操作查看💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="recDraftView-tab-iframe"]')
			span_click("票据操作查看")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			implici_wait("xpath", "//div[text()='CNY-人民币']")
			switch_default()
			print("应收票据查看，票据操作查看")
			sleep(3)
			
			# 点击支票管理菜单，收回菜单
			click("xpath", "//span[@title='承兑汇票管理']")
			sleep(1)
			
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("应收票据查看失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
	
		# 测试应付票据查看💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
		try:
			logger.info("开始测试票据管理-承兑汇票管理-应付票据查看")
			# 点击承兑汇票管理
			click("xpath", "//span[@title='承兑汇票管理']")
			sleep(1)
			# 点击应付支票登记菜单
			click("xpath", "//span[@title='应付票据查看']")
			sleep(1)
			# 退出所有的iframe窗体
			switch_default()
			
			# 票据信息查看💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="payDraftView-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			implici_wait("xpath", "//div[text()='BOC-中国银行']")
			switch_default()
			print("应收票据查看，票据信息查看成功")
			sleep(3)
			# 票据操作查看💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="payDraftView-tab-iframe"]')
			span_click("票据操作查看")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			implici_wait("xpath", "//div[text()='CNY-人民币']")
			switch_default()
			print("应付票据查看，票据操作查看")
			sleep(3)
			
			# 点击支票管理菜单，收回菜单
			click("xpath", "//span[@title='承兑汇票管理']")
			sleep(1)
			
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("应付票据查看失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		
		
		# 测试托管票据查看💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
		try:
			logger.info("开始测试票据管理-承兑汇票管理-托管票据查看")
			# 点击承兑汇票管理
			click("xpath", "//span[@title='承兑汇票管理']")
			sleep(1)
			# 点击应付支票登记菜单
			click("xpath", "//span[@title='托管票据查看']")
			sleep(1)
			# 退出所有的iframe窗体
			switch_default()
			
			# 托管应付票据查看💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="depositview-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			implici_wait("xpath", "//div[text()='BOC-中国银行']")
			switch_default()
			print("托管票据查看，托管应付票据查看成功")
			sleep(3)
			
			# 托管应收票据查看💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="depositview-tab-iframe"]')
			span_click("托管应收票据查看")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			implici_wait("xpath", "//div[text()='浙江华语科技']")
			switch_default()
			print("托管票据查看，托管应收票据查看成功")
			sleep(3)
			
			# 点击支票管理菜单，收回菜单
			click("xpath", "//span[@title='承兑汇票管理']")
			sleep(1)
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("应付票据查看失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		
		
		# 测试信用证收证管理💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
		try:
			logger.info("开始测试票据管理--信用证管理--信用证收证管理")
			# 点击承兑汇票管理
			click("xpath", "//span[@title='信用证管理']")
			sleep(1)
			# 点击应付支票登记菜单
			click("xpath", "//span[@title='信用证收证管理']")
			sleep(1)
			# 退出所有的iframe窗体
			switch_default()
			
			# 新增💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			for i in range(1,4):
				# 切入‘信用证收证管理’的iframe窗体
				switch_to("xpath", "//iframe[@id='expLOCredits-tab-iframe']")
				js_click("xpath", "//span[text()='新增']")
				sleep(1)
				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='addWin-iframe']")
				
				# 融资产品
				input("xpath", "//input[@id='combobox-input-credittypeid']", "104-信用证收证")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-credittypeid']")
				input_enter("xpath", "//input[@id='combobox-input-credittypeid']")
				time.sleep(1)
				
				# 信用证号码
				XYZHM = time.strftime("%Y%m%d%H%M%S")
				input("xpath",'//*[@id="creditnumber"]',str(XYZHM))
				sleep(1)
				
				# 输入开证金额
				XYZJE=random.randint(100,300)
				input("xpath", '//*[@id="amount-input"]', XYZJE)
				sleep(1)
				
				# 输入开证币种
				input("xpath", "//input[@id='combobox-input-currencyid']", "CNY-人民币")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-currencyid']")
				input_enter("xpath", "//input[@id='combobox-input-currencyid']")
				time.sleep(1)
				
				# 输入开证方
				input("xpath", "//input[@id='issuefactory']", "浙江华语科技")
				sleep(1)
				
				#折美元汇率
				double_click("xpath",'//*[@id="dollarrate-input"]')
				sleep(1)
				input("xpath",'//*[@id="dollarrate-input"]','6.3')
				sleep(1)
				
				
				# 输入截止日期
				today = date.today()
				expirydate = today + timedelta(days=720)
				click("xpath", "//input[@id='expirydate-input']")
				sleep(1)
				clear("xpath", "//input[@id='expirydate-input']")
				sleep(1)
				input("xpath", "//input[@id='expirydate-input']", str(expirydate))
				# 模拟回车键
				keyDown('enter')
				keyUp('enter')
				time.sleep(1)
				
				# 输入溢短
				click("xpath", "//input[@id='overflowratio-input']")
				sleep(1)
				clear("xpath", "//input[@id='overflowratio-input']")
				sleep(1)
				input("xpath", "//input[@id='overflowratio-input']", "5")
				sleep(1)
				
				# 点击保存按钮
				click("xpath", "//span[text()='保存']")
				
				# 退出所有iframe窗体
				switch_default()
				# 用隐式等待方法等页面出现提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				if i ==3 :
					print("信用证收证管理，新增成功")
				time.sleep(3)
				
			# 修改功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入‘信用证收证管理’的iframe窗体
			switch_to("xpath", "//iframe[@id='expLOCredits-tab-iframe']")
			#刷新、勾选按钮
			click("xpath",'//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath",'//*[@id="grid-body-table"]/tbody/tr[3]/td[2]/div/button')
			sleep(1)
			
			span_click("修改")
			# 切入修改的iframe窗体
			switch_to("xpath", "//iframe[@id='modWin-iframe']")
			#远期
			click("xpath",'//*[@id="isforwards"]')
			sleep(1)
			#远期天数
			input("xpath",'//*[@id="forwarddays-input"]','60')
			sleep(1)
			
			# 点击保存按钮
			click("xpath", "//span[text()='保存']")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("信用证收证管理，修改成功！")
			time.sleep(3)
			
			# 删除功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入‘信用证收证管理’的iframe窗体
			switch_to("xpath", "//iframe[@id='expLOCredits-tab-iframe']")
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
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
			implici_wait("xpath", "//span[contains(text(),'信用证收证成功删除1条!')]")
			print("信用证收证管理，删除成功！")
			time.sleep(3)
			
			# 审核、取消审核功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入‘信用证收证管理’的iframe窗体
			switch_to("xpath", "//iframe[@id='expLOCredits-tab-iframe']")
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
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
			implici_wait("xpath", "//span[contains(text(),'审核成功！')]")
			print("信用证收证管理，审核成功！")
			time.sleep(3)
			
			# 取消审核功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入‘信用证收证管理’的iframe窗体
			switch_to("xpath", "//iframe[@id='expLOCredits-tab-iframe']")
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
		
			triangle_cick_and_element("审核",'取消审核')
			ok_click()
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'取消审核成功！')]")
			print("信用证收证管理，取消审核成功！")
			time.sleep(3)
			
			# 终止、取消终止功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入‘信用证收证管理’的iframe窗体
			switch_to("xpath", "//iframe[@id='expLOCredits-tab-iframe']")
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
		
			span_click("终止")
			ok_click()
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'终止成功！')]")
			print("信用证收证管理，终止成功！")
			time.sleep(3)
			
			# 取消终止功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入‘信用证收证管理’的iframe窗体
			switch_to("xpath", "//iframe[@id='expLOCredits-tab-iframe']")
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("终止",'取消终止')
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'取消终止成功')]")
			print("信用证收证管理，取消终止成功！")
			time.sleep(3)
			
			# 交单功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入‘信用证收证管理’的iframe窗体
			switch_to("xpath", "//iframe[@id='expLOCredits-tab-iframe']")
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("审核")
			ok_click()
			sleep(3)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			span_click("交单")
			switch_to("xpath",'//*[@id="deliverWin-iframe"]')
			span_click("保存")
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'交单成功！')]")
			print("信用证收证管理，交单成功！")
			time.sleep(3)
			
			# 取消交单功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入‘信用证收证管理’的iframe窗体
			switch_to("xpath", "//iframe[@id='expLOCredits-tab-iframe']")
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("交单",'取消交单')
			ok_click()
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'取消交单成功！')]")
			print("信用证收证管理，交单成功！")
			time.sleep(3)
			
			# 变更功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入‘信用证收证管理’的iframe窗体
			switch_to("xpath", "//iframe[@id='expLOCredits-tab-iframe']")
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("交单")
			switch_to("xpath",'//*[@id="deliverWin-iframe"]')
			span_click("保存")
			switch_parent()
			sleep(3)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("变更")
			switch_to("xpath",'//*[@id="changeWin-iframe"]')
			#描述
			input("xpath",'//*[@id="description"]','测试变更')
			sleep(1)
			span_click("变更")
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("信用证收证管理，变更成功！")
			time.sleep(3)
			
			# 收汇功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入‘信用证收证管理’的iframe窗体
			switch_to("xpath", "//iframe[@id='expLOCredits-tab-iframe']")
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("到单处理",'收汇')
			switch_to("xpath",'//*[@id="opWin-iframe"]')
			
			#金额
			double_click("xpath",'//*[@id="opamount-input"]')
			sleep(1)
			input("xpath",'//*[@id="opamount-input"]','10')
			sleep(1)
			span_click("保存")
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("信用证收证管理，收汇成功！")
			time.sleep(3)
			
			# 押汇功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入‘信用证收证管理’的iframe窗体
			switch_to("xpath", "//iframe[@id='expLOCredits-tab-iframe']")
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("到单处理", '押汇')
			switch_to("xpath", '//*[@id="opWin-iframe"]')
			# 金额
			double_click("xpath", '//*[@id="opamount-input"]')
			sleep(1)
			input("xpath", '//*[@id="opamount-input"]', '10')
			sleep(1)
			span_click("保存")
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("信用证收证管理，押汇成功！")
			time.sleep(3)
			
			# 远期结汇功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入‘信用证收证管理’的iframe窗体
			switch_to("xpath", "//iframe[@id='expLOCredits-tab-iframe']")
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("到单处理", '远期结汇')
			switch_to("xpath", '//*[@id="opWin-iframe"]')
			# 金额
			double_click("xpath", '//*[@id="opamount-input"]')
			sleep(1)
			input("xpath", '//*[@id="opamount-input"]', '10')
			sleep(1)
			span_click("保存")
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("信用证收证管理，远期结汇成功！")
			time.sleep(3)
			
			# 贴现功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入‘信用证收证管理’的iframe窗体
			switch_to("xpath", "//iframe[@id='expLOCredits-tab-iframe']")
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("到单处理", '贴现')
			switch_to("xpath", '//*[@id="opWin-iframe"]')
			# 金额
			double_click("xpath", '//*[@id="opamount-input"]')
			sleep(1)
			input("xpath", '//*[@id="opamount-input"]', '10')
			sleep(1)
			span_click("保存")
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("信用证收证管理，贴现成功！")
			time.sleep(3)
			
			# 福费廷功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入‘信用证收证管理’的iframe窗体
			switch_to("xpath", "//iframe[@id='expLOCredits-tab-iframe']")
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("到单处理", '福费廷')
			switch_to("xpath", '//*[@id="opWin-iframe"]')
			# 金额
			double_click("xpath", '//*[@id="opamount-input"]')
			sleep(1)
			input("xpath", '//*[@id="opamount-input"]', '10')
			sleep(1)
			span_click("保存")
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("信用证收证管理，福费廷成功！")
			time.sleep(3)
			
			# 客户承兑功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入‘信用证收证管理’的iframe窗体
			switch_to("xpath", "//iframe[@id='expLOCredits-tab-iframe']")
			# 刷新、勾选按钮、审核
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[2]/td[2]/div/button')
			sleep(1)
			span_click("审核")
			ok_click()
			sleep(3)
			
			# 刷新、勾选按钮、交单
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[2]/td[2]/div/button')
			sleep(1)
			span_click("交单")
			switch_to("xpath", '//*[@id="deliverWin-iframe"]')
			span_click("保存")
			switch_parent()
			sleep(3)
			
			# 刷新、勾选按钮、客户承兑
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[2]/td[2]/div/button')
			sleep(1)
			triangle_cick_and_element("到单处理", '客户承兑')
			switch_to("xpath", '//*[@id="opWin-iframe"]')
			# 金额
			double_click("xpath", '//*[@id="opamount-input"]')
			sleep(1)
			input("xpath", '//*[@id="opamount-input"]', '10')
			sleep(1)
			span_click("保存")
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("信用证收证管理，客户承兑成功！")
			time.sleep(3)
			
			#操作记录功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入‘信用证收证管理’的iframe窗体
			switch_to("xpath", "//iframe[@id='expLOCredits-tab-iframe']")
			# 刷新、勾选按钮、审核
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("操作记录")
			switch_to("xpath",'//*[@id="opdetailWin-iframe"]')
			
			#勾选按钮、点击功能
			click("xpath",'//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			span_click("取消福费廷")
			ok_click()
			print("信用证收证管理，取消福费廷成功")
			sleep(3)
			
			# 勾选按钮、点击功能
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[3]/td[2]/div/button')
			sleep(1)
			span_click("取消贴现")
			ok_click()
			print("信用证收证管理，取消贴现成功")
			sleep(3)
			
			# 勾选按钮、点击功能
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[5]/td[2]/div/button')
			sleep(1)
			span_click("取消远期结汇")
			ok_click()
			print("信用证收证管理，取消远期结汇成功")
			sleep(3)
			
			# 勾选按钮、点击功能
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[7]/td[2]/div/button')
			sleep(1)
			span_click("取消押汇")
			ok_click()
			print("信用证收证管理，取消押汇成功")
			sleep(3)
			
			# 勾选按钮、点击功能
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[9]/td[2]/div/button')
			sleep(1)
			span_click("取消收汇")
			ok_click()
			print("信用证收证管理，取消收汇成功")
			switch_default()
			span_click("信用证收证管理")
			sleep(3)
			
			# 操作记录功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入‘信用证收证管理’的iframe窗体
			switch_to("xpath", "//iframe[@id='expLOCredits-tab-iframe']")
			# 刷新、勾选按钮、审核
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[2]/td[2]/div/button')
			sleep(1)
			
			span_click("操作记录")
			switch_to("xpath", '//*[@id="opdetailWin-iframe"]')
			
			# 勾选按钮、点击功能
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			span_click("取消承兑")
			ok_click()
			print("信用证收证管理，取消承兑")
			sleep(3)
			
			#点击信用证管理，收回窗体
			switch_default()
			click("xpath", "//span[@title='信用证管理']")
			sleep(1)
			
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("信用证收证管理失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		
		
		# 测试信用证收证查看💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
		try:
			logger.info("开始测试票据管理--信用证管理--信用证收证查看")
			# 点击承兑汇票管理
			click("xpath", "//span[@title='信用证管理']")
			sleep(1)
			# 点击应付支票登记菜单
			click("xpath", "//span[@title='信用证收证查看']")
			sleep(1)
			# 退出所有的iframe窗体
			switch_default()
			
			#切入信用证收证查看窗体
			switch_to("xpath",'//*[@id="expLOCreditsView-tab-iframe"]')
			implici_wait("xpath","//div[text()='CNY-人民币']")
			print("信用证收证查看,查看成功")
			#收回窗体
			switch_default()
			span_click("信用证管理")
			
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("信用证收证查看失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		
		
		# 测试信用证开证管理💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
		try:
			logger.info("开始测试票据管理--信用证管理--信用证开证管理")
			# 点击承兑汇票管理
			click("xpath", "//span[@title='信用证管理']")
			sleep(1)
			# 点击应付支票登记菜单
			click("xpath", "//span[@title='信用证开证管理']")
			sleep(1)
			# 退出所有的iframe窗体
			switch_default()
			
			
			# 测试新增💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			for i in range (1,5):
				#切入信用证开证管理窗体
				switch_to("xpath",'//*[@id="impLOCredits-tab-iframe"]')
				span_click("新增")
				switch_to("xpath",'//*[@id="addWin-iframe"]')
				
				#融资产品
				input("xpath",'//*[@id="combobox-input-credittypeid"]','105-信用证开证')
				sleep(1)
				up_enter_click('//*[@id="combobox-input-credittypeid"]')
				
				#信用证号码
				XYZHM=time.strftime("%Y%m%d%H%M%S")
				input("xpath",'//*[@id="creditnumber"]',XYZHM)
				sleep(1)
				
				#开证银行
				input("xpath",'//*[@id="combobox-input-issuingbankid"]','BOC-中国银行')
				sleep(1)
				up_enter_click('//*[@id="combobox-input-issuingbankid"]')
				
				#开证金额
				KZJE=random.randint(100,300)
				double_click("xpath",'//*[@id="amount-input"]')
				sleep(1)
				input("xpath",'//*[@id="amount-input"]',str(KZJE))
				sleep(1)
				
				#开证币种
				input("xpath",'//*[@id="combobox-input-currencyid"]','CNY-人民币')
				sleep(1)
				up_enter_click('//*[@id="combobox-input-currencyid"]')
				
				#折美元汇率
				double_click("xpath",'//*[@id="dollarrate-input"]')
				sleep(1)
				input("xpath",'//*[@id="dollarrate-input"]','6.3')
				sleep(1)
				
				# 输入截止日期
				today = date.today()
				expirydate = today + timedelta(days=60)
				click("xpath", "//input[@id='expirydate-input']")
				sleep(1)
				clear("xpath", "//input[@id='expirydate-input']")
				sleep(1)
				input("xpath", "//input[@id='expirydate-input']", str(expirydate))
				sleep(1)
				# 模拟回车键
				keyDown('enter')
				keyUp('enter')
				time.sleep(1)
				
				#授信协议
				input("xpath",'//*[@id="combobox-input-creditid"]','XYH5555')
				sleep(1)
				up_enter_click('//*[@id="combobox-input-creditid"]')
				
				#溢短
				double_click("xpath",'//*[@id="overflowratio-input"]')
				sleep(1)
				input("xpath",'//*[@id="overflowratio-input"]','5')
				sleep(1)
				span_click("保存")
				
				# 退出所有iframe窗体
				switch_default()
				
				# 用隐式等待方法等页面出现提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				if i ==4 :
					print("信用证开证管理，新增成功！")
				time.sleep(3)
			
			# 测试删除💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入信用证开证管理窗体
			switch_to("xpath", '//*[@id="impLOCredits-tab-iframe"]')
			#刷新、勾选按钮
			click("xpath",'//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("删除")
			ok_click()
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'信用证成功删除1条!')]")
			print("信用证开证管理，删除成功！")
			time.sleep(3)
			
			# 测试审核💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入信用证开证管理窗体
			switch_to("xpath", '//*[@id="impLOCredits-tab-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("审核")
			ok_click()
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'审核成功！')]")
			print("信用证开证管理，审核成功！")
			time.sleep(3)
			
			# 测试取消审核💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入信用证开证管理窗体
			switch_to("xpath", '//*[@id="impLOCredits-tab-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("审核",'取消审核')
			ok_click()
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'取消审核成功！')]")
			print("信用证开证管理，取消审核成功！")
			time.sleep(3)
			
			# 测试审核并开证💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入信用证开证管理窗体
			switch_to("xpath", '//*[@id="impLOCredits-tab-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("审核",'审核并开证')
			ok_click()
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'开证成功！')]")
			print("信用证开证管理，审核并开证成功！")
			time.sleep(3)
			
			# 测试终止💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入信用证开证管理窗体
			switch_to("xpath", '//*[@id="impLOCredits-tab-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("终止")
			ok_click()
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'终止成功！')]")
			print("信用证开证管理，终止成功！")
			time.sleep(3)
			
			# 测试取消终止💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入信用证开证管理窗体
			switch_to("xpath", '//*[@id="impLOCredits-tab-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("终止",'取消终止')
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'取消终止成功！')]")
			print("信用证开证管理，取消终止成功！")
			time.sleep(3)
			
			# 测试取消开证💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入信用证开证管理窗体
			switch_to("xpath", '//*[@id="impLOCredits-tab-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("开证", '取消开证')
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'取消开证成功！')]")
			print("信用证开证管理，取消开证成功！")
			time.sleep(3)
			
			# 测试开证💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入信用证开证管理窗体
			switch_to("xpath", '//*[@id="impLOCredits-tab-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("开证")
			ok_click()
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'开证成功！')]")
			print("信用证开证管理，开证成功！")
			time.sleep(3)
			
			# 测试变更💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入信用证开证管理窗体
			switch_to("xpath", '//*[@id="impLOCredits-tab-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("变更")
			switch_to("xpath",'//*[@id="changeWin-iframe"]')
			input('xpath','//*[@id="description"]','测试变更')
			sleep(1)
			
			span_click("变更")
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("信用证开证管理，变更成功！")
			time.sleep(3)
			
			# 测试付汇💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入信用证开证管理窗体
			switch_to("xpath", '//*[@id="impLOCredits-tab-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("到单处理",'付汇')
			switch_to("xpath",'//*[@id="operateWin-iframe"]')
			#金额
			double_click("xpath",'//*[@id="amount-input"]')
			sleep(1)
			input("xpath",'//*[@id="amount-input"]','10')
			sleep(1)
			span_click("确定")
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("信用证开证管理，付汇成功！")
			time.sleep(3)
			
			# 测试押汇💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入信用证开证管理窗体
			switch_to("xpath", '//*[@id="impLOCredits-tab-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("到单处理", '押汇')
			switch_to("xpath", '//*[@id="operateWin-iframe"]')
			# 金额
			double_click("xpath", '//*[@id="amount-input"]')
			sleep(1)
			input("xpath", '//*[@id="amount-input"]', '10')
			sleep(1)
			span_click("确定")
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("信用证开证管理，押汇成功！")
			time.sleep(3)
			
			# 测试到单登记💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入信用证开证管理窗体
			switch_to("xpath", '//*[@id="impLOCredits-tab-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("到单处理", '到单登记')
			switch_to("xpath", '//*[@id="operateWin-iframe"]')
			# 金额
			double_click("xpath", '//*[@id="amount-input"]')
			sleep(1)
			input("xpath", '//*[@id="amount-input"]', '15')
			sleep(1)
			span_click("确定")
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("信用证开证管理，到单登记成功！")
			time.sleep(3)
			
			# 测试修改💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入信用证开证管理窗体
			switch_to("xpath", '//*[@id="impLOCredits-tab-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[2]/td[2]/div/button')
			sleep(1)
			
			span_click("修改")
			switch_to("xpath",'//*[@id="modWin-iframe"]')
			#远期
			click("xpath",'//*[@id="isforwards"]')
			sleep(1)
			#远期天数
			input("xpath",'//*[@id="forwarddays-input"]','60')
			sleep(1)
			span_click("保存")
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("信用证开证管理，修改成功！")
			time.sleep(3)
			
			# 测试承兑💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入信用证开证管理窗体
			switch_to("xpath", '//*[@id="impLOCredits-tab-iframe"]')
			# 刷新、勾选按钮、审核并开证
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[2]/td[2]/div/button')
			sleep(1)
			triangle_cick_and_element("审核",'审核并开证')
			ok_click()
			sleep(3)
			
			# 刷新、勾选按钮、到单登记
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[2]/td[2]/div/button')
			sleep(1)
			triangle_cick_and_element("到单处理", '到单登记')
			switch_to("xpath", '//*[@id="operateWin-iframe"]')
			# 金额
			double_click("xpath", '//*[@id="amount-input"]')
			sleep(1)
			input("xpath", '//*[@id="amount-input"]', '20')
			sleep(1)
			span_click("确定")
			switch_parent()
			sleep(3)
			
			# 刷新、勾选按钮、承兑
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[2]/td[2]/div/button')
			sleep(1)
			triangle_cick_and_element("到单处理", '承兑')
			switch_to("xpath", '//*[@id="operateWin-iframe"]')
			# 金额
			double_click("xpath", '//*[@id="amount-input"]')
			sleep(1)
			input("xpath", '//*[@id="amount-input"]', '10')
			sleep(1)
			span_click("确定")
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("信用证开证管理，承兑成功！")
			time.sleep(3)
			
			# 测试保证金登记💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入信用证开证管理窗体
			switch_to("xpath", '//*[@id="impLOCredits-tab-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("保证金登记")
			switch_to("xpath",'//*[@id="registerBailsWin-iframe"]')
			span_click("新增行")
			#付款日期
			FKRQ = date.today()
			click("xpath",'//*[@id="bailgrid-paydate-0-input"]')
			sleep(1)
			input("xpath",'//*[@id="bailgrid-paydate-0-input"]',str(FKRQ))
			sleep(1)
			keyDown('enter')
			
			#保证金账户
			input("xpath",'//*[@id="combobox-input-bailgrid-accountid-0"]','20211005')
			sleep(1)
			up_enter_click('//*[@id="combobox-input-bailgrid-accountid-0"]')
			sleep(1)
			
			#保证金原币金额
			double_click("xpath",'//*[@id="bailgrid-bailsourceamount-0-input"]')
			sleep(1)
			input("xpath",'//*[@id="bailgrid-bailsourceamount-0-input"]','10')
			sleep(1)
			
			#保证金币种
			input("xpath",'//*[@id="combobox-input-bailgrid-currencyid-0"]','CNY-人民币')
			sleep(1)
			up_enter_click('//*[@id="combobox-input-bailgrid-currencyid-0"]')
			
			# 保证金比例
			double_click("xpath", '//*[@id="bailgrid-bailrate-0-input"]')
			sleep(1)
			input("xpath", '//*[@id="bailgrid-bailrate-0-input"]', '5')
			sleep(1)
			
			span_click("保证金登记")
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("信用证开证管理，保证金登记成功！")
			time.sleep(3)
			
			# 测试报关单登记💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入信用证开证管理窗体
			switch_to("xpath", '//*[@id="impLOCredits-tab-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("报关单登记")
			switch_to("xpath", '//*[@id="registerDeclarationsWin-iframe"]')
			sleep(1)
			span_click("新增行")
			
			#报关单号
			BGDH = time.strftime("%Y%m%d%S")
			input("xpath",'//*[@id="declarationsgrid-declarationnumber-0"]',str(BGDH))
			sleep(1)
			
			#报关日期
			BGRQ = date.today()
			click("xpath", '//*[@id="declarationsgrid-declarationdate-0-input"]')
			sleep(1)
			input("xpath", '//*[@id="declarationsgrid-declarationdate-0-input"]', str(BGRQ))
			sleep(1)
			keyDown('enter')
			
			#金额
			double_click("xpath", '//*[@id="declarationsgrid-declarationamount-0-input"]')
			sleep(1)
			input("xpath", '//*[@id="declarationsgrid-declarationamount-0-input"]', '5')
			sleep(1)
			
			# 币种
			input("xpath", '//*[@id="combobox-input-declarationsgrid-currencyid-0"]', 'CNY-人民币')
			sleep(1)
			up_enter_click('//*[@id="combobox-input-declarationsgrid-currencyid-0"]')
			
			span_click("报关单登记")
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("信用证开证管理，报关单成功！")
			time.sleep(3)
			
			# 测试结清💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入信用证开证管理窗体
			switch_to("xpath", '//*[@id="impLOCredits-tab-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("结清")
			ok_click()
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("信用证开证管理，结清成功！")
			time.sleep(3)
			
			# 测试关联收证💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入信用证开证管理窗体
			switch_to("xpath", '//*[@id="impLOCredits-tab-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[3]/td[2]/div/button')
			sleep(1)
			
			span_click("修改")
			switch_to("xpath",'//*[@id="modWin-iframe"]')
			
			#开证方式
			
			clear("xpath",'//*[@id="combobox-input-issuetype"]')
			sleep(1)
			input("xpath",'//*[@id="combobox-input-issuetype"]','背对背开证')
			sleep(1)
			up_enter_click('//*[@id="combobox-input-issuetype"]')
			
			js_gd("xpath", "//span[contains(text(),'关联收证信息')]")
			sleep(1)
			span_click("关联收证信息")
			sleep(1)
			#新增行
			click("xpath", "//span[@title='原证号码']/ancestor::*[6]/following-sibling::*[2]/descendant::*[7]")
			sleep(1)
			#原证号码
			click("xpath",'//*[@id="combobox-input-locreditsrelationsgrid-explocreditid-0"]')
			sleep(1)
			up_enter_click('//*[@id="combobox-input-locreditsrelationsgrid-explocreditid-0"]')
			
			span_click("保存")
			switch_default()
			sleep(3)
			
			# 切入信用证开证管理窗体
			switch_to("xpath", '//*[@id="impLOCredits-tab-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[3]/td[2]/div/button')
			sleep(1)
			
			span_click("关联收证")
			switch_to("xpath",'//*[@id="locreditsRelationsWin-iframe"]')
			sleep(1)
			span_click("关联收证信息")
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("信用证开证管理，关联收证信息成功！")
			time.sleep(3)
			
			# 测试操作记录💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入信用证开证管理窗体
			switch_to("xpath", '//*[@id="impLOCredits-tab-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("操作记录")
			switch_to("xpath",'//*[@id="operationWin-iframe"]')
			
			#勾选、取消结清
			click("xpath",'//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			span_click("取消结清")
			ok_click()
			print("信用证开征管理，取消结清成功")
			sleep(3)
			
			# 勾选、取消到单登记
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[3]/td[2]/div/button')
			sleep(1)
			span_click("取消到单登记")
			ok_click()
			print("信用证开征管理，取消到单登记成功")
			sleep(3)
			
			# 勾选、取消押汇
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[5]/td[2]/div/button')
			sleep(1)
			span_click("取消押汇")
			ok_click()
			print("信用证开征管理，取消押汇成功")
			sleep(3)
			
			# 勾选、取消付汇
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[7]/td[2]/div/button')
			sleep(1)
			span_click("取消付汇")
			ok_click()
			print("信用证开征管理，取消付汇成功")
			sleep(3)
			
			switch_default()
			span_click("信用证开证管理")
			sleep(2)
			
			# 切入信用证开证管理窗体
			switch_to("xpath", '//*[@id="impLOCredits-tab-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[2]/td[2]/div/button')
			sleep(1)
			
			span_click("操作记录")
			switch_to("xpath", '//*[@id="operationWin-iframe"]')
			
			# 勾选、取消结清
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			span_click("取消承兑")
			ok_click()
			print("信用证开征管理，取消承兑成功")
			sleep(3)
			switch_default()
			
			#点击信用证管理，收回窗体
			click("xpath", "//span[@title='信用证管理']")
			sleep(1)
			
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("信用证开证管理失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		
		
		# 测试信用证开证证查看💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
		try:
			logger.info("开始测试票据管理--信用证管理--信用证开证查看")
			# 点击承兑汇票管理
			click("xpath", "//span[@title='信用证管理']")
			sleep(1)
			# 点击应付支票登记菜单
			click("xpath", "//span[@title='信用证开证查看']")
			sleep(1)
			# 退出所有的iframe窗体
			switch_default()
			
			# 切入信用证收证查看窗体
			switch_to("xpath", '//*[@id="impLOCreditsView-tab-iframe"]')
			implici_wait("xpath", "//div[text()='CNY-人民币']")
			print("信用证开证查看,查看成功")
			# 收回窗体
			switch_default()
			span_click("信用证管理")
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("信用证收证查看失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		
	
		
		# 测试委托方保函管理💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
		try:
			logger.info("开始测试票据管理--保函管理--委托方保函管理")
			# 点击承兑汇票管理
			click("xpath", "//span[@title='保函管理']")
			sleep(1)
			# 点击应付支票登记菜单
			click("xpath", "//span[@title='委托方保函管理']")
			sleep(1)
			# 退出所有的iframe窗体
			switch_default()
			
			# 测试新增💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			for i in range(1,3):
				global BHBH1
				global BHBH2
				#切入委托方保函管理窗体
				switch_to("xpath",'//*[@id="prinLOGuarantees-tab-iframe"]')
				span_click("新增")
				switch_to("xpath",'//*[@id="addWin-iframe"]')
				
				#保函编号
				if i ==1:
					BHBH1=time.strftime("%Y%m%d%H%M%S")
					input("xpath",'//*[@id="guaranteenumber"]',BHBH1)
					sleep(1)
				if i ==2:
					BHBH2=time.strftime("%Y%m%d%H%M%S")
					input("xpath",'//*[@id="guaranteenumber"]',BHBH2)
					sleep(1)
				#受益人类型
				input("xpath",'//*[@id="combobox-input-beneficiarytype"]','交易对手')
				sleep(1)
				up_enter_click('//*[@id="combobox-input-beneficiarytype"]')
				
				#受益人
				input("xpath",'//*[@id="beneficiary"]','浙江华语科技')
				sleep(1)
				
				#保函类型
				input("xpath",'//*[@id="combobox-input-guaranteetypeid"]','106-保函')
				sleep(1)
				up_enter_click('//*[@id="combobox-input-guaranteetypeid"]')
				
				#担报银行
				input_up_click('//*[@id="combobox-input-issuingbankid"]','BOC-中国银行')
				
				#开立方式
				input_up_click('//*[@id="combobox-input-issuetype"]','直开信开')
				
				#币种
				input_up_click('//*[@id="combobox-input-currencyid"]','CNY-人民币')
				
				#保函金额
				money=random.randint(100,300)
				input("xpath",'//*[@id="guaranteeamount-input"]',str(money))
				sleep(1)
				
				# 输入担保天数
				input("xpath", "//input[@id='guaranteedays-input']", "60")
				sleep(1)
				
				#保证金担保方式
				input_up_click('//*[@id="combobox-input-bailtype"]','票据质押保证')
				
				span_click("保存")
				# 退出所有iframe窗体
				switch_default()
				
				# 用隐式等待方法等页面出现提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				if i == 2:
					print("受益方保函管理，新增成功！" )
				time.sleep(3)
			
			# 测试修改💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入委托方保函管理窗体
			switch_to("xpath", '//*[@id="prinLOGuarantees-tab-iframe"]')
			#查询数据
			click("xpath",'//*[@id="north"]/div[2]/span')
			sleep(1)
			input("xpath",'//*[@id="guaranteenumber"]',BHBH1)
			sleep(1)
			span_click("查询")
			
			#刷新、勾选按钮
			click("xpath",'//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("修改")
			switch_to("xpath",'//*[@id="modWin-iframe"]')
			#备注
			input("xpath",'//*[@id="description"]','测试修改')
			sleep(1)
			span_click("保存")
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("受益方保函管理，修改成功！")
			time.sleep(3)
			
			# 测试删除💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入委托方保函管理窗体
			switch_to("xpath", '//*[@id="prinLOGuarantees-tab-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("删除")
			ok_click()
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'保函成功删除1条!')]")
			print("受益方保函管理，删除成功！")
			span_click("委托方保函管理")
			time.sleep(3)
			
			# 测试审核💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入委托方保函管理窗体
			switch_to("xpath", '//*[@id="prinLOGuarantees-tab-iframe"]')
			# 查询数据
			click("xpath", '//*[@id="north"]/div[2]/span')
			sleep(1)
			input("xpath", '//*[@id="guaranteenumber"]', BHBH2)
			sleep(1)
			span_click("查询")
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("审核")
			ok_click()
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'保函审核成功1条!')]")
			print("受益方保函管理，审核成功！")
			time.sleep(3)
			
			# 测试取消审核💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入委托方保函管理窗体
			switch_to("xpath", '//*[@id="prinLOGuarantees-tab-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("审核",'取消审核')
			ok_click()
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'保函取消审核成功1条!')]")
			print("受益方保函管理，取消审核成功！")
			time.sleep(3)
			
			# 测试变更💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入委托方保函管理窗体
			switch_to("xpath", '//*[@id="prinLOGuarantees-tab-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			span_click("审核")
			ok_click()
			sleep(3)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			span_click("变更")
			switch_to("xpath",'//*[@id="modWin-iframe"]')
			#备注
			input('xpath','//*[@id="description"]','测试变更')
			sleep(1)
			span_click("保存")
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功')]")
			print("受益方保函管理，变更成功！")
			time.sleep(3)
			
			# 测试操作记录💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入委托方保函管理窗体
			switch_to("xpath", '//*[@id="prinLOGuarantees-tab-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("操作记录")
			switch_to("xpath",'//*[@id="operationWin-iframe"]')
			implici_wait("xpath", "//div[contains(text(),'变更')]")
			print(print("受益方保函管理，操作记录查看！"))
			switch_parent()
			click("xpath",'//*[@id="f-win-title-operationWin"]/div[1]/div')
			sleep(1)
			switch_default()
			
			# 测试到期关闭💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入委托方保函管理窗体
			switch_to("xpath", '//*[@id="prinLOGuarantees-tab-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("到期关闭")
			span_click("确定")
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'保函到期关闭成功1条!')]")
			print("委托方保函管理，到期关闭成功！")
			time.sleep(3)
			#收回窗体
			switch_default()
			click("xpath", "//span[@title='保函管理']")
			sleep(1)
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("委托方保函管理失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		
		
		# 测试委托方保函查看💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
		try:
			logger.info("开始测试票据管理--保函管理--委托方保函查看")
			# 点击承兑汇票管理
			click("xpath", "//span[@title='保函管理']")
			sleep(1)
			# 点击应付支票登记菜单
			click("xpath", "//span[@title='委托方保函查看']")
			sleep(1)
			# 退出所有的iframe窗体
			switch_default()
			
			# 切入信用证收证查看窗体
			switch_to("xpath", '//*[@id="prinLOGuaranteesView-tab-iframe"]')
			implici_wait("xpath", "//div[text()='BOC-中国银行']")
			print("保函管理,委托方保函查看成功")
			# 收回窗体
			switch_default()
			span_click("保函管理")
			
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("信用证收证查看失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		
		# 测试受益方保函管理💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
		try:
			logger.info("开始测试票据管理--保函管理--受益方保函管理")
			# 点击承兑汇票管理
			click("xpath", "//span[@title='保函管理']")
			sleep(1)
			# 点击应付支票登记菜单
			click("xpath", "//span[@title='受益方保函管理']")
			sleep(1)
			# 退出所有的iframe窗体
			switch_default()
		
			# 测试新增💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			for i in range (1,3):
				global BHBH3
				global BHBH4
				switch_to("xpath",'//*[@id="benLOGuarantees-tab-iframe"]')
				span_click("新增")
				switch_to("xpath",'//*[@id="addWin-iframe"]')
				
				#委托人
				input("xpath",'//*[@id="entruster"]','浙江华语科技')
				sleep(1)
				
				#保函编号
				if i ==1 :
					BHBH3 =time.strftime("%Y%m%d%H%M%S")
					input("xpath",'//*[@id="guaranteenumber"]',str(BHBH3))
					sleep(1)
				if i ==2 :
					BHBH4 =time.strftime("%Y%m%d%H%M%S")
					input("xpath",'//*[@id="guaranteenumber"]',str(BHBH4))
					sleep(1)
				
				#保函类型
				input_up_click('//*[@id="combobox-input-guaranteetypeid"]','106-保函')
				
				#担保机构
				input_up_click('//*[@id="combobox-input-issuingbankid"]', 'BOC-中国银行')
				
				# 开立方式
				input_up_click('//*[@id="combobox-input-issuetype"]', '直开信开')
				
				# 币种
				input_up_click('//*[@id="combobox-input-currencyid"]', 'CNY-人民币')
				
				# 保函金额
				BHJE=random.randint(100,300)
				input("xpath",'//*[@id="guaranteeamount-input"]',str(BHJE))
				sleep(1)
				
				#担保天数
				double_click("xpath",'//*[@id="guaranteedays-input"]')
				sleep(1)
				input("xpath",'//*[@id="guaranteedays-input"]','60')
				sleep(1)
				span_click("保存")
				
				# 退出所有iframe窗体
				switch_default()
				# 用隐式等待方法等页面出现提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				if i ==2 :
					print("受益方保函管理，新增成功！" )
				time.sleep(3)
				
			
			
			# 修改💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入委托方保函管理窗体
			switch_to("xpath", '//*[@id="benLOGuarantees-tab-iframe"]')
			# 查询数据
			click("xpath", '//*[@id="north"]/div[2]/span')
			sleep(1)
			input("xpath", '//*[@id="guaranteenumber"]', BHBH3)
			sleep(1)
			span_click("查询")
			#刷新、勾选按钮
			click("xpath",'//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("修改")
			switch_to("xpath",'//*[@id="modWin-iframe"]')
			#备注
			input("xpath",'//*[@id="description"]','测试修改')
			sleep(1)
			span_click("保存")
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("受益方保函管理，修改成功！")
			time.sleep(3)
			
			# 删除💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="benLOGuarantees-tab-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
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
			implici_wait("xpath", "//span[contains(text(),'成功删除1条!')]")
			print("受益方保函管理，删除成功！")
			span_click("受益方保函管理")
			time.sleep(3)
			
			# 审核💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="benLOGuarantees-tab-iframe"]')
			# 查询数据
			click("xpath", '//*[@id="north"]/div[2]/span')
			sleep(1)
			input("xpath", '//*[@id="guaranteenumber"]', BHBH4)
			sleep(1)
			span_click("查询")
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
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
			implici_wait("xpath", "//span[contains(text(),'保函审核成功1条!')]")
			print("受益方保函管理，审核成功！")
			time.sleep(3)
			
			# 撤销审核💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="benLOGuarantees-tab-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("审核",'取消审核')
			ok_click()
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'保函取消审核成功1条!')]")
			print("受益方保函管理，取消审核成功！")
			time.sleep(3)
			
			# 变更💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="benLOGuarantees-tab-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			# 点击审核按钮
			click("xpath", "//span[text()='审核']")
			sleep(1)
			# 点击弹出框的OK键
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
			sleep(3)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			span_click("变更")
			switch_to("xpath",'//*[@id="modWin-iframe"]')
			#备注
			input("xpath",'//*[@id="description"]','测试变更')
			sleep(1)
			span_click("保存")
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("受益方保函管理，变更成功！")
			time.sleep(3)
			
			# 操作记录💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="benLOGuarantees-tab-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("操作记录")
			switch_to("xpath",'//*[@id="operationWin-iframe"]')
			implici_wait("xpath", "//div[contains(text(),'变更')]")
			print("受益方保函管理，操作记录查看成功！")
			sleep(1)
			switch_parent()
			click("xpath",'//*[@id="f-win-title-operationWin"]/div[1]/div')
			sleep(1)
			switch_default()
			
			# 到期关闭💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="benLOGuarantees-tab-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("到期关闭")
			span_click("确定")
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'保函到期关闭成功1条!')]")
			print("受益方保函管理，到期关闭成功！")
			time.sleep(3)
			# 收回窗体
			switch_default()
			click("xpath", "//span[@title='保函管理']")
			sleep(1)
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("受益方保函管理失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		
		# 测试受益方保函查看💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
		try:
			logger.info("开始测试票据管理--保函管理--受益方保函管理")
			# 点击承兑汇票管理
			click("xpath", "//span[@title='保函管理']")
			sleep(1)
			# 点击应付支票登记菜单
			click("xpath", "//span[@title='受益方保函查看']")
			sleep(1)
			# 退出所有的iframe窗体
			switch_default()
				
			# 测试查看💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			#切入受益方保函查看窗体
			switch_to("xpath",'//*[@id="benLOGuaranteesView-tab-iframe"]')
			#双击数据
			double_click("xpath",'//*[@id="grid-body-table"]/tbody/tr[1]/td[3]/div')
			sleep(1)
			switch_to("xpath",'//*[@id="detailWin-iframe"]')
			implici_wait("xpath", "//span[text()='保函编号']")
			print("受益方保函查看，查看成功")
			switch_default()
			span_click("受益方保函查看")
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("受益方保函管理失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		
if __name__ == '__main__':
	#  启动单元测试
	unittest.main(verbosity=2)
