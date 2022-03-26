# encoding=utf-8
# @Time : 2020/8/14 14:49
# @Author : 张中国
# 此文件是测试账户资金监控模块，包含基础设置，账户生命周期，离线账户维护，直联账户查询，结构账户余额，账户余额查看，账户明细查看，离线账户日结
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

# print("开始时间：",time.strftime("%Y-%m-%d %H:%M:%S"))

driver = ""


@pytest.mark.flaky(reruns=pytest_flaky, reruns_delay=10)
class Test_Zhzj(unittest.TestCase):
	
	# 启动浏览器
	def setUp(self):
		# 启动浏览器的另外一个方法：通过封装启动浏览器的驱动，启动不同浏览器
		self.driver = get("chrome")
	
	# 登陆系统、对系统设置进行操作
	def test_trade(self):
		
		login(G_Ora_Url, mindy, Password, "亚唐科技")
		
		# 将页面的滚动条滑动到‘票据管理’页面的地方
		js_gd("xpath", "//span[contains(text(),'账户资金监控')]")
		# 用JS的方法点击票据管理菜单按钮
		js_click("xpath", "//span[contains(text(),'账户资金监控')]")
		sleep(1)

		# 测试基础设置--账户性质🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱
		try:
			logging.info("测试账户资金监控--基础设置--账户性质")
			# 点击基础设置菜单
			span_click("基础设置")
			# 点击账户性质菜单
			click("xpath", "//span[text()='账户性质']")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			
			#测试新增功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			for i in range(1, 3):
				# 切入账户性质的iframe窗体
				switch_to("xpath", "//iframe[@id='bankAccountType-tab-iframe']")
				# 用JS的方法点击新增按钮
				js_click("xpath", "//span[text()='新增']")
				sleep(1)
				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='addWin-iframe']")
				
				# 用途代码
				code = time.strftime("%H%M%S")
				input("xpath", "//input[@name='code']", code)
				sleep(1)

				# 输入的账户性质
				name = "ZHXZ"+time.strftime("%H%M%S")
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
					print("基础设置-账户性质，新增成功！")
				time.sleep(3)
			
			# 测试修改功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入账户性质的iframe窗体
			switch_to("xpath", "//iframe[@id='bankAccountType-tab-iframe']")
			span_click("代码")
			#刷新、勾选按钮
			click("xpath",'//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath",'//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("修改")
			
			# 切入修改的iframe窗体
			switch_to("xpath", "//iframe[@id='modWin-iframe']")
			# 修改描述框中的内容
			input("xpath", "//textarea[@id='description']", "修改")
			sleep(1)
			# 点击保存按钮
			click("xpath", "//span[text()='保存']")
			sleep(1)
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("基础设置-账户性质，修改成功！")
			time.sleep(3)
			
			# 测试删除功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入账户性质的iframe窗体
			switch_to("xpath", "//iframe[@id='bankAccountType-tab-iframe']")
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("删除")
			ok_click()
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("基础设置-账户性质，删除成功！")
			time.sleep(3)
			
			#点击基础设置，收回窗体
			span_click("基础设置")
			
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("账户性质失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
			
		
		# 测试基础设置--账户分组🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱
		try:
			logging.info("测试账户资金监控--基础设置--账户分组")
			# 点击基础设置菜单
			span_click("基础设置")
			# 点击账户性质菜单
			click("xpath", "//span[text()='账户分组']")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			
			# 测试新增功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			for i in range(1, 3):
				# 切入账户性质的iframe窗体
				switch_to("xpath", '//*[@id="bankAccountGroup-tab-iframe"]')
				# 用JS的方法点击新增按钮
				js_click("xpath", "//span[text()='新增']")
				sleep(1)
				# 切入新增的iframe窗体
				switch_to("xpath", '//*[@id="addWin-iframe"]')
				
				# 用途代码
				code = time.strftime("%H%M%S")
				input("xpath",'//*[@id="code"]', code)
				sleep(1)
				
				# 输入名称
				name = "ZHFZ" + time.strftime("%H%M%S")
				input("xpath",'//*[@id="name"]', name)
				sleep(1)
				
				# 点击保存按钮
				click("xpath", "//span[text()='保存']")
				sleep(1)
				# 退出所有iframe窗体
				switch_default()
				
				# 用隐式等待方法等页面出现新增成功的提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				if i == 2:
					print("基础设置-账户分组，新增成功！")
				time.sleep(3)
			
			# 测试修改功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入账户性质的iframe窗体
			switch_to("xpath", '//*[@id="bankAccountGroup-tab-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("修改")
			
			# 切入修改的iframe窗体
			switch_to("xpath", '//*[@id="modWin-iframe"]')
			# 修改描述框中的内容
			input("xpath", "//textarea[@id='description']", "修改")
			sleep(1)
			# 点击保存按钮
			click("xpath", "//span[text()='保存']")
			sleep(1)
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("基础设置-账户分组，修改成功！")
			time.sleep(3)
			
			# 测试删除功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入账户性质的iframe窗体
			switch_to("xpath", '//*[@id="bankAccountGroup-tab-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("删除")
			ok_click()
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("基础设置-账户分组，删除成功！")
			time.sleep(3)
			
			# 点击基础设置，收回窗体
			span_click("基础设置")
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("账户分组失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		
		
		# 测试基础设置--账户分类🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱
		try:
			logging.info("测试账户资金监控--基础设置--账户分类")
			# 点击基础设置菜单
			span_click("基础设置")
			# 点击账户性质菜单
			click("xpath", "//span[text()='账户分类']")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			
			# 测试新增功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			for i in range(1, 3):
				switch_to("xpath",'//*[@id="bankAccountClass-tab-iframe"]')
				sleep(20)
				span_click("新增")
				switch_to("xpath",'//*[@id="addWin-iframe"]')
				
				#代码
				coad=time.strftime("%H%M%S")
				input("xpath",'//*[@id="code"]',coad)
				sleep(1)
				
				#名称
				name = "账户分类"+coad
				input("xpath",'//*[@id="name"]',name)
				sleep(1)
				
				span_click("保存")
				
				# 退出所有iframe窗体
				switch_default()
				
				# 用隐式等待方法等页面出现新增成功的提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				if i == 2:
					print("基础设置-账户分类，新增成功！")
				time.sleep(3)
			
			# 测试修改功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="bankAccountClass-tab-iframe"]')
			sleep(20)
			#刷新、勾选按钮
			
			click("xpath",'//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("修改")
			switch_to("xpath",'//*[@id="modWin-iframe"]')
			
			input("xpath",'//*[@id="description"]','测试修改')
			sleep(1)
			
			span_click("保存")
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("基础设置-账户分类，修改成功！")
			time.sleep(3)
			
			# 测试删除功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="bankAccountClass-tab-iframe"]')
			sleep(20)
			# 刷新、勾选按钮
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("删除")
			ok_click()
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("基础设置-账户分类，删除成功！")
			time.sleep(3)
			
			
			
			# 点击基础设置，收回窗体
			span_click("基础设置")
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("账户分组失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		
		
		# 测试基础设置--受限原因🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱
		try:
			logging.info("测试账户资金监控--基础设置--受限原因")
			# 点击基础设置菜单
			span_click("基础设置")
			# 点击账户性质菜单
			click("xpath", "//span[text()='受限原因']")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			
			# 测试新增功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			for i in range(1, 3):
				# 切入账户分类的iframe窗体
				switch_to("xpath", '//*[@id="bankAccountRestrictReason-tab-iframe"]')
				# 用JS的方法点击新增按钮
				js_click("xpath", "//span[text()='新增']")
				sleep(1)
				# 切入新增的iframe窗体
				switch_to("xpath", '//*[@id="addWin-iframe"]')
				
				# 用途代码
				code = time.strftime("%H%M%S")
				input("xpath", '//*[@id="code"]', code)
				sleep(1)
				
				# 输入名称
				name = "SXYY" + time.strftime("%H%M%S")
				input("xpath", '//*[@id="name"]', name)
				sleep(1)
				
				# 点击保存按钮
				click("xpath", "//span[text()='保存']")
				sleep(1)
				# 退出所有iframe窗体
				switch_default()
				
				# 用隐式等待方法等页面出现新增成功的提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				if i == 2:
					print("基础设置-受限原因，新增成功！")
				time.sleep(3)
			
			# 测试修改功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入账户分类的iframe窗体
			switch_to("xpath", '//*[@id="bankAccountRestrictReason-tab-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
			sleep(1)
			
			span_click("修改")
			
			# 切入修改的iframe窗体
			switch_to("xpath", '//*[@id="modWin-iframe"]')
			# 修改描述框中的内容
			input("xpath", "//textarea[@id='description']", "修改")
			sleep(1)
			# 点击保存按钮
			click("xpath", "//span[text()='保存']")
			sleep(1)
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("基础设置-受限原因，修改成功！")
			time.sleep(3)
			
			# 测试删除功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入账户分类的iframe窗体
			switch_to("xpath", '//*[@id="bankAccountRestrictReason-tab-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("删除")
			ok_click()
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("基础设置-受限原因，删除成功！")
			time.sleep(3)
			
			# 点击基础设置，收回窗体
			span_click("基础设置")
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("受限原因失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		
		
		# 测试账户生命周期--账户维护🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱
		try:
			logging.info("测试账户生命周期--账户维护--单币种账户")
			# 点击账户生命周期菜单
			click("xpath", "//span[contains(text(),'账户生命周期')]")
			sleep(1)
			# 点击账户维护菜单
			click("xpath", "//span[text()='账户维护']")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			
			# 测试新增功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			for i in range(1, 5):
				switch_to("xpath",'//*[@id="bankAccounts-tab-iframe"]')
				switch_to("xpath",'//*[@id="subTabOne-iframe"]')
				sleep(1)
				
				span_click("新增")
				# 切入新增窗体
				switch_to("xpath", '//*[@id="addWin-iframe"]')
				
				# 银行
				click("xpath", "//input[@id='combobox-input-bankid']")
				sleep(1)
				# 模糊匹配报错，因此选择直接点击
				click("xpath", "//div[@title='代码-名称:BOC-中国银行']")
				sleep(1)
				
				# 选择开户行
				input("xpath", "//input[@id='combobox-input-banklocationid']", "大连泡崖")
				sleep(1)
				click("xpath", "//div[@title='联行号-开户行名:104222000965-中国银行股份有限公司大连泡崖街支行']")
				sleep(1)
				
				# 选择币种
				input_up_click("//input[@id='combobox-input-currencyid']", "CNY")
				
				# 选择账户性质
				input_up_click("//input[@id='combobox-input-accounttypeid']", "基本户")
				
				# # 选择银企直联户isbankdirect
				click("xpath", "//input[@id='isbankdirect']")
				sleep(1)
				
				# 选择境内外
				input_up_click("//input[@id='combobox-input-inorout']", "境内")
				
				# 输入银行账号
				number=str(time.strftime("%Y%m%d%H%M%S"))
				input("xpath", '//*[@id="accountnumber"]', number)
				sleep(1)
				
				#账户名
				name = "测试账户"+number
				input("xpath", '//*[@id="accountname"]', name)
				sleep(1)
				# 点击保存按钮
				click("xpath", "//span[text()='保存']")
				sleep(1)
				# 退出所有iframe窗体
				switch_default()
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				if i ==3 :
					print("账户维护-单币种账户，新增成功")
				sleep(3)
			
			#测试修改功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="bankAccounts-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			#刷新、勾选按钮
			click("xpath",'//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("修改")
			switch_to("xpath",'//*[@id="modWin-iframe"]')
			
			#修改备注
			input("xpath",'//*[@id="remark"]','测试修改')
			sleep(1)
			
			span_click("保存")
			# 退出所有iframe窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("账户维护-单币种账户，修改成功")
			sleep(3)
			
			# 测试删除功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="bankAccounts-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("删除")
			ok_click()
			# 退出所有iframe窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'删除成功！')]")
			print("账户维护-单币种账户，删除成功")
			sleep(3)
			
			# 测试审核功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="bankAccounts-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("审核")
			ok_click()
			# 退出所有iframe窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'账户成功审核1条！')]")
			print("账户维护-单币种账户，审核成功")
			sleep(3)
			
			# 测试取消审核功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="bankAccounts-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("审核",'取消审核')
			ok_click()
			# 退出所有iframe窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'账户成功取消审核1条！')]")
			print("账户维护-单币种账户，取消审核成功")
			sleep(3)
			
			# 测试送审功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="bankAccounts-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("送审")
			ok_click()
			# 退出所有iframe窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'送审成功！')]")
			print("账户维护-单币种账户，送审成功")
			sleep(3)
			
			# 测试撤销送审功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="bankAccounts-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("送审",'撤销送审')
			ok_click()
			# 退出所有iframe窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'成功撤销送审1条记录！')]")
			print("账户维护-单币种账户，撤销送审成功")
			sleep(3)
			
			# 测试开户功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			for i in range(1,4):
				switch_to("xpath", '//*[@id="bankAccounts-tab-iframe"]')
				switch_to("xpath", '//*[@id="subTabOne-iframe"]')
				sleep(1)
				
				# 刷新、勾选按钮
				click("xpath", '//*[@id="gridbar-page-refresh"]')
				sleep(1)
				if i ==1 :
					click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
					sleep(1)
				if i ==2 :
					click("xpath", '//*[@id="grid-body-table"]/tbody/tr[2]/td[2]/div/button')
					sleep(1)
				if i ==3 :
					click("xpath", '//*[@id="grid-body-table"]/tbody/tr[3]/td[2]/div/button')
					sleep(1)
				
				triangle_cick_and_element("维护", '开户')
				
				# 开户日期
				today = date.today()
				open_date = today - timedelta(days=20)
				clear("xpath", "//input[@id='openeddatewin-input']")
				sleep(1)
				input("xpath", "//input[@id='openeddatewin-input']", str(open_date))
				time.sleep(1)
				
				# 日记账余额
				click("xpath", '//*[@id="journalbalance-input"]')
				sleep(1)
				clear("xpath", '//*[@id="journalbalance-input"]')
				sleep(1)
				input("xpath", '//*[@id="journalbalance-input"]', "50000")
				sleep(1)
				click("xpath", "//span[text()='确定']")
				sleep(1)
				# 退出所有窗体
				switch_default()
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				if i ==3 :
					print("账户维护-单币种账户，开户成功")
				sleep(3)
			
			# 测试冻结功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="bankAccounts-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("维护",'冻结')
			ok_click()
			# 退出所有iframe窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("账户维护-单币种账户，冻结成功")
			sleep(3)
			
			# 测试解冻功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="bankAccounts-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("维护", '解冻')
			
			# 退出所有iframe窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("账户维护-单币种账户，解冻成功")
			sleep(3)
			
			# 测试变更功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="bankAccounts-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("维护", '变更')
			switch_to("xpath",'//*[@id="updateAccountWin-iframe"]')
			sleep(1)
			input("xpath",'//*[@id="remark"]','测试变更')
			sleep(1)
			
			span_click("保存")
			# 退出所有iframe窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("账户维护-单币种账户，变更成功")
			sleep(3)
			
			# 测试编辑账户事件功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="bankAccounts-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("维护", '编辑账户事件')
			switch_to("xpath", '//*[@id="accountMaintainEventWin-iframe"]')
			sleep(1)
			
			span_click("新增行")
			input("xpath",'//*[@id="editgrid-description-4"]','编辑账户事件')
			sleep(1)
			
			span_click("保存")
			# 退出所有iframe窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("账户维护-单币种账户，编辑账户事件成功")
			sleep(3)
			
			# 测试年检功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="bankAccounts-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("维护", '年检')
			
			click("xpath",'//*[@id="closesubmit1"]/span/span')
			sleep(1)
			ok_click()
			
			# 退出所有iframe窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("账户维护-单币种账户，年检成功")
			sleep(3)
			
			# 测试所属组织转移功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="bankAccounts-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("维护", '所属组织转移')
			switch_to("xpath",'//*[@id="accountOrgChangeWin-iframe"]')
			sleep(1)
			
			click("xpath",'//*[@id="combobox-input-orgid"]')
			sleep(1)
			click("xpath",'//*[@id="orgid-combogrid-body-table"]/tbody/tr[2]/td[2]/div')
			sleep(1)
			
			span_click("保存")
			
			# 退出所有iframe窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("账户维护-单币种账户，所属组织转移成功")
			sleep(3)
			
			# 测试冻结💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="bankAccounts-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("维护", '冻结')
			ok_click()
			# 退出所有iframe窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("账户维护-单币种账户，冻结成功")
			sleep(3)
			
			#回到初始页面
			click("xpath", "//span[contains(text(),'账户生命周期')]")
			sleep(1)
			
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("单币种账户功能失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		
		
		# 测试账户生命周期--账户维护-多币种账户🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱
		try:
			logging.info("测试账户生命周期--账户维护--多币种账户")
			# 点击账户生命周期菜单
			click("xpath", "//span[contains(text(),'账户生命周期')]")
			sleep(1)
			# 点击账户维护菜单
			click("xpath", "//span[text()='账户维护']")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
		
			# 测试新增功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			for i in range(1, 4):
				switch_to("xpath", '//*[@id="bankAccounts-tab-iframe"]')
				span_click("多币种账户")
				switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
				sleep(1)
				
				span_click("新增")
				# 切入新增窗体
				switch_to("xpath", '//*[@id="addWin-iframe"]')
				
				# 银行
				click("xpath", "//input[@id='combobox-input-bankid']")
				sleep(1)
				# 模糊匹配报错，因此选择直接点击
				click("xpath", "//div[@title='代码-名称:BOC-中国银行']")
				sleep(1)
				
				# 选择开户行
				input("xpath", "//input[@id='combobox-input-banklocationid']", "大连泡崖")
				sleep(1)
				click("xpath", "//div[@title='联行号-开户行名:104222000965-中国银行股份有限公司大连泡崖街支行']")
				sleep(1)
				
				# 选择币种
				input_up_click("//input[@id='combobox-input-currencyid']", "CNY")
				
				# 选择账户性质
				input_up_click("//input[@id='combobox-input-accounttypeid']", "基本户")
				
				# 选择境内外
				input_up_click("//input[@id='combobox-input-inorout']", "境内")
				
				# 输入银行账号
				number = str(time.strftime("%Y%m%d%H%M%S"))
				input("xpath", '//*[@id="accountnumber"]', number)
				sleep(1)
				
				# 账户名
				name = "测试账户" + number
				input("xpath", '//*[@id="accountname"]', name)
				sleep(1)
				# 点击保存按钮
				click("xpath", "//span[text()='保存']")
				sleep(1)
				# 退出所有iframe窗体
				switch_default()
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				if i == 3:
					print("账户维护-多币种账户，新增成功")
				sleep(3)
			
			# 测试修改功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="bankAccounts-tab-iframe"]')
			span_click("多币种账户")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("修改")
			switch_to("xpath", '//*[@id="modWin-iframe"]')
			sleep(1)
			# 修改备注
			input("xpath", '//*[@id="remark"]', '测试修改')
			sleep(1)
			
			span_click("保存")
			# 退出所有iframe窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("账户维护-多币种账户，修改成功")
			sleep(3)
			
			# 测试删除功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="bankAccounts-tab-iframe"]')
			span_click("多币种账户")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("删除")
			ok_click()
			# 退出所有iframe窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'删除成功！')]")
			print("账户维护-多币种账户，删除成功")
			sleep(3)
			
			# 测试审核功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="bankAccounts-tab-iframe"]')
			span_click("多币种账户")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("审核")
			ok_click()
			# 退出所有iframe窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'账户成功审核1条！')]")
			print("账户维护-多币种账户，删除成功")
			sleep(3)
			
			# 测试取消审核功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="bankAccounts-tab-iframe"]')
			span_click("多币种账户")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("审核",'取消审核')
			ok_click()
			# 退出所有iframe窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'账户成功取消审核1条！')]")
			print("账户维护-多币种账户，取消审核成功")
			sleep(3)
			
			# 测试送审功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="bankAccounts-tab-iframe"]')
			span_click("多币种账户")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("送审")
			ok_click()
			# 退出所有iframe窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'送审成功！')]")
			print("账户维护-多币种账户，送审成功")
			sleep(3)
			
			# 测试撤销送审功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="bankAccounts-tab-iframe"]')
			span_click("多币种账户")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("送审",'撤销送审')
			ok_click()
			# 退出所有iframe窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'成功撤销送审1条记录！')]")
			print("账户维护-多币种账户，撤销送审成功")
			sleep(3)
			
			# 测试撤销送审功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			for i in range (1,3):
				switch_to("xpath", '//*[@id="bankAccounts-tab-iframe"]')
				span_click("多币种账户")
				switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
				sleep(1)
				
				# 刷新、勾选按钮
				click("xpath", '//*[@id="treepagingbar-page-refresh"]')
				sleep(1)
				if i ==1 :
					click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
					sleep(1)
				if i ==2 :
					click("xpath", '//*[@id="t1_t1-fixed"]/td[2]/div/button')
					sleep(1)
				
				triangle_cick_and_element("维护", '开户')
				switch_to("xpath",'//*[@id="openAccountWin-iframe"]')
				
				#开户日期
				expireddate = str(date.today() - timedelta(days=720))
				clear("xpath",'//*[@id="openeddate-input"]')
				sleep(1)
				input("xpath",'//*[@id="openeddate-input"]',expireddate)
				sleep(1)
				
				#初始余额
				double_click("xpath",'//*[@id="initbalance1-input"]')
				sleep(1)
				input("xpath",'//*[@id="initbalance1-input"]','5000')
				sleep(1)
				
				click("xpath",'//*[@id="submit"]/span/span')
				sleep(1)
				
				# 退出所有iframe窗体
				switch_default()
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				if i == 2:
					print("账户维护-多币种账户，开户成功")
				sleep(3)
			
			
			# 测试冻结功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="bankAccounts-tab-iframe"]')
			span_click("多币种账户")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("维护",'冻结')
			ok_click()
			# 退出所有iframe窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("账户维护-多币种账户，冻结成功")
			sleep(3)
			
			# 测试解冻功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="bankAccounts-tab-iframe"]')
			span_click("多币种账户")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("维护", '解冻')
			
			# 退出所有iframe窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("账户维护-多币种账户，解冻成功")
			sleep(3)
			
			# 测试变更功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="bankAccounts-tab-iframe"]')
			span_click("多币种账户")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("维护", '变更')
			switch_to("xpath",'//*[@id="updateAccountWin-iframe"]')
			sleep(1)
			input("xpath",'//*[@id="remark"]','变更')
			sleep(1)
			span_click("保存")
			# 退出所有iframe窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("账户维护-多币种账户，变更成功")
			sleep(3)
			
			# 测试编辑账户事件功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="bankAccounts-tab-iframe"]')
			span_click("多币种账户")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("维护", '编辑账户事件')
			switch_to("xpath", '//*[@id="accountMaintaineventWin-iframe"]')
			sleep(1)
			span_click("账户事件")
			span_click("新增行")
			input("xpath",'//*[@id="editgrid-description-4"]','账户事件')
			sleep(1)
			span_click("保存")
			
			# 退出所有iframe窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("账户维护-多币种账户，编辑账户事件成功")
			sleep(3)
			
			# 测试年检功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="bankAccounts-tab-iframe"]')
			span_click("多币种账户")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("维护", '年检')
			click("xpath",'//*[@id="closesubmit1"]/span/span')
			sleep(1)
			ok_click()
			# 退出所有iframe窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("账户维护-多币种账户，年检成功")
			sleep(3)
		
			# 回到初始页面
			click("xpath", "//span[contains(text(),'账户生命周期')]")
			sleep(1)
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("多币种账户功能失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
	
		
		# 测试账户生命周期--账户申请🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱
		try:
			logging.info("测试账户生命周期--账户申请")
			# 点击账户生命周期菜单
			click("xpath", "//span[contains(text(),'账户生命周期')]")
			sleep(1)
			# 点击账户维护菜单
			click("xpath", "//span[text()='账户申请']")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			
			
			# 做数据💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			for i in range (1,4):
				switch_to("xpath", '//*[@id="bankAccountApply-tab-iframe"]')
				sleep(1)
				
				triangle_cick_and_element("申请", '申请开户')
				switch_to("xpath", '//*[@id="kaihuWin-iframe"]')
				sleep(1)
				
				# 银行
				input_up_click('//*[@id="combobox-input-bankid"]', "中国银行")
				
				# 开户银行
				click_up_click('//*[@id="combobox-input-banklocationid"]')
				
				# 币种
				input_up_click('//*[@id="combobox-input-currencyid"]', "CNY-人民币")
				
				# 申请原因
				input("xpath", '//*[@id="applyreason"]', '测试申请开户')
				sleep(1)
				
				span_click("保存")
				# 退出所有iframe窗体
				switch_default()
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				if i ==3 :
					print("账户申请，申请开户成功")
				sleep(3)
			
			# 测试修改功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="bankAccountApply-tab-iframe"]')
			sleep(1)
			
			#刷新、勾选按钮
			click("xpath",'//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath",'//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("修改")
			switch_to("xpath",'//*[@id="eidteWin-iframe"]')
			sleep(1)
			input("xpath",'//*[@id="remark"]','测试修改')
			sleep(1)
			
			span_click("保存")
			# 退出所有iframe窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("账户申请，修改成功")
			sleep(3)
			
			# 测试删除功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="bankAccountApply-tab-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("删除")
			ok_click()
			# 退出所有iframe窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("账户申请，删除成功")
			sleep(3)
			
			# 测试送审功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="bankAccountApply-tab-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("送审")
			ok_click()
			# 退出所有iframe窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'送审成功！')]")
			print("账户申请，送审成功")
			sleep(3)
			
			# 测试撤销送审功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="bankAccountApply-tab-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("送审",'撤销送审')
			ok_click()
			# 退出所有iframe窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'成功撤销送审1条记录！')]")
			print("账户申请，撤销送审成功")
			sleep(3)
			
			# 测试作废功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="bankAccountApply-tab-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("作废")
			ok_click()
			switch_to("xpath",'//*[@id="canceldesrpWin-iframe"]')
			click("xpath",'//*[@id="cancelreason"]')
			sleep(1)
			input("xpath",'//*[@id="cancelreason"]','作废')
			sleep(1)
			click("xpath",'//*[@id="save"]/span/span')
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("账户申请，作废成功")
			sleep(3)
			
			# 测试申请开户流程💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="bankAccountApply-tab-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("送审")
			ok_click()
			sleep(3)
			double_click("xpath",'//*[@id="grid-body-table"]/tbody/tr[1]/td[3]/div')
			sleep(1)
			switch_to("xpath",'//*[@id="wf_taskProcessing_win-iframe"]')
			sleep(2)
			span_click("同意")
			switch_parent()
			sleep(3)
			
			#终审💨💨💨💨💨💨💨💨💨💨
			double_click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[3]/div')
			sleep(1)
			switch_to("xpath", '//*[@id="wf_taskProcessing_win-iframe"]')
			sleep(2)
			span_click("终审")
			switch_parent()
			sleep(3)
			
			#维护账户💨💨💨💨💨💨💨💨💨💨
			double_click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[3]/div')
			sleep(1)
			switch_to("xpath", '//*[@id="wf_taskProcessing_win-iframe"]')
			switch_to("xpath",'//*[@id="wf_busi_form"]')
			sleep(1)
			
			#银行账号
			number=time.strftime("%Y%m%d%S")
			input("xpath",'//*[@id="accountnumber"]',str(number))
			sleep(1)
		
			#账户名称
			name = "Test"
			input("xpath",'//*[@id="accountname"]',name)
			sleep(1)
			
			#账户性质
			click_up_click('//*[@id="combobox-input-accounttypeid"]')
			
			switch_parent()
			span_click("提交")
			switch_parent()
			sleep(3)
			
			#维护审核💨💨💨💨💨💨💨💨💨💨
			double_click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[3]/div')
			sleep(1)
			switch_to("xpath", '//*[@id="wf_taskProcessing_win-iframe"]')
			sleep(1)
			span_click("同意")
			switch_to("xpath", '//*[@id="wf_busi_form"]')
			sleep(1)
			click("xpath",'//*[@id="submit"]/span/span')
			sleep(1)
			
			# 退出所有iframe窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("账户申请，申请开户流程成功")
			sleep(3)
			
			# 测试申请变更流程💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="bankAccountApply-tab-iframe"]')
			sleep(1)
			
			triangle_cick_and_element("申请",'申请变更')
			switch_to("xpath",'//*[@id="biangengWin-iframe"]')
			sleep(2)
			
			#银行
			input_up_click('//*[@id="combobox-input-bankid"]','BOC-中国银行')
			
			#银行账户
			click_up_click('//*[@id="combobox-input-accountid"]')
			
			#申请原因
			input("xpath",'//*[@id="applyreason"]','测试变更')
			sleep(1)
			
			span_click("保存")
			switch_parent()
			sleep(3)
			
			#变更审核💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("送审")
			ok_click()
			sleep(3)
			
			double_click("xpath",'//*[@id="grid-body-table"]/tbody/tr[1]/td[3]/div')
			sleep(1)
			switch_to("xpath",'//*[@id="wf_taskProcessing_win-iframe"]')
			sleep(2)
			span_click("同意")
			switch_parent()
			sleep(3)
			
			double_click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[3]/div')
			sleep(1)
			switch_to("xpath", '//*[@id="wf_taskProcessing_win-iframe"]')
			sleep(2)
			span_click("同意")
			switch_parent()
			sleep(3)
			
			#提交💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			double_click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[3]/div')
			sleep(1)
			switch_to("xpath", '//*[@id="wf_taskProcessing_win-iframe"]')
			sleep(2)
			span_click("提交")
			switch_parent()
			sleep(3)
			
			double_click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[3]/div')
			sleep(1)
			switch_to("xpath", '//*[@id="wf_taskProcessing_win-iframe"]')
			sleep(2)
			span_click("同意")
			
			# 退出所有iframe窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("账户申请，账户变更流程成功")
			sleep(3)
			
			# 测试申请冻结流程💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="bankAccountApply-tab-iframe"]')
			sleep(1)
			
			triangle_cick_and_element("申请", '申请冻结')
			switch_to("xpath", '//*[@id="dongjieWin-iframe"]')
			sleep(2)
			
			#银行账号
			click_up_click('//*[@id="combobox-input-accountid"]')
			
			#申请原因
			input("xpath",'//*[@id="applyreason"]','测试冻结')
			sleep(1)
			
			span_click("保存")
			switch_parent()
			sleep(3)
			
			#对冻结的账户进行审核💨💨💨💨💨💨💨💨💨💨
			#刷新、勾选按钮
			click("xpath",'//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath",'//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("送审")
			ok_click()
			sleep(3)
			
			double_click("xpath",'//*[@id="grid-body-table"]/tbody/tr[1]/td[3]/div')
			sleep(1)
			switch_to("xpath",'//*[@id="wf_taskProcessing_win-iframe"]')
			sleep(2)
			span_click("同意")
			switch_parent()
			double_click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[3]/div')
			sleep(1)
			switch_to("xpath", '//*[@id="wf_taskProcessing_win-iframe"]')
			sleep(2)
			span_click("同意")
			
			# 退出所有iframe窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("账户申请，账户冻结流程成功")
			sleep(3)
			
			# 测试申请解冻流程💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="bankAccountApply-tab-iframe"]')
			sleep(1)
			
			triangle_cick_and_element("申请", '申请解冻')
			switch_to("xpath", '//*[@id="jiedongWin-iframe"] ')
			sleep(2)
			
			#银行账号
			click_up_click('//*[@id="combobox-input-accountid"]')
			
			#申请原因
			input("xpath",'//*[@id="applyreason"]','测试解冻流程')
			sleep(1)
			
			span_click("保存")
			switch_parent()
			sleep(3)
			
			#对解冻的账户进行审批💨💨💨💨💨💨💨💨
			#刷新、勾选按钮
			click("xpath",'//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath",'//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("送审")
			ok_click()
			sleep(3)
			
			double_click("xpath",'//*[@id="grid-body-table"]/tbody/tr[1]/td[3]/div')
			sleep(1)
			switch_to("xpath",'//*[@id="wf_taskProcessing_win-iframe"]')
			sleep(2)
			span_click("同意")
			
			# 退出所有iframe窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("账户申请，账户解冻流程成功")
			sleep(3)
			
			# 测试申请年检流程💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="bankAccountApply-tab-iframe"]')
			sleep(1)
			
			triangle_cick_and_element("申请", '申请年检')
			switch_to("xpath", '//*[@id="nianjianWin-iframe"]')
			sleep(2)
			
			#银行账户
			click_up_click('//*[@id="combobox-input-accountid"]')
			
			#账户本次年检日期
			today = date.today()
			click("xpath",'//*[@id="acclastannualinspecdate-input"]')
			sleep(1)
			input("xpath",'//*[@id="acclastannualinspecdate-input"]',str(today))
			sleep(1)
			double_click("xpath",'//*[@id="combobox-input-deposittype"]')
			sleep(1)
			
			#账户下次年检日期
			expireddate = today + timedelta(days=720)
			click("xpath", '//*[@id="accnextannualinspecdate-input"]')
			sleep(1)
			input("xpath", '//*[@id="accnextannualinspecdate-input"]', str(expireddate))
			sleep(1)
			double_click("xpath", '//*[@id="combobox-input-deposittype"]')
			sleep(1)
			
			span_click("保存")
			switch_parent()
			sleep(3)
			
			#对年检账户进行审批💨💨💨💨💨💨💨💨💨
			#刷新、勾选按钮
			click("xpath",'//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath",'//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("送审")
			ok_click()
			sleep(3)
			
			double_click("xpath",'//*[@id="grid-body-table"]/tbody/tr[1]/td[3]/div')
			sleep(1)
			switch_to("xpath",'//*[@id="wf_taskProcessing_win-iframe"]')
			sleep(2)
			span_click("同意")
			switch_parent()
			sleep(3)
			
			double_click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[3]/div')
			sleep(1)
			switch_to("xpath", '//*[@id="wf_taskProcessing_win-iframe"]')
			sleep(2)
			
			span_click("终审")
			# 退出所有iframe窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("账户申请，账户申请年检流程成功")
			sleep(3)
			
			# 测试申请销户流程💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="bankAccountApply-tab-iframe"]')
			sleep(1)
			
			triangle_cick_and_element("申请", '申请销户')
			switch_to("xpath", '//*[@id="xiaohuWin-iframe"]')
			sleep(2)
			
			#银行账户
			click_up_click('//*[@id="combobox-input-accountid"]')
			
			span_click("保存")
			switch_parent()
			sleep(3)
			
			#对申请销户的账户进行审批💨💨💨💨💨💨💨💨💨💨💨
			#刷新、勾选按钮
			click("xpath",'//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath",'//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("送审")
			ok_click()
			click("xpath",'//*[@id="f-message-webgen-0-yesBnt"]')
			sleep(3)
			
			double_click("xpath",'//*[@id="grid-body-table"]/tbody/tr[1]/td[3]/div')
			sleep(1)
			switch_to("xpath",'//*[@id="wf_taskProcessing_win-iframe"]')
			sleep(2)
			span_click("同意")
			switch_parent()
			sleep(3)
			
			double_click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[3]/div')
			sleep(1)
			switch_to("xpath", '//*[@id="wf_taskProcessing_win-iframe"]')
			sleep(2)
			span_click("同意")
			switch_parent()
			sleep(3)
			
			double_click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[3]/div')
			sleep(1)
			switch_to("xpath", '//*[@id="wf_taskProcessing_win-iframe"]')
			sleep(2)
			span_click("提交")
			switch_parent()
			sleep(3)
			
			double_click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[3]/div')
			sleep(1)
			switch_to("xpath", '//*[@id="wf_taskProcessing_win-iframe"]')
			sleep(2)
			span_click("终审")
			
			switch_to("xpath",'//*[@id="wf_busi_form"]')
			click_up_click('//*[@id="combobox-input-paytypeid"]')
			click("xpath",'//*[@id="submit"]/span/span')
			sleep(1)
			
			# 退出所有iframe窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("账户申请，账户申请销户流程成功")
			sleep(3)
			
			# 回到初始页面
			click("xpath", "//span[contains(text(),'账户生命周期')]")
			sleep(1)
			
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("账户申请功能失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		
		
		# 测试测试账户资金监控--账户生命周期--银行账户结构🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱
		try:
			logging.info("测试账户资金监控--账户生命周期--银行账户结构")
			#点击账户生命周期
			click("xpath", "//span[contains(text(),'账户生命周期')]")
			sleep(1)
			# 点击账户维护菜单
			click("xpath", "//span[text()='银行账户结构']")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			
			# 测试添加账户树功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath",'//*[@id="bankAccountStructures-tab-iframe"]')
			sleep(1)
			span_click("添加账户结构树")
			switch_to("xpath",'//*[@id="addstructureaccountWin-iframe"]')
			
			#结构账户类型
			click("xpath",'//*[@id="combobox-input-accountstructuretype"]')
			sleep(1)
			click("xpath", '//*[@id="f-combo-accountstructuretype-list-0"]')
			sleep(1)
			
			#名称
			name="中国企业"+str(time.strftime("%Y%S"))
			input("xpath",'//*[@id="tname"]',name)
			sleep(1)
			span_click("保存")
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("账户生命周期--银行账户结构，添加账户结构树成功！")
			time.sleep(3)
			
			# 测试添加下级账户功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="bankAccountStructures-tab-iframe"]')
			sleep(1)
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			span_click("添加下级账户")
			
			switch_to("xpath",'//*[@id="addlowaccountWin-iframe"]')
			sleep(2)
			#账户
			click_up_click('//*[@id="combobox-input-accountid"]')
			
			span_click("保存")
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("账户生命周期--银行账户结构，添加下级账户成功！")
			time.sleep(3)
			
			# 测试添加同级账户功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="bankAccountStructures-tab-iframe"]')
			sleep(1)
			#刷新、勾选按钮
			click("xpath",'//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath",'//*[@id="t1_t0_t0-fixed"]/td[2]/div/button')
			sleep(1)
			span_click("添加同级账户")
			
			switch_to("xpath", '//*[@id="addsameaccountWin-iframe"]')
			sleep(2)
			# 账户
			click("xpath",'//*[@id="combobox-input-accountid"]')
			sleep(1)
			click("xpath", '//*[@id="accountid-combogrid-body-table"]/tbody/tr[2]/td[2]/div')
			sleep(1)
			
			span_click("保存")
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("账户生命周期--银行账户结构，添加同级账户成功！")
			time.sleep(3)
			
			# 测试修改功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="bankAccountStructures-tab-iframe"]')
			sleep(1)
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			span_click("修改")
			
			switch_to("xpath", '//*[@id="modWin-iframe"]')
			sleep(2)
			input("xpath",'//*[@id="description"]','测试修改')
			
			span_click("保存")
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("账户生命周期--银行账户结构，修改成功！")
			time.sleep(3)
			
			# 测试删除功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="bankAccountStructures-tab-iframe"]')
			sleep(1)
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t0_t1-fixed"]/td[2]/div/button')
			sleep(1)
			span_click("删除")
			ok_click()
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("账户生命周期--银行账户结构，删除成功！")
			time.sleep(3)
			
			# 点击基础设置，收回窗体
			click("xpath", "//span[contains(text(),'账户生命周期')]")
			sleep(1)
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("账户性质失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		
		
		# 测试基账户资金监控--账户生命周期--银行账户查看🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱
		try:
			logging.info("测试账户资金监控--账户生命周期--银行账户查看")
			# 点击账户生命周期
			click("xpath", "//span[contains(text(),'账户生命周期')]")
			sleep(1)
			# 点击账户维护菜单
			click("xpath", "//span[text()='银行账户查看']")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			
			# 测试当前及下级组织查看💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath",'//*[@id="bankAccountsView-tab-iframe"]')
			switch_to("xpath",'//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			#查询
			click("xpath",'//*[@id="north"]/div[2]/span')
			sleep(1)
			click("xpath",'//*[@id="combobox-input-bankid"]')
			sleep(1)
			click("xpath", '//*[@id="bankid-combogrid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			span_click("查询")
			
			double_click("xpath",'//*[@id="grid-body-table"]/tbody/tr[1]/td[3]/div')
			sleep(1)
			switch_to("xpath",'//*[@id="detailWin-iframe"]')
			sleep(2)
			
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'组织')]")
			print("账户生命周期--银行账户结构，当前及下级组织查询成功！")
			time.sleep(3)
			#点击×号
			switch_parent()
			click("xpath",'//*[@id="f-win-title-detailWin"]/div[1]/div')
			switch_default()
			sleep(3)
			
			# 测试所有可操作组织查询💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="bankAccountsView-tab-iframe"]')
			span_click("所有可操作组织查询")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			sleep(1)
			
			# 查询
			click("xpath", '//*[@id="north"]/div[2]/span')
			sleep(1)
			click("xpath", '//*[@id="combobox-input-bankid"]')
			sleep(1)
			click("xpath", '//*[@id="bankid-combogrid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			span_click("查询")
			
			double_click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[3]/div')
			sleep(1)
			switch_to("xpath", '//*[@id="detailWin-iframe"]')
			sleep(2)
			
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'组织')]")
			print("账户生命周期--银行账户结构，当前及下级组织查询成功！")
			time.sleep(3)
			# 点击×号
			switch_parent()
			click("xpath", '//*[@id="f-win-title-detailWin"]/div[1]/div')
			switch_default()
			sleep(3)
			
			# 点击基础设置，收回窗体
			click("xpath", "//span[contains(text(),'账户生命周期')]")
			sleep(1)
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("账户性质失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		
		
		# 测试基账户资金监控--直联账户查询🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱
		try:
			logging.info("测试账户资金监控--直联账户查询")
			# 点击账户生命周期
			click("xpath", "//span[contains(text(),'直联账户查询')]")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			
			# 测试余额查询💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			#进入余额查询窗体
			switch_to("xpath",'//*[@id="directBankAccountQuery-tab-iframe"]')
			switch_to("xpath",'//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			#刷新、勾选按钮
			click("xpath",'//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("余额查询")
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'余额查询-查询成功')]")
			print("直联账户查询--当前操作组织查询，余额查询成功")
			switch_default()
			time.sleep(3)
			
			# 测试今日明细查询💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 进入余额查询窗体
			switch_to("xpath", '//*[@id="directBankAccountQuery-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("今日明细查询")
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//a[contains(text(),'明细查看')]")
			print("直联账户查询--当前操作组织查询，今日明细查询成功")
			switch_default()
			time.sleep(3)
			
			# 测试历史明细查询💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 进入余额查询窗体
			switch_to("xpath", '//*[@id="directBankAccountQuery-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("历史明细查询")
			today=date.today()
			start = today - timedelta(days=2)
			end   = today - timedelta(days=1)
			
			#查询起止日期
			input("xpath",'//*[@id="begindate-input"]',str(start))
			sleep(1)
			span_click("查询起始日期")
			
			#查询截止日期
			input("xpath", '//*[@id="enddate-input"]', str(end))
			sleep(1)
			span_click("查询截止日期")
			
			click("xpath",'//*[@id="hisensureclick"]/span/span')
			sleep(1)
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//a[contains(text(),'历史明细')]")
			print("直联账户查询--当前操作组织查询，历史明细查询成功")
			switch_default()
			time.sleep(3)
			
			# 测试近7天历史明细查询💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 进入余额查询窗体
			switch_to("xpath", '//*[@id="directBankAccountQuery-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("近7天历史明细查询")
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'历史明细查询-查询成功')]")
			print("直联账户查询--当前操作组织查询，近7天历史明细查询成功")
			switch_default()
			time.sleep(3)
			
			# 测试昨日明细查看,核准功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 进入余额查询窗体
			switch_to("xpath", '//*[@id="directBankAccountQuery-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("昨日明细查看")
			switch_to("xpath",'//*[@id="detail-iframe"]')
			
			#查询数据
			click("xpath",'//*[@id="north"]/div[2]/span')
			sleep(1)
			clear("xpath",'//*[@id="tradedatestart-input"]')
			sleep(1)
			clear("xpath", '//*[@id="tradedateend-input"]')
			sleep(1)
			span_click("查询")
			
			
			#刷新勾选按钮
			click("xpath",'//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath",'//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("核准")
			switch_to("xpath",'//*[@id="matchWin-iframe"]')
			
			#银行账户
			click("xpath",'//*[@id="combobox-input-accountid"]')
			sleep(1)
			click("xpath",'//*[@id="accountid-combogrid-head-table"]/thead/tr/th[2]/div/button')
			sleep(1)
			click("xpath",'//*[@id="match"]/span/span')
			sleep(1)
			
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'核准结果')]")
			print("直联账户查询--当前操作组织查询，核准功能正常")
			click("xpath", "//span[contains(text(),'直联账户查询')]")
			sleep(1)
			switch_default()
			time.sleep(3)
			
			# 测试昨日明细查看,核准规则功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 进入余额查询窗体
			switch_to("xpath", '//*[@id="directBankAccountQuery-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("昨日明细查看")
			switch_to("xpath", '//*[@id="detail-iframe"]')
			
			span_click("核准规则")
			switch_to("xpath",'//*[@id="ruleWin-iframe"]')
			sleep(1)
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'匹配顺序')]")
			print("直联账户查询--当前操作组织查询，核准规则正常")
			switch_default()
			click("xpath", "//span[contains(text(),'直联账户查询')]")
			sleep(1)
			switch_default()
			time.sleep(3)
			
			# 测试昨日明细查看,撤销已导出功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 进入余额查询窗体
			switch_to("xpath", '//*[@id="directBankAccountQuery-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
		
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("昨日明细查看")
			switch_to("xpath", '//*[@id="detail-iframe"]')
			
			# 查询数据
			click("xpath", '//*[@id="north"]/div[2]/span')
			sleep(1)
			clear("xpath", '//*[@id="tradedatestart-input"]')
			sleep(1)
			clear("xpath", '//*[@id="tradedateend-input"]')
			sleep(1)
			span_click("查询")
			
			# 刷新勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("撤销已导出")
			ok_click()
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'成功')]")
			print("直联账户查询--当前操作组织查询，撤销已导出正常")
			click("xpath", "//span[contains(text(),'直联账户查询')]")
			sleep(1)
			switch_default()
			time.sleep(3)
			
			# 测试昨日明细查看,取消功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 进入余额查询窗体
			switch_to("xpath", '//*[@id="directBankAccountQuery-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("昨日明细查看")
			switch_to("xpath", '//*[@id="detail-iframe"]')
			
			# 查询数据
			click("xpath", '//*[@id="north"]/div[2]/span')
			sleep(1)
			clear("xpath", '//*[@id="tradedatestart-input"]')
			sleep(1)
			clear("xpath", '//*[@id="tradedateend-input"]')
			sleep(1)
			span_click("查询")
			
			# 刷新勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("取消核准")
			ok_click()
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'核准操作')]")
			print("直联账户查询--当前操作组织查询，取消核准正常")
			click("xpath", "//span[contains(text(),'直联账户查询')]")
			sleep(1)
			switch_default()
			time.sleep(3)
			
			# 测试近七天历史余额查询功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 进入余额查询窗体
			switch_to("xpath", '//*[@id="directBankAccountQuery-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("近7天历史余额查询")
			
			#退出所有窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'账户查询成功！')]")
			print("直联账户查询--当前操作组织查询，近七天历史明细查询成功")
			
			# 测试余额调整功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 进入当前操作组织查询窗体
			switch_to("xpath", '//*[@id="directBankAccountQuery-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("余额调整")
			
			#当前余额
			double_click("xpath",'//*[@id="balancevalue-input"]')
			sleep(1)
			input("xpath",'//*[@id="balancevalue-input"]','50000')
			sleep(1)
			
			# 银行可用余额
			double_click("xpath", '//*[@id="bankbalance-input"]')
			sleep(1)
			input("xpath", '//*[@id="bankbalance-input"]', '40000')
			sleep(1)
			
			# 冻结余额
			double_click("xpath", '//*[@id="freezebalance-input"]')
			sleep(1)
			input("xpath", '//*[@id="freezebalance-input"]', '10000')
			sleep(1)
			
			#调整原因
			input("xpath",'//*[@id="adjustreason"]','测试余额调整')
			sleep(1)
			
			click("xpath",'//*[@id="hisensureclick1"]/span/span')
			sleep(1)
			# 退出所有窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("直联账户查询--当前操作组织查询，余额调整成功")
			
			# 测试调整历史查看功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 进入当前操作组织查询窗体
			switch_to("xpath", '//*[@id="directBankAccountQuery-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("余额调整",'调整历史查看')
			switch_to("xpath",'//*[@id="printWin-iframe"]')
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//div[contains(text(),'mindy')]")
			print("直联账户查询--当前操作组织查询，余额调整历史查看成功")
			switch_default()
			click("xpath", "//span[contains(text(),'直联账户查询')]")
			sleep(1)
			
			# 测试所有可操作组织查询--余额查询功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 进入当前操作组织查询窗体
			switch_to("xpath", '//*[@id="directBankAccountQuery-tab-iframe"]')
			span_click("所有可操作组织查询")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("余额查询")
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'余额查询-查询成功')]")
			print("直联账户查询--所有可操作组织，余额查询成功")
			switch_default()
			
			# 测试所有可操作组织查询--今日明细查询功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 进入当前操作组织查询窗体
			switch_to("xpath", '//*[@id="directBankAccountQuery-tab-iframe"]')
			span_click("所有可操作组织查询")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("今日明细查询")
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'今日明细查询-查询成功')]")
			print("直联账户查询--所有可操作组织，今日明细查询成功")
			switch_default()
			
			# 测试所有可操作组织查询--历史明细查询功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 进入当前操作组织查询窗体
			switch_to("xpath", '//*[@id="directBankAccountQuery-tab-iframe"]')
			span_click("所有可操作组织查询")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("历史明细查询")
			
			today = date.today()
			start = today - timedelta(days=2)
			end = today - timedelta(days=1)
			
			# 查询起止日期
			input("xpath", '//*[@id="begindate-input"]', str(start))
			sleep(1)
			span_click("查询起始日期")
			
			# 查询截止日期
			input("xpath", '//*[@id="enddate-input"]', str(end))
			sleep(1)
			span_click("查询截止日期")
			
			click("xpath",'//*[@id="hisensure"]/span/span')
			sleep(1)
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'历史明细查询-查询成功')]")
			print("直联账户查询--所有可操作组织，历史明细查询成功")
			switch_default()
			
			# 测试所有可操作组织查询--7天历史明细查询功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 进入当前操作组织查询窗体
			switch_to("xpath", '//*[@id="directBankAccountQuery-tab-iframe"]')
			span_click("所有可操作组织查询")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("近7天历史明细查询")
		
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'历史明细查询-查询成功')]")
			print("直联账户查询--所有可操作组织，近7天历史明细查询成功")
			switch_default()
			
			# 测试所有可操作组织查询--昨日明明细查询--核准功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 进入当前操作组织查询窗体
			switch_to("xpath", '//*[@id="directBankAccountQuery-tab-iframe"]')
			span_click("所有可操作组织查询")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("昨日明细查看")
			switch_to("xpath", '//*[@id="detail-iframe"]')
			
			#查询数据
			click("xpath",'//*[@id="north"]/div[2]/span')
			sleep(1)
			clear("xpath",'//*[@id="tradedatestart-input"]')
			sleep(1)
			clear("xpath", '//*[@id="tradedateend-input"]')
			sleep(1)
			span_click("查询")
			
			# 刷新勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("核准")
			switch_to("xpath", '//*[@id="matchWin-iframe"]')
			
			# 银行账户
			click("xpath", '//*[@id="combobox-input-accountid"]')
			sleep(1)
			click("xpath", '//*[@id="accountid-combogrid-head-table"]/thead/tr/th[2]/div/button')
			sleep(1)
			click("xpath", '//*[@id="match"]/span/span')
			sleep(1)
			
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'核准结果')]")
			print("直联账户查询--所有可操作组织查询，核准功能正常")
			click("xpath", "//span[contains(text(),'直联账户查询')]")
			sleep(1)
			switch_default()
			time.sleep(3)
			
			# 测试所有可操作组织查询--昨日明明细查询--取消核准功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 进入当前操作组织查询窗体
			switch_to("xpath", '//*[@id="directBankAccountQuery-tab-iframe"]')
			span_click("所有可操作组织查询")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("昨日明细查看")
			switch_to("xpath", '//*[@id="detail-iframe"]')
			
			# 查询数据
			click("xpath", '//*[@id="north"]/div[2]/span')
			sleep(1)
			clear("xpath", '//*[@id="tradedatestart-input"]')
			sleep(1)
			clear("xpath", '//*[@id="tradedateend-input"]')
			sleep(1)
			span_click("查询")
			
			# 刷新勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("取消核准")
			ok_click()
			
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'核准操作')]")
			print("直联账户查询--所有可操作组织查询，取消核准正常")
			click("xpath", "//span[contains(text(),'直联账户查询')]")
			sleep(1)
			switch_default()
			time.sleep(3)
			
			# 测试所有可操作组织查询--昨日明明细查询--取消核准功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 进入当前操作组织查询窗体
			switch_to("xpath", '//*[@id="directBankAccountQuery-tab-iframe"]')
			span_click("所有可操作组织查询")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("昨日明细查看")
			switch_to("xpath", '//*[@id="detail-iframe"]')
			
			span_click("核准规则")
			switch_to("xpath", '//*[@id="ruleWin-iframe"]')
			sleep(1)
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'匹配顺序')]")
			print("直联账户查询--所有可操作组织查询，核准规则正常")
			switch_default()
			click("xpath", "//span[contains(text(),'直联账户查询')]")
			sleep(1)
			switch_default()
			time.sleep(3)
			
			# 测试所有可操作组织查询--昨日明明细查询--撤销已导出功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 进入当前操作组织查询窗体
			switch_to("xpath", '//*[@id="directBankAccountQuery-tab-iframe"]')
			span_click("所有可操作组织查询")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("昨日明细查看")
			switch_to("xpath", '//*[@id="detail-iframe"]')
			
			# 查询数据
			click("xpath", '//*[@id="north"]/div[2]/span')
			sleep(1)
			clear("xpath", '//*[@id="tradedatestart-input"]')
			sleep(1)
			clear("xpath", '//*[@id="tradedateend-input"]')
			sleep(1)
			span_click("查询")
			
			# 刷新勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("撤销已导出")
			ok_click()
			
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'不能撤销')]")
			print("直联账户查询--所有可操作组织查询，撤销已导出功能正常")
			click("xpath", "//span[contains(text(),'直联账户查询')]")
			sleep(1)
			switch_default()
			time.sleep(3)
			
			# 测试余额调整功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 进入当前操作组织查询窗体
			switch_to("xpath", '//*[@id="directBankAccountQuery-tab-iframe"]')
			span_click("所有可操作组织查询")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("余额调整")
			
			# 当前余额
			double_click("xpath", '//*[@id="balancevalue-input"]')
			sleep(1)
			input("xpath", '//*[@id="balancevalue-input"]', '50000')
			sleep(1)
			
			# 银行可用余额
			double_click("xpath", '//*[@id="bankbalance-input"]')
			sleep(1)
			input("xpath", '//*[@id="bankbalance-input"]', '40000')
			sleep(1)
			
			# 冻结余额
			double_click("xpath", '//*[@id="freezebalance-input"]')
			sleep(1)
			input("xpath", '//*[@id="freezebalance-input"]', '10000')
			sleep(1)
			
			# 调整原因
			input("xpath", '//*[@id="adjustreason"]', '测试余额调整')
			sleep(1)
			
			click("xpath", '//*[@id="hisensureclick1"]/span/span')
			sleep(1)
			# 退出所有窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("直联账户查询--所有可操作组织，余额调整成功")
			
			# 测试调整历史查看功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 进入当前操作组织查询窗体
			switch_to("xpath", '//*[@id="directBankAccountQuery-tab-iframe"]')
			span_click("所有可操作组织查询")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("余额调整", '调整历史查看')
			switch_to("xpath", '//*[@id="printWin-iframe"]')
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//div[contains(text(),'mindy')]")
			print("直联账户查询--所有可操作住址，余额调整历史查看成功")
			switch_default()
			click("xpath", "//span[contains(text(),'直联账户查询')]")
			sleep(1)
			
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("直联账户查询失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		
		
		# 测试账户资金监控--结构账户余额🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱
		try:
			logging.info("测试账户资金监控--结构账户余额")
			# 点击账户生命周期菜单
			click("xpath", "//span[contains(text(),'结构账户余额')]")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			
			# 测试直联余额查询功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath",'//*[@id="bankAccountStructuresBalance-tab-iframe"]')
			
			#勾选按钮
			click("xpath",'//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("直联余额查询")
			# 退出所有iframe窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'直联余额查询成功')]")
			print("离线账户维护-明细维护，新增成功")
			sleep(3)
			
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("结构账户余额失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
			
	
		# 测试账户资金监控--账户余额查看🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱
		try:
			logging.info("测试账户资金监控--账户余额查看")
			# 点击账户生命周期菜单
			click("xpath", "//span[contains(text(),'账户余额查看')]")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			
			# 测试当前及下级余额查看功能功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="bankAccountBalanceView-tab-iframe"]')
			span_click("当前及下级组织余额查看")
			switch_to("xpath",'//*[@id="subTab1-iframe"]')
			
			double_click("xpath",'//*[@id="grid-body-table"]/tbody/tr[1]/td[3]/div')
			sleep(1)
			switch_to("xpath",'//*[@id="detail-iframe"]')
			sleep(1)
			implici_wait("xpath", "//span[contains(text(),'组织')]")
			print("账户余额查看-当前及下级组织余额查看，查看成功")
			switch_default()
			click("xpath", "//span[contains(text(),'账户余额查看')]")
			sleep(3)
			
			# 测试可操作组织余额查看功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="bankAccountBalanceView-tab-iframe"]')
			span_click("可操作组织余额查看")
			switch_to("xpath", '//*[@id="subTab2-iframe"]')
			
			double_click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[3]/div')
			sleep(1)
			switch_to("xpath", '//*[@id="detail-iframe"]')
			sleep(1)
			implici_wait("xpath", "//span[contains(text(),'组织')]")
			print("账户余额查看--可操作组织余额查看，查看成功")
			switch_default()
			click("xpath", "//span[contains(text(),'账户余额查看')]")
			sleep(3)
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("结构账户余额失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		
		
		# 测试账户资金监控--账户明细查看🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱
		try:
			logging.info("测试账户资金监控--账户明细查看")
			# 点击账户生命周期菜单
			click("xpath", "//span[contains(text(),'账户明细查看')]")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			
			# 测试打印功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="accountDetailView-tab-iframe"]')
			span_click("当前及下级组织明细查看")
			switch_to("xpath", '//*[@id="subTab1-iframe"]')
			
			#勾选按钮
			click("xpath",'//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div')
			sleep(1)
			
			span_click("打印")
			# 获取所有窗口句柄
			all_handles = self.driver.window_handles
			# 循环遍历所有新打开的窗口句柄，也就是说不包括主窗口
			now_handle = self.driver.current_window_handle
			for handle in all_handles:
				self.driver.switch_to.window(handle)
				if self.driver.title == u"banktransactionprint":
					implici_wait("xpath", "//td[contains(text(),'收款人')]")
					print("账户明细查看--当前及下级组织明细查看，打印成功!！")
					time.sleep(3)
					self.driver.switch_to.window(now_handle)
					switch_default()
			
			# 测试打印功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="accountDetailView-tab-iframe"]')
			span_click("可操作组织明细查看")
			switch_to("xpath", '//*[@id="subTab2-iframe"]')
			
			# 勾选按钮
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("打印")
			# 获取所有窗口句柄
			all_handles = self.driver.window_handles
			# 循环遍历所有新打开的窗口句柄，也就是说不包括主窗口
			now_handle = self.driver.current_window_handle
			for handle in all_handles:
				self.driver.switch_to.window(handle)
				if self.driver.title == u"banktransactionprint":
					implici_wait("xpath", "//td[contains(text(),'收款人')]")
					print("账户明细查看--可操作组织明细查看，打印成功!！")
					time.sleep(3)
					self.driver.switch_to.window(now_handle)
					switch_default()
			
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("账户明细查看失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
			
		
		
		
		# 测试账户资金监控--离线账户日结🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱
		try:
			logging.info("测试账户资金监控--离线账户日结")
			# 点击账户生命周期菜单
			click("xpath", "//span[contains(text(),'离线账户日结')]")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			
			# 测试日结功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="knotDates-tab-iframe"]')
			span_click("日结")
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			
			span_click("日结")
			click("xpath",'//*[@id="submit"]/span/span')
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'成功日结3条！')]")
			print("离线账户日结，日结成功")
			sleep(3)
			
			# 测试日结记录功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="knotDates-tab-iframe"]')
			span_click("日结记录")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			
			double_click("xpath",'//*[@id="grid-body-table"]/tbody/tr[1]/td[3]/div')
			sleep(1)
			switch_to("xpath",'//*[@id="detailWin-iframe"]')
			implici_wait("xpath", "//span[contains(text(),'组织')]")
			print("离线账户日结，日结记录查看成功")
			switch_default()
			click("xpath", "//span[contains(text(),'离线账户日结')]")
			sleep(3)
			
			# 测试反日结功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="knotDates-tab-iframe"]')
			span_click("日结")
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			
			span_click("反日结")
			click("xpath",'//*[@id="knotdatewin-trigger"]')
			sleep(1)
			
			switch_default()
			switch_to("xpath",'/html/body/div[6]/iframe')
			click("xpath",'//*[@id="dpTodayInput"]')
			sleep(1)
			switch_default()
			switch_to("xpath", '//*[@id="knotDates-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			
			js_click("xpath", '//*[@id="submit"]/span/span')
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'成功反日结3条！')]")
			print("离线账户日结，反日结成功")
			sleep(3)
			
			
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("账户明细查看失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
			

			
			
			
		# 测试账户资金监控--离线账户维护--明细维护🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱
		try:
			logging.info("测试账户资金监控--离线账户维护--明细维护")
			# 点击账户生命周期菜单
			click("xpath", "//span[contains(text(),'离线账户维护')]")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			
			# 测试新增功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			for i in range(1, 3):
				switch_to("xpath",'//*[@id="bankTransNonDirect-tab-iframe"]')
				span_click("明细维护")
				switch_to("xpath",'//*[@id="subTab1-iframe"]')
				
				span_click("新增")
				switch_to("xpath",'//*[@id="addWin-iframe"]')
				
				#银行账户
				click_up_click('//*[@id="combobox-input-accountid"]')
				
				#交易日期
				today=date.today()
				input("xpath",'//*[@id="tradedate-input"]',today)
				sleep(1)
				
				#交易方向
				input_up_click('//*[@id="combobox-input-moneyway"]','支出')
				
				#交易金额
				double_click("xpath",'//*[@id="amount-input"]')
				sleep(1)
				input("xpath",'//*[@id="amount-input"]','500')
				sleep(1)
				
				
				
				span_click("保存")
				# 退出所有iframe窗体
				switch_default()
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				if i == 2:
					print("离线账户维护-明细维护，新增成功")
				sleep(3)
				
			# 测试修改功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="bankTransNonDirect-tab-iframe"]')
			span_click("明细维护")
			switch_to("xpath", '//*[@id="subTab1-iframe"]')
			
			#刷新、勾选按钮
			click("xpath",'//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath",'//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
			sleep(1)
			
			span_click("修改")
			switch_to("xpath",'//*[@id="modWin-iframe"]')
			input("xpath",'//*[@id="comments"]','测试修改')
			sleep(1)
			span_click("保存")
			# 退出所有iframe窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("离线账户维护-明细维护，修改成功")
			sleep(3)
			
			# 测试修改功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="bankTransNonDirect-tab-iframe"]')
			span_click("明细维护")
			switch_to("xpath", '//*[@id="subTab1-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
			sleep(1)
			
			span_click("修改")
			switch_to("xpath", '//*[@id="modWin-iframe"]')
			input("xpath", '//*[@id="comments"]', '测试修改')
			sleep(1)
			span_click("保存")
			# 退出所有iframe窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("离线账户维护-明细维护，修改成功")
			sleep(3)
			
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("账户申请功能失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		
		
		
		
		
		
		
		
		
		
if __name__ == '__main__':
	#  启动单元测试
	unittest.main(verbosity=2)