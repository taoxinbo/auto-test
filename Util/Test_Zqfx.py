# encoding=utf-8
# @Time : 2020/8/14 14:49
# @Author : Mindy
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

# print("开始时间：",time.strftime("%Y-%m-%d %H:%M:%S"))

driver = ""


class Test_Zqfx(unittest.TestCase):
	
	# 启动浏览器
	def setUp(self):
		
		# 启动浏览器的另外一个方法：通过封装启动浏览器的驱动，启动不同浏览器
		self.driver = get("chrome")
	
	# 登陆系统、对系统设置进行操作
	def test_trade(self):
		
		# 通过登陆封装函数，进行登陆
		# login( G_Ora_Url,TestUser,Password, "自动化测试租户")
		# login( G_Ora_Url,Tao, Password,"默认租户")
		login(G_Ora_Url, mindy, Password, "亚唐科技")
		# login(G_Ora_Url, mindy, Password, "Mindy")
		# login( G_Mys_Url,TestUser,Password, "自动化测试租户")
		# login(G_Mys_Url, Tao, Password, "亚唐科技")
		# login(G_Mys_Url, mindy, Password, "亚唐科技")
		# login(G_Mys_Url, judy, Password, "默认租户")
		
		logging.info("开始测试债券发行管理的页面功能")
		# 将页面的滚动条滑动到‘债券发行管理’页面的地方
		js_gd("xpath", "//span[contains(text(),'债券发行管理')]")
		# 用JS的方法点击债券发行管理菜单按钮
		js_click("xpath", "//span[contains(text(),'债券发行管理')]")
		"""
		# 测试基础设置--监管机构
		try:
			# 点击基础设置菜单
			click("xpath", "//li[@f_value='bondissuancesetting']/descendant-or-self::*[5]")
			# 点击监管机构菜单
			click("xpath", "//li[@f_value='bondregisterorg']/descendant-or-self::*[5]")
			# 退出所有iframe窗体
			switch_default()

			for i in range(1, 3):
				# 切入监管机构的iframe窗体
				switch_to("xpath", "//iframe[@id='bondregisterorg-tab-iframe']")
				logging.info("开始测试监管机构功能")

				# 用JS的方法点击新增按钮
				js_click("xpath", "//span[text()='新增']")

				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='addWin-iframe']")
				sleep(1)

				# 输入代码
				input("xpath", "//input[@name='code']", "TestReg")
				sleep(1)

				# 输入的名称
				input("xpath", "//input[@id='name']", "自动化测试监管机构")
				sleep(1)

				# 描述框中填入值
				input("xpath", "//textarea[@id='description']", "自动化测试监管机构描述框")
				sleep(1)

				# 点击保存按钮
				click("xpath", "//span[text()='保存']")

				# 退出所有iframe窗体
				switch_default()

				# 用隐式等待方法等页面出现新增成功的提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				print("监管机构，保存成功！")
				time.sleep(3)

				if i == 1:
					# 删除功能
					# 切入监管机构的iframe窗体
					switch_to("xpath", "//iframe[@id='bondregisterorg-tab-iframe']")

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
					click("xpath", "//div[@title='代码:TestReg']/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 点击删除按钮
					click("xpath", "//span[text()='删除']")

					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现删除的提示框
					implici_wait("xpath", "//span[contains(text(),'成功删除')]")
					print("监管机构，删除成功！")
					time.sleep(3)

			# 切入‘监管机构’的iframe窗体
			switch_to("xpath", "//iframe[@id='bondregisterorg-tab-iframe']")

			# 点击查看
			# 清空代码框的内容
			clear("xpath", "//input[@id='code']")
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
			print("监管机构，修改成功！")
			time.sleep(3)

			# 切入‘监管机构’的iframe窗体
			switch_to("xpath", "//iframe[@id='bondregisterorg-tab-iframe']")

			# 失效按钮
			# 勾选
			click("xpath", "//div[@title='代码:TestReg']/parent::*/preceding-sibling::*[1]/descendant::*[2]")

			# 点击失效按钮
			click("xpath", "//span[text()='失效']")

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'失效成功！')]")
			print("监管机构，点击失效成功！")
			time.sleep(3)

			# 切入‘监管机构’的iframe窗体
			switch_to("xpath", "//iframe[@id='bondregisterorg-tab-iframe']")

			# 生效按钮
			# 勾选
			click("xpath", "//div[@title='代码:TestReg']/parent::*/preceding-sibling::*[1]/descendant::*[2]")

			# 点击生效按钮
			click("xpath", "//span[text()='生效']")

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'生效成功！')]")
			print("监管机构，点击生效成功！")
			time.sleep(3)

			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='监管机构']/child::*[1]")

			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//li[@f_value='bondissuancesetting']/descendant-or-self::*[5]")

			# 打印操作成功日志
			print("监管机构，操作成功!")
			logging.info("监管机构，操作成功!")
			time.sleep(2)
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("监管机构失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)

		# 测试基础设置--评级机构
		try:
			# 点击基础设置菜单
			click("xpath", "//li[@f_value='bondissuancesetting']/descendant-or-self::*[5]")
			# 点击评级机构菜单
			click("xpath", "//span[text()='评级机构']")
			# 退出所有iframe窗体
			switch_default()

			for i in range(1, 3):
				# 切入评级机构的iframe窗体
				switch_to("xpath", "//iframe[@id='bondratingagency-tab-iframe']")
				logging.info("开始测试评级机构功能")

				# 用JS的方法点击新增按钮
				js_click("xpath", "//span[text()='新增']")

				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='addWin-iframe']")
				sleep(1)

				# 输入代码
				input("xpath", "//input[@name='code']", "TestRat")
				sleep(1)

				# 输入的名称
				input("xpath", "//input[@id='name']", "自动化测试评级机构")
				sleep(1)

				# 描述框中填入值
				input("xpath", "//textarea[@id='description']", "自动化测试评级机构描述框")
				sleep(1)

				# 点击保存按钮
				click("xpath", "//span[text()='保存']")

				# 退出所有iframe窗体
				switch_default()

				# 用隐式等待方法等页面出现提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				print("评级机构，保存成功！")
				time.sleep(3)

				if i == 1:
					# 删除功能
					# 切入评级机构的iframe窗体
					switch_to("xpath", "//iframe[@id='bondratingagency-tab-iframe']")

					# 点击查看
					# 用JS的方法点击放大镜
					js_click("xpath", "//span[@class='f-contrac-close']")
					sleep(1)

					# 输入代码：
					input("xpath", "//input[@id='code']", "TestRat")
					sleep(1)

					# 点击查询
					click("xpath", "//span[text()='查询']")

					# 勾选
					click("xpath", "//div[@title='代码:TestRat']/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 点击删除按钮
					click("xpath", "//span[text()='删除']")

					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现删除的提示框
					implici_wait("xpath", "//span[contains(text(),'成功删除')]")
					print("评级机构，删除成功！")
					time.sleep(3)

			# 切入‘监管机构’的iframe窗体
			switch_to("xpath", "//iframe[@id='bondratingagency-tab-iframe']")

			# 点击查看
			# 清空代码框的内容
			clear("xpath", "//input[@id='code']")
			sleep(1)

			# 输入代码：
			input("xpath", "//input[@id='code']", "TestRat")
			sleep(1)

			# 点击查询
			click("xpath", "//span[text()='查询']")

			# 修改
			# 勾选
			click("xpath", "//div[@title='代码:TestRat']/parent::*/preceding-sibling::*[1]/descendant::*[2]")

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
			print("评级机构，修改成功！")
			time.sleep(3)

			# 切入‘评级机构’的iframe窗体
			switch_to("xpath", "//iframe[@id='bondratingagency-tab-iframe']")

			# 失效按钮
			# 勾选
			click("xpath", "//div[@title='代码:TestRat']/parent::*/preceding-sibling::*[1]/descendant::*[2]")

			# 点击失效按钮
			click("xpath", "//span[text()='失效']")

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'失效成功！')]")
			print("评级机构，点击失效成功！")
			time.sleep(3)

			# 切入‘评级机构’的iframe窗体
			switch_to("xpath", "//iframe[@id='bondratingagency-tab-iframe']")

			# 生效按钮
			# 勾选
			click("xpath", "//div[@title='代码:TestRat']/parent::*/preceding-sibling::*[1]/descendant::*[2]")

			# 点击生效按钮
			click("xpath", "//span[text()='生效']")

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'生效成功！')]")
			print("评级机构，点击生效成功！")
			time.sleep(3)

			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='评级机构']/child::*[1]")

			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//li[@f_value='bondissuancesetting']/descendant-or-self::*[5]")

			# 打印操作成功日志
			print("评级机构，操作成功!")
			logging.info("评级机构，操作成功!")
			time.sleep(2)
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("评级机构失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)

		# 测试基础设置--注册品种
		try:
			# 点击基础设置菜单
			click("xpath", "//li[@f_value='bondissuancesetting']/descendant-or-self::*[5]")
			# 点击评级机构菜单
			click("xpath", "//span[text()='注册品种']")
			# 退出所有iframe窗体
			switch_default()

			for i in range(1, 3):
				# 切入注册品种的iframe窗体
				switch_to("xpath", "//iframe[@id='bondregistervariety-tab-iframe']")
				logging.info("开始测试注册品种功能")

				# 用JS的方法点击新增按钮
				js_click("xpath", "//span[text()='新增']")

				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='addWin-iframe']")
				sleep(1)

				# 输入代码
				input("xpath", "//input[@name='code']", "TestZc")
				sleep(1)

				# 输入的名称
				input("xpath", "//input[@id='name']", "自动化测试注册品种")
				sleep(1)

				# 第二次新建的时候，期限品种选‘永续’
				if i == 2:
					# 点击‘期限品种’代码框
					click("xpath", "//input[@id='combobox-input-duration']")

					# 清空‘期限品种’代码框
					clear("xpath", "//input[@id='combobox-input-duration']")
					sleep(1)

					# 输入内容
					input("xpath", "//input[@id='combobox-input-duration']", "永续")
					sleep(1)

					# 确认回车
					input_enter("xpath", "//input[@id='combobox-input-duration']")

				# 描述框中填入值
				input("xpath", "//textarea[@id='description']", "自动化测试注册品种描述框")
				sleep(1)

				# 点击保存按钮
				click("xpath", "//span[text()='保存']")

				# 退出所有iframe窗体
				switch_default()

				# 用隐式等待方法等页面出现提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				print("注册品种，保存成功！")
				time.sleep(3)

				if i == 1:
					# 删除功能
					# 切入注册品种的iframe窗体
					switch_to("xpath", "//iframe[@id='bondregistervariety-tab-iframe']")

					# 点击查看
					# 用JS的方法点击放大镜
					js_click("xpath", "//span[@class='f-contrac-close']")
					sleep(1)

					# 输入代码：
					input("xpath", "//input[@id='code']", "TestZc")
					sleep(1)

					# 点击查询
					click("xpath", "//span[text()='查询']")

					# 勾选
					click("xpath", "//div[@title='代码:TestZc']/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 点击删除按钮
					click("xpath", "//span[text()='删除']")

					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现删除的提示框
					implici_wait("xpath", "//span[contains(text(),'成功删除')]")
					print("注册品种，删除成功！")
					time.sleep(3)

			# 切入‘注册品种’的iframe窗体
			switch_to("xpath", "//iframe[@id='bondregistervariety-tab-iframe']")

			# 点击查看
			# 清空代码框的内容
			clear("xpath", "//input[@id='code']")
			sleep(1)

			# 输入代码：
			input("xpath", "//input[@id='code']", "TestZc")
			sleep(1)

			# 点击查询
			click("xpath", "//span[text()='查询']")

			# 修改
			# 勾选
			click("xpath", "//div[@title='代码:TestZc']/parent::*/preceding-sibling::*[1]/descendant::*[2]")

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
			print("注册品种，修改成功！")
			time.sleep(3)

			# 切入‘注册品种’的iframe窗体
			switch_to("xpath", "//iframe[@id='bondregistervariety-tab-iframe']")

			# 失效按钮
			# 勾选
			click("xpath", "//div[@title='代码:TestZc']/parent::*/preceding-sibling::*[1]/descendant::*[2]")

			# 点击失效按钮
			click("xpath", "//span[text()='失效']")

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'失效成功！')]")
			print("注册品种，点击失效成功！")
			time.sleep(3)

			# 切入‘注册品种’的iframe窗体
			switch_to("xpath", "//iframe[@id='bondregistervariety-tab-iframe']")

			# 生效按钮
			# 勾选
			click("xpath", "//div[@title='代码:TestZc']/parent::*/preceding-sibling::*[1]/descendant::*[2]")

			# 点击生效按钮
			click("xpath", "//span[text()='生效']")

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'生效成功！')]")
			print("注册品种，点击生效成功！")
			time.sleep(3)

			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='注册品种']/child::*[1]")

			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//li[@f_value='bondissuancesetting']/descendant-or-self::*[5]")

			# 打印操作成功日志
			print("注册品种，操作成功!")
			logging.info("注册品种，操作成功!")
			time.sleep(2)
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("注册品种失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)

		# 测试基础设置--法律顾问
		try:
			# 点击基础设置菜单
			click("xpath", "//li[@f_value='bondissuancesetting']/descendant-or-self::*[5]")
			# 点击评级机构菜单
			click("xpath", "//span[text()='法律顾问']")
			# 退出所有iframe窗体
			switch_default()

			for i in range(1, 3):
				# 切入‘法律顾问’的iframe窗体
				switch_to("xpath", "//iframe[@id='bondlegaladviser-tab-iframe']")
				logging.info("开始测试法律顾问功能")

				# 用JS的方法点击新增按钮
				js_click("xpath", "//span[text()='新增']")

				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='addWin-iframe']")
				sleep(1)

				# 输入代码
				input("xpath", "//input[@name='code']", "TestLeg")
				sleep(1)

				# 输入的名称
				input("xpath", "//input[@id='name']", "自动化测试法律顾问")
				sleep(1)

				# 描述框中填入值
				input("xpath", "//textarea[@id='description']", "自动化测试法律顾问描述框")
				sleep(1)

				# 点击保存按钮
				click("xpath", "//span[text()='保存']")

				# 退出所有iframe窗体
				switch_default()

				# 用隐式等待方法等页面出现提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				print("法律顾问，保存成功！")
				time.sleep(3)

				if i == 1:
					# 删除功能
					# 切入‘法律顾问’的iframe窗体
					switch_to("xpath", "//iframe[@id='bondlegaladviser-tab-iframe']")

					# 点击查看
					# 用JS的方法点击放大镜
					js_click("xpath", "//span[@class='f-contrac-close']")
					sleep(1)

					# 输入代码：
					input("xpath", "//input[@id='code']", "TestLeg")
					sleep(1)

					# 点击查询
					click("xpath", "//span[text()='查询']")

					# 勾选
					click("xpath", "//div[@title='代码:TestLeg']/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 点击删除按钮
					click("xpath", "//span[text()='删除']")

					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现删除的提示框
					implici_wait("xpath", "//span[contains(text(),'成功删除')]")
					print("法律顾问，删除成功！")
					time.sleep(3)

			# 切入‘法律顾问’的iframe窗体
			switch_to("xpath", "//iframe[@id='bondlegaladviser-tab-iframe']")

			# 点击查看
			# 清空代码框的内容
			clear("xpath", "//input[@id='code']")
			sleep(1)

			# 输入代码：
			input("xpath", "//input[@id='code']", "TestLeg")
			sleep(1)

			# 点击查询
			click("xpath", "//span[text()='查询']")

			# 修改
			# 勾选
			click("xpath", "//div[@title='代码:TestLeg']/parent::*/preceding-sibling::*[1]/descendant::*[2]")

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
			print("法律顾问，修改成功！")
			time.sleep(3)

			# 切入‘法律顾问’的iframe窗体
			switch_to("xpath", "//iframe[@id='bondlegaladviser-tab-iframe']")

			# 失效按钮
			# 勾选
			click("xpath", "//div[@title='代码:TestLeg']/parent::*/preceding-sibling::*[1]/descendant::*[2]")

			# 点击失效按钮
			click("xpath", "//span[text()='失效']")

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'失效成功！')]")
			print("法律顾问，点击失效成功！")
			time.sleep(3)

			# 切入‘注册品种’的iframe窗体
			switch_to("xpath", "//iframe[@id='bondlegaladviser-tab-iframe']")

			# 生效按钮
			# 勾选
			click("xpath", "//div[@title='代码:TestLeg']/parent::*/preceding-sibling::*[1]/descendant::*[2]")

			# 点击生效按钮
			click("xpath", "//span[text()='生效']")

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'生效成功！')]")
			print("法律顾问，点击生效成功！")
			time.sleep(3)

			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='法律顾问']/child::*[1]")

			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//li[@f_value='bondissuancesetting']/descendant-or-self::*[5]")

			# 打印操作成功日志
			print("法律顾问，操作成功!")
			logging.info("法律顾问，操作成功!")
			time.sleep(2)
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("法律顾问失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)

		# 测试基础设置--资金用途
		try:
			# 点击基础设置菜单
			click("xpath", "//li[@f_value='bondissuancesetting']/descendant-or-self::*[5]")
			# 点击资金用途菜单
			click("xpath", "//span[text()='资金用途']")
			# 退出所有iframe窗体
			switch_default()

			for i in range(1, 3):
				# 切入‘资金用途’的iframe窗体
				switch_to("xpath", "//iframe[@id='bondpurpose-tab-iframe']")
				logging.info("开始测试‘资金用途’功能")

				# 用JS的方法点击新增按钮
				js_click("xpath", "//span[text()='新增']")

				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='addWin-iframe']")
				sleep(1)

				# 输入代码
				input("xpath", "//input[@name='code']", "TestBpur")
				sleep(1)

				# 输入的名称
				input("xpath", "//input[@id='name']", "自动化测试资金用途")
				sleep(1)

				# 描述框中填入值
				input("xpath", "//textarea[@id='description']", "自动化测试资金用途描述框")
				sleep(1)

				# 点击保存按钮
				click("xpath", "//span[text()='保存']")

				# 退出所有iframe窗体
				switch_default()

				# 用隐式等待方法等页面出现提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				print("资金用途，保存成功！")
				time.sleep(3)

				if i == 1:
					# 删除功能
					# 切入‘资金用途’的iframe窗体
					switch_to("xpath", "//iframe[@id='bondpurpose-tab-iframe']")

					# 点击查看
					# 用JS的方法点击放大镜
					js_click("xpath", "//span[@class='f-contrac-close']")
					sleep(1)

					# 输入代码：
					input("xpath", "//input[@id='code']", "TestBpur")
					sleep(1)

					# 点击查询
					click("xpath", "//span[text()='查询']")

					# 勾选
					click("xpath", "//div[@title='代码:TestBpur']/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 点击删除按钮
					click("xpath", "//span[text()='删除']")

					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现删除的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功')]")
					print("资金用途，删除成功！")
					time.sleep(3)

			# 切入‘资金用途’的iframe窗体
			switch_to("xpath", "//iframe[@id='bondpurpose-tab-iframe']")

			# 点击查看
			# 清空代码框的内容
			clear("xpath", "//input[@id='code']")
			sleep(1)

			# 输入代码：
			input("xpath", "//input[@id='code']", "TestBpur")
			sleep(1)

			# 点击查询
			click("xpath", "//span[text()='查询']")

			# 修改
			# 勾选
			click("xpath", "//div[@title='代码:TestBpur']/parent::*/preceding-sibling::*[1]/descendant::*[2]")

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
			print("资金用途，修改成功！")
			time.sleep(3)

			# 切入‘资金用途’的iframe窗体
			switch_to("xpath", "//iframe[@id='bondpurpose-tab-iframe']")

			# 失效按钮
			# 勾选
			click("xpath", "//div[@title='代码:TestBpur']/parent::*/preceding-sibling::*[1]/descendant::*[2]")

			# 点击失效按钮
			click("xpath", "//span[text()='失效']")

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'失效成功！')]")
			print("资金用途，点击失效成功！")
			time.sleep(3)

			# 切入‘资金用途’的iframe窗体
			switch_to("xpath", "//iframe[@id='bondpurpose-tab-iframe']")

			# 生效按钮
			# 勾选
			click("xpath", "//div[@title='代码:TestBpur']/parent::*/preceding-sibling::*[1]/descendant::*[2]")

			# 点击生效按钮
			click("xpath", "//span[text()='生效']")

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'生效成功！')]")
			print("资金用途，点击生效成功！")
			time.sleep(3)

			# 删除功能
			# 切入‘资金用途’的iframe窗体
			switch_to("xpath", "//iframe[@id='bondpurpose-tab-iframe']")

			# 点击删除按钮
			click("xpath", "//span[text()='删除']")

			# 勾选
			click("xpath", "//div[@title='代码:TestBpur']/parent::*/preceding-sibling::*[1]/descendant::*[2]")

			# 点击弹出框的OK键
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

			# 退出所有iframe窗体


			switch_default()

			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功')]")
			print("资金用途，删除成功！")
			time.sleep(3)

			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='资金用途']/child::*[1]")

			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//li[@f_value='bondissuancesetting']/descendant-or-self::*[5]")

			# 打印操作成功日志
			print("资金用途，操作成功!")
			logging.info("资金用途，操作成功!")
			time.sleep(2)
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("资金用途,失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		# 测试基础设置--主承销商
		try:
			# 点击基础设置菜单
			click("xpath", "//li[@f_value='bondissuancesetting']/descendant-or-self::*[5]")
			# 点击主承销商菜单
			click("xpath", "//span[text()='主承销商']")
			# 退出所有iframe窗体
			switch_default()

			for i in range(1, 3):
				# 切入‘主承销商’的iframe窗体
				switch_to("xpath", "//iframe[@id='bondconsignee-tab-iframe']")
				logging.info("开始测试主承销商功能")

				# 用JS的方法点击新增按钮
				js_click("xpath", "//span[text()='新增']")

				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='addWin-iframe']")
				sleep(1)

				# 输入代码
				input("xpath", "//input[@name='code']", "TestBcon")
				sleep(1)

				# 输入的名称
				input("xpath", "//input[@id='name']", "自动化测试主承销商")
				sleep(1)

				# 描述框中填入值
				input("xpath", "//textarea[@id='description']", "自动化测试主承销商描述框")
				sleep(1)

				# 点击保存按钮
				click("xpath", "//span[text()='保存']")

				# 退出所有iframe窗体
				switch_default()

				# 用隐式等待方法等页面出现提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				print("主承销商，保存成功！")
				time.sleep(3)

				if i == 1:
					# 删除功能
					# 切入‘主承销商’的iframe窗体
					switch_to("xpath", "//iframe[@id='bondconsignee-tab-iframe']")

					# 点击查看
					# 用JS的方法点击放大镜
					js_click("xpath", "//span[@class='f-contrac-close']")
					sleep(1)

					# 输入代码：
					input("xpath", "//input[@id='code']", "TestBcon")
					sleep(1)

					# 点击查询
					click("xpath", "//span[text()='查询']")

					# 勾选
					click("xpath", "//div[@title='代码:TestBcon']/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 点击删除按钮
					click("xpath", "//span[text()='删除']")

					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现删除的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功')]")
					print("主承销商，删除成功！")
					time.sleep(3)

			# 切入‘主承销商’的iframe窗体
			switch_to("xpath", "//iframe[@id='bondconsignee-tab-iframe']")

			# 点击查看
			# 清空代码框的内容
			clear("xpath", "//input[@id='code']")
			sleep(1)

			# 输入代码：
			input("xpath", "//input[@id='code']", "TestBcon")
			sleep(1)

			# 点击查询
			click("xpath", "//span[text()='查询']")

			# 修改
			# 勾选
			click("xpath", "//div[@title='代码:TestBcon']/parent::*/preceding-sibling::*[1]/descendant::*[2]")

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
			print("主承销商，修改成功！")
			time.sleep(3)

			# 切入‘主承销商’的iframe窗体
			switch_to("xpath", "//iframe[@id='bondconsignee-tab-iframe']")

			# 失效按钮
			# 勾选
			click("xpath", "//div[@title='代码:TestBcon']/parent::*/preceding-sibling::*[1]/descendant::*[2]")

			# 点击失效按钮
			click("xpath", "//span[text()='失效']")

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'失效成功！')]")
			print("主承销商，点击失效成功！")
			time.sleep(3)

			# 切入‘主承销商’的iframe窗体
			switch_to("xpath", "//iframe[@id='bondconsignee-tab-iframe']")

			# 生效按钮
			# 勾选
			click("xpath", "//div[@title='代码:TestBcon']/parent::*/preceding-sibling::*[1]/descendant::*[2]")

			# 点击生效按钮
			click("xpath", "//span[text()='生效']")

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'生效成功！')]")
			print("主承销商，点击生效成功！")
			time.sleep(3)

			# # 删除数据功能
			# # 切入‘主承销商’的iframe窗体
			# switch_to("xpath", "//iframe[@id='bondconsignee-tab-iframe']")
			#
			# # 勾选
			# click("xpath", "//div[@title='代码:TestBcon']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
			#
			# # 点击删除按钮
			# click("xpath", "//span[text()='删除']")
			#
			# # 点击弹出框的OK键
			# click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
			#
			# # 退出所有iframe窗体
			# switch_default()
			#
			# # 用隐式等待方法等页面出现删除的提示框
			# implici_wait("xpath", "//span[contains(text(),'操作成功')]")
			# print("主承销商，删除成功！")
			# time.sleep(3)

			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='主承销商']/child::*[1]")

			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//li[@f_value='bondissuancesetting']/descendant-or-self::*[5]")

			# 打印操作成功日志
			print("主承销商，操作成功!")
			logging.info("主承销商，操作成功!")
			time.sleep(2)
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("主承销商,失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		"""
		# 测试注册登记
		try:
			# 点击主承销商菜单
			click("xpath", "//span[text()='注册登记']")
			# 退出所有iframe窗体
			switch_default()
			
			logging.info("开始测试注册登记功能")
			for i in range(1, 4):
				# 切入‘注册登记’的iframe窗体
				switch_to("xpath", "//iframe[@id='bondregister-tab-iframe']")
				
				# 用JS的方法点击新增按钮
				js_click("xpath", "//span[text()='新增']")
				
				# 设置时间的变成存储
				temp = time.strftime("%Y%m%d%H%M%S")
				
				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='addWin-iframe']")
				sleep(1)
				
				# 输入注册编码
				input("xpath", "//input[@name='code']", str(temp) + "ZCBM")
				sleep(1)
				
				# 阳光城项目特有,输入债券名称
				# input("xpath", "//input[@name='name']", str("测试"+temp) + "ZCBM")
				# sleep(1)
				
				# 境内/境外，第一次选择境内，其他选择境外
				if i == 1:
					click("xpath", "//input[@id='combobox-input-consigneetype']")
					sleep(1)
					input("xpath", "//input[@id='combobox-input-consigneetype']", "境内")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-consigneetype']")
					input_enter("xpath", "//input[@id='combobox-input-consigneetype']")
					sleep(1)
				else:
					click("xpath", "//input[@id='combobox-input-consigneetype']")
					sleep(1)
					input("xpath", "//input[@id='combobox-input-consigneetype']", "境外")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-consigneetype']")
					input_enter("xpath", "//input[@id='combobox-input-consigneetype']")
					sleep(1)
				
				# 选择监管机构
				click("xpath", "//input[@id='combobox-input-registerorg']")
				sleep(1)
				input("xpath", "//input[@id='combobox-input-registerorg']", "TestReg-自动化测试监管机构")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-registerorg']")
				input_enter("xpath", "//input[@id='combobox-input-registerorg']")
				sleep(1)
				
				# 发行方式，第一次选择公募，其他选择私募
				if i == 1:
					click("xpath", "//input[@id='combobox-input-issuetype']")
					sleep(1)
					input("xpath", "//input[@id='combobox-input-issuetype']", "公募")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-issuetype']")
					input_enter("xpath", "//input[@id='combobox-input-issuetype']")
					sleep(1)
				else:
					click("xpath", "//input[@id='combobox-input-issuetype']")
					sleep(1)
					input("xpath", "//input[@id='combobox-input-issuetype']", "私募")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-issuetype']")
					input_enter("xpath", "//input[@id='combobox-input-issuetype']")
					sleep(1)
				
				# 注册品种，选择'TestZc-自动化测试注册品种'
				click("xpath", "//input[@id='combobox-input-varietys']")
				sleep(1)
				input("xpath", "//input[@id='combobox-input-varietys']", "TestReg-自动化测试监管机构")
				sleep(1)
				# 勾选
				click("xpath",
				      "//div[@title='代码-名称:TestZc-自动化测试注册品种']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
				sleep(1)
				
				# 输入注册额度
				click("xpath", "//input[@id='amount-input']")
				sleep(1)
				# 清空内容
				clear("xpath", "//input[@id='amount-input']")
				sleep(1)
				# 输入金额
				input("xpath", "//input[@id='amount-input']", "10000000")
				sleep(1)
				
				# 选择'注册币种'，第一次选‘人民币’，其他选‘美元’
				if i == 1:
					click("xpath", "//input[@id='combobox-input-currencyid']")
					sleep(1)
					input("xpath", "//input[@id='combobox-input-currencyid']", "CNY-人民币")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-currencyid']")
					input_enter("xpath", "//input[@id='combobox-input-currencyid']")
					sleep(1)
				else:
					click("xpath", "//input[@id='combobox-input-currencyid']")
					sleep(1)
					input("xpath", "//input[@id='combobox-input-currencyid']", "USD-美元")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-currencyid']")
					input_enter("xpath", "//input[@id='combobox-input-currencyid']")
					sleep(1)
				
				# 输入批文文号
				temp1 = time.strftime("%Y%m%d%H%M%S")
				input("xpath", "//input[@id='registerapproval']", str(temp1))
				sleep(1)
				
				# 输入批文下发日
				today = date.today()
				input("xpath", "//input[@id='approvaldate-input']", str(today))
				# 模拟回车键
				keyDown('enter')
				keyUp('enter')
				time.sleep(1)
				
				# 输入额度生效日
				input("xpath", "//input[@id='begindate-input']", str(today))
				# 模拟回车键
				keyDown('enter')
				keyUp('enter')
				time.sleep(1)
				
				# 输入额度到期日
				today1 = today + timedelta(days=730)
				input("xpath", "//input[@id='enddate-input']", str(today1))
				# 模拟回车键
				keyDown('enter')
				keyUp('enter')
				time.sleep(1)
				
				# 选择评级机构，勾选‘TestRat-自动化测试评级机构’
				click("xpath", "//input[@id='combobox-input-ratingagency']")
				sleep(1)
				input("xpath", "//input[@id='combobox-input-ratingagency']", "TestRat-自动化测试评级机构")
				sleep(1)
				# 勾选
				click("xpath",
				      "//div[@title='代码-名称:TestRat-自动化测试评级机构']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
				sleep(1)
				
				# 输入主体评级
				click("xpath", "//input[@id='combobox-input-orgrating']")
				sleep(1)
				input("xpath", "//input[@id='combobox-input-orgrating']", "AA")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-orgrating']")
				input_enter("xpath", "//input[@id='combobox-input-orgrating']")
				
				# 输入债券评级
				click("xpath", "//input[@id='combobox-input-bondrating']")
				sleep(1)
				input("xpath", "//input[@id='combobox-input-bondrating']", "AA")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-bondrating']")
				input_enter("xpath", "//input[@id='combobox-input-bondrating']")
				
				# 选择法律顾问，勾选‘TestLeg-自动化测试法律顾问’
				# 用JS点击下拉框
				js_click("xpath", "//input[@id='combobox-input-legaladviser']/following-sibling::*[1]")
				sleep(1)
				input("xpath", "//input[@id='combobox-input-legaladviser']", "TestLeg-自动化测试法律顾问")
				sleep(1)
				# 勾选
				click("xpath",
				      "//div[@title='代码-名称:TestLeg-自动化测试法律顾问']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
				sleep(1)
				
				# 输入资金用途
				input("xpath", "//input[@id='purpose']", "债券发行使用")
				sleep(1)
				
				# 输入投资项目
				# 用JS点击下拉框
				js_click("xpath", "//input[@id='combobox-input-projectitemid']/following-sibling::*[1]")
				sleep(2)
				input_down("xpath", "//input[@id='combobox-input-projectitemid']")
				input_enter("xpath", "//input[@id='combobox-input-projectitemid']")
				
				# 输入增信措施
				input("xpath", "//textarea[@id='addcreditmeasures']", "自动化测试注册登记增信措施")
				sleep(1)
				
				# 备注框中填入值
				input("xpath", "//textarea[@id='description']", "自动化测试注册登记备注")
				sleep(1)
				
				# 增加第1行
				click("xpath", "//span[text()='新增行']")
				time.sleep(1)
				
				# 增加第2行
				click("xpath", "//span[text()='新增行']")
				time.sleep(1)
				
				# 在第一行里面的主承销商输入内容
				click("xpath", "//input[@id='combobox-input-consigneegrid-bondconsigneeid-0']")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-consigneegrid-bondconsigneeid-0']")
				input_enter("xpath", "//input[@id='combobox-input-consigneegrid-bondconsigneeid-0']")
				sleep(1)
				
				# 在第一行里面的承销额度输入内容
				input("xpath", "//input[@id='consigneegrid-amount-0-input']", "3000000")
				sleep(1)
				
				# 在第一行里面的备注输入内容
				input("xpath", "//input[@id='consigneegrid-description-0']", "第一行3000W金额")
				sleep(1)
				
				# 在第二行里面的主承销商输入内容
				click("xpath", "//input[@id='combobox-input-consigneegrid-bondconsigneeid-1']")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-consigneegrid-bondconsigneeid-1']")
				input_down("xpath", "//input[@id='combobox-input-consigneegrid-bondconsigneeid-1']")
				input_enter("xpath", "//input[@id='combobox-input-consigneegrid-bondconsigneeid-1']")
				sleep(1)
				
				# 在第二行里面的承销额度输入内容
				input("xpath", "//input[@id='consigneegrid-amount-1-input']", "7000000")
				sleep(1)
				
				# 在第二行里面的备注输入内容
				input("xpath", "//input[@id='consigneegrid-description-1']", "第二行7000W金额")
				sleep(1)
				
				# 缺少附件上传功能
				
				# 点击保存按钮
				click("xpath", "//span[text()='保存']")
				
				# 退出所有iframe窗体
				switch_default()
				
				# 用隐式等待方法等页面出现提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				print("注册登记第%s次，保存成功！" % i)
				logging.info("注册登记第%s次，保存成功！" % i)
				time.sleep(3)
				
				# 第一笔，就先修改，再删除新建的‘注册登记’
				if i == 1:
					# 切入‘注册登记’的iframe窗体
					switch_to("xpath", "//iframe[@id='bondregister-tab-iframe']")
					
					# 点击查看
					# 用JS的方法点击放大镜
					js_click("xpath", "//span[@class='f-contrac-close']")
					sleep(1)
					
					# 输入注册代码：ZCBM
					input("xpath", "//input[@id='code']", "ZCBM")
					sleep(1)
					
					# 点击查询
					click("xpath", "//span[text()='查询']")
					
					# 修改
					# 勾选
					click("xpath", "//div[contains(text(),'ZCBM')]/parent::*/preceding-sibling::*[3]//descendant::*[2]")
					
					# 点击修改按钮
					click("xpath", "//span[text()='修改']")
					
					# 切入修改的iframe窗体
					switch_to("xpath", "//iframe[@id='modWin-iframe']")
					sleep(1)
					
					# 增信措施输入新内容
					input("xpath", "//textarea[@id='addcreditmeasures']", "修改填入增信措施内容")
					sleep(1)
					
					# 备注框中输入新内容
					input("xpath", "//textarea[@id='description']", "修改填入备注内容")
					sleep(1)
					
					# 删除2行‘主承销商’
					# 勾选‘主承销商’第一行
					click("xpath", "//tr[@id='consigneegrid-tr-0']/child::*[2]/descendant::*[2]")
					# 点击‘移出行’
					click("xpath", "//span[contains(text(),'移出行')]")
					sleep(1)
					
					# 勾选‘主承销商’第二行
					click("xpath", "//tr[@id='consigneegrid-tr-1']/child::*[2]/descendant::*[2]")
					# 点击‘移出行’
					click("xpath", "//span[contains(text(),'移出行')]")
					
					# 增加第1行
					click("xpath", "//span[text()='新增行']")
					time.sleep(1)
					
					# 增加第2行
					click("xpath", "//span[text()='新增行']")
					time.sleep(1)
					
					# 在新增第一行里面的主承销商输入内容
					click("xpath", "//input[@id='combobox-input-consigneegrid-bondconsigneeid-2']")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-consigneegrid-bondconsigneeid-2']")
					input_enter("xpath", "//input[@id='combobox-input-consigneegrid-bondconsigneeid-2']")
					sleep(1)
					
					# 在新增第一行里面的承销额度输入内容
					input("xpath", "//input[@id='consigneegrid-amount-2-input']", "3000000")
					sleep(1)
					
					# 在新增行里面的备注输入内容
					input("xpath", "//input[@id='consigneegrid-description-2']", "新增一行金额300W金额")
					sleep(1)
					
					#  在新增第二行里面的主承销商输入内容
					click("xpath", "//input[@id='combobox-input-consigneegrid-bondconsigneeid-3']")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-consigneegrid-bondconsigneeid-3']")
					input_down("xpath", "//input[@id='combobox-input-consigneegrid-bondconsigneeid-3']")
					input_enter("xpath", "//input[@id='combobox-input-consigneegrid-bondconsigneeid-3']")
					sleep(1)
					
					# 在新增第一行里面的承销额度输入内容
					input("xpath", "//input[@id='consigneegrid-amount-3-input']", "7000000")
					sleep(1)
					
					# 在新增行里面的备注输入内容
					input("xpath", "//input[@id='consigneegrid-description-3']", "新增一行金额700W金额")
					sleep(1)
					
					# 点击保存按钮
					click("xpath", "//span[text()='保存']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("注册登记，修改成功！")
					logging.info("注册登记，修改成功！")
					time.sleep(3)
					
					# 切入‘注册登记’的iframe窗体
					switch_to("xpath", "//iframe[@id='bondregister-tab-iframe']")
					
					# 删除
					# 勾选
					click("xpath", "//div[contains(text(),'ZCBM')]/parent::*/preceding-sibling::*[3]//descendant::*[2]")
					
					# 点击删除按钮
					click("xpath", "//span[text()='删除']")
					
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现删除的提示框
					implici_wait("xpath", "//span[contains(text(),'删除债券注册合同成功')]")
					print("注册登记，删除成功！")
					logging.info("注册登记，删除成功！")
					time.sleep(3)
				
				# 第二笔，先审核、再取消审核、再变更、再作废
				elif i == 2:
					
					# 第一次审核
					# 切入‘注册登记’的iframe窗体
					switch_to("xpath", "//iframe[@id='bondregister-tab-iframe']")
					
					# 勾选
					click("xpath", "//div[contains(text(),'ZCBM')]/parent::*/preceding-sibling::*[3]//descendant::*[2]")
					
					# 点击审核按钮
					click("xpath", "//span[text()='审核']")
					
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现删除的提示框
					implici_wait("xpath", "//span[contains(text(),'审批债券注册合同成功')]")
					print("注册登记，第一次审核成功！")
					logging.info("注册登记，第一次审核成功！")
					time.sleep(3)
					
					# 取消审核
					# 切入‘注册登记’的iframe窗体
					switch_to("xpath", "//iframe[@id='bondregister-tab-iframe']")
					
					# 勾选
					click("xpath", "//div[contains(text(),'ZCBM')]/parent::*/preceding-sibling::*[3]//descendant::*[2]")
					
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
					
					# 用隐式等待方法等页面出现删除的提示框
					implici_wait("xpath", "//span[contains(text(),'取消审核债券注册合同成功')]")
					print("注册登记，取消审核成功！")
					logging.info("注册登记，取消审核成功！")
					time.sleep(3)
					
					# 第二次审核
					# 切入‘注册登记’的iframe窗体
					switch_to("xpath", "//iframe[@id='bondregister-tab-iframe']")
					
					# 勾选
					click("xpath", "//div[contains(text(),'ZCBM')]/parent::*/preceding-sibling::*[3]//descendant::*[2]")
					
					# 点击审核按钮
					click("xpath", "//span[text()='审核']")
					
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现删除的提示框
					implici_wait("xpath", "//span[contains(text(),'审批债券注册合同成功')]")
					print("注册登记，第二次审核成功！")
					logging.info("注册登记，第二次审核成功！")
					time.sleep(3)
					
					# 变更
					# 切入‘注册登记’的iframe窗体
					switch_to("xpath", "//iframe[@id='bondregister-tab-iframe']")
					
					# 勾选
					click("xpath", "//div[contains(text(),'ZCBM')]/parent::*/preceding-sibling::*[3]//descendant::*[2]")
					
					# 点击变更按钮
					click("xpath", "//span[text()='变更']")
					
					# 切入修改的iframe窗体
					switch_to("xpath", "//iframe[@id='modWin-iframe']")
					sleep(1)
					
					# 增信措施输入新内容
					input("xpath", "//textarea[@id='addcreditmeasures']", "变更填入增信措施内容")
					sleep(1)
					
					# 备注框中输入新内容
					input("xpath", "//textarea[@id='description']", "变更填入备注内容")
					sleep(1)
					
					# 点击保存按钮
					click("xpath", "//span[text()='保存']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("注册登记，变更成功！")
					logging.info("注册登记，变更成功！")
					time.sleep(3)
					
					# 作废
					# 切入‘注册登记’的iframe窗体
					switch_to("xpath", "//iframe[@id='bondregister-tab-iframe']")
					
					# 勾选
					click("xpath", "//div[contains(text(),'ZCBM')]/parent::*/preceding-sibling::*[3]//descendant::*[2]")
					
					# 点击作废按钮
					click("xpath", "//span[text()='作废']")
					
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现删除的提示框
					implici_wait("xpath", "//span[contains(text(),'作废债券注册合同成功')]")
					print("注册登记，作废成功！")
					logging.info("注册登记，作废成功！")
					time.sleep(3)
				
				# 第三笔，审核
				elif i == 3:
					# 切入‘注册登记’的iframe窗体
					switch_to("xpath", "//iframe[@id='bondregister-tab-iframe']")
					
					# 勾选
					click("xpath", "//div[contains(text(),'ZCBM')]/parent::*/preceding-sibling::*[3]//descendant::*[2]")
					
					# 点击审核按钮
					click("xpath", "//span[text()='审核']")
					
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现删除的提示框
					implici_wait("xpath", "//span[contains(text(),'审批债券注册合同成功')]")
					print("注册登记，第三笔审核成功！")
					logging.info("注册登记，第三笔审核成功！")
					time.sleep(3)
			
			# 退出所有iframe窗体
			switch_default()
			
			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='注册登记']/child::*[1]")
			
			# 打印操作成功日志
			print("注册登记，操作成功!")
			logging.info("注册登记，操作成功!")
			time.sleep(2)
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("注册登记,失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		
		# 测试发行登记功能
		try:
			# 点击‘发行登记’菜单
			click("xpath", "//span[text()='发行登记']")
			# 退出所有iframe窗体
			switch_default()
			
			logging.info("开始测试发行登记功能")
			for i in range(1, 7):
				# 切入‘发行登记’的iframe窗体
				switch_to("xpath", "//iframe[@id='bondissuance-tab-iframe']")
				
				# 用JS的方法点击新增按钮
				js_click("xpath", "//span[text()='新增']")
				
				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='addWin-iframe']")
				sleep(1)
				
				# 选择注册编码
				# 点击‘注册编码’框
				click("xpath", "//input[@id='combobox-input-bondregisterid']")
				# 输入ZCBM，模糊查询
				input("xpath", "//input[@id='combobox-input-bondregisterid']", "ZCBM")
				sleep(1)
				double_click("xpath", "//div[contains(text(),'ZCBM')]")
				sleep(1)
				
				# 设置时间的变成存储，变成
				temp = time.strftime("%Y%m%d%H%M%S")
				# 输入债券代码
				input("xpath", "//input[@id='code']", "Test" + str(temp))
				sleep(1)
				
				# 设置时间的变成存储，变成
				temp1 = time.strftime("%H%M%S")
				# 输入债券全称
				input("xpath", "//input[@id='name']", "债券全称" + str(temp1))
				sleep(1)
				
				# 输入债券简称
				input("xpath", "//input[@id='simplename']", "债券简称" + str(temp1))
				time.sleep(1)
				
				# 输入发行日期
				# 点击发行日期的日历按钮
				js_click("xpath", "//span[@id='issuancedate-trigger']")
				time.sleep(1)
				
				# 退出所有iframe窗体
				switch_default()
				# 切入日历框的iframe
				switch_to("xpath", "//iframe[@hidefocus='true']")
				# 点击日历框中今天的按钮
				click("xpath", "//input[@id='dpTodayInput']")
				time.sleep(1)
				# 退出当前日历框的iframe窗体
				switch_parent()
				
				# 法定到期日
				# 切入‘发行登记’的iframe窗体
				switch_to("xpath", "//iframe[@id='bondissuance-tab-iframe']")
				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='addWin-iframe']")
				# 点击法定到期日的日历按钮
				js_click("xpath", "//span[@id='legalenddate-trigger']")
				time.sleep(1)
				
				# 退出所有iframe窗体
				switch_default()
				# 切入日历框的iframe
				switch_to("xpath", "//iframe[@hidefocus='true']")
				# 点击日历框中今天的按钮
				click("xpath", "//input[@id='dpTodayInput']")
				time.sleep(1)
				# 退出当前日历框的iframe窗体
				switch_parent()
				
				# 切入‘发行登记’的iframe窗体
				switch_to("xpath", "//iframe[@id='bondissuance-tab-iframe']")
				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='addWin-iframe']")
				
				# 输入发行期限（日）
				# 先清空发行期限（日）内容
				clear("xpath", "//input[@id='termday-input']")
				input("xpath", "//input[@id='termday-input']", "90")
				time.sleep(1)
				
				# 输入含权期限
				input("xpath", "//input[@id='weightterm']", "30")
				time.sleep(1)
				
				# 输入发行金额
				input("xpath", "//input[@id='amount-input']", "100000")
				sleep(1)
				
				# 输入发行场所
				input("xpath", "//input[@id='issuanceplace']", "清算所")
				sleep(1)
				
				# 输入资金用途
				# input("xpath", "//input[@id='purposeid']", "融资使用")
				# sleep(1)
				
				# 第二笔的时候选择‘是否回售’
				if i == 2:
					click("xpath", "//input[@id='isresale']")
				
				# 输入备注
				input("xpath", "//textarea[@id='memo']", "发行登记备注内容")
				
				# 计息方式中输入值
				# 点击计息方式插页
				click("xpath", "//span[contains(text(),'计息方式')]")
				# 1、选择还本方式
				click("xpath", "//input[@id='combobox-input-repaymode']")
				# 按键往下，选择‘按季还款’
				input_down("xpath", "//input[@id='combobox-input-repaymode']")
				input_enter("xpath", "//input[@id='combobox-input-repaymode']")
				time.sleep(1)
				# 2、选择还息方式
				click("xpath", "//input[@id='combobox-input-interestmode']")
				# 按键往下，选择‘按季还款’
				input_down("xpath", "//input[@id='combobox-input-interestmode']")
				input_enter("xpath", "//input[@id='combobox-input-interestmode']")
				time.sleep(1)
				# 3、选择利率方案
				click("xpath", "//input[@id='combobox-input-interestrateschemeid']")
				# 按键往下，选择利率方案
				sleep(2)
				input_down("xpath", "//input[@id='combobox-input-interestrateschemeid']")
				input_enter("xpath", "//input[@id='combobox-input-interestrateschemeid']")
				
				# 费用中输入值
				# 点击费用插页
				click("xpath", "//span[text()='费用']")
				time.sleep(1)
				
				# 点击费用新增行，新增第一行
				click("xpath", "//span[@title='费用类型']/ancestor::*[6]/following-sibling::*[2]/descendant::*[7]")
				sleep(1)
				
				# 在第一行的‘费用类型’中选择‘律师费’
				click("xpath", "//input[@id='combobox-input-feesgrid-feestype-0']")
				time.sleep(1)
				input("xpath", "//input[@id='combobox-input-feesgrid-feestype-0']", "律师费")
				time.sleep(1)
				input_down("xpath", "//input[@id='combobox-input-feesgrid-feestype-0']")
				time.sleep(1)
				input_enter("xpath", "//input[@id='combobox-input-feesgrid-feestype-0']")
				# 模拟回车键
				keyDown('enter')
				keyUp('enter')
				time.sleep(1)
				# 在第一行的‘费用金额’中输入金额
				click("xpath", "//input[@id='feesgrid-feesamount-0-input']")
				input("xpath", "//input[@id='feesgrid-feesamount-0-input']", "100")
				time.sleep(1)
				# 在第一行的‘费用日期’中输入日期
				today = date.today()
				input("xpath", "//input[@id='feesgrid-feesdate-0-input']", str(today))
				# 模拟回车键
				keyDown('enter')
				keyUp('enter')
				time.sleep(1)
				# 在第一行的‘付款主体’中‘001000-亚唐科技’
				click("xpath", "//input[@id='combobox-input-feesgrid-paymainpart-0']")
				input("xpath", "//input[@id='combobox-input-feesgrid-paymainpart-0']", "001000-亚唐科技")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-feesgrid-paymainpart-0']")
				input_enter("xpath", "//input[@id='combobox-input-feesgrid-paymainpart-0']")
				# 在第一行的‘备注’中输入‘第一行备注律师费’
				input("xpath", "//input[@id='feesgrid-description-0']", "第一行备注律师费")
				sleep(1)
				
				# 点击费用新增行，新增第二行
				click("xpath", "//span[@title='费用类型']/ancestor::*[6]/following-sibling::*[2]/descendant::*[7]")
				sleep(1)
				
				# 在第二行的‘费用类型’中选择‘其他’
				click("xpath", "//input[@id='combobox-input-feesgrid-feestype-1']")
				time.sleep(1)
				input("xpath", "//input[@id='combobox-input-feesgrid-feestype-1']", "其他")
				time.sleep(1)
				input_down("xpath", "//input[@id='combobox-input-feesgrid-feestype-1']")
				time.sleep(1)
				input_enter("xpath", "//input[@id='combobox-input-feesgrid-feestype-1']")
				# 模拟回车键
				keyDown('enter')
				keyUp('enter')
				time.sleep(1)
				
				# 在第二行的‘费用金额’中输入金额
				click("xpath", "//input[@id='feesgrid-feesamount-1-input']")
				input("xpath", "//input[@id='feesgrid-feesamount-1-input']", "22222")
				time.sleep(1)
				
				# 在第二行的‘费用日期’中输入日期
				today = date.today()
				input("xpath", "//input[@id='feesgrid-feesdate-1-input']", str(today))
				# 模拟回车键
				keyDown('enter')
				keyUp('enter')
				time.sleep(1)
				
				# 在第二行的‘付款主体’中‘001000-亚唐科技’
				click("xpath", "//input[@id='combobox-input-feesgrid-paymainpart-1']")
				input("xpath", "//input[@id='combobox-input-feesgrid-paymainpart-1']", "001000-亚唐科技")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-feesgrid-paymainpart-1']")
				input_enter("xpath", "//input[@id='combobox-input-feesgrid-paymainpart-1']")
				# 在第二行的‘备注’中输入‘第二行备注其他费’
				input("xpath", "//input[@id='feesgrid-description-1']", "第二行备注其他费")
				sleep(1)
				
				# 点击主承销商插页
				click("xpath", "//span[text()='主承销商']")
				time.sleep(1)
				
				# 主承销商插页修改承销金额
				# 修改第一行的金额
				click("xpath", "//input[@id='consigneegrid-amount-0-input']")
				sleep(1)
				clear("xpath", "//input[@id='consigneegrid-amount-0-input']")
				sleep(1)
				input("xpath", "//input[@id='consigneegrid-amount-0-input']", "2000")
				sleep(1)
				
				# 修改第一行的备注框
				
				click("xpath", "//input[@id='consigneegrid-description-0']")
				sleep(1)
				clear("xpath", "//input[@id='consigneegrid-description-0']")
				sleep(1)
				input("xpath", "//input[@id='consigneegrid-description-0']", "第一行2000RMB金额")
				sleep(1)
				
				# 修改第二行金额
				click("xpath", "//input[@id='consigneegrid-amount-1-input']")
				sleep(1)
				clear("xpath", "//input[@id='consigneegrid-amount-1-input']")
				sleep(1)
				input("xpath", "//input[@id='consigneegrid-amount-1-input']", "1000")
				sleep(1)
				
				# 修改第一行的备注框
				click("xpath", "//input[@id='consigneegrid-description-1']")
				sleep(1)
				clear("xpath", "//input[@id='consigneegrid-description-1']")
				sleep(1)
				input("xpath", "//input[@id='consigneegrid-description-1']", "第二行1000RMB金额")
				sleep(1)
				
				# 公共版本是‘头寸准备计划’；点击‘头寸准备计划’插页，
				click("xpath", "//span[text()='头寸准备计划']")
				# 阳光城版本是‘资金归集计划’；点击‘资金归集计划’插页，
				
				# click("xpath", "//span[text()='资金归集计划']")
				time.sleep(1)
				
				# 点击头寸准备计划插页
				# 点击头寸准备计划新增行，新增第一行
				click("xpath", "//span[@title='类型']/ancestor::*[6]/following-sibling::*[2]/descendant::*[7]")
				sleep(1)
				
				# 在第一行的‘类型’中选择‘还本’
				click("xpath", "//input[@id='combobox-input-positionplangrid-positionplantype-0']")
				time.sleep(1)
				input("xpath", "//input[@id='combobox-input-positionplangrid-positionplantype-0']", "还本")
				time.sleep(1)
				input_down("xpath", "//input[@id='combobox-input-positionplangrid-positionplantype-0']")
				time.sleep(1)
				input_enter("xpath", "//input[@id='combobox-input-positionplangrid-positionplantype-0']")
				# 模拟回车键
				keyDown('enter')
				keyUp('enter')
				time.sleep(1)
				# 在第一行的‘日期’中输入日期
				today = date.today()
				input("xpath", "//input[@id='positionplangrid-positionplandate-0-input']",
				      str(today + timedelta(days=30)))
				# 模拟回车键
				keyDown('enter')
				keyUp('enter')
				time.sleep(1)
				# 在第一行的‘金额’中输入值
				clear("xpath", "//input[@id='positionplangrid-positionplanamount-0-input']")
				input("xpath", "//input[@id='positionplangrid-positionplanamount-0-input']", "500")
				time.sleep(1)
				# 在第一行的‘备注’中输入‘第一行备注还本500’
				input("xpath", "//input[@id='positionplangrid-description-0']", "第一行备注还本500")
				sleep(1)
				
				# 点击头寸准备计划新增行，新增第二行
				click("xpath", "//span[@title='类型']/ancestor::*[6]/following-sibling::*[2]/descendant::*[7]")
				sleep(1)
				
				# 在第二行的‘类型’中选择‘还息’
				js_click("xpath",
				         "//input[@id='combobox-input-positionplangrid-positionplantype-1']/following-sibling::*[1]")
				time.sleep(1)
				input("xpath", "//input[@id='combobox-input-positionplangrid-positionplantype-1']", "还息")
				time.sleep(1)
				input_down("xpath", "//input[@id='combobox-input-positionplangrid-positionplantype-1']")
				time.sleep(1)
				input_enter("xpath", "//input[@id='combobox-input-positionplangrid-positionplantype-1']")
				# 模拟回车键
				keyDown('enter')
				keyUp('enter')
				time.sleep(1)
				# 在第二行的‘日期’中输入日期
				today = date.today()
				input("xpath", "//input[@id='positionplangrid-positionplandate-1-input']",
				      str(today + timedelta(days=30)))
				# 模拟回车键
				keyDown('enter')
				keyUp('enter')
				time.sleep(1)
				# 在第二行的‘金额’中输入值
				clear("xpath", "//input[@id='positionplangrid-positionplanamount-1-input']")
				sleep(1)
				input("xpath", "//input[@id='positionplangrid-positionplanamount-1-input']", "200")
				time.sleep(1)
				# 在第二行的‘备注’中输入‘第二行备注还息200’
				input("xpath", "//input[@id='positionplangrid-description-1']", "第二行备注还息200")
				sleep(1)
				
				# 担保信息
				
				# 募集资金
				
				# 点击保存按钮
				click("xpath", "//span[text()='保存']")
				
				# 退出所有iframe窗体
				switch_default()
				
				# 用隐式等待方法等页面出现提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				print("发行登记第%s次，保存成功！" % i)
				logging.info("发行登记第%s次，保存成功！" % i)
				time.sleep(3)
				
				# 第一笔 先修改 再审核又取消审核、再删除新增的发行登记
				if i == 1:
					# 切入‘发行登记’的iframe窗体
					switch_to("xpath", "//iframe[@id='bondissuance-tab-iframe']")
					
					# 点击查看
					# 用JS的方法点击放大镜
					js_click("xpath", "//span[@class='f-contrac-close']")
					sleep(1)
					
					# 注册合同号
					click("xpath", "//input[@id='combobox-input-bondregisterid']")
					sleep(1)
					input("xpath", "//input[@id='combobox-input-bondregisterid']", "ZCBM")
					sleep(1)
					click("xpath", "//span[text()='代码-名称']/ancestor::*[3]/preceding-sibling::*[1]/descendant::*[2]")
					sleep(1)
					
					# 点击查询
					click("xpath", "//span[text()='查询']")
					
					# 修改
					# 勾选
					click("xpath", "//div[contains(text(),'ZCBM')]/parent::*/preceding-sibling::*[3]/descendant::*[2]")
					
					# 点击修改按钮
					click("xpath", "//span[text()='修改']")
					sleep(1)
					
					# 切入修改的iframe窗体
					switch_to("xpath", "//iframe[@id='modWin-iframe']")
					sleep(1)
					
					# 修改备注框
					input("xpath", "//textarea[@id='addcreditmeasures']", "自动化测试修改")
					sleep(1)
					
					# 备注框中填入值
					input("xpath", "//textarea[@id='memo']", "自动化测试修改")
					sleep(1)
					
					# 点击保存按钮
					click("xpath", "//span[text()='保存']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("发行登记，修改成功！")
					logging.info("发行登记，修改成功！")
					time.sleep(3)
					
					# 审核--取消审核 # 第一次审核
					# 切入‘发行登记’的iframe窗体
					switch_to("xpath", "//iframe[@id='bondissuance-tab-iframe']")
					
					# 勾选
					click("xpath", "//div[contains(text(),'ZCBM')]/parent::*/preceding-sibling::*[3]/descendant::*[2]")
					
					# 点击审核按钮
					click("xpath", "//span[text()='审核']")
					
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'成功审核1条记录')]")
					print("发行登记，第一次审核成功！")
					logging.info("发行登记，第一次审核成功！")
					time.sleep(3)
					
					# 取消审核
					# 切入‘发行登记’的iframe窗体
					switch_to("xpath", "//iframe[@id='bondissuance-tab-iframe']")
					
					# 勾选
					click("xpath", "//div[contains(text(),'ZCBM')]/parent::*/preceding-sibling::*[3]/descendant::*[2]")
					
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
					implici_wait("xpath", "//span[contains(text(),'成功取消审核:1条')]")
					print("发行登记，第一次审核后取消审核成功！")
					logging.info("发行登记，第一次审核后取消审核成功！")
					time.sleep(3)
					
					# 切入‘发行登记’的iframe窗体
					switch_to("xpath", "//iframe[@id='bondissuance-tab-iframe']")
					
					# 删除
					# 勾选
					click("xpath", "//div[contains(text(),'ZCBM')]/parent::*/preceding-sibling::*[3]/descendant::*[2]")
					
					# 点击删除按钮
					click("xpath", "//span[text()='删除']")
					
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现删除的提示框
					implici_wait("xpath", "//span[contains(text(),'成功删除1条记录！')]")
					print("发行登记，删除成功！")
					logging.info("发行登记，删除成功！")
					time.sleep(3)
				
				# 第二笔，审核、资金到账、取消到账、生成到账交易单
				if i == 2:
					# 第二次审核
					# 切入‘发行登记’的iframe窗体
					switch_to("xpath", "//iframe[@id='bondissuance-tab-iframe']")
					
					# 勾选
					click("xpath", "//div[contains(text(),'ZCBM')]/parent::*/preceding-sibling::*[3]/descendant::*[2]")
					
					# 点击审核按钮
					click("xpath", "//span[text()='审核']")
					
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'成功审核1条记录')]")
					print("发行登记，第二次审核成功！")
					logging.info("发行登记，第二次审核成功！")
					time.sleep(3)
					
					# 资金到账
					# 切入‘发行登记’的iframe窗体
					switch_to("xpath", "//iframe[@id='bondissuance-tab-iframe']")
					
					# 勾选
					click("xpath", "//div[contains(text(),'ZCBM')]/parent::*/preceding-sibling::*[3]/descendant::*[2]")
					
					# 点击资金到账按钮
					js_click("xpath", "//span[text()='资金到账']")
					sleep(1)
					
					# 切入资金到账的iframe窗体
					switch_to("xpath", "//iframe[@id='accountWin-iframe']")
					sleep(1)
					
					# 输入到账金额
					click("xpath", "//input[@id='amount-input']")
					sleep(1)
					clear("xpath", "//input[@id='amount-input']")
					sleep(1)
					input("xpath", "//input[@id='amount-input']", "80")
					sleep(1)
					
					# 点击保存按钮
					click("xpath", "//span[text()='保存']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("发行登记，资金到账成功！")
					logging.info("发行登记，资金到账成功！")
					sleep(3)
					
					# 资金到账--取消到账
					# 切入‘发行登记’的iframe窗体
					switch_to("xpath", "//iframe[@id='bondissuance-tab-iframe']")
					
					# 勾选
					click("xpath", "//div[contains(text(),'ZCBM')]/parent::*/preceding-sibling::*[3]/descendant::*[2]")
					
					# 用JS方便点击‘资金到账’按钮旁边的倒三角形
					js_click("xpath", "//span[text()='资金到账']/parent::*/following-sibling::*/child::*")
					sleep(1)
					
					# 点击取消到账按钮
					js_click("xpath", "//a[contains(text(),'取消到账')]")
					sleep(1)
					
					# 切入取消到账的窗体页面cancelAccountWin-iframe
					switch_to("xpath", "//iframe[@id='cancelAccountWin-iframe']")
					
					# 点击勾选当前资金到账的数据
					click("xpath", "//a[text()='未生成']/ancestor::*[2]/preceding-sibling::*[1]/descendant::*[2]")
					sleep(1)
					
					# 点击取消到账
					click("xpath", "//span[text()='取消到账']")
					sleep(1)
					
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'成功取消:1条记录！')]")
					print("发行登记，取消到账成功！")
					logging.info("发行登记，取消到账成功！")
					sleep(3)
					
					# 切入资金到账的iframe窗体
					switch_to("xpath", "//iframe[@id='bondissuance-tab-iframe']")
					sleep(1)
					
					# 点击关闭取消到账的关闭按钮
					click("xpath", "//span[text()='到账取消']/preceding-sibling::*[1]")
					
					switch_default()
					
					# 资金到账
					# 切入‘发行登记’的iframe窗体
					switch_to("xpath", "//iframe[@id='bondissuance-tab-iframe']")
					
					# 点击资金到账按钮
					js_click("xpath", "//span[text()='资金到账']")
					sleep(1)
					
					# 切入资金到账的iframe窗体
					switch_to("xpath", "//iframe[@id='accountWin-iframe']")
					sleep(1)
					
					# 输入到账金额
					click("xpath", "//input[@id='amount-input']")
					sleep(1)
					clear("xpath", "//input[@id='amount-input']")
					sleep(1)
					input("xpath", "//input[@id='amount-input']", "80")
					sleep(1)
					
					# 点击保存按钮
					click("xpath", "//span[text()='保存']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("发行登记，资金到账成功！")
					logging.info("发行登记，资金到账成功！")
					sleep(3)
				
				if i == 3:
					# 债券转股
					# 切入‘发行登记’的iframe窗体
					switch_to("xpath", "//iframe[@id='bondissuance-tab-iframe']")
					
					# 选择已审核、未生成的
					# 用JS的方法点击高级查询按钮
					js_click("xpath", "//span[text()='高级查询']")
					
					click("xpath", "//input[@id='combobox-input-property_0']")
					sleep(1)
					clear("xpath", "//input[@id='combobox-input-property_0']")
					sleep(1)
					# 输入作废状态，通过模糊匹配搜索
					input("xpath", "//input[@id='combobox-input-property_0']", "审核状态")
					sleep(1)
					# 模拟回车
					click("xpath", "//div[contains(text(),'审核状态')]")
					sleep(1)
					
					click("xpath", "//input[@id='combobox-input-condition_0']")
					sleep(1)
					# 输入包含，通过模糊匹配搜索
					input("xpath", "//input[@id='combobox-input-condition_0']", "包含")
					sleep(1)
					# 模拟回车
					click("xpath", "//div[contains(text(),'包含')]")
					sleep(1)
					
					click("xpath", "//input[@id='combobox-input-value_0']")
					sleep(1)
					# 输入审核状态，通过模糊匹配搜索
					click("xpath", "//div[contains(text(),'已审核')]/preceding-sibling::*[1]")
					sleep(1)
					
					# 到账状态
					click("xpath", "//input[@id='combobox-input-property_1']")
					sleep(1)
					clear("xpath", "//input[@id='combobox-input-property_1']")
					sleep(1)
					# 输入作废状态，通过模糊匹配搜索
					input("xpath", "//input[@id='combobox-input-property_1']", "到账状态")
					sleep(1)
					# 模拟回车
					click("xpath", "//div[contains(text(),'到账状态')]")
					sleep(1)
					
					click("xpath", "//input[@id='combobox-input-value_1']")
					sleep(1)
					# 输入放款状态，通过模糊匹配搜索
					click("xpath", "//div[contains(text(),'完全到账')]/preceding-sibling::*[1]")
					sleep(1)
					
					click("xpath", "//div[contains(text(),'部分到账')]/preceding-sibling::*[1]")
					sleep(1)
					
					click("xpath", "//div[contains(text(),'查询')]")
					sleep(1)
					
					js_click("xpath", "//span[text()='自定义查询']/preceding-sibling::*[1]")
					sleep(1)
					
					# 勾选
					click("xpath", "//div[contains(text(),'ZCBM')]/parent::*/preceding-sibling::*[3]/descendant::*[2]")
					
					# 点击债券替换按钮
					js_click("xpath", "//span[text()='债券替换']")
					sleep(1)
					
					# 切入债券替换的iframe窗体
					switch_to("xpath", "//iframe[@id='modWin-iframe']")
					sleep(1)
					
					# 设置时间的变成存储，变成
					temp = time.strftime("%Y%m%d%H%M%S")
					# 输入债券代码
					input("xpath", "//input[@id='code']", "Test" + str(temp))
					sleep(1)
					
					# 设置时间的变成存储，变成
					temp1 = time.strftime("%H%M%S")
					# 输入债券全称
					input("xpath", "//input[@id='name']", "债券全称" + str(temp1))
					sleep(1)
					
					# 输入债券简称
					input("xpath", "//input[@id='simplename']", "债券简称" + str(temp1))
					time.sleep(1)
					
					# 输入发行金额
					click("xpath", "//input[@id='amount-input']")
					sleep(1)
					clear("xpath", "//input[@id='amount-input']")
					sleep(1)
					input("xpath", "//input[@id='amount-input']", "100000")
					sleep(1)
					
					# 点击主承销商插页
					click("xpath", "//span[text()='主承销商']")
					time.sleep(1)
					
					# 主承销商插页修改承销金额
					# 修改第一行的金额
					click("xpath", "//input[@id='consigneegrid-amount-0-input']")
					sleep(1)
					clear("xpath", "//input[@id='consigneegrid-amount-0-input']")
					sleep(1)
					input("xpath", "//input[@id='consigneegrid-amount-0-input']", "2000")
					sleep(1)
					
					# 修改第一行的备注框
					click("xpath", "//input[@id='consigneegrid-description-0']")
					sleep(1)
					clear("xpath", "//input[@id='consigneegrid-description-0']")
					sleep(1)
					
					# 修改第二行金额
					click("xpath", "//input[@id='consigneegrid-amount-1-input']")
					sleep(1)
					clear("xpath", "//input[@id='consigneegrid-amount-1-input']")
					sleep(1)
					input("xpath", "//input[@id='consigneegrid-amount-1-input']", "1000")
					sleep(1)
					
					# 修改第一行的备注框
					click("xpath", "//input[@id='consigneegrid-description-1']")
					sleep(1)
					clear("xpath", "//input[@id='consigneegrid-description-1']")
					sleep(1)
					
					# 点击保存按钮
					click("xpath", "//span[text()='保存']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("发行登记，债券替换保存成功！")
					logging.info("发行登记，债券替换保存成功！")
					time.sleep(3)
				
				if i == 4:
					# 第二次审核
					# 切入‘发行登记’的iframe窗体
					switch_to("xpath", "//iframe[@id='bondissuance-tab-iframe']")
					sleep(1)
					
					# # 点击查看
					# # 用JS的方法点击放大镜
					# js_click("xpath", "//span[@class='f-contrac-close']")
					# sleep(1)
					
					# 选择未审核
					click("xpath", "//input[@id='combobox-input-approvestate']")
					sleep(1)
					click("xpath", "//div[@id='f-combo-approvestate-list-0']/child::*[1]")
					sleep(1)
					
					# 点击查询
					click("xpath", "//span[text()='查询']")
					
					# 勾选
					click("xpath", "//div[contains(text(),'ZCBM')]/parent::*/preceding-sibling::*[3]/descendant::*[2]")
					
					# 点击审核按钮
					click("xpath", "//span[text()='审核']")
					
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'成功审核1条记录')]")
					print("发行登记，第二次审核成功！")
					logging.info("发行登记，第二次审核成功！")
					time.sleep(3)
					
					switch_to("xpath", "//iframe[@id='bondissuance-tab-iframe']")
					sleep(1)
					
					# 选择已审核
					click("xpath", "//input[@id='combobox-input-approvestate']")
					sleep(1)
					click("xpath", "//div[@id='f-combo-approvestate-list-0']/child::*[1]")
					sleep(1)
					click("xpath", "//div[@id='f-combo-approvestate-list-1']/child::*[1]")
					sleep(1)
					
					# 点击查询
					click("xpath", "//span[text()='查询']")
					
					# # 资金到账
					# # 切入‘发行登记’的iframe窗体
					# switch_to("xpath", "//iframe[@id='bondissuance-tab-iframe']")
					
					# 勾选
					click("xpath", "//div[contains(text(),'ZCBM')]/parent::*/preceding-sibling::*[3]/descendant::*[2]")
					
					# 点击资金到账按钮
					js_click("xpath", "//span[text()='资金到账']")
					sleep(1)
					
					# 切入资金到账的iframe窗体
					switch_to("xpath", "//iframe[@id='accountWin-iframe']")
					sleep(1)
					
					# 输入到账金额
					click("xpath", "//input[@id='amount-input']")
					sleep(1)
					clear("xpath", "//input[@id='amount-input']")
					sleep(1)
					input("xpath", "//input[@id='amount-input']", "80")
					sleep(1)
					
					# 点击保存按钮
					click("xpath", "//span[text()='保存']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("发行登记，资金到账成功！")
					logging.info("发行登记，资金到账成功！")
					sleep(3)
					
					# 债券转股
					# 切入‘发行登记’的iframe窗体
					switch_to("xpath", "//iframe[@id='bondissuance-tab-iframe']")
					
					# 勾选
					click("xpath", "//div[contains(text(),'ZCBM')]/parent::*/preceding-sibling::*[3]/descendant::*[2]")
					
					# 点击债券转股按钮
					js_click("xpath", "//span[text()='债券转股']")
					sleep(1)
					
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'成功转股:1条！')]")
					print("发行登记，债券转股成功！")
					logging.info("发行登记，债券转股成功！")
					time.sleep(3)
					
					# 重新生成还款付息
					# 切入‘发行登记’的iframe窗体
					switch_to("xpath", "//iframe[@id='bondissuance-tab-iframe']")
					
					# 勾选
					click("xpath", "//div[contains(text(),'ZCBM')]/parent::*/preceding-sibling::*[3]/descendant::*[2]")
					
					# 点击重新生成还款付息按钮
					click("xpath", "//span[text()='重新生成还本付息']")
					
					# 点击确认按钮
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'成功重新计息:1条！')]")
					print("发行登记，重新生成还本付息成功！")
					logging.info("发行登记，重新生成还本付息成功！")
					time.sleep(3)
				
				if i == 5:
					# 切入‘发行登记’的iframe窗体
					switch_to("xpath", "//iframe[@id='bondissuance-tab-iframe']")
					
					# 选择未审核
					click("xpath", "//input[@id='combobox-input-approvestate']")
					sleep(1)
					click("xpath", "//div[@id='f-combo-approvestate-list-0']/child::*[1]")
					sleep(1)
					click("xpath", "//div[@id='f-combo-approvestate-list-1']/child::*[1]")
					sleep(1)
					
					# 点击查询
					click("xpath", "//span[text()='查询']")
					
					# 勾选
					click("xpath", "//div[contains(text(),'ZCBM')]/parent::*/preceding-sibling::*[3]/descendant::*[2]")
					
					# 点击审核按钮
					click("xpath", "//span[text()='审核']")
					
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'成功审核1条记录')]")
					print("发行登记，第三次审核成功！")
					logging.info("发行登记，第三次审核成功！")
					time.sleep(3)
					
					# 作废
					# 切入‘发行登记’的iframe窗体
					switch_to("xpath", "//iframe[@id='bondissuance-tab-iframe']")
					sleep(1)
					
					# 选择已审核
					click("xpath", "//input[@id='combobox-input-approvestate']")
					sleep(1)
					click("xpath", "//div[@id='f-combo-approvestate-list-0']/child::*[1]")
					sleep(1)
					click("xpath", "//div[@id='f-combo-approvestate-list-1']/child::*[1]")
					sleep(1)
					
					# 点击查询
					click("xpath", "//span[text()='查询']")
					
					# 勾选
					click("xpath", "//div[contains(text(),'ZCBM')]/parent::*/preceding-sibling::*[3]/descendant::*[2]")
					
					# 点击作废按钮
					click("xpath", "//span[text()='作废']")
					
					# 点击确认按钮
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'成功作废1条记录！')]")
					print("发行登记，作废成功！")
					logging.info("发行登记，作废成功！")
					time.sleep(3)
				
				if i == 6:
					# 第4次审核
					# 切入‘发行登记’的iframe窗体
					switch_to("xpath", "//iframe[@id='bondissuance-tab-iframe']")
					sleep(1)
					
					# 选择未审核
					click("xpath", "//input[@id='combobox-input-approvestate']")
					sleep(1)
					click("xpath", "//div[@id='f-combo-approvestate-list-0']/child::*[1]")
					sleep(1)
					click("xpath", "//div[@id='f-combo-approvestate-list-1']/child::*[1]")
					sleep(1)
					
					# 点击查询
					click("xpath", "//span[text()='查询']")
					
					# 勾选
					click("xpath", "//div[contains(text(),'ZCBM')]/parent::*/preceding-sibling::*[3]/descendant::*[2]")
					
					# 点击审核按钮
					click("xpath", "//span[text()='审核']")
					
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'成功审核1条记录')]")
					print("发行登记，第四次审核成功！")
					logging.info("发行登记，第四次审核成功！")
					time.sleep(3)
					
					switch_to("xpath", "//iframe[@id='bondissuance-tab-iframe']")
					sleep(1)
					
					# 选择已审核
					click("xpath", "//input[@id='combobox-input-approvestate']")
					sleep(1)
					click("xpath", "//div[@id='f-combo-approvestate-list-0']/child::*[1]")
					sleep(1)
					click("xpath", "//div[@id='f-combo-approvestate-list-1']/child::*[1]")
					sleep(1)
					
					# 点击查询
					click("xpath", "//span[text()='查询']")
					
					# 勾选
					click("xpath", "//div[contains(text(),'ZCBM')]/parent::*/preceding-sibling::*[3]/descendant::*[2]")
					
					# 点击资金到账按钮
					js_click("xpath", "//span[text()='资金到账']")
					sleep(1)
					
					# 切入资金到账的iframe窗体
					switch_to("xpath", "//iframe[@id='accountWin-iframe']")
					sleep(1)
					
					# 输入到账金额
					click("xpath", "//input[@id='amount-input']")
					sleep(1)
					clear("xpath", "//input[@id='amount-input']")
					sleep(1)
					input("xpath", "//input[@id='amount-input']", "88")
					sleep(1)
					
					# 点击保存按钮
					click("xpath", "//span[text()='保存后生成收款单']")
					sleep(1)
					switch_parent()
					
					# 进入确认下一步页面
					switch_to("xpath", "//iframe[@id='addRecWin-iframe']")
					sleep(1)
					
					click("xpath", "//span[text()='下一步']")
					
					switch_parent()
					
					switch_to("xpath", "//iframe[@id='addRecWin-iframe']")
					sleep(1)
					
					# 选择交易类型
					click("xpath", "//input[@id='combobox-input-paytypeid']")
					input("xpath", "//input[@id='combobox-input-paytypeid']", "201-外部收款")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-paytypeid']")
					input_enter("xpath", "//input[@id='combobox-input-paytypeid']")
					time.sleep(1)
					
					# 选择结算方式
					click("xpath", "//input[@id='combobox-input-settlementmodeid']")
					clear("xpath", "//input[@id='combobox-input-settlementmodeid']")
					input_down("xpath", "//input[@id='combobox-input-settlementmodeid']")
					sleep(1)
					input_enter("xpath", "//input[@id='combobox-input-settlementmodeid']")
					time.sleep(1)
					
					# 收方账户
					click("xpath", "//input[@id='combobox-input-ourbankaccountid']")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-ourbankaccountid']")
					sleep(1)
					input_enter("xpath", "//input[@id='combobox-input-ourbankaccountid']")
					time.sleep(1)
					
					# 付方组织
					click("xpath", "//input[@id='combobox-input-oppcounterpartyid']")
					sleep(1)
					input("xpath", "//input[@id='combobox-input-oppcounterpartyid']", "Mindy")
					click("xpath", "//div[contains(text(),'Mindy自动化测试')]")
					sleep(1)
					
					# 点击保存
					click("xpath", "//span[text()='保存']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("发行登记，资金到账成功！")
					logging.info("发行登记，资金到账成功！")
					sleep(3)
			
			# 退出所有iframe窗体
			switch_default()
			
			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='发行登记']/child::*[1]")
			
			# 打印操作成功日志
			print("发行登记，操作成功!")
			logging.info("发行登记，操作成功!")
			time.sleep(2)
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("发行登记,失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		
		#  配置自定义字段，重新回归测试
		#  系统设置里面设置自定义字段
		try:
			
			# 点击系统设置
			click("xpath", "//div[@class='sysconfigset']")
			
			# 点击进入系统设置页面
			switch_to("xpath", "//iframe[@id='systemconfig-tab-iframe']")
			sleep(1)
			
			logging.info("开始测试基础资料--自定义字段的功能")
			# 将页面的滚动条滑动到‘自定义字段’页面的地方
			js_gd("xpath", "//span[contains(text(),'自定义字段')]")
			# 用JS的方法点击自定义字段菜单按钮
			js_click("xpath", "//span[contains(text(),'自定义字段')]")
			
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
			
			# 点击选择
			click("xpath", "//div[@title='扩展表说明:债券发行登记扩展表']/parent::*[1]/preceding-sibling::*[2]/descendant::*[2]")
			sleep(1)
			
			click("xpath", "//span[text()='配置']")
			sleep(1)
			
			# 进入iframe 窗体
			switch_to("xpath", "//iframe[@id='modWin-iframe']")
			sleep(1)
			
			# 点击新增行
			click("xpath", "//span[text()='新增行']")
			sleep(1)
			
			# 输入排序号
			input("xpath", "//input[@id='customformfieldconfig-displayorder-0-input']", "1")
			sleep(1)
			
			# 选择字段名称
			click("xpath", "//input[@id='combobox-input-customformfieldconfig-fieldname-0']")
			sleep(1)
			click("xpath", "//div[@title='扩展字段1']")
			sleep(1)
			
			# 选择字段类型
			click("xpath", "//input[@id='combobox-input-customformfieldconfig-fieldtype-0']")
			sleep(1)
			click("xpath", "//div[@title='文本']")
			sleep(1)
			
			# 选择分类名称
			click("xpath", "//input[@id='combobox-input-customformfieldconfig-fieldclass-0']")
			sleep(1)
			input_down("xpath", "//input[@id='combobox-input-customformfieldconfig-fieldclass-0']")
			sleep(1)
			input_enter("xpath", "//input[@id='combobox-input-customformfieldconfig-fieldclass-0']")
			sleep(1)
			
			# 输入字段显示名称
			input("xpath", "//input[@id='customformfieldconfig-fieldcomment-0']", "债券发行测试")
			sleep(1)
			
			# 是否必填
			click("xpath", "//input[@id='combobox-input-customformfieldconfig-isrequired-0']")
			sleep(1)
			# 选择必填
			click("xpath", "//div[@title='√']")
			sleep(1)
			
			# 点击新增行
			click("xpath", "//span[text()='新增行']")
			sleep(1)
			
			# 输入排序号
			input("xpath", "//input[@id='customformfieldconfig-displayorder-1-input']", "2")
			sleep(1)
			
			# 选择字段名称
			click("xpath", "//input[@id='combobox-input-customformfieldconfig-fieldname-1']")
			sleep(1)
			click("xpath", "//div[@title='扩展字段2' and @id='f-combo-customformfieldconfig-fieldname-1-list-1']")
			sleep(1)
			
			# 选择字段类型
			click("xpath", "//input[@id='combobox-input-customformfieldconfig-fieldtype-1']")
			sleep(1)
			input("xpath", "//input[@id='combobox-input-customformfieldconfig-fieldtype-1']", "数值")
			sleep(1)
			input_down("xpath", "//input[@id='combobox-input-customformfieldconfig-fieldtype-1']")
			input_enter("xpath", "//input[@id='combobox-input-customformfieldconfig-fieldtype-1']")
			sleep(1)
			
			# 选择分类名称
			click("xpath", "//input[@id='combobox-input-customformfieldconfig-fieldclass-1']")
			sleep(1)
			input_down("xpath", "//input[@id='combobox-input-customformfieldconfig-fieldclass-1']")
			input_enter("xpath", "//input[@id='combobox-input-customformfieldconfig-fieldclass-1']")
			sleep(1)
			
			# 输入字段显示名称
			input("xpath", "//input[@id='customformfieldconfig-fieldcomment-1']", "债券发行测试2")
			sleep(1)
			
			# 是否必填
			click("xpath", "//input[@id='combobox-input-customformfieldconfig-isrequired-1']")
			sleep(1)
			# 选择必填
			input("xpath", "//input[@id='combobox-input-customformfieldconfig-isrequired-1']", "×")
			sleep(1)
			input_down("xpath", "//input[@id='combobox-input-customformfieldconfig-isrequired-1']")
			sleep(1)
			input_enter("xpath", "//input[@id='combobox-input-customformfieldconfig-isrequired-1']")
			sleep(1)
			
			click("xpath", "//span[text()='保存']")
			
			switch_default()
			
			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功')]")
			print("债券发行登记拓展表，保存成功！")
			time.sleep(3)
			
			# 再次点击基础设置菜单，使之关闭
			# 用JS的方法关闭当前页面
			
			js_click("xpath", "//a[@title='自定义字段']/child::*[1]")
			
			# 打印操作成功日志
			print("自定义字段，操作成功!")
			logging.info("自定义字段，操作成功!")
			time.sleep(2)
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("自定义字段,失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		
		# 系统参数--利率方案
		try:
			# 点击系统设置
			click("xpath", "//div[@class='sysconfigset']")
			
			# 点击进入系统设置页面
			switch_to("xpath", "//iframe[@id='systemconfig-tab-iframe']")
			sleep(1)
			
			logging.info("开始测试基础资料--利率方案功能")
			# 将页面的滚动条滑动到‘利率方案’页面的地方
			js_gd("xpath", "//span[contains(text(),'利率方案')]")
			# 用JS的方法利率方案字段菜单按钮
			js_click("xpath", "//span[contains(text(),'利率方案')]")
			
			switch_default()
			
			switch_to("xpath", "//iframe[@id='interestRateSchemes-tab-iframe']")
			
			# 用JS的方法点击新增按钮
			js_click("xpath", "//span[text()='新增']")
			
			# 切入新增的iframe窗体
			switch_to("xpath", "//iframe[@id='addWin-iframe']")
			sleep(1)
			
			# 输入代码
			input("xpath", "//input[@name='code']", "L08")
			sleep(1)
			
			# 输入名称
			input("xpath", "//input[@id='name']", "债券发行")
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
			
			# 再次点击基础设置菜单，使之关闭
			# 用JS的方法关闭当前页面
			
			js_click("xpath", "//a[@title='利率方案']/child::*[1]")
			
			# 打印操作成功日志
			print("利率方案，操作成功!")
			logging.info("利率方案，操作成功!")
			time.sleep(2)
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("利率方案,失败！" + str(traceback.format_exc()))
			# Action中
			#
			# 新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		
		# 测试发行登记
		try:
			# 点击‘发行登记’菜单
			click("xpath", "//span[text()='发行登记']")
			# 退出所有iframe窗体
			switch_default()
			
			logging.info("开始测试发行登记功能")
			for i in range(1, 7):
				# 切入‘发行登记’的iframe窗体
				switch_to("xpath", "//iframe[@id='bondissuance-tab-iframe']")
				
				# 用JS的方法点击新增按钮
				js_click("xpath", "//span[text()='新增']")
				
				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='addWin-iframe']")
				sleep(1)
				
				# 选择注册编码
				# 点击‘注册编码’框
				click("xpath", "//input[@id='combobox-input-bondregisterid']")
				# 输入ZCBM，模糊查询
				input("xpath", "//input[@id='combobox-input-bondregisterid']", "ZCBM")
				sleep(1)
				double_click("xpath", "//div[contains(text(),'ZCBM')]")
				sleep(1)
				
				# 设置时间的变成存储，变成
				temp = time.strftime("%Y%m%d%H%M%S")
				# 输入债券代码
				input("xpath", "//input[@id='code']", "Test" + str(temp))
				sleep(1)
				
				# 设置时间的变成存储，变成
				temp1 = time.strftime("%H%M%S")
				# 输入债券全称
				input("xpath", "//input[@id='name']", "债券全称" + str(temp1))
				sleep(1)
				
				# 输入债券简称
				input("xpath", "//input[@id='simplename']", "债券简称" + str(temp1))
				time.sleep(1)
				
				# 输入发行日期
				# 点击发行日期的日历按钮
				js_click("xpath", "//span[@id='issuancedate-trigger']")
				time.sleep(1)
				
				# 退出所有iframe窗体
				switch_default()
				# 切入日历框的iframe
				switch_to("xpath", "//iframe[@hidefocus='true']")
				# 点击日历框中今天的按钮
				click("xpath", "//input[@id='dpTodayInput']")
				time.sleep(1)
				# 退出当前日历框的iframe窗体
				switch_parent()
				
				# 法定到期日
				# 切入‘发行登记’的iframe窗体
				switch_to("xpath", "//iframe[@id='bondissuance-tab-iframe']")
				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='addWin-iframe']")
				# 点击法定到期日的日历按钮
				js_click("xpath", "//span[@id='legalenddate-trigger']")
				time.sleep(1)
				
				# 退出所有iframe窗体
				switch_default()
				# 切入日历框的iframe
				switch_to("xpath", "//iframe[@hidefocus='true']")
				# 点击日历框中今天的按钮
				click("xpath", "//input[@id='dpTodayInput']")
				time.sleep(1)
				# 退出当前日历框的iframe窗体
				switch_parent()
				
				# 切入‘发行登记’的iframe窗体
				switch_to("xpath", "//iframe[@id='bondissuance-tab-iframe']")
				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='addWin-iframe']")
				
				# 输入发行期限（日）
				# 先清空发行期限（日）内容
				clear("xpath", "//input[@id='termday-input']")
				input("xpath", "//input[@id='termday-input']", "90")
				time.sleep(1)
				
				# 输入含权期限
				input("xpath", "//input[@id='weightterm']", "30")
				time.sleep(1)
				
				# 输入发行金额
				input("xpath", "//input[@id='amount-input']", "100000")
				sleep(1)
				
				# 输入发行场所
				input("xpath", "//input[@id='issuanceplace']", "清算所")
				sleep(1)
				
				# 输入资金用途
				# input("xpath", "//input[@id='purposeid']", "融资使用")
				# sleep(1)
				
				# 第二笔的时候选择‘是否回售’
				if i == 2:
					click("xpath", "//input[@id='isresale']")
				
				# 输入备注
				input("xpath", "//textarea[@id='memo']", "发行登记备注内容")
				sleep(1)
				
				# 计息方式中输入值
				# 点击计息方式插页
				click("xpath", "//span[contains(text(),'计息方式')]")
				sleep(1)
				
				# 1、选择还本方式
				click("xpath", "//input[@id='combobox-input-repaymode']")
				# 按键往下，选择‘按季还款’
				input_down("xpath", "//input[@id='combobox-input-repaymode']")
				input_enter("xpath", "//input[@id='combobox-input-repaymode']")
				time.sleep(1)
				# 2、选择还息方式
				click("xpath", "//input[@id='combobox-input-interestmode']")
				# 按键往下，选择‘按季还款’
				input_down("xpath", "//input[@id='combobox-input-interestmode']")
				input_enter("xpath", "//input[@id='combobox-input-interestmode']")
				time.sleep(1)
				# 3、选择利率方案
				click("xpath", "//input[@id='combobox-input-interestrateschemeid']")
				# 按键往下，选择利率方案
				sleep(2)
				input_down("xpath", "//input[@id='combobox-input-interestrateschemeid']")
				input_enter("xpath", "//input[@id='combobox-input-interestrateschemeid']")
				
				# 费用中输入值
				# 点击费用插页
				click("xpath", "//span[text()='费用']")
				time.sleep(1)
				
				# 点击费用新增行，新增第一行
				click("xpath", "//span[@title='费用类型']/ancestor::*[6]/following-sibling::*[2]/descendant::*[7]")
				sleep(1)
				
				# 在第一行的‘费用类型’中选择‘律师费’
				click("xpath", "//input[@id='combobox-input-feesgrid-feestype-0']")
				time.sleep(1)
				input("xpath", "//input[@id='combobox-input-feesgrid-feestype-0']", "律师费")
				time.sleep(1)
				input_down("xpath", "//input[@id='combobox-input-feesgrid-feestype-0']")
				time.sleep(1)
				input_enter("xpath", "//input[@id='combobox-input-feesgrid-feestype-0']")
				# 模拟回车键
				keyDown('enter')
				keyUp('enter')
				time.sleep(1)
				# 在第一行的‘费用金额’中输入金额
				click("xpath", "//input[@id='feesgrid-feesamount-0-input']")
				input("xpath", "//input[@id='feesgrid-feesamount-0-input']", "100")
				time.sleep(1)
				# 在第一行的‘费用日期’中输入日期
				today = date.today()
				input("xpath", "//input[@id='feesgrid-feesdate-0-input']", str(today))
				# 模拟回车键
				keyDown('enter')
				keyUp('enter')
				time.sleep(1)
				# 在第一行的‘付款主体’中‘001000-亚唐科技’
				click("xpath", "//input[@id='combobox-input-feesgrid-paymainpart-0']")
				input("xpath", "//input[@id='combobox-input-feesgrid-paymainpart-0']", "001000-亚唐科技")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-feesgrid-paymainpart-0']")
				input_enter("xpath", "//input[@id='combobox-input-feesgrid-paymainpart-0']")
				# 在第一行的‘备注’中输入‘第一行备注律师费’
				input("xpath", "//input[@id='feesgrid-description-0']", "第一行备注律师费")
				sleep(1)
				
				# 点击费用新增行，新增第二行
				click("xpath", "//span[@title='费用类型']/ancestor::*[6]/following-sibling::*[2]/descendant::*[7]")
				sleep(1)
				
				# 在第二行的‘费用类型’中选择‘其他’
				click("xpath", "//input[@id='combobox-input-feesgrid-feestype-1']")
				time.sleep(1)
				input("xpath", "//input[@id='combobox-input-feesgrid-feestype-1']", "其他")
				time.sleep(1)
				input_down("xpath", "//input[@id='combobox-input-feesgrid-feestype-1']")
				time.sleep(1)
				input_enter("xpath", "//input[@id='combobox-input-feesgrid-feestype-1']")
				# 模拟回车键
				keyDown('enter')
				keyUp('enter')
				time.sleep(1)
				
				# 在第二行的‘费用金额’中输入金额
				click("xpath", "//input[@id='feesgrid-feesamount-1-input']")
				input("xpath", "//input[@id='feesgrid-feesamount-1-input']", "22222")
				time.sleep(1)
				
				# 在第二行的‘费用日期’中输入日期
				today = date.today()
				input("xpath", "//input[@id='feesgrid-feesdate-1-input']", str(today))
				# 模拟回车键
				keyDown('enter')
				keyUp('enter')
				time.sleep(1)
				
				# 在第二行的‘付款主体’中‘001000-亚唐科技’
				click("xpath", "//input[@id='combobox-input-feesgrid-paymainpart-1']")
				input("xpath", "//input[@id='combobox-input-feesgrid-paymainpart-1']", "001000-亚唐科技")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-feesgrid-paymainpart-1']")
				input_enter("xpath", "//input[@id='combobox-input-feesgrid-paymainpart-1']")
				# 在第二行的‘备注’中输入‘第二行备注其他费’
				input("xpath", "//input[@id='feesgrid-description-1']", "第二行备注其他费")
				sleep(1)
				
				# 点击主承销商插页
				click("xpath", "//span[text()='主承销商']")
				time.sleep(1)
				
				# 主承销商插页修改承销金额
				# 修改第一行的金额
				click("xpath", "//input[@id='consigneegrid-amount-0-input']")
				sleep(1)
				clear("xpath", "//input[@id='consigneegrid-amount-0-input']")
				sleep(1)
				input("xpath", "//input[@id='consigneegrid-amount-0-input']", "2000")
				sleep(1)
				
				# 修改第一行的备注框
				
				click("xpath", "//input[@id='consigneegrid-description-0']")
				sleep(1)
				clear("xpath", "//input[@id='consigneegrid-description-0']")
				sleep(1)
				input("xpath", "//input[@id='consigneegrid-description-0']", "第一行2000RMB金额")
				sleep(1)
				
				# 修改第二行金额
				click("xpath", "//input[@id='consigneegrid-amount-1-input']")
				sleep(1)
				clear("xpath", "//input[@id='consigneegrid-amount-1-input']")
				sleep(1)
				input("xpath", "//input[@id='consigneegrid-amount-1-input']", "1000")
				sleep(1)
				
				# 修改第一行的备注框
				click("xpath", "//input[@id='consigneegrid-description-1']")
				sleep(1)
				clear("xpath", "//input[@id='consigneegrid-description-1']")
				sleep(1)
				input("xpath", "//input[@id='consigneegrid-description-1']", "第二行1000RMB金额")
				sleep(1)
				
				# 公共版本是‘头寸准备计划’；点击‘头寸准备计划’插页，
				click("xpath", "//span[text()='头寸准备计划']")
				# 阳光城版本是‘资金归集计划’；点击‘资金归集计划’插页，
				
				# click("xpath", "//span[text()='资金归集计划']")
				time.sleep(1)
				
				# 点击头寸准备计划插页
				# 点击头寸准备计划新增行，新增第一行
				click("xpath", "//span[@title='类型']/ancestor::*[6]/following-sibling::*[2]/descendant::*[7]")
				sleep(1)
				
				# 在第一行的‘类型’中选择‘还本’
				click("xpath", "//input[@id='combobox-input-positionplangrid-positionplantype-0']")
				time.sleep(1)
				input("xpath", "//input[@id='combobox-input-positionplangrid-positionplantype-0']", "还本")
				time.sleep(1)
				input_down("xpath", "//input[@id='combobox-input-positionplangrid-positionplantype-0']")
				time.sleep(1)
				input_enter("xpath", "//input[@id='combobox-input-positionplangrid-positionplantype-0']")
				# 模拟回车键
				keyDown('enter')
				keyUp('enter')
				time.sleep(1)
				# 在第一行的‘日期’中输入日期
				today = date.today()
				input("xpath", "//input[@id='positionplangrid-positionplandate-0-input']",
				      str(today + timedelta(days=30)))
				# 模拟回车键
				keyDown('enter')
				keyUp('enter')
				time.sleep(1)
				# 在第一行的‘金额’中输入值
				clear("xpath", "//input[@id='positionplangrid-positionplanamount-0-input']")
				input("xpath", "//input[@id='positionplangrid-positionplanamount-0-input']", "500")
				time.sleep(1)
				# 在第一行的‘备注’中输入‘第一行备注还本500’
				input("xpath", "//input[@id='positionplangrid-description-0']", "第一行备注还本500")
				sleep(1)
				
				# 点击头寸准备计划新增行，新增第二行
				click("xpath", "//span[@title='类型']/ancestor::*[6]/following-sibling::*[2]/descendant::*[7]")
				sleep(1)
				
				# 在第二行的‘类型’中选择‘还息’
				js_click("xpath",
				         "//input[@id='combobox-input-positionplangrid-positionplantype-1']/following-sibling::*[1]")
				time.sleep(1)
				input("xpath", "//input[@id='combobox-input-positionplangrid-positionplantype-1']", "还息")
				time.sleep(1)
				input_down("xpath", "//input[@id='combobox-input-positionplangrid-positionplantype-1']")
				time.sleep(1)
				input_enter("xpath", "//input[@id='combobox-input-positionplangrid-positionplantype-1']")
				# 模拟回车键
				keyDown('enter')
				keyUp('enter')
				time.sleep(1)
				# 在第二行的‘日期’中输入日期
				today = date.today()
				input("xpath", "//input[@id='positionplangrid-positionplandate-1-input']",
				      str(today + timedelta(days=30)))
				# 模拟回车键
				keyDown('enter')
				keyUp('enter')
				time.sleep(1)
				# 在第二行的‘金额’中输入值
				clear("xpath", "//input[@id='positionplangrid-positionplanamount-1-input']")
				sleep(1)
				input("xpath", "//input[@id='positionplangrid-positionplanamount-1-input']", "200")
				time.sleep(1)
				# 在第二行的‘备注’中输入‘第二行备注还息200’
				input("xpath", "//input[@id='positionplangrid-description-1']", "第二行备注还息200")
				sleep(1)
				
				# 担保信息
				
				# 募集资金
				
				# 自定义属性
				click("xpath", "//span[text()='自定义属性']")
				sleep(1)
				
				if i == 1:
					# 输入必填文本
					input("xpath", "//input[@id='extfield1']", "自定义发行登记必填")
					sleep(1)
				
				else:
					# 输入必填文本
					input("xpath", "//input[@id='extfield1']", "自定义发行登记必填")
					sleep(1)
					
					# 输入非必填字段
					
					input("xpath", "//input[@id='extfield2-input']", "自定义发行登记非必填")
					sleep(1)
				
				# 点击保存按钮
				click("xpath", "//span[text()='保存']")
				
				# 退出所有iframe窗体
				switch_default()
				
				# 用隐式等待方法等页面出现提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				print("发行登记第%s次，保存成功！" % i)
				logging.info("发行登记第%s次，保存成功！" % i)
				time.sleep(3)
				
				# 第一笔 先修改 再审核又取消审核、再删除新增的发行登记
				if i == 1:
					# 切入‘发行登记’的iframe窗体
					switch_to("xpath", "//iframe[@id='bondissuance-tab-iframe']")
					
					# 点击查看
					# 用JS的方法点击放大镜
					js_click("xpath", "//span[@class='f-contrac-close']")
					sleep(1)
					
					# 注册合同号
					click("xpath", "//input[@id='combobox-input-bondregisterid']")
					sleep(1)
					input("xpath", "//input[@id='combobox-input-bondregisterid']", "ZCBM")
					sleep(1)
					click("xpath", "//span[text()='代码-名称']/ancestor::*[3]/preceding-sibling::*[1]/descendant::*[2]")
					sleep(1)
					
					# 点击查询
					click("xpath", "//span[text()='查询']")
					
					# 修改
					# 勾选
					click("xpath", "//div[contains(text(),'ZCBM')]/parent::*/preceding-sibling::*[3]/descendant::*[2]")
					
					# 点击修改按钮
					click("xpath", "//span[text()='修改']")
					sleep(1)
					
					# 切入修改的iframe窗体
					switch_to("xpath", "//iframe[@id='modWin-iframe']")
					sleep(1)
					
					# 修改备注框
					input("xpath", "//textarea[@id='addcreditmeasures']", "自动化测试修改")
					sleep(1)
					
					# 备注框中填入值
					input("xpath", "//textarea[@id='memo']", "自动化测试修改")
					sleep(1)
					
					# 点击保存按钮
					click("xpath", "//span[text()='保存']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("发行登记，修改成功！")
					logging.info("发行登记，修改成功！")
					time.sleep(3)
					
					# 审核--取消审核 # 第一次审核
					# 切入‘发行登记’的iframe窗体
					switch_to("xpath", "//iframe[@id='bondissuance-tab-iframe']")
					
					# 勾选
					click("xpath", "//div[contains(text(),'ZCBM')]/parent::*/preceding-sibling::*[3]/descendant::*[2]")
					
					# 点击审核按钮
					click("xpath", "//span[text()='审核']")
					
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'成功审核1条记录')]")
					print("发行登记，第一次审核成功！")
					logging.info("发行登记，第一次审核成功！")
					time.sleep(3)
					
					# 取消审核
					# 切入‘发行登记’的iframe窗体
					switch_to("xpath", "//iframe[@id='bondissuance-tab-iframe']")
					
					# 勾选
					click("xpath", "//div[contains(text(),'ZCBM')]/parent::*/preceding-sibling::*[3]/descendant::*[2]")
					
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
					implici_wait("xpath", "//span[contains(text(),'成功取消审核:1条')]")
					print("发行登记，第一次审核后取消审核成功！")
					logging.info("发行登记，第一次审核后取消审核成功！")
					time.sleep(3)
					
					# 切入‘发行登记’的iframe窗体
					switch_to("xpath", "//iframe[@id='bondissuance-tab-iframe']")
					
					# 删除
					# 勾选
					click("xpath", "//div[contains(text(),'ZCBM')]/parent::*/preceding-sibling::*[3]/descendant::*[2]")
					
					# 点击删除按钮
					click("xpath", "//span[text()='删除']")
					
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现删除的提示框
					implici_wait("xpath", "//span[contains(text(),'成功删除1条记录！')]")
					print("发行登记，删除成功！")
					logging.info("发行登记，删除成功！")
					time.sleep(3)
				
				# 第二笔，审核、资金到账、取消到账、生成到账交易单
				if i == 2:
					# 第二次审核
					# 切入‘发行登记’的iframe窗体
					switch_to("xpath", "//iframe[@id='bondissuance-tab-iframe']")
					
					# 勾选
					click("xpath", "//div[contains(text(),'ZCBM')]/parent::*/preceding-sibling::*[3]/descendant::*[2]")
					
					# 点击审核按钮
					click("xpath", "//span[text()='审核']")
					
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'成功审核1条记录')]")
					print("发行登记，第二次审核成功！")
					logging.info("发行登记，第二次审核成功！")
					time.sleep(3)
					
					# 资金到账
					# 切入‘发行登记’的iframe窗体
					switch_to("xpath", "//iframe[@id='bondissuance-tab-iframe']")
					
					# 勾选
					click("xpath", "//div[contains(text(),'ZCBM')]/parent::*/preceding-sibling::*[3]/descendant::*[2]")
					
					# 点击资金到账按钮
					js_click("xpath", "//span[text()='资金到账']")
					sleep(1)
					
					# 切入资金到账的iframe窗体
					switch_to("xpath", "//iframe[@id='accountWin-iframe']")
					sleep(1)
					
					# 输入到账金额
					click("xpath", "//input[@id='amount-input']")
					sleep(1)
					clear("xpath", "//input[@id='amount-input']")
					sleep(1)
					input("xpath", "//input[@id='amount-input']", "80")
					sleep(1)
					
					# 点击保存按钮
					click("xpath", "//span[text()='保存']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("发行登记，资金到账成功！")
					logging.info("发行登记，资金到账成功！")
					sleep(3)
					
					# 资金到账--取消到账
					# 切入‘发行登记’的iframe窗体
					switch_to("xpath", "//iframe[@id='bondissuance-tab-iframe']")
					
					# 勾选
					click("xpath", "//div[contains(text(),'ZCBM')]/parent::*/preceding-sibling::*[3]/descendant::*[2]")
					
					# 用JS方便点击‘资金到账’按钮旁边的倒三角形
					js_click("xpath", "//span[text()='资金到账']/parent::*/following-sibling::*/child::*")
					sleep(1)
					
					# 点击取消到账按钮
					js_click("xpath", "//a[contains(text(),'取消到账')]")
					sleep(1)
					
					# 切入取消到账的窗体页面cancelAccountWin-iframe
					switch_to("xpath", "//iframe[@id='cancelAccountWin-iframe']")
					
					# 点击勾选当前资金到账的数据
					click("xpath", "//a[text()='未生成']/ancestor::*[2]/preceding-sibling::*[1]/descendant::*[2]")
					sleep(1)
					
					# 点击取消到账
					click("xpath", "//span[text()='取消到账']")
					sleep(1)
					
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'成功取消:1条记录！')]")
					print("发行登记，取消到账成功！")
					logging.info("发行登记，取消到账成功！")
					sleep(3)
					
					# 切入资金到账的iframe窗体
					switch_to("xpath", "//iframe[@id='bondissuance-tab-iframe']")
					sleep(1)
					
					# 点击关闭取消到账的关闭按钮
					click("xpath", "//span[text()='到账取消']/preceding-sibling::*[1]")
					
					switch_default()
					
					# 资金到账
					# 切入‘发行登记’的iframe窗体
					switch_to("xpath", "//iframe[@id='bondissuance-tab-iframe']")
					
					# 点击资金到账按钮
					js_click("xpath", "//span[text()='资金到账']")
					sleep(1)
					
					# 切入资金到账的iframe窗体
					switch_to("xpath", "//iframe[@id='accountWin-iframe']")
					sleep(1)
					
					# 输入到账金额
					click("xpath", "//input[@id='amount-input']")
					sleep(1)
					clear("xpath", "//input[@id='amount-input']")
					sleep(1)
					input("xpath", "//input[@id='amount-input']", "80")
					sleep(1)
					
					# 点击保存按钮
					click("xpath", "//span[text()='保存']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("发行登记，资金到账成功！")
					logging.info("发行登记，资金到账成功！")
					sleep(3)
				
				if i == 3:
					# 债券转股
					# 切入‘发行登记’的iframe窗体
					switch_to("xpath", "//iframe[@id='bondissuance-tab-iframe']")
					
					# 选择已审核、未生成的
					# 用JS的方法点击高级查询按钮
					js_click("xpath", "//span[text()='高级查询']")
					
					click("xpath", "//input[@id='combobox-input-property_0']")
					sleep(1)
					clear("xpath", "//input[@id='combobox-input-property_0']")
					sleep(1)
					# 输入作废状态，通过模糊匹配搜索
					input("xpath", "//input[@id='combobox-input-property_0']", "审核状态")
					sleep(1)
					# 模拟回车
					click("xpath", "//div[contains(text(),'审核状态')]")
					sleep(1)
					
					click("xpath", "//input[@id='combobox-input-condition_0']")
					sleep(1)
					# 输入包含，通过模糊匹配搜索
					input("xpath", "//input[@id='combobox-input-condition_0']", "包含")
					sleep(1)
					# 模拟回车
					click("xpath", "//div[contains(text(),'包含')]")
					sleep(1)
					
					click("xpath", "//input[@id='combobox-input-value_0']")
					sleep(1)
					# 输入审核状态，通过模糊匹配搜索
					click("xpath", "//div[contains(text(),'已审核')]/preceding-sibling::*[1]")
					sleep(1)
					
					# 到账状态
					click("xpath", "//input[@id='combobox-input-property_1']")
					sleep(1)
					clear("xpath", "//input[@id='combobox-input-property_1']")
					sleep(1)
					# 输入作废状态，通过模糊匹配搜索
					input("xpath", "//input[@id='combobox-input-property_1']", "到账状态")
					sleep(1)
					# 模拟回车
					click("xpath", "//div[contains(text(),'到账状态')]")
					sleep(1)
					
					click("xpath", "//input[@id='combobox-input-value_1']")
					sleep(1)
					# 输入放款状态，通过模糊匹配搜索
					click("xpath", "//div[contains(text(),'完全到账')]/preceding-sibling::*[1]")
					sleep(1)
					
					click("xpath", "//div[contains(text(),'部分到账')]/preceding-sibling::*[1]")
					sleep(1)
					
					click("xpath", "//div[contains(text(),'查询')]")
					sleep(1)
					
					js_click("xpath", "//span[text()='自定义查询']/preceding-sibling::*[1]")
					sleep(1)
					
					# 勾选
					click("xpath", "//div[contains(text(),'ZCBM')]/parent::*/preceding-sibling::*[3]/descendant::*[2]")
					
					# 点击债券替换按钮
					js_click("xpath", "//span[text()='债券替换']")
					sleep(1)
					
					# 切入债券替换的iframe窗体
					switch_to("xpath", "//iframe[@id='modWin-iframe']")
					sleep(1)
					
					# 设置时间的变成存储，变成
					temp = time.strftime("%Y%m%d%H%M%S")
					# 输入债券代码
					input("xpath", "//input[@id='code']", "Test" + str(temp))
					sleep(1)
					
					# 设置时间的变成存储，变成
					temp1 = time.strftime("%H%M%S")
					# 输入债券全称
					input("xpath", "//input[@id='name']", "债券全称" + str(temp1))
					sleep(1)
					
					# 输入债券简称
					input("xpath", "//input[@id='simplename']", "债券简称" + str(temp1))
					time.sleep(1)
					
					# 输入发行金额
					click("xpath", "//input[@id='amount-input']")
					sleep(1)
					clear("xpath", "//input[@id='amount-input']")
					sleep(1)
					input("xpath", "//input[@id='amount-input']", "100000")
					sleep(1)
					
					# 点击主承销商插页
					click("xpath", "//span[text()='主承销商']")
					time.sleep(1)
					
					# 主承销商插页修改承销金额
					# 修改第一行的金额
					click("xpath", "//input[@id='consigneegrid-amount-0-input']")
					sleep(1)
					clear("xpath", "//input[@id='consigneegrid-amount-0-input']")
					sleep(1)
					input("xpath", "//input[@id='consigneegrid-amount-0-input']", "2000")
					sleep(1)
					
					# 修改第一行的备注框
					click("xpath", "//input[@id='consigneegrid-description-0']")
					sleep(1)
					clear("xpath", "//input[@id='consigneegrid-description-0']")
					sleep(1)
					
					# 修改第二行金额
					click("xpath", "//input[@id='consigneegrid-amount-1-input']")
					sleep(1)
					clear("xpath", "//input[@id='consigneegrid-amount-1-input']")
					sleep(1)
					input("xpath", "//input[@id='consigneegrid-amount-1-input']", "1000")
					sleep(1)
					
					# 修改第一行的备注框
					click("xpath", "//input[@id='consigneegrid-description-1']")
					sleep(1)
					clear("xpath", "//input[@id='consigneegrid-description-1']")
					sleep(1)
					
					# 点击保存按钮
					click("xpath", "//span[text()='保存']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("发行登记，债券替换保存成功！")
					logging.info("发行登记，债券替换保存成功！")
					time.sleep(3)
				
				if i == 4:
					# 第二次审核
					# 切入‘发行登记’的iframe窗体
					switch_to("xpath", "//iframe[@id='bondissuance-tab-iframe']")
					sleep(1)
					
					# # 点击查看
					# # 用JS的方法点击放大镜
					# js_click("xpath", "//span[@class='f-contrac-close']")
					# sleep(1)
					
					# 选择未审核
					click("xpath", "//input[@id='combobox-input-approvestate']")
					sleep(1)
					click("xpath", "//div[@id='f-combo-approvestate-list-0']/child::*[1]")
					sleep(1)
					
					# 点击查询
					click("xpath", "//span[text()='查询']")
					
					# 勾选
					click("xpath", "//div[contains(text(),'ZCBM')]/parent::*/preceding-sibling::*[3]/descendant::*[2]")
					
					# 点击审核按钮
					click("xpath", "//span[text()='审核']")
					
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'成功审核1条记录')]")
					print("发行登记，第二次审核成功！")
					logging.info("发行登记，第二次审核成功！")
					time.sleep(3)
					
					switch_to("xpath", "//iframe[@id='bondissuance-tab-iframe']")
					sleep(1)
					
					# 选择已审核
					click("xpath", "//input[@id='combobox-input-approvestate']")
					sleep(1)
					click("xpath", "//div[@id='f-combo-approvestate-list-0']/child::*[1]")
					sleep(1)
					click("xpath", "//div[@id='f-combo-approvestate-list-1']/child::*[1]")
					sleep(1)
					
					# 点击查询
					click("xpath", "//span[text()='查询']")
					
					# # 资金到账
					# # 切入‘发行登记’的iframe窗体
					# switch_to("xpath", "//iframe[@id='bondissuance-tab-iframe']")
					
					# 勾选
					click("xpath", "//div[contains(text(),'ZCBM')]/parent::*/preceding-sibling::*[3]/descendant::*[2]")
					
					# 点击资金到账按钮
					js_click("xpath", "//span[text()='资金到账']")
					sleep(1)
					
					# 切入资金到账的iframe窗体
					switch_to("xpath", "//iframe[@id='accountWin-iframe']")
					sleep(1)
					
					# 输入到账金额
					click("xpath", "//input[@id='amount-input']")
					sleep(1)
					clear("xpath", "//input[@id='amount-input']")
					sleep(1)
					input("xpath", "//input[@id='amount-input']", "80")
					sleep(1)
					
					# 点击保存按钮
					click("xpath", "//span[text()='保存']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("发行登记，资金到账成功！")
					logging.info("发行登记，资金到账成功！")
					sleep(3)
					
					# 债券转股
					# 切入‘发行登记’的iframe窗体
					switch_to("xpath", "//iframe[@id='bondissuance-tab-iframe']")
					
					# 勾选
					click("xpath", "//div[contains(text(),'ZCBM')]/parent::*/preceding-sibling::*[3]/descendant::*[2]")
					
					# 点击债券转股按钮
					js_click("xpath", "//span[text()='债券转股']")
					sleep(1)
					
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'成功转股:1条！')]")
					print("发行登记，债券转股成功！")
					logging.info("发行登记，债券转股成功！")
					time.sleep(3)
					
					# 重新生成还款付息
					# 切入‘发行登记’的iframe窗体
					switch_to("xpath", "//iframe[@id='bondissuance-tab-iframe']")
					
					# 勾选
					click("xpath", "//div[contains(text(),'ZCBM')]/parent::*/preceding-sibling::*[3]/descendant::*[2]")
					
					# 点击重新生成还款付息按钮
					click("xpath", "//span[text()='重新生成还本付息']")
					
					# 点击确认按钮
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'成功重新计息:1条！')]")
					print("发行登记，重新生成还本付息成功！")
					logging.info("发行登记，重新生成还本付息成功！")
					time.sleep(3)
				
				if i == 5:
					# 切入‘发行登记’的iframe窗体
					switch_to("xpath", "//iframe[@id='bondissuance-tab-iframe']")
					
					# 选择未审核
					click("xpath", "//input[@id='combobox-input-approvestate']")
					sleep(1)
					click("xpath", "//div[@id='f-combo-approvestate-list-0']/child::*[1]")
					sleep(1)
					click("xpath", "//div[@id='f-combo-approvestate-list-1']/child::*[1]")
					sleep(1)
					
					# 点击查询
					click("xpath", "//span[text()='查询']")
					
					# 勾选
					click("xpath", "//div[contains(text(),'ZCBM')]/parent::*/preceding-sibling::*[3]/descendant::*[2]")
					
					# 点击审核按钮
					click("xpath", "//span[text()='审核']")
					
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'成功审核1条记录')]")
					print("发行登记，第三次审核成功！")
					logging.info("发行登记，第三次审核成功！")
					time.sleep(3)
					
					# 作废
					# 切入‘发行登记’的iframe窗体
					switch_to("xpath", "//iframe[@id='bondissuance-tab-iframe']")
					sleep(1)
					
					# 选择已审核
					click("xpath", "//input[@id='combobox-input-approvestate']")
					sleep(1)
					click("xpath", "//div[@id='f-combo-approvestate-list-0']/child::*[1]")
					sleep(1)
					click("xpath", "//div[@id='f-combo-approvestate-list-1']/child::*[1]")
					sleep(1)
					
					# 点击查询
					click("xpath", "//span[text()='查询']")
					
					# 勾选
					click("xpath", "//div[contains(text(),'ZCBM')]/parent::*/preceding-sibling::*[3]/descendant::*[2]")
					
					# 点击作废按钮
					click("xpath", "//span[text()='作废']")
					
					# 点击确认按钮
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'成功作废1条记录！')]")
					print("发行登记，作废成功！")
					logging.info("发行登记，作废成功！")
					time.sleep(3)
				
				if i == 6:
					# 第4次审核
					# 切入‘发行登记’的iframe窗体
					switch_to("xpath", "//iframe[@id='bondissuance-tab-iframe']")
					sleep(1)
					
					# 选择未审核
					click("xpath", "//input[@id='combobox-input-approvestate']")
					sleep(1)
					click("xpath", "//div[@id='f-combo-approvestate-list-0']/child::*[1]")
					sleep(1)
					click("xpath", "//div[@id='f-combo-approvestate-list-1']/child::*[1]")
					sleep(1)
					
					# 点击查询
					click("xpath", "//span[text()='查询']")
					
					# 勾选
					click("xpath", "//div[contains(text(),'ZCBM')]/parent::*/preceding-sibling::*[3]/descendant::*[2]")
					
					# 点击审核按钮
					click("xpath", "//span[text()='审核']")
					
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'成功审核1条记录')]")
					print("发行登记，第四次审核成功！")
					logging.info("发行登记，第四次审核成功！")
					time.sleep(3)
					
					switch_to("xpath", "//iframe[@id='bondissuance-tab-iframe']")
					sleep(1)
					
					# 选择已审核
					click("xpath", "//input[@id='combobox-input-approvestate']")
					sleep(1)
					click("xpath", "//div[@id='f-combo-approvestate-list-0']/child::*[1]")
					sleep(1)
					click("xpath", "//div[@id='f-combo-approvestate-list-1']/child::*[1]")
					sleep(1)
					
					# 点击查询
					click("xpath", "//span[text()='查询']")
					
					# 勾选
					click("xpath", "//div[contains(text(),'ZCBM')]/parent::*/preceding-sibling::*[3]/descendant::*[2]")
					
					# 点击资金到账按钮
					js_click("xpath", "//span[text()='资金到账']")
					sleep(1)
					
					# 切入资金到账的iframe窗体
					switch_to("xpath", "//iframe[@id='accountWin-iframe']")
					sleep(1)
					
					# 输入到账金额
					click("xpath", "//input[@id='amount-input']")
					sleep(1)
					clear("xpath", "//input[@id='amount-input']")
					sleep(1)
					input("xpath", "//input[@id='amount-input']", "88")
					sleep(1)
					
					# 点击保存按钮
					click("xpath", "//span[text()='保存后生成收款单']")
					sleep(1)
					switch_parent()
					
					# 进入确认下一步页面
					switch_to("xpath", "//iframe[@id='addRecWin-iframe']")
					sleep(1)
					
					click("xpath", "//span[text()='下一步']")
					
					switch_parent()
					
					switch_to("xpath", "//iframe[@id='addRecWin-iframe']")
					sleep(1)
					
					# 选择交易类型
					click("xpath", "//input[@id='combobox-input-paytypeid']")
					input("xpath", "//input[@id='combobox-input-paytypeid']", "201-外部收款")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-paytypeid']")
					input_enter("xpath", "//input[@id='combobox-input-paytypeid']")
					time.sleep(1)
					
					# 选择结算方式
					click("xpath", "//input[@id='combobox-input-settlementmodeid']")
					clear("xpath", "//input[@id='combobox-input-settlementmodeid']")
					input_down("xpath", "//input[@id='combobox-input-settlementmodeid']")
					sleep(1)
					input_enter("xpath", "//input[@id='combobox-input-settlementmodeid']")
					time.sleep(1)
					
					# 收方账户
					click("xpath", "//input[@id='combobox-input-ourbankaccountid']")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-ourbankaccountid']")
					sleep(1)
					input_enter("xpath", "//input[@id='combobox-input-ourbankaccountid']")
					time.sleep(1)
					
					# 付方组织
					click("xpath", "//input[@id='combobox-input-oppcounterpartyid']")
					sleep(1)
					input("xpath", "//input[@id='combobox-input-oppcounterpartyid']", "Mindy")
					click("xpath", "//div[contains(text(),'Mindy自动化测试')]")
					sleep(1)
					
					# 点击保存
					click("xpath", "//span[text()='保存']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("发行登记，资金到账成功！")
					logging.info("发行登记，资金到账成功！")
					sleep(3)
			
			# 退出所有iframe窗体
			switch_default()
			
			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='发行登记']/child::*[1]")
			
			# 打印操作成功日志
			print("发行登记，操作成功!")
			logging.info("发行登记，操作成功!")
			time.sleep(2)
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("发行登记,失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		
		# 债券兑付申请页面功能
		# 此处需要业务关联，需要先在资金结算管理--资金系统收付--收款处理页面完成确认收款
		# 将页面的滚动条滑动到‘资金结算管理’页面的地方
		js_gd("xpath", "//span[contains(text(),'资金结算管理')]")
		# 用JS的方法点击债券发行管理菜单按钮
		js_click("xpath", "//span[contains(text(),'资金结算管理')]")
		
		# 点击资金系统收付
		js_click("xpath", "//span[@title='资金系统收付']")
		sleep(1)
		
		# 点击收款处理菜单
		click("xpath", "//span[@title='收款处理']")
		sleep(1)
		
		# 退出所有的iframe窗体
		switch_default()
		
		# 进入收款处理的页面
		
		switch_to("xpath", "//iframe[@id='generalRecment-tab-iframe']")
		
		switch_to("xpath", "//iframe[@id='subTabEight-iframe']")
		
		# 点击查看
		# 用JS的方法点击放大镜
		js_click("xpath", "//span[@class='f-contrac-close']")
		sleep(1)
		
		# 审核状态
		click("xpath", "//input[@id='combobox-input-approvestate']")
		sleep(1)
		click("xpath", "//div[@title='未审批']")
		sleep(1)
		
		# 收款状态
		click("xpath", "//input[@id='combobox-input-paystate']")
		sleep(1)
		click("xpath", "//div[@title='未收付']")
		sleep(1)
		
		# 收款金额从
		input("xpath", "//input[@id='ouramountstart-input']", "88")
		sleep(1)
		
		# 收款金额到
		input("xpath", "//input[@id='ouramountend-input']", "88")
		sleep(1)
		
		# 点击查询
		click("xpath", "//span[text()='查询']")
		sleep(1)
		
		click("xpath", "//span[text()='收款单号']/ancestor::*[3]/preceding-sibling::*[1]/descendant::*[2]")
		sleep(1)
		
		# 点击确认收款
		click("xpath", "//span[text()='确认收款']")
		sleep(1)
		
		# 点击确定
		click("xpath", "//span[text()='确定']")
		sleep(1)
		
		# 退出所有iframe窗体
		switch_default()
		
		# 用隐式等待方法等页面出现提示框
		implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
		print("收款处理，保存成功！")
		logging.info("收款处理，保存成功！")
		time.sleep(3)
		
		# 将页面的滚动条滑动到‘债券发行管理’页面的地方
		js_gd("xpath", "//span[contains(text(),'债券发行管理')]")
		# 用JS的方法点击债券发行管理菜单按钮
		js_click("xpath", "//span[contains(text(),'债券发行管理')]")
		
		# 测试债券发行管理-债券兑付申请功能
		try:
			
			# 点击债券兑付申请
			click("xpath", "//span[@title='债券兑付申请']")
			# 退出所有的iframe窗体
			switch_default()
			
			logging.info("开始债券兑付申请功能")
			for i in range(1, 4):
				# 切入‘债券兑付申请’的iframe窗体
				switch_to("xpath", "//iframe[@id='bondredeemsapply-tab-iframe']")
				
				# 用JS的方法点击新增按钮
				js_click("xpath", "//span[text()='新增']")
				
				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='modWin-iframe']")
				sleep(1)
				
				# 选择债券代码combobox-input-bondissuancesid
				click("xpath", "//input[@id='combobox-input-bondissuancesid']")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-bondissuancesid']")
				sleep(1)
				input_enter("xpath", "//input[@id='combobox-input-bondissuancesid']")
				sleep(1)
				
				if i == 1:
					
					# 选择债券发行兑付分类
					click("xpath", "//input[@id='combobox-input-redeemtypeid']")
					sleep(1)
					input("xpath", "//input[@id='combobox-input-redeemtypeid']", "兑付")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-redeemtypeid']")
					input_enter("xpath", "//input[@id='combobox-input-redeemtypeid']")
					sleep(1)
				
				else:
					# 选择债券发行兑付分类
					click("xpath", "//input[@id='combobox-input-redeemtypeid']")
					sleep(1)
					input("xpath", "//input[@id='combobox-input-redeemtypeid']", "付息")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-redeemtypeid']")
					input_enter("xpath", "//input[@id='combobox-input-redeemtypeid']")
					sleep(1)
				
				# 点击下一步
				click("xpath", "//span[text()='下一步']")
				sleep(1)
				
				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='bondredeemsWin-iframe']")
				sleep(1)
				
				if i == 1:
					
					# 标题
					temp1 = time.strftime("%H%M%S")
					input("xpath", "//textarea[@id='title']", "债券全称-本金支付申请" + str(temp1))
					
					# 兑付本金
					click("xpath", "//input[@id='capital-input']")
					sleep(1)
					clear("xpath", "//input[@id='capital-input']")
					sleep(1)
					input("xpath", "//input[@id='capital-input']", "10")
					sleep(1)
					
					# 兑付利息
					click("xpath", "//input[@id='interest-input']")
					sleep(1)
					clear("xpath", "//input[@id='interest-input']")
					sleep(1)
					input("xpath", "//input[@id='interest-input']", "1")
					sleep(1)
				
				else:
					
					# 标题
					temp1 = time.strftime("%H%M%S")
					input("xpath", "//textarea[@id='title']", "债券全称-利息支付申请" + str(temp1))
					# 兑付利息
					click("xpath", "//input[@id='interest-input']")
					sleep(1)
					clear("xpath", "//input[@id='interest-input']")
					sleep(1)
					input("xpath", "//input[@id='interest-input']", "1")
					sleep(1)
				
				# 点击保存按钮
				click("xpath", "//span[text()='保存']")
				
				# 退出所有iframe窗体
				switch_default()
				
				# 用隐式等待方法等页面出现提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				print("债券兑付申请%s新增，保存成功！" % i)
				logging.info("债券兑付申请 %s新增，保存成功" % i)
				time.sleep(3)
				
				# 第一笔，就先修改，再删除新建的‘债券兑付申请’
				if i == 1:
					# 切入‘债券兑付申请’的iframe窗体
					switch_to("xpath", "//iframe[@id='bondredeemsapply-tab-iframe']")
					
					# 点击查看
					# 用JS的方法点击放大镜
					js_click("xpath", "//span[@class='f-contrac-close']")
					sleep(1)
					
					# 债券代码
					input("xpath", "//input[@id='bondissuances']", "Test")
					sleep(1)
					
					# 用JS的方法点击高级查询按钮
					js_click("xpath", "//span[text()='高级查询']")
					click("xpath", "//input[@id='combobox-input-property_0']")
					sleep(1)
					clear("xpath", "//input[@id='combobox-input-property_0']")
					sleep(1)
					# 输入审核状态，通过模糊匹配搜索
					input("xpath", "//input[@id='combobox-input-property_0']", "审核状态")
					sleep(1)
					# 模拟回车
					click("xpath", "//div[contains(text(),'审核状态')]")
					sleep(1)
					
					click("xpath", "//input[@id='combobox-input-value_0']")
					sleep(1)
					# 输入审批状态，通过模糊匹配搜索
					input("xpath", "//input[@id='combobox-input-value_0']", "未审批")
					sleep(1)
					# 模拟回车
					click("xpath", "//div[contains(text(),'未审批')]")
					sleep(1)
					
					click("xpath", "//div[contains(text(),'查询')]")
					
					js_click("xpath", "//span[text()='自定义查询']/preceding-sibling::*[1]")
					
					# 勾选
					click("xpath", "//div[contains(text(),'Test')]/parent::*/preceding-sibling::*[2]/descendant::*[2]")
					
					# 点击修改按钮
					click("xpath", "//span[text()='修改']")
					sleep(1)
					
					# 切入修改的iframe窗体
					switch_to("xpath", "//iframe[@id='modWin-iframe']")
					print("进入窗体")
					sleep(1)
					
					implici_wait("xpath", "//span[contains(text(),'保存')]")
					
					# 备注框中输入新内容
					input("xpath", "//textarea[@id='description']", "自动化测试债券兑付申请修改备注框")
					sleep(1)
					
					# 点击保存按钮
					click("xpath", "//span[text()='保存']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("债券兑付申请，修改成功！")
					logging.info("债券兑付申请，修改成功！")
					time.sleep(3)
					
					# 第一次审核
					# 切入‘债券兑付申请’的iframe窗体
					switch_to("xpath", "//iframe[@id='bondredeemsapply-tab-iframe']")
					
					# 删除 # 勾选
					# 勾选
					click("xpath", "//div[contains(text(),'Test')]/parent::*/preceding-sibling::*[2]/descendant::*[2]")
					
					# 点击送审按钮
					click("xpath", "//span[text()='送审']")
					
					# 点击弹出的OK框
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'送审成功！')]")
					print("债券兑付申请，第一次送审成功！")
					logging.info("债券兑付申请，第一次送审成功！")
					time.sleep(3)
					
					# 切入‘债券兑付申请’的iframe窗体
					switch_to("xpath", "//iframe[@id='bondredeemsapply-tab-iframe']")
					
					# 用JS的方法点击高级查询按钮
					js_click("xpath", "//span[text()='高级查询']")
					click("xpath", "//input[@id='combobox-input-property_0']")
					sleep(1)
					clear("xpath", "//input[@id='combobox-input-property_0']")
					sleep(1)
					# 输入审核状态，通过模糊匹配搜索
					input("xpath", "//input[@id='combobox-input-property_0']", "审核状态")
					sleep(1)
					# 模拟回车
					click("xpath", "//div[contains(text(),'审核状态')]")
					sleep(1)
					
					click("xpath", "//input[@id='combobox-input-value_0']")
					sleep(1)
					# 输入审批状态，通过模糊匹配搜索
					input("xpath", "//input[@id='combobox-input-value_0']", "审批中")
					sleep(1)
					# 模拟回车
					click("xpath", "//div[contains(text(),'审批中')]")
					sleep(1)
					
					click("xpath", "//div[contains(text(),'查询')]")
					
					js_click("xpath", "//span[text()='自定义查询']/preceding-sibling::*[1]")
					
					# 勾选
					click("xpath", "//div[contains(text(),'Test')]/parent::*/preceding-sibling::*[2]/descendant::*[2]")
					
					# 点击撤销送审按钮
					js_click("xpath", "//span[text()='送审']/parent::*/following-sibling::*/child::*")
					sleep(1)
					
					# 点击票据出票按钮
					click("xpath", "//a[contains(text(),'撤销送审')]")
					sleep(1)
					
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现删除的提示框
					implici_wait("xpath", "//span[contains(text(),'撤销送审成功！')]")
					print("债券兑付申请，撤销送审成功！")
					logging.info("债券兑付申请，撤销送审成功！")
					time.sleep(3)
					
					# 切入‘债券兑付申请’的iframe窗体
					switch_to("xpath", "//iframe[@id='bondredeemsapply-tab-iframe']")
					
					# 用JS的方法点击高级查询按钮
					js_click("xpath", "//span[text()='高级查询']")
					click("xpath", "//input[@id='combobox-input-property_0']")
					sleep(1)
					clear("xpath", "//input[@id='combobox-input-property_0']")
					sleep(1)
					# 输入审核状态，通过模糊匹配搜索
					input("xpath", "//input[@id='combobox-input-property_0']", "审核状态")
					sleep(1)
					# 模拟回车
					click("xpath", "//div[contains(text(),'审核状态')]")
					sleep(1)
					
					click("xpath", "//input[@id='combobox-input-value_0']")
					sleep(1)
					# 输入审批状态，通过模糊匹配搜索
					input("xpath", "//input[@id='combobox-input-value_0']", "未审批")
					sleep(1)
					# 模拟回车
					click("xpath", "//div[contains(text(),'未审批')]")
					sleep(1)
					
					click("xpath", "//div[contains(text(),'查询')]")
					
					js_click("xpath", "//span[text()='自定义查询']/preceding-sibling::*[1]")
					
					# 删除 # 勾选
					click("xpath", "//div[contains(text(),'Test')]/parent::*/preceding-sibling::*[2]/descendant::*[2]")
					
					# 点击删除按钮
					click("xpath", "//span[text()='删除']")
					
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现删除的提示框
					implici_wait("xpath", "//span[contains(text(),'债券发行兑付成功删除:1条！')]")
					print("债券兑付，删除成功！")
					logging.info("债券发行兑付，删除成功！")
					time.sleep(3)
				
				# 第二笔，先审核、再取消审核、再托收、再托收到账
				elif i == 2:
					
					# 切入‘债券兑付申请’的iframe窗体
					switch_to("xpath", "//iframe[@id='bondredeemsapply-tab-iframe']")
					
					# 第二次审核
					# 勾选
					click("xpath", "//div[contains(text(),'Test')]/parent::*/preceding-sibling::*[2]/descendant::*[2]")
					
					# 点击送审按钮
					click("xpath", "//span[text()='送审']")
					
					# 点击弹出的OK框
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'送审成功！')]")
					print("债券兑付申请，第一次送审成功！")
					logging.info("债券兑付申请，第一次送审成功！")
					time.sleep(3)
					
					# 第一次审批
					# 切入‘债券兑付申请’的iframe窗体
					switch_to("xpath", "//iframe[@id='bondredeemsapply-tab-iframe']")
					
					# 用JS的方法点击高级查询按钮
					js_click("xpath", "//span[text()='高级查询']")
					click("xpath", "//input[@id='combobox-input-property_0']")
					sleep(1)
					clear("xpath", "//input[@id='combobox-input-property_0']")
					sleep(1)
					# 输入审核状态，通过模糊匹配搜索
					input("xpath", "//input[@id='combobox-input-property_0']", "审核状态")
					sleep(1)
					# 模拟回车
					click("xpath", "//div[contains(text(),'审核状态')]")
					sleep(1)
					
					click("xpath", "//input[@id='combobox-input-value_0']")
					sleep(1)
					# 输入审批状态，通过模糊匹配搜索
					input("xpath", "//input[@id='combobox-input-value_0']", "审批中")
					sleep(1)
					# 模拟回车
					click("xpath", "//div[contains(text(),'审批中')]")
					sleep(1)
					
					click("xpath", "//div[contains(text(),'查询')]")
					
					js_click("xpath", "//span[text()='自定义查询']/preceding-sibling::*[1]")
					
					# 点击审核按钮
					double_click("xpath",
					             "//div[contains(text(),'Test')]/parent::*/preceding-sibling::*[2]/descendant::*[2]")
					sleep(1)
					
					switch_to("xpath", "//iframe[@id='wf_taskProcessing_win-iframe']")
					sleep(1)
					
					click("xpath", "//span[text()='同意']")
					sleep(1)
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("债券兑付，第一次审批成功！")
					logging.info("债券兑付，第一次审批成功！")
					time.sleep(3)
					
					# 第二次审批
					# 切入‘债券兑付申请’的iframe窗体
					switch_to("xpath", "//iframe[@id='bondredeemsapply-tab-iframe']")
					
					# 点击审核按钮
					double_click("xpath",
					             "//div[contains(text(),'Test')]/parent::*/preceding-sibling::*[2]/descendant::*[2]")
					sleep(1)
					
					switch_to("xpath", "//iframe[@id='wf_taskProcessing_win-iframe']")
					sleep(1)
					
					click("xpath", "//span[text()='同意']")
					sleep(1)
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("债券兑付，第二次审批成功！")
					logging.info("债券兑付，第二次审批成功！")
					time.sleep(3)
					
					# 债券兑付变更
					# 切入‘债券兑付申请’的iframe窗体
					switch_to("xpath", "//iframe[@id='bondredeemsapply-tab-iframe']")
					
					# 用JS的方法点击高级查询按钮
					js_click("xpath", "//span[text()='高级查询']")
					click("xpath", "//input[@id='combobox-input-property_0']")
					sleep(1)
					clear("xpath", "//input[@id='combobox-input-property_0']")
					sleep(1)
					# 输入审核状态，通过模糊匹配搜索
					input("xpath", "//input[@id='combobox-input-property_0']", "审核状态")
					sleep(1)
					# 模拟回车
					click("xpath", "//div[contains(text(),'审核状态')]")
					sleep(1)
					
					click("xpath", "//input[@id='combobox-input-value_0']")
					sleep(1)
					# 输入审批状态，通过模糊匹配搜索
					input("xpath", "//input[@id='combobox-input-value_0']", "已审批")
					sleep(1)
					# 模拟回车
					click("xpath", "//div[contains(text(),'已审批')]")
					sleep(1)
					
					click("xpath", "//div[contains(text(),'查询')]")
					
					js_click("xpath", "//span[text()='自定义查询']/preceding-sibling::*[1]")
					
					# 删除 # 勾选
					click("xpath", "//div[contains(text(),'Test')]/parent::*/preceding-sibling::*[2]/descendant::*[2]")
					
					# 用JS方便点击‘送审’按钮旁边的倒三角形
					click("xpath", "//span[text()='变更']")
					sleep(1)
					
					switch_to("xpath", "//iframe[@id='modWin-iframe']")
					
					# 备注框中输入新内容
					input("xpath", "//textarea[@id='description']", "自动化测试债券兑付变更备注框")
					sleep(1)
					
					# 点击保存按钮
					click("xpath", "//span[text()='保存']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("债券兑付，变更成功！")
					logging.info("债券兑付，变更成功！")
					time.sleep(3)
					
					# 切入‘债券兑付申请’的iframe窗体
					switch_to("xpath", "//iframe[@id='bondredeemsapply-tab-iframe']")
					
					# 用JS的方法点击高级查询按钮
					js_click("xpath", "//span[text()='高级查询']")
					click("xpath", "//input[@id='combobox-input-property_0']")
					sleep(1)
					clear("xpath", "//input[@id='combobox-input-property_0']")
					sleep(1)
					# 输入审核状态，通过模糊匹配搜索
					input("xpath", "//input[@id='combobox-input-property_0']", "审核状态")
					sleep(1)
					# 模拟回车
					click("xpath", "//div[contains(text(),'审核状态')]")
					sleep(1)
					
					click("xpath", "//input[@id='combobox-input-value_0']")
					sleep(1)
					# 输入审批状态，通过模糊匹配搜索
					input("xpath", "//input[@id='combobox-input-value_0']", "已审批")
					sleep(1)
					# 模拟回车
					click("xpath", "//div[contains(text(),'已审批')]")
					sleep(1)
					
					click("xpath", "//div[contains(text(),'查询')]")
					
					js_click("xpath", "//span[text()='自定义查询']/preceding-sibling::*[1]")
					
					# 勾选
					click("xpath", "//div[contains(text(),'Test')]/parent::*/preceding-sibling::*[2]/descendant::*[2]")
					
					# 点击作废按钮
					click("xpath", "//span[text()='作废']")
					
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'作废成功！')]")
					print("债券兑付，作废成功！")
					logging.info("债券兑付，作废成功！")
					time.sleep(3)
				
				# 第三笔，作废
				elif i == 3:
					
					# 切入‘债券兑付申请’的iframe窗体
					switch_to("xpath", "//iframe[@id='bondredeemsapply-tab-iframe']")
					
					# 用JS的方法点击高级查询按钮
					js_click("xpath", "//span[text()='高级查询']")
					click("xpath", "//input[@id='combobox-input-property_0']")
					sleep(1)
					clear("xpath", "//input[@id='combobox-input-property_0']")
					sleep(1)
					# 输入审核状态，通过模糊匹配搜索
					input("xpath", "//input[@id='combobox-input-property_0']", "审核状态")
					sleep(1)
					# 模拟回车
					click("xpath", "//div[contains(text(),'审核状态')]")
					sleep(1)
					
					click("xpath", "//input[@id='combobox-input-value_0']")
					sleep(1)
					# 输入审批状态，通过模糊匹配搜索
					input("xpath", "//input[@id='combobox-input-value_0']", "未审批")
					sleep(1)
					# 模拟回车
					click("xpath", "//div[contains(text(),'未审批')]")
					sleep(1)
					
					click("xpath", "//div[contains(text(),'查询')]")
					
					js_click("xpath", "//span[text()='自定义查询']/preceding-sibling::*[1]")
					
					# 第二次审核
					# 勾选
					click("xpath", "//div[contains(text(),'Test')]/parent::*/preceding-sibling::*[2]/descendant::*[2]")
					
					# 点击送审按钮
					click("xpath", "//span[text()='送审']")
					
					# 点击弹出的OK框
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'送审成功！')]")
					print("债券兑付申请，第一次送审成功！")
					logging.info("债券兑付申请，第一次送审成功！")
					time.sleep(3)
					
					# 第一次审批
					# 切入‘债券兑付申请’的iframe窗体
					switch_to("xpath", "//iframe[@id='bondredeemsapply-tab-iframe']")
					
					# 用JS的方法点击高级查询按钮
					js_click("xpath", "//span[text()='高级查询']")
					click("xpath", "//input[@id='combobox-input-property_0']")
					sleep(1)
					clear("xpath", "//input[@id='combobox-input-property_0']")
					sleep(1)
					# 输入审核状态，通过模糊匹配搜索
					input("xpath", "//input[@id='combobox-input-property_0']", "审核状态")
					sleep(1)
					# 模拟回车
					click("xpath", "//div[contains(text(),'审核状态')]")
					sleep(1)
					
					click("xpath", "//input[@id='combobox-input-value_0']")
					sleep(1)
					# 输入审批状态，通过模糊匹配搜索
					input("xpath", "//input[@id='combobox-input-value_0']", "审批中")
					sleep(1)
					# 模拟回车
					click("xpath", "//div[contains(text(),'审批中')]")
					sleep(1)
					
					click("xpath", "//div[contains(text(),'查询')]")
					
					js_click("xpath", "//span[text()='自定义查询']/preceding-sibling::*[1]")
					
					# 点击审核按钮
					double_click("xpath",
					             "//div[contains(text(),'Test')]/parent::*/preceding-sibling::*[2]/descendant::*[2]")
					sleep(1)
					
					switch_to("xpath", "//iframe[@id='wf_taskProcessing_win-iframe']")
					sleep(1)
					
					click("xpath", "//span[text()='同意']")
					sleep(1)
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("债券兑付，第一次审批成功！")
					logging.info("债券兑付，第一次审批成功！")
					time.sleep(3)
					
					# 第二次审批
					# 切入‘债券兑付申请’的iframe窗体
					switch_to("xpath", "//iframe[@id='bondredeemsapply-tab-iframe']")
					
					# 点击审核按钮
					double_click("xpath",
					             "//div[contains(text(),'Test')]/parent::*/preceding-sibling::*[2]/descendant::*[2]")
					sleep(1)
					
					switch_to("xpath", "//iframe[@id='wf_taskProcessing_win-iframe']")
					sleep(1)
					
					click("xpath", "//span[text()='同意']")
					sleep(1)
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("债券兑付，第二次审批成功！")
					logging.info("债券兑付，第二次审批成功！")
					time.sleep(3)
					
					# 切入‘债券兑付申请’的iframe窗体
					switch_to("xpath", "//iframe[@id='bondredeemsapply-tab-iframe']")
					
					# 用JS的方法点击高级查询按钮
					js_click("xpath", "//span[text()='高级查询']")
					click("xpath", "//input[@id='combobox-input-property_0']")
					sleep(1)
					clear("xpath", "//input[@id='combobox-input-property_0']")
					sleep(1)
					# 输入审核状态，通过模糊匹配搜索
					input("xpath", "//input[@id='combobox-input-property_0']", "审核状态")
					sleep(1)
					# 模拟回车
					click("xpath", "//div[contains(text(),'审核状态')]")
					sleep(1)
					
					click("xpath", "//input[@id='combobox-input-value_0']")
					sleep(1)
					# 输入审批状态，通过模糊匹配搜索
					input("xpath", "//input[@id='combobox-input-value_0']", "已审批")
					sleep(1)
					# 模拟回车
					click("xpath", "//div[contains(text(),'已审批')]")
					sleep(1)
					
					click("xpath", "//div[contains(text(),'查询')]")
					
					js_click("xpath", "//span[text()='自定义查询']/preceding-sibling::*[1]")
					
					# 勾选
					click("xpath", "//div[contains(text(),'Test')]/parent::*/preceding-sibling::*[2]/descendant::*[2]")
					
					# 点击生成交易单按钮
					click("xpath", "//span[text()='生成交易单']")
					
					# 进入生成交易单页面
					switch_to("xpath", "//iframe[@id='genRecWin-iframe']")
					sleep(1)
					
					# 选择付款单
					click("xpath", "//a[text()='未生成']/ancestor::*[2]/preceding-sibling::*[1]/descendant::*[2]")
					
					# 选择下一步
					click("xpath", "//span[text()='下一步']")
					
					switch_parent()
					
					switch_to("xpath", "//iframe[@id='addRecWin-iframe']")
					sleep(1)
					
					# 组织机构代码
					temp1 = time.strftime("%H%M%S")
					input("xpath", "//input[@id='ourregorgcode']", "Test" + str(temp1))
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
					sleep(1)
					# clear("xpath", "//input[@id='combobox-input-settlementmodeid']")
					input_down("xpath", "//input[@id='combobox-input-settlementmodeid']")
					sleep(1)
					input_enter("xpath", "//input[@id='combobox-input-settlementmodeid']")
					sleep(1)
					
					# 汇款人币种
					click("xpath", "//input[@id='combobox-input-ourcurrencyid']")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-ourcurrencyid']")
					sleep(1)
					input_enter("xpath", "//input[@id='combobox-input-ourcurrencyid']")
					time.sleep(1)
					
					# 购汇账户
					click("xpath", "//input[@id='combobox-input-purchasebankaccountid']")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-purchasebankaccountid']")
					sleep(1)
					input_enter("xpath", "//input[@id='combobox-input-purchasebankaccountid']")
					sleep(1)
					
					# 收方名称
					click("xpath", "//input[@id='combobox-input-oppcounterpartyid']")
					sleep(1)
					input("xpath", "//input[@id='combobox-input-oppcounterpartyid']", "Mindy")
					click("xpath", "//div[contains(text(),'Mindy自动化测试')]")
					sleep(1)
					
					# 收方账户
					input("xpath", "//input[@id='combobox-input-oppcounterpartyaccountid']", "1221221")
					sleep(1)
					
					# 收方开户银行
					click("xpath", "//input[@id='combobox-input-oppbanklocationid']")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-oppbanklocationid']")
					sleep(1)
					input_enter("xpath", "//input[@id='combobox-input-oppbanklocationid']")
					time.sleep(1)
					
					# 收方收方SWIFT代码
					input("xpath", "//input[@id='oppbranchswiftcode']", "1220")
					sleep(1)
					
					# 收方SWIFT名称
					input("xpath", "//input[@id='oppbranchswiftname']", "1330")
					sleep(1)
					
					# 点击保存
					click("xpath", "//span[text()='保存']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("债券兑付，生成交易单成功！")
					logging.info("债券兑付，生成交易单成功！")
					sleep(3)
			
			# 退出所有iframe窗体
			switch_default()
			
			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='债券兑付申请']/child::*[1]")
			
			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//span[contains(text(),'债券发行管理')]")
			
			# 打印操作成功日志
			print("债券兑付申请，操作成功!")
			logging.info("债券兑付申请，操作成功!")
			time.sleep(2)
		except Exception as err:
			
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			
			logging.debug("债券兑付申请,失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		
		# 测试注册登记查看
		try:
			# 点击保函管理菜单
			click("xpath", "//span[@title='注册登记查看']")
			
			# 退出所有的iframe窗体
			switch_default()
			logging.info("开始测试注册登记查看功能")
			
			# 切入‘注册登记查看’的iframe窗体
			switch_to("xpath", "//iframe[@id='bondregisterview-tab-iframe']")
			
			# 点击查看
			# 用JS的方法点击放大镜
			js_click("xpath", "//span[@class='f-contrac-close']")
			sleep(1)
			
			# 输入注册编码
			click("xpath", "//input[@id='code']")
			input("xpath", "//input[@id='code']", "ZCBM")
			
			# 点击查询
			click("xpath", "//span[text()='查询']")
			
			# 用隐式等待方法等页面出现预期数据：法律顾问:TestLeg-自动化测试法律顾问
			implici_wait("xpath", "//div[@title='法律顾问:TestLeg-自动化测试法律顾问']")
			print("注册登记查看成功！")
			time.sleep(3)
			
			# 退出所有iframe窗体
			switch_default()
			
			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='注册登记查看']/child::*[1]")
			
			# # 再次点击基础设置菜单，使之关闭
			# click("xpath", "//span[contains(text(),'债券发行管理')]")
			
			# 打印操作成功日志
			print("注册登记查看，操作成功!")
			logging.info("注册登记查看，操作成功!")
			time.sleep(2)
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("注册登记查看,失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		
		# 测试发行登记查看
		try:
			# 点击保函管理菜单
			click("xpath", "//span[@title='发行登记查看']")
			
			# 退出所有的iframe窗体
			switch_default()
			logging.info("开始测试发行登记查看功能")
			
			# 切入‘注册登记查看’的iframe窗体
			switch_to("xpath", "//iframe[@id='bondissuanceview-tab-iframe']")
			
			# 点击查看
			# 用JS的方法点击放大镜
			js_click("xpath", "//span[@class='f-contrac-close']")
			sleep(1)
			
			# 选择监管机构
			click("xpath", "//input[@id='combobox-input-registerorg']")
			click("xpath", "//div[@title='代码-名称:TestReg-自动化测试监管机构']")
			sleep(1)
			
			# 点击查询
			click("xpath", "//span[text()='查询']")
			
			# 用隐式等待方法等页面出现预期数据：注册品种:TestZc-自动化测试注册品种
			implici_wait("xpath", "//div[@title='注册品种:TestZc-自动化测试注册品种']")
			print("发行登记查看成功！")
			time.sleep(3)
			
			# 退出所有iframe窗体
			switch_default()
			
			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='发行登记查看']/child::*[1]")
			
			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//span[contains(text(),'债券发行管理')]")
			
			# 打印操作成功日志
			print("发行登记查看，操作成功!")
			logging.info("发行登记查看，操作成功!")
			time.sleep(2)
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("发行登记查看,失败！" + str(traceback.format_exc()))
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