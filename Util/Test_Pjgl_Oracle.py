# encoding=utf-8
# @Time : 2020/8/18 10:29
# @Author : Mindy
# 此文件是测试Oracle版本票据管理，包含基础设置，支票管理，承兑汇票管理，信用证管理，保函管理
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

# print("开始时间：",time.strftime("%Y-%m-%d %H:%M:%S"))

driver = ""


class Test_Pjgl(unittest.TestCase):
	
	# 启动浏览器
	def setUp(self):
		
		# 启动浏览器的另外一个方法：通过封装启动浏览器的驱动，启动不同浏览器
		self.driver = get("chrome")
	
	# 登陆系统、对系统设置进行操作
	def test_trade(self):
		
		# 通过登陆封装函数，进行登陆
		# login( G_Ora_Url,TestUser,Password, "自动化测试租户")
		# login( G_Ora_Url,Tao, Password,"默认租户")
		# login(G_Ora_Url, mindy, Password, "默认租户")
		login(G_Ora_Url, mindy, Password, "亚唐科技")
		# login( G_Mys_Url,TestUser,Password, "自动化测试租户")
		# login(G_Mys_Url, Tao, Password, "默认租户")
		# login(G_Mys_Url, mindy, Password, "亚唐科技")
		# login(G_Mys_Url, judy, Password, "默认租户")
		
		logging.info("开始测试票据管理的页面功能")
		# 将页面的滚动条滑动到‘票据管理’页面的地方
		js_gd("xpath", "//span[contains(text(),'票据管理')]")
		# 用JS的方法点击票据管理菜单按钮
		js_click("xpath", "//span[contains(text(),'票据管理')]")
		
		"""
		# 测试基础设置--支票用途
		try:
			# 点击基础设置菜单
			click("xpath", "//li[@f_value='billSetting']/descendant-or-self::*[5]")
			# 点击支票用途菜单
			click("xpath", "//li[@f_value='chequePurpose']/descendant-or-self::*[5]")
			# 退出所有iframe窗体
			switch_default()

			for i in range(1, 3):
				# 切入支票用途的iframe窗体
				switch_to("xpath", "//iframe[@id='chequePurpose-tab-iframe']")
				logging.info("开始测试支票用途功能")

				# 用JS的方法点击新增按钮
				js_click("xpath", "//span[text()='新增']")

				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='addWin-iframe']")
				sleep(1)

				# 输入用途代码
				input("xpath", "//input[@name='code']", "TestReg")
				sleep(1)

				# 输入的支票用途
				input("xpath", "//input[@id='name']", "自动化测试支票用途")
				sleep(1)

				# 描述框中填入值
				input("xpath", "//textarea[@id='description']", "自动化测试支票用途描述框")
				sleep(1)

				# 点击保存按钮
				click("xpath", "//span[text()='保存']")

				# 退出所有iframe窗体
				switch_default()

				# 用隐式等待方法等页面出现新增成功的提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				print("支票用途，保存成功！")
				time.sleep(3)

				if i == 1:
					# 删除功能
					# 切入支票用途的iframe窗体
					switch_to("xpath", "//iframe[@id='chequePurpose-tab-iframe']")

					# 点击查看
					# 用JS的方法点击放大镜
					js_click("xpath", "//span[@class='f-contrac-close']")
					sleep(1)

					# 输入代码：
					input("xpath", "//input[@id='code']", "TestReg")
					sleep(1)

					# 点击查询
					click("xpath", "//span[text()='查询']")

					# 勾选
					click("xpath", "//div[@title='用途代码:TestReg']/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 点击删除按钮
					click("xpath", "//span[text()='删除']")

					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现删除的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功')]")
					print("支票用途，删除成功！")
					time.sleep(3)

			# 切入‘支票用途’的iframe窗体
			switch_to("xpath", "//iframe[@id='chequePurpose-tab-iframe']")

			# 点击查看
			# 清空代码框的内容
			clear("xpath", "//input[@id='code']")
			sleep(1)

			# 输入用途代码：
			input("xpath", "//input[@id='code']", "TestReg")
			sleep(1)

			# 点击查询
			click("xpath", "//span[text()='查询']")

			# 修改
			# 勾选
			click("xpath", "//div[@title='用途代码:TestReg']/parent::*/preceding-sibling::*[1]/descendant::*[2]")

			# 点击修改按钮
			click("xpath", "//span[text()='修改']")

			# 切入修改的iframe窗体
			switch_to("xpath", "//iframe[@id='modWin-iframe']")
			sleep(1)

			# 修改描述框中的内容
			input("xpath", "//textarea[@id='description']", "自动化测试修改")
			sleep(1)

			# 点击保存按钮
			click("xpath", "//span[text()='保存']")

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("支票用途，修改成功！")
			time.sleep(3)

			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='支票用途']/child::*[1]")

			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//li[@f_value='billSetting']/descendant-or-self::*[5]")

			# 打印操作成功日志
			print("支票用途，操作成功!")
			logging.info("支票用途，操作成功!")
			time.sleep(2)
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("支票打印失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)

		# 测试基础设置--支票作废原因
		try:
			# 点击基础设置菜单
			click("xpath", "//li[@f_value='billSetting']/descendant-or-self::*[5]")
			# 点击支票作废原因菜单
			click("xpath", "//li[@f_value='chequeInvalidReason']/descendant-or-self::*[5]")
			# 退出所有iframe窗体
			switch_default()

			for i in range(1, 3):
				# 切入支票作废原因的iframe窗体
				switch_to("xpath", "//iframe[@id='chequeInvalidReason-tab-iframe']")
				logging.info("开始测试支票作废原因功能")

				# 用JS的方法点击新增按钮
				js_click("xpath", "//span[text()='新增']")

				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='addWin-iframe']")
				sleep(1)

				# 输入作废代码
				input("xpath", "//input[@name='code']", "TestReg")
				sleep(1)

				# 输入作废原因名称
				input("xpath", "//input[@id='name']", "自动化测试支票作废原因")
				sleep(1)

				# 描述框中填入值
				input("xpath", "//textarea[@id='description']", "自动化测试支票作废原因描述框")
				sleep(1)

				# 点击保存按钮
				click("xpath", "//span[text()='保存']")

				# 退出所有iframe窗体
				switch_default()

				# 用隐式等待方法等页面出现新增成功的提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				print("支票作废原因，保存成功！")
				time.sleep(3)

				if i == 1:
					# 删除功能
					# 切入支票作废原因的iframe窗体
					switch_to("xpath", "//iframe[@id='chequeInvalidReason-tab-iframe']")

					# 点击查看
					# 用JS的方法点击放大镜
					js_click("xpath", "//span[@class='f-contrac-close']")
					sleep(1)

					# 输入代码：
					input("xpath", "//input[@id='code']", "TestReg")
					sleep(1)

					# 点击查询
					click("xpath", "//span[text()='查询']")

					# 勾选
					click("xpath", "//div[@title='作废代码:TestReg']/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 点击删除按钮
					click("xpath", "//span[text()='删除']")

					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现删除的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功')]")
					print("支票作废原因，删除成功！")
					time.sleep(3)

			# 切入‘支票作废原因’的iframe窗体
			switch_to("xpath", "//iframe[@id='chequeInvalidReason-tab-iframe']")

			# 点击查看
			# 清空代码框的内容
			clear("xpath", "//input[@id='code']")
			sleep(1)

			# 输入作废代码：
			input("xpath", "//input[@id='code']", "TestReg")
			sleep(1)

			# 点击查询
			click("xpath", "//span[text()='查询']")

			# 修改
			# 勾选
			click("xpath", "//div[@title='作废代码:TestReg']/parent::*/preceding-sibling::*[1]/descendant::*[2]")

			# 点击修改按钮
			click("xpath", "//span[text()='修改']")

			# 切入修改的iframe窗体
			switch_to("xpath", "//iframe[@id='modWin-iframe']")
			sleep(1)

			# 修改描述框中的内容
			input("xpath", "//textarea[@id='description']", "自动化测试修改")
			sleep(1)

			# 点击保存按钮
			click("xpath", "//span[text()='保存']")

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("支票作废原因，修改成功！")
			time.sleep(3)


			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='支票作废原因']/child::*[1]")

			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//li[@f_value='billSetting']/descendant-or-self::*[5]")

			# 打印操作成功日志
			print("支票作废原因，操作成功!")
			logging.info("支票作废原因，操作成功!")
			time.sleep(2)

		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("支票作废原因打印失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)

		# 测试基础设置--承兑银行信息
		try:
			# 点击基础设置菜单
			click("xpath", "//li[@f_value='billSetting']/descendant-or-self::*[5]")
			# 点击承兑银行信息菜单
			click("xpath", "//li[@f_value='acceptancebankinfos']/descendant-or-self::*[5]")
			# 退出所有iframe窗体
			switch_default()

			for i in range(1, 2):
				# 切入承兑银行信息的iframe窗体
				switch_to("xpath", "//iframe[@id='acceptancebankinfos-tab-iframe']")
				logging.info("开始承兑银行信息功能")

				# 用JS的方法点击新增按钮
				js_click("xpath", "//span[text()='新增']")

				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='addacceptanceBankInfosWin-iframe']")
				sleep(1)

				# 模糊匹配，查找银行
				click("xpath", "//span[@title='银行']/parent::*/following-sibling::*/descendant::*[3]")

				# 输入银行名称，通过模糊匹配搜索
				input("xpath", "//span[@title='银行']/parent::*/following-sibling::*/descendant::*[3]", "工商银行")
				sleep(1)

				# 模拟回车
				double_click("xpath", "//div[contains(text(),'工商银行')]")
				sleep(1)

				# 输入评级
				input("xpath", "//span[@title='评级']/parent::*/following-sibling::*/descendant::*[3]", "AAA")
				sleep(1)

				# 输入可收票额度
				input("xpath", "//input[@id='draftamount-input']", "30000")
				sleep(1)

				# 输入贴息率(%)
				input("xpath", "//input[@id='rate-input']", "30")
				sleep(1)

				# 点击保存按钮
				click("xpath", "//span[text()='保存']")

				# 退出所有iframe窗体
				switch_default()

				# 用隐式等待方法等页面出现提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				print("承兑银行信息，保存成功！")
				time.sleep(3)

				# 通过循环验证了两个不同银行的删除功能
				if i == 1:

					# 修改功能
					# 切入承兑银行信息的iframe窗体
					switch_to("xpath", "//iframe[@id='acceptancebankinfos-tab-iframe']")

					# 点击查看
					# 用JS的方法点击放大镜
					js_click("xpath", "//span[@class='f-contrac-close']")
					sleep(1)

					# 输入银行，通过模糊匹配搜索
					click("xpath", "//input[@id='combobox-input-bankid']")
					sleep(1)
					input("xpath", "//input[@id='combobox-input-bankid']", "ICBC-工商银行")
					sleep(1)
					click("xpath", "//div[@title='代码-名称:ICBC-工商银行']")
					sleep(1)

					# 点击查询
					click("xpath", "//span[text()='查询']")

					# 修改
					# 勾选
					click("xpath", "//div[@title='评级:AAA']/parent::*/preceding-sibling::*[2]/descendant::*[2]")

					# 点击修改按钮
					click("xpath", "//span[text()='修改']")

					# 切入修改的iframe窗体
					switch_to("xpath", "//iframe[@id='modWin-iframe']")
					sleep(1)

					# 因为是金额，所以先清空，再修改描述框中的内容
					clear("xpath", "//input[@id='draftamount-input']")
					sleep(1)
					input("xpath", "//input[@id='draftamount-input']", "40000")

					# 因为是贴息率，所以先清空，再修改描述框中的内容
					clear("xpath", "//input[@id='rate-input']")
					sleep(1)
					input("xpath", "//input[@id='rate-input']", "40")
					sleep(1)

					# 点击保存按钮
					click("xpath", "//span[text()='保存']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现新增成功的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("承兑银行信息，修改成功！")
					time.sleep(3)

			# 切入‘承兑银行信息’的iframe窗体
			switch_to("xpath", "//iframe[@id='acceptancebankinfos-tab-iframe']")

			# 点击查看
			# 清空代码框的内容
			clear("xpath", "//input[@id='combobox-input-bankid']")
			sleep(1)

			click("xpath", "//input[@id='combobox-input-bankid']")
			sleep(1)
			input("xpath", "//input[@id='combobox-input-bankid']", "工商银行")
			sleep(1)
			click("xpath", "//div[@title='代码-名称:ICBC-工商银行']")
			sleep(1)

			# 点击查询
			click("xpath", "//span[text()='查询']")

			# 勾选
			click("xpath", "//div[@title='评级:AAA']/parent::*/preceding-sibling::*[2]/descendant::*[2]")

			# 点击删除按钮
			click("xpath", "//span[text()='删除']")

			# 点击弹出框的OK键
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功')]")
			print("承兑银行信息，删除成功！")
			time.sleep(3)

			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='承兑银行信息']/child::*[1]")

			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//li[@f_value='billSetting']/descendant-or-self::*[5]")

			# 打印操作成功日志
			print("承兑银行信息，操作成功!")
			logging.info("承兑银行信息，操作成功!")
			time.sleep(2)

		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("承兑银行信息打印失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)

		# 测试基础设置--电票操作类别
		try:
			# 点击基础设置菜单
			click("xpath", "//li[@f_value='billSetting']/descendant-or-self::*[5]")
			# 点击电票操作类别菜单
			click("xpath", "//span[@title='电票操作类别']")
			# 退出所有iframe窗体
			switch_default()

			for i in range(1, 2):
				# 切入支票用途的iframe窗体
				switch_to("xpath", "//iframe[@id='operationfincation-tab-iframe']")
				logging.info("开始测试电票操作类别功能")

				# 用JS的方法点击新增按钮
				js_click("xpath", "//span[text()='新增']")

				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='addWin-iframe']")
				sleep(1)

				# 输入代码
				input("xpath", "//input[@name='code']", "TestReg")
				sleep(1)

				# 输入的名称
				input("xpath", "//input[@id='name']", "自动化测试电票操作类别操作用途")
				sleep(1)

				# 描述框中填入值
				input("xpath", "//textarea[@id='description']", "自动化测试电票操作类别描述框")
				sleep(1)

				# 点击保存按钮
				click("xpath", "//span[text()='保存']")

				# 退出所有iframe窗体
				switch_default()

				# 用隐式等待方法等页面出现新增成功的提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				print("电票操作类别，保存成功！")
				time.sleep(3)

				if i == 1:
					# 删除功能
					# 切入电票操作类别的iframe窗体
					switch_to("xpath", "//iframe[@id='operationfincation-tab-iframe']")

					# 点击查看
					# 用JS的方法点击放大镜
					js_click("xpath", "//span[@class='f-contrac-close']")
					sleep(1)

					# 输入代码：
					input("xpath", "//input[@id='code']", "TestReg")
					sleep(1)

					# 点击查询
					click("xpath", "//span[text()='查询']")

					# 修改
					# 勾选
					click("xpath", "//div[@title='代码:TestReg']/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 点击修改按钮
					click("xpath", "//span[text()='修改']")

					# 切入修改的iframe窗体
					switch_to("xpath", "//iframe[@id='modWin-iframe']")
					sleep(1)

					# 修改描述框中的内容
					input("xpath", "//textarea[@id='description']", "自动化测试修改")
					sleep(1)

					# 点击保存按钮
					click("xpath", "//span[text()='保存']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现新增成功的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("电票操作类别，修改成功！")
					time.sleep(3)

			# 切入‘电票操作类别’的iframe窗体
			switch_to("xpath", "//iframe[@id='operationfincation-tab-iframe']")

			# 点击查看
			# 清空代码框的内容
			clear("xpath", "//input[@id='code']")
			sleep(1)

			# 输入代码：
			input("xpath", "//input[@id='code']", "TestReg")
			sleep(1)

			# 点击查询
			click("xpath", "//span[text()='查询']")

			# 勾选
			click("xpath", "//div[@title='代码:TestReg']/parent::*/preceding-sibling::*[1]/descendant::*[2]")

			# 点击删除按钮
			click("xpath", "//span[text()='删除']")

			# 点击弹出框的OK键
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功')]")
			print("电票操作类别用途，删除成功！")
			time.sleep(3)

			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='电票操作类别']/child::*[1]")

			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//li[@f_value='billSetting']/descendant-or-self::*[5]")

			# 打印操作成功日志
			print("电票操作类别，操作成功!")
			logging.info("电票操作类别，操作成功!")
			time.sleep(2)
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("电票操作类别打印失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)

		# 测试基础设置
		# --电票经办网点
		try:
			# 点击基础设置菜单
			click("xpath", "//li[@f_value='billSetting']/descendant-or-self::*[5]")
			# 点击承兑银行信息菜单
			click("xpath", "//span[@title='电票经办网点']")
			# 退出所有iframe窗体
			switch_default()

			for i in range(1, 3):
				# 切入电票经办网点的iframe窗体
				switch_to("xpath", "//iframe[@id='eledraftnetwork-tab-iframe']")
				logging.info("开始电票经办网点功能")

				# 用JS的方法点击新增按钮
				js_click("xpath", "//span[text()='新增']")

				# 切入新增的iframe窗体

				switch_to("xpath", "//iframe[@id='addWin-iframe']")
				sleep(1)

				# 通过循环让每次取值不同，第一次取建设银行
				if i == 1:
					click("xpath", "//input[@id='combobox-input-accountid']")

					# 输入银行名称，通过模糊匹配搜索
					input("xpath", "//input[@id='combobox-input-accountid']", "CNY")
					sleep(1)

					# 模拟回车
					double_click("xpath", "//div[contains(text(),'CNY')]")
					sleep(1)

				# 第二次取交通银行
				if i == 2:
					click("xpath", "//input[@id='combobox-input-accountid']")

					# 输入银行名称，通过模糊匹配搜索
					input("xpath", "//input[@id='combobox-input-accountid']", "USD")
					sleep(1)
					input_enter("xpath", "//input[@id='combobox-input-accountid']")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-accountid']")
					sleep(1)
					input_enter("xpath", "//input[@id='combobox-input-accountid']")
					sleep(1)
					# 模拟回车
					# double_click("xpath", "//div[contains(text(),'USD')]")
					# sleep(1)

				# 点击保存按钮
				click("xpath", "//span[text()='保存']")

				# 退出所有iframe窗体
				switch_default()

				# 用隐式等待方法等页面出现提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				print("电票经办网点，保存成功！")
				time.sleep(3)

				# 通过循环验证了两个不同银行的删除功能
				if i == 1:
					# 删除功能
					# 切入电票经办网点的iframe窗体
					switch_to("xpath", "//iframe[@id='eledraftnetwork-tab-iframe']")

					# 点击查看
					# 用JS的方法点击放大镜
					js_click("xpath", "//span[@class='f-contrac-close']")
					sleep(1)

					# 输入银行，通过模糊匹配搜索
					click("xpath", "//input[@id='combobox-input-accountid']")
					sleep(1)
					input("xpath", "//input[@id='combobox-input-accountid']", "CNY")
					sleep(1)
					# 模拟回车
					double_click("xpath", "//div[contains(text(),'CNY')]")
					sleep(1)

					# 点击查询
					click("xpath", "//span[text()='查询']")

					# 勾选
					click("xpath", "//div[contains(text(),'亚唐科技')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 点击删除按钮
					click("xpath", "//span[text()='删除']")

					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					sleep(1)

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现新增成功的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("电票经办网点，删除成功！")
					time.sleep(3)

			# 切入‘电票经办网点’的iframe窗体
			switch_to("xpath", "//iframe[@id='eledraftnetwork-tab-iframe']")

			# 点击查看
			# 清空代码框的内容
			clear("xpath", "//input[@id='combobox-input-accountid']")
			sleep(1)

			# 输入银行，通过模糊匹配搜索
			click("xpath", "//input[@id='combobox-input-accountid']")
			sleep(1)
			# 输入银行名称，通过模糊匹配搜索
			input("xpath", "//input[@id='combobox-input-accountid']", "USD")
			sleep(1)
			input_enter("xpath", "//input[@id='combobox-input-accountid']")
			time.sleep(1)
			# 模拟回车
			input_down("xpath","//input[@id='combobox-input-accountid']")
			sleep(1)
			input_enter("xpath","//input[@id='combobox-input-accountid']")
			time.sleep(1)
			# double_click("xpath", "//div[contains(text(),'USD')]")
			# sleep(1)

			# 点击查询
			click("xpath", "//span[text()='查询']")

			# 修改
			# 勾选
			click("xpath", "//div[contains(text(),'亚唐科技')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

			# 点击修改按钮
			click("xpath", "//span[text()='修改']")

			# 切入修改的iframe窗体
			switch_to("xpath", "//iframe[@id='modWin-iframe']")
			sleep(1)

			# 因为是金额，所以先清空，再修改描述框中的内容
			click("xpath", "//input[@id='combobox-input-accountid']")
			sleep(1)
			clear("xpath", "//input[@id='combobox-input-accountid']")
			sleep(1)
			input("xpath", "//input[@id='combobox-input-accountid']", "USD")
			sleep(1)
			input_enter("xpath", "//input[@id='combobox-input-accountid']")
			sleep(1)
			input_down("xpath", "//input[@id='combobox-input-accountid']")
			sleep(1)
			input_enter("xpath", "//input[@id='combobox-input-accountid']")
			sleep(1)
			# 点击保存按钮
			click("xpath", "//span[text()='保存']")

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("电票经办网点，修改成功！")
			time.sleep(3)

			# 删除功能
			# 切入电票经办网点的iframe窗体
			switch_to("xpath", "//iframe[@id='eledraftnetwork-tab-iframe']")

			# 勾选
			click("xpath", "//div[contains(text(),'亚唐科技')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

			# 点击删除按钮
			click("xpath", "//span[text()='删除']")

			# 点击弹出框的OK键
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
			sleep(1)

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("电票经办网点，删除成功！")
			time.sleep(3)

			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='电票经办网点']/child::*[1]")

			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//li[@f_value='billSetting']/descendant-or-self::*[5]")

			# 打印操作成功日志
			print("电票经办网点，操作成功!")
			logging.info("电票经办网点，操作成功!")
			time.sleep(2)

		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("电票经办网点打印失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)

		# 添加部门数据
		# 系统参数--部门
		try:
			# 点击系统设置
			click("xpath", "//div[@class='sysconfigset']")

			# 点击进入系统设置页面
			switch_to("xpath", "//iframe[@id='systemconfig-tab-iframe']")
			sleep(1)

			logging.info("开始测试基础资料--部门功能")
			# 将页面的滚动条滑动到‘部门’页面的地方
			js_gd("xpath", "//span[contains(text(),'部门')]")
			# 用JS的方法部门字段菜单按钮
			js_click("xpath", "//span[contains(text(),'部门')]")

			switch_default()

			switch_to("xpath", "//iframe[@id='deptManager-tab-iframe']")

			# 用JS的方法点击新增按钮
			js_click("xpath", "//span[text()='新增']")

			# 切入新增的iframe窗体
			switch_to("xpath", "//iframe[@id='addWin-iframe']")
			sleep(1)

			# 输入代码
			temp = time.strftime("%Y%m%d%H%M%S")
			input("xpath", "//input[@name='code']", "TestBm" + str(temp))
			sleep(1)

			# 输入名称
			input("xpath", "//input[@id='name']", "自动化测试部")
			sleep(1)

			# 选择生效
			click("xpath", "//input[@id='isactive']")
			sleep(1)

			# 点击保存按钮
			click("xpath", "//span[text()='保存']")

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("部门功能，保存成功！")
			time.sleep(3)

			# 再次点击基础设置菜单，使之关闭
			# 用JS的方法关闭当前页面

			js_click("xpath", "//a[@title='部门']/child::*[1]")

			# 打印操作成功日志
			print("部门，操作成功!")
			logging.info("部门，操作成功!")
			time.sleep(2)

		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("部门功能,失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)

		# 添加资金类别数据
		# 系统参数--资金类别
		try:
			# 点击系统设置
			click("xpath", "//div[@class='sysconfigset']")

			# 点击进入系统设置页面
			switch_to("xpath", "//iframe[@id='systemconfig-tab-iframe']")
			sleep(1)

			logging.info("开始测试基础资料--资金类别功能")
			# 将页面的滚动条滑动到‘资金类别’页面的地方
			js_gd("xpath", "//span[contains(text(),'资金类别')]")
			# 用JS的方法部门字段菜单按钮
			js_click("xpath", "//span[contains(text(),'资金类别')]")

			switch_default()

			switch_to("xpath", "//iframe[@id='fundCategoriesManager-tab-iframe']")

			# 用JS的方法点击新增按钮
			js_click("xpath", "//span[text()='新增']")

			# 切入新增的iframe窗体
			switch_to("xpath", "//iframe[@id='addWin-iframe']")
			sleep(1)

			# 输入代码
			temp = time.strftime("%Y%m%d%H%M%S")
			input("xpath", "//input[@name='code']", "TestZjle" + str(temp))
			sleep(1)

			# 输入名称
			input("xpath", "//input[@id='name']", "自动化测试资金类别")
			sleep(1)

			# 点击保存按钮
			click("xpath", "//span[text()='保存']")

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("资金类别，保存成功！")
			time.sleep(3)

			# 再次点击基础设置菜单，使之关闭
			# 用JS的方法关闭当前页面

			js_click("xpath", "//a[@title='资金类别']/child::*[1]")

			# 打印操作成功日志
			print("资金类别，操作成功!")
			logging.info("资金类别，操作成功!")
			time.sleep(2)

		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("资金类别,失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)

		# 添加现金流量项目数据
		# 系统参数--现金流量项目
		try:
			# 点击系统设置
			click("xpath", "//div[@class='sysconfigset']")

			# 点击进入系统设置页面
			switch_to("xpath", "//iframe[@id='systemconfig-tab-iframe']")
			sleep(1)

			logging.info("开始测试基础资料--现金流量项目功能")
			# 将页面的滚动条滑动到‘现金流量项目’页面的地方
			js_gd("xpath", "//span[contains(text(),'现金流量项目')]")
			# 用JS的方法现金流量项目菜单按钮
			js_click("xpath", "//span[contains(text(),'现金流量项目')]")

			switch_default()

			switch_to("xpath", "//iframe[@id='cashFlowItem-tab-iframe']")

			# 用JS的方法点击新增按钮
			js_click("xpath", "//span[text()='新增']")

			# 切入新增的iframe窗体
			switch_to("xpath", "//iframe[@id='modWin-iframe']")
			sleep(1)

			# 输入代码
			temp = time.strftime("%Y%m%d%H%M%S")
			input("xpath", "//input[@name='code']", "TestXjlXm" + str(temp))
			sleep(1)

			# 输入名称
			input("xpath", "//input[@id='name']", "自动化测试现金流量项目")
			sleep(1)

			# 选择交易方式
			click("xpath", "//input[@id='combobox-input-moneyway']")
			sleep(1)
			input("xpath", "//input[@id='combobox-input-moneyway']", "收入")
			input_enter("xpath", "//input[@id='combobox-input-moneyway']")
			sleep(1)
			input_down("xpath", "//input[@id='combobox-input-moneyway']")
			sleep(1)
			input_enter("xpath", "//input[@id='combobox-input-moneyway']")
			sleep(1)

			# 点击保存按钮
			click("xpath", "//span[text()='保存']")

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("现金流量项目，保存成功！")
			time.sleep(3)

			# 再次点击基础设置菜单，使之关闭
			# 用JS的方法关闭当前页面

			js_click("xpath", "//a[@title='现金流量项目']/child::*[1]")

			# 打印操作成功日志
			print("现金流量项目，操作成功!")
			logging.info("现金流量项目，操作成功!")
			time.sleep(2)
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("现金流量项目,失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)

		# 添加工程项目管理数据
		# 系统参数--工程项目管理
		try:
			# 点击系统设置
			click("xpath", "//div[@class='sysconfigset']")

			# 点击进入系统设置页面
			switch_to("xpath", "//iframe[@id='systemconfig-tab-iframe']")
			sleep(1)

			logging.info("开始测试基础资料--工程项目管理功能")
			# 将页面的滚动条滑动到‘现金流量项目’页面的地方
			js_gd("xpath", "//span[contains(text(),'工程项目管理')]")
			# 用JS的方法现金流量项目菜单按钮
			js_click("xpath", "//span[contains(text(),'工程项目管理')]")

			switch_default()

			switch_to("xpath", "//iframe[@id='projectItemsManage-tab-iframe']")
			switch_to("xpath", "//iframe[@id='subTabOne-iframe']")

			# 用JS的方法点击新增按钮
			js_click("xpath", "//span[text()='新增']")

			# 切入新增的iframe窗体
			switch_to("xpath", "//iframe[@id='addWin-iframe']")
			sleep(1)

			# 输入代码TestPro001-自动化测试工程项目
			input("xpath", "//input[@name='code']", "TestPro001")
			sleep(1)

			# 输入名称
			input("xpath", "//input[@id='name']", "自动化测试工程项目")
			sleep(1)

			# 选择下级组织共享
			click("xpath", "//input[@id='includesubs']")
			sleep(1)

			# 选择组织
			click("xpath", "//input[@id='combobox-input-orgid']")
			sleep(1)
			input("xpath", "//input[@id='combobox-input-orgid']", "亚唐科技")
			input_enter("xpath", "//input[@id='combobox-input-orgid']")
			sleep(1)
			input_down("xpath", "//input[@id='combobox-input-orgid']")
			sleep(1)
			input_enter("xpath", "//input[@id='combobox-input-orgid']")
			sleep(1)
			# 点击保存按钮
			click("xpath", "//span[text()='保存']")

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("工程项目管理，保存成功！")
			time.sleep(3)

			# 再次点击基础设置菜单，使之关闭
			# 用JS的方法关闭当前页面

			js_click("xpath", "//a[@title='工程项目管理']/child::*[1]")

			# 打印操作成功日志
			print("工程项目管理，操作成功!")
			logging.info("工程项目管理，操作成功!")
			time.sleep(2)
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("工程项目管理,失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)

		# 测试支票管理--应付支票登记功能
		try:
			# 点击支票管理菜单
			click("xpath", "//span[@title='支票管理']")
			# 点击应付支票登记菜单
			click("xpath", "//span[@title='应付支票登记']")
			# 退出所有的iframe窗体
			switch_default()

			logging.info("开始测试应付支票登记功能")
			for i in range(1, 3):
				# 切入应付支票登记iframe窗体
				switch_to("xpath", "//iframe[@id='chequeStorage-tab-iframe']")

				# 用JS的方法点击新增按钮
				js_click("xpath", "//span[text()='新增']")

				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='addWin-iframe']")
				sleep(1)

				# 通过循环让每次取值不同，第一次取现金/转账
				if i == 1:
					click("xpath", "//input[@id='combobox-input-booktype']")
					# 输入银行名称，通过模糊匹配搜索
					input("xpath", "//input[@id='combobox-input-booktype']", "现金/转账")
					sleep(1)
					# 模拟回车
					double_click("xpath", "//div[contains(text(),'现金/转账')]")
					sleep(1)

					# 输入起始码
					input("xpath", "//input[@id='codefrom']", "1117")
					sleep(1)

					# 输入终止码
					input("xpath", "//input[@id='codeto']", "1119")
					sleep(1)

					click("xpath", "//input[@id='combobox-input-bankid']")
					# 输入银行名称，通过模糊匹配搜索
					input("xpath", "//input[@id='combobox-input-bankid']", "BOC-中国银行")
					sleep(1)
					# 模拟回车
					double_click("xpath", "//div[contains(text(),'BOC-中国银行')]")
					sleep(1)

					click("xpath", "//input[@id='combobox-input-accountid']")
					# 输入银行名称，通过模糊匹配搜索
					input("xpath", "//input[@id='combobox-input-accountid']", "2020")
					sleep(1)
					input_enter("xpath", "//input[@id='combobox-input-accountid']")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-accountid']")
					sleep(1)
					input_enter("xpath", "//input[@id='combobox-input-accountid']")
					time.sleep(1)

					# 备注框中填入值
					input("xpath", "//textarea[@id='description']", "自动化测试应付支票登记备注框")
					sleep(1)

					# 点击保存按钮
					click("xpath", "//span[text()='保存']")

					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					sleep(1)

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("应付支票登记第%s次，保存成功！" % i)
					logging.info("应付支票登记第%s次，保存成功！" % i)
					time.sleep(3)

				else:
					click("xpath", "//input[@id='combobox-input-booktype']")
					# 输入银行名称，通过模糊匹配搜索
					input("xpath", "//input[@id='combobox-input-booktype']", "转账")
					sleep(1)
					# 模拟回车
					double_click("xpath", "//div[contains(text(),'转账')]")
					sleep(1)

					# 输入起始码
					input("xpath", "//input[@id='codefrom']", "1208")
					sleep(1)

					# 输入终止码
					input("xpath", "//input[@id='codeto']", "1210")
					sleep(1)

					click("xpath", "//input[@id='combobox-input-bankid']")
					# 输入银行名称，通过模糊匹配搜索
					input("xpath", "//input[@id='combobox-input-bankid']", "中国银行")
					sleep(1)
					# 模拟回车
					double_click("xpath", "//div[contains(text(),'中国银行')]")
					sleep(1)

					click("xpath", "//input[@id='combobox-input-accountid']")
					# 输入银行名称，通过模糊匹配搜索
					input("xpath", "//input[@id='combobox-input-accountid']", "CNY")
					sleep(1)
					# 模拟回车
					double_click("xpath", "//div[contains(text(),'CNY')]")
					sleep(1)

					# 备注框中填入值
					input("xpath", "//textarea[@id='description']", "自动化测试应付支票登记备注框")
					sleep(1)

					# 点击保存按钮
					click("xpath", "//span[text()='保存']")

					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					sleep(1)

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("应付支票登记第%s次，保存成功！" % i)
					logging.info("应付支票登记第%s次，保存成功！" % i)
					time.sleep(3)

				# 通过循环验证了两个不同银行的删除功能
				if i == 1:
					# 删除功能
					# 切入应付支票登记iframe窗体
					switch_to("xpath", "//iframe[@id='chequeStorage-tab-iframe']")

					# 点击查看
					# 用JS的方法点击放大镜
					js_click("xpath", "//span[@class='f-contrac-close']")
					sleep(1)

					# # 输入银行，通过模糊匹配搜索
					# click("xpath", "//input[@id='combobox-input-accountid']")
					# sleep(1)
					# input("xpath", "//input[@id='combobox-input-accountid']", "CNY")
					# sleep(1)
					# input_down("xpath", "//input[@id='combobox-input-accountid']")
					# input_enter("xpath", "//input[@id='combobox-input-accountid']")
					# time.sleep(1)

					# 输入银行，通过模糊匹配搜索
					click("xpath", "//input[@id='combobox-input-booktype']")
					sleep(1)
					input("xpath", "//input[@id='combobox-input-booktype']", "现金/转账")
					sleep(1)
					click("xpath", "//div[@title='现金/转账']")
					sleep(1)

					# 点击查询
					click("xpath", "//span[text()='查询']")

					# 勾选
					click("xpath", "//div[@title='币种:CNY-人民币']/parent::*/preceding-sibling::*[3]/descendant::*[2]")

					# 点击删除按钮
					click("xpath", "//span[text()='删除']")

					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					sleep(1)

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现新增成功的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("应付支票登记，删除成功！")
					time.sleep(3)

			# # 切入'应付支票登记’的iframe窗体
			switch_to("xpath", "//iframe[@id='chequeStorage-tab-iframe']")

			# 点击查看
			# 清空银行账号框的内容
			clear("xpath", "//input[@id='combobox-input-accountid']")
			sleep(1)

			# 输入银行，通过模糊匹配搜索
			click("xpath", "//input[@id='combobox-input-booktype']")
			sleep(1)
			click("xpath", "//div[@title='现金/转账']")
			sleep(1)
			click("xpath", "//div[@title='转账']")
			sleep(1)

			# 点击查询
			click("xpath", "//span[text()='查询']")

			# 修改
			# 勾选
			click("xpath", "//div[@title='币种:CNY-人民币']/parent::*/preceding-sibling::*[3]/descendant::*[2]")

			# 点击修改按钮
			click("xpath", "//span[text()='修改']")

			# 切入修改的iframe窗体
			switch_to("xpath", "//iframe[@id='modWin-iframe']")
			sleep(2)

			# 修改起始码框中的内容
			click("xpath", "//input[@id='codefrom']")
			sleep(1)
			clear("xpath", "//input[@id='codefrom']")
			sleep(1)
			input("xpath", "//input[@id='codefrom']", "1220")
			sleep(1)

			# 修改终止码框中的内容
			clear("xpath", "//input[@id='codeto']")
			sleep(1)
			input("xpath", "//input[@id='codeto']", "1223")
			sleep(1)

			# 修改银行，先清空原有银行，再修改银行框中的内容
			click("xpath", "//input[@id='combobox-input-bankid']")
			sleep(1)
			clear("xpath", "//input[@id='combobox-input-bankid']")
			sleep(1)
			input("xpath", "//input[@id='combobox-input-bankid']", "HXB-华夏银行")
			sleep(1)
			# 模拟回车
			double_click("xpath", "//div[contains(text(),'HXB-华夏银行')]")
			sleep(1)

			# 修改银行，先清空原有银行，再修改银行框中的内容
			click("xpath", "//input[@id='combobox-input-accountid']")
			sleep(1)
			clear("xpath", "//input[@id='combobox-input-accountid']")
			sleep(1)
			input("xpath", "//input[@id='combobox-input-accountid']", "CNY")
			sleep(1)
			input_enter("xpath", "//input[@id='combobox-input-accountid']")
			sleep(1)
			# 模拟回车
			input_down("xpath", "//input[@id='combobox-input-accountid']")
			sleep(1)
			input_enter("xpath", "//input[@id='combobox-input-accountid']")
			time.sleep(1)

			# 修改备注框中值
			input("xpath", "//textarea[@id='description']", "自动化测试修改")
			sleep(1)

			# 点击保存按钮
			click("xpath", "//span[text()='保存']")

			# 点击弹出框的OK键
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
			sleep(1)

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("应付支票登记，修改成功！")
			time.sleep(3)

			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='应付支票登记']/child::*[1]")

			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//span[@title='支票管理']")

			# 打印操作成功日志
			print("应付支票登记，操作成功!")
			logging.info("应付支票登记，操作成功!")
			time.sleep(2)

		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("应付支票登记打印失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)

		# 支票登记后去付款处理新增该账户的付款单
		logging.info("开始测试资金结算管理的页面功能")
		# 将页面的滚动条滑动到‘资金结算管理’页面的地方
		js_gd("xpath", "//span[contains(text(),'资金结算管理')]")
		# 用JS的方法点击资金结算管理菜单按钮
		js_click("xpath", "//span[contains(text(),'资金结算管理')]")

		# 付款处理--支票支付
		try:
			# 点击资金系统收付菜单
			click("xpath", "//span[@title='资金系统收付']")
			# 点击应付支票领用菜单
			click("xpath", "//span[@title='付款处理']")
			# 退出所有的iframe窗体
			switch_default()

			logging.info("开始测试付款处理功能")

			# 切入‘付款处理’的iframe窗体
			switch_to("xpath", "//iframe[@id='generalPayment-tab-iframe']")

			# 点击支票支付tab页
			click("xpath", "//span[text()='支票支付']")

			# 切入‘支票支付’的iframe窗体
			switch_to("xpath", "//iframe[@id='subTabFive-iframe']")
			sleep(1)

			# 用JS的方法点击新增按钮
			js_click("xpath", "//span[text()='新增']")

			# 切入新增的iframe窗体
			switch_to("xpath", "//iframe[@id='addWin-iframe']")
			sleep(1)

			# 选择交易类型
			click("xpath", "//input[@id='combobox-input-paytypeid']")
			input("xpath", "//input[@id='combobox-input-paytypeid']", "103-对外付款")
			sleep(1)
			input_down("xpath", "//input[@id='combobox-input-paytypeid']")
			input_enter("xpath", "//input[@id='combobox-input-paytypeid']")
			time.sleep(1)

			# 选择结算方式
			click("xpath", "//input[@id='combobox-input-settlementmodeid']")
			clear("xpath", "//input[@id='combobox-input-settlementmodeid']")
			input("xpath", "//input[@id='combobox-input-settlementmodeid']", "402-转账支票支付")
			sleep(1)
			input_down("xpath", "//input[@id='combobox-input-settlementmodeid']")
			sleep(1)
			input_enter("xpath", "//input[@id='combobox-input-settlementmodeid']")
			time.sleep(1)

			# 付方账户
			click("xpath", "//input[@id='combobox-input-ourbankaccountid']")
			sleep(1)
			input("xpath", "//input[@id='combobox-input-ourbankaccountid']", "华夏银行")
			sleep(1)
			input_enter("xpath", "//input[@id='combobox-input-ourbankaccountid']")
			time.sleep(1)
			input_down("xpath", "//input[@id='combobox-input-ourbankaccountid']")
			sleep(1)
			input_enter("xpath", "//input[@id='combobox-input-ourbankaccountid']")
			time.sleep(1)

			# 收方名称
			click("xpath", "//input[@id='combobox-input-oppcounterpartyid']")
			sleep(1)
			input("xpath", "//input[@id='combobox-input-oppcounterpartyid']", "Mindy自动化测试")
			sleep(1)

			click("xpath", "//input[@id='combobox-input-oppcardtype']")
			sleep(1)

			# 输入金额
			input("xpath", "//input[@id='ouramount-input']", "226")
			sleep(1)

			# 点击保存
			click("xpath", "//span[text()='保存']")

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("付款处理，支票支付保存成功！")
			logging.info("付款处理，支票支付保存成功！")
			sleep(3)

			# 切入‘付款处理’的iframe窗体
			switch_to("xpath", "//iframe[@id='generalPayment-tab-iframe']")

			# 点击支票支付tab页
			click("xpath", "//span[text()='支票支付']")

			# 切入‘支票支付’的iframe窗体
			switch_to("xpath", "//iframe[@id='subTabFive-iframe']")
			sleep(1)

			# 选择新建的付款单
			click("xpath", "//div[@title='收款户名:Mindy自动化测试']/parent::*[1]/preceding-sibling::*[6]/descendant::*[2]")

			# 点击送审按钮
			click("xpath", "//span[text()='送审']")

			# 点击弹出的OK框
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！送审成功1笔，失败0笔。')]")
			print("支票支付，第一次送审成功！")
			logging.info("支票支付，第一次送审成功！")
			time.sleep(3)

			# 点击审核
			# 切入‘付款处理’的iframe窗体
			switch_to("xpath", "//iframe[@id='generalPayment-tab-iframe']")

			# 点击支票支付tab页
			click("xpath", "//span[text()='支票支付']")

			# 切入‘支票支付’的iframe窗体
			switch_to("xpath", "//iframe[@id='subTabFive-iframe']")
			sleep(1)

			# 点击审核按钮
			double_click("xpath",
			             "//div[@title='收款户名:Mindy自动化测试']/parent::*[1]/preceding-sibling::*[6]/descendant::*[2]")
			sleep(1)

			switch_to("xpath", "//iframe[@id='wf_taskProcessing_win-iframe']")
			sleep(1)

			click("xpath", "//span[text()='同意']")
			sleep(1)

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("支票支付，审批成功！")
			logging.info("支票支付，审批成功！")
			time.sleep(3)

			# 切入‘付款处理’的iframe窗体
			switch_to("xpath", "//iframe[@id='generalPayment-tab-iframe']")

			# 点击支票支付tab页
			click("xpath", "//span[text()='支票支付']")

			# 切入‘支票支付’的iframe窗体
			switch_to("xpath", "//iframe[@id='subTabFive-iframe']")
			sleep(1)

			# 选择新建的付款单
			click("xpath", "//div[@title='收款户名:Mindy自动化测试']/parent::*[1]/preceding-sibling::*[6]/descendant::*[2]")

			# 点击领用按钮
			click("xpath", "//span[text()='领用']")
			sleep(1)

			# 切入领用的iframe窗体
			switch_to("xpath", "//iframe[@id='chequerecipientsWin-iframe']")
			sleep(1)

			# 选择一条数据
			click("xpath", "//div[@title='支票号:1222']/parent::*[1]/preceding-sibling::*[5]/descendant::*[2]")
			sleep(1)

			# 点击下一步
			click("xpath", "//span[text()='下一步']")
			sleep(1)

			# 切入领用页面的iframe窗体applyWin-iframe
			switch_to("xpath", "//iframe[@id='applyWin-iframe']")
			sleep(1)

			# 输入领用人名称
			input("xpath", "//input[@id='username']", "mindy")
			sleep(1)

			click("xpath", "//input[@id='combobox-input-chequepurposeid']")
			# 输入支票用途，通过模糊匹配搜索
			input("xpath", "//input[@id='combobox-input-chequepurposeid']", "自动化测试支票用途")
			sleep(1)
			# 模拟回车
			double_click("xpath", "//div[contains(text(),'自动化测试支票用途')]")
			sleep(1)

			# 点击领用按钮
			click("xpath", "//span[text()='领用']")

			# 显示等待3秒，首先页面不退出，继续点击该页面的审核按钮
			print("应付支票领用成功！")
			sleep(3)

			# 点击审核按钮
			click("xpath", "//span[text()='审核']")
			print("应付支票审核成功！")
			sleep(3)
			switch_default()

			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='付款处理']/child::*[1]")

			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//span[@title='资金系统收付']")

			# 打印操作成功日志
			print("付款处理，操作成功!")
			logging.info("付款处理，操作成功!")
			time.sleep(2)

		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("付款处理，支票支付打印失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)

		logging.info("开始测试票据管理的页面功能")
		# 将页面的滚动条滑动到‘票据管理’页面的地方
		# js_gd("xpath", "//span[contains(text(),'票据管理')]")
		# 用JS的方法点击票据管理菜单按钮
		js_click("xpath", "//span[contains(text(),'票据管理')]")

		# 测试应付支票领用
		try:
			# 点击支票管理菜单
			click("xpath", "//span[@title='支票管理']")
			# 点击应付支票领用菜单
			click("xpath", "//span[@title='应付支票领用']")
			# 退出所有的iframe窗体
			switch_default()

			logging.info("开始测试应付支票领用功能")
			# 切入‘应付支票领用’的iframe窗体
			switch_to("xpath", "//iframe[@id='chequeRecipients-tab-iframe']")

			# 通过一组数据实现页面功能的测试
			# 点击查看
			# 用JS的方法点击放大镜
			js_click("xpath", "//span[@class='f-contrac-close']")
			sleep(1)

			# 输入支票号，通过模糊匹配搜索
			click("xpath", "//input[@id='chequecode']")
			sleep(1)
			input("xpath", "//input[@id='chequecode']", "1222")
			sleep(1)

			# 点击查询
			click("xpath", "//span[text()='查询']")

			# 用隐式等待方法等页面出现预期数据：支票状态:登记入库
			implici_wait("xpath", "//div[@title='支票状态:已领用']")
			implici_wait("xpath", "//div[@title='审核状态:已审核']")
			print("应用支票领用状态查看成功！")
			time.sleep(3)

			switch_default()

			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='应付支票领用']/child::*[1]")

			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//span[@title='支票管理']")

			# 打印操作成功日志
			print("应付支票领用，操作成功!")
			logging.info("应付支票领用，操作成功!")
			time.sleep(2)

		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("应付支票领用,失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)

		# 支票登记后去付款处理新增该账户的付款单
		logging.info("开始测试资金结算管理的页面功能")
		# 将页面的滚动条滑动到‘资金结算管理’页面的地方
		js_gd("xpath", "//span[contains(text(),'资金结算管理')]")
		# 用JS的方法点击资金结算管理菜单按钮
		js_click("xpath", "//span[contains(text(),'资金结算管理')]")

		# 付款处理--支票支付
		try:
			# 点击资金系统收付菜单
			click("xpath", "//span[@title='资金系统收付']")
			# 点击应付支票领用菜单
			click("xpath", "//span[@title='付款处理']")
			# 退出所有的iframe窗体
			switch_default()

			logging.info("开始测试付款处理功能")

			# 切入‘付款处理’的iframe窗体
			switch_to("xpath", "//iframe[@id='generalPayment-tab-iframe']")

			# 点击支票支付tab页
			click("xpath", "//span[text()='支票支付']")

			# 切入‘支票支付’的iframe窗体
			switch_to("xpath", "//iframe[@id='subTabFive-iframe']")
			sleep(1)

			# 选择新建的付款单
			click("xpath", "//div[@title='收款户名:Mindy自动化测试']/parent::*[1]/preceding-sibling::*[6]/descendant::*[2]")

			# 点击作废按钮
			click("xpath", "//span[text()='作废']")

			# 点击弹出的OK框
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("支票支付，作废成功！")
			logging.info("支票支付，作废成功！")
			time.sleep(3)

			switch_default()

			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='付款处理']/child::*[1]")

			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//span[@title='资金系统收付']")

			# 打印操作成功日志
			print("付款处理，作废操作成功!")
			logging.info("付款处理，作废操作成功!")
			time.sleep(2)

		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("付款处理，作废操作失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)

		logging.info("开始测试票据管理的页面功能")
		# 将页面的滚动条滑动到‘票据管理’页面的地方
		# js_gd("xpath", "//span[contains(text(),'票据管理')]")
		# 用JS的方法点击票据管理菜单按钮
		js_click("xpath", "//span[contains(text(),'票据管理')]")

		# 测试应付支票领用
		try:
			# 点击支票管理菜单
			click("xpath", "//span[@title='支票管理']")
			# 点击应付支票领用菜单
			click("xpath", "//span[@title='应付支票领用']")
			# 退出所有的iframe窗体
			switch_default()

			logging.info("开始测试应付支票领用功能")
			# 切入‘应付支票领用’的iframe窗体
			switch_to("xpath", "//iframe[@id='chequeRecipients-tab-iframe']")

			# 通过一组数据实现页面功能的测试
			# 点击查看
			# 用JS的方法点击放大镜
			js_click("xpath", "//span[@class='f-contrac-close']")
			sleep(1)

			# 输入支票号，通过模糊匹配搜索
			click("xpath", "//input[@id='chequecode']")
			sleep(1)
			input("xpath", "//input[@id='chequecode']", "1222")
			sleep(1)

			# 点击查询
			click("xpath", "//span[text()='查询']")

			# 勾选
			click("xpath", "//div[@title='支票号:1222']/parent::*/preceding-sibling::*[5]/descendant::*[2]")

			# 用JS的方法点击支票领用按钮
			js_click("xpath", "//span[text()='支票领用']")

			# 切入支票领用的iframe窗体
			switch_to("xpath", "//iframe[@id='applyWin-iframe']")
			sleep(1)

			# 输入领用人名称
			input("xpath", "//input[@id='username']", "mindy")
			sleep(1)

			click("xpath", "//input[@id='combobox-input-usedepartid']")
			# 输入领用部门名称，通过模糊匹配搜索
			input("xpath", "//input[@id='combobox-input-usedepartid']", "自动化测试部")
			sleep(1)
			# 模拟回车
			double_click("xpath", "//div[contains(text(),'自动化测试部')]")
			sleep(1)

			# 输入收款人名称
			input("xpath", "//input[@id='receiever']", "mindy")
			sleep(1)

			click("xpath", "//input[@id='combobox-input-chequepurposeid']")
			# 输入支票用途，通过模糊匹配搜索
			input("xpath", "//input[@id='combobox-input-chequepurposeid']", "自动化测试支票用途")
			sleep(1)
			# 模拟回车
			double_click("xpath", "//div[contains(text(),'自动化测试支票用途')]")
			sleep(1)

			# 金额中填入值
			clear("xpath", "//input[@id='useamount-input']")
			input("xpath", "//input[@id='useamount-input']", "500")
			sleep(1)

			# 备注框中填入值
			input("xpath", "//textarea[@id='description']", "自动化测试应付支票领用备注框")
			sleep(1)

			# 点击领用按钮
			click("xpath", "//span[text()='领用']")

			# 显示等待3秒，首先页面不退出，继续点击该页面的审核按钮
			print("应付支票领用成功！")
			sleep(3)

			# 点击审核按钮
			click("xpath", "//span[text()='审核']")
			print("应付支票审核成功！")
			sleep(3)
			switch_default()
			# 切入应付支票领用窗体
			switch_to("xpath", "//iframe[@id='chequeRecipients-tab-iframe']")

			# 先清除支票号输入框，然后输入支票号，通过模糊匹配搜索
			clear("xpath", "//input[@id='chequecode']")
			sleep(1)
			input("xpath", "//input[@id='chequecode']", "1222")
			sleep(1)

			# 点击查询
			click("xpath", "//span[text()='查询']")
			# 勾选
			click("xpath", "//div[@title='支票号:1222']/parent::*/preceding-sibling::*[5]/descendant::*[2]")

			# 点击取消审核
			click("xpath", "//span[text()='取消审核']")

			# 点击弹出框的OK键
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
			sleep(1)

			print("应付支票领用审核取消成功！！")
			sleep(3)

			# 选择勾选，完成领用取消
			click("xpath", "//div[@title='支票号:1222']/parent::*/preceding-sibling::*[5]/descendant::*[2]")

			# 点击领用取消
			click("xpath", "//span[text()='领用取消']")

			# 点击弹出框的OK键
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
			sleep(1)

			print("应付支票领用取消成功！！")
			sleep(3)

			click("xpath", "//div[@title='支票号:1222']/parent::*/preceding-sibling::*[5]/descendant::*[2]")

			# 用JS的方法点击支票领用按钮，再次支票领用
			js_click("xpath", "//span[text()='支票领用']")

			# 切入支票领用的iframe窗体
			switch_to("xpath", "//iframe[@id='applyWin-iframe']")
			sleep(1)

			# click("xpath", "//input[@id='username']")
			# 输入领用人名称，通过模糊匹配搜索
			input("xpath", "//input[@id='username']", "Biandi Tian")
			sleep(1)

			click("xpath", "//input[@id='combobox-input-usedepartid']")
			# 输入领用部门名称，通过模糊匹配搜索
			input("xpath", "//input[@id='combobox-input-usedepartid']", "自动化测试部")
			sleep(1)
			# 模拟回车
			double_click("xpath", "//div[contains(text(),'自动化测试部')]")
			sleep(1)

			input("xpath", "//input[@id='receiever']", "田遍地")
			sleep(1)

			click("xpath", "//input[@id='combobox-input-chequepurposeid']")
			# 输入支票用途名称，通过模糊匹配搜索
			input("xpath", "//input[@id='combobox-input-chequepurposeid']", "自动化测试支票用途")
			sleep(1)
			# 模拟回车
			double_click("xpath", "//div[contains(text(),'自动化测试支票用途')]")
			sleep(1)

			# 金额中填入值
			clear("xpath", "//input[@id='useamount-input']")
			input("xpath", "//input[@id='useamount-input']", "800")
			sleep(1)

			# 备注框中填入值
			input("xpath", "//textarea[@id='description']", "自动化测试应付支票领用备注框修改")
			sleep(1)

			# 点击领用按钮
			click("xpath", "//span[text()='领用']")

			print("应付支票领用成功！")
			sleep(3)

			# 第二次领用后点击返回按钮，在应付支票领用页面完成审核
			click("xpath", "//span[text()='返回']")
			print("应付支票返回成功！")
			sleep(3)
			switch_default()
			switch_to("xpath", "//iframe[@id='chequeRecipients-tab-iframe']")

			# 点击查看
			# 用JS的方法点击放大镜
			js_click("xpath", "//span[@class='f-contrac-close']")
			sleep(1)
			click("xpath", "//input[@id='chequecode']")
			sleep(1)
			input("xpath", "//input[@id='chequecode']", "1222")
			sleep(1)

			# 点击查询
			click("xpath", "//span[text()='查询']")
			# 勾选
			click("xpath", "//div[@title='支票号:1222']/parent::*/preceding-sibling::*[5]/descendant::*[2]")

			click("xpath", "//span[text()='领用审核']")

			# 点击弹出框的OK键
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
			sleep(1)
			print("应付支票领用审核成功！！")
			sleep(3)

			# 点击打印
			# 勾选
			click("xpath", "//div[@title='支票号:1222']/parent::*/preceding-sibling::*[5]/descendant::*[2]")

			# 用JS的方法点击打印
			js_click("xpath", "//span[text()='打印']")

			# 切入打印页面的iframe窗体
			switch_to("xpath", "//iframe[@id='printWin-iframe']")
			sleep(1)

			# 用隐式等待方法等页面出现预期数据：自动化测试支票用途
			implici_wait("xpath", "//td[contains(text(),'自动化测试支票用途')]")
			print("应付支票领用打印成功！")
			time.sleep(3)

			# 退出所有iframe窗体
			switch_default()

			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='应付支票领用']/child::*[1]")

			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//span[@title='支票管理']")

			# 打印操作成功日志
			print("应付支票领用，操作成功!")
			logging.info("应付支票领用，操作成功!")
			time.sleep(2)
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("应付支票领用,失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)

		# 测试应付支票作废
		try:
			# 点击支票管理菜单
			click("xpath", "//span[@title='支票管理']")
			# 点击应付支票作废菜单
			click("xpath", "//span[@title='应付支票作废']")
			# 退出所有的iframe窗体
			switch_default()

			logging.info("开始测试应付支票作废功能")
			# 切入‘应付支票作废’的iframe窗体
			switch_to("xpath", "//iframe[@id='chequeInvalid-tab-iframe']")

			# 通过一组数据实现页面功能的测试
			# 点击查看
			# 用JS的方法点击放大镜
			js_click("xpath", "//span[@class='f-contrac-close']")
			sleep(1)

			# 输入支票号，通过模糊匹配搜索
			click("xpath", "//input[@id='chequecode']")
			sleep(1)
			input("xpath", "//input[@id='chequecode']", "1222")
			sleep(1)

			# 点击查询
			click("xpath", "//span[text()='查询']")

			# 勾选
			click("xpath", "//div[@title='支票号:1222']/parent::*/preceding-sibling::*[5]/descendant::*[2]")

			# 用JS的方法点击支票领用按钮
			js_click("xpath", "//span[text()='支票作废']")

			# 切入支票领用的iframe窗体
			switch_to("xpath", "//iframe[@id='applyWin-iframe']")
			sleep(1)

			click("xpath", "//input[@id='combobox-input-chequecancelreasonid']")
			# 输入作废原因，通过模糊匹配搜索
			input("xpath", "//input[@id='combobox-input-chequecancelreasonid']", "自动化测试支票作废原因")
			sleep(1)
			# 模拟回车
			double_click("xpath", "//div[contains(text(),'自动化测试支票作废原因')]")
			sleep(1)

			# 输入作废描述
			input("xpath", "//input[@id='canceldescript']", "自动化测试作废描述")
			sleep(1)

			click("xpath", "//span[text()='保存']")

			# 用隐式等待方法等页面出现新增成功的提示框
			# implici_wait("xpath", "//span[contains(text(),'操作成功')]")
			print("应付支票作废成功！")
			time.sleep(3)
			switch_default()
			# 切入应付支票领用窗体
			switch_to("xpath", "//iframe[@id='chequeInvalid-tab-iframe']")

			# 用JS的方法点击支票领用按钮
			js_click("xpath", "//span[text()='高级查询']")
			click("xpath", "//input[@id='combobox-input-property_0']")
			sleep(1)
			clear("xpath", "//input[@id='combobox-input-property_0']")
			sleep(1)
			# 输入作废状态，通过模糊匹配搜索
			input("xpath", "//input[@id='combobox-input-property_0']", "作废状态")
			sleep(1)
			# 模拟回车
			double_click("xpath", "//div[contains(text(),'作废状态')]")
			sleep(1)

			click("xpath", "//input[@id='combobox-input-condition_0']")
			sleep(1)
			# 输入作废状态，通过模糊匹配搜索
			input("xpath", "//input[@id='combobox-input-condition_0']", "等于")
			sleep(1)
			# 模拟回车
			double_click("xpath", "//div[contains(text(),'等于')]")
			sleep(1)

			click("xpath", "//input[@id='combobox-input-value_0']")
			sleep(1)
			# 输入作废状态，通过模糊匹配搜索
			input("xpath", "//input[@id='combobox-input-value_0']", "已作废")
			sleep(1)
			# 模拟回车
			double_click("xpath", "//div[contains(text(),'已作废')]")
			sleep(1)

			click("xpath", "//div[contains(text(),'查询')]")

			js_click("xpath", "//span[text()='自定义查询']/preceding-sibling::*[1]")

			# 勾选
			click("xpath", "//div[@title='支票号:1222']/parent::*/preceding-sibling::*[5]/descendant::*[2]")
			sleep(1)

			click("xpath", "//span[text()='作废取消']")
			# 点击弹出框的OK键
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
			sleep(1)
			print("作废取消成功！！")
			sleep(3)
			# 退出所有iframe窗体
			switch_default()

			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='应付支票作废']/child::*[1]")

			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//span[@title='支票管理']")

			# 打印操作成功日志
			print("应付支票作废，操作成功!")
			logging.info("应付支票作废，操作成功!")
			time.sleep(2)
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("应付支票作废,失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)

		# 测试应付支票查看
		try:
			# 点击支票管理菜单
			click("xpath", "//span[@title='支票管理']")
			# 点击应付支票作废菜单
			click("xpath", "//span[@title='应付支票查看']")
			# 退出所有的iframe窗体
			switch_default()

			logging.info("开始测试应付支票查看功能")
			# 切入‘应付支票作废’的iframe窗体
			switch_to("xpath", "//iframe[@id='chequeView-tab-iframe']")

			# 点击查看
			# 用JS的方法点击放大镜
			js_click("xpath", "//span[@class='f-contrac-close']")
			sleep(1)

			# 选择银行
			click("xpath", "//input[@id='combobox-input-bankid']")
			sleep(1)
			input("xpath", "//input[@id='combobox-input-bankid']", "HXB-华夏银行")
			sleep(1)
			click("xpath", "//div[@title='代码-名称:HXB-华夏银行']")
			sleep(1)

			# 点击查询
			click("xpath", "//span[text()='查询']")

			# 用隐式等待方法等页面出现预期数据：复核人:mindy
			implici_wait("xpath", "//div[@title='复核人:mindy']")
			print("应付支票查看成功！")
			time.sleep(3)

			# 退出所有iframe窗体
			switch_default()

			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='应付支票查看']/child::*[1]")

			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//span[@title='支票管理']")

			# 打印操作成功日志
			print("应付支票查看，操作成功!")
			logging.info("应付支票查看，操作成功!")
			time.sleep(2)
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("应付支票查看,失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		# 应付支票查看结束后返回删除应付支票登记里面的数据
		# 测试支票管理--应付支票登记删除功能
		try:
			# 点击支票管理菜单
			click("xpath", "//span[@title='支票管理']")
			# 点击应付支票登记菜单
			click("xpath", "//span[@title='应付支票登记']")
			# 退出所有的iframe窗体
			switch_default()

			logging.info("开始测试应付支票登记数据删除功能")

			# 删除功能
			# 切入应付支票登记iframe窗体
			switch_to("xpath", "//iframe[@id='chequeStorage-tab-iframe']")

			# 点击查看
			# 用JS的方法点击放大镜
			js_click("xpath", "//span[@class='f-contrac-close']")
			sleep(1)

			# 输入银行，通过模糊匹配搜索
			click("xpath", "//input[@id='combobox-input-accountid']")
			sleep(1)
			input("xpath", "//input[@id='combobox-input-accountid']", "CNY")
			sleep(1)
			click("xpath", "//div[contains(text(),'CNY')]")
			time.sleep(1)

			# 输入银行，通过模糊匹配搜索
			click("xpath", "//input[@id='combobox-input-booktype']")
			sleep(1)
			input("xpath", "//input[@id='combobox-input-booktype']", "转账")
			sleep(1)
			click("xpath", "//div[@title='转账']")
			sleep(1)

			# 点击查询
			click("xpath", "//span[text()='查询']")

			# 勾选
			click("xpath", "//div[@title='银行:HXB-华夏银行']/parent::*/preceding-sibling::*[1]/descendant::*[2]")

			# 点击删除按钮
			click("xpath", "//span[text()='删除']")

			# 点击弹出框的OK键
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
			sleep(1)

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("应付支票登记，删除成功！")
			time.sleep(3)

			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='应付支票登记']/child::*[1]")

			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//span[@title='支票管理']")

			# 打印操作成功日志
			print("应付支票登记，数据删除操作成功!")
			logging.info("应付支票登记，数据删除操作成功!")
			time.sleep(2)

		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("应付支票登记数据删除打印失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)

		# 应付支票登记删除后删除支票用途
		# 测试基础设置--删除支票用途数据
		try:
			# 点击基础设置菜单
			click("xpath", "//li[@f_value='billSetting']/descendant-or-self::*[5]")
			# 点击支票用途菜单
			click("xpath", "//li[@f_value='chequePurpose']/descendant-or-self::*[5]")
			# 退出所有iframe窗体
			switch_default()

			# 切入支票用途的iframe窗体
			switch_to("xpath", "//iframe[@id='chequePurpose-tab-iframe']")
			logging.info("开始测试支票用途数据删除功能")

			# 点击查看
			# 用JS的方法点击放大镜
			js_click("xpath", "//span[@class='f-contrac-close']")
			sleep(1)

			# 输入代码：
			input("xpath", "//input[@id='code']", "TestReg")
			sleep(1)

			# 点击查询
			click("xpath", "//span[text()='查询']")

			# 勾选
			click("xpath", "//div[@title='用途代码:TestReg']/parent::*/preceding-sibling::*[1]/descendant::*[2]")

			# 点击删除按钮
			click("xpath", "//span[text()='删除']")

			# 点击弹出框的OK键
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功')]")
			print("支票用途，删除成功！")
			time.sleep(3)

			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='支票用途']/child::*[1]")

			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//li[@f_value='billSetting']/descendant-or-self::*[5]")

			# 打印操作成功日志
			print("支票用途，删除操作成功!")
			logging.info("支票用途，删除操作成功!")
			time.sleep(2)

		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("支票用途删除打印失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)

		# 测试基础设置--支票作废原因数据删除
		try:
			# 点击基础设置菜单
			click("xpath", "//li[@f_value='billSetting']/descendant-or-self::*[5]")
			# 点击支票作废原因菜单
			click("xpath", "//li[@f_value='chequeInvalidReason']/descendant-or-self::*[5]")
			# 退出所有iframe窗体
			switch_default()

			# 切入支票作废原因的iframe窗体
			switch_to("xpath", "//iframe[@id='chequeInvalidReason-tab-iframe']")
			logging.info("开始测试支票作废原因数据删除功能")

			# 点击查看
			# 用JS的方法点击放大镜
			js_click("xpath", "//span[@class='f-contrac-close']")
			sleep(1)

			# 输入代码：
			input("xpath", "//input[@id='code']", "TestReg")
			sleep(1)

			# 点击查询
			click("xpath", "//span[text()='查询']")

			# 勾选
			click("xpath", "//div[@title='作废代码:TestReg']/parent::*/preceding-sibling::*[1]/descendant::*[2]")

			# 点击删除按钮
			click("xpath", "//span[text()='删除']")

			# 点击弹出框的OK键
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功')]")
			print("支票作废原因，删除成功！")
			time.sleep(3)

			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='支票作废原因']/child::*[1]")

			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//li[@f_value='billSetting']/descendant-or-self::*[5]")

			# 打印操作成功日志
			print("支票作废原因，数据删除操作成功!")
			logging.info("支票作废原因，数据删除操作成功!")
			time.sleep(2)

		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("支票作废原因数据删除打印失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)

		# 测试应收支票管理
		try:

			# 点击支票管理菜单
			click("xpath", "//span[@title='支票管理']")
			# 点击应付支票登记菜单
			click("xpath", "//span[@title='应收支票管理']")
			# 退出所有的iframe窗体
			switch_default()

			logging.info("开始测试应收支票管理功能")
			for i in range(1, 4):
				# 切入‘应收支票管理’的iframe窗体
				switch_to("xpath", "//iframe[@id='collectChequeManage-tab-iframe']")

				# 用JS的方法点击新增按钮
				js_click("xpath", "//span[text()='新增']")

				# 设置时间的变成存储
				temp = time.strftime("%Y%m%d%H%M%S")

				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='addWin-iframe']")
				sleep(1)

				# 输入部门
				click("xpath", "//input[@id='combobox-input-deptid']")
				sleep(1)
				input("xpath", "//input[@id='combobox-input-deptid']", "自动化测试部")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-deptid']")
				input_enter("xpath", "//input[@id='combobox-input-deptid']")
				sleep(1)

				# 输入支票号
				input("xpath", "//input[@id='chequecode']", str(temp) + "ZPH")
				sleep(1)

				# 输入票面金额
				click("xpath", "//input[@id='amount-input']")
				sleep(1)
				# 清空内容
				clear("xpath", "//input[@id='amount-input']")
				sleep(1)
				# 输入金额
				input("xpath", "//input[@id='amount-input']", "100000")
				sleep(1)

				# 输入到期日期
				today = date.today()
				due_date = today + timedelta(days=60)
				click("xpath", "//input[@id='expiredate-input']")
				sleep(1)
				clear("xpath", "//input[@id='expiredate-input']")
				sleep(1)
				input("xpath", "//input[@id='expiredate-input']", str(due_date))
				# 模拟回车键
				keyDown('enter')
				keyUp('enter')
				time.sleep(1)

				# 选择签发银行，第一次选择BOC-中国银行’，后面选择ICBC-工商银行
				if i == 1:
					click("xpath", "//input[@id='combobox-input-issuebankid']")
					sleep(1)
					input("xpath", "//input[@id='combobox-input-issuebankid']", "BOC-中国银行")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-issuebankid']")
					input_enter("xpath", "//input[@id='combobox-input-issuebankid']")
					sleep(1)
				else:
					click("xpath", "//input[@id='combobox-input-issuebankid']")
					sleep(1)
					input("xpath", "//input[@id='combobox-input-issuebankid']", "ICBC-工商银行")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-issuebankid']")
					input_enter("xpath", "//input[@id='combobox-input-issuebankid']")
					sleep(1)

				# 输入付款单位
				click("xpath", "//input[@id='combobox-input-oppcounterpartyid']")
				sleep(1)
				input("xpath", "//input[@id='combobox-input-oppcounterpartyid']", "Mindy自动化测试")
				sleep(1)

				# 输入收票日期
				# today = date.today()
				receipt_date = today + timedelta(days=60)
				click("xpath", "//input[@id='recdate-input']")
				sleep(1)
				clear("xpath", "//input[@id='recdate-input']")
				sleep(1)
				input("xpath", "//input[@id='recdate-input']", str(receipt_date))
				# 模拟回车键
				keyDown('enter')
				keyUp('enter')
				time.sleep(1)

				# 输入收款通知单号
				temp1 = time.strftime("%Y%m%d%H%M%S")
				input("xpath", "//input[@id='receivablesno']", str(temp1))
				sleep(1)

				# 输入片区
				input("xpath", "//input[@id='area']", "自动化测试应收支票管理片区")
				sleep(1)

				# 输入业务员编码
				input("xpath", "//input[@id='salesmanno']", "Mindy")
				sleep(1)

				# 输入业务员名称
				input("xpath", "//input[@id='salesmanname']", "田遍地")
				sleep(1)

				# 备注框中输入新内容
				input("xpath", "//textarea[@id='memo']", "自动化测试应收支票管理备注测试")
				sleep(1)

				# 点击保存按钮
				click("xpath", "//span[text()='保存']")

				# 退出所有iframe窗体
				switch_default()

				# 用隐式等待方法等页面出现提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				print("应收支票管理第%s次，保存成功！" % i)
				logging.info("应收支票管理第%s次，保存成功！" % i)
				time.sleep(3)

				# 第一笔，就先修改，再删除新建的‘应收支票管理’
				if i == 1:
					# 切入‘应收支票管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='collectChequeManage-tab-iframe']")

					# 点击查看
					# 用JS的方法点击放大镜
					js_click("xpath", "//span[@class='f-contrac-close']")
					sleep(1)

					# 输入支票号：ZPH
					input("xpath", "//input[@id='chequecode']", "ZPH")
					sleep(1)

					# 点击查询
					click("xpath", "//span[text()='查询']")

					# 修改
					# 勾选
					click("xpath", "//div[contains(text(),'ZPH')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 点击修改按钮
					click("xpath", "//span[text()='修改']")

					# 切入修改的iframe窗体
					switch_to("xpath", "//iframe[@id='modWin-iframe']")
					sleep(1)

					# 修改票面金额
					click("xpath", "//input[@id='amount-input']")
					sleep(1)
					# 清空内容
					clear("xpath", "//input[@id='amount-input']")
					sleep(1)
					# 输入金额
					input("xpath", "//input[@id='amount-input']", "500000")
					sleep(1)

					# 备注框中输入新内容
					input("xpath", "//textarea[@id='memo']", "修改备注内容")
					sleep(1)

					# 点击保存按钮
					click("xpath", "//span[text()='保存']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("应收支票管理，修改成功！")
					logging.info("应收支票管理，修改成功！")
					time.sleep(3)

					# 切入‘应收支票管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='collectChequeManage-tab-iframe']")

					# 删除
					# 勾选
					click("xpath", "//div[contains(text(),'ZPH')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 点击删除按钮
					click("xpath", "//span[text()='删除']")

					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现删除的提示框
					implici_wait("xpath", "//span[contains(text(),'成功删除1条记录！')]")
					print("应收支票管理，删除成功！")
					logging.info("应收支票管理，删除成功！")
					time.sleep(3)

				# 第二笔，先审核、再取消审核、再托收、再托收到账
				elif i == 2:

					# 第一次审核
					# 切入‘应收支票管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='collectChequeManage-tab-iframe']")

					# 勾选
					click("xpath", "//div[contains(text(),'ZPH')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 点击审核按钮
					click("xpath", "//span[text()='审核']")

					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'成功审核1条!')]")
					print("应收支票管理，第一次审核成功！")
					logging.info("应收支票管理，第一次审核成功！")
					time.sleep(3)

					# 取消审核
					# 切入‘应收支票管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='collectChequeManage-tab-iframe']")

					# 勾选
					click("xpath", "//div[contains(text(),'ZPH')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 用JS方便点击‘审核’按钮旁边的倒三角形
					js_click("xpath", "//span[text()='审核']/parent::*/following-sibling::*/child::*")
					sleep(1)

					# 点击取消审核按钮
					js_click("xpath", "//a[contains(text(),'取消审核')]")
					sleep(1)

					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'成功取消审核1条！')]")
					print("应收支票管理，取消审核成功！")
					logging.info("应收支票管理，取消审核成功！")
					time.sleep(3)

					# 第二次审核
					# 切入‘应收支票管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='collectChequeManage-tab-iframe']")

					# 勾选
					click("xpath", "//div[contains(text(),'ZPH')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 点击审核按钮
					click("xpath", "//span[text()='审核']")

					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'成功审核1条!')]")
					print("应收支票管理，第二次审核成功！")
					logging.info("应收支票管理，第二次审核成功！")
					time.sleep(3)

					# 托收
					# 切入‘应收支票管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='collectChequeManage-tab-iframe']")

					# 勾选
					click("xpath", "//div[contains(text(),'ZPH')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 点击托收按钮
					click("xpath", "//span[text()='托收']")

					# 点击托收日期
					click("xpath", "//input[@id='collectiondate-input']")
					sleep(1)
					clear("xpath", "//input[@id='collectiondate-input']")
					sleep(1)
					# 输入托收日期
					collection_date = today + timedelta(days=60)
					input("xpath", "//input[@id='collectiondate-input']", str(collection_date))
					# # 模拟回车键
					# keyDown('enter')
					# keyUp('enter')
					time.sleep(1)

					# 选择托收银行
					click("xpath", "//input[@id='combobox-input-collectionbankid']")
					sleep(1)
					input("xpath", "//input[@id='combobox-input-collectionbankid']", "ABC-农业银行")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-collectionbankid']")
					input_enter("xpath", "//input[@id='combobox-input-collectionbankid']")
					sleep(1)

					# 点击确定按钮
					click("xpath",
					      "//input[@id='collectiondate-input']/ancestor::*[10]/following-sibling::*[2]/descendant::*[3]")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'成功托收1条！')]")
					print("应收支票登记，托收成功！")
					logging.info("应收支票登记，托收成功！")
					sleep(3)

					# 托收到账
					# 切入‘应收支票登记’的iframe窗体
					switch_to("xpath", "//iframe[@id='collectChequeManage-tab-iframe']")

					# 勾选
					click("xpath", "//div[contains(text(),'ZPH')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 点击托收到账按钮
					js_click("xpath", "//span[text()='托收到账']")

					# 切入‘托收到账’的iframe窗体
					switch_to("xpath", "//iframe[@id='impawneWin-iframe']")
					sleep(1)

					# 点击托收到账日期

					# 输入到期日期
					today = date.today()
					collection_date = today + timedelta(days=70)
					click("xpath", "//input[@id='arrivaldate-input']")
					sleep(1)
					clear("xpath", "//input[@id='arrivaldate-input']")
					sleep(1)
					input("xpath", "//input[@id='arrivaldate-input']", str(collection_date))
					# 模拟回车键
					keyDown('enter')
					keyUp('enter')
					time.sleep(2)

					# 点击让日期下拉框消失
					double_click("xpath", "//span[text()='托收到账日期']")
					sleep(1)

					# 点击确定按钮
					click("xpath",
					      "//input[@id='arrivaldate-input']/ancestor::*[10]/following-sibling::*[2]/descendant::*[3]")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'成功到账1条！')]")
					print("应收支票管理，托收到账成功！")
					logging.info("应收支票管理，托收到账成功！")
					time.sleep(3)

				# 第三笔，审核
				elif i == 3:
					# 切入‘应收支票登记’的iframe窗体
					switch_to("xpath", "//iframe[@id='collectChequeManage-tab-iframe']")

					# 勾选
					click("xpath", "//div[contains(text(),'ZPH')]/parent::*/preceding-sibling::*[1]//descendant::*[2]")

					# 点击审核按钮
					click("xpath", "//span[text()='审核']")

					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'成功审核1条!')]")
					print("应收支票管理，第三次审核成功！")
					logging.info("应收支票管理，第三次审核成功！")
					time.sleep(3)

			# 退出所有iframe窗体
			switch_default()

			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='应收支票管理']/child::*[1]")

			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//span[@title='支票管理']")

			# 打印操作成功日志
			print("应收支票管理，操作成功!")
			logging.info("应收支票管理，操作成功!")
			time.sleep(2)
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("应收支票管理,失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)

		# 测试应收支票查看
		try:
			# 点击支票管理菜单
			click("xpath", "//span[@title='支票管理']")
			# 点击应付支票作废菜单
			click("xpath", "//span[@title='应收支票查看']")
			# 退出所有的iframe窗体
			switch_default()

			logging.info("开始测试应收支票查看功能")
			# 切入‘应收支票查看’的iframe窗体
			switch_to("xpath", "//iframe[@id='chequeManageView-tab-iframe']")

			# 点击查看
			# 用JS的方法点击放大镜
			js_click("xpath", "//span[@class='f-contrac-close']")
			sleep(1)

			click("xpath", "//input[@id='chequecode']")

			# 输入内容
			input("xpath", "//input[@id='chequecode']", "ZPH")
			sleep(1)

			# 点击查询
			click("xpath", "//span[text()='查询']")

			# 用隐式等待方法等页面出现预期数据：片区:自动化测试应收支票管理片区
			implici_wait("xpath", "//div[@title='片区:自动化测试应收支票管理片区']")
			print("应收支票查看成功！")
			time.sleep(3)

			# 退出所有iframe窗体
			switch_default()

			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='应收支票查看']/child::*[1]")

			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//span[@title='支票管理']")

			# 打印操作成功日志
			print("应收支票查看，操作成功!")
			logging.info("应收支票查看，操作成功!")
			time.sleep(2)
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("应付支票作废,失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)

		# 测试承兑票据管理-应收票据管理
		try:
			# 点击承兑票据管理菜单
			click("xpath", "//span[@title='承兑汇票管理']")
			# 点击应收支票登记菜单
			click("xpath", "//span[@title='应收票据管理']")
			# 退出所有的iframe窗体
			switch_default()
			logging.info("开始测试应收票据管理功能")
			for i in range(1, 7):
				# 切入‘应收票据管理’的iframe窗体
				switch_to("xpath", "//iframe[@id='recDraftManage-tab-iframe']")
				# 用JS的方法点击新增按钮
				js_click("xpath", "//span[text()='新增']")
				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='addWin-iframe']")
				sleep(1)

				# 选择工程项目
				# 点击‘工程项目’框
				click("xpath", "//input[@id='combobox-input-projectitemid']")
				# 输入自动化测试工程项目，模糊查询
				input("xpath", "//input[@id='combobox-input-projectitemid']", "自动化测试工程项目")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-projectitemid']")
				input_enter("xpath", "//input[@id='combobox-input-projectitemid']")
				time.sleep(1)

				# 选择部门
				# 点击‘部门’框
				click("xpath", "//input[@id='combobox-input-deptid']")
				# 输入自动化测试工程项目，模糊查询
				input("xpath", "//input[@id='combobox-input-deptid']", "自动化测试部")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-deptid']")
				input_enter("xpath", "//input[@id='combobox-input-deptid']")
				time.sleep(1)

				# 选择票据类型
				# 第一次选择109-银行承兑汇票，第二次选择205-商业承兑汇票
				# 点击‘票据类型’框
				if i == 1:
					click("xpath", "//input[@id='combobox-input-drafttype']")
					input("xpath", "//input[@id='combobox-input-drafttype']", "109")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-drafttype']")
					input_enter("xpath", "//input[@id='combobox-input-drafttype']")
					time.sleep(1)
				else:
					click("xpath", "//input[@id='combobox-input-drafttype']")
					input("xpath", "//input[@id='combobox-input-drafttype']", "商业承兑汇票")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-drafttype']")
					input_enter("xpath", "//input[@id='combobox-input-drafttype']")
					time.sleep(1)

				# 设置时间的变成存储，变成
				temp1 = time.strftime("%H%M%S")
				# 输入票据号
				click("xpath", "//span[text()='票据号']/ancestor::*[2]/descendant::*[6]/descendant::*[1]")
				sleep(1)
				input("xpath", "//span[text()='票据号']/ancestor::*[2]/descendant::*[6]/descendant::*[1]",
				      "PJH" + str(temp1))
				sleep(1)

				# 输入到期期限
				click("xpath", "//input[@id='terms-input']")
				sleep(1)
				clear("xpath", "//input[@id='terms-input']")
				sleep(1)
				input("xpath", "//input[@id='terms-input']", "60")
				sleep(1)

				if i == 2:
					# 点击‘币种’框
					click("xpath", "//input[@id='combobox-input-currencyid']")
					clear("xpath", "//input[@id='combobox-input-currencyid']")
					# 输入币种，模糊查询
					input("xpath", "//input[@id='combobox-input-currencyid']", "NOK-挪威克朗")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-currencyid']")
					input_enter("xpath", "//input[@id='combobox-input-currencyid']")
					time.sleep(1)

				# 输入票面金额
				click("xpath", "//input[@id='draftamount-input']")
				sleep(1)
				clear("xpath", "//input[@id='draftamount-input']")
				sleep(1)
				input("xpath", "//input[@id='draftamount-input']", "1000000")
				sleep(1)

				# 当第二次的时候给票单位类型选择内部组织
				if i == 2:
					click("xpath", "//input[@id='combobox-input-endorsetype']")
					# 输入内部组织，模糊查询
					input("xpath", "//input[@id='combobox-input-endorsetype']", "内部组织")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-endorsetype']")
					input_enter("xpath", "//input[@id='combobox-input-endorsetype']")
					time.sleep(1)

				# 输入外部给票单位
				click("xpath", "//input[@id='combobox-input-endorsecounterpartyid']")
				# 输入自动化测试，模糊查询
				input("xpath", "//input[@id='combobox-input-endorsecounterpartyid']", "Mindy自动化测试")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-endorsecounterpartyid']")
				input_enter("xpath", "//input[@id='combobox-input-endorsecounterpartyid']")
				time.sleep(1)

				# 输入出票单位
				input("xpath", "//input[@id='deptcode']", "1000000")
				sleep(1)

				# 输入承兑银行
				if i == 1:
					# 输入承兑银行，
					click("xpath", "//input[@id='combobox-input-paybankid']")
					# 输入中国银行，模糊查询
					input("xpath", "//input[@id='combobox-input-paybankid']", "BOC-中国银行")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-paybankid']")
					input_enter("xpath", "//input[@id='combobox-input-paybankid']")
					time.sleep(1)

					# 输入承兑开户银行，
					click("xpath", "//input[@id='combobox-input-paybanklocationid']")
					# 输入后模糊查询
					input("xpath", "//input[@id='combobox-input-paybanklocationid']", "中国银行股份有限公司大连泡崖街支行")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-paybanklocationid']")
					input_enter("xpath", "//input[@id='combobox-input-paybanklocationid']")
					time.sleep(1)

					# 输入收款方
					input("xpath", "//input[@id='recname']", "Mindy科技有限公司")
					sleep(1)

					# 收票银行账号
					click("xpath", "//input[@id='combobox-input-recaccountid']")
					# 输入中国银行，模糊查询
					input("xpath", "//input[@id='combobox-input-recaccountid']", "中国银行")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-recaccountid']")
					input_enter("xpath", "//input[@id='combobox-input-recaccountid']")
					time.sleep(1)

					# 输入承兑开户银行(名)
					input("xpath", "//input[@id='paybanklocations']", "自动化测试承兑开户银行")
					sleep(1)

				else:
					# 输入承兑方
					input("xpath", "//input[@id='acceptor']", "自动化测试承兑方")
					sleep(1)

					# 输入收款方
					input("xpath", "//input[@id='recname']", "Mindy自动化测试公司")
					sleep(1)

					click("xpath", "//input[@id='combobox-input-recaccountid']")
					# 输入收票银行，模糊查询
					input("xpath", "//input[@id='combobox-input-recaccountid']", "华夏银行")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-recaccountid']")
					input_enter("xpath", "//input[@id='combobox-input-recaccountid']")
					time.sleep(1)

				# 输入背书单位前手名称
				input("xpath", "//input[@id='fronthandendorsers']", "自动化测试背书单位前手名称")
				sleep(1)

				# 输入备注
				input("xpath", "//textarea[@id='description']", "自动化测试应收票据管理")

				# 点击费用信息新增行，新增第一行
				click("xpath", "//span[@title='费用名称']/ancestor::*[6]/following-sibling::*[2]/descendant::*[7]")
				sleep(1)
				# 输入费用信息
				input("xpath", "//input[@id='editgrid-feesname-0']", "自动化测试评估费用")
				sleep(1)
				# 输入费用日期
				today = date.today()
				cost_date = today
				click("xpath", "//input[@id='editgrid-feesdate-0-input']")
				sleep(1)
				clear("xpath", "//input[@id='editgrid-feesdate-0-input']")
				sleep(1)
				input("xpath", "//input[@id='editgrid-feesdate-0-input']", str(cost_date))
				# 模拟回车键
				keyDown('enter')
				keyUp('enter')
				time.sleep(2)
				# 输入费用金额
				input("xpath", "//input[@id='editgrid-feesamount-0-input']", "30000")
				sleep(1)
				# 输入描述
				input("xpath", "//input[@id='editgrid-description-0']", "自动化测试描述")
				sleep(1)

				# 点击费用信息新增行，新增第二行
				click("xpath", "//span[@title='费用名称']/ancestor::*[6]/following-sibling::*[2]/descendant::*[7]")
				sleep(1)
				# 输入费用信息
				input("xpath", "//input[@id='editgrid-feesname-1']", "自动化测试运营费用")
				sleep(1)
				# 输入费用日期
				today = date.today() + timedelta(days=70)
				cost_date = today
				click("xpath", "//input[@id='editgrid-feesdate-1-input']")
				sleep(1)
				clear("xpath", "//input[@id='editgrid-feesdate-1-input']")
				sleep(1)
				input("xpath", "//input[@id='editgrid-feesdate-1-input']", str(cost_date))
				# 模拟回车键
				keyDown('enter')
				keyUp('enter')
				time.sleep(2)
				# 输入费用金额
				input("xpath", "//input[@id='editgrid-feesamount-1-input']", "10000")
				sleep(1)
				# 输入描述
				input("xpath", "//input[@id='editgrid-description-1']", "自动化测试描述")
				sleep(1)

				# 缺少附件上传功能

				# 点击保存按钮
				click("xpath", "//span[text()='保存']")

				# 退出所有iframe窗体
				switch_default()

				# 用隐式等待方法等页面出现提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				print("应收票据管理第%s次，保存成功！" % i)
				logging.info("应收票据管理第%s次，保存成功！" % i)
				time.sleep(3)

				# 第一笔，就先修改，再删除新建的‘应收票据管理’
				if i == 1:
					# 切入‘应收票据管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='recDraftManage-tab-iframe']")

					# 点击查看
					# 用JS的方法点击放大镜
					js_click("xpath", "//span[@class='f-contrac-close']")
					sleep(1)

					# 输入支票号：ZPH
					input("xpath", "//input[@id='draftcode']", "PJH")
					sleep(1)

					# 点击查询
					click("xpath", "//span[text()='查询']")

					# 修改
					# 勾选
					click("xpath", "//div[contains(text(),'PJH')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 点击修改按钮
					click("xpath", "//span[text()='修改']")

					# 切入修改的iframe窗体
					switch_to("xpath", "//iframe[@id='editRecDraftWin-iframe']")
					sleep(1)

					# 修改票面金额
					click("xpath", "//input[@id='draftamount-input']")
					sleep(1)
					# 清空内容
					clear("xpath", "//input[@id='draftamount-input']")
					sleep(1)
					# 输入金额
					input("xpath", "//input[@id='draftamount-input']", "500000")
					sleep(1)

					# 备注框中输入新内容
					input("xpath", "//textarea[@id='description']", "修改备注内容")
					sleep(1)

					# 点击费用信息第一行删除行
					click("xpath", "//input[@id='editgrid-syscheck-0']")
					sleep(1)
					click("xpath", "//span[@title='费用名称']/ancestor::*[6]/following-sibling::*[2]/descendant::*[9]")
					sleep(1)

					# 点击费用信息第二行删除行
					click("xpath", "//input[@id='editgrid-syscheck-1']")
					sleep(1)
					click("xpath", "//span[@title='费用名称']/ancestor::*[6]/following-sibling::*[2]/descendant::*[9]")
					sleep(1)

					# 点击费用信息新增行，新增第一行
					click("xpath", "//span[@title='费用名称']/ancestor::*[6]/following-sibling::*[2]/descendant::*[7]")
					sleep(1)
					# 输入费用信息
					input("xpath", "//input[@id='editgrid-feesname-2']", "自动化测试修改评估费用")
					sleep(1)
					# 输入费用日期
					today = date.today()
					cost_date = today
					click("xpath", "//input[@id='editgrid-feesdate-2-input']")
					sleep(1)
					clear("xpath", "//input[@id='editgrid-feesdate-2-input']")
					sleep(1)
					input("xpath", "//input[@id='editgrid-feesdate-2-input']", str(cost_date))
					# 模拟回车键
					keyDown('enter')
					keyUp('enter')
					time.sleep(2)
					# 输入费用金额
					input("xpath", "//input[@id='editgrid-feesamount-2-input']", "40000")
					sleep(1)
					# 输入描述
					input("xpath", "//input[@id='editgrid-description-2']", "自动化测试修改描述")
					sleep(1)

					# 点击保存按钮
					click("xpath", "//span[text()='保存']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("应收票据管理，修改成功！")
					logging.info("应收票据管理，修改成功！")
					time.sleep(3)

					# 切入‘应收票据管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='recDraftManage-tab-iframe']")

					# 删除
					# 勾选
					click("xpath", "//div[contains(text(),'PJH')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 点击删除按钮
					click("xpath", "//span[text()='删除']")

					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现删除的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("应收票据管理，删除成功！")
					logging.info("应收票据管理，删除成功！")
					time.sleep(3)

				# 第二笔，先审核、再取消审核、再托收、再托收到账
				elif i == 2:

					# 第一次审核
					# 切入‘应收票据管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='recDraftManage-tab-iframe']")

					# 勾选
					click("xpath", "//div[contains(text(),'PJH')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 点击审核按钮
					click("xpath", "//span[text()='审核']")

					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("应收票据管理，第一次审核成功！")
					logging.info("应收票据管理，第一次审核成功！")
					time.sleep(3)

					# 取消审核
					# 切入‘应收票据管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='recDraftManage-tab-iframe']")

					# 勾选
					click("xpath", "//div[contains(text(),'PJH')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 用JS方便点击‘审核’按钮旁边的倒三角形
					js_click("xpath", "//span[text()='审核']/parent::*/following-sibling::*/child::*")
					sleep(1)

					# 点击取消审核按钮
					js_click("xpath", "//a[contains(text(),'取消审核')]")
					sleep(1)

					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("应收票据管理，取消审核成功！")
					logging.info("应收票据管理，取消审核成功！")
					time.sleep(3)

					# 第二次审核
					# 切入‘应收支票管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='recDraftManage-tab-iframe']")

					# 勾选
					click("xpath", "//div[contains(text(),'PJH')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 点击审核按钮
					click("xpath", "//span[text()='审核']")

					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("应收票据管理，第二次审核成功！")
					logging.info("应收票据管理，第二次审核成功！")
					time.sleep(3)

					# 票据背书
					# 切入‘应收支票管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='recDraftManage-tab-iframe']")

					# 勾选
					click("xpath", "//div[contains(text(),'PJH')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 用JS方便点击‘票据操作’按钮旁边的倒三角形
					js_click("xpath", "//span[text()='票据操作']/parent::*/following-sibling::*/child::*")
					sleep(1)

					# 点击票据背书按钮
					js_click("xpath", "//a[contains(text(),'票据背书')]")
					sleep(1)

					# 切入票据背书的窗体页面endorseWin-iframe
					switch_to("xpath", "//iframe[@id='endorseWin-iframe']")

					click("xpath", "//input[@id='combobox-input-endorsetype']")
					# 输入被背书对象类型，模糊查询
					input("xpath", "//input[@id='combobox-input-endorsetype']", "内部组织")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-endorsetype']")
					input_enter("xpath", "//input[@id='combobox-input-endorsetype']")
					time.sleep(1)

					click("xpath", "//input[@id='combobox-input-endorseorgid']")
					# 输入被背书对象类型，模糊查询
					input("xpath", "//input[@id='combobox-input-endorseorgid']", "Mindy科技有限公司")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-endorseorgid']")
					input_enter("xpath", "//input[@id='combobox-input-endorseorgid']")
					time.sleep(1)

					# 输入备注
					input("xpath", "//span[@title='背书金额']/ancestor::*[3]/following-sibling::*[3]/descendant::*[5]",
					      "自动化测试票据背书备注")

					# 点击确定按钮
					click("xpath", "//span[@title='被背书对象类型']/ancestor::*[10]/preceding-sibling::*[1]/descendant::*[3]")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("应收票据管理，票据背书成功！")
					logging.info("应收票据管理，票据背书成功！")
					sleep(3)

					# 取消背书
					# 切入‘应收支票管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='recDraftManage-tab-iframe']")

					# 勾选
					click("xpath", "//div[contains(text(),'PJH')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 用JS方便点击‘票据操作’按钮旁边的倒三角形
					js_click("xpath", "//span[text()='票据操作']/parent::*/following-sibling::*/child::*")
					sleep(1)

					# 点击取消票据背书按钮
					js_click("xpath", "//a[contains(text(),'取消背书')]")
					sleep(1)

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("应收票据管理，取消背书成功！")
					logging.info("应收票据管理，取消背书成功！")
					sleep(3)

					# 票据贴现
					# 切入‘应收票据管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='recDraftManage-tab-iframe']")

					# 勾选
					click("xpath", "//div[contains(text(),'PJH')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 用JS方便点击‘票据操作’按钮旁边的倒三角形
					js_click("xpath", "//span[text()='票据操作']/parent::*/following-sibling::*/child::*")
					sleep(1)

					# 点击票据贴现按钮
					js_click("xpath", "//a[contains(text(),'票据贴现')]")
					sleep(1)

					# 切入票据贴现的窗体页面endorseWin-iframe
					switch_to("xpath", "//iframe[@id='discountWin-iframe']")

					click("xpath", "//span[text()='贴现收款账户']/parent::*/following-sibling::*/descendant::*[3]")
					# 输入被背书对象类型，模糊查询
					input("xpath", "//span[text()='贴现收款账户']/parent::*/following-sibling::*/descendant::*[3]", "华夏银行")
					sleep(1)
					input_down("xpath", "//span[text()='贴现收款账户']/parent::*/following-sibling::*/descendant::*[3]")
					input_enter("xpath", "//span[text()='贴现收款账户']/parent::*/following-sibling::*/descendant::*[3]")
					time.sleep(1)

					# 输入备注
					input("xpath", "//span[@title='贴现日期']/ancestor::*[3]/following-sibling::*[1]/descendant::*[5]",
					      "自动化测试票据贴现备注")

					# 输入贴现利率
					input("xpath", "//input[@id='editgrid-discountrate-0-input']", "4")

					# 点击贴现按钮
					click("xpath", "//span[@title='贴现收款账户']/ancestor::*[10]/preceding-sibling::*[1]/descendant::*[3]")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("应收票据管理，票据贴现成功！")
					logging.info("应收票据管理，票据贴现成功！")
					sleep(3)

					# 取消贴现
					# 切入‘应收票据管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='recDraftManage-tab-iframe']")

					# 勾选
					click("xpath", "//div[contains(text(),'PJH')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 用JS方便点击‘票据操作’按钮旁边的倒三角形
					js_click("xpath", "//span[text()='票据操作']/parent::*/following-sibling::*/child::*")
					sleep(1)

					# 点击取消票据背书按钮
					js_click("xpath", "//a[contains(text(),'取消贴现')]")
					sleep(1)

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("应收票据管理，取消贴现成功！")
					logging.info("应收票据管理，取消贴现成功！")
					sleep(3)

					# 票据托收
					# 切入‘应收票据管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='recDraftManage-tab-iframe']")

					# 勾选
					click("xpath", "//div[contains(text(),'PJH')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 用JS方便点击‘票据操作’按钮旁边的倒三角形
					js_click("xpath", "//span[text()='票据操作']/parent::*/following-sibling::*/child::*")
					sleep(1)

					# 点击票据贴现按钮
					js_click("xpath", "//a[contains(text(),'票据托收')]")
					sleep(1)

					# 切入票据托收的窗体页面endorseWin-iframe
					switch_to("xpath", "//iframe[@id='endorseWin-iframe']")

					click("xpath", "//span[text()='托收收款账户']/parent::*/following-sibling::*/descendant::*[3]")
					# 输入被背书对象类型，模糊查询
					input("xpath", "//span[text()='托收收款账户']/parent::*/following-sibling::*/descendant::*[3]", "华夏银行")
					sleep(1)
					input_down("xpath", "//span[text()='托收收款账户']/parent::*/following-sibling::*/descendant::*[3]")
					input_enter("xpath", "//span[text()='托收收款账户']/parent::*/following-sibling::*/descendant::*[3]")
					time.sleep(1)

					# 输入备注
					input("xpath", "//span[@title='托收日期']/ancestor::*[3]/following-sibling::*[1]/descendant::*[5]",
					      "自动化测试票据托收备注")

					# 点击托收按钮
					click("xpath", "//span[@title='托收收款账户']/ancestor::*[10]/preceding-sibling::*[1]/descendant::*[3]")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("应收票据管理，票据托收成功！")
					logging.info("应收票据管理，票据托收成功！")
					sleep(3)

					# 取消托收
					# 切入‘应收票据管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='recDraftManage-tab-iframe']")

					# 勾选
					click("xpath", "//div[contains(text(),'PJH')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 用JS方便点击‘票据操作’按钮旁边的倒三角形
					js_click("xpath", "//span[text()='票据操作']/parent::*/following-sibling::*/child::*")
					sleep(1)

					# 点击取消票据背书按钮
					js_click("xpath", "//a[contains(text(),'取消托收')]")
					sleep(1)

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("应收票据管理，取消托收成功！")
					logging.info("应收票据管理，取消托收成功！")
					sleep(3)

					# 票据质押
					# 切入‘应收票据管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='recDraftManage-tab-iframe']")

					# 勾选
					click("xpath", "//div[contains(text(),'PJH')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 用JS方便点击‘票据操作’按钮旁边的倒三角形
					js_click("xpath", "//span[text()='票据操作']/parent::*/following-sibling::*/child::*")
					sleep(1)

					# 点击票据贴现按钮
					js_click("xpath", "//a[contains(text(),'票据质押')]")
					sleep(1)

					# 切入票据托收的窗体页面endorseWin-iframe
					switch_to("xpath", "//iframe[@id='impawneWin-iframe']")

					# 输入备注
					input("xpath", "//span[@title='质押金额']/ancestor::*[3]/following-sibling::*[3]/descendant::*[5]",
					      "自动化测试票据质押备注")

					# 点击保存按钮
					click("xpath", "//span[@title='质押日期']/ancestor::*[10]/preceding-sibling::*[1]/descendant::*[3]")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("应收票据管理，票据质押成功！")
					logging.info("应收票据管理，票据质押成功！")
					sleep(3)

					# 质押到期托收
					# 切入‘应收票据管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='recDraftManage-tab-iframe']")

					# 勾选
					click("xpath", "//div[contains(text(),'PJH')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 用JS方便点击‘票据操作’按钮旁边的倒三角形
					js_click("xpath", "//span[text()='票据操作']/parent::*/following-sibling::*/child::*")
					sleep(1)

					# 点击质押到期托收按钮
					js_click("xpath", "//a[contains(text(),'质押到期托收')]")
					sleep(1)

					# 切入质押到期托收的窗体页面
					switch_to("xpath", "//iframe[@id='impawneCollectionWin-iframe']")

					click("xpath", "//span[text()='质押到期托收日期']/ancestor::*[3]//preceding-sibling::*[6]/descendant::*[8]")
					# 输入被背书对象类型，模糊查询
					input("xpath", "//span[text()='质押到期托收日期']/ancestor::*[3]//preceding-sibling::*[6]/descendant::*[8]",
					      "华夏银行")
					sleep(1)
					input_down("xpath",
					           "//span[text()='质押到期托收日期']/ancestor::*[3]//preceding-sibling::*[6]/descendant::*[8]")
					input_enter("xpath",
					            "//span[text()='质押到期托收日期']/ancestor::*[3]//preceding-sibling::*[6]/descendant::*[8]")
					time.sleep(1)

					# 输入备注
					input("xpath", "//span[@title='质押到期托收日期']/ancestor::*[3]/following-sibling::*[1]/descendant::*[5]",
					      "自动化测试票据质押备注")

					# 点击保存按钮
					click("xpath", "//span[@title='质押到期托收日期']/ancestor::*[10]/preceding-sibling::*[1]/descendant::*[3]")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("应收票据管理，质押到期托收成功！")
					logging.info("应收票据管理，质押到期托收成功！")
					sleep(3)

					# 取消取消质押托收
					# 切入‘应收票据管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='recDraftManage-tab-iframe']")

					# 勾选
					click("xpath", "//div[contains(text(),'PJH')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 用JS方便点击‘票据操作’按钮旁边的倒三角形
					js_click("xpath", "//span[text()='票据操作']/parent::*/following-sibling::*/child::*")
					sleep(1)

					# 点击取消质押托收按钮
					js_click("xpath", "//a[contains(text(),'取消质押托收')]")
					sleep(1)

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("应收票据管理，取消质押托收！")
					logging.info("应收票据管理，取消质押托收成功！")
					sleep(3)

					# 取消质押
					# 切入‘应收票据管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='recDraftManage-tab-iframe']")

					# 勾选
					click("xpath", "//div[contains(text(),'PJH')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 用JS方便点击‘票据操作’按钮旁边的倒三角形
					js_click("xpath", "//span[text()='票据操作']/parent::*/following-sibling::*/child::*")
					sleep(1)

					# 点击取消质押托收按钮
					js_click("xpath", "//a[contains(text(),'取消质押')]")
					sleep(1)

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("应收票据管理，取消质押成功！")
					logging.info("应收票据管理，取消质押成功！")
					sleep(3)

					# 缺少换票功能

					# 坏票
					# 切入‘应收票据管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='recDraftManage-tab-iframe']")

					# 勾选
					click("xpath", "//div[contains(text(),'PJH')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 用JS方便点击‘票据操作’按钮旁边的倒三角形
					js_click("xpath", "//span[text()='票据操作']/parent::*/following-sibling::*/child::*")
					sleep(1)

					# 点击坏票按钮
					js_click("xpath", "//a[contains(text(),'坏票')]")
					sleep(1)

					# 切入质押到期托收的窗体页面
					switch_to("xpath", "//iframe[@id='badBillWin-iframe']")

					# 输入备注
					input("xpath", "//span[@title='坏票日期']/ancestor::*[3]/following-sibling::*[3]/descendant::*[5]",
					      "自动化测试坏票备注")

					# 点击保存按钮
					click("xpath", "//span[@title='坏票日期']/ancestor::*[10]/preceding-sibling::*[1]/descendant::*[3]")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("应收票据管理，坏票成功！")
					logging.info("应收票据管理，坏票成功！")
					sleep(3)

					# 取消坏票
					# 切入‘应收票据管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='recDraftManage-tab-iframe']")

					# 勾选
					click("xpath", "//div[contains(text(),'PJH')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 用JS方便点击‘票据操作’按钮旁边的倒三角形
					js_click("xpath", "//span[text()='票据操作']/parent::*/following-sibling::*/child::*")
					sleep(1)

					# 点击取消坏票按钮
					js_click("xpath", "//a[contains(text(),'取消坏票')]")
					sleep(1)

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("应收票据管理，取消坏票成功！")
					logging.info("应收票据管理，取消坏票成功！")
					sleep(3)

					# 第二次票据背书
					# 切入‘应收支票管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='recDraftManage-tab-iframe']")

					# 勾选
					click("xpath", "//div[contains(text(),'PJH')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 用JS方便点击‘票据操作’按钮旁边的倒三角形
					js_click("xpath", "//span[text()='票据操作']/parent::*/following-sibling::*/child::*")
					sleep(1)

					# 点击票据背书按钮
					js_click("xpath", "//a[contains(text(),'票据背书')]")
					sleep(1)

					# 切入票据背书的窗体页面endorseWin-iframe
					switch_to("xpath", "//iframe[@id='endorseWin-iframe']")

					click("xpath", "//input[@id='combobox-input-endorsetype']")
					# 输入被背书对象类型，模糊查询
					input("xpath", "//input[@id='combobox-input-endorsetype']", "交易对手")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-endorsetype']")
					input_enter("xpath", "//input[@id='combobox-input-endorsetype']")
					time.sleep(1)

					click("xpath", "//input[@id='combobox-input-endorsecounterpartyid']")
					# 输入被背书对象类型，模糊查询
					input("xpath", "//input[@id='combobox-input-endorsecounterpartyid']", "Mindy自动化测试")
					sleep(1)

					# 输入备注
					input("xpath", "//span[@title='背书金额']/ancestor::*[3]/following-sibling::*[3]/descendant::*[5]",
					      "自动化测试票据背书备注")

					# 点击确定按钮
					click("xpath", "//span[@title='被背书对象类型']/ancestor::*[10]/preceding-sibling::*[1]/descendant::*[3]")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("应收票据管理，第二次票据背书成功！")
					logging.info("应收票据管理，第二次票据背书成功！")
					sleep(3)

					# 退票
					# 切入‘应收票据管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='recDraftManage-tab-iframe']")

					# 勾选
					click("xpath", "//div[contains(text(),'PJH')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 用JS方便点击‘票据操作’按钮旁边的倒三角形
					js_click("xpath", "//span[text()='票据操作']/parent::*/following-sibling::*/child::*")
					sleep(1)

					# 点击坏票按钮
					js_click("xpath", "//a[contains(text(),'退票')]")
					sleep(1)

					# 切入退票的iframe页面
					switch_to("xpath", "//iframe[@id='returnedBillWin-iframe']")

					# 输入备注
					input("xpath", "//span[@title='退票日期']/ancestor::*[3]/following-sibling::*[3]/descendant::*[5]",
					      "自动化测试坏票备注")

					# 点击保存按钮
					click("xpath", "//span[@title='退票日期']/ancestor::*[10]/preceding-sibling::*[1]/descendant::*[3]")

					# 退出所有iframe窗体
					switch_default()
					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("应收票据管理，退票成功！")
					logging.info("应收票据管理，退票成功！")
					sleep(3)

					# 票据托管
					# 切入‘应收票据管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='recDraftManage-tab-iframe']")

					# 勾选
					click("xpath", "//div[contains(text(),'PJH')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 用JS方便点击‘票据操作’按钮旁边的倒三角形
					js_click("xpath", "//span[text()='票据操作']/parent::*/following-sibling::*/child::*")
					sleep(1)

					# 点击票据贴现按钮
					js_click("xpath", "//a[contains(text(),'票据托管')]")
					sleep(1)

					# 切入票据托管的窗体页面endorseWin-iframe
					switch_to("xpath", "//iframe[@id='trusteeshipWin-iframe']")

					# 输入托管日期
					today = date.today()
					cost_date = today
					click("xpath", "//input[@id='trusteeshipdate-input']")
					sleep(1)
					clear("xpath", "//input[@id='trusteeshipdate-input']")
					sleep(1)
					input("xpath", "//input[@id='trusteeshipdate-input']", str(cost_date))
					# 模拟回车键
					keyDown('enter')
					keyUp('enter')
					time.sleep(2)

					# 输入备注
					input("xpath", "//span[@title='托管日期']/ancestor::*[3]/following-sibling::*[2]/descendant::*[5]",
					      "自动化测试票据托管备注")

					# 点击托管按钮
					click("xpath", "//span[@title='托管日期']/ancestor::*[10]/preceding-sibling::*[1]/descendant::*[3]")
					sleep(1)

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("应收票据管理，票据托管成功！")
					logging.info("应收票据管理，票据托管成功！")
					sleep(3)

					# 取消托管
					# 切入‘应收票据管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='recDraftManage-tab-iframe']")

					# 勾选
					click("xpath", "//div[contains(text(),'PJH')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 用JS方便点击‘票据操作’按钮旁边的倒三角形
					js_click("xpath", "//span[text()='票据操作']/parent::*/following-sibling::*/child::*")
					sleep(1)

					# 点击取消托管按钮
					js_click("xpath", "//a[contains(text(),'取消托管')]")
					sleep(1)

					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					sleep(1)

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("应收票据管理，取消托管成功！")
					logging.info("应收票据管理，取消托管成功！")
					sleep(3)

					# 贴息
					# 切入‘应收票据管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='recDraftManage-tab-iframe']")

					# 勾选
					click("xpath", "//div[contains(text(),'PJH')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 用JS方便点击‘票据操作’按钮旁边的倒三角形
					js_click("xpath", "//span[text()='票据操作']/parent::*/following-sibling::*/child::*")
					sleep(1)

					# 点击票据贴现按钮
					js_click("xpath", "//a[contains(text(),'贴息')]")
					sleep(1)

					# 切入贴息的窗体页面endorseWin-iframe
					switch_to("xpath", "//iframe[@id='subsidiesWin-iframe']")

					# 输入贴息日期
					today = date.today()
					cost_date = today
					click("xpath", "//span[@title='贴息日期']/parent::*/following-sibling::*[1]/descendant::*[5]")
					sleep(1)
					clear("xpath", "//span[@title='贴息日期']/parent::*/following-sibling::*[1]/descendant::*[5]")
					sleep(1)
					input("xpath", "//span[@title='贴息日期']/parent::*/following-sibling::*[1]/descendant::*[5]",
					      str(cost_date))
					# 模拟回车键
					keyDown('enter')
					keyUp('enter')
					time.sleep(3)

					# 输入贴息率
					double_click("xpath", "//input[@id='discountrate-input']")
					input("xpath", "//input[@id='discountrate-input']", "20")
					sleep(1)

					# 贴息收款账号
					click("xpath", "//span[@title='贴息收款账号']/parent::*/following-sibling::*/descendant::*[3]")
					sleep(2)
					# 输入银行名称，模糊查询
					input("xpath", "//span[@title='贴息收款账号']/parent::*/following-sibling::*/descendant::*[3]", "华夏银行")
					sleep(1)
					input_down("xpath", "//span[@title='贴息收款账号']/parent::*/following-sibling::*/descendant::*[3]")
					input_enter("xpath", "//span[@title='贴息收款账号']/parent::*/following-sibling::*/descendant::*[3]")
					time.sleep(1)

					# 点击贴息按钮
					click("xpath", "//span[@title='贴息日期']/ancestor::*[10]/preceding-sibling::*[1]/descendant::*[3]")
					sleep(1)

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("应收票据管理，贴息成功！")
					logging.info("应收票据管理，贴息成功！")
					sleep(3)

					# 入账
					# 切入‘应收票据管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='recDraftManage-tab-iframe']")
					# 勾选
					click("xpath", "//div[contains(text(),'PJH')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 点击入账按钮
					js_click("xpath", "//span[(text()='入账')]")
					sleep(1)
					# 切入入账的窗体页面
					switch_to("xpath", "//iframe[@id='entryaccountWin-iframe']")
					# 勾选
					click("xpath", "//div[contains(text(),'票据贴息')]/parent::*/preceding-sibling::*[4]/descendant::*[2]")
					sleep(1)
					# 用JS的方法点击入账按钮
					js_click("xpath",
					         "//span[text()='查看交易单']/ancestor::*[9]/preceding-sibling::*[2]/child::*[6]/descendant::*[3]")
					switch_to("xpath", "//iframe[@id='entryaccountWin-iframe']")
					# 输入业务员
					input("xpath", "//input[@id='salesman']", "mindy")
					sleep(1)
					# 收款银行账号
					click("xpath", "//input[@id='combobox-input-bankaccountid']")
					# 输入银行名称，模糊查询
					input("xpath", "//input[@id='combobox-input-bankaccountid']", "华夏银行")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-bankaccountid']")
					input_enter("xpath", "//input[@id='combobox-input-bankaccountid']")
					time.sleep(1)
					# 点击保存按钮
					click("xpath", "//span[text()='业务员']/ancestor::*[10]/preceding-sibling::*[1]/descendant::*[3]")
					sleep(1)
					# 退出当前页面的iframe窗体
					switch_default()
					# 用隐式等待方法等页面出现提示框
					# implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("应收票据管理，入账成功！")
					logging.info("应收票据管理，入账成功！")
					sleep(3)
					# 切入应收票据管理的iframe窗体，去点击关闭
					switch_to("xpath", "//iframe[@id='recDraftManage-tab-iframe']")
					click("xpath", "//span[@class='f-win-title ' and contains(text(),'入账')]/preceding-sibling::*")
					# 退出所有iframe窗体
					switch_default()
				# 第三笔，审核
				elif i == 3:
					# 操作记录查看
					# 切入‘应收票据管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='recDraftManage-tab-iframe']")

					# 输入支票号：ZPH
					click("xpath", "//input[@id='draftcode']")
					sleep(1)
					clear("xpath", "//input[@id='draftcode']")
					input("xpath", "//input[@id='draftcode']", "PJH")
					sleep(1)

					# 点击查询
					click("xpath", "//span[text()='查询']")

					# 勾选
					click("xpath", "//div[contains(text(),'PJH')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 点击审核按钮
					click("xpath", "//span[text()='审核']")

					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					sleep(1)

					# 勾选
					click("xpath", "//div[contains(text(),'PJH')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 点击操作记录查看按钮
					js_click("xpath", "//span[(text()='操作记录查看')]")
					sleep(1)
					# 切入操作记录查看的窗体页面
					switch_to("xpath", "//iframe[@id='operationWin-iframe']")
					# 勾选
					js_click("xpath", "//span[@class='f-contrac-close']")
					sleep(1)
					# 输入票据号：
					input("xpath", "//input[@id='draftcode' and @class='f-textField ']", "PJH")
					sleep(1)
					click("xpath", "//div[@title='操作标识:收票']/parent::*/preceding-sibling::*[4]/descendant::*[2]")
					js_click("xpath", "//span[(text()='生成交易单')]")
					sleep(1)
					switch_parent()
					switch_to("xpath", "//iframe[@id='recmentsWin-iframe']")
					sleep(1)

					# mysql和oracle版本在交易类型数据带出时有区别，因此自动化选择数据combobox-input-paytypeid
					# 部门
					click("xpath", "//input[@id='combobox-input-paytypeid']")
					sleep(1)
					clear("xpath", "//input[@id='combobox-input-paytypeid']")
					sleep(1)
					# 输入交易类型名称，模糊查询
					input("xpath", "//input[@id='combobox-input-paytypeid']", "201-外部收款")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-paytypeid']")
					input_enter("xpath", "//input[@id='combobox-input-paytypeid']")
					time.sleep(1)

					# 部门
					click("xpath", "//input[@id='combobox-input-applyorgid']/ancestor::*[5]/descendant::*[21]")
					# 输入银行名称，模糊查询
					input("xpath", "//input[@id='combobox-input-applyorgid']/ancestor::*[5]/descendant::*[21]",
					      "自动化测试部")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-applyorgid']/ancestor::*[5]/descendant::*[21]")
					input_enter("xpath", "//input[@id='combobox-input-applyorgid']/ancestor::*[5]/descendant::*[21]")
					time.sleep(1)

					# # 用途
					input("xpath", "//input[@id='combobox-input-purpose']", "TestHth001")
					sleep(1)

					# 收方账户
					# 输入银行名称，模糊查询
					input("xpath",
					      "//input[@id='combobox-input-ourbankaccountid' and @class='f-combo-input f-input-bg  f-combo-input-forceselect']",
					      "中国银行 ")
					sleep(1)
					input_down("xpath",
					           "//input[@id='combobox-input-ourbankaccountid' and @class='f-combo-input f-input-bg  f-combo-input-forceselect']")
					input_enter("xpath",
					            "//input[@id='combobox-input-ourbankaccountid' and @class='f-combo-input f-input-bg  f-combo-input-forceselect']")
					time.sleep(1)

					# 计划项目
					click("xpath", "//input[@id='combobox-input-budgetitemid']")
					# 输入银行名称，模糊查询
					input("xpath", "//input[@id='combobox-input-budgetitemid']", "自动化测试计划项目")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-budgetitemid']")
					input_enter("xpath", "//input[@id='combobox-input-budgetitemid']")
					time.sleep(1)

					# 资金类别
					click("xpath", "//input[@id='combobox-input-capitalcategoryid']")
					# 输入银行名称，模糊查询
					input("xpath", "//input[@id='combobox-input-capitalcategoryid']", "自动化测试资金类别")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-capitalcategoryid']")
					input_enter("xpath", "//input[@id='combobox-input-capitalcategoryid']")
					time.sleep(1)

					# 现金流量项目
					click("xpath", "//input[@id='combobox-input-cashflowitemid']")
					# 输入银行名称，模糊查询
					input("xpath", "//input[@id='combobox-input-cashflowitemid']", "自动化测试现金流")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-cashflowitemid']")
					input_enter("xpath", "//input[@id='combobox-input-cashflowitemid']")
					time.sleep(1)

					# 短信通知
					input("xpath", "//input[@id='oppcellphone']", "178短信通知")
					sleep(1)

					# 邮件通知
					input("xpath", "//input[@id='oppemailaddress']", "1074658681@qq.com邮件通知")
					sleep(1)
					# 合同号
					input("xpath", "//input[@id='contractnumber']", "TestHth001")
					sleep(1)
					# 工程项目
					click("xpath", "//input[@id='combobox-input-projectitemid']")
					# 输入银行名称，模糊查询
					input("xpath", "//input[@id='combobox-input-projectitemid']", "自动化测试工程项目")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-projectitemid']")
					input_enter("xpath", "//input[@id='combobox-input-projectitemid']")
					time.sleep(1)

					# 备注框中填入值
					input("xpath", "//textarea[@id='memo']", "自动化测试生成交易单备注框")
					sleep(1)

					# 备注框中填入值
					input("xpath", "//textarea[@id='description']", "自动化测试生成交易单描述框")
					sleep(1)

					# 点击收款明细
					click("xpath", "//span[(text()='收款明细')]")
					sleep(1)

					# 点击收款明细新增行，新增第一行
					click("xpath", "//span[@title='部门']/ancestor::*[6]/following-sibling::*[2]/descendant::*[7]")
					sleep(1)

					# 输入组织
					click("xpath", "//input[@id='combobox-input-recmenteditgrid-claimorgid-0']")
					# 输入银行名称，模糊查询
					input("xpath", "//input[@id='combobox-input-recmenteditgrid-claimorgid-0']", "亚唐科技")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-recmenteditgrid-claimorgid-0']")
					input_enter("xpath", "//input[@id='combobox-input-recmenteditgrid-claimorgid-0']")
					time.sleep(1)

					# 输入部门
					click("xpath", "//input[@id='combobox-input-recmenteditgrid-deptid-0']")
					# 输入银行名称，模糊查询
					input("xpath", "//input[@id='combobox-input-recmenteditgrid-deptid-0']", "自动化测试部")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-recmenteditgrid-deptid-0']")
					input_enter("xpath", "//input[@id='combobox-input-recmenteditgrid-deptid-0']")
					time.sleep(1)

					# 金额
					input("xpath", "//input[@id='recmenteditgrid-amount-0-input']", "1000000.00")
					sleep(1)

					# 输入工程项目
					click("xpath", "//input[@id='combobox-input-recmenteditgrid-projectitemid-0']")
					# 输入银行名称，模糊查询
					input("xpath", "//input[@id='combobox-input-recmenteditgrid-projectitemid-0']", "自动化测试工程项目")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-recmenteditgrid-projectitemid-0']")
					input_enter("xpath", "//input[@id='combobox-input-recmenteditgrid-projectitemid-0']")
					time.sleep(1)

					# 合同号
					input("xpath", "//input[@id='recmenteditgrid-contractcode-0']", "TestHth001")
					sleep(1)

					# 资金类别
					click("xpath", "//input[@id='combobox-input-recmenteditgrid-capitalcategoryid-0']")
					# 输入银行名称，模糊查询
					input("xpath", "//input[@id='combobox-input-recmenteditgrid-capitalcategoryid-0']", "自动化测试资金类别")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-recmenteditgrid-capitalcategoryid-0']")
					input_enter("xpath", "//input[@id='combobox-input-recmenteditgrid-capitalcategoryid-0']")
					time.sleep(1)

					# 计划项目
					click("xpath", "//input[@id='combobox-input-recmenteditgrid-budgetitemid-0']")
					# 输入银行名称，模糊查询
					input("xpath", "//input[@id='combobox-input-recmenteditgrid-budgetitemid-0']", "自动化计划项目")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-recmenteditgrid-budgetitemid-0']")
					input_enter("xpath", "//input[@id='combobox-input-recmenteditgrid-budgetitemid-0']")
					time.sleep(1)

					# 现金流量项目
					click("xpath", "//input[@id='combobox-input-recmenteditgrid-cashflowitemid-0']")
					# 输入银行名称，模糊查询
					input("xpath", "//input[@id='combobox-input-recmenteditgrid-cashflowitemid-0']", "自动化测试现金流")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-recmenteditgrid-cashflowitemid-0']")
					input_enter("xpath", "//input[@id='combobox-input-recmenteditgrid-cashflowitemid-0']")
					time.sleep(1)

					# 备注框中填入值
					input("xpath", "//input[@id='recmenteditgrid-memo-0']", "自动化测试生成交易单备注框")
					sleep(1)

					# 点击确认保存
					click("xpath", "//span[text()='保存']")
					# 退出所有的iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现新增成功的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("操作记录查看，生成交易单保存成功！")
					sleep(3)

				elif i == 4:
					# 收票生成交易单
					# 切入‘应收票据管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='recDraftManage-tab-iframe']")

					# 输入支票号：ZPH
					click("xpath", "//input[@id='draftcode']")
					sleep(1)
					clear("xpath", "//input[@id='draftcode']")
					input("xpath", "//input[@id='draftcode']", "PJH")
					sleep(1)

					# 点击查询
					click("xpath", "//span[text()='查询']")

					# 勾选
					click("xpath", "//div[contains(text(),'PJH')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 点击审核按钮
					click("xpath", "//span[text()='审核']")

					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					sleep(1)

					# 勾选
					click("xpath", "//div[contains(text(),'PJH')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 点击收票生成交易单按钮
					js_click("xpath", "//span[(text()='收票生成交易单')]")
					sleep(1)

					# 切入收票生成交易单的iframe页面
					switch_to("xpath", "//iframe[@id='receiveGenRecmentWin-iframe']")

					# mysql和oracle版本在交易类型数据带出时有区别，因此自动化选择数据combobox-input-paytypeid
					# 部门
					click("xpath", "//input[@id='combobox-input-paytypeid']")
					sleep(1)
					clear("xpath", "//input[@id='combobox-input-paytypeid']")
					sleep(1)
					# 输入交易类型名称，模糊查询
					input("xpath", "//input[@id='combobox-input-paytypeid']", "201-外部收款")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-paytypeid']")
					input_enter("xpath", "//input[@id='combobox-input-paytypeid']")
					time.sleep(1)

					# 收方账户
					click("xpath",
					      "//input[@id='combobox-input-ourbankaccountid' and @class='f-combo-input f-input-bg  f-combo-input-forceselect']")
					# 输入银行名称，模糊查询
					input("xpath",
					      "//input[@id='combobox-input-ourbankaccountid' and @class='f-combo-input f-input-bg  f-combo-input-forceselect']",
					      "中国银行 ")
					sleep(1)
					input_down("xpath",
					           "//input[@id='combobox-input-ourbankaccountid' and @class='f-combo-input f-input-bg  f-combo-input-forceselect']")
					input_enter("xpath",
					            "//input[@id='combobox-input-ourbankaccountid' and @class='f-combo-input f-input-bg  f-combo-input-forceselect']")
					time.sleep(1)

					# 部门
					click("xpath", "//input[@id='combobox-input-deptid']")
					# 输入银行名称，模糊查询
					input("xpath", "//input[@id='combobox-input-deptid']", "自动化测试部")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-deptid']")
					input_enter("xpath", "//input[@id='combobox-input-deptid']")
					time.sleep(1)

					# 计划项目
					click("xpath", "//input[@id='combobox-input-budgetitemid']")
					# 输入银行名称，模糊查询
					input("xpath", "//input[@id='combobox-input-budgetitemid']", "自动化计划项目")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-budgetitemid']")
					input_enter("xpath", "//input[@id='combobox-input-budgetitemid']")
					time.sleep(1)

					# 现金流量项目
					click("xpath", "//input[@id='combobox-input-cashflowitemid']")
					# 输入银行名称，模糊查询
					input("xpath", "//input[@id='combobox-input-cashflowitemid']", "自动化测试现金流")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-cashflowitemid']")
					input_enter("xpath", "//input[@id='combobox-input-cashflowitemid']")
					time.sleep(1)

					# 资金类别
					click("xpath", "//input[@id='combobox-input-capitalcategoryid']")
					# 输入银行名称，模糊查询
					input("xpath", "//input[@id='combobox-input-capitalcategoryid']", "自动化测试资金类别")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-capitalcategoryid']")
					input_enter("xpath", "//input[@id='combobox-input-capitalcategoryid']")
					time.sleep(1)

					# 工程项目
					click("xpath", "//input[@id='combobox-input-projectitemid']")
					# 输入银行名称，模糊查询
					input("xpath", "//input[@id='combobox-input-projectitemid']", "自动化测试工程项目")
					sleep(1)
					# 模拟回车
					click("xpath",
					      "//div[@title='代码-名称:TestPro001-自动化测试工程项目']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
					sleep(1)

					# 合同号
					input("xpath", "//input[@id='contractnumber']", "TestHth001")
					sleep(1)
					click("xpath", "//span[text()='确认']")
					# 退出所有的iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现新增成功的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("收票生成交易单，保存成功！")
					sleep(3)

					# 批量筛选票据
					switch_to("xpath", "//iframe[@id='recDraftManage-tab-iframe']")
					# 点击收票生成交易单按钮
					js_click("xpath", "//span[(text()='批量筛选票据')]")
					sleep(1)
					input("xpath", "//textarea[@id='selectdraftcodes']", "PJH")

					click("xpath", "//span[text()='确定']")
					# 用隐式等待方法等页面出现预期数据：外部给票单位:Mindy自动化测试
					implici_wait("xpath", "//div[@title='外部给票单位:Mindy自动化测试']")
					print("批量筛选票据成功！")
					time.sleep(3)
					switch_default()

				elif i == 5:
					# 收票生成交易单
					# 切入‘应收票据管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='recDraftManage-tab-iframe']")

					# 输入支票号：ZPH
					click("xpath", "//input[@id='draftcode']")
					sleep(1)
					clear("xpath", "//input[@id='draftcode']")
					input("xpath", "//input[@id='draftcode']", "PJH")
					sleep(1)

					# 点击查询
					click("xpath", "//span[text()='查询']")

					# 勾选
					click("xpath", "//div[contains(text(),'PJH')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 点击审核按钮
					click("xpath", "//span[text()='审核']")

					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					sleep(1)

					switch_default()
					# 用隐式等待方法等页面出现预期数据：外部给票单位:Mindy自动化测试
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("第5次审核成功，保存成功！")
					sleep(3)

					# 支票登记后去付款处理新增该账户的付款单
					logging.info("开始测试资金结算管理的页面功能")
					# 将页面的滚动条滑动到‘资金结算管理’页面的地方
					js_gd("xpath", "//span[contains(text(),'资金结算管理')]")
					# 用JS的方法点击资金结算管理菜单按钮
					js_click("xpath", "//span[contains(text(),'资金结算管理')]")

					# 付款处理--支票支付
					try:
						# 点击资金系统收付菜单
						click("xpath", "//span[@title='资金系统收付']")
						# 点击应付支票领用菜单
						click("xpath", "//span[@title='付款处理']")
						# 退出所有的iframe窗体
						switch_default()

						logging.info("开始测试付款处理功能")

						# 切入‘付款处理’的iframe窗体
						switch_to("xpath", "//iframe[@id='generalPayment-tab-iframe']")

						# 点击承兑汇票支付
						click("xpath", "//span[text()='承兑汇票支付']")

						# 切入‘支票支付’的iframe窗体
						switch_to("xpath", "//iframe[@id='subTabSix-iframe']")
						sleep(1)

						# 用JS的方法点击新增按钮
						js_click("xpath", "//span[text()='新增']")

						# 切入新增的iframe窗体
						switch_to("xpath", "//iframe[@id='addWin-iframe']")
						sleep(1)

						# 选择交易类型
						click("xpath", "//input[@id='combobox-input-paytypeid']")
						input("xpath", "//input[@id='combobox-input-paytypeid']", "103-对外付款")
						sleep(1)
						input_down("xpath", "//input[@id='combobox-input-paytypeid']")
						input_enter("xpath", "//input[@id='combobox-input-paytypeid']")
						time.sleep(1)

						# 选择结算方式
						click("xpath", "//input[@id='combobox-input-settlementmodeid']")
						clear("xpath", "//input[@id='combobox-input-settlementmodeid']")
						input("xpath", "//input[@id='combobox-input-settlementmodeid']", "201-应收承兑汇票背书")
						sleep(1)
						input_down("xpath", "//input[@id='combobox-input-settlementmodeid']")
						sleep(1)
						input_enter("xpath", "//input[@id='combobox-input-settlementmodeid']")
						time.sleep(1)

						# 收方名称
						click("xpath", "//input[@id='combobox-input-oppcounterpartyid']")
						sleep(1)
						input("xpath", "//input[@id='combobox-input-oppcounterpartyid']", "Mindy自动化测试")
						sleep(1)

						# 输入金额
						input("xpath", "//input[@id='ouramount-input']", "226")
						sleep(1)

						# 点击保存
						click("xpath", "//span[text()='保存']")

						# 退出所有iframe窗体
						switch_default()

						# 用隐式等待方法等页面出现提示框
						implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
						print("付款处理，承兑汇票支付保存成功！")
						logging.info("付款处理，承兑汇票支付保存成功！")
						sleep(3)

						# 切入‘付款处理’的iframe窗体
						switch_to("xpath", "//iframe[@id='generalPayment-tab-iframe']")

						# 点击支票支付tab页
						click("xpath", "//span[text()='承兑汇票支付']")

						# 切入‘支票支付’的iframe窗体
						switch_to("xpath", "//iframe[@id='subTabSix-iframe']")
						sleep(1)

						# 选择新建的付款单
						click("xpath",
						      "//div[@title='收方名称:Mindy自动化测试']/parent::*[1]/preceding-sibling::*[6]/descendant::*[2]")

						# 点击送审按钮
						click("xpath", "//span[text()='送审']")

						# 退出所有iframe窗体
						switch_default()

						# 用隐式等待方法等页面出现审核的提示框
						implici_wait("xpath", "//span[contains(text(),'操作成功！送审成功1笔，失败0笔。')]")
						print("承兑汇票支付，第一次送审成功！")
						logging.info("承兑汇票支付，第一次送审成功！")
						time.sleep(3)

						# 点击审核
						# 切入‘付款处理’的iframe窗体
						switch_to("xpath", "//iframe[@id='generalPayment-tab-iframe']")

						# 点击支票支付tab页
						click("xpath", "//span[text()='承兑汇票支付']")

						# 切入‘支票支付’的iframe窗体
						switch_to("xpath", "//iframe[@id='subTabSix-iframe']")
						sleep(1)

						# 点击审核按钮
						double_click("xpath",
						             "//div[@title='收方名称:Mindy自动化测试']/parent::*[1]/preceding-sibling::*[6]/descendant::*[2]")
						sleep(1)

						switch_to("xpath", "//iframe[@id='wf_taskProcessing_win-iframe']")
						sleep(1)

						click("xpath", "//span[text()='同意']")
						sleep(1)

						# 退出所有iframe窗体
						switch_default()

						# 用隐式等待方法等页面出现审核的提示框
						implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
						print("承兑汇票支付，审批成功！")
						logging.info("承兑汇票支付，审批成功！")
						time.sleep(3)

						# 切入‘付款处理’的iframe窗体
						switch_to("xpath", "//iframe[@id='generalPayment-tab-iframe']")

						# 点击支票支付tab页
						click("xpath", "//span[text()='承兑汇票支付']")

						# 切入‘支票支付’的iframe窗体
						switch_to("xpath", "//iframe[@id='subTabSix-iframe']")
						sleep(1)

						# 选择新建的付款单
						click("xpath",
						      "//div[@title='收方名称:Mindy自动化测试']/parent::*[1]/preceding-sibling::*[6]/descendant::*[2]")

						# 点击领用按钮
						click("xpath", "//span[text()='领票/开票']")
						sleep(1)

						# 切入领票/开票的iframe窗体
						switch_to("xpath", "//iframe[@id='payWin-iframe']")
						sleep(1)

						# 选择一条数据
						click("xpath",
						      "//div[contains(text(),'PJH')]/parent::*/preceding-sibling::*[4]/descendant::*[2]")
						sleep(1)

						# 点击背书
						click("xpath", "//span[text()='背书']")
						sleep(1)

						# 点击弹出框的OK键
						click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
						sleep(1)

						# 进入背书确认的iframe窗体
						switch_to("xpath", "//iframe[@id='endorseWin-iframe']")

						# 点击保存按钮
						click("xpath", "//span[text()='保存']")
						sleep(1)

						# 退出所有的iframe窗体
						switch_default()

						# 用隐式等待方法等页面出现新增成功的提示框
						implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
						print("承兑汇票支付，领票/开票保存成功！")
						sleep(3)

						switch_default()

						# 用JS的方法关闭当前页面
						js_click("xpath", "//a[@title='付款处理']/child::*[1]")

						# 再次点击基础设置菜单，使之关闭
						click("xpath", "//span[@title='资金系统收付']")

						# 打印操作成功日志
						print("付款处理，操作成功!")
						logging.info("付款处理，操作成功!")
						time.sleep(2)

					except Exception as err:
						# 发生其他异常时，打印异常堆栈信息
						print(traceback.print_exc())
						logging.debug("付款处理，支票支付打印失败！" + str(traceback.format_exc()))
						# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
						dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
						dir_path = make_current_hour_dir(dir_path + "\\")
						pic_path = os.path.join(dir_path, get_current_time() + ".png")
						capture(pic_path)

					logging.info("开始测试票据管理的页面功能")
					# 将页面的滚动条滑动到‘票据管理’页面的地方
					# js_gd("xpath", "//span[contains(text(),'票据管理')]")
					# 用JS的方法点击票据管理菜单按钮
					js_click("xpath", "//span[contains(text(),'票据管理')]")

					# 测试承兑票据管理-应收票据管理

					# 点击承兑票据管理菜单
					# js_click("xpath", "//span[@title='承兑汇票管理']")
					# 点击应收支票登记菜单
					click("xpath", "//span[@title='应收票据管理']")
					# 退出所有的iframe窗体
					switch_default()
					logging.info("开始测试应收票据管理功能")

					# 收票生成交易单
					# 切入‘应收票据管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='recDraftManage-tab-iframe']")

					# 勾选
					click("xpath", "//div[@title='票据状态:已背书']/parent::*/preceding-sibling::*[3]/descendant::*[2]")

					# 用JS方便点击‘票据操作’按钮旁边的倒三角形
					js_click("xpath", "//span[text()='票据操作']/parent::*/following-sibling::*/child::*")
					sleep(1)

					# 点击退票按钮
					click("xpath", "//a[contains(text(),'换票')]")
					sleep(1)

					# 进入换票的iframe窗体

					switch_to("xpath", "//iframe[@id='replaceWin-iframe']")
					sleep(1)

					# 点击选择
					click("xpath", "//div[@title='票据状态:已收票']/parent::*/preceding-sibling::*[3]/descendant::*[2]")
					sleep(1)

					# 点击背书按钮
					click("xpath", "//span[text()='确定']")
					sleep(1)

					# 退出所有iframe窗体
					switch_default()
					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("应付票据管理，换票成功！")
					logging.info("应付票据管理，换票成功！")
					sleep(3)

					# 退出所有iframe窗体
					switch_default()

				elif i == 6:
					# 收票生成交易单
					# 切入‘应收票据管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='recDraftManage-tab-iframe']")

					# # 输入支票号：ZPH
					# click("xpath", "//input[@id='draftcode']")
					# sleep(1)
					# clear("xpath", "//input[@id='draftcode']")
					# input("xpath", "//input[@id='draftcode']", "PJH")
					# sleep(1)
					#
					# # 点击查询
					# click("xpath", "//span[text()='查询']")

					# 勾选
					click("xpath", "//div[contains(text(),'PJH')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 点击审核按钮
					click("xpath", "//span[text()='审核']")

					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					sleep(1)

					switch_default()
					# 用隐式等待方法等页面出现预期数据：外部给票单位:Mindy自动化测试
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("第5次审核成功，保存成功！")
					sleep(3)

			# 退出所有iframe窗体
			switch_default()

			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='应收票据管理']/child::*[1]")

			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//span[@title='承兑汇票管理']")

			# 打印操作成功日志
			print("应收票据管理，操作成功!")
			logging.info("应收票据管理，操作成功!")
			time.sleep(2)

		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("应收票据管理,失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)

		# 在测试应付票据之前先新增授信协议
		logging.info("开始测试融资管理-融资授信-授信协议功能")
		# 将页面的滚动条滑动到‘融资管理’页面的地方
		# js_gd("xpath", "//span[contains(text(),'融资管理')]")
		# 用JS的方法点击票据管理菜单按钮
		js_click("xpath", "//span[contains(text(),'融资管理')]")

		# 测试基础设置--融资产品
		try:
			# 点击基础设置菜单
			click("xpath", "//li[@f_value='loanSetting']/descendant-or-self::*[5]")
			# 点击授信协议菜单
			click("xpath", "//span[@title='融资产品']")
			# 退出所有的iframe窗体
			switch_default()

			# 进入融资产品的iframe窗体
			switch_to("xpath", "//iframe[@id='products-tab-iframe']")
			sleep(1)

			# 点击设置使用范围
			click("xpath", "//span[text()='设置适用范围']")
			sleep(1)

			# 银行授信单
			# 进入单据对象可选授信产品
			switch_to("xpath", "//iframe[@id='setscopeWin-iframe']")
			sleep(1)

			# 点击进入设置使用范围iframe窗体
			switch_to("xpath", "//iframe[@id='subTab-iframe']")
			sleep(1)
			logging.info("进入窗体")

			# 点击查看
			# 用JS的方法点击放大镜
			js_click("xpath", "//span[@class='f-contrac-close']")
			sleep(1)

			# 输入名称
			input("xpath", "//input[@id='name']", "授信")
			sleep(1)

			# 点击查询
			click("xpath", "//span[text()='查询']")
			sleep(1)

			# 选择一条数据进行设置使用范围
			click("xpath", "//div[@title='名称:银行授信单']/parent::*/preceding-sibling::*[2]/descendant::*[2]")
			sleep(1)

			# 点击分配
			click("xpath", "//span[text()='分配']")
			sleep(1)

			# 点击进入分配详情iframe窗体
			switch_to("xpath", "//iframe[@id='distributeWin-iframe']")
			sleep(1)

			# 点击三角
			# 用JS方便点击‘分配授信产品’按钮旁边的倒三角形
			js_click("xpath", "//span[text()='分配授信产品']/parent::*/descendant::*[3]")
			sleep(1)

			# 点击选择全部按钮
			click("xpath", "//div[contains(text(),'选择全部')]")
			sleep(1)

			click("xpath", "//span[text()='保存']")

			switch_default()

			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("银行授信单，操作成功！")
			logging.info("银行授信单，操作成功！")
			sleep(3)

			# 进入融资产品的iframe窗体
			switch_to("xpath", "//iframe[@id='products-tab-iframe']")
			sleep(1)

			# 保函
			# 进入单据对象可选授信产品
			switch_to("xpath", "//iframe[@id='setscopeWin-iframe']")
			sleep(1)

			# 点击进入设置使用范围iframe窗体
			switch_to("xpath", "//iframe[@id='subTab-iframe']")
			sleep(1)
			logging.info("进入窗体")

			# 输入名称
			clear("xpath", "//input[@id='name']")
			sleep(1)
			input("xpath", "//input[@id='name']", "保函")
			sleep(1)

			# 点击查询
			click("xpath", "//span[text()='查询']")
			sleep(1)

			# 选择一条数据进行设置使用范围
			click("xpath", "//div[@title='名称:委托方保函']/parent::*/preceding-sibling::*[2]/descendant::*[2]")
			sleep(1)

			# 点击分配
			click("xpath", "//span[text()='重置']")
			sleep(1)

			# 点击进入分配详情iframe窗体
			switch_to("xpath", "//iframe[@id='resetWin-iframe']")
			sleep(1)

			# 选择保函
			click("xpath", "//input[@id='editgrid-distributefldvalue-5']")

			click("xpath", "//span[text()='保存']")

			switch_default()

			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("委托方保函，操作成功！")
			logging.info("委托方保函，操作成功！")
			sleep(3)

			# 进入融资产品的iframe窗体
			switch_to("xpath", "//iframe[@id='products-tab-iframe']")
			sleep(1)

			# 保函
			# 进入单据对象可选授信产品
			switch_to("xpath", "//iframe[@id='setscopeWin-iframe']")
			sleep(1)

			# 点击进入设置使用范围iframe窗体
			switch_to("xpath", "//iframe[@id='subTab-iframe']")
			sleep(1)
			logging.info("进入窗体")

			# 选择一条数据进行设置使用范围
			click("xpath", "//div[@title='名称:受益方保函']/parent::*/preceding-sibling::*[2]/descendant::*[2]")
			sleep(1)

			# 点击分配
			click("xpath", "//span[text()='重置']")
			sleep(1)

			# 点击进入分配详情iframe窗体
			switch_to("xpath", "//iframe[@id='resetWin-iframe']")
			sleep(1)

			# 选择保函
			click("xpath", "//input[@id='editgrid-distributefldvalue-5']")

			click("xpath", "//span[text()='保存']")

			switch_default()

			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("委托方保函，操作成功！")
			logging.info("委托方保函，操作成功！")
			sleep(3)

			# 用JS的方法关闭当前页面
			click("xpath", "//span[text()='融资产品']")

			# 用JS的方法关闭当前页面
			js_click("xpath", "//li[@f_value='loanSetting']/descendant-or-self::*[5]")

			# 打印操作成功日志
			print("融资产品，操作成功!")
			logging.info("融资产品，操作成功!")
			time.sleep(2)

		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("融资产品操作失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)

		# 测试融资授信--授信协议
		try:

			# 点击融资授信菜单
			click("xpath", "//span[@title='融资授信']")
			# 点击授信协议菜单
			click("xpath", "//span[@title='授信协议']")
			# 退出所有的iframe窗体
			switch_default()

			for i in range(1, 3):
				# 切入授信协议的iframe窗体
				logging.info("开始测试授信协议功能")
				switch_to("xpath", "//iframe[@id='credits-tab-iframe']")

				# 用JS的方法点击新增按钮
				js_click("xpath", "//span[text()='新增']")

				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='addWin-iframe']")
				sleep(1)

				# 协议号
				if i == 1:
					temp1 = time.strftime("%H%M%S")
					input("xpath", "//input[@id='contractcode']", "ZDHXYH002" + str(temp1))

				if i == 2:
					temp1 = time.strftime("%H%M%S")
					input("xpath", "//input[@id='contractcode']", "ZDHZYFXYH001" + str(temp1))

				# 融资机构类别
				click("xpath", "//input[@id='combobox-input-financialinstitutiontype']")
				sleep(1)
				input("xpath", "//input[@id='combobox-input-financialinstitutiontype']", "银行")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-financialinstitutiontype']")
				sleep(1)
				input_enter("xpath", "//input[@id='combobox-input-financialinstitutiontype']")
				time.sleep(1)

				# 融资机构
				click("xpath", "//input[@id='combobox-input-bankid']")
				sleep(1)
				input("xpath", "//input[@id='combobox-input-bankid']", "中国银行")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-bankid']")
				sleep(1)
				input_enter("xpath", "//input[@id='combobox-input-bankid']")
				time.sleep(1)

				# 输入授信额度
				clear("xpath", "//input[@id='creditamount-input']")
				sleep(1)
				input("xpath", "//input[@id='creditamount-input']", "3000000")
				sleep(1)

				# 协议开始日期
				today = date.today()
				begin_date = today - timedelta(days=20)
				click("xpath", "//input[@id='begindate-input']")
				sleep(1)
				clear("xpath", "//input[@id='begindate-input']")
				sleep(1)
				input("xpath", "//input[@id='begindate-input']", str(begin_date))
				time.sleep(1)

				# 协议结束日期
				today = date.today()
				end_date = today + timedelta(days=40)
				click("xpath", "//input[@id='enddate-input']")
				sleep(1)
				clear("xpath", "//input[@id='enddate-input']")
				sleep(1)
				input("xpath", "//input[@id='enddate-input']", str(end_date))
				time.sleep(1)

				# 选择使用模式
				click("xpath", "//input[@id='combobox-input-usemode']")
				sleep(1)
				input("xpath", "//input[@id='combobox-input-usemode']", "下属组织共享")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-usemode']")
				sleep(1)
				input_enter("xpath", "//input[@id='combobox-input-usemode']")
				time.sleep(1)

				# 选择循环使用
				click("xpath", "//input[@id ='iscycleused']")
				sleep(1)

				# 选择控制授信产品使用额度
				click("xpath", "//input[@id ='iscontrolproductamount']")
				sleep(1)

				if i == 2:
					# 选择授信方式使用额度iscontrolguaranteeamount
					click("xpath", "//input[@id ='iscontrolguaranteeamount']")
					sleep(1)

					# 授信方式控制授信额度
					click("xpath", "//input[@id ='combobox-input-controlguaranteeamountmode']")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-controlguaranteeamountmode']")
					sleep(1)
					input_enter("xpath", "//input[@id='combobox-input-controlguaranteeamountmode']")
					time.sleep(1)

				# 点击授信产品tab页
				click("xpath", "//span[text()='授信产品']")
				sleep(1)

				if i == 1:
					# 授信产品新增第一行
					click("xpath", "//span[text()='新增行']")
					sleep(1)

					# 选择授信产品
					click("xpath", "//input[@id='combobox-input-creditbusinessgrid-financeproductid-0']")
					sleep(1)
					input("xpath", "//input[@id='combobox-input-creditbusinessgrid-financeproductid-0']", "109-银行承兑汇票")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-creditbusinessgrid-financeproductid-0']")
					sleep(1)
					input_enter("xpath", "//input[@id='combobox-input-creditbusinessgrid-financeproductid-0']")
					time.sleep(1)

					# 输入额度
					clear("xpath", "//input[@id='creditbusinessgrid-creditamount-0-input']")
					sleep(1)
					input("xpath", "//input[@id='creditbusinessgrid-creditamount-0-input']", "3000000")
					sleep(1)

					# 授信产品新增第一行
					click("xpath", "//span[text()='新增行']")
					sleep(1)

					# 选择授信产品
					click("xpath", "//input[@id='combobox-input-creditbusinessgrid-financeproductid-1']")
					sleep(1)
					input("xpath", "//input[@id='combobox-input-creditbusinessgrid-financeproductid-1']", "CDBT-承兑保贴")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-creditbusinessgrid-financeproductid-1']")
					sleep(1)
					input_enter("xpath", "//input[@id='combobox-input-creditbusinessgrid-financeproductid-1']")
					time.sleep(1)

					# 输入额度
					clear("xpath", "//input[@id='creditbusinessgrid-creditamount-1-input']")
					sleep(1)
					input("xpath", "//input[@id='creditbusinessgrid-creditamount-1-input']", "3000000")
					sleep(1)

					# 授信产品新增第二行
					click("xpath", "//span[text()='新增行']")
					sleep(1)

					# 选择授信产品
					click("xpath", "//input[@id='combobox-input-creditbusinessgrid-financeproductid-2']")
					sleep(1)
					input("xpath", "//input[@id='combobox-input-creditbusinessgrid-financeproductid-2']", "保函")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-creditbusinessgrid-financeproductid-2']")
					sleep(1)
					input_enter("xpath", "//input[@id='combobox-input-creditbusinessgrid-financeproductid-2']")
					time.sleep(1)

					# 输入额度
					clear("xpath", "//input[@id='creditbusinessgrid-creditamount-2-input']")
					sleep(1)
					input("xpath", "//input[@id='creditbusinessgrid-creditamount-2-input']", "3000000")
					sleep(1)

					# 授信产品新增第三行
					click("xpath", "//span[text()='新增行']")
					sleep(1)

					# 选择授信产品
					click("xpath", "//input[@id='combobox-input-creditbusinessgrid-financeproductid-3']")
					sleep(1)
					input("xpath", "//input[@id='combobox-input-creditbusinessgrid-financeproductid-3']", "信用证开证")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-creditbusinessgrid-financeproductid-3']")
					sleep(1)
					input_enter("xpath", "//input[@id='combobox-input-creditbusinessgrid-financeproductid-3']")
					time.sleep(1)

					# 输入额度
					clear("xpath", "//input[@id='creditbusinessgrid-creditamount-3-input']")
					sleep(1)
					input("xpath", "//input[@id='creditbusinessgrid-creditamount-3-input']", "3000000")
					sleep(1)

				if i == 2:
					# 授信产品新增第一行
					click("xpath", "//span[text()='新增行']")
					sleep(1)

					# 选择授信产品
					click("xpath", "//input[@id='combobox-input-creditbusinessgrid-financeproductid-0']")
					sleep(1)
					input("xpath", "//input[@id='combobox-input-creditbusinessgrid-financeproductid-0']", "信用证开证")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-creditbusinessgrid-financeproductid-0']")
					sleep(1)
					input_enter("xpath", "//input[@id='combobox-input-creditbusinessgrid-financeproductid-0']")
					time.sleep(1)

					# 输入额度
					clear("xpath", "//input[@id='creditbusinessgrid-creditamount-0-input']")
					sleep(1)
					input("xpath", "//input[@id='creditbusinessgrid-creditamount-0-input']", "3000000")
					sleep(1)

					# 授信产品新增第二行
					click("xpath", "//span[text()='新增行']")
					sleep(1)

					# 选择授信产品
					click("xpath", "//input[@id='combobox-input-creditbusinessgrid-financeproductid-1']")
					sleep(1)
					input("xpath", "//input[@id='combobox-input-creditbusinessgrid-financeproductid-1']", "保函")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-creditbusinessgrid-financeproductid-1']")
					sleep(1)
					input_enter("xpath", "//input[@id='combobox-input-creditbusinessgrid-financeproductid-1']")
					time.sleep(1)

					# 输入额度
					clear("xpath", "//input[@id='creditbusinessgrid-creditamount-1-input']")
					sleep(1)
					input("xpath", "//input[@id='creditbusinessgrid-creditamount-1-input']", "3000000")
					sleep(1)

					# 点击授信方式tab页
					click("xpath", "//span[text()='授信方式']")
					sleep(1)
					# 授信方式新增第一行
					click("xpath", "//span[@title='授信方式']/ancestor::*[6]/following-sibling::*[2]/descendant::*[7]")
					sleep(1)

					# 选择授信方式
					click("xpath", "//input[@id='combobox-input-detailcontrolgrid-guaranteetype-0']")
					sleep(1)
					input("xpath", "//input[@id='combobox-input-detailcontrolgrid-guaranteetype-0']", "信用")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-detailcontrolgrid-guaranteetype-0']")
					sleep(1)
					input_enter("xpath", "//input[@id='combobox-input-detailcontrolgrid-guaranteetype-0']")
					time.sleep(1)

					# 输入额度
					clear("xpath", "//input[@id='detailcontrolgrid-creditamount-0-input']")
					sleep(1)
					input("xpath", "//input[@id='detailcontrolgrid-creditamount-0-input']", "300000")
					sleep(1)

					# 授信方式新增第二行

					click("xpath", "//span[@title='授信方式']/ancestor::*[6]/following-sibling::*[2]/descendant::*[7]")
					sleep(1)

					# 选择授信方式
					click("xpath", "//input[@id='combobox-input-detailcontrolgrid-guaranteetype-1']")
					sleep(1)
					input("xpath", "//input[@id='combobox-input-detailcontrolgrid-guaranteetype-1']", "抵押")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-detailcontrolgrid-guaranteetype-1']")
					sleep(1)
					input_enter("xpath", "//input[@id='combobox-input-detailcontrolgrid-guaranteetype-1']")
					time.sleep(1)

					# 输入额度
					clear("xpath", "//input[@id='detailcontrolgrid-creditamount-1-input']")
					sleep(1)
					input("xpath", "//input[@id='detailcontrolgrid-creditamount-1-input']", "300000")
					sleep(1)

				# 点击保存按钮
				click("xpath", "//span[text()='保存']")

				# 退出所有iframe窗体
				switch_default()

				# 用隐式等待方法等页面出现新增成功的提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				print("授信协议新增，保存成功！")
				time.sleep(3)

				if i == 1:
					switch_to("xpath", "//iframe[@id='credits-tab-iframe']")

					click("xpath",
					      "//div[contains(text(),'ZDHXYH')]/parent::*/preceding-sibling::*[2]/descendant::*[2]")
					# 点击审核按钮
					click("xpath", "//span[text()='审核']")
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'审核成功')]")
					print("授信协议，审核成功！")
					logging.info("授信协议，审核成功！")
					time.sleep(3)

					switch_to("xpath", "//iframe[@id='credits-tab-iframe']")

					click("xpath",
					      "//div[contains(text(),'ZDHXYH')]/parent::*/preceding-sibling::*[2]/descendant::*[2]")
					# 点击审核按钮
					click("xpath", "//span[text()='生效']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'授信合同生效成功！')]")
					print("授信协议，生效成功！")
					logging.info("授信协议，生效成功！")
					time.sleep(3)

				if i == 2:
					switch_to("xpath", "//iframe[@id='credits-tab-iframe']")

					click("xpath",
					      "//div[contains(text(),'ZDHZYFXYH')]/parent::*/preceding-sibling::*[2]/descendant::*[2]")
					# 点击审核按钮
					click("xpath", "//span[text()='审核']")
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'审核成功')]")
					print("授信协议，审核成功！")
					logging.info("授信协议，审核成功！")
					time.sleep(3)

					switch_to("xpath", "//iframe[@id='credits-tab-iframe']")

					click("xpath",
					      "//div[contains(text(),'ZDHZYFXYH')]/parent::*/preceding-sibling::*[2]/descendant::*[2]")
					# 点击审核按钮
					click("xpath", "//span[text()='生效']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'授信合同生效成功！')]")
					print("授信协议，生效成功！")
					logging.info("授信协议，生效成功！")
					time.sleep(3)

			switch_default()

			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='授信协议']/child::*[1]")

			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//span[text()='融资授信']")

			# 打印操作成功日志
			print("授信协议，操作成功!")
			logging.info("授信协议，操作成功!")
			time.sleep(2)
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("授信协议操作失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)

		logging.info("开始测试票据管理的页面功能")
		# 将页面的滚动条滑动到‘票据管理’页面的地方
		js_gd("xpath", "//span[contains(text(),'票据管理')]")
		# 用JS的方法点击票据管理菜单按钮
		js_click("xpath", "//span[contains(text(),'票据管理')]")


		# 测试承兑票据管理-应付票据管理
		try:
			# 点击承兑票据管理菜单
			click("xpath", "//span[@title='承兑汇票管理']")
			# 点击应收支票登记菜单
			click("xpath", "//span[@title='应付票据管理']")
			# 退出所有的iframe窗体
			switch_default()

			logging.info("开始测试应付票据管理功能")
			for i in range(1, 4):
				# 切入‘应付票据管理’的iframe窗体
				switch_to("xpath", "//iframe[@id='payDraftManage-tab-iframe']")

				# 用JS的方法点击新增按钮
				js_click("xpath", "//span[text()='新增']")

				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='addWin-iframe']")
				sleep(1)

				# 选择工程项目
				# 点击‘工程项目’框
				click("xpath", "//input[@id='combobox-input-projectitemid']")
				# 输入自动化测试工程项目，模糊查询
				input("xpath", "//input[@id='combobox-input-projectitemid']", "自动化测试工程项目")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-projectitemid']")
				input_enter("xpath", "//input[@id='combobox-input-projectitemid']")
				time.sleep(1)

				# 选择部门
				# 点击‘部门’框
				click("xpath", "//input[@id='combobox-input-deptid']")
				# 输入自动化测试工程项目，模糊查询
				input("xpath", "//input[@id='combobox-input-deptid']", "自动化测试部")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-deptid']")
				input_enter("xpath", "//input[@id='combobox-input-deptid']")
				time.sleep(1)

				# 选择票据类型
				# 第一次选择109-银行承兑汇票，第二次选择205-商业承兑汇票
				# 点击‘票据类型’框
				if i == 1:
					# 选择票据类型，点击‘票据类型’框
					# 第一次选择109-银行承兑汇票，第二次选择205-商业承兑汇票
					click("xpath", "//input[@id='combobox-input-drafttype']")
					input("xpath", "//input[@id='combobox-input-drafttype']", "109-银行承兑汇票")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-drafttype']")
					input_enter("xpath", "//input[@id='combobox-input-drafttype']")
					time.sleep(1)

					# 设置时间的变成存储，设置唯一性
					temp1 = time.strftime("%H%M%S")
					# 输入票据号
					click("xpath", "//span[text()='票据号']/ancestor::*[2]/descendant::*[6]/descendant::*[1]")
					sleep(1)
					input("xpath", "//span[text()='票据号']/ancestor::*[2]/descendant::*[6]/descendant::*[1]",
					      "YFPJ" + str(temp1))
					sleep(1)

					# 选择开票银行账户
					click("xpath", "//span[@title='开票银行账户']/parent::*/following-sibling::*[1]/descendant::*[3]")
					# 输入收票银行账户，模糊查询
					input("xpath", "//span[@title='开票银行账户']/parent::*/following-sibling::*[1]/descendant::*[3]", "中国银行")
					sleep(1)
					input_down("xpath", "//span[@title='开票银行账户']/parent::*/following-sibling::*[1]/descendant::*[3]")
					input_enter("xpath", "//span[@title='开票银行账户']/parent::*/following-sibling::*[1]/descendant::*[3]")
					time.sleep(1)

					# 选择承兑银行
					click("xpath", "//input[@id='combobox-input-paybankid']")
					# 输入收票银行账户，模糊查询
					input("xpath", "//input[@id='combobox-input-paybankid']", "中国银行")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-paybankid']")
					input_enter("xpath", "//input[@id='combobox-input-paybankid']")
					time.sleep(1)

					# 选择承兑开户银行
					click("xpath", "//input[@id='combobox-input-paybanklocationid']")
					# 输入承兑开户银行，模糊查询
					input("xpath", "//input[@id='combobox-input-paybanklocationid']", "上海市菊园新区")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-paybanklocationid']")
					input_enter("xpath", "//input[@id='combobox-input-paybanklocationid']")
					time.sleep(1)

					# 输入承兑开户银行(名)
					input("xpath", "//input[@id='paybanklocations']", "亚唐科技")
					sleep(2)

					# 选择外部收款单位
					click("xpath", "//span[@title='外部收款单位']/parent::*/following-sibling::*[1]/descendant::*[3]")
					# 输入银行名称，通过模糊匹配搜索
					input("xpath", "//span[@title='外部收款单位']/parent::*/following-sibling::*[1]/descendant::*[3]",
					      "Mindy自动化测试")
					sleep(1)

					# 输入付款期限
					click("xpath", "//input[@id='terms-input']")
					sleep(1)
					clear("xpath", "//input[@id='terms-input']")
					sleep(1)
					input("xpath", "//input[@id='terms-input']", "60")
					sleep(1)

					# 输入票面金额
					click("xpath", "//input[@id='draftamount-input']")
					sleep(1)
					clear("xpath", "//input[@id='draftamount-input']")
					sleep(1)
					input("xpath", "//input[@id='draftamount-input']", "2000")
					sleep(1)

					# 选择保证金担保方式
					click("xpath", "//input[@id='combobox-input-bailtype']")
					# 输入收票银行账户，模糊查询
					input("xpath", "//input[@id='combobox-input-bailtype']", "一定比例保证金")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-bailtype']")
					input_enter("xpath", "//input[@id='combobox-input-bailtype']")
					time.sleep(2)

					# 保证金
					click("xpath", "//input[@id='bailamount-input']")
					sleep(1)
					clear("xpath", "//input[@id='bailamount-input']")
					sleep(1)
					input("xpath", "//input[@id='bailamount-input']", "500")
					sleep(1)

					# 选择授信协议
					click("xpath", "//input[@id='combobox-input-creditid']")
					# 输入收票银行账户，模糊查询
					input("xpath", "//input[@id='combobox-input-creditid']", "ZDHXYH002")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-creditid']")
					input_enter("xpath", "//input[@id='combobox-input-creditid']")
					time.sleep(1)

					# 描述框中填入值
					input("xpath", "//textarea[@id='description']", "自动化测试应付票据描述框")
					sleep(1)

					# 点击保存按钮
					click("xpath", "//span[text()='保存']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("应付票据管理第%s次，保存成功！" % i)
					logging.info("应付票据管理第%s次，保存成功！" % i)
					time.sleep(3)

				else:
					# 选择票据类型，点击‘票据类型’框
					# 第一次选择109-银行承兑汇票，第二次选择205-商业承兑汇票
					click("xpath", "//input[@id='combobox-input-drafttype']")
					input("xpath", "//input[@id='combobox-input-drafttype']", "商业承兑汇票")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-drafttype']")
					input_enter("xpath", "//input[@id='combobox-input-drafttype']")
					time.sleep(1)

					# 设置时间的变成存储，设置唯一性
					temp1 = time.strftime("%H%M%S")
					# 输入票据号
					click("xpath", "//span[text()='票据号']/ancestor::*[2]/descendant::*[6]/descendant::*[1]")
					sleep(1)
					input("xpath", "//span[text()='票据号']/ancestor::*[2]/descendant::*[6]/descendant::*[1]",
					      "YFPJ" + str(temp1))
					sleep(1)

					# 选择开票银行账户
					click("xpath", "//span[@title='开票银行账户']/parent::*/following-sibling::*[1]/descendant::*[3]")
					# 输入收票银行账户，模糊查询
					input("xpath", "//span[@title='开票银行账户']/parent::*/following-sibling::*[1]/descendant::*[3]", "CNY")
					sleep(1)
					input_enter("xpath", "//span[@title='开票银行账户']/parent::*/following-sibling::*[1]/descendant::*[3]")
					sleep(1)
					input_down("xpath", "//span[@title='开票银行账户']/parent::*/following-sibling::*[1]/descendant::*[3]")
					sleep(1)
					input_enter("xpath", "//span[@title='开票银行账户']/parent::*/following-sibling::*[1]/descendant::*[3]")
					time.sleep(1)

					# 选择承兑方
					click("xpath", "//input[@id='acceptor']")
					# 输入收票银行账户，模糊查询
					input("xpath", "//input[@id='acceptor']", "Mindy自动化测试承兑方")
					sleep(1)
					input_down("xpath", "//input[@id='acceptor']")
					input_enter("xpath", "//input[@id='acceptor']")
					time.sleep(1)

					# 选择外部收款单位
					click("xpath",
					      "//input[@id='combobox-input-reccounterpartyid' and @class='f-combo-input f-input-bg  f-combo-input-noforceselect']")
					# 输入银行名称，通过模糊匹配搜索
					input("xpath",
					      "//input[@id='combobox-input-reccounterpartyid' and @class='f-combo-input f-input-bg  f-combo-input-noforceselect']",
					      "Mindy自动化测试")
					sleep(1)
					# 模拟回车
					double_click("xpath", "//div[contains(text(),'Mindy自动化测试')]")
					sleep(1)

					# 输入付款期限
					click("xpath", "//span[@title='付款期限']/ancestor::*[2]/descendant::*[8]")
					sleep(1)
					clear("xpath", "//span[@title='付款期限']/ancestor::*[2]/descendant::*[8]")
					sleep(1)
					input("xpath", "//span[@title='付款期限']/ancestor::*[2]/descendant::*[8]", "60")
					sleep(1)

					# 输入票面金额
					click("xpath", "//input[@id='draftamount-input']")
					sleep(1)
					clear("xpath", "//input[@id='draftamount-input']")
					sleep(1)
					input("xpath", "//input[@id='draftamount-input']", "1000")
					sleep(1)

					# 选择保证金担保方式
					click("xpath", "//input[@id='combobox-input-bailtype']")
					# 输入收票银行账户，模糊查询
					input("xpath", "//input[@id='combobox-input-bailtype']", "票据质押保证")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-bailtype']")
					input_enter("xpath", "//input[@id='combobox-input-bailtype']")
					time.sleep(1)

					# 选择抵质押物
					click("xpath", "//input[@id='combobox-input-collateralsid']")
					# 输入收票银行账户，模糊查询
					input("xpath", "//input[@id='combobox-input-collateralsid']", "抵押01")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-collateralsid']")
					input_enter("xpath", "//input[@id='combobox-input-collateralsid']")
					time.sleep(1)

					# 描述框中填入值
					input("xpath", "//textarea[@id='description']", "自动化测试应付票据描述框")
					sleep(1)

					# 点击保存按钮
					click("xpath", "//span[text()='保存']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("应付票据管理第%s次，保存成功！" % i)
					logging.info("应付票据管理第%s次，保存成功！" % i)
					time.sleep(3)

				# 第一笔，就先修改，再删除新建的‘应付票据管理’
				if i == 1:
					# 切入‘应付票据管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='payDraftManage-tab-iframe']")

					# 点击查看
					# 用JS的方法点击放大镜
					js_click("xpath", "//span[@class='f-contrac-close']")
					sleep(1)

					# 输入支票号：YFPJ
					input("xpath", "//input[@id='draftcode']", "YFPJ")
					sleep(1)

					# 点击查询
					click("xpath", "//span[text()='查询']")

					# 修改
					# 勾选
					click("xpath", "//div[contains(text(),'YFPJ')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 点击修改按钮
					click("xpath", "//span[text()='修改']")

					# 切入修改的iframe窗体
					switch_to("xpath", "//iframe[@id='modWin-iframe']")
					sleep(1)

					# 修改票面金额
					click("xpath", "//input[@id='draftamount-input']")
					sleep(1)
					# 清空内容
					clear("xpath", "//input[@id='draftamount-input']")
					sleep(1)
					# 输入金额
					input("xpath", "//input[@id='draftamount-input']", "800")
					sleep(1)

					# 备注框中输入新内容
					input("xpath", "//textarea[@id='description']", "修改应付票据管理备注内容")
					sleep(1)

					# 点击保存按钮
					click("xpath",
					      "//input[@id='combobox-input-projectitemid']/ancestor::*[10]/preceding-sibling::*[1]/descendant::*[3]")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("应付票据管理，修改成功！")
					logging.info("应付票据管理，修改成功！")
					time.sleep(3)

					# 第一次审核
					# 切入‘应付票据管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='payDraftManage-tab-iframe']")

					# 勾选
					click("xpath", "//div[contains(text(),'YFPJ')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 点击审核按钮
					click("xpath", "//span[text()='审核']")

					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("应付票据管理，第一次审核成功！")
					logging.info("应付票据管理，第一次审核成功！")
					time.sleep(3)

					# 票据出票
					# 切入‘应收支票管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='payDraftManage-tab-iframe']")

					# 勾选
					click("xpath", "//div[contains(text(),'YFPJ')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 用JS方便点击‘票据操作’按钮旁边的倒三角形
					js_click("xpath", "//span[text()='票据操作']/parent::*/following-sibling::*/child::*")
					sleep(1)

					# 点击票据出票按钮
					click("xpath", "//a[contains(text(),'票据出票')]")
					sleep(1)

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("应付票据管理，票据出票成功！")
					logging.info("应付票据管理，票据出票成功！")
					sleep(3)

					# 保证金登记
					switch_to("xpath", "//iframe[@id='payDraftManage-tab-iframe']")

					# 勾选
					click("xpath", "//div[contains(text(),'YFPJ')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 点击审核按钮
					js_click("xpath", "//span[text()='保证金登记']")
					sleep(1)

					# 切入保证金登记的窗体页面
					switch_to("xpath", "//iframe[@id='registerBailsWin-iframe']")

					# 点击保存钮
					click("xpath", "//span[text()='保证金登记']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("应付票据管理，票据保证金登记成功！")
					logging.info("应付票据管理，票据保证金登记成功！")
					sleep(3)

					# 取消出票
					# 切入‘应收支票管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='payDraftManage-tab-iframe']")

					# 勾选
					click("xpath", "//div[contains(text(),'YFPJ')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 用JS方便点击‘票据操作’按钮旁边的倒三角形
					js_click("xpath", "//span[text()='票据操作']/parent::*/following-sibling::*/child::*")
					sleep(1)

					# 点击取消票据背书按钮
					js_click("xpath", "//a[contains(text(),'取消出票')]")
					sleep(1)

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("应付票据管理，取消出票成功！")
					logging.info("应付票据管理，取消出票成功！")
					sleep(3)

					# 取消审核
					# 切入‘应付票据管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='payDraftManage-tab-iframe']")

					# 勾选
					click("xpath", "//div[contains(text(),'YFPJ')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 用JS方便点击‘审核’按钮旁边的倒三角形
					js_click("xpath", "//span[text()='审核']/parent::*/following-sibling::*/child::*")
					sleep(1)

					# 点击取消审核按钮
					js_click("xpath", "//a[contains(text(),'取消审核')]")
					sleep(1)

					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("应付票据管理，取消审核成功！")
					logging.info("应付票据管理，取消审核成功！")
					time.sleep(3)

					# 切入‘应付票据管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='payDraftManage-tab-iframe']")

					# 删除
					# 勾选
					click("xpath", "//div[contains(text(),'YFPJ')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 点击删除按钮
					click("xpath", "//span[text()='删除']")

					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现删除的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("应付票据管理，删除成功！")
					logging.info("应付票据管理，删除成功！")
					time.sleep(3)

				# 第二笔，先审核、再取消审核、再托收、再托收到账
				elif i == 2:

					# 第一次审核
					# 切入‘应付票据管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='payDraftManage-tab-iframe']")

					# 勾选
					click("xpath", "//div[contains(text(),'YFPJ')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 点击审核按钮
					click("xpath", "//span[text()='审核']")

					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("应付票据管理，第一次审核成功！")
					logging.info("应付票据管理，第一次审核成功！")
					time.sleep(3)

					# 取消审核
					# 切入‘应付票据管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='payDraftManage-tab-iframe']")

					# 勾选
					click("xpath", "//div[contains(text(),'YFPJ')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 用JS方便点击‘审核’按钮旁边的倒三角形
					js_click("xpath", "//span[text()='审核']/parent::*/following-sibling::*/child::*")
					sleep(1)

					# 点击取消审核按钮
					js_click("xpath", "//a[contains(text(),'取消审核')]")
					sleep(1)

					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("应付票据管理，取消审核成功！")
					logging.info("应付票据管理，取消审核成功！")
					time.sleep(3)

					# 第二次审核
					# 切入‘应收支票管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='payDraftManage-tab-iframe']")

					# 勾选
					click("xpath", "//div[contains(text(),'YFPJ')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 点击审核按钮
					click("xpath", "//span[text()='审核']")

					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("应付票据管理，第二次审核成功！")
					logging.info("应付票据管理，第二次审核成功！")
					time.sleep(3)

					# 票据出票
					# 切入‘应收支票管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='payDraftManage-tab-iframe']")

					# 勾选
					click("xpath", "//div[contains(text(),'YFPJ')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 用JS方便点击‘票据操作’按钮旁边的倒三角形
					js_click("xpath", "//span[text()='票据操作']/parent::*/following-sibling::*/child::*")
					sleep(1)

					# 点击票据出票按钮
					click("xpath", "//a[contains(text(),'票据出票')]")
					sleep(1)

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("应付票据管理，票据出票成功！")
					logging.info("应付票据管理，票据出票成功！")
					sleep(3)

					# 取消出票
					# 切入‘应收支票管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='payDraftManage-tab-iframe']")

					# 勾选
					click("xpath", "//div[contains(text(),'YFPJ')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 用JS方便点击‘票据操作’按钮旁边的倒三角形
					js_click("xpath", "//span[text()='票据操作']/parent::*/following-sibling::*/child::*")
					sleep(1)

					# 点击取消票据背书按钮
					js_click("xpath", "//a[contains(text(),'取消出票')]")
					sleep(1)

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("应付票据管理，取消出票成功！")
					logging.info("应付票据管理，取消出票成功！")
					sleep(3)

					# 票据出票
					# 切入‘应收支票管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='payDraftManage-tab-iframe']")

					# 勾选
					click("xpath", "//div[contains(text(),'YFPJ')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 用JS方便点击‘票据操作’按钮旁边的倒三角形
					js_click("xpath", "//span[text()='票据操作']/parent::*/following-sibling::*/child::*")
					sleep(1)

					# 点击票据出票按钮
					click("xpath", "//a[contains(text(),'票据出票')]")
					sleep(1)

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("应付票据管理，票据出票成功！")
					logging.info("应付票据管理，票据出票成功！")
					sleep(3)

					# # 保证贴现
					# # 切入‘应付票据管理’的iframe窗体
					# switch_to("xpath", "//iframe[@id='payDraftManage-tab-iframe']")
					#
					# # 勾选
					# click("xpath", "//div[contains(text(),'YFPJ')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")
					#
					# # 用JS方便点击‘票据操作’按钮旁边的倒三角形
					# js_click("xpath", "//span[text()='票据操作']/parent::*/following-sibling::*/child::*")
					# sleep(1)
					#
					# # 点击保证贴现按钮
					# js_click("xpath", "//a[contains(text(),'保证贴现')]")
					# sleep(1)
					#
					# # 切入保证贴现的窗体页面endorseWin-iframe
					# switch_to("xpath", "//iframe[@id='ensureDiscountWin-iframe']")
					#
					# # 授信协议
					# click("xpath", "//input[@id='usecreditamount-input' and @class='f-textField']/ancestor::*[5]/preceding-sibling::*[1]/descendant::*[8]")
					# # 输入被背书对象类型，模糊查询
					# input("xpath", "//input[@id='usecreditamount-input' and @class='f-textField']/ancestor::*[5]/preceding-sibling::*[1]/descendant::*[8]","ZDHXYH002")
					# sleep(1)
					# # 模拟回车
					# double_click("xpath", "//div[contains(text(),'ZDHXYH002')]")
					# sleep(1)
					#
					# # 点击保存钮
					# click("xpath", "//span[text()='保存']")
					#
					# # 退出所有iframe窗体
					# switch_default()
					#
					# # 用隐式等待方法等页面出现提示框
					# implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					# print("应付管理，票据保证贴现成功！")
					# logging.info("应付票据管理，票据保证贴现成功！")
					# sleep(3)
					#
					# # 取消保贴
					# # 切入‘应付票据管理’的iframe窗体
					# switch_to("xpath", "//iframe[@id='payDraftManage-tab-iframe']")
					#
					# # 勾选
					# click("xpath", "//div[contains(text(),'YFPJ')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")
					#
					# # 用JS方便点击‘票据操作’按钮旁边的倒三角形
					# js_click("xpath", "//span[text()='票据操作']/parent::*/following-sibling::*/child::*")
					# sleep(1)
					#
					# # 点击取消票据背书按钮
					# js_click("xpath", "//a[contains(text(),'取消保贴')]")
					# sleep(1)
					# # 点击弹出框的OK键
					# click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					# sleep(1)
					#
					# # 退出所有iframe窗体
					# switch_default()
					#
					# # 用隐式等待方法等页面出现提示框
					# implici_wait("xpath", "//span[contains(text(),'取消保贴成功！')]")
					# print("应付票据管理，取消保贴成功！")
					# logging.info("应付票据管理，取消保贴成功！")
					# sleep(3)

					# 到期付款
					# 切入‘应付票据管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='payDraftManage-tab-iframe']")

					# 勾选
					click("xpath", "//div[contains(text(),'YFPJ')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 用JS方便点击‘票据操作’按钮旁边的倒三角形
					js_click("xpath", "//span[text()='票据操作']/parent::*/following-sibling::*/child::*")
					sleep(1)

					# 点击到期付款按钮
					js_click("xpath", "//a[contains(text(),'到期付款')]")
					sleep(1)

					# 点击托收按钮
					click("xpath", "//span[text()='确定']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("应付票据管理，到期付款成功！")
					logging.info("应付票据管理，到期付款成功！")
					sleep(3)

					# 取消付款
					# 切入‘应付票据管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='payDraftManage-tab-iframe']")

					# 勾选
					click("xpath", "//div[contains(text(),'YFPJ')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 用JS方便点击‘票据操作’按钮旁边的倒三角形
					js_click("xpath", "//span[text()='票据操作']/parent::*/following-sibling::*/child::*")
					sleep(1)

					# 点击取消票据背书按钮
					js_click("xpath", "//a[contains(text(),'取消付款')]")
					sleep(1)

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("应付票据管理，取消付款成功！")
					logging.info("应付票据管理，取消付款成功！")
					sleep(3)

					# 退票
					# 切入‘应付票据管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='payDraftManage-tab-iframe']")

					# 勾选
					click("xpath", "//div[contains(text(),'YFPJ')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 用JS方便点击‘票据操作’按钮旁边的倒三角形
					js_click("xpath", "//span[text()='票据操作']/parent::*/following-sibling::*/child::*")
					sleep(1)

					# 点击退票按钮
					click("xpath", "//a[contains(text(),'退票')]")
					sleep(1)

					# 退出所有iframe窗体
					switch_default()
					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("应付票据管理，退票成功！")
					logging.info("应付票据管理，退票成功！")
					sleep(3)

					# 取消退票
					# 切入‘应付票据管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='payDraftManage-tab-iframe']")

					# 勾选
					click("xpath", "//div[contains(text(),'YFPJ')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 用JS方便点击‘票据操作’按钮旁边的倒三角形
					js_click("xpath", "//span[text()='票据操作']/parent::*/following-sibling::*/child::*")
					sleep(1)

					# 点击取消票据背书按钮
					js_click("xpath", "//a[contains(text(),'取消退票')]")
					sleep(1)

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("应付管理，取消退票成功！")
					logging.info("应付票据管理，取消退票成功！")
					sleep(3)

				# 第三笔，审核
				elif i == 3:

					# 操作记录查看
					# 切入‘应付票据管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='payDraftManage-tab-iframe']")

					# 勾选
					click("xpath", "//div[contains(text(),'YFPJ')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 点击审核按钮
					click("xpath", "//span[text()='审核']")

					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("应付票据管理，第三次审核成功！")
					logging.info("应付票据管理，第三次审核成功！")
					time.sleep(3)

					# 票据出票
					# 切入‘应收支票管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='payDraftManage-tab-iframe']")

					# 勾选
					click("xpath", "//div[contains(text(),'YFPJ')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 用JS方便点击‘票据操作’按钮旁边的倒三角形
					js_click("xpath", "//span[text()='票据操作']/parent::*/following-sibling::*/child::*")
					sleep(1)

					# 点击票据出票按钮
					click("xpath", "//a[contains(text(),'票据出票')]")
					sleep(1)

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("应付票据管理，票据出票成功！")
					logging.info("应付票据管理，票据出票成功！")
					sleep(3)

					# 到期付款
					# 切入‘应付票据管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='payDraftManage-tab-iframe']")

					# 勾选
					click("xpath", "//div[contains(text(),'YFPJ')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 用JS方便点击‘票据操作’按钮旁边的倒三角形
					js_click("xpath", "//span[text()='票据操作']/parent::*/following-sibling::*/child::*")
					sleep(1)

					# 点击到期付款按钮
					js_click("xpath", "//a[contains(text(),'到期付款')]")
					sleep(1)

					# 点击确定按钮
					click("xpath", "//span[text()='确定']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("应付票据管理，到期付款成功！")
					logging.info("应付票据管理，到期付款成功！")
					sleep(3)

					# 切入‘应付票据管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='payDraftManage-tab-iframe']")
					# 勾选
					click("xpath", "//div[contains(text(),'YFPJ')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 点击操作记录查看按钮
					click("xpath", "//span[text()='操作记录查看']")

					# 切入修改的iframe窗体
					switch_to("xpath", "//iframe[@id='operationWin-iframe']")
					sleep(1)
					click("xpath", "//div[@title='操作标识:承付']/parent::*/preceding-sibling::*[4]/descendant::*[2]")

					# 勾选
					js_click("xpath", "//span[(text()='生成交易单')]")
					sleep(1)
					switch_parent()
					switch_to("xpath", "//iframe[@id='otherPayWin-iframe']")
					sleep(1)

					# 部门
					click("xpath", "//input[@id='combobox-input-deptid']")
					# 输入银行名称，模糊查询
					input("xpath", "//input[@id='combobox-input-deptid']", "自动化测试部")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-deptid']")
					input_enter("xpath", "//input[@id='combobox-input-deptid']")
					time.sleep(1)

					# 交易类型
					click("xpath", "//input[@id='combobox-input-paytypeid']")
					# 输入银行名称，模糊查询
					input("xpath", "//input[@id='combobox-input-paytypeid']", "对外付款")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-paytypeid']")
					input_enter("xpath", "//input[@id='combobox-input-paytypeid']")
					time.sleep(1)

					# 交易类型
					click("xpath", "//input[@id='combobox-input-settlementmodeid']")
					# 输入银行名称，模糊查询
					input("xpath", "//input[@id='combobox-input-settlementmodeid']", "其他支付")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-settlementmodeid']")
					input_enter("xpath", "//input[@id='combobox-input-settlementmodeid']")
					time.sleep(1)

					# 付方账户
					click("xpath", "//input[@id='combobox-input-ourbankaccountid']")
					# 输入银行名称，模糊查询
					input("xpath", "//input[@id='combobox-input-ourbankaccountid']", "华夏银行")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-ourbankaccountid']")
					input_enter("xpath", "//input[@id='combobox-input-ourbankaccountid']")
					time.sleep(1)

					# 收方账户
					click("xpath", "//input[@id='combobox-input-oppcounterpartyaccountid']")
					# 输入银行名称，模糊查询
					input("xpath", "//input[@id='combobox-input-oppcounterpartyaccountid']", "CNY")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-oppcounterpartyaccountid']")
					input_enter("xpath", "//input[@id='combobox-input-oppcounterpartyaccountid']")
					time.sleep(1)

					# # 用途
					input("xpath", "//input[@id='combobox-input-purpose']", "TestPur001")
					sleep(1)

					# # 手续费
					click("xpath", "//input[@id='costs-input']")
					sleep(1)
					clear("xpath", "//input[@id='costs-input']")
					sleep(1)
					input("xpath", "//input[@id='costs-input']", "1000")
					sleep(1)

					# 计划项目
					click("xpath", "//input[@id='combobox-input-budgetitemid']")
					# 输入银行名称，模糊查询
					input("xpath", "//input[@id='combobox-input-budgetitemid']", "日常费用")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-budgetitemid']")
					input_enter("xpath", "//input[@id='combobox-input-budgetitemid']")
					time.sleep(1)

					# 资金类别
					click("xpath", "//input[@id='combobox-input-capitalcategoryid']")
					# 输入银行名称，模糊查询
					input("xpath", "//input[@id='combobox-input-capitalcategoryid']", "其他")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-capitalcategoryid']")
					input_enter("xpath", "//input[@id='combobox-input-capitalcategoryid']")
					time.sleep(1)

					# 现金流量项目
					click("xpath", "//input[@id='combobox-input-cashflowitemid']")
					# 输入银行名称，模糊查询
					input("xpath", "//input[@id='combobox-input-cashflowitemid']", "自动化测试现金流")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-cashflowitemid']")
					input_enter("xpath", "//input[@id='combobox-input-cashflowitemid']")
					time.sleep(1)

					# 短信通知
					input("xpath", "//input[@id='oppcellphone']", "178短信通知")
					sleep(1)

					# 邮件通知
					input("xpath", "//input[@id='oppemailaddress']", "1074658681@qq.com邮件通知")
					sleep(1)

					# 备注框中填入值
					input("xpath", "//textarea[@id='memo']", "自动化测试生成交易单备注框")
					sleep(1)

					# 点击确认保存
					click("xpath", "//span[text()='保存']")
					# 退出所有的iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现新增成功的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("操作记录查看，生成交易单保存成功！")
					sleep(3)

					switch_default()

					# 用JS的方法关闭当前页面
					js_click("xpath", "//a[@title='应付票据管理']/child::*[1]")

					# 再次点击基础设置菜单，使之关闭
					click("xpath", "//span[@title='承兑汇票管理']")

					# 打印操作成功日志
					print("应收票据管理，操作成功!")
					logging.info("应收票据管理，操作成功!")
					time.sleep(2)

					# 关联付款处理页面。查看交易单状态

					# 支票登记后去付款处理新增该账户的付款单
					logging.info("开始测试资金结算管理的页面功能")
					# 将页面的滚动条滑动到‘资金结算管理’页面的地方
					js_gd("xpath", "//span[contains(text(),'资金结算管理')]")
					# 用JS的方法点击资金结算管理菜单按钮
					js_click("xpath", "//span[contains(text(),'资金结算管理')]")

					# 点击资金系统收付菜单
					click("xpath", "//span[@title='资金系统收付']")
					# 点击应付支票领用菜单
					click("xpath", "//span[@title='付款处理']")
					# 退出所有的iframe窗体
					switch_default()

					logging.info("开始测试付款处理功能")

					# 切入‘付款处理’的iframe窗体
					switch_to("xpath", "//iframe[@id='generalPayment-tab-iframe']")

					# 点击支票支付tab页
					click("xpath", "//span[text()='其他支付']")

					# 切入‘支票支付’的iframe窗体
					switch_to("xpath", "//iframe[@id='subTabEight-iframe']")
					sleep(1)

					# 选择新建的付款单
					click("xpath",
					      "//div[@title='付款金额:1,000.00']/parent::*[1]/preceding-sibling::*[7]/descendant::*[2]")

					# 点击送审按钮
					click("xpath", "//span[text()='作废']")

					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					sleep(1)

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("付款处理，其他支付作废成功！")
					logging.info("付款处理，其他支付作废成功！")
					time.sleep(3)

					switch_default()

					# 用JS的方法关闭当前页面
					js_click("xpath", "//a[@title='付款处理']/child::*[1]")

					# 再次点击基础设置菜单，使之关闭
					click("xpath", "//span[@title='资金系统收付']")

					# 打印操作成功日志
					print("付款处理，作废操作成功!")
					logging.info("付款处理，作废操作成功!")
					time.sleep(2)

					logging.info("开始测试票据管理的页面功能")
					# 将页面的滚动条滑动到‘票据管理’页面的地方
					# js_gd("xpath", "//span[contains(text(),'票据管理')]")
					# 用JS的方法点击票据管理菜单按钮
					js_click("xpath", "//span[contains(text(),'票据管理')]")

					# 测试承兑票据管理-应收票据管理
					# 点击承兑票据管理菜单
					click("xpath", "//span[@title='承兑汇票管理']")
					# 点击应收支票登记菜单
					click("xpath", "//span[@title='应付票据管理']")
					# 退出所有的iframe窗体
					switch_default()

					# 操作记录查看
					# 切入‘应付票据管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='payDraftManage-tab-iframe']")
					# 勾选
					click("xpath", "//div[contains(text(),'YFPJ')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 点击操作记录查看按钮
					click("xpath", "//span[text()='操作记录查看']")

					# 切入修改的iframe窗体
					switch_to("xpath", "//iframe[@id='operationWin-iframe']")
					sleep(1)
					click("xpath", "//div[@title='操作标识:承付']/parent::*/preceding-sibling::*[4]/descendant::*[2]")

					# 勾选
					js_click("xpath", "//span[(text()='生成交易单')]")
					sleep(1)

					switch_parent()
					switch_to("xpath", "//iframe[@id='otherPayWin-iframe']")
					sleep(1)

					# 部门
					click("xpath", "//input[@id='combobox-input-deptid']")
					# 输入银行名称，模糊查询
					input("xpath", "//input[@id='combobox-input-deptid']", "自动化测试部")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-deptid']")
					input_enter("xpath", "//input[@id='combobox-input-deptid']")
					time.sleep(1)

					# 交易类型
					click("xpath", "//input[@id='combobox-input-paytypeid']")
					# 输入银行名称，模糊查询
					input("xpath", "//input[@id='combobox-input-paytypeid']", "对外付款")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-paytypeid']")
					input_enter("xpath", "//input[@id='combobox-input-paytypeid']")
					time.sleep(1)

					# 交易类型
					click("xpath", "//input[@id='combobox-input-settlementmodeid']")
					# 输入银行名称，模糊查询
					input("xpath", "//input[@id='combobox-input-settlementmodeid']", "其他支付")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-settlementmodeid']")
					input_enter("xpath", "//input[@id='combobox-input-settlementmodeid']")
					time.sleep(1)

					# 付方账户
					click("xpath", "//input[@id='combobox-input-ourbankaccountid']")
					# 输入银行名称，模糊查询
					input("xpath", "//input[@id='combobox-input-ourbankaccountid']", "华夏银行")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-ourbankaccountid']")
					input_enter("xpath", "//input[@id='combobox-input-ourbankaccountid']")
					time.sleep(1)

					# 收方账户
					click("xpath", "//input[@id='combobox-input-oppcounterpartyaccountid']")
					# 输入银行名称，模糊查询
					input("xpath", "//input[@id='combobox-input-oppcounterpartyaccountid']", "CNY")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-oppcounterpartyaccountid']")
					input_enter("xpath", "//input[@id='combobox-input-oppcounterpartyaccountid']")
					time.sleep(1)

					# 用途
					input("xpath", "//input[@id='combobox-input-purpose']", "TestPur001")
					sleep(1)

					# 手续费
					click("xpath", "//input[@id='costs-input']")
					sleep(1)
					clear("xpath", "//input[@id='costs-input']")
					sleep(1)
					input("xpath", "//input[@id='costs-input']", "1000")
					sleep(1)

					# 计划项目
					click("xpath", "//input[@id='combobox-input-budgetitemid']")
					# 输入银行名称，模糊查询
					input("xpath", "//input[@id='combobox-input-budgetitemid']", "日常费用")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-budgetitemid']")
					input_enter("xpath", "//input[@id='combobox-input-budgetitemid']")
					time.sleep(1)

					# 资金类别
					click("xpath", "//input[@id='combobox-input-capitalcategoryid']")
					# 输入银行名称，模糊查询
					input("xpath", "//input[@id='combobox-input-capitalcategoryid']", "其他")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-capitalcategoryid']")
					input_enter("xpath", "//input[@id='combobox-input-capitalcategoryid']")
					time.sleep(1)

					# 现金流量项目
					click("xpath", "//input[@id='combobox-input-cashflowitemid']")
					# 输入银行名称，模糊查询
					input("xpath", "//input[@id='combobox-input-cashflowitemid']", "自动化测试现金流")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-cashflowitemid']")
					input_enter("xpath", "//input[@id='combobox-input-cashflowitemid']")
					time.sleep(1)

					# 短信通知
					input("xpath", "//input[@id='oppcellphone']", "178短信通知")
					sleep(1)

					# 邮件通知
					input("xpath", "//input[@id='oppemailaddress']", "1074658681@qq.com邮件通知")
					sleep(1)

					# 备注框中填入值
					input("xpath", "//textarea[@id='memo']", "自动化测试生成交易单备注框")
					sleep(1)

					# 点击确认保存
					click("xpath", "//span[text()='保存']")
					# 退出所有的iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现新增成功的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("操作记录查看，生成交易单保存成功！")
					sleep(3)

			# 退出所有iframe窗体
			switch_default()

			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='应付票据管理']/child::*[1]")

			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//span[@title='承兑汇票管理']")

			# 打印操作成功日志
			print("应付票据管理，操作成功!")
			logging.info("应付票据管理，操作成功!")
			time.sleep(2)

		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("应付票据管理,失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)

		# 测试应收票据查看
		try:
			# 点击承兑票据管理菜单
			click("xpath", "//span[@title='承兑汇票管理']")
			# 点击应收支票登记菜单
			click("xpath", "//span[@title='应收票据查看']")
			# 退出所有的iframe窗体
			switch_default()
			logging.info("开始测试应收票据查看功能")
			# 切入‘应收票据查看’的iframe窗体
			switch_to("xpath", "//iframe[@id='recDraftView-tab-iframe']")
			sleep(1)
			switch_to("xpath", "//iframe[@id='subTabOne-iframe']")
			sleep(1)
			# 点击查看
			# 用JS的方法点击放大镜
			js_click("xpath", "//span[@class='f-contrac-close']")
			sleep(1)

			click("xpath",
			      "//input[ @id='combobox-input-recaccountid']/ancestor::*[3]/preceding-sibling::*[5]/descendant::*[6]")

			# 输入内容
			input("xpath",
			      "//input[ @id='combobox-input-recaccountid']/ancestor::*[3]/preceding-sibling::*[5]/descendant::*[6]",
			      "PJH")
			sleep(1)

			# 点击查询
			click("xpath", "//span[text()='查询']")

			# 用隐式等待方法等页面出现预期数据：背书单位前手名称:自动化测试背书单位前手名称
			implici_wait("xpath", "//div[@title='背书单位前手名称:自动化测试背书单位前手名称']")
			print("应收票据，票据信息查看成功！")
			time.sleep(3)

			# 退出所有iframe窗体
			switch_default()

			logging.info("现在开始测试应收票据操作查看功能")
			# 切入‘应收票据查看’的iframe窗体
			switch_to("xpath", "//iframe[@id='recDraftView-tab-iframe']")
			sleep(1)

			click("xpath", "//span[text()='票据操作查看']")
			sleep(1)

			switch_to("xpath", "//iframe[@id='subTabTwo-iframe']")
			sleep(1)
			# 点击查看
			# 用JS的方法点击放大镜
			js_click("xpath", "//span[@class='f-contrac-close']")
			sleep(1)

			click("xpath",
			      "//input[@id='combobox-input-operateflag']/ancestor::*[3]/following-sibling::*[1]/descendant::*[6]")
			# 输入内容
			input("xpath",
			      "//input[@id='combobox-input-operateflag']/ancestor::*[3]/following-sibling::*[1]/descendant::*[6]",
			      "PJH")
			sleep(1)

			# 确认回车
			input_enter("xpath",
			            "//input[@id='combobox-input-operateflag']/ancestor::*[3]/following-sibling::*[1]/descendant::*[6]")

			# 点击查询
			click("xpath", "//span[text()='查询']")
			sleep(1)

			click("xpath", "//div[@title='操作标识:收票']/parent::*[1]/preceding-sibling::*[4]/descendant::*[2]")
			sleep(1)

			js_click("xpath", "//span[text()='合并生成收票交易单']")
			sleep(1)
			switch_to("xpath", "//iframe[@id='receiveGenRecmentWin-iframe']")

			# mysql和oracle版本在交易类型数据带出时有区别，因此自动化选择数据combobox-input-paytypeid
			# 部门
			click("xpath", "//input[@id='combobox-input-paytypeid']")
			sleep(1)
			clear("xpath", "//input[@id='combobox-input-paytypeid']")
			sleep(1)
			# 输入交易类型名称，模糊查询
			input("xpath", "//input[@id='combobox-input-paytypeid']", "201-外部收款")
			sleep(1)
			input_down("xpath", "//input[@id='combobox-input-paytypeid']")
			input_enter("xpath", "//input[@id='combobox-input-paytypeid']")
			time.sleep(1)

			# 收方账户
			click("xpath", "//input[@id='combobox-input-ourbankaccountid']")
			# 输入银行名称，模糊查询
			input("xpath", "//input[@id='combobox-input-ourbankaccountid']", "中国银行")
			sleep(1)
			input_down("xpath", "//input[@id='combobox-input-ourbankaccountid']")
			input_enter("xpath", "//input[@id='combobox-input-ourbankaccountid']")
			time.sleep(1)

			# 部门
			click("xpath", "//input[@id='combobox-input-deptid']")
			# 输入银行名称，模糊查询
			input("xpath", "//input[@id='combobox-input-deptid']", "自动化测试部")
			sleep(1)
			input_down("xpath", "//input[@id='combobox-input-deptid']")
			input_enter("xpath", "//input[@id='combobox-input-deptid']")
			time.sleep(1)

			# 计划项目
			click("xpath", "//input[@id='combobox-input-budgetitemid']")
			# 输入银行名称，模糊查询
			input("xpath", "//input[@id='combobox-input-budgetitemid']", "自动化计划项目")
			sleep(1)
			input_down("xpath", "//input[@id='combobox-input-budgetitemid']")
			input_enter("xpath", "//input[@id='combobox-input-budgetitemid']")
			time.sleep(1)

			# 现金流量项目
			click("xpath", "//input[@id='combobox-input-cashflowitemid']")
			# 输入银行名称，模糊查询
			input("xpath", "//input[@id='combobox-input-cashflowitemid']", "自动化测试现金流")
			sleep(1)
			input_down("xpath", "//input[@id='combobox-input-cashflowitemid']")
			input_enter("xpath", "//input[@id='combobox-input-cashflowitemid']")
			time.sleep(1)

			# 资金类别
			click("xpath", "//input[@id='combobox-input-capitalcategoryid']")
			# 输入银行名称，模糊查询
			input("xpath", "//input[@id='combobox-input-capitalcategoryid']", "其他")
			sleep(1)
			input_down("xpath", "//input[@id='combobox-input-capitalcategoryid']")
			input_enter("xpath", "//input[@id='combobox-input-capitalcategoryid']")
			time.sleep(1)

			# 工程项目
			click("xpath", "//input[@id='combobox-input-projectitemid']")
			# 输入银行名称，通过模糊匹配搜索
			input("xpath", "//input[@id='combobox-input-projectitemid']", "自动化测试工程项目")
			sleep(1)
			# 模拟回车
			double_click("xpath", "//div[contains(text(),'自动化测试工程项目')]")
			sleep(1)

			# 合同号
			input("xpath", "//input[@id='contractnumber']", "自动化合同号")
			sleep(1)
			click("xpath", "//span[text()='确认']")
			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			sleep(3)
			print("应付票据查看，合并生成收票交易单成功！")
			logging.info("应付票据查看，合并生成收票交易单成功！")
			switch_default()

			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='应收票据查看']/child::*[1]")

			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//span[@title='承兑汇票管理']")

			# 打印操作成功日志
			print("应收票据查看，操作成功!")
			logging.info("应收票据查看，操作成功!")
			time.sleep(2)

		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("应付票据查看,失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)

		# 测试应付票据查看
		try:
			# 点击承兑票据管理菜单
			click("xpath", "//span[@title='承兑汇票管理']")
			# 点击应收支票登记菜单
			click("xpath", "//span[@title='应付票据查看']")
			# 退出所有的iframe窗体
			switch_default()
			logging.info("开始测试应付票据查看功能")
			# 切入‘应收票据查看’的iframe窗体
			switch_to("xpath", "//iframe[@id='payDraftView-tab-iframe']")
			sleep(1)
			switch_to("xpath", "//iframe[@id='subTabOne-iframe']")
			sleep(1)
			# 点击查看
			# 用JS的方法点击放大镜
			js_click("xpath", "//span[@class='f-contrac-close']")
			sleep(1)

			click("xpath",
			      "//input[@id='combobox-input-payaccountid']/ancestor::*[3]/preceding-sibling::*[5]/descendant::*[6]")

			# 输入内容
			input("xpath",
			      "//input[@id='combobox-input-payaccountid']/ancestor::*[3]/preceding-sibling::*[5]/descendant::*[6]",
			      "YFPJ")
			sleep(1)

			# 点击查询
			click("xpath", "//span[text()='查询']")

			# 用隐式等待方法等页面出现预期数据：承兑方:Mindy自动化测试承兑方
			implici_wait("xpath", "//div[@title='承兑方:Mindy自动化测试承兑方']")
			print("应付票据，票据信息查看成功！")
			time.sleep(3)

			# 退出所有iframe窗体
			switch_default()

			logging.info("现在开始测试应收票据操作查看功能")
			# 切入‘应收票据查看’的iframe窗体
			switch_to("xpath", "//iframe[@id='payDraftView-tab-iframe']")
			sleep(1)

			click("xpath", "//span[text()='票据操作查看']")
			sleep(1)

			switch_to("xpath", "//iframe[@id='subTabTwo-iframe']")
			sleep(1)
			# 点击查看
			# 用JS的方法点击放大镜
			js_click("xpath", "//span[@class='f-contrac-close']")
			sleep(1)

			click("xpath",
			      "//input[@id='combobox-input-operateflag']/ancestor::*[3]/following-sibling::*[1]/descendant::*[6]")
			# 输入内容
			input("xpath",
			      "//input[@id='combobox-input-operateflag']/ancestor::*[3]/following-sibling::*[1]/descendant::*[6]",
			      "YFPJ")
			sleep(1)

			click("xpath", "//span[text()='查询']")

			# 用隐式等待方法等页面出现预期数据：操作标识:承付
			implici_wait("xpath", "//div[@title='操作标识:承付']")
			print("应付票据，票据操作查看成功！")
			time.sleep(3)
			switch_default()

			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='应付票据查看']/child::*[1]")

			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//span[@title='承兑汇票管理']")

			# 打印操作成功日志
			print("应付票据查看，操作成功!")
			logging.info("应付票据支票查看，操作成功!")
			time.sleep(2)

		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("应付票据查看,失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)

		# 测试托管票据查看
		try:
			# 点击承兑票据管理菜单
			click("xpath", "//span[@title='承兑汇票管理']")
			# 点击应收支票登记菜单
			click("xpath", "//span[@title='托管票据查看']")
			# 退出所有的iframe窗体
			switch_default()
			logging.info("开始测试托管票据查看功能")
			# 切入‘应收票据查看’的iframe窗体
			switch_to("xpath", "//iframe[@id='depositview-tab-iframe']")
			sleep(1)
			switch_to("xpath", "//iframe[@id='subTabOne-iframe']")
			sleep(1)
			# 点击查看
			# 用JS的方法点击放大镜
			js_click("xpath", "//span[@class='f-contrac-close']")
			sleep(1)

			click("xpath", "//input[@id='draftcode']")

			# 输入内容
			input("xpath", "//input[@id='draftcode']", "YFPJ")
			sleep(1)

			# 点击查询
			click("xpath", "//span[text()='查询']")

			# 用隐式等待方法等页面出现预期数据：承兑方:Mindy自动化测试承兑方
			implici_wait("xpath", "//div[@title='承兑方:Mindy自动化测试承兑方']")
			print("应付票据，托管应付票据查看成功！")
			time.sleep(3)

			# 退出所有iframe窗体
			switch_default()

			logging.info("现在开始测试应收票据操作查看功能")
			# 切入‘应收票据查看’的iframe窗体
			switch_to("xpath", "//iframe[@id='depositview-tab-iframe']")
			sleep(1)

			click("xpath", "//span[text()='托管应收票据查看']")
			sleep(1)

			switch_to("xpath", "//iframe[@id='subTabTwo-iframe']")
			sleep(1)
			# 点击查看
			# 用JS的方法点击放大镜
			js_click("xpath", "//span[@class='f-contrac-close']")
			sleep(1)

			click("xpath",
			      "//input[@id='combobox-input-recaccountid']/ancestor::*[3]/preceding-sibling::*[5]/descendant::*[6]")
			# 输入内容
			input("xpath",
			      "//input[@id='combobox-input-recaccountid']/ancestor::*[3]/preceding-sibling::*[5]/descendant::*[6]",
			      "PJH")
			sleep(1)
			# 点击查询
			click("xpath", "//span[text()='查询']")

			# 用隐式等待方法等页面出现预期数据：外部给票单位:Mindy自动化测试
			implici_wait("xpath", "//div[@title='外部给票单位:Mindy自动化测试']")
			print("应付票据，票据操作查看成功！")
			time.sleep(3)
			switch_default()

			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='托管票据查看']/child::*[1]")

			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//span[@title='承兑汇票管理']")

			# 打印操作成功日志
			print("应付票据查看，操作成功!")
			logging.info("应付票据查看，操作成功!")
			time.sleep(2)

		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("应付票据查看,失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)

		# 测试信用证管理-信用证收证管理
		try:
			# 点击承兑票据管理菜单
			click("xpath", "//span[@title='信用证管理']")
			# 点击应收支票登记菜单
			click("xpath", "//span[@title='信用证收证管理']")
			# 退出所有的iframe窗体
			switch_default()
			logging.info("开始测试信用证收证管理功能")
			for i in range(1, 3):
				# 切入‘信用证收证管理’的iframe窗体
				switch_to("xpath", "//iframe[@id='expLOCredits-tab-iframe']")
				# 用JS的方法点击新增按钮
				js_click("xpath", "//span[text()='新增']")
				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='addWin-iframe']")
				sleep(1)

				# 选择部门
				# 点击‘部门’框
				click("xpath",
				      "//input[@id='combobox-input-credittypeid']/ancestor::*[4]/preceding-sibling::*[1]/descendant::*[7]")
				# 输入自动化测试工程项目，模糊查询
				input("xpath",
				      "//input[@id='combobox-input-credittypeid']/ancestor::*[4]/preceding-sibling::*[1]/descendant::*[7]",
				      "自动化测试部")
				sleep(1)
				input_down("xpath",
				           "//input[@id='combobox-input-credittypeid']/ancestor::*[4]/preceding-sibling::*[1]/descendant::*[7]")
				input_enter("xpath",
				            "//input[@id='combobox-input-credittypeid']/ancestor::*[4]/preceding-sibling::*[1]/descendant::*[7]")
				time.sleep(1)

				# 选择融资产品
				# 点击‘融资产品’框
				click("xpath", "//input[@id='combobox-input-credittypeid']")
				# 输入信用证类型，模糊查询
				input("xpath", "//input[@id='combobox-input-credittypeid']", "104-信用证收证")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-credittypeid']")
				input_enter("xpath", "//input[@id='combobox-input-credittypeid']")
				time.sleep(1)

				# 设置时间的变成存储，变成
				temp1 = time.strftime("%H%M%S")
				# 输入票据号
				click("xpath", "//span[text()='信用证号码']/ancestor::*[2]/descendant::*[6]/descendant::*[1]")
				sleep(1)
				input("xpath", "//span[text()='信用证号码']/ancestor::*[2]/descendant::*[6]/descendant::*[1]",
				      "XYZ" + str(temp1))
				sleep(1)

				# 输入开证金额
				input("xpath", "//span[text()='开证金额']/ancestor::*[2]/descendant::*[8]", "600000")
				sleep(1)

				# 输入开证币种
				click("xpath", "//input[@id='combobox-input-currencyid']")
				sleep(1)
				input("xpath", "//input[@id='combobox-input-currencyid']", "CNY-人民币")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-currencyid']")
				input_enter("xpath", "//input[@id='combobox-input-currencyid']")
				time.sleep(1)

				# 输入开证方
				input("xpath", "//input[@id='issuefactory']", "自动化测试开证方")
				sleep(1)

				# 折美元金额
				click("xpath", "//input[@id='dollaramount-input']")
				sleep(1)
				clear("xpath", "//input[@id='dollaramount-input']")
				sleep(1)
				input("xpath", "//input[@id='dollaramount-input']", "360000")
				sleep(1)

				# 输入收到日期
				today = date.today()
				receivedate = today + timedelta(days=60)
				click("xpath", "//input[@id='receivedate-input']")
				sleep(1)
				input("xpath", "//input[@id='receivedate-input']", str(receivedate))
				# 模拟回车键
				keyDown('enter')
				keyUp('enter')
				time.sleep(1)
				if i == 2:
					click("xpath", "//input[@id='isforwards']")

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

				# 输入交单日期
				today = date.today()
				deliverydate = today + timedelta(days=720)
				click("xpath", "//input[@id='deliverydate-input']")
				sleep(1)
				input("xpath", "//input[@id='deliverydate-input']", str(deliverydate))
				# 模拟回车键
				keyDown('enter')
				keyUp('enter')
				time.sleep(1)

				# 输入应收汇日期
				today = date.today()
				deliverydate = today + timedelta(days=720)
				click("xpath", "//input[@id='receivabledate-input']")
				sleep(1)
				input("xpath", "//input[@id='receivabledate-input']", str(deliverydate))
				# 模拟回车键
				keyDown('enter')
				keyUp('enter')
				time.sleep(1)

				# 输入通知银行
				click("xpath", "//input[@id='combobox-input-advisingbankid']")
				sleep(1)
				input("xpath", "//input[@id='combobox-input-advisingbankid']", "中国银行")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-advisingbankid']")
				input_enter("xpath", "//input[@id='combobox-input-advisingbankid']")
				time.sleep(1)

				# 输入付款单位
				input("xpath", "//input[@id='payname']", "Mindy科技有限公司")
				sleep(1)

				# 输入溢短
				click("xpath", "//input[@id='overflowratio-input']")
				sleep(1)
				clear("xpath", "//input[@id='overflowratio-input']")
				sleep(1)
				input("xpath", "//input[@id='overflowratio-input']", "20")
				sleep(1)

				# 输入客户
				input("xpath", "//input[@id='customer']", "Mindy自动化测试客户")
				sleep(1)

				# 缺少附件上传功能

				# 点击保存按钮
				click("xpath", "//span[text()='保存']")

				# 退出所有iframe窗体
				switch_default()

				# 用隐式等待方法等页面出现提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				print("信用证收证管理第%s次，保存成功！" % i)
				logging.info("信用证收证管理第%s次，保存成功！" % i)
				time.sleep(3)

				# 第一笔，就先修改，再删除新建的‘应收票据管理’
				if i == 1:
					# 切入‘应收票据管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='expLOCredits-tab-iframe']")

					# 点击查看
					# 用JS的方法点击放大镜
					js_click("xpath", "//span[@class='f-contrac-close']")
					sleep(1)

					# 输入支票号：XYZ
					input("xpath", "//input[@id='creditnumber']", "XYZ")
					sleep(1)

					# 点击查询
					click("xpath", "//span[text()='查询']")

					# 修改
					# 勾选
					click("xpath", "//div[contains(text(),'XYZ')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 点击修改按钮
					click("xpath", "//span[text()='修改']")

					# 切入修改的iframe窗体
					switch_to("xpath", "//iframe[@id='modWin-iframe']")
					sleep(1)

					# 修改开证金额
					click("xpath", "//input[@id='amount-input']")
					sleep(1)
					clear("xpath", "//input[@id='amount-input']")
					sleep(1)
					input("xpath", "//input[@id='amount-input']", "20000000")
					sleep(1)

					# 输入溢短
					click("xpath", "//input[@id='overflowratio-input']")
					sleep(1)
					clear("xpath", "//input[@id='overflowratio-input']")
					sleep(1)
					input("xpath", "//input[@id='overflowratio-input']", "20")
					sleep(1)

					# 点击保存按钮
					click("xpath", "//span[text()='保存']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("信用证收证管理，修改成功！")
					logging.info("信用证收证管理，修改成功！")
					time.sleep(3)

					# 切入‘信用证收证管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='expLOCredits-tab-iframe']")

					# 删除
					# 勾选
					click("xpath", "//div[contains(text(),'XYZ')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 点击删除按钮
					click("xpath", "//span[text()='删除']")

					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现删除的提示框
					implici_wait("xpath", "//span[contains(text(),'信用证收证成功删除1条!')]")
					print("信用证收证管理，删除成功！")
					logging.info("信用证收证管理，删除成功！")
					time.sleep(3)

				# 第二笔，先审核、再取消审核、再托收、再托收到账
				elif i == 2:

					# 第一次审核
					# 切入‘信用证收证管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='expLOCredits-tab-iframe']")

					# 勾选
					click("xpath", "//div[contains(text(),'XYZ')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 点击审核按钮
					click("xpath", "//span[text()='审核']")

					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'审核成功！')]")
					print("信用证收证管理，第一次审核成功！")
					logging.info("信用证收证管理，第一次审核成功！")
					time.sleep(3)

					# 取消审核
					# 切入‘信用证收证管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='expLOCredits-tab-iframe']")

					# 勾选
					click("xpath", "//div[contains(text(),'XYZ')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 用JS方便点击‘审核’按钮旁边的倒三角形
					js_click("xpath", "//span[text()='审核']/parent::*/following-sibling::*/child::*")
					sleep(1)

					# 点击取消审核按钮
					js_click("xpath", "//a[contains(text(),'取消审核')]")
					sleep(1)

					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'取消审核成功！')]")
					print("信用证收证管理，取消审核成功！")
					logging.info("信用证收证管理，取消审核成功！")
					time.sleep(3)

					# 第二次审核
					# 切入‘信用证收证管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='expLOCredits-tab-iframe']")

					# 勾选
					click("xpath", "//div[contains(text(),'XYZ')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 点击审核按钮
					click("xpath", "//span[text()='审核']")

					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'审核成功！')]")
					print("信用证收证管理，第二次审核成功！")
					logging.info("信用证收证管理，第二次审核成功！")
					time.sleep(3)

					# 交单
					# 切入‘信用证收证管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='expLOCredits-tab-iframe']")

					# 勾选
					click("xpath", "//div[contains(text(),'XYZ')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 用JS方便点击‘交单’
					js_click("xpath", "//span[text()='交单']")
					sleep(1)

					# 切入交单的窗体页面endorseWin-iframe
					switch_to("xpath", "//iframe[@id='deliverWin-iframe']")

					# 点击确定按钮
					click("xpath", "//span[text()='保存']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'交单成功！')]")
					print("信用证收证管理，交单成功！")
					logging.info("信用证收证管理，交单成功！")
					sleep(3)

					# 取消交单
					# 切入‘信用证收证管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='expLOCredits-tab-iframe']")

					# 勾选
					click("xpath", "//div[contains(text(),'XYZ')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 用JS方便点击‘交单’按钮旁边的倒三角形
					js_click("xpath", "//span[text()='交单']/parent::*/following-sibling::*/child::*")
					sleep(1)

					# 点击取消交单按钮
					js_click("xpath", "//a[contains(text(),'取消交单')]")
					sleep(1)
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'取消交单成功！')]")
					print("信用证收证管理，取消交单成功！")
					logging.info("信用证收证管理，取消交单成功！")
					sleep(3)

					# 交单
					# 切入‘信用证收证管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='expLOCredits-tab-iframe']")

					# 勾选
					click("xpath", "//div[contains(text(),'XYZ')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 用JS方便点击‘交单’
					js_click("xpath", "//span[text()='交单']")
					sleep(1)

					# 切入交单的窗体页面endorseWin-iframe
					switch_to("xpath", "//iframe[@id='deliverWin-iframe']")
					sleep(1)

					# 点击确定按钮
					click("xpath", "//span[text()='保存']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'交单成功！')]")
					print("信用证收证管理，交单成功！")
					logging.info("信用证收证管理，交单成功！")
					sleep(3)

					# 到单处理--客户承兑
					# 切入‘信用证收证管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='expLOCredits-tab-iframe']")

					# 勾选
					click("xpath", "//div[contains(text(),'XYZ')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 用JS方便点击‘到单处理’按钮旁边的倒三角形
					js_click("xpath", "//span[text()='到单处理']/parent::*/following-sibling::*/child::*")
					sleep(1)

					# 点击到单处理按钮
					js_click("xpath", "//a[contains(text(),'客户承兑')]")
					sleep(1)

					# 切入收汇的窗体页面endorseWin-iframe
					switch_to("xpath", "//iframe[@id='opWin-iframe']")

					# 点击保存按钮
					click("xpath", "//span[text()='保存']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("信用证开证管理，客户承兑成功！")
					logging.info("信用证开证管理，客户承兑成功！")
					sleep(3)

					# 到单处理--收汇
					# 切入‘信用证收证管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='expLOCredits-tab-iframe']")

					# 勾选
					click("xpath", "//div[contains(text(),'XYZ')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 用JS方便点击‘到单处理’按钮旁边的倒三角形
					js_click("xpath", "//span[text()='到单处理']/parent::*/following-sibling::*/child::*")
					sleep(1)

					# 点击到单处理按钮
					js_click("xpath", "//a[contains(text(),'收汇')]")
					sleep(1)

					# 切入收汇的窗体页面endorseWin-iframe
					switch_to("xpath", "//iframe[@id='opWin-iframe']")

					# 输入金额
					click("xpath", "//input[@id='opamount-input']")
					sleep(1)
					clear("xpath", "//input[@id='opamount-input']")
					sleep(1)
					input("xpath", "//input[@id='opamount-input']", "200")
					sleep(1)
					# 点击保存按钮
					click("xpath", "//span[text()='保存']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("信用证开证管理，收汇成功！")
					logging.info("信用证开证管理，收汇成功！")
					sleep(3)

					# 到单处理--押汇
					# 切入‘信用证收证管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='expLOCredits-tab-iframe']")

					# 勾选
					click("xpath", "//div[contains(text(),'XYZ')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 用JS方便点击‘到单处理’按钮旁边的倒三角形
					js_click("xpath", "//span[text()='到单处理']/parent::*/following-sibling::*/child::*")
					sleep(1)

					# 点击到单处理按钮
					js_click("xpath", "//a[contains(text(),'押汇')]")
					sleep(1)

					# 切入押汇的窗体页面endorseWin-iframe
					switch_to("xpath", "//iframe[@id='opWin-iframe']")

					# 输入金额
					click("xpath", "//input[@id='opamount-input']")
					sleep(1)
					clear("xpath", "//input[@id='opamount-input']")
					sleep(1)
					input("xpath", "//input[@id='opamount-input']", "200")
					sleep(1)
					# 点击保存按钮
					click("xpath", "//span[text()='保存']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("信用证开证管理，押汇成功！")
					logging.info("信用证开证管理，押汇成功！")
					sleep(3)

					# 到单处理--远期结汇
					# 切入‘信用证收证管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='expLOCredits-tab-iframe']")

					# 勾选
					click("xpath", "//div[contains(text(),'XYZ')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 用JS方便点击‘到单处理’按钮旁边的倒三角形
					js_click("xpath", "//span[text()='到单处理']/parent::*/following-sibling::*/child::*")
					sleep(1)

					# 点击到单处理按钮
					js_click("xpath", "//a[contains(text(),'远期结汇')]")
					sleep(1)

					# 切入收汇的窗体页面endorseWin-iframe
					switch_to("xpath", "//iframe[@id='opWin-iframe']")

					# 输入金额
					click("xpath", "//input[@id='opamount-input']")
					sleep(1)
					clear("xpath", "//input[@id='opamount-input']")
					sleep(1)
					input("xpath", "//input[@id='opamount-input']", "200")
					sleep(1)
					# 点击保存按钮
					click("xpath", "//span[text()='保存']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("信用证开证管理，远期结汇成功！")
					logging.info("信用证开证管理，远期结汇成功！")
					sleep(3)

					# 到单处理--贴现
					# 切入‘信用证收证管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='expLOCredits-tab-iframe']")

					# 勾选
					click("xpath", "//div[contains(text(),'XYZ')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 用JS方便点击‘到单处理’按钮旁边的倒三角形
					js_click("xpath", "//span[text()='到单处理']/parent::*/following-sibling::*/child::*")
					sleep(1)

					# 点击到单处理按钮
					js_click("xpath", "//a[contains(text(),'贴现')]")
					sleep(1)

					# 切入收汇的窗体页面endorseWin-iframe
					switch_to("xpath", "//iframe[@id='opWin-iframe']")

					# 输入金额
					click("xpath", "//input[@id='opamount-input']")
					sleep(1)
					clear("xpath", "//input[@id='opamount-input']")
					sleep(1)
					input("xpath", "//input[@id='opamount-input']", "200")
					sleep(1)
					# 点击保存按钮
					click("xpath", "//span[text()='保存']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("信用证开证管理，贴现成功！")
					logging.info("信用证开证管理，贴现成功！")
					sleep(3)

					# 到单处理--福费延
					# 切入‘信用证收证管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='expLOCredits-tab-iframe']")

					# 勾选
					click("xpath", "//div[contains(text(),'XYZ')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 用JS方便点击‘到单处理’按钮旁边的倒三角形
					js_click("xpath", "//span[text()='到单处理']/parent::*/following-sibling::*/child::*")
					sleep(1)

					# 点击到单处理按钮
					js_click("xpath", "//a[contains(text(),'福费廷')]")
					sleep(1)

					# 切入收汇的窗体页面endorseWin-iframe
					switch_to("xpath", "//iframe[@id='opWin-iframe']")

					# 输入金额
					click("xpath", "//input[@id='opamount-input']")
					sleep(1)
					clear("xpath", "//input[@id='opamount-input']")
					sleep(1)
					input("xpath", "//input[@id='opamount-input']", "200")
					sleep(1)
					# 点击保存按钮
					click("xpath", "//span[text()='保存']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("信用证开证管理，福费廷成功！")
					logging.info("信用证开证管理，福费廷成功！")
					sleep(3)

					# 到单处理--变更
					# 切入‘信用证收证管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='expLOCredits-tab-iframe']")

					# 勾选
					click("xpath", "//div[contains(text(),'XYZ')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 用JS方便点击‘到单处理’按钮旁边的倒三角形
					js_click("xpath", "//span[text()='变更']")
					sleep(1)
					# 切入收汇的窗体页面
					switch_to("xpath", "//iframe[@id='changeWin-iframe']")

					# 输入金额
					click("xpath", "//input[@id='amount-input']")
					sleep(1)
					clear("xpath", "//input[@id='amount-input']")
					sleep(1)
					input("xpath", "//input[@id='amount-input']", "66200000")
					sleep(1)
					# 点击保存按钮
					click("xpath", "//span[text()='变更']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("信用证开证管理，变更成功！")
					logging.info("信用证开证管理，变更成功！")
					sleep(3)

					# 终止
					# 切入‘信用证收证管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='expLOCredits-tab-iframe']")

					# 勾选
					click("xpath", "//div[contains(text(),'XYZ')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 点击审核按钮
					click("xpath", "//span[text()='终止']")

					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'终止成功！')]")
					print("信用证收证管理，终止成功！")
					logging.info("信用证收证管理，终止成功！")
					time.sleep(3)

					# 取消审核
					# 切入‘信用证收证管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='expLOCredits-tab-iframe']")

					# 勾选
					click("xpath", "//div[contains(text(),'XYZ')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 用JS方便点击‘审核’按钮旁边的倒三角形
					js_click("xpath", "//span[text()='终止']/parent::*/following-sibling::*/child::*")
					sleep(1)

					# 点击取消审核按钮
					click("xpath", "//a[contains(text(),'取消终止')]")
					sleep(1)

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'取消终止成功！')]")
					print("信用证收证管理，取消终止成功！")
					logging.info("信用证收证管理，取消终止成功！")
					time.sleep(3)

					# 操作记录查看
					# 切入‘信用证收证管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='expLOCredits-tab-iframe']")

					# 勾选
					click("xpath", "//div[contains(text(),'XYZ')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 点击操作记录按钮
					click("xpath", "//span[text()='操作记录']")
					sleep(1)

					# 切入收汇的窗体页面
					switch_to("xpath", "//iframe[@id='opdetailWin-iframe']")

					click("xpath", "//div[@title='操作标志:福费廷']/parent::*/preceding-sibling::*[2]/descendant::*[2]")
					sleep(1)
					click("xpath", "//span[text()='取消福费廷']")
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					# 退出所有iframe窗体
					# switch_parent()

					# # 用隐式等待方法等页面出现审核的提示框
					# implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("信用证收证管理，取消福费廷成功！")
					logging.info("信用证收证管理，取消福费廷成功！")
					time.sleep(3)

					# # 切入收汇的窗体页面
					# switch_to("xpath", "//iframe[@id='opdetailWin-iframe']")

					click("xpath", "//div[@title='操作标志:贴现']/parent::*/preceding-sibling::*[2]/descendant::*[2]")
					sleep(1)
					click("xpath", "//span[text()='取消贴现']")
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					# 退出所有iframe窗体
					# switch_parent()
					# 用隐式等待方法等页面出现审核的提示框
					# implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("信用证收证管理，取消贴现成功！")
					logging.info("信用证收证管理，取消贴现成功！")
					time.sleep(3)

					# 切入收汇的窗体页面
					# switch_to("xpath", "//iframe[@id='opdetailWin-iframe']")

					click("xpath", "//div[@title='操作标志:远期结汇']/parent::*/preceding-sibling::*[2]/descendant::*[2]")
					sleep(1)
					click("xpath", "//span[text()='取消远期结汇']")
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					# 退出所有iframe窗体
					# switch_parent()
					#
					# # 用隐式等待方法等页面出现审核的提示框
					# implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("信用证收证管理，取消远期结汇成功！")
					logging.info("信用证收证管理，取消远期结汇成功！")
					time.sleep(3)

					# 切入押汇的窗体页面
					# switch_to("xpath", "//iframe[@id='opdetailWin-iframe']")

					click("xpath", "//div[@title='操作标志:押汇']/parent::*/preceding-sibling::*[2]/descendant::*[2]")
					sleep(1)
					click("xpath", "//span[text()='取消押汇']")
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					# 退出所有iframe窗体
					# switch_parent()
					# # 用隐式等待方法等页面出现审核的提示框
					# implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("信用证收证管理，取消押汇成功！")
					logging.info("信用证收证管理，取消押汇成功！")
					time.sleep(3)

					# 切入收汇的窗体页面
					# switch_to("xpath", "//iframe[@id='opdetailWin-iframe']")

					click("xpath", "//div[@title='操作标志:收汇']/parent::*/preceding-sibling::*[2]/descendant::*[2]")
					sleep(1)
					click("xpath", "//span[text()='取消收汇']")
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					# 退出所有iframe窗体
					# switch_parent()
					# # 用隐式等待方法等页面出现审核的提示框
					# implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("信用证收证管理，取消收汇成功！")
					logging.info("信用证收证管理，取消收汇成功！")
					time.sleep(3)

					# 切入收汇的窗体页面
					# switch_to("xpath", "//iframe[@id='opdetailWin-iframe']")

					click("xpath", "//div[@title='操作标志:客户承兑']/parent::*/preceding-sibling::*[2]/descendant::*[2]")
					sleep(1)
					click("xpath", "//span[text()='取消承兑']")
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					# 退出所有iframe窗体
					# switch_parent()
					#
					# # 用隐式等待方法等页面出现审核的提示框
					# implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("信用证收证管理，取消承兑成功！")
					logging.info("信用证收证管理，取消承兑成功！")
					time.sleep(3)

			# 退出所有iframe窗体
			switch_default()

			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='信用证收证管理']/child::*[1]")

			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//span[@title='信用证管理']")

			# 打印操作成功日志
			print("信用证收证管理，操作成功!")
			logging.info("信用证收证管理，操作成功!")
			time.sleep(2)

		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("信用证收证管理,失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)

		# 测试信用证收证查看功能
		try:
			# 点击支票管理菜单
			click("xpath", "//span[@title='信用证管理']")
			# 点击应付支票作废菜单
			click("xpath", "//span[@title='信用证收证查看']")
			# 退出所有的iframe窗体
			switch_default()

			logging.info("开始测试信用证收证查看功能")
			# 切入‘应付支票作废’的iframe窗体
			switch_to("xpath", "//iframe[@id='expLOCreditsView-tab-iframe']")

			# 点击查看
			# 用JS的方法点击放大镜
			js_click("xpath", "//span[@class='f-contrac-close']")
			sleep(1)

			click("xpath", "//input[@id='creditnumber']")

			# 输入内容
			input("xpath", "//input[@id='creditnumber']", "XYZ")
			sleep(1)
			# 点击查询
			click("xpath", "//span[text()='查询']")

			# 用隐式等待方法等页面出现预期数据：客户:Mindy自动化测试客户
			implici_wait("xpath", "//div[@title='客户:Mindy自动化测试客户']")
			print("信用证收证查看成功！")
			time.sleep(3)

			# 退出所有iframe窗体
			switch_default()

			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='信用证收证查看']/child::*[1]")

			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//span[@title='信用证管理']")

			# 打印操作成功日志
			print("信用证收证查看，操作成功!")
			logging.info("信用证收证查看，操作成功!")
			time.sleep(2)
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("信用证收证查看,失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)

		# 测试信用证管理-信用证开证管理
		try:
			# 点击承兑票据管理菜单
			click("xpath", "//span[@title='信用证管理']")
			# 点击应收支票登记菜单
			click("xpath", "//span[@title='信用证开证管理']")

			# 退出所有的iframe窗体
			switch_default()
			logging.info("开始测试信用证开证管理功能")
			for i in range(1, 4):
				# 切入‘信用证收证管理’的iframe窗体
				switch_to("xpath", "//iframe[@id='impLOCredits-tab-iframe']")
				# 用JS的方法点击新增按钮
				js_click("xpath", "//span[text()='新增']")
				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='addWin-iframe']")
				sleep(1)

				# 选择部门
				# 点击‘部门’框
				click("xpath", "//input[@id='combobox-input-deptid']")
				# 输入自动化测试部，模糊查询
				input("xpath", "//input[@id='combobox-input-deptid']", "自动化测试部")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-deptid']")
				input_enter("xpath", "//input[@id='combobox-input-deptid']")
				time.sleep(1)

				# 选择工程项目
				# 点击‘工程项目’框
				click("xpath", "//input[@id='combobox-input-projectitemid']")
				# 输入自动化测试部，模糊查询
				input("xpath", "//input[@id='combobox-input-projectitemid']", "自动化测试工程项目")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-projectitemid']")
				input_enter("xpath", "//input[@id='combobox-input-projectitemid']")
				time.sleep(1)

				# 选择融资产品
				# 点击‘融资产品’框
				click("xpath", "//input[@id='combobox-input-credittypeid']")
				# 输入信用证类型，模糊查询
				input("xpath", "//input[@id='combobox-input-credittypeid']", "105")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-credittypeid']")
				input_enter("xpath", "//input[@id='combobox-input-credittypeid']")
				time.sleep(1)

				# 设置时间的变成存储，变成
				temp1 = time.strftime("%H%M%S")
				# 输入信用证号码
				click("xpath", "//span[text()='信用证号码']/ancestor::*[2]/descendant::*[6]/descendant::*[1]")
				sleep(1)
				input("xpath", "//span[text()='信用证号码']/ancestor::*[2]/descendant::*[6]/descendant::*[1]",
				      "KZXZH" + str(temp1))
				sleep(1)

				if i == 2:
					# 开证方式
					click("xpath", "//input[@id='combobox-input-issuetype']")
					clear("xpath", "//input[@id='combobox-input-issuetype']")
					sleep(1)
					# 输入信用证类型，模糊查询
					input("xpath", "//input[@id='combobox-input-issuetype']", "背对背开证")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-issuetype']")
					input_enter("xpath", "//input[@id='combobox-input-issuetype']")
					time.sleep(1)

				if i == 3:
					# 开证方式
					click("xpath", "//input[@id='combobox-input-issuetype']")
					clear("xpath", "//input[@id='combobox-input-issuetype']")
					sleep(1)
					# 输入信用证类型，模糊查询
					input("xpath", "//input[@id='combobox-input-issuetype']", "前对背开证")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-issuetype']")
					input_enter("xpath", "//input[@id='combobox-input-issuetype']")
					time.sleep(1)

				# 点击开证银行框
				click("xpath", "//input[@id='combobox-input-issuingbankid']")
				# 输入信用证类型，模糊查询
				input("xpath", "//input[@id='combobox-input-issuingbankid']", "中国银行")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-issuingbankid']")
				input_enter("xpath", "//input[@id='combobox-input-issuingbankid']")
				time.sleep(1)

				# 点击开证开户银行框
				click("xpath", "//input[@id='combobox-input-issuingbanklocationid']")
				# 输入信用证类型，模糊查询
				input("xpath", "//input[@id='combobox-input-issuingbanklocationid']", "甘肃省分行")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-issuingbanklocationid']")
				input_enter("xpath", "//input[@id='combobox-input-issuingbanklocationid']")
				time.sleep(1)

				# 输入开证金额
				click("xpath", "//span[text()='开证金额']/ancestor::*[2]/descendant::*[8]")
				sleep(1)
				clear("xpath", "//span[text()='开证金额']/ancestor::*[2]/descendant::*[8]")
				sleep(1)
				input("xpath", "//span[text()='开证金额']/ancestor::*[2]/descendant::*[8]", "10000")
				sleep(1)

				# 输入开证币种
				click("xpath", "//input[@id='combobox-input-currencyid']")
				sleep(1)
				input("xpath", "//input[@id='combobox-input-currencyid']", "CNY-人民币")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-currencyid']")
				input_enter("xpath", "//input[@id='combobox-input-currencyid']")
				time.sleep(1)

				if i == 2:
					double_click("xpath", "//input[@id='dollarrate-input']")
					click("xpath", "//input[@id='isforwards']")
					sleep(1)
					# 输入远期天数
					input("xpath", "//input[@id='forwarddays-input']", "30")
					sleep(1)

				if i == 3:
					double_click("xpath", "//input[@id='dollarrate-input']")
					click("xpath", "//input[@id='isforwards']")
					sleep(1)
					# 输入远期天数
					input("xpath", "//input[@id='forwarddays-input']", "30")
					sleep(1)

				# 输入截止日期
				today = date.today()
				expirydate = today + timedelta(days=60)
				click("xpath", "//input[@id='expirydate-input']")
				sleep(1)
				clear("xpath", "//input[@id='expirydate-input']")
				sleep(1)
				input("xpath", "//input[@id='expirydate-input']", str(expirydate))
				# 模拟回车键
				keyDown('enter')
				keyUp('enter')
				time.sleep(1)

				if i == 1:
					# 授信协议
					click("xpath", "//input[@id='combobox-input-creditid']")
					sleep(1)
					input("xpath", "//input[@id='combobox-input-creditid']", "ZDHXYH00")
					sleep(1)
					input_enter("xpath", "//input[@id='combobox-input-creditid']")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-creditid']")
					sleep(1)
					input_enter("xpath", "//input[@id='combobox-input-creditid']")
					time.sleep(1)
				else:
					# 授信协议
					click("xpath", "//input[@id='combobox-input-creditid']")
					sleep(1)
					input("xpath", "//input[@id='combobox-input-creditid']", "ZDHZYFXYH001")
					sleep(1)
					input_enter("xpath", "//input[@id='combobox-input-creditid']")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-creditid']")
					input_enter("xpath", "//input[@id='combobox-input-creditid']")
					time.sleep(1)

				# 使用授信额度
				click("xpath", "//input[@id='usecreditamount-input']")
				sleep(1)
				clear("xpath", "//input[@id='usecreditamount-input']")
				sleep(1)
				input("xpath", "//input[@id='usecreditamount-input']", "3000")
				sleep(1)

				# 信用证类型
				click("xpath", "//input[@id='combobox-input-credittype']")
				sleep(1)
				input("xpath", "//input[@id='combobox-input-credittype']", "国际贸易")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-credittype']")
				input_enter("xpath", "//input[@id='combobox-input-credittype']")
				time.sleep(1)

				# 输入到单次数
				input("xpath", "//input[@id='exchangecount']", "30")
				sleep(1)

				# 预计到单日期
				today = date.today()
				expectexchangedate = today + timedelta(days=40)
				click("xpath", "//input[@id='expectexchangedate-input']")
				sleep(1)
				input("xpath", "//input[@id='expectexchangedate-input']", str(expectexchangedate))
				time.sleep(2)

				# 输入备注
				double_click("xpath", "//textarea[@id='description']")
				sleep(1)
				input("xpath", "//textarea[@id='description']", "自动化测试信用证开证备注框")
				sleep(1)

				if i == 1:
					# 输入溢短
					click("xpath", "//input[@id='overflowratio-input']")
					sleep(1)
					clear("xpath", "//input[@id='overflowratio-input']")
					sleep(1)
					input("xpath", "//input[@id='overflowratio-input']", "5")
					sleep(1)

				else:
					# 填写授信占用信息
					# 点击授新增行，新增第一行
					click("xpath", "//span[@title='额度']/ancestor::*[6]/following-sibling::*[2]/descendant::*[7]")
					sleep(1)
					# 输入授信方式
					input("xpath", "//input[@id='combobox-input-sumcontrolgrid-guaranteetype-0']", "信用")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-sumcontrolgrid-guaranteetype-0']")
					input_enter("xpath", "//input[@id='combobox-input-sumcontrolgrid-guaranteetype-0']")
					time.sleep(1)

					click("xpath", "//input[@id='sumcontrolgrid-transamount-0-input']")
					sleep(1)
					clear("xpath", "//input[@id='sumcontrolgrid-transamount-0-input']")
					sleep(1)
					# 输入占用额度
					input("xpath", "//input[@id='sumcontrolgrid-transamount-0-input']", "3000")
					sleep(1)

					# 点击关联收证tab页
					click("xpath", "//span[text()='关联收证信息']")
					sleep(1)

					# 关联收证信息新增一行
					click("xpath", "//span[@title='原证号码']/ancestor::*[6]/following-sibling::*[2]/descendant::*[7]")

					# 原证号码
					click("xpath", "//input[@id='combobox-input-locreditsrelationsgrid-explocreditid-0']")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-locreditsrelationsgrid-explocreditid-0']")
					input_enter("xpath", "//input[@id='combobox-input-locreditsrelationsgrid-explocreditid-0']")
					time.sleep(1)

				# 点击保证金tab页
				click("xpath", "//span[text()='保证金']")
				sleep(1)

				# 保证金新增一行
				click("xpath", "//span[@title='付款日期']/ancestor::*[6]/following-sibling::*[2]/descendant::*[7]")

				# 选择付款日期
				today = date.today()
				begin_date = today + timedelta(days=1)
				click("xpath", "//input[@id='bailgrid-paydate-0-input']")
				sleep(1)
				clear("xpath", "//input[@id='bailgrid-paydate-0-input']")
				sleep(1)
				input("xpath", "//input[@id='bailgrid-paydate-0-input']", str(begin_date))
				time.sleep(1)

				# 预计收回日期
				today = date.today()
				begin_date = today + timedelta(days=20)
				click("xpath", "//input[@id='bailgrid-recyclingdate-0-input']")
				sleep(1)
				clear("xpath", "//input[@id='bailgrid-recyclingdate-0-input']")
				sleep(1)
				input("xpath", "//input[@id='bailgrid-recyclingdate-0-input']", str(begin_date))
				time.sleep(1)

				# 保证金账户
				click("xpath", "//input[@id='combobox-input-bailgrid-accountid-0']")
				sleep(1)
				input("xpath", "//input[@id='combobox-input-bailgrid-accountid-0']", "CNY")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-bailgrid-accountid-0']")
				input_enter("xpath", "//input[@id='combobox-input-bailgrid-accountid-0']")
				time.sleep(1)

				# 保证金原币金额
				double_click("xpath", "//input[@id='bailgrid-bailsourceamount-0-input']")
				sleep(1)
				input("xpath", "//input[@id='bailgrid-bailsourceamount-0-input']", "300")
				sleep(1)

				# 保证金币种
				click("xpath", "//input[@id='combobox-input-bailgrid-currencyid-0']")
				sleep(1)
				input("xpath", "//input[@id='combobox-input-bailgrid-currencyid-0']", "CNY")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-bailgrid-currencyid-0']")
				input_enter("xpath", "//input[@id='combobox-input-bailgrid-currencyid-0']")
				time.sleep(1)

				# 点击报关单tab页
				click("xpath", "//span[text()='报关单']")
				sleep(1)

				# 报关单新增一行
				click("xpath", "//span[@title='报关单号']/ancestor::*[6]/following-sibling::*[2]/descendant::*[7]")

				# 报关单号
				input("xpath", "//input[@id='declarationsgrid-declarationnumber-0']", "BGD001")
				sleep(1)

				# 选择报关日期
				today = date.today()
				begin_date = today - timedelta(days=20)
				click("xpath", "//input[@id='declarationsgrid-declarationdate-0-input']")
				sleep(1)
				clear("xpath", "//input[@id='declarationsgrid-declarationdate-0-input']")
				sleep(1)
				input("xpath", "//input[@id='declarationsgrid-declarationdate-0-input']", str(begin_date))
				time.sleep(1)

				# 输入金额
				click("xpath", "//input[@id='declarationsgrid-declarationamount-0-input']")
				sleep(1)
				clear("xpath", "//input[@id='declarationsgrid-declarationamount-0-input']")
				sleep(1)
				input("xpath", "//input[@id='declarationsgrid-declarationamount-0-input']", "300")
				sleep(1)

				# 币种
				click("xpath", "//input[@id='combobox-input-declarationsgrid-currencyid-0']")
				sleep(1)
				input("xpath", "//input[@id='combobox-input-declarationsgrid-currencyid-0']", "CNY")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-declarationsgrid-currencyid-0']")
				input_enter("xpath", "//input[@id='combobox-input-declarationsgrid-currencyid-0']")
				time.sleep(1)

				# 缺少附件上传功能

				# 点击保存按钮
				click("xpath", "//span[text()='保存']")

				# 退出所有iframe窗体
				switch_default()

				# 用隐式等待方法等页面出现提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				print("信用证开证管理第%s次，保存成功！" % i)
				logging.info("信用证开证管理第%s次，保存成功！" % i)
				time.sleep(3)

				# 第一笔，就先修改，再删除新建的‘信用证开证管理’
				if i == 1:
					# 切入‘应收票据管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='impLOCredits-tab-iframe']")

					# 点击查看
					# 用JS的方法点击放大镜
					js_click("xpath", "//span[@class='f-contrac-close']")
					sleep(1)

					# 输入信用证号：KZXZH
					input("xpath", "//input[@id='creditnumber']", "KZXZH")
					sleep(1)

					# 点击查询
					click("xpath", "//span[text()='查询']")

					# 修改
					# 勾选
					click("xpath", "//div[contains(text(),'KZXZH')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 点击修改按钮
					click("xpath", "//span[text()='修改']")

					# 切入修改的iframe窗体
					switch_to("xpath", "//iframe[@id='modWin-iframe']")
					sleep(1)

					# 修改开证金额
					click("xpath", "//input[@id='amount-input']")
					sleep(1)
					clear("xpath", "//input[@id='amount-input']")
					sleep(1)
					input("xpath", "//input[@id='amount-input']", "1200")
					sleep(1)

					# 输入溢短
					click("xpath", "//input[@id='overflowratio-input']")
					sleep(1)
					clear("xpath", "//input[@id='overflowratio-input']")
					sleep(1)
					input("xpath", "//input[@id='overflowratio-input']", "5")
					sleep(1)

					# 修改输入备注
					input("xpath", "//textarea[@id='traderemark']", "自动化测试信用证开证备注框修改备注")
					sleep(1)

					# 点击保存按钮
					click("xpath", "//span[text()='保存']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("信用证开证管理，修改成功！")
					logging.info("信用证开证管理，修改成功！")
					time.sleep(3)

					# 切入‘信用证收证管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='impLOCredits-tab-iframe']")

					# 删除
					# 勾选
					click("xpath", "//div[contains(text(),'KZXZH')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 点击删除按钮
					click("xpath", "//span[text()='删除']")

					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现删除的提示框
					implici_wait("xpath", "//span[contains(text(),'删除1条!')]")
					print("信用证开证管理，删除成功！")
					logging.info("信用证开证管理，删除成功！")
					time.sleep(3)

				# 第二笔，先审核、再取消审核、再托收、再托收到账
				elif i == 2:

					# 第一次审核
					# 切入‘信用证收证管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='impLOCredits-tab-iframe']")

					# 勾选
					click("xpath", "//div[contains(text(),'KZXZH')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 点击审核按钮
					click("xpath", "//span[text()='审核']")

					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'审核成功！')]")
					print("信用证开证管理，第一次审核成功！")
					logging.info("信用证开证管理，第一次审核成功！")
					time.sleep(3)

					# 取消审核
					# 切入‘信用证收证管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='impLOCredits-tab-iframe']")

					# 勾选
					click("xpath", "//div[contains(text(),'KZXZH')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 用JS方便点击‘审核’按钮旁边的倒三角形
					js_click("xpath", "//span[text()='审核']/parent::*/following-sibling::*/child::*")
					sleep(1)

					# 点击取消审核按钮
					js_click("xpath", "//a[contains(text(),'取消审核')]")
					sleep(1)

					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'取消审核成功！')]")
					print("信用证收证管理，取消审核成功！")
					logging.info("信用证收证管理，取消审核成功！")
					time.sleep(3)

					# 第二次审核并开证
					# 切入‘信用证开证管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='impLOCredits-tab-iframe']")

					# 勾选
					click("xpath", "//div[contains(text(),'KZXZH')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 用JS方便点击‘审核’按钮旁边的倒三角形
					js_click("xpath", "//span[text()='审核']/parent::*/following-sibling::*/child::*")
					sleep(1)

					# 点击取消票据背书按钮
					js_click("xpath", "//a[contains(text(),'审核并开证')]")
					sleep(1)

					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'开证成功！')]")
					print("信用证开证管理，审核开证成功！")
					logging.info("信用证开证管理，审核开证成功！")
					sleep(3)

					# 取消开证
					# 切入‘信用证开证管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='impLOCredits-tab-iframe']")

					# 勾选
					click("xpath", "//div[contains(text(),'KZXZH')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 用JS方便点击‘票据操作’按钮旁边的倒三角形
					js_click("xpath", "//span[text()='开证']/parent::*/following-sibling::*/child::*")
					sleep(1)

					# 点击取消票据背书按钮
					js_click("xpath", "//a[contains(text(),'取消开证')]")
					sleep(1)

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'取消开证成功！')]")
					print("信用证开证管理，取消开证成功！")
					logging.info("信用证开证管理，取消开证成功！")
					sleep(3)

					# 开证
					# 切入‘信用证开证管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='impLOCredits-tab-iframe']")

					# 勾选
					click("xpath", "//div[contains(text(),'KZXZH')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 用JS方便点击‘开证’
					click("xpath", "//span[text()='开证']")
					sleep(1)

					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'开证成功！')]")
					print("信用证开证管理，开证成功！")
					logging.info("信用证开证管理，开证成功！")
					sleep(3)

					# 到单处理--到单登记
					# 切入‘信用证开证管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='impLOCredits-tab-iframe']")

					# 勾选
					click("xpath", "//div[contains(text(),'KZXZH')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 用JS方便点击‘到单处理’按钮旁边的倒三角形
					js_click("xpath", "//span[text()='到单处理']/parent::*/following-sibling::*/child::*")
					sleep(1)

					# 点击到单处理按钮
					js_click("xpath", "//a[contains(text(),'到单登记')]")
					sleep(1)

					# 切入到单登记的窗体页面endorseWin-iframe
					switch_to("xpath", "//iframe[@id='operateWin-iframe']")
					sleep(1)

					# 预计到期付款日
					today = date.today()
					duedatepayment = today + timedelta(days=20)
					click("xpath", "//input[@id='duedatepayment-input']")
					sleep(1)
					clear("xpath", "//input[@id='duedatepayment-input']")
					sleep(1)
					input("xpath", "//input[@id='duedatepayment-input']", str(duedatepayment))
					time.sleep(1)

					# 输入通知付款金额
					click("xpath", "//input[@id='amount-input']")
					sleep(1)
					clear("xpath", "//input[@id='amount-input']")
					sleep(1)
					input("xpath", "//input[@id='amount-input']", "1000")
					sleep(1)

					# 点击保存按钮
					click("xpath", "//span[text()='确定']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("信用证开证管理，到单登记成功！")
					logging.info("信用证开证管理，到单登记成功！")
					sleep(3)

					# 到单处理--承兑
					# 切入‘信用证收证管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='impLOCredits-tab-iframe']")

					# 勾选
					click("xpath", "//div[contains(text(),'KZXZH')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 用JS方便点击‘到单处理’按钮旁边的倒三角形
					js_click("xpath", "//span[text()='到单处理']/parent::*/following-sibling::*/child::*")
					sleep(1)

					# 点击到单处理按钮
					js_click("xpath", "//a[contains(text(),'承兑')]")
					sleep(1)

					# 切入收汇的窗体页面endorseWin-iframe
					switch_to("xpath", "//iframe[@id='operateWin-iframe']")

					# 输入金额
					click("xpath", "//input[@id='amount-input']")
					sleep(1)
					clear("xpath", "//input[@id='amount-input']")
					sleep(1)
					input("xpath", "//input[@id='amount-input']", "800")
					sleep(1)

					# 点击保存按钮
					click("xpath", "//span[text()='确定']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("信用证开证管理，承兑成功！")
					logging.info("信用证开证管理，承兑成功！")
					sleep(3)

					# 到单处理--付汇
					# 切入‘信用证收证管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='impLOCredits-tab-iframe']")

					# 勾选
					click("xpath", "//div[contains(text(),'KZXZH')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 用JS方便点击‘到单处理’按钮旁边的倒三角形
					js_click("xpath", "//span[text()='到单处理']/parent::*/following-sibling::*/child::*")
					sleep(1)

					# 点击到单处理按钮
					js_click("xpath", "//a[contains(text(),'付汇')]")
					sleep(1)

					# 切入收汇的窗体页面endorseWin-iframe
					switch_to("xpath", "//iframe[@id='operateWin-iframe']")

					# 输入金额
					double_click("xpath", "//input[@id='amount-input']")
					sleep(1)
					input("xpath", "//input[@id='amount-input']", "400")
					sleep(1)

					# 点击保存按钮
					click("xpath", "//span[text()='确定']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("信用证开证管理，付汇成功！")
					logging.info("信用证开证管理，付汇成功！")
					sleep(3)

					# 到单处理--押汇
					# 切入‘信用证收证管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='impLOCredits-tab-iframe']")

					# 勾选
					click("xpath", "//div[contains(text(),'KZXZH')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 用JS方便点击‘到单处理’按钮旁边的倒三角形
					js_click("xpath", "//span[text()='到单处理']/parent::*/following-sibling::*/child::*")
					sleep(1)

					# 点击到单处理按钮
					js_click("xpath", "//a[contains(text(),'押汇')]")
					sleep(1)

					# 切入收汇的窗体页面endorseWin-iframe
					switch_to("xpath", "//iframe[@id='operateWin-iframe']")

					# 输入金额
					double_click("xpath", "//input[@id='amount-input']")
					sleep(1)
					input("xpath", "//input[@id='amount-input']", "80")
					sleep(1)

					# 点击保存按钮
					click("xpath", "//span[text()='确定']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("信用证开证管理，押汇成功！")
					logging.info("信用证开证管理，押汇成功！")
					sleep(3)

					# 到单处理--变更
					# 切入‘信用证收证管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='impLOCredits-tab-iframe']")

					# 勾选
					click("xpath", "//div[contains(text(),'KZXZH')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 用JS方便点击‘到单处理’按钮旁边的倒三角形
					js_click("xpath", "//span[text()='变更']")
					sleep(1)
					# 切入收汇的窗体页面
					switch_to("xpath", "//iframe[@id='changeWin-iframe']")
					sleep(1)

					# 点击保存按钮
					click("xpath", "//span[text()='变更']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("信用证开证管理，变更成功！")
					logging.info("信用证开证管理，变更成功！")
					sleep(3)

					# 终止
					# 切入‘信用证收证管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='impLOCredits-tab-iframe']")

					# 勾选
					click("xpath", "//div[contains(text(),'KZXZH')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 点击审核按钮
					click("xpath", "//span[text()='终止']")

					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'终止成功！')]")
					print("信用证收证管理，终止成功！")
					logging.info("信用证收证管理，终止成功！")
					time.sleep(3)

					# 取消终止
					# 切入‘信用证收证管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='impLOCredits-tab-iframe']")

					# 勾选
					click("xpath", "//div[contains(text(),'KZXZH')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 用JS方便点击‘终止’按钮旁边的倒三角形
					js_click("xpath", "//span[text()='终止']/parent::*/following-sibling::*/child::*")
					sleep(1)

					# 点击取消审核按钮
					click("xpath", "//a[contains(text(),'取消终止')]")
					sleep(1)

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'取消终止成功！')]")
					print("信用证收证管理，取消终止成功！")
					logging.info("信用证收证管理，取消终止成功！")
					time.sleep(3)

					# 保证金登记
					# 切入‘信用证收证管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='impLOCredits-tab-iframe']")

					# 勾选
					click("xpath", "//div[contains(text(),'KZXZH')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 点击审核按钮
					js_click("xpath", "//span[text()='保证金登记']")
					sleep(1)

					switch_to("xpath", "//iframe[@id='registerBailsWin-iframe']")

					# 点击保证金新增行，新增第一行
					click("xpath", "//span[@title='预计收回日期']/ancestor::*[6]/following-sibling::*[2]/descendant::*[7]")
					sleep(1)

					# 付款日期
					today = date.today()
					duedatepayment = today
					click("xpath", "//input[@id='bailgrid-paydate-1-input']")
					sleep(1)
					input("xpath", "//input[@id='bailgrid-paydate-1-input']", str(duedatepayment))
					# 模拟回车键
					keyDown('enter')
					keyUp('enter')
					time.sleep(1)

					# 输入保证金账户
					click("xpath", "//input[@id='combobox-input-bailgrid-accountid-1']")
					sleep(1)
					input("xpath", "//input[@id='combobox-input-bailgrid-accountid-1']", "CNY")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-bailgrid-accountid-1']")
					input_enter("xpath", "//input[@id='combobox-input-bailgrid-accountid-1']")
					time.sleep(1)

					# 预计收回日期
					today = date.today()
					recyclingdate = today + timedelta(days=40)
					click("xpath", "//input[@id='bailgrid-recyclingdate-1-input']")
					sleep(1)
					input("xpath", "//input[@id='bailgrid-recyclingdate-1-input']", str(recyclingdate))
					time.sleep(1)

					# 保证金
					double_click("xpath", "//input[@id='bailgrid-bailsourceamount-1-input']")
					sleep(1)
					input("xpath", "//input[@id='bailgrid-bailsourceamount-1-input']", "10")
					sleep(1)

					# 保证金金币
					input("xpath", "//input[@id='combobox-input-bailgrid-currencyid-1']", "CNY")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-bailgrid-currencyid-1']")
					input_enter("xpath", "//input[@id='combobox-input-bailgrid-currencyid-1']")
					time.sleep(1)

					# 点击审核按钮
					click("xpath", "//span[text()='保证金登记']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("信用证收证管理，保证金登记成功！")
					logging.info("信用证收证管理，保证金登记成功！")
					time.sleep(3)

					# 操作记录查看
					# 切入‘信用证收证管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='impLOCredits-tab-iframe']")

					# 勾选
					click("xpath", "//div[contains(text(),'KZXZH')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 点击操作记录按钮
					click("xpath", "//span[text()='操作记录']")
					sleep(1)

					# 切入收汇的窗体页面
					switch_to("xpath", "//iframe[@id='operationWin-iframe']")

					click("xpath", "//div[@title='操作标志:到单登记']/parent::*/preceding-sibling::*[2]/descendant::*[2]")
					sleep(1)
					click("xpath", "//span[text()='取消到单登记']")
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

					print("信用证收证管理，取消到单登记成功！")
					logging.info("信用证收证管理，取消到单登记成功！")
					time.sleep(3)

					# # 切入收汇的窗体页面
					# switch_to("xpath", "//iframe[@id='opdetailWin-iframe']")

					click("xpath", "//div[@title='操作标志:押汇']/parent::*/preceding-sibling::*[2]/descendant::*[2]")
					sleep(1)
					click("xpath", "//span[text()='取消押汇']")
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

					print("信用证收证管理，取消押汇成功！")
					logging.info("信用证收证管理，取消押汇成功！")
					time.sleep(3)

					click("xpath", "//div[@title='操作标志:付汇']/parent::*/preceding-sibling::*[2]/descendant::*[2]")
					sleep(1)
					click("xpath", "//span[text()='取消付汇']")
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

					print("信用证收证管理，取消付汇成功！")
					logging.info("信用证收证管理，取消付汇成功！")
					time.sleep(3)

					switch_default()

					switch_to("xpath", "//iframe[@id='impLOCredits-tab-iframe']")

					# 点击关闭
					click("xpath", "//span[text()='操作记录查看']/preceding-sibling::*[1]")

					switch_default()

				if i == 3:
					# 审核并开证
					# 切入‘信用证开证管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='impLOCredits-tab-iframe']")

					# 勾选
					click("xpath", "//div[contains(text(),'KZXZH')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 用JS方便点击‘审核’按钮旁边的倒三角形
					js_click("xpath", "//span[text()='审核']/parent::*/following-sibling::*/child::*")
					sleep(1)

					# 点击取消票据背书按钮
					js_click("xpath", "//a[contains(text(),'审核并开证')]")
					sleep(1)

					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'开证成功！')]")
					print("信用证开证管理，审核开证成功！")
					logging.info("信用证开证管理，审核开证成功！")
					sleep(3)

					# 到单处理--到单登记
					# 切入‘信用证开证管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='impLOCredits-tab-iframe']")

					# 勾选
					click("xpath", "//div[contains(text(),'KZXZH')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 用JS方便点击‘到单处理’按钮旁边的倒三角形
					js_click("xpath", "//span[text()='到单处理']/parent::*/following-sibling::*/child::*")
					sleep(1)

					# 点击到单处理按钮
					js_click("xpath", "//a[contains(text(),'到单登记')]")
					sleep(1)

					# 切入到单登记的窗体页面endorseWin-iframe
					switch_to("xpath", "//iframe[@id='operateWin-iframe']")
					sleep(1)

					# 预计到期付款日
					today = date.today()
					duedatepayment = today + timedelta(days=20)
					click("xpath", "//input[@id='duedatepayment-input']")
					sleep(1)
					clear("xpath", "//input[@id='duedatepayment-input']")
					sleep(1)
					input("xpath", "//input[@id='duedatepayment-input']", str(duedatepayment))
					time.sleep(1)

					# 输入通知付款金额
					click("xpath", "//input[@id='amount-input']")
					sleep(1)
					clear("xpath", "//input[@id='amount-input']")
					sleep(1)
					input("xpath", "//input[@id='amount-input']", "1000")
					sleep(1)

					# 点击保存按钮
					click("xpath", "//span[text()='确定']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("信用证开证管理，到单登记成功！")
					logging.info("信用证开证管理，到单登记成功！")
					sleep(3)

					# 到单处理--承兑
					# 切入‘信用证收证管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='impLOCredits-tab-iframe']")

					# 勾选
					click("xpath", "//div[contains(text(),'KZXZH')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 用JS方便点击‘到单处理’按钮旁边的倒三角形
					js_click("xpath", "//span[text()='到单处理']/parent::*/following-sibling::*/child::*")
					sleep(1)

					# 点击到单处理按钮
					js_click("xpath", "//a[contains(text(),'承兑')]")
					sleep(1)

					# 切入收汇的窗体页面endorseWin-iframe
					switch_to("xpath", "//iframe[@id='operateWin-iframe']")

					# 点击保存按钮
					click("xpath", "//span[text()='确定']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("信用证开证管理，承兑成功！")
					logging.info("信用证开证管理，承兑成功！")
					sleep(3)

					# 保证金登记
					# 切入‘信用证收证管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='impLOCredits-tab-iframe']")

					# 勾选
					click("xpath", "//div[contains(text(),'KZXZH')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 点击审核按钮
					js_click("xpath", "//span[text()='保证金登记']")
					sleep(1)

					switch_to("xpath", "//iframe[@id='registerBailsWin-iframe']")

					# 点击选择保证金数据
					click("xpath", "//span[@title='预计收回日期']/ancestor::*[2]/preceding-sibling::*[3]/descendant::*[2]")
					sleep(1)

					# 点击保证金新增行，新增第一行
					click("xpath", "//span[@title='预计收回日期']/ancestor::*[6]/following-sibling::*[2]/descendant::*[9]")
					sleep(1)

					# 点击审核按钮
					click("xpath", "//span[text()='保证金登记']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("信用证收证管理，保证金登记成功！")
					logging.info("信用证收证管理，保证金登记成功！")
					time.sleep(3)

					# 报关单登记
					# 切入‘信用证收证管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='impLOCredits-tab-iframe']")

					# 勾选
					click("xpath", "//div[contains(text(),'KZXZH')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 点击审核按钮
					js_click("xpath", "//span[text()='报关单登记']")
					sleep(1)

					switch_to("xpath", "//iframe[@id='registerDeclarationsWin-iframe']")
					sleep(1)

					# 报关单新增一行
					click("xpath", "//span[@title='报关单号']/ancestor::*[6]/following-sibling::*[2]/descendant::*[7]")

					# 报关单号
					input("xpath", "//input[@id='declarationsgrid-declarationnumber-1']", "BGDS001")
					sleep(1)

					# 选择报关日期
					today = date.today()
					begin_date = today - timedelta(days=20)
					click("xpath", "//input[@id='declarationsgrid-declarationdate-1-input']")
					sleep(1)
					clear("xpath", "//input[@id='declarationsgrid-declarationdate-1-input']")
					sleep(1)
					input("xpath", "//input[@id='declarationsgrid-declarationdate-1-input']", str(begin_date))
					time.sleep(1)

					# 双击
					double_click("xpath", "//input[@id='declarationsgrid-description-1']")
					sleep(1)

					# 输入金额
					click("xpath", "//input[@id='declarationsgrid-declarationamount-1-input']")
					sleep(1)
					clear("xpath", "//input[@id='declarationsgrid-declarationamount-1-input']")
					sleep(1)
					input("xpath", "//input[@id='declarationsgrid-declarationamount-1-input']", "300")
					sleep(1)

					# 币种
					click("xpath", "//input[@id='combobox-input-declarationsgrid-currencyid-1']")
					sleep(1)
					input("xpath", "//input[@id='combobox-input-declarationsgrid-currencyid-1']", "CNY")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-declarationsgrid-currencyid-1']")
					input_enter("xpath", "//input[@id='combobox-input-declarationsgrid-currencyid-1']")
					time.sleep(1)

					# 点击审核按钮
					click("xpath", "//span[text()='报关单登记']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("信用证收证管理，报关单登记成功！")
					logging.info("信用证收证管理，报关单登记成功！")
					time.sleep(3)

					# 关联收证
					# 切入‘信用证收证管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='impLOCredits-tab-iframe']")

					# 勾选
					click("xpath", "//div[contains(text(),'KZXZH')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 点击关联收证按钮
					js_click("xpath", "//span[text()='关联收证']")
					sleep(1)

					switch_to("xpath", "//iframe[@id='locreditsRelationsWin-iframe']")
					sleep(1)

					# 关联收证信息新增一行
					click("xpath", "//span[@title='原证号码']/ancestor::*[6]/following-sibling::*[2]/descendant::*[7]")

					# 原证号码
					click("xpath", "//input[@id='combobox-input-locreditsrelationsgrid-explocreditid-1']")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-locreditsrelationsgrid-explocreditid-1']")
					input_down("xpath", "//input[@id='combobox-input-locreditsrelationsgrid-explocreditid-1']")
					input_enter("xpath", "//input[@id='combobox-input-locreditsrelationsgrid-explocreditid-1']")
					time.sleep(1)
					# 点击审核按钮
					click("xpath", "//span[text()='关联收证信息']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("信用证收证管理，关联收证信息成功！")
					logging.info("信用证收证管理，关联收证信息成功！")
					time.sleep(3)

					# 结清
					# 切入‘信用证收证管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='impLOCredits-tab-iframe']")

					# 勾选
					click("xpath", "//div[contains(text(),'KZXZH')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 点击审核按钮
					js_click("xpath", "//span[text()='结清']")
					sleep(1)

					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("信用证收证管理，关联收证信息成功！")
					logging.info("信用证收证管理，关联收证信息成功！")
					time.sleep(3)

					# 操作记录查看
					# 切入‘信用证收证管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='impLOCredits-tab-iframe']")

					# 勾选
					click("xpath", "//div[contains(text(),'KZXZH')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 点击操作记录按钮
					click("xpath", "//span[text()='操作记录']")
					sleep(1)

					# 切入收汇的窗体页面
					switch_to("xpath", "//iframe[@id='operationWin-iframe']")

					click("xpath", "//div[@title='操作标志:到单登记']/parent::*/preceding-sibling::*[2]/descendant::*[2]")
					sleep(1)
					click("xpath", "//span[text()='取消到单登记']")
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

					print("信用证收证管理，取消到单登记成功！")
					logging.info("信用证收证管理，取消到单登记成功！")
					time.sleep(3)

					click("xpath", "//div[@title='操作标志:承兑']/parent::*/preceding-sibling::*[2]/descendant::*[2]")
					sleep(1)
					click("xpath", "//span[text()='取消承兑']")
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

					print("信用证收证管理，取消承兑成功！")
					logging.info("信用证收证管理，取消承兑成功！")
					time.sleep(3)

					click("xpath", "//div[@title='操作标志:结清']/parent::*/preceding-sibling::*[2]/descendant::*[2]")
					sleep(1)
					click("xpath", "//span[text()='取消结清']")
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

					print("信用证收证管理，取消结清成功！")
					logging.info("信用证收证管理，取消结清成功！")
					time.sleep(3)

			# 退出所有iframe窗体
			switch_default()

			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='信用证开证管理']/child::*[1]")

			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//span[@title='信用证管理']")

			# 打印操作成功日志
			print("信用证开证管理，操作成功!")
			logging.info("信用证开证管理，操作成功!")
			time.sleep(2)

		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("信用证开证管理,失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
			
		# 测试信用证开证查看
		try:
			# 点击支票管理菜单
			click("xpath", "//span[@title='信用证管理']")
			# 点击应付支票作废菜单
			click("xpath", "//span[@title='信用证开证查看']")
			# 退出所有的iframe窗体
			switch_default()

			logging.info("开始测试信用证开证查看功能")
			# 切入‘应付支票作废’的iframe窗体
			switch_to("xpath", "//iframe[@id='impLOCreditsView-tab-iframe']")

			# 点击查看
			# 用JS的方法点击放大镜
			js_click("xpath", "//span[@class='f-contrac-close']")
			sleep(1)

			click("xpath", "//input[@id='creditnumber']")

			# 输入内容
			input("xpath", "//input[@id='creditnumber']", "KZXZH")
			sleep(1)
			# 点击查询
			click("xpath", "//span[text()='查询']")

			# 用隐式等待方法等页面出现预期数据：客户:Mindy自动化测试客户
			implici_wait("xpath", "//div[contains(text(), 'ZDHZYFXYH')]")
			print("信用证开证查看成功！")
			time.sleep(3)

			# 退出所有iframe窗体
			switch_default()

			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='信用证开证查看']/child::*[1]")

			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//span[@title='信用证管理']")

			# 打印操作成功日志
			print("信用证开证查看，操作成功!")
			logging.info("信用证开证查看，操作成功!")
			time.sleep(2)
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("信用证开证查看,失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		
		# 测试委托方保函管理
		try:
			# 点击保函管理菜单
			click("xpath", "//span[@title='保函管理']")
			# 点击应收支票登记菜单
			click("xpath", "//span[@title='委托方保函管理']")
			# 退出所有的iframe窗体
			switch_default()
			logging.info("开始测试委托方保函管理功能")
			for i in range(1, 3):
				# 切入‘信用证收证管理’的iframe窗体
				switch_to("xpath", "//iframe[@id='prinLOGuarantees-tab-iframe']")
				# 用JS的方法点击新增按钮
				js_click("xpath", "//span[text()='新增']")
				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='addWin-iframe']")
				sleep(1)
				
				# 选择部门
				# 点击‘部门’框
				click("xpath", "//input[@id='combobox-input-deptid']")
				# 输入自动化测试部，模糊查询
				input("xpath", "//input[@id='combobox-input-deptid']", "自动化测试部")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-deptid']")
				input_enter("xpath", "//input[@id='combobox-input-deptid']")
				time.sleep(1)
				
				# 设置时间的变成存储，变成
				temp1 = time.strftime("%H%M%S")
				# 输入保函编号
				click("xpath", "//span[text()='保函编号']/ancestor::*[2]/descendant::*[6]/descendant::*[1]")
				sleep(1)
				input("xpath", "//span[text()='保函编号']/ancestor::*[2]/descendant::*[6]/descendant::*[1]",
				      "WTBH" + str(temp1))
				sleep(1)
				
				if i == 1:
					
					# 选择受益人类型
					click("xpath", "//input[@id='combobox-input-beneficiarytype']")
					# 输入信用证类型，模糊查询
					input("xpath", "//input[@id='combobox-input-beneficiarytype']", "内部组织")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-beneficiarytype']")
					input_enter("xpath", "//input[@id='combobox-input-beneficiarytype']")
					time.sleep(1)
					
					# 选择受益人
					click("xpath", "//input[@id='combobox-input-beneficiaryorgid']")
					# 输入信用证类型，模糊查询
					input("xpath", "//input[@id='combobox-input-beneficiaryorgid']", "亚唐科技")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-beneficiaryorgid']")
					input_enter("xpath", "//input[@id='combobox-input-beneficiaryorgid']")
					time.sleep(1)
				else:
					# 选择受益人类型
					click("xpath", "//input[@id='combobox-input-beneficiarytype']")
					# 输入信用证类型，模糊查询
					input("xpath", "//input[@id='combobox-input-beneficiarytype']", "交易对手")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-beneficiarytype']")
					input_enter("xpath", "//input[@id='combobox-input-beneficiarytype']")
					time.sleep(1)
					
					# 输入受益人
					input("xpath", "//input[@id='beneficiary']", "Mindy科技有限公司")
					sleep(1)
				
				# 选择保函类型
				click("xpath", "//input[@id='combobox-input-guaranteetypeid']")
				# 输入信用证类型，模糊查询
				input("xpath", "//input[@id='combobox-input-guaranteetypeid']", "106-保函")
				sleep(1)
				click("xpath", "//div[@title='代码-名称:106-保函']")
				sleep(1)
				
				# 选择担保银行
				click("xpath", "//input[@id='combobox-input-issuingbankid']")
				# 输入信用证类型，模糊查询
				input("xpath", "//input[@id='combobox-input-issuingbankid']", "中国银行")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-issuingbankid']")
				input_enter("xpath", "//input[@id='combobox-input-issuingbankid']")
				time.sleep(1)
				
				if i == 1:
					
					# 选择开立方式
					click("xpath", "//input[@id='combobox-input-issuetype']")
					# 输入信用证类型，模糊查询
					input("xpath", "//input[@id='combobox-input-issuetype']", "直开")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-issuetype']")
					input_enter("xpath", "//input[@id='combobox-input-issuetype']")
					time.sleep(1)
				else:
					# 选择开立方式
					click("xpath", "//input[@id='combobox-input-issuetype']")
					# 输入信用证类型，模糊查询
					input("xpath", "//input[@id='combobox-input-issuetype']", "转开")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-issuetype']")
					input_enter("xpath", "//input[@id='combobox-input-issuetype']")
					time.sleep(1)
				
				# 选择币种
				click("xpath", "//input[@id='combobox-input-currencyid']")
				# 输入信用证类型，模糊查询
				input("xpath", "//input[@id='combobox-input-currencyid']", "CNY")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-currencyid']")
				input_enter("xpath", "//input[@id='combobox-input-currencyid']")
				time.sleep(1)
				
				# 输入保函金额
				input("xpath", "//input[@id='guaranteeamount-input']", "3000")
				sleep(1)
				
				# 输入担保天数
				input("xpath", "//input[@id='guaranteedays-input']", "100")
				sleep(1)
				
				if i == 1:
					# 选择保证金担保方式
					click("xpath", "//input[@id='combobox-input-bailtype']")
					# 输入信用证类型，模糊查询
					input("xpath", "//input[@id='combobox-input-bailtype']", "票据质押保证")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-bailtype']")
					input_enter("xpath", "//input[@id='combobox-input-bailtype']")
					time.sleep(1)
					
					# 选择授信协议
					click("xpath", "//input[@id='combobox-input-creditid']")
					# 输入信用证类型，模糊查询
					input("xpath", "//input[@id='combobox-input-creditid']", "ZDHXYH")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-creditid']")
					input_enter("xpath", "//input[@id='combobox-input-creditid']")
					time.sleep(1)
				
				else:
					# 选择保证金担保方式
					click("xpath", "//input[@id='combobox-input-bailtype']")
					# 输入信用证类型，模糊查询
					input("xpath", "//input[@id='combobox-input-bailtype']", "一定比例保证金")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-bailtype']")
					input_enter("xpath", "//input[@id='combobox-input-bailtype']")
					time.sleep(1)
					
					# 选择授信协议
					click("xpath", "//input[@id='combobox-input-creditid']")
					# 输入信用证类型，模糊查询
					input("xpath", "//input[@id='combobox-input-creditid']", "ZDHZYFXYH")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-creditid']")
					input_enter("xpath", "//input[@id='combobox-input-creditid']")
					time.sleep(1)
					
					# 填写授信占用信息
					# 点击授新增行，新增第一行
					click("xpath", "//span[@title='额度']/ancestor::*[6]/following-sibling::*[2]/descendant::*[7]")
					sleep(1)
					# 输入授信方式
					click("xpath", "//input[@id='combobox-input-sumcontrolgrid-guaranteetype-0']")
					sleep(1)
					input("xpath", "//input[@id='combobox-input-sumcontrolgrid-guaranteetype-0']", "信用")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-sumcontrolgrid-guaranteetype-0']")
					input_enter("xpath", "//input[@id='combobox-input-sumcontrolgrid-guaranteetype-0']")
					time.sleep(1)
					click("xpath", "//input[@id='combobox-input-sumcontrolgrid-guaranteetype-0']")
					sleep(1)
					# 输入占用额度sumcontrolgrid-transamount-0-input
					click("xpath", "//input[@id='sumcontrolgrid-transamount-0-input']")
					sleep(1)
					clear("xpath", "//input[@id='sumcontrolgrid-transamount-0-input']")
					sleep(1)
					input("xpath", "//input[@id='sumcontrolgrid-transamount-0-input']", "1000")
					sleep(1)
					# 授信占用信息新增第二行
					click("xpath", "//span[@title='额度']/ancestor::*[6]/following-sibling::*[2]/descendant::*[7]")
					sleep(1)
					# 输入授信方式
					click("xpath", "//input[@id='combobox-input-sumcontrolgrid-guaranteetype-1']")
					sleep(1)
					input("xpath", "//input[@id='combobox-input-sumcontrolgrid-guaranteetype-1']", "抵押")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-sumcontrolgrid-guaranteetype-1']")
					input_enter("xpath", "//input[@id='combobox-input-sumcontrolgrid-guaranteetype-1']")
					time.sleep(1)
					click("xpath", "//input[@id='combobox-input-sumcontrolgrid-guaranteetype-1']")
					sleep(1)
					# 输入占用额度
					click("xpath", "//input[@id='sumcontrolgrid-transamount-1-input']")
					sleep(1)
					clear("xpath", "//input[@id='sumcontrolgrid-transamount-1-input']")
					sleep(1)
					input("xpath", "//input[@id='sumcontrolgrid-transamount-1-input']", "2000")
					sleep(1)
				
				# 点击保存按钮
				click("xpath", "//span[text()='保存']")
				
				# 退出所有iframe窗体
				switch_default()
				
				# 用隐式等待方法等页面出现提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				print("委托方保函管理第%s次，保存成功！" % i)
				logging.info("委托方保函管理第%s次，保存成功！" % i)
				time.sleep(3)
				
				# 第一笔，就先修改，再删除新建的‘委托方保函管理’
				if i == 1:
					# 切入‘委托方保函管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='prinLOGuarantees-tab-iframe']")
					
					# 点击查看
					# 用JS的方法点击放大镜
					js_click("xpath", "//span[@class='f-contrac-close']")
					sleep(1)
					
					# 输入支票号：WTBH
					input("xpath", "//input[@id='guaranteenumber']", "WTBH")
					sleep(1)
					
					# 修改保函金额
					click("xpath", "//input[@id='combobox-input-beneficiarytype']")
					sleep(1)
					input("xpath", "//input[@id='combobox-input-beneficiarytype']", "内部组织")
					sleep(1)
					click("xpath", "//div[@title='内部组织']")
					
					# 点击查询
					click("xpath", "//span[text()='查询']")
					
					# 修改
					# 勾选
					# MySQL 环境
					click("xpath", "//div[contains(text(),'WTBH')]/parent::*/preceding-sibling::*[3]/descendant::*[2]")
					
					# 点击修改按钮
					click("xpath", "//span[text()='修改']")
					
					# 切入修改的iframe窗体
					switch_to("xpath", "//iframe[@id='modWin-iframe']")
					sleep(1)
					
					# 修改保函金额
					click("xpath", "//input[@id='guaranteeamount-input']")
					sleep(1)
					clear("xpath", "//input[@id='guaranteeamount-input']")
					sleep(1)
					input("xpath", "//input[@id='guaranteeamount-input']", "20000")
					sleep(1)
					
					# 点击保存按钮
					click("xpath", "//span[text()='保存']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("委托方保函管理，修改成功！")
					logging.info("委托方保函管理，修改成功！")
					time.sleep(3)
					
					# 切入‘委托方保函管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='prinLOGuarantees-tab-iframe']")
					
					# 删除
					# 勾选
					click("xpath", "//div[contains(text(),'WTBH')]/parent::*/preceding-sibling::*[3]/descendant::*[2]")
					
					# 点击删除按钮
					click("xpath", "//span[text()='删除']")
					
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现删除的提示框
					implici_wait("xpath", "//span[contains(text(),'成功删除1条!')]")
					print("委托方保函管理，删除成功！")
					logging.info("委托方保函管理，删除成功！")
					time.sleep(3)
				
				# 第二笔，先审核、再取消审核、再托收、再托收到账
				elif i == 2:
					
					# 第一次审核
					# 切入‘委托方保函管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='prinLOGuarantees-tab-iframe']")
					
					# 修改保函金额
					click("xpath", "//input[@id='combobox-input-beneficiarytype']")
					sleep(1)
					
					click("xpath", "//div[@title='交易对手']")
					
					# 点击查询
					click("xpath", "//span[text()='查询']")
					sleep(1)
					
					# # 点击查询
					# click("xpath", "//span[text()='保函编号']")
					# sleep(1)
					
					# 勾选
					click("xpath", "//div[contains(text(),'WTBH')]/parent::*/preceding-sibling::*[3]/descendant::*[2]")
					# 点击审核按钮
					click("xpath", "//span[text()='审核']")
					
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'保函审核成功1条!')]")
					print("委托方保函管理，第一次审核成功！")
					logging.info("委托方保函管理，第一次审核成功！")
					time.sleep(3)
					
					# 取消审核
					# 切入‘委托方保函管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='prinLOGuarantees-tab-iframe']")
					
					# 勾选
					click("xpath", "//div[contains(text(),'WTBH')]/parent::*/preceding-sibling::*[3]/descendant::*[2]")
					
					# 用JS方便点击‘审核’按钮旁边的倒三角形
					js_click("xpath", "//span[text()='审核']/parent::*/following-sibling::*/child::*")
					sleep(1)
					
					# 点击取消审核按钮
					js_click("xpath", "//a[contains(text(),'取消审核')]")
					sleep(1)
					
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'保函取消审核成功1条!')]")
					print("委托方保函管理，取消审核成功！")
					logging.info("委托方保函管理，取消审核成功！")
					time.sleep(3)
					
					# 第二次审核
					# 切入‘委托方保函管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='prinLOGuarantees-tab-iframe']")
					
					# 勾选
					click("xpath", "//div[contains(text(),'WTBH')]/parent::*/preceding-sibling::*[3]/descendant::*[2]")
					
					# 点击审核按钮
					click("xpath", "//span[text()='审核']")
					
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'保函审核成功1条!')]")
					print("委托方保函管理，第二次审核成功！")
					logging.info("委托方保函管理，第二次审核成功！")
					time.sleep(3)
					
					# 变更
					# 切入‘委托方保函管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='prinLOGuarantees-tab-iframe']")
					
					# 勾选
					click("xpath", "//div[contains(text(),'WTBH')]/parent::*/preceding-sibling::*[3]/descendant::*[2]")
					
					# 用JS方便点击‘交单’
					js_click("xpath", "//span[text()='变更']")
					sleep(1)
					
					# 切入变更的窗体页面
					switch_to("xpath", "//iframe[@id='modWin-iframe']")
					
					# 修改保函金额
					click("xpath", "//input[@id='guaranteeamount-input']")
					sleep(1)
					clear("xpath", "//input[@id='guaranteeamount-input']")
					sleep(1)
					input("xpath", "//input[@id='guaranteeamount-input']", "3000")
					sleep(1)
					
					# 填写授信占用信息
					# 点击授新增行，新增第一行
					click("xpath", "//span[contains(text(),'授信占用信息')]")
					sleep(1)
					click("xpath", "//span[@title='额度']/ancestor::*[6]/following-sibling::*[2]/descendant::*[7]")
					sleep(1)
					# 输入授信方式
					click("xpath", "//input[@id='combobox-input-sumcontrolgrid-guaranteetype-0']")
					sleep(1)
					input("xpath", "//input[@id='combobox-input-sumcontrolgrid-guaranteetype-0']", "信用")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-sumcontrolgrid-guaranteetype-0']")
					input_enter("xpath", "//input[@id='combobox-input-sumcontrolgrid-guaranteetype-0']")
					time.sleep(1)
					
					# 点击确定按钮
					click("xpath", "//span[text()='保存']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("委托方保函管理，变更成功！")
					logging.info("委托方保函管理，变更成功！")
					sleep(3)
					
					# 到期关闭
					# 切入‘委托方保函管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='prinLOGuarantees-tab-iframe']")
					
					# 勾选
					click("xpath", "//div[contains(text(),'WTBH')]/parent::*/preceding-sibling::*[3]/descendant::*[2]")
					
					# 用JS方便点击‘到期关闭’
					js_click("xpath", "//span[text()='到期关闭']")
					sleep(1)
					
					click("xpath", "//span[text()='确定']")
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'保函到期关闭成功1条!')]")
					print("委托方保函管理，到期关闭成功！")
					logging.info("委托方保函管理，到期关闭成功！")
					sleep(3)
					
					# 操作记录
					# 切入‘委托方保函管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='prinLOGuarantees-tab-iframe']")
					
					# 勾选
					click("xpath", "//div[contains(text(),'WTBH')]/parent::*/preceding-sibling::*[3]/descendant::*[2]")
					
					# 用JS方便点击‘交单’
					js_click("xpath", "//span[text()='操作记录']")
					sleep(1)
					
					# 切入操作记录的窗体页面
					switch_to("xpath", "//iframe[@id='operationWin-iframe']")
					
					# 用隐式等待方法等页面出现预期数据：title="保函编号:BH01"
					implici_wait("xpath", "//div[contains(text(),'WTBH')]")
					print("委托方保函管理查看成功！")
					time.sleep(3)
			
			# 退出所有iframe窗体
			switch_default()
			
			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='委托方保函管理']/child::*[1]")
			
			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//span[@title='保函管理']")
			
			# 打印操作成功日志
			print("委托方保函管理，操作成功!")
			logging.info("委托方保函管理，操作成功!")
			time.sleep(2)
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("委托方保函管理,失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		
		# 测试委托方保函查看
		try:
			# 点击保函管理菜单
			click("xpath", "//span[@title='保函管理']")
			# 点击应收支票登记菜单
			click("xpath", "//span[@title='委托方保函查看']")
			# 退出所有的iframe窗体
			switch_default()
			logging.info("开始测试委托方保函查看功能")
			
			# 切入‘委托方保函查看’的iframe窗体
			switch_to("xpath", "//iframe[@id='prinLOGuaranteesView-tab-iframe']")
			
			# 点击查看
			# 用JS的方法点击放大镜
			js_click("xpath", "//span[@class='f-contrac-close']")
			sleep(1)
			
			click("xpath", "//input[@id='guaranteenumber']")
			
			# 输入内容
			input("xpath", "//input[@id='guaranteenumber']", "WTBH")
			sleep(1)
			# 点击查询
			click("xpath", "//span[text()='查询']")
			
			# 用隐式等待方法等页面出现预期数据：受益人:Mindy科技有限公司
			implici_wait("xpath", "//div[@title='受益人:Mindy科技有限公司']")
			print("委托方保函查看成功！")
			time.sleep(3)
			
			# 退出所有iframe窗体
			switch_default()
			
			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='委托方保函查看']/child::*[1]")
			
			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//span[@title='保函管理']")
			
			# 打印操作成功日志
			print("委托方保函查看，操作成功!")
			logging.info("委托方保函查看，操作成功!")
			time.sleep(2)
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("委托方保函查看,失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		"""
		# 测试受益方保函管管理
		try:
			# 点击保函管理菜单
			click("xpath", "//span[@title='保函管理']")
			# 点击应收支票登记菜单
			click("xpath", "//span[@title='受益方保函管理']")
			# 退出所有的iframe窗体
			switch_default()
			logging.info("开始测试受益方保函管理功能")
			for i in range(1, 3):
				# 切入‘信用证收证管理’的iframe窗体
				switch_to("xpath", "//iframe[@id='benLOGuarantees-tab-iframe']")
				# 用JS的方法点击新增按钮
				js_click("xpath", "//span[text()='新增']")
				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='addWin-iframe']")
				sleep(1)
				
				# 选择委托人
				# 点击‘部门’框
				click("xpath", "//input[@id='entruster']")
				# 输入自动化测试部，模糊查询
				input("xpath", "//input[@id='entruster']", "Mindy科技有限公司")
				sleep(1)
				input_down("xpath", "//input[@id='entruster']")
				input_enter("xpath", "//input[@id='entruster']")
				time.sleep(1)
				
				# 设置时间的变成存储，变成
				temp1 = time.strftime("%H%M%S")
				# 输入保函编号
				click("xpath", "//span[text()='保函编号']/ancestor::*[2]/descendant::*[6]/descendant::*[1]")
				sleep(1)
				input("xpath", "//span[text()='保函编号']/ancestor::*[2]/descendant::*[6]/descendant::*[1]","SYBH" + str(temp1))
				sleep(1)
				
				# 选择保函类型
				click("xpath", "//input[@id='combobox-input-guaranteetypeid']")
				# 输入信用证类型，模糊查询
				input("xpath", "//input[@id='combobox-input-guaranteetypeid']", "106-保函")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-guaranteetypeid']")
				input_enter("xpath", "//input[@id='combobox-input-guaranteetypeid']")
				time.sleep(1)
				
				# 选择担保类型
				click("xpath", "//input[@id='combobox-input-financialinstitutiontype']")
				# 输入信用证类型，模糊查询
				input("xpath", "//input[@id='combobox-input-financialinstitutiontype']", "银行")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-financialinstitutiontype']")
				input_enter("xpath", "//input[@id='combobox-input-financialinstitutiontype']")
				time.sleep(1)
				
				# 选择担保机构
				click("xpath", "//input[@id='combobox-input-issuingbankid']")
				# 输入信用证类型，模糊查询
				input("xpath", "//input[@id='combobox-input-issuingbankid']", "中国银行")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-issuingbankid']")
				input_enter("xpath", "//input[@id='combobox-input-issuingbankid']")
				time.sleep(1)
				
				if i == 1:
					
					# 选择开立方式
					click("xpath", "//input[@id='combobox-input-issuetype']")
					# 输入信用证类型，模糊查询
					input("xpath", "//input[@id='combobox-input-issuetype']", "直开")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-issuetype']")
					input_enter("xpath", "//input[@id='combobox-input-issuetype']")
					time.sleep(1)
				else:
					# 选择开立方式
					click("xpath", "//input[@id='combobox-input-issuetype']")
					# 输入信用证类型，模糊查询
					input("xpath", "//input[@id='combobox-input-issuetype']", "转开")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-issuetype']")
					input_enter("xpath", "//input[@id='combobox-input-issuetype']")
					time.sleep(1)
				
				# 输入合同号
				input("xpath", "//input[@id='contractno']", "SYHT001")
				sleep(1)
				
				# 输入业务申请人
				input("xpath", "//input[@id='applyoperator']", "Mindy")
				sleep(1)
				
				# 选择币种
				click("xpath", "//input[@id='combobox-input-currencyid']")
				# 输入信用证类型，模糊查询
				input("xpath", "//input[@id='combobox-input-currencyid']", "CNY")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-currencyid']")
				input_enter("xpath", "//input[@id='combobox-input-currencyid']")
				time.sleep(1)
				
				# 输入保函金额
				input("xpath", "//input[@id='guaranteeamount-input']", "20000")
				sleep(1)
				
				# 输入担保天数
				input("xpath", "//input[@id='guaranteedays-input']", "100")
				sleep(1)
				
				# 点击保存按钮
				click("xpath", "//span[text()='保存']")
				
				# 退出所有iframe窗体
				switch_default()
				
				# 用隐式等待方法等页面出现提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				print("受益方保函管理第%s次，保存成功！" % i)
				logging.info("受益方保函管理管理第%s次，保存成功！" % i)
				time.sleep(3)
				
				# 第一笔，就先修改，再删除新建的‘受益方保函管理’
				if i == 1:
					# 切入‘受益方保函管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='benLOGuarantees-tab-iframe']")
					
					# 点击查看
					# 用JS的方法点击放大镜
					js_click("xpath", "//span[@class='f-contrac-close']")
					sleep(1)
					
					# 输入支票号：SYBH
					input("xpath", "//input[@id='guaranteenumber']", "SYBH")
					sleep(1)
					
					# 点击查询
					click("xpath", "//span[text()='查询']")
					sleep(1)
					
					# 点击保函编号
					click("xpath", "//span[text()='保函编号']")
					sleep(1)
					
					# 修改
					# 勾选
					click("xpath", "//div[contains(text(),'SYBH')]/parent::*/preceding-sibling::*[3]/descendant::*[2]")
					
					# 点击修改按钮
					click("xpath", "//span[text()='修改']")
					
					# 切入修改的iframe窗体
					switch_to("xpath", "//iframe[@id='modWin-iframe']")
					sleep(1)
					
					# 修改保函金额
					click("xpath", "//input[@id='guaranteeamount-input']")
					sleep(1)
					clear("xpath", "//input[@id='guaranteeamount-input']")
					sleep(1)
					input("xpath", "//input[@id='guaranteeamount-input']", "20000")
					sleep(1)
					
					# 点击保存按钮
					click("xpath", "//span[text()='保存']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("受益方保函管理，修改成功！")
					logging.info("受益方保函管理，修改成功！")
					time.sleep(3)
					
					# 切入‘受益方保函管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='benLOGuarantees-tab-iframe']")
					
					# 删除
					# 勾选
					click("xpath", "//div[contains(text(),'SYBH')]/parent::*/preceding-sibling::*[3]/descendant::*[2]")
					
					# 点击删除按钮
					click("xpath", "//span[text()='删除']")
					
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现删除的提示框
					implici_wait("xpath", "//span[contains(text(),'成功删除1条!')]")
					print("受益方保函管理，删除成功！")
					logging.info("受益方保函管理，删除成功！")
					time.sleep(3)
				
				# 第二笔，先审核、再取消审核、再托收、再托收到账
				elif i == 2:
					
					# 第一次审核
					# 切入‘受益方保函管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='benLOGuarantees-tab-iframe']")
					
					# 勾选
					click("xpath", "//div[contains(text(),'SYBH')]/parent::*/preceding-sibling::*[3]/descendant::*[2]")
					
					# 点击审核按钮
					click("xpath", "//span[text()='审核']")
					
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'保函审核成功1条!')]")
					print("受益方保函管理，第一次审核成功！")
					logging.info("受益方保函管理，第一次审核成功！")
					time.sleep(3)
					
					# 取消审核
					# 切入‘受益方保函管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='benLOGuarantees-tab-iframe']")
					
					# 勾选
					click("xpath", "//div[contains(text(),'SYBH')]/parent::*/preceding-sibling::*[3]/descendant::*[2]")
					
					# 用JS方便点击‘审核’按钮旁边的倒三角形
					js_click("xpath", "//span[text()='审核']/parent::*/following-sibling::*/child::*")
					sleep(1)
					
					# 点击取消审核按钮
					js_click("xpath", "//a[contains(text(),'取消审核')]")
					sleep(1)
					
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'保函取消审核成功1条!')]")
					print("受益方保函管理，取消审核成功！")
					logging.info("受益方保函管理，取消审核成功！")
					time.sleep(3)
					
					# 第二次审核
					# 切入‘受益方保函管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='benLOGuarantees-tab-iframe']")
					
					# 勾选
					click("xpath", "//div[contains(text(),'SYBH')]/parent::*/preceding-sibling::*[3]/descendant::*[2]")
					
					# 点击审核按钮
					click("xpath", "//span[text()='审核']")
					
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'保函审核成功1条!')]")
					print("受益方保函管理，第二次审核成功！")
					logging.info("受益方保函管理，第二次审核成功！")
					time.sleep(3)
					
					# 变更
					# 切入‘受益方保函管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='benLOGuarantees-tab-iframe']")
					
					# 勾选
					click("xpath", "//div[contains(text(),'SYBH')]/parent::*/preceding-sibling::*[3]/descendant::*[2]")
					
					# 用JS方便点击‘交单’
					js_click("xpath", "//span[text()='变更']")
					sleep(1)
					
					# 切入变更的窗体页面
					switch_to("xpath", "//iframe[@id='modWin-iframe']")
					
					# 修改保函金额
					click("xpath", "//input[@id='guaranteeamount-input']")
					sleep(1)
					clear("xpath", "//input[@id='guaranteeamount-input']")
					sleep(1)
					input("xpath", "//input[@id='guaranteeamount-input']", "40000")
					sleep(1)
					
					# 点击确定按钮
					click("xpath", "//span[text()='保存']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("委托方保函管理，变更成功！")
					logging.info("委托方保函管理，变更成功！")
					sleep(3)
					
					# 到期关闭
					# 切入‘委托方保函管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='benLOGuarantees-tab-iframe']")
					
					# 勾选
					click("xpath", "//div[contains(text(),'SYBH')]/parent::*/preceding-sibling::*[3]/descendant::*[2]")
					
					# 用JS方便点击‘到期关闭’
					js_click("xpath", "//span[text()='到期关闭']")
					sleep(1)
					
					click("xpath", "//span[text()='确定']")
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("委托方保函管理，到期关闭成功！")
					logging.info("委托方保函管理，到期关闭成功！")
					sleep(3)
					
					# 操作记录
					# 切入‘委托方保函管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='benLOGuarantees-tab-iframe']")
					
					# 勾选
					click("xpath", "//div[contains(text(),'SYBH')]/parent::*/preceding-sibling::*[3]/descendant::*[2]")
					
					# 用JS方便点击‘交单’
					js_click("xpath", "//span[text()='操作记录']")
					sleep(1)
					
					# 切入操作记录的窗体页面
					switch_to("xpath", "//iframe[@id='operationWin-iframe']")
					
					# 用隐式等待方法等页面出现预期数据：title="保函编号:BH01"
					implici_wait("xpath", "//div[contains(text(),'SYBH')]")
					print("受益方保函管理查看成功！")
					time.sleep(3)
			
			# 退出所有iframe窗体
			switch_default()
			
			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='受益方保函管理']/child::*[1]")
			
			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//span[@title='保函管理']")
			
			# 打印操作成功日志
			print("受益方保函管理，操作成功!")
			logging.info("受益方保函管理，操作成功!")
			time.sleep(2)
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("受益方保函管理,失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		
		# 测试受益方保函查看
		try:
			# 点击保函管理菜单
			click("xpath", "//span[@title='保函管理']")
			# 点击应收支票登记菜单
			click("xpath", "//span[@title='受益方保函查看']")
			# 退出所有的iframe窗体
			switch_default()
			logging.info("开始测试受益方保函查看功能")
			
			# 切入‘委托方保函查看’的iframe窗体
			switch_to("xpath", "//iframe[@id='benLOGuaranteesView-tab-iframe']")
			
			# 点击查看
			# 用JS的方法点击放大镜
			js_click("xpath", "//span[@class='f-contrac-close']")
			sleep(1)
			
			click("xpath", "//input[@id='guaranteenumber']")
			
			# 输入内容
			input("xpath", "//input[@id='guaranteenumber']", "SYBH")
			sleep(1)
			# 点击查询
			click("xpath", "//span[text()='查询']")
			
			# 用隐式等待方法等页面出现预期数据：受益人:Mindy科技有限公司
			implici_wait("xpath", "//div[@title='委托方:Mindy科技有限公司']")
			print("受益方保函查看成功！")
			time.sleep(3)
			
			# 退出所有iframe窗体
			switch_default()
			
			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='受益方保函查看']/child::*[1]")
			
			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//span[@title='保函管理']")
			
			# 打印操作成功日志
			print("受益方保函查看，操作成功!")
			logging.info("受益方保函查看，操作成功!")
			time.sleep(2)
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("受益方保函查看,失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		
		# def tearDown(self):
		#     self.driver.quit()
		print("结束时间：", time.strftime("%Y-%m-%d %H:%M:%S"))


if __name__ == '__main__':
	#  启动单元测试
	unittest.main(verbosity=2)
