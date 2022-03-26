# encoding=utf-8
# @Time : 2020/8/14 14:49
# @Author : Mindy
# 此文件是测试内部借款管理，包含基础设置，借出方管理以及借入方管理
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


class Test_NbJk(unittest.TestCase):
	
	# 启动浏览器
	def setUp(self):
		
		# 启动浏览器的另外一个方法：通过封装启动浏览器的驱动，启动不同浏览器
		self.driver = get("chrome")
	
	# 登陆系统、对系统设置进行操作
	def test_trade(self):
		
		# 通过登陆封装函数，进行登陆
		# login( G_Ora_Url,TestUser,Password, "自动化测试租户")
		# login( G_Ora_Url,Tao, Password,"默认租户")
		login(G_Ora_Url, mindy, Password, "默认租户")
		# login(G_Ora_Url, mindy, Password, "Mindy")
		# login( G_Mys_Url,TestUser,Password, "自动化测试租户")
		# login(G_Mys_Url, Tao, Password, "默认租户")
		# login(G_Mys_Url, mindy, Password, "亚唐科技")
		# login(G_Mys_Url, judy, Password, "默认租户")
		
		logging.info("开始测试内部借款管理的页面功能")
		# 将页面的滚动条滑动到‘资金结算管理’页面的地方
		js_gd("xpath", "//span[contains(text(),'内部借款管理')]")
		# 用JS的方法点击资金结算管理菜单按钮
		js_click("xpath", "//span[contains(text(),'内部借款管理')]")
		"""
		# 测试基础设置--往来决议
		try:
			# 点击基础设置菜单
			click("xpath", "//li[@f_value='ifloansetting']/descendant-or-self::*[5]")
			# 点击往来决议菜单
			js_gd("xpath", "//span[contains(text(),'往来决议')]")
			click("xpath", "//span[contains(text(),'往来决议')]")

			# 退出所有iframe窗体
			switch_default()

			for i in range(1, 3):
				# 切入往来决议的iframe窗体
				switch_to("xpath", "//iframe[@id='contactDecision-tab-iframe']")
				logging.info("开始测试往来决议功能")

				# 用JS的方法点击新增按钮
				js_click("xpath", "//span[text()='新增']")

				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='addWin-iframe']")
				sleep(1)

				# 授信对象
				click("xpath", "//input[@id='combobox-input-opporgid']")
				sleep(1)
				input("xpath", "//input[@id='combobox-input-opporgid']", "Mindy科技有限公司")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-opporgid']")
				input_enter("xpath", "//input[@id='combobox-input-opporgid']")
				sleep(1)

				# 决议编号+ str(temp1)
				# temp1 = time.strftime("%H%M%S")
				# 输入决议编号
				input("xpath", "//input[@id='contractcode']", "ZDHJYBH001")
				sleep(1)

				# 输入授信额度
				input("xpath", "//input[@id='amount-input']", "3000")
				sleep(1)

				# 授信开始日期
				today = date.today()
				due_date = today - timedelta(days=20)
				click("xpath", "//input[@id='begindate-input']")
				sleep(1)
				clear("xpath", "//input[@id='begindate-input']")
				sleep(1)
				input("xpath", "//input[@id='begindate-input']", str(due_date))
				# 模拟回车键
				# keyDown('enter')
				# keyUp('enter')
				time.sleep(1)

				# 授信截止日期
				today = date.today()
				due_date = today + timedelta(days=60)
				click("xpath", "//input[@id='enddate-input']")
				sleep(1)
				clear("xpath", "//input[@id='enddate-input']")
				sleep(1)
				input("xpath", "//input[@id='enddate-input']", str(due_date))
				# 模拟回车键
				keyDown('enter')
				keyUp('enter')
				time.sleep(1)

				# 描述框中填入值
				input("xpath", "//textarea[@id='description']", "自动化测试往来决议备注框")
				sleep(1)

				# 缺少附件上传

				# 点击保存按钮
				click("xpath", "//span[text()='保存']")

				# 退出所有iframe窗体
				switch_default()

				# 用隐式等待方法等页面出现新增成功的提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				print("往来决议，保存成功！")
				time.sleep(3)

				if i == 1:
					# 切入往来决议的iframe窗体
					switch_to("xpath", "//iframe[@id='contactDecision-tab-iframe']")
					sleep(1)

					# 点击查看
					# 用JS的方法点击放大镜
					js_click("xpath", "//span[@class='f-contrac-close']")
					sleep(1)

					# 输入决议编号
					input("xpath", "//input[@id='contractcode']", "ZDHJYBH001")
					sleep(1)

					# 点击查询
					click("xpath", "//span[text()='查询']")
					sleep(1)

					# 勾选
					click("xpath", "//div[@title='决议编号:ZDHJYBH001']/parent::*/preceding-sibling::*[3]/descendant::*[2]")
					sleep(1)

					click("xpath", "//span[text()='删除']")
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现删除的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("往来决议，删除成功！")
					time.sleep(3)

			# 修改功能
			# 切入‘往来决议’的iframe窗体
			switch_to("xpath", "//iframe[@id='contactDecision-tab-iframe']")
			sleep(1)

			# 勾选
			click("xpath", "//div[@title='决议编号:ZDHJYBH001']/parent::*/preceding-sibling::*[3]/descendant::*[2]")
			sleep(1)

			# 点击修改按钮
			click("xpath", "//span[text()='修改']")
			sleep(1)

			# 切入新增的iframe窗体
			switch_to("xpath", "//iframe[@id='modWin-iframe']")
			sleep(1)

			# 描述框中填入值
			input("xpath", "//textarea[@id='description']", "自动化测试往来决议描述框修改")
			sleep(1)

			# 点击保存按钮
			click("xpath", "//span[text()='保存']")

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功')]")
			print("往来决议，修改成功！")
			time.sleep(3)

			# 切入往来决议的iframe窗体
			switch_to("xpath", "//iframe[@id='contactDecision-tab-iframe']")
			sleep(1)

			# 勾选
			click("xpath", "//div[@title='决议编号:ZDHJYBH001']/parent::*/preceding-sibling::*[3]/descendant::*[2]")
			sleep(1)

			# 点击审核按钮
			click("xpath", "//span[text()='审核']")
			# 点击弹出框的OK键
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'成功条数:1')]")
			print("往来决议，第一次送审成功！")
			logging.info("往来决议，第一次送审成功！")
			time.sleep(3)

			# 取消送审
			# 切入‘往来决议’的iframe窗体
			# 切入往来决议的iframe窗体
			switch_to("xpath", "//iframe[@id='contactDecision-tab-iframe']")
			sleep(1)

			# 勾选
			click("xpath", "//div[@title='决议编号:ZDHJYBH001']/parent::*/preceding-sibling::*[3]/descendant::*[2]")
			sleep(1)

			# 用JS方便点击‘审核’按钮旁边的倒三角形
			js_click("xpath", "//span[text()='审核']/parent::*/following-sibling::*/child::*")
			sleep(1)

			# 点击取消送审按钮
			js_click("xpath", "//a[contains(text(),'取消审核')]")
			sleep(1)

			# 点击弹出框的OK键
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'取消审核成功1笔:')]")
			print("往来决议，取消审核成功！")
			logging.info("往来决议，取消审核成功！")
			time.sleep(3)

			# 切入往来决议的iframe窗体
			switch_to("xpath", "//iframe[@id='contactDecision-tab-iframe']")
			sleep(1)

			# 勾选
			click("xpath", "//div[@title='决议编号:ZDHJYBH001']/parent::*/preceding-sibling::*[3]/descendant::*[2]")
			sleep(1)

			# 点击审核按钮
			click("xpath", "//span[text()='审核']")
			# 点击弹出框的OK键
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'成功条数:1')]")
			print("往来决议，第二次送审成功！")
			logging.info("往来决议，第二次送审成功！")
			time.sleep(3)

			switch_to("xpath", "//iframe[@id='contactDecision-tab-iframe']")
			sleep(1)

			# 勾选
			click("xpath", "//div[@title='决议编号:ZDHJYBH001']/parent::*/preceding-sibling::*[3]/descendant::*[2]")
			sleep(1)

			# 点击修改按钮
			click("xpath", "//span[text()='变更']")
			sleep(1)

			# 切入新增的iframe窗体
			switch_to("xpath", "//iframe[@id='modWin-iframe']")
			sleep(1)

			# 描述框中填入值
			input("xpath", "//textarea[@id='description']", "自动化测试往来决议描述框变更")
			sleep(1)

			# 点击保存按钮
			click("xpath", "//span[text()='保存']")

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功')]")
			print("往来决议，变更成功！")
			time.sleep(3)

			switch_to("xpath", "//iframe[@id='contactDecision-tab-iframe']")
			sleep(1)

			# 勾选
			click("xpath", "//div[@title='决议编号:ZDHJYBH001']/parent::*/preceding-sibling::*[3]/descendant::*[2]")
			sleep(1)

			# 点击生按钮
			click("xpath", "//span[text()='作废']")
			sleep(1)

			# 点击弹出框的OK键
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'作废成功:1条')]")
			print("往来协议，成功作废1条!！")
			time.sleep(3)

			switch_default()

			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='往来决议']/child::*[1]")

			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//li[@f_value='ifloansetting']/descendant-or-self::*[5]")

			# 打印操作成功日志
			print("往来决议，操作成功!")
			logging.info("往来决议，操作成功!")
			time.sleep(2)

		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("往来决议操作失败！" + str(traceback.format_exc()))
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
			input("xpath", "//input[@name='code']", "L09")
			sleep(1)
			
			# 输入名称
			input("xpath", "//input[@id='name']", "借出往来合同")
			sleep(1)
			# 单据对象
			click("xpath", "//input[@id='combobox-input-noteobjectid']")
			sleep(1)
			input("xpath", "//input[@id='combobox-input-noteobjectid']", "借出往来合同")
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
			input("xpath", "//input[@name='code']", "L10")
			sleep(1)
			
			# 输入名称
			input("xpath", "//input[@id='name']", "借入往来合同")
			sleep(1)
			# 单据对象
			click("xpath", "//input[@id='combobox-input-noteobjectid']")
			sleep(1)
			input("xpath", "//input[@id='combobox-input-noteobjectid']", "借入往来合同")
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
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		"""
		# 借款类型
		# 测试内部借款管理--借出方管理
		try:
			# 点击理财投资菜单
			click("xpath", "//span[@title='借出方管理']")
			# 点击理财合同登记菜单
			click("xpath", "//span[@title='借出合同登记']")
			# 退出所有的iframe窗体
			switch_default()

			logging.info("开始测试借出合同登记功能")
			for i in range(1, 4):
				# 切入‘理财合同’的iframe窗体
				switch_to("xpath", "//iframe[@id='lendingcontract-tab-iframe']")

				# 用JS的方法点击新增按钮
				js_click("xpath", "//span[text()='新增']")

				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='addWin-iframe']")
				sleep(1)

				# 借入组织
				click("xpath", "//input[@id='combobox-input-opporgid']")
				sleep(1)
				input("xpath", "//input[@id='combobox-input-opporgid']", "Mindy科技有限公司")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-opporgid']")
				input_enter("xpath", "//input[@id='combobox-input-opporgid']")
				sleep(1)

				# 借款类型
				click("xpath", "//input[@id='combobox-input-loantype']")
				sleep(1)
				input("xpath", "//input[@id='combobox-input-loantype']", "一般借款")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-loantype']")
				input_enter("xpath", "//input[@id='combobox-input-loantype']")
				sleep(1)

				# 借款方式
				click("xpath", "//input[@id='combobox-input-loanmode']")
				sleep(1)
				input("xpath", "//input[@id='combobox-input-loanmode']", "现金")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-loanmode']")
				input_enter("xpath", "//input[@id='combobox-input-loanmode']")
				sleep(1)

				# 工程项目
				click("xpath", "//input[@id='combobox-input-projectitemid']")
				sleep(1)
				input("xpath", "//input[@id='combobox-input-projectitemid']", "自动化测试工程项目")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-projectitemid']")
				input_enter("xpath", "//input[@id='combobox-input-projectitemid']")
				sleep(1)

				# 合同编号
				temp1 = time.strftime("%H%M%S")
				# 合同编号
				input("xpath", "//input[@id='contractcode']", "ZDHLCHTH" + str(temp1))
				sleep(1)

				# 合同签订日
				today = date.today()
				sign_date = today - timedelta(days=20)
				click("xpath", "//input[@id='signeddate-input']")
				sleep(1)
				clear("xpath", "//input[@id='signeddate-input']")
				sleep(1)
				input("xpath", "//input[@id='signeddate-input']", str(sign_date))
				# 模拟回车键
				# keyDown('enter')
				# keyUp('enter')
				time.sleep(1)

				# 合同起始日
				today = date.today()
				sign_date = today - timedelta(days=20)
				click("xpath", "//input[@id='begindate-input']")
				sleep(1)
				clear("xpath", "//input[@id='begindate-input']")
				sleep(1)
				input("xpath", "//input[@id='begindate-input']", str(sign_date))
				# 模拟回车键
				# keyDown('enter')
				# keyUp('enter')
				time.sleep(1)

				# 合同到期日
				today = date.today()
				end_date = today + timedelta(days=20)
				click("xpath", "//input[@id='enddate-input']")
				sleep(1)
				clear("xpath", "//input[@id='enddate-input']")
				sleep(1)
				input("xpath", "//input[@id='enddate-input']", str(end_date))
				# 模拟回车键
				# keyDown('enter')
				# keyUp('enter')
				time.sleep(1)

				# 合同期限日
				input("xpath", "//input[@id='loantermday-input']", "40")
				sleep(1)

				# 币种
				click("xpath", "//input[@id='combobox-input-currencyid']")
				sleep(1)
				input("xpath", "//input[@id='combobox-input-currencyid']", "人民币")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-currencyid']")
				input_enter("xpath", "//input[@id='combobox-input-currencyid']")
				sleep(1)

				# 金额
				click("xpath", "//input[@id='amount-input']")
				sleep(1)
				# 清空内容
				clear("xpath", "//input[@id='amount-input']")
				sleep(1)
				# 输入金额
				input("xpath", "//input[@id='amount-input']", "100000")
				sleep(1)

				# 借款经办人
				input("xpath", "//input[@id='loanoperator']", "田遍地")
				sleep(1)

				# 费率
				click("xpath", "//input[@id='feerate-input']")
				sleep(1)
				# 清空内容
				clear("xpath", "//input[@id='feerate-input']")
				sleep(1)
				# 输入金额
				input("xpath", "//input[@id='feerate-input']", "30")
				sleep(1)

				# 计息开始日期
				today = date.today()
				start_date = today + timedelta(days=20)
				click("xpath", "//input[@id='intereststartdate-input']")
				sleep(1)
				clear("xpath", "//input[@id='intereststartdate-input']")
				sleep(1)
				input("xpath", "//input[@id='intereststartdate-input']", str(start_date))
				time.sleep(1)

				# 点击输入用途
				click("xpath", "//textarea[@id='abstracts']")
				sleep(1)
				input("xpath", "//textarea[@id='abstracts']", "自动化测试借出合同输入用途")
				sleep(1)

				# 计息方式中输入值
				# 点击计息方式插页
				# 1、选择还本方式
				click("xpath", "//input[@id='combobox-input-repaymode']")
				# 按键往下，选择‘按季还款’
				input_down("xpath", "//input[@id='combobox-input-repaymode']")
				input_enter("xpath", "//input[@id='combobox-input-repaymode']")
				time.sleep(1)

				# 2、选择计息方式
				click("xpath", "//input[@id='combobox-input-interestmode']")
				# 按键往下，选择利率方案
				sleep(2)
				input_down("xpath", "//input[@id='combobox-input-interestmode']")
				input_enter("xpath", "//input[@id='combobox-input-interestmode']")
				sleep(1)

				# 3、选择利率方案
				click("xpath", "//input[@id='combobox-input-interestrateschemeid']")
				# 按键往下，选择利率方案
				sleep(2)
				input_down("xpath", "//input[@id='combobox-input-interestrateschemeid']")
				input_enter("xpath", "//input[@id='combobox-input-interestrateschemeid']")
				sleep(1)

				# 4、选择浮动方式
				click("xpath", "//input[@id='combobox-input-interestratefloattype']")
				# 按键往下，选择利率方案
				sleep(2)
				input_down("xpath", "//input[@id='combobox-input-interestratefloattype']")
				input_enter("xpath", "//input[@id='combobox-input-interestratefloattype']")
				sleep(1)

				# # 点击拓展信息
				# click("xpath", "//span[text()='扩展信息']")
				# sleep(1)
				#
				# # 点击日期按钮
				# today = date.today()
				# end_date = today
				# click("xpath", "//input[@id='extend3-input']")
				# sleep(1)
				# clear("xpath", "//input[@id='extend3-input']")
				# sleep(1)
				# input("xpath", "//input[@id='extend3-input']", str(end_date))
				# # 模拟回车键
				# # keyDown('enter')
				# # keyUp('enter')
				# time.sleep(1)

				# 点击保存按钮
				click("xpath", "//span[text()='保存']")

				# 退出所有iframe窗体
				switch_default()

				# 用隐式等待方法等页面出现提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				print("借出合同第%s次新增成功" % i)
				logging.info("借出合同第%s次新增成功" % i)
				time.sleep(3)

				# 第一笔，就先修改，再删除新建的‘借出合同’
				if i == 1:
					# 切入‘借出合同’的iframe窗体
					switch_to("xpath", "//iframe[@id='lendingcontract-tab-iframe']")

					# 点击查看
					# 用JS的方法点击放大镜
					js_click("xpath", "//span[@class='f-contrac-close']")
					sleep(1)

					# 合同号查询
					input("xpath", "//input[@id='contractcode']", "ZDHLCHTH")
					sleep(1)

					# 点击查询
					click("xpath", "//span[text()='查询']")

					# 修改 # 勾选
					click("xpath", "//div[@title='借入单位:002001-Mindy科技有限公司']/parent::*/preceding-sibling::*[3]/descendant::*[2]")

					# 点击修改按钮
					click("xpath", "//span[text()='修改']")
					sleep(1)

					# 切入修改的iframe窗体
					switch_to("xpath", "//iframe[@id='modWin-iframe']")
					print("进入修改窗体")
					sleep(1)

					# 描述abstracts
					input("xpath", "//textarea[@id='abstracts']", "自动化测试借出合同备注框")
					sleep(1)

					# 备注框中输入新内容
					input("xpath", "//textarea[@id='description']", "自动化测试借出合同修改备注框")
					sleep(1)

					# 点击保存按钮
					click("xpath", "//span[text()='保存']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("借出合同，修改成功！")
					logging.info("借出合同，修改成功！")
					time.sleep(3)

					# 第一次审核
					# 切入‘借出合同登记’的iframe窗体
					switch_to("xpath", "//iframe[@id='lendingcontract-tab-iframe']")

					# 勾选
					click("xpath", "//div[@title='借入单位:002001-Mindy科技有限公司']/parent::*/preceding-sibling::*[3]/descendant::*[2]")

					# 点击审核按钮
					click("xpath", "//span[text()='审核']")

					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'成功审核1条记录')]")
					print("借出合同登记，第一次审批成功！")
					logging.info("借出合同登记，第一次审批成功！")
					time.sleep(3)

					# 切入‘借出合同登记’的iframe窗体
					switch_to("xpath", "//iframe[@id='lendingcontract-tab-iframe']")

					# 勾选
					click("xpath", "//div[@title='借入单位:002001-Mindy科技有限公司']/parent::*/preceding-sibling::*[3]/descendant::*[2]")

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
					implici_wait("xpath", "//span[contains(text(),'成功取消审核:1条')]")
					print("借出合同登记，取消审核成功！")
					logging.info("借出合同登记，取消审核成功！")
					time.sleep(3)

					# 切入‘借出合同登记’的iframe窗体
					switch_to("xpath", "//iframe[@id='lendingcontract-tab-iframe']")

					# 勾选
					click("xpath", "//div[@title='借入单位:002001-Mindy科技有限公司']/parent::*/preceding-sibling::*[3]/descendant::*[2]")

					# 点击删除按钮
					click("xpath", "//span[text()='删除']")

					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现删除的提示框
					implici_wait("xpath", "//span[contains(text(),'成功删除1条记录！')]")
					print("借出合同登记，删除成功！")
					logging.info("借出合同登记，删除成功！")
					time.sleep(3)

				# 第二笔，先审核、再继承、再放款、再回款、再利息登记
				elif i == 2:

					# 第二次审核
					# 切入‘借出合同登记’的iframe窗体
					switch_to("xpath", "//iframe[@id='lendingcontract-tab-iframe']")

					# 勾选
					click("xpath", "//div[@title='借入单位:002001-Mindy科技有限公司']/parent::*/preceding-sibling::*[3]/descendant::*[2]")

					# 点击审核按钮
					click("xpath", "//span[text()='审核']")

					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'成功审核1条记录')]")
					print("借出合同登记，第二次审批成功！")
					logging.info("借出合同登记，第二次审批成功！")
					time.sleep(3)

					# 借出合同放款申请
					# 切入‘借出合同登记’的iframe窗体
					switch_to("xpath", "//iframe[@id='lendingcontract-tab-iframe']")

					# 勾选
					click("xpath", "//div[@title='借入单位:002001-Mindy科技有限公司']/parent::*/preceding-sibling::*[3]/descendant::*[2]")

					# 点击取消审核按钮
					click("xpath", "//span[text()='放款']")
					sleep(1)

					switch_to("xpath", "//iframe[@id='lendPayWin-iframe']")

					# 输入放款日期
					# 点击放款日期的日历按钮
					js_click("xpath", "//span[@id='lenddate-trigger']")
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

					# 切入‘借出登记登记’的iframe窗体
					switch_to("xpath", "//iframe[@id='lendingcontract-tab-iframe']")
					# 切入新增的iframe窗体
					switch_to("xpath", "//iframe[@id='lendPayWin-iframe']")

					# 放款金额
					input("xpath", "//input[@id='amount-input']", "3000")
					sleep(1)

					# 点击保存按钮
					click("xpath", "//span[text()='保存']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("借出合同登记，申请放款成功！")
					logging.info("借出合同登记，申请放款成功！")
					time.sleep(3)

					# 退出所有iframe窗体

					switch_default()

					# 用JS的方法关闭当前页面
					js_click("xpath", "//a[@title='借出合同登记']/child::*[1]")

					# 点击理财合同登记菜单
					click("xpath", "//span[@title='放款处理']")

					# 退出所有的iframe窗体
					switch_default()

					logging.info("开始测试放款处理功能")

					# 切入‘放款处理’的iframe窗体
					switch_to("xpath", "//iframe[@id='lendingloan-tab-iframe']")
					# 点击

					click("xpath", "//span[text()='主动放款']")

					# 切入新增的iframe窗体
					switch_to("xpath", "//iframe[@id='subTabTwo-iframe']")

					# 勾选
					click("xpath", "//div[@title='借入单位:002001-Mindy科技有限公司']/parent::*/preceding-sibling::*[3]/descendant::*[2]")

					# 点击放款按钮
					click("xpath", "//span[text()='放款']")

					switch_to("xpath", "//iframe[@id='modWin-iframe']")

					# 勾选
					click("xpath", "//div[@title='借入单位:002001-Mindy科技有限公司']/parent::*/preceding-sibling::*[3]/descendant::*[2]")
					sleep(1)

					# 点击确认放款按钮
					click("xpath", "//span[text()='确认放款']")
					sleep(1)

					switch_default()

					# 切入‘放款处理’的iframe窗体
					switch_to("xpath", "//iframe[@id='lendingloan-tab-iframe']")

					# 点击
					click("xpath", "//span[text()='主动放款']")

					# 切入新增的iframe窗体
					switch_to("xpath", "//iframe[@id='subTabTwo-iframe']")

					switch_to("xpath", "//iframe[@id='modWin-iframe']")

					# 输入放款日期
					# 点击放款日期的日历按钮
					js_click("xpath", "//span[@id='lenddate-trigger']")
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

					# 切入‘放款处理’的iframe窗体
					switch_to("xpath", "//iframe[@id='lendingloan-tab-iframe']")

					# 点击
					click("xpath", "//span[text()='主动放款']")

					# 切入新增的iframe窗体
					switch_to("xpath", "//iframe[@id='subTabTwo-iframe']")

					switch_to("xpath", "//iframe[@id='modWin-iframe']")

					# 放款金额操作成功！
					input("xpath", "//input[@id='amount-input']", "3000")
					sleep(1)

					# 点击保存按钮
					click("xpath", "//span[text()='保存']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("借出合同登记，放款成功！")
					logging.info("借出合同登记，放款成功！")
					time.sleep(3)

					# 切入‘放款处理’的iframe窗体
					switch_to("xpath", "//iframe[@id='lendingloan-tab-iframe']")

					# 点击
					click("xpath", "//span[text()='主动放款']")

					# 切入新增的iframe窗体
					switch_to("xpath", "//iframe[@id='subTabTwo-iframe']")

					# 勾选
					click("xpath", "//div[@title='借入单位:002001-Mindy科技有限公司']/parent::*/preceding-sibling::*[3]/descendant::*[2]")

					# 点击送审按钮
					click("xpath", "//span[text()='送审']")

					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					sleep(1)

					# 退出所有iframe窗体
					switch_default()
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'送审成功:1笔！失败0笔！')]")
					print("放款申请，送审成功！")
					logging.info("放款申请，送审成功！")
					time.sleep(3)

					# 切入‘放款处理’的iframe窗体
					switch_to("xpath", "//iframe[@id='lendingloan-tab-iframe']")

					# 点击
					click("xpath", "//span[text()='主动放款']")

					# 切入新增的iframe窗体
					switch_to("xpath", "//iframe[@id='subTabTwo-iframe']")

					# 双击勾选数据
					double_click("xpath", "//div[@title='审批状态:审批中']/parent::*/preceding-sibling::*[8]/descendant::*[2]")
					sleep(1)

					switch_to("xpath", "//iframe[@id='wf_taskProcessing_win-iframe']")
					sleep(3)

					click("xpath", "//span[text()='同意']")
					sleep(1)

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("放款申请，第一次审批同意成功！")
					logging.info("放款申请，第一次审批同意成功！")
					time.sleep(3)

					# 切入‘放款处理’的iframe窗体
					switch_to("xpath", "//iframe[@id='lendingloan-tab-iframe']")

					# 点击主动放款
					click("xpath", "//span[text()='主动放款']")

					# 切入新增的iframe窗体
					switch_to("xpath", "//iframe[@id='subTabTwo-iframe']")

					# 双击勾选数据
					double_click("xpath", "//div[@title='审批状态:审批中']/parent::*/preceding-sibling::*[8]/descendant::*[2]")
					sleep(1)

					switch_to("xpath", "//iframe[@id='wf_taskProcessing_win-iframe']")
					sleep(3)

					click("xpath", "//span[text()='同意']")
					sleep(1)

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("放款申请，第二次审批同意成功！")
					logging.info("放款申请，第二次审批同意成功！")
					time.sleep(3)

					# 退出所有iframe窗体
					switch_default()

					# 用JS的方法关闭当前页面
					js_click("xpath", "//a[@title='放款处理']/child::*[1]")

					# 点击理财合同登记菜单
					click("xpath", "//span[@title='借出合同登记']")

					# 切入‘借出合同登记’的iframe窗体
					switch_to("xpath", "//iframe[@id='lendingcontract-tab-iframe']")

					# 用JS的方法点击高级查询按钮
					js_click("xpath", "//span[text()='高级查询']")

					click("xpath", "//input[@id='combobox-input-property_0']")
					sleep(1)
					clear("xpath", "//input[@id='combobox-input-property_0']")
					sleep(1)
					# 输入作废状态，通过模糊匹配搜索
					input("xpath", "//input[@id='combobox-input-property_0']", "合同编号")
					sleep(1)
					# 模拟回车
					click("xpath", "//div[contains(text(),'合同编号')]")
					sleep(1)

					click("xpath", "//input[@id='combobox-input-condition_0']")
					sleep(1)
					# 输入作废状态，通过模糊匹配搜索
					input("xpath", "//input[@id='combobox-input-condition_0']", "模糊")
					sleep(1)
					# 模拟回车
					click("xpath", "//div[contains(text(),'模糊')]")
					sleep(1)

					click("xpath", "//input[@id='value_0']")
					sleep(1)
					# 输入作废状态，通过模糊匹配搜索
					input("xpath", "//input[@id='value_0']", "ZDHLCHTH")
					sleep(1)
					# 模拟回车
					click("xpath", "//div[contains(text(),'ZDHLCHTH')]")
					sleep(1)

					# 放款状态
					click("xpath", "//input[@id='combobox-input-property_1']")
					sleep(1)
					clear("xpath", "//input[@id='combobox-input-property_1']")
					sleep(1)
					# 输入作废状态，通过模糊匹配搜索
					input("xpath", "//input[@id='combobox-input-property_1']", "放款状态")
					sleep(1)
					# 模拟回车
					click("xpath", "//div[contains(text(),'放款状态')]")
					sleep(1)

					click("xpath", "//input[@id='combobox-input-condition_1']")
					sleep(1)
					# 输入作废状态，通过模糊匹配搜索
					input("xpath", "//input[@id='combobox-input-condition_1']", "包含")
					sleep(1)
					# 模拟回车
					click("xpath", "//div[contains(text(),'包含')]")
					sleep(1)

					click("xpath", "//input[@id='combobox-input-value_1']")
					sleep(1)
					# 输入放款状态，通过模糊匹配搜索
					click("xpath", "//div[contains(text(),'已全额发放')]/preceding-sibling::*[1]")
					sleep(1)

					click("xpath", "//div[contains(text(),'部分发放')]/preceding-sibling::*[1]")
					sleep(1)

					click("xpath", "//div[contains(text(),'查询')]")
					sleep(1)

					js_click("xpath", "//span[text()='自定义查询']/preceding-sibling::*[1]")
					sleep(1)

					# 勾选
					click("xpath", "//div[@title='借入单位:002001-Mindy科技有限公司']/parent::*/preceding-sibling::*[3]/descendant::*[2]")

					# 点击保存按钮
					click("xpath", "//span[text()='回款']")
					sleep(1)

					# 进入回款窗体
					switch_to("xpath", "//iframe[@id='lendPayWin-iframe']")
					sleep(1)

					# 输入回款日期
					# 点击回款日期的日历按钮
					js_click("xpath", "//span[@id='repaydate-trigger']")
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

					# 切入‘放款处理’的iframe窗体
					switch_to("xpath", "//iframe[@id='lendingcontract-tab-iframe']")

					# 进入回款的窗体
					switch_to("xpath", "//iframe[@id='lendPayWin-iframe']")
					
					# 放款金额
					click("xpath", "//input[@id='principal-input']")
					sleep(1)
					clear("xpath", "//input[@id='principal-input']")
					sleep(1)
					input("xpath", "//input[@id='principal-input']", "3000")
					sleep(1)

					# # 输入应计利息
					# click("xpath", "//input[@id='possibleinterest-input']")
					# sleep(1)
					# clear("xpath", "//input[@id='possibleinterest-input']")
					# sleep(1)
					# input("xpath", "//input[@id='possibleinterest-input']", "30")
					# sleep(1)
					#
					# # 输入实收利息
					# click("xpath", "//input[@id='interest-input']")
					# sleep(1)
					# clear("xpath", "//input[@id='interest-input']")
					# sleep(1)
					# input("xpath", "//input[@id='interest-input']", "50")
					# sleep(1)

					# 点击保存按钮
					click("xpath", "//span[text()='保存']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("借出合同登记，回款成功！")
					logging.info("借出合同登记，回款成功！")
					time.sleep(3)

					# 利息登记
					# 切入‘借出合同登记’的iframe窗体
					switch_to("xpath", "//iframe[@id='lendingcontract-tab-iframe']")

					click("xpath", "//div[@title='借入单位:002001-Mindy科技有限公司']/parent::*/preceding-sibling::*[3]/descendant::*[2]")

					# 点击保存按钮
					click("xpath", "//span[text()='利息登记']")
					sleep(1)

					# 进入利息登记的窗体
					switch_to("xpath", "//iframe[@id='lendPayWin-iframe']")
					sleep(1)

					# 输入回款日期
					today = date.today()
					repay_date = today
					click("xpath", "//input[@id='repaydate-input']")
					sleep(1)
					clear("xpath", "//input[@id='repaydate-input']")
					sleep(1)
					input("xpath", "//input[@id='repaydate-input']", str(repay_date))
					# 模拟回车键
					keyDown('enter')
					keyUp('enter')
					time.sleep(2)
					
					# 选择结息方式
					click("xpath", "//input[@id='combobox-input-settlementinterestmode']")
					sleep(1)
					clear("xpath", "//input[@id='combobox-input-settlementinterestmode']")
					sleep(1)
					input("xpath", "//input[@id='combobox-input-settlementinterestmode']", "结算归还本金的利息")
					sleep(1)
					input_enter("xpath", "//input[@id='combobox-input-settlementinterestmode']")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-settlementinterestmode']")
					sleep(1)
					input_enter("xpath", "//input[@id='combobox-input-settlementinterestmode']")
					sleep(1)

					# 输入应计利息
					click("xpath", "//input[@id='possibleinterest-input']")
					sleep(1)
					clear("xpath", "//input[@id='possibleinterest-input']")
					sleep(1)
					input("xpath", "//input[@id='possibleinterest-input']", "30")
					sleep(1)
					
					# 输入实收利息
					click("xpath", "//input[@id='interest-input']")
					sleep(1)
					clear("xpath", "//input[@id='interest-input']")
					sleep(1)
					input("xpath", "//input[@id='interest-input']", "50")
					sleep(1)

					# 点击保存按钮
					click("xpath", "//span[text()='保存']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("借出合同登记，利息登记成功！")
					logging.info("借出合同登记，利息登记成功！")
					time.sleep(3)

					# 应收利息
					# 切入‘借出合同登记’的iframe窗体
					switch_to("xpath", "//iframe[@id='lendingcontract-tab-iframe']")

					click("xpath", "//div[@title='借入单位:002001-Mindy科技有限公司']/parent::*/preceding-sibling::*[3]/descendant::*[2]")

					# 点击保存按钮
					click("xpath", "//span[text()='应收利息']")
					sleep(1)

					# 进入应收利息的窗体
					switch_to("xpath", "//iframe[@id='lendPayWin-iframe']")
					sleep(1)
					
					# 选择结算方式
					click("xpath", "//input[@id='combobox-input-settlementinterestmode']")
					sleep(1)
					input("xpath", "//input[@id='combobox-input-settlementinterestmode']", "")

					# 点击保存按钮
					click("xpath", "//span[text()='试算']")
					sleep(1)

					# 点击取消按钮
					click("xpath", "//span[text()='取消']")
					sleep(1)

					# 退出所有iframe窗体
					switch_default()

					# 打印成功日志
					print("借出合同登记，应收利息成功！")
					logging.info("借出合同登记，应收利息成功！")
					time.sleep(3)

					# 重新生成还款计息计划
					# 切入‘借出合同登记’的iframe窗体
					switch_to("xpath", "//iframe[@id='lendingcontract-tab-iframe']")
					sleep(1)

					# # 勾选数据
					# click("xpath", "//div[@title='借入单位:002001-Mindy科技有限公司']/parent::*/preceding-sibling::*[3]/descendant::*[2]")
					#
					# 用JS方便点击‘调整还款计划’按钮旁边的倒三角形
					js_click("xpath", "//span[text()='调整还款计划']/parent::*/following-sibling::*/child::*")
					sleep(1)
					
					# 点击重新生成还款计息计划核按钮
					js_click("xpath", "//a[contains(text(),'重新生成还款计息计划')]")
					sleep(1)

					# 点击确认按钮
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'成功重新计息:1条！')]")
					print("借出合同登记，重新生成还款计息计划成功！")
					logging.info("借出合同登记，重新生成还款计息计划成功！")
					time.sleep(3)

				# 第三笔，作废
				elif i == 3:

					# 第三次审核
					# 切入‘借出合同登记’的iframe窗体
					switch_to("xpath", "//iframe[@id='lendingcontract-tab-iframe']")

					# 勾选
					click("xpath", "//div[@title='借入单位:002001-Mindy科技有限公司']/parent::*/preceding-sibling::*[3]/descendant::*[2]")

					# 点击审核按钮
					click("xpath", "//span[text()='审核']")

					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'成功审核1条记录')]")
					print("借出合同登记，第三次审批成功！")
					logging.info("借出合同登记，第三次审批成功！")
					time.sleep(3)

					# 变更 # 勾选 点击变更按钮会报执行BO方法出错，请联系系统维护人员！
					# 切入‘借出合同登记’的iframe窗体
					switch_to("xpath", "//iframe[@id='lendingcontract-tab-iframe']")

					click("xpath", "//div[@title='借入单位:002001-Mindy科技有限公司']/parent::*/preceding-sibling::*[3]/descendant::*[2]")

					# 点击变更按钮
					click("xpath", "//span[text()='变更']")
					sleep(1)

					# 切入变更的iframe窗体
					switch_to("xpath", "//iframe[@id='modWin-iframe']")
					print("进入变更窗体")
					sleep(1)

					# 描述abstracts
					input("xpath", "//textarea[@id='abstracts']", "自动化测试借出合同备注框")
					sleep(1)

					# 备注框中输入新内容
					input("xpath", "//textarea[@id='description']", "自动化测试借出合同变更备注框")
					sleep(1)

					# 点击保存按钮
					click("xpath", "//span[text()='保存']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("借出合同，变更成功！")
					logging.info("借出合同，变更成功！")
					time.sleep(3)

					# 作废 #切入‘借出合同登记’的iframe窗体
					switch_to("xpath", "//iframe[@id='lendingcontract-tab-iframe']")

					# 勾选
					click("xpath", "//div[@title='借入单位:002001-Mindy科技有限公司']/parent::*/preceding-sibling::*[3]/descendant::*[2]")

					# 点击审核按钮
					click("xpath", "//span[text()='作废']")

					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'成功作废1条记录！')]")
					print("借出合同登记，作废成功！")
					logging.info("借出合同登记，作废成功！")
					time.sleep(3)

			# 退出所有iframe窗体
			switch_default()

			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='借出合同登记']/child::*[1]")

			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//span[@title='借出方管理']")

			# 打印操作成功日志
			print("借出合同登记，操作成功!")
			logging.info("借出合同登记，操作成功!")
			time.sleep(2)
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("借出合同登记,失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		
		# 测试内部借款管理-借出方登记-放款处理
		try:
			# 点击理财投资菜单
			click("xpath", "//span[@title='借出方管理']")
			# 点击理财合同登记菜单
			click("xpath", "//span[@title='放款处理']")

			# 退出所有的iframe窗体
			switch_default()

			logging.info("开始测试放款处理功能")

			# # 切入‘放款处理’的iframe窗体
			# switch_to("xpath", "//iframe[@id='lendingloan-tab-iframe']")
			# # 测试申请放款功能
			# click("xpath", "//span[text()='申请放款']")
			#
			# # 切入‘申请放款’的iframe窗体
			# switch_to("xpath", "//iframe[@id='subTabOne-iframe']")
			# sleep(1)
			#
			# # 勾选
			# click("xpath", "//div[@title='生成交易单状态:未生成']/parent::*/preceding-sibling::*[10]/descendant::*[2]")
			#
			# # 点击查询
			# click("xpath", "//span[text()='生成交易单']")
			#
			# # 切入申请放款的窗体lendGenRecWin-iframe
			# switch_to("xpath", "//iframe[@id='lendGenRecWin-iframe']")
			# sleep(1)
			#
			# # 选择支付类型
			# click("xpath", "//input[@id='combobox-input-dealtype']")
			# sleep(1)
			# input("xpath", "//input[@id='combobox-input-dealtype']", "直联")
			# input_enter("xpath", "//input[@id='combobox-input-dealtype']")
			# time.sleep(1)
			#
			# # 选择下一步
			# click("xpath", "//span[text()='下一步']")
			# sleep(1)
			#
			# switch_default()
			#
			# # 切入‘放款处理’的iframe窗体
			# switch_to("xpath", "//iframe[@id='lendingloan-tab-iframe']")
			#
			# click("xpath", "//span[text()='申请放款']")
			#
			# # 切入‘申请放款’的iframe窗体
			# switch_to("xpath", "//iframe[@id='subTabOne-iframe']")
			# sleep(1)
			#
			# switch_to("xpath", "//iframe[@id='addRecWin-iframe']")
			# sleep(1)
			#
			# # 部门
			# click("xpath", "//input[@id='combobox-input-deptid']")
			# # 输入银行名称，模糊查询
			# input("xpath", "//input[@id='combobox-input-deptid']", "自动化测试部")
			# sleep(1)
			# input_down("xpath", "//input[@id='combobox-input-deptid']")
			# input_enter("xpath", "//input[@id='combobox-input-deptid']")
			# time.sleep(1)
			#
			# # 选择交易类型
			# click("xpath", "//input[@id='combobox-input-paytypeid']")
			# sleep(1)
			# clear("xpath", "//input[@id='combobox-input-paytypeid']")
			# sleep(1)
			# # 输入交易类型名称，模糊查询
			# input("xpath", "//input[@id='combobox-input-paytypeid']", "对外付款")
			# sleep(1)
			# input_down("xpath", "//input[@id='combobox-input-paytypeid']")
			# input_enter("xpath", "//input[@id='combobox-input-paytypeid']")
			# time.sleep(1)
			#
			# # 结算方式
			# click("xpath", "//input[@id='combobox-input-settlementmodeid']")
			# sleep(1)
			# clear("xpath", "//input[@id='combobox-input-settlementmodeid']")
			# sleep(1)
			# # 输入交易类型名称，模糊查询
			# input("xpath", "//input[@id='combobox-input-settlementmodeid']", "直联单笔转账")
			# sleep(1)
			# input_down("xpath", "//input[@id='combobox-input-settlementmodeid']")
			# input_enter("xpath", "//input[@id='combobox-input-settlementmodeid']")
			# time.sleep(1)
			#
			# # 付方账户
			# # 输入银行名称，模糊查询
			# input("xpath", "//input[@id='combobox-input-ourbankaccountid' and @class='f-combo-input f-input-bg  f-combo-input-forceselect']", "中国银行 ")
			# sleep(1)
			# input_down("xpath", "//input[@id='combobox-input-ourbankaccountid' and @class='f-combo-input f-input-bg  f-combo-input-forceselect']")
			# input_enter("xpath", "//input[@id='combobox-input-ourbankaccountid' and @class='f-combo-input f-input-bg  f-combo-input-forceselect']")
			# time.sleep(1)
			#
			# # 收方名称
			# click("xpath", "//input[@id='combobox-input-oppcounterpartyid']")
			# input("xpath", "//input[@id='combobox-input-oppcounterpartyid']", "002001-Mindy自动化测试")
			# sleep(1)
			# input_down("xpath", "//input[@id='combobox-input-oppcounterpartyid']")
			# input_enter("xpath", "//input[@id='combobox-input-oppcounterpartyid']")
			# time.sleep(1)
			#
			# # 用途
			# input("xpath", "//input[@id='combobox-input-purpose']", "自动化测试申请放款")
			# sleep(1)
			#
			# # 计划项目
			# click("xpath", "//input[@id='combobox-input-budgetitemid']")
			# # 输入银行名称，模糊查询
			# input("xpath", "//input[@id='combobox-input-budgetitemid']", "自动化计划项目")
			# sleep(1)
			# input_down("xpath", "//input[@id='combobox-input-budgetitemid']")
			# input_enter("xpath", "//input[@id='combobox-input-budgetitemid']")
			# time.sleep(1)
			#
			# # 资金类别
			# click("xpath", "//input[@id='combobox-input-capitalcategoryid']")
			# input("xpath", "//input[@id='combobox-input-capitalcategoryid']", "其他")
			# input_down("xpath", "//input[@id='combobox-input-capitalcategoryid']")
			# input_enter("xpath", "//input[@id='combobox-input-capitalcategoryid']")
			# time.sleep(1)
			#
			# # 现金流量项目
			# click("xpath", "//input[@id='combobox-input-cashflowitemid']")
			# input("xpath", "//input[@id='combobox-input-cashflowitemid']", "对外投资等到活动所支付的现金")
			# input_down("xpath", "//input[@id='combobox-input-cashflowitemid']")
			# input_enter("xpath", "//input[@id='combobox-input-cashflowitemid']")
			# time.sleep(1)
			#
			# # 短信通知
			# input("xpath", "//input[@id='oppcellphone']", "178短信通知")
			# sleep(1)
			#
			# # 邮件通知
			# input("xpath", "//input[@id='oppemailaddress']", "1074658681@qq.com邮件通知")
			# sleep(1)
			#
			# # 备注框中填入值
			# input("xpath", "//textarea[@id='memo']", "自动化测试生成交易单备注框")
			# sleep(1)
			#
			# # 描述框中填入值
			# input("xpath", "//textarea[@id='description']", "自动化测试生成交易单描述框")
			# sleep(1)
			#
			# # 点击确认保存
			# click("xpath", "//span[text()='保存']")
			# # 退出所有的iframe窗体
			# switch_default()
			#
			# # 用隐式等待方法等页面出现新增成功的提示框
			# implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			# print("申请放款，生成交易单保存成功！")
			# sleep(3)
			#
			# # 切入‘放款处理’的iframe窗体
			# switch_to("xpath", "//iframe[@id='lendingloan-tab-iframe']")
			#
			# click("xpath", "//span[text()='申请放款']")
			#
			# # 切入‘申请放款’的iframe窗体
			# switch_to("xpath", "//iframe[@id='subTabOne-iframe']")
			# sleep(1)
			#
			# # 勾选
			# click("xpath", "//div[@title='生成交易单状态:未生成']/parent::*/preceding-sibling::*[10]/descendant::*[2]")
			# sleep(1)
			#
			# # 点击作废按钮
			# click("xpath", "//span[text()='作废']")
			#
			# # 点击弹出框的OK键
			# click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
			#
			# # 退出所有的iframe窗体
			# switch_default()
			#
			# # 用隐式等待方法等页面出现新增成功的提示框
			# implici_wait("xpath", "//span[contains(text(),'作废成功:1笔！失败:0笔！')]")
			# print("申请放款，作废成功！")
			# sleep(3)
			#
			# 切入‘放款处理’的iframe窗体
			switch_to("xpath", "//iframe[@id='lendingloan-tab-iframe']")
			# 点击

			click("xpath", "//span[text()='主动放款']")

			# 切入新增的iframe窗体
			switch_to("xpath", "//iframe[@id='subTabTwo-iframe']")

			# 勾选
			click("xpath", "//div[@title='借入单位:002001-Mindy科技有限公司']/parent::*/preceding-sibling::*[3]/descendant::*[2]")

			# 点击放款按钮
			click("xpath", "//span[text()='放款']")

			switch_to("xpath", "//iframe[@id='modWin-iframe']")

			# 勾选
			click("xpath", "//div[@title='借入单位:002001-Mindy科技有限公司']/parent::*/preceding-sibling::*[3]/descendant::*[2]")
			sleep(1)

			# 点击确认放款按钮
			click("xpath", "//span[text()='确认放款']")
			sleep(1)

			switch_default()

			# 切入‘放款处理’的iframe窗体
			switch_to("xpath", "//iframe[@id='lendingloan-tab-iframe']")
			# 点击

			click("xpath", "//span[text()='主动放款']")

			# 切入新增的iframe窗体
			switch_to("xpath", "//iframe[@id='subTabTwo-iframe']")

			switch_to("xpath", "//iframe[@id='modWin-iframe']")

			# 输入放款日期
			# 点击放款日期的日历按钮
			js_click("xpath", "//span[@id='lenddate-trigger']")
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

			# 切入‘放款处理’的iframe窗体
			switch_to("xpath", "//iframe[@id='lendingloan-tab-iframe']")
			# 点击

			click("xpath", "//span[text()='主动放款']")

			# 切入新增的iframe窗体
			switch_to("xpath", "//iframe[@id='subTabTwo-iframe']")

			switch_to("xpath", "//iframe[@id='modWin-iframe']")

			# 放款金额操作成功！
			input("xpath", "//input[@id='amount-input']", "3000")
			sleep(1)

			# 点击保存按钮
			click("xpath", "//span[text()='保存']")

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("借出合同登记，放款成功！")
			logging.info("借出合同登记，放款成功！")
			time.sleep(3)

			# 切入‘放款处理’的iframe窗体
			switch_to("xpath", "//iframe[@id='lendingloan-tab-iframe']")
			# 点击

			click("xpath", "//span[text()='主动放款']")

			# 切入新增的iframe窗体
			switch_to("xpath", "//iframe[@id='subTabTwo-iframe']")

			# 勾选
			click("xpath", "//div[@title='审批状态:未审批']/parent::*/preceding-sibling::*[8]/descendant::*[2]")
			sleep(1)

			# 点击审核
			click("xpath", "//span[text()='审核']")
			sleep(1)

			# 点击弹出框的OK键
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
			sleep(1)

			# 退出所有的iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功!审核成功1笔，失败0笔')]")
			print("主动放款，审核成功！")
			sleep(3)

			# 切入‘放款处理’的iframe窗体
			switch_to("xpath", "//iframe[@id='lendingloan-tab-iframe']")

			# 点击
			click("xpath", "//span[text()='主动放款']")

			# 切入新增的iframe窗体
			switch_to("xpath", "//iframe[@id='subTabTwo-iframe']")

			# 勾选
			click("xpath", "//div[@title='审批状态:已审批']/parent::*/preceding-sibling::*[8]/descendant::*[2]")
			sleep(1)

			# 用JS方便点击‘审核’按钮旁边的倒三角形
			js_click("xpath", "//span[text()='审核']/parent::*/following-sibling::*/child::*")
			sleep(1)

			# 点击取消送审按钮
			js_click("xpath", "//a[contains(text(),'取消审核')]")
			sleep(1)

			# 点击弹出框的OK键
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
			sleep(1)

			# 退出所有的iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("主动放款，取消审核成功！")
			sleep(3)

			# 切入‘放款处理’的iframe窗体
			switch_to("xpath", "//iframe[@id='lendingloan-tab-iframe']")
			# 点击

			click("xpath", "//span[text()='主动放款']")

			# 切入新增的iframe窗体
			switch_to("xpath", "//iframe[@id='subTabTwo-iframe']")

			# 勾选
			click("xpath", "//div[@title='审批状态:未审批']/parent::*/preceding-sibling::*[8]/descendant::*[2]")
			sleep(1)

			# 点击审核
			click("xpath", "//span[text()='审核']")
			sleep(1)

			# 点击弹出框的OK键
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
			sleep(1)

			# 退出所有的iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功!审核成功1笔，失败0笔')]")
			print("主动放款，审核成功！")
			sleep(3)

			# 切入‘放款处理’的iframe窗体
			switch_to("xpath", "//iframe[@id='lendingloan-tab-iframe']")

			# 点击
			click("xpath", "//span[text()='主动放款']")

			# 切入新增的iframe窗体
			switch_to("xpath", "//iframe[@id='subTabTwo-iframe']")

			# 勾选
			click("xpath", "//div[@title='审批状态:已审批']/parent::*/preceding-sibling::*[8]/descendant::*[2]")
			sleep(1)

			# 点击变更
			click("xpath", "//span[text()='变更']")
			sleep(1)

			switch_to("xpath", "//iframe[@id='modWin-iframe']")

			# 点击保存
			click("xpath", "//span[text()='保存']")
			sleep(1)

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("主动放款，变更成功！")
			logging.info("主动放款，变更成功！")
			time.sleep(3)

			# 切入‘放款处理’的iframe窗体
			switch_to("xpath", "//iframe[@id='lendingloan-tab-iframe']")
			# 点击

			click("xpath", "//span[text()='主动放款']")

			# 切入新增的iframe窗体
			switch_to("xpath", "//iframe[@id='subTabTwo-iframe']")

			# 勾选
			click("xpath", "//div[@title='审批状态:未审批']/parent::*/preceding-sibling::*[8]/descendant::*[2]")
			sleep(1)

			# 点击审核
			click("xpath", "//span[text()='审核']")
			sleep(1)

			# 点击弹出框的OK键
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
			sleep(1)

			# 退出所有的iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功!审核成功1笔，失败0笔')]")
			print("主动放款，审核成功！")
			sleep(3)

			# 切入‘放款处理’的iframe窗体
			switch_to("xpath", "//iframe[@id='lendingloan-tab-iframe']")

			# 点击
			click("xpath", "//span[text()='主动放款']")

			# 切入新增的iframe窗体
			switch_to("xpath", "//iframe[@id='subTabTwo-iframe']")

			# 查询条件里增加过滤条件
			# 用JS的方法点击放大镜
			js_click("xpath", "//span[@class='f-contrac-close']")
			sleep(1)

			# 选择已审批、未生成交易单的数据来生成交易单
			click("xpath", "//input[@id='combobox-input-approvestate']")
			sleep(1)
			click("xpath", "//div[@title='已审批']")
			sleep(1)

			# 点击查询
			click("xpath", "//span[text()='查询']")

			# 勾选
			click("xpath", "//div[@title='生成交易单状态:未生成']/parent::*/preceding-sibling::*[10]/descendant::*[2]")
			sleep(1)

			# 点击生成交易单
			click("xpath", "//span[text()='生成交易单']")

			# 切入主动放款生成交易单的窗体
			switch_to("xpath", "//iframe[@id='lendGenRecWin-iframe']")
			sleep(1)

			# 选择支付类型
			click("xpath", "//input[@id='combobox-input-dealtype']")
			sleep(1)
			input("xpath", "//input[@id='combobox-input-dealtype']", "直联")
			input_enter("xpath", "//input[@id='combobox-input-dealtype']")
			time.sleep(1)

			# 选择下一步
			click("xpath", "//span[text()='下一步']")
			sleep(1)

			switch_default()

			# 切入‘放款处理’的iframe窗体
			switch_to("xpath", "//iframe[@id='lendingloan-tab-iframe']")
			# 点击

			click("xpath", "//span[text()='主动放款']")

			# 切入新增的iframe窗体
			switch_to("xpath", "//iframe[@id='subTabTwo-iframe']")

			switch_to("xpath", "//iframe[@id='addRecWin-iframe']")
			sleep(1)

			# 部门
			click("xpath", "//input[@id='combobox-input-deptid']")
			# 输入银行名称，模糊查询
			input("xpath", "//input[@id='combobox-input-deptid']", "自动化测试部")
			sleep(1)
			input_down("xpath", "//input[@id='combobox-input-deptid']")
			input_enter("xpath", "//input[@id='combobox-input-deptid']")
			time.sleep(1)

			# 选择交易类型
			click("xpath", "//input[@id='combobox-input-paytypeid']")
			sleep(1)
			clear("xpath", "//input[@id='combobox-input-paytypeid']")
			sleep(1)
			# 输入交易类型名称，模糊查询
			input("xpath", "//input[@id='combobox-input-paytypeid']", "对外付款")
			sleep(1)
			input_down("xpath", "//input[@id='combobox-input-paytypeid']")
			input_enter("xpath", "//input[@id='combobox-input-paytypeid']")
			time.sleep(1)

			# 结算方式
			click("xpath", "//input[@id='combobox-input-settlementmodeid']")
			sleep(1)
			clear("xpath", "//input[@id='combobox-input-settlementmodeid']")
			sleep(1)
			# 输入交易类型名称，模糊查询
			input("xpath", "//input[@id='combobox-input-settlementmodeid']", "直联单笔转账")
			sleep(1)
			input_down("xpath", "//input[@id='combobox-input-settlementmodeid']")
			input_enter("xpath", "//input[@id='combobox-input-settlementmodeid']")
			time.sleep(1)

			# 付方账户
			# 输入银行名称，模糊查询
			input("xpath", "//input[@id='combobox-input-ourbankaccountid' and @class='f-combo-input f-input-bg  f-combo-input-forceselect']", "中国银行")
			sleep(1)
			input_down("xpath", "//input[@id='combobox-input-ourbankaccountid' and @class='f-combo-input f-input-bg  f-combo-input-forceselect']")
			input_enter("xpath","//input[@id='combobox-input-ourbankaccountid' and @class='f-combo-input f-input-bg  f-combo-input-forceselect']")
			time.sleep(1)

			# 收方名称
			input("xpath", "//input[@id='combobox-input-oppcounterpartyid']", "002001-Mindy自动化测试")
			sleep(1)

			# 点击空白处
			click("xpath", "//span[text()='卡折类型']")

			# 收方账户
			input("xpath", "//input[@id='combobox-input-oppcounterpartyaccountid']", "20203212344")
			sleep(1)
			click("xpath", "//span[text()='卡折类型']")

			# 收方开户银行
			click("xpath", "//input[@id='combobox-input-oppbanklocationid']")
			input("xpath", "//input[@id='combobox-input-oppbanklocationid']", "402368340019-安徽桐城农村商业银行股份有限公司枞阳支行")
			sleep(1)
			input_down("xpath", "//input[@id='combobox-input-oppbanklocationid']")
			input_enter("xpath", "//input[@id='combobox-input-oppbanklocationid']")
			time.sleep(1)

			# 用途
			input("xpath", "//input[@id='combobox-input-purpose']", "自动化测试申请放款")
			sleep(1)

			# 计划项目
			click("xpath", "//input[@id='combobox-input-budgetitemid']")
			# 输入银行名称，模糊查询
			input("xpath", "//input[@id='combobox-input-budgetitemid']", "自动化计划项目")
			sleep(1)
			input_down("xpath", "//input[@id='combobox-input-budgetitemid']")
			input_enter("xpath", "//input[@id='combobox-input-budgetitemid']")
			time.sleep(1)

			# 资金类别
			click("xpath", "//input[@id='combobox-input-capitalcategoryid']")
			input("xpath", "//input[@id='combobox-input-capitalcategoryid']", "其他")
			input_down("xpath", "//input[@id='combobox-input-capitalcategoryid']")
			input_enter("xpath", "//input[@id='combobox-input-capitalcategoryid']")
			time.sleep(1)

			# 现金流量项目
			click("xpath", "//input[@id='combobox-input-cashflowitemid']")
			input("xpath", "//input[@id='combobox-input-cashflowitemid']", "对外投资等到活动所支付的现金")
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

			# 描述框中填入值
			input("xpath", "//textarea[@id='description']", "自动化测试生成交易单描述框")
			sleep(1)

			# 点击确认保存
			click("xpath", "//span[text()='保存']")
			# 退出所有的iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("主动放款，生成交易单保存成功！")
			sleep(3)

			# 切入‘放款处理’的iframe窗体
			switch_to("xpath", "//iframe[@id='lendingloan-tab-iframe']")

			# 点击
			click("xpath", "//span[text()='主动放款']")

			# 切入新增的iframe窗体
			switch_to("xpath", "//iframe[@id='subTabTwo-iframe']")

			# 选择已审批、未生成交易单的数据来生成交易单
			click("xpath", "//input[@id='combobox-input-approvestate']")
			sleep(1)
			click("xpath", "//div[@title='已审批']")
			sleep(1)
			click("xpath", "//div[@title='未审批']")
			sleep(1)

			# 点击查询
			click("xpath", "//span[text()='查询']")

			# 勾选
			click("xpath", "//div[@title='生成交易单状态:未生成']/parent::*/preceding-sibling::*[10]/descendant::*[2]")
			sleep(1)

			click("xpath", "//span[text()='删除']")

			# 点击弹出框的OK键
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
			sleep(1)

			# 退出所有的iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'删除成功:1笔！失败0笔！')]")
			print("主动放款，删除成功！")
			sleep(3)

			# 切入‘放款处理’的iframe窗体
			switch_to("xpath", "//iframe[@id='lendingloan-tab-iframe']")
			# 点击

			click("xpath", "//span[text()='主动放款']")

			# 切入新增的iframe窗体
			switch_to("xpath", "//iframe[@id='subTabTwo-iframe']")

			# 勾选
			click("xpath", "//div[@title='生成交易单状态:未生成']/parent::*/preceding-sibling::*[10]/descendant::*[2]")
			sleep(1)

			# 点击审核
			click("xpath", "//span[text()='审核']")
			sleep(1)

			# 点击弹出框的OK键
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
			sleep(1)

			# 退出所有的iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功!审核成功1笔，失败0笔')]")
			print("主动放款，审核成功！")
			sleep(3)

			# 切入‘放款处理’的iframe窗体
			switch_to("xpath", "//iframe[@id='lendingloan-tab-iframe']")
			# 点击

			click("xpath", "//span[text()='主动放款']")

			# 切入新增的iframe窗体
			switch_to("xpath", "//iframe[@id='subTabTwo-iframe']")

			# 选择已审批、未生成交易单的数据来生成交易单
			click("xpath", "//input[@id='combobox-input-approvestate']")
			sleep(1)
			click("xpath", "//div[@title='未审批']")
			click("xpath", "//div[@title='已审批']")
			sleep(1)

			# 点击查询
			click("xpath", "//span[text()='查询']")

			# 勾选
			click("xpath", "//div[@title='生成交易单状态:未生成']/parent::*/preceding-sibling::*[10]/descendant::*[2]")
			sleep(1)

			click("xpath", "//span[text()='作废']")
			# 点击弹出框的OK键
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
			sleep(1)

			# 退出所有的iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'作废成功:1笔！失败0笔！')]")
			print("主动放款，作废成功！")
			sleep(3)

			# 退出所有iframe窗体
			switch_default()

			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='放款处理']/child::*[1]")

			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//span[@title='借出方管理']")

			# 打印操作成功日志
			print("放款处理，操作成功!")
			logging.info("放款处理，操作成功!")
			time.sleep(2)

		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("放款处理,失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)

		# 测试内部借款管理--回款登记
		try:
			# 点击借出方管理菜单
			click("xpath", "//span[@title='借出方管理']")
			# 点击回款登记菜单
			click("xpath", "//span[@title='回款登记']")

			# 退出所有的iframe窗体
			switch_default()

			logging.info("开始测试回款登记功能")

			# 切入‘回款登记’的iframe窗体
			switch_to("xpath", "//iframe[@id='lendingsrepayment-tab-iframe']")
			sleep(1)

			# 点击回款按钮
			click("xpath", "//span[text()='回款']")

			switch_to("xpath", "//iframe[@id='modWin-iframe']")

			# 勾选
			click("xpath", "//div[@title='借入单位:002001-Mindy科技有限公司']/parent::*/preceding-sibling::*[3]/descendant::*[2]")
			sleep(1)

			# 点击确认回款按钮
			click("xpath", "//span[text()='确认回款']")
			sleep(1)

			switch_default()

			# 切入‘回款登记’的iframe窗体
			switch_to("xpath", "//iframe[@id='lendingsrepayment-tab-iframe']")

			switch_to("xpath", "//iframe[@id='modWin-iframe']")

			# 输入回款日期
			# 点击回款日期的日历按钮
			js_click("xpath", "//span[@id='repaydate-trigger']")
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

			# 切入回款登记的iframe窗体
			switch_to("xpath", "//iframe[@id='lendingsrepayment-tab-iframe']")

			# 进入确认回款的窗体
			switch_to("xpath", "//iframe[@id='modWin-iframe']")

			# 回款金额
			clear("xpath", "//input[@id='principal-input']")
			sleep(1)
			input("xpath", "//input[@id='principal-input']", "3000")
			sleep(1)

			# 点击保存按钮
			click("xpath", "//span[text()='保存']")

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("回款登记，回款成功！")
			logging.info("回款登记，回款成功！")
			time.sleep(3)

			# 切入‘回款登记’的iframe窗体
			switch_to("xpath", "//iframe[@id='lendingsrepayment-tab-iframe']")
			# 点击
			# 勾选
			click("xpath", "//div[@title='审批状态:未审批']/parent::*/preceding-sibling::*[8]/descendant::*[2]")
			sleep(1)

			# 点击审核
			click("xpath", "//span[text()='审核']")
			sleep(1)

			# 点击弹出框的OK键
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
			sleep(1)

			# 退出所有的iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功!审核成功1笔，失败0笔')]")
			print("回款登记，审核成功！")
			sleep(3)

			# 切入‘回款登记’的iframe窗体
			switch_to("xpath", "//iframe[@id='lendingsrepayment-tab-iframe']")

			# 勾选
			click("xpath", "//div[@title='审批状态:已审批']/parent::*/preceding-sibling::*[8]/descendant::*[2]")
			sleep(1)

			# 用JS方便点击‘审核’按钮旁边的倒三角形
			js_click("xpath", "//span[text()='审核']/parent::*/following-sibling::*/child::*")
			sleep(1)

			# 点击取消送审按钮
			js_click("xpath", "//a[contains(text(),'取消审核')]")
			sleep(1)

			# 点击弹出框的OK键
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
			sleep(1)

			# 退出所有的iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("回款登记，取消审核成功！")
			sleep(3)

			# 切入‘回款登记’的iframe窗体
			switch_to("xpath", "//iframe[@id='lendingsrepayment-tab-iframe']")

			# 勾选
			click("xpath", "//div[@title='审批状态:未审批']/parent::*/preceding-sibling::*[8]/descendant::*[2]")
			sleep(1)

			# 点击审核
			click("xpath", "//span[text()='审核']")
			sleep(1)

			# 点击弹出框的OK键
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
			sleep(1)

			# 退出所有的iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功!审核成功1笔，失败0笔')]")
			print("回款登记，审核成功！")
			sleep(3)

			# 切入‘回款登记’的iframe窗体
			switch_to("xpath", "//iframe[@id='lendingsrepayment-tab-iframe']")

			# 勾选
			click("xpath", "//div[@title='审批状态:已审批']/parent::*/preceding-sibling::*[8]/descendant::*[2]")
			sleep(1)

			# 点击变更
			click("xpath", "//span[text()='变更']")
			sleep(1)

			switch_to("xpath", "//iframe[@id='modWin-iframe']")

			# 点击保存
			click("xpath", "//span[text()='保存']")
			sleep(1)

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("回款登记，变更成功！")
			logging.info("回款登记，变更成功！")
			time.sleep(3)

			# 切入‘回款登记’的iframe窗体
			switch_to("xpath", "//iframe[@id='lendingsrepayment-tab-iframe']")

			# 勾选
			click("xpath", "//div[@title='审批状态:未审批']/parent::*/preceding-sibling::*[8]/descendant::*[2]")
			sleep(1)

			# 点击审核
			click("xpath", "//span[text()='审核']")
			sleep(1)

			# 点击弹出框的OK键
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
			sleep(1)

			# 退出所有的iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功!审核成功1笔，失败0笔')]")
			print("回款登记，审核成功！")
			sleep(3)

			# 切到内部账户管理模块新增内部账户资金池以及内部账户
			# 先退出所有iframe窗体
			switch_default()

			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='回款登记']/child::*[1]")

			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//span[@title='借出方管理']")

			# 打印操作成功日志
			print("退出回款登记页面成功")
			logging.info("退出回款登记页面成功")
			time.sleep(2)

			logging.info("开始测试内部资金池功能")
			# 将页面的滚动条滑动到‘内部资金池’页面的地方
			js_gd("xpath", "//span[contains(text(),'内部资金池')]")
			# 用JS的方法点击资金结算管理菜单按钮
			js_click("xpath", "//span[contains(text(),'内部资金池')]")

			# 点击资金池内部计价菜单
			click("xpath", "//span[@title='资金池内部计价']")
			# 点击内部账户管理菜单
			click("xpath", "//span[@title='内部账户管理']")

			# 退出所有的iframe窗体
			switch_default()

			logging.info("开始测试内部账户管理功能")
			# 切入‘内部账户管理’的iframe窗体
			switch_to("xpath", "//iframe[@id='accountManage-tab-iframe']")
			sleep(1)

			# 新增内部账户池按钮
			click("xpath", "//span[text()='新增内部账户池']")

			switch_to("xpath", "//iframe[@id='addWin-iframe']")

			# 设置时间的变成存储，变成
			temp1 = time.strftime("%H%M%S")

			# 输入代码
			click("xpath", "//input[@id='code']")
			sleep(1)
			input("xpath", "//input[@id='code']", "Test_AccountPool" + str(temp1))

			# 输入名称
			click("xpath", "//input[@id='name']")
			sleep(1)
			input("xpath", "//input[@id='name']", "Test_AccountPool" + str(temp1))

			# 点击保存按钮
			click("xpath", "//span[text()='保存']")

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("新增内部账户池，新增成功！")
			logging.info("新增内部账户池，新增成功！")
			time.sleep(3)

			# 新增内部账户
			# 切入‘内部账户管理’的iframe窗体
			switch_to("xpath", "//iframe[@id='accountManage-tab-iframe']")
			sleep(1)

			# 新增内部账户按钮
			click("xpath", "//span[text()='新增内部账户']")

			switch_to("xpath", "//iframe[@id='addWin-iframe']")

			# 选择内部账户池
			click("xpath", "//input[@id='combobox-input-accountpoolid']")
			sleep(1)
			click("xpath", "//div[contains(text(),'Test_AccountPool')]")
			sleep(1)

			# 选择内部账户
			click("xpath", "//input[@id='combobox-input-orgid']")
			sleep(1)
			input("xpath", "//input[@id='combobox-input-orgid']", "亚唐科技")
			input_down("xpath", "//input[@id='combobox-input-orgid']")
			input_enter("xpath", "//input[@id='combobox-input-orgid']")
			time.sleep(1)

			click("xpath", "//span[@title='默认结算户']")
			sleep(1)

			# 设置时间的变成存储，变成
			temp1 = time.strftime("%H%M%S")

			# 输入账号
			input("xpath", "//input[@id='code']", "202076" + str(temp1))

			# 输入名称
			input("xpath", "//input[@id='name']", "202076" + str(temp1))

			# 币种
			click("xpath", "//input[@id='combobox-input-currencyid']")
			sleep(1)
			input("xpath", "//input[@id='combobox-input-currencyid']", "CNY")
			input_down("xpath", "//input[@id='combobox-input-currencyid']")
			input_enter("xpath", "//input[@id='combobox-input-currencyid']")
			time.sleep(1)

			# 账户存款类型
			click("xpath", "//input[@id='combobox-input-deposittype']")
			sleep(1)
			click("xpath", "//div[contains(text(),'活期')]")
			sleep(1)

			# 存货标识

			click("xpath", "//input[@id='combobox-input-depositloansign']")
			sleep(1)
			click("xpath", "//div[contains(text(),'存款')]")
			sleep(1)

			# 透支金额
			clear("xpath", "//input[@id='maxoverdraftamount-input']")
			input("xpath", "//input[@id='maxoverdraftamount-input']", "3000")
			sleep(1)

			# 利率方案
			click("xpath", "//input[@id='combobox-input-interestrateschemeid']")
			# 按键往下，选择利率方案
			sleep(2)
			input_down("xpath", "//input[@id='combobox-input-interestrateschemeid']")
			input_enter("xpath", "//input[@id='combobox-input-interestrateschemeid']")
			sleep(1)

			# 计息周期
			click("xpath", "//input[@id='combobox-input-interestperiodtype']")
			# 按键往下，选择利率方案
			sleep(2)
			input_down("xpath", "//input[@id='combobox-input-interestperiodtype']")
			input_enter("xpath", "//input[@id='combobox-input-interestperiodtype']")
			sleep(1)

			# 结息日
			input("xpath", "//input[@id='interestsettlementdate']", "12")
			sleep(1)

			# 点击保存按钮
			click("xpath", "//span[text()='保存']")

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("新增内部账户池，新增成功！")
			logging.info("新增内部账户池，新增成功！")
			time.sleep(3)

			# 切入‘内部账户管理’的iframe窗体
			switch_to("xpath", "//iframe[@id='accountManage-tab-iframe']")
			sleep(1)

			# 点击查看
			# 用JS的方法点击放大镜
			js_click("xpath", "//span[@class='f-contrac-close']")
			sleep(1)

			# 输入内部账户池
			click("xpath", "//input[@id='combobox-input-accountpoolid']")
			sleep(1)
			click("xpath", "//div[contains(text(),'Test_AccountPool')]")

			# 点击查询
			click("xpath", "//span[text()='查询']")
			sleep(1)

			# 点击勾选
			click("xpath", "//span[contains(text(),'新建')]/ancestor::*[8]/descendant::*[1]/descendant::*[27]")
			sleep(1)

			# 选择开户
			# 用JS方便点击‘申请’按钮旁边的倒三角形
			js_click("xpath", "//span[text()='维护']/parent::*/following-sibling::*/child::*")
			sleep(1)

			# 点击开户按钮
			js_click("xpath", "//a[contains(text(),'开户')]")
			sleep(1)

			# 选择开户日期
			today = date.today()
			open_date = today - timedelta(days=20)
			click("xpath", "//input[@id='openeddatewin-input']")
			sleep(1)
			clear("xpath", "//input[@id='openeddatewin-input']")
			sleep(1)
			input("xpath", "//input[@id='openeddatewin-input']", str(open_date))
			time.sleep(1)

			# 填写初始余额
			click("xpath", "//input[@id='initbalance-input']")
			sleep(1)
			clear("xpath", "//input[@id='initbalance-input']")
			sleep(1)
			input("xpath", "//input[@id='initbalance-input']", "30000")
			sleep(1)

			click("xpath", "//div[text()='确定']")
			sleep(1)

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("内部账户，开户成功！")
			logging.info("内部账户，开户成功！")
			time.sleep(3)

			# 再次切到内部借款管理模块完成生成交易单功能
			# 先退出所有iframe窗体
			switch_default()

			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='内部账户管理']/child::*[1]")

			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//span[@title='资金池内部计价']")

			# 打印操作成功日志
			print("退出内部账户管理页面成功")
			logging.info("退出内部账户管理页面成功")
			time.sleep(2)

			logging.info("开始测试回款登记生成交易单功能")
			# 将页面的滚动条滑动到‘资金结算管理’页面的地方
			js_gd("xpath", "//span[contains(text(),'内部借款管理')]")
			# 用JS的方法点击资金结算管理菜单按钮
			js_click("xpath", "//span[contains(text(),'内部借款管理')]")

			# # 点击借出方管理菜单
			# click("xpath", "//span[@title='借出方管理']")
			# sleep(1)
			# # 点击回款登记菜单
			# click("xpath", "//span[@title='回款登记']")
			# sleep(1)

			# 退出所有的iframe窗体
			switch_default()

			# 切入‘回款登记’的iframe窗体
			switch_to("xpath", "//iframe[@id='lendingsrepayment-tab-iframe']")

			# 查询条件里增加过滤条件
			# 用JS的方法点击放大镜
			js_click("xpath", "//span[@class='f-contrac-close']")
			sleep(1)

			# 选择已审批、未生成交易单的数据来生成交易单
			click("xpath", "//input[@id='combobox-input-approvestate']")
			sleep(1)
			click("xpath", "//div[@title='已审批']")
			sleep(1)

			# 点击查询
			click("xpath", "//span[text()='查询']")

			# 勾选
			click("xpath", "//div[@title='生成交易单状态:未生成']/parent::*/preceding-sibling::*[11]/descendant::*[2]")
			sleep(1)

			# 点击生成交易单
			click("xpath", "//span[text()='生成交易单']")

			# 切入回款登记生成交易单的窗体
			switch_to("xpath", "//iframe[@id='lendGenRecWin-iframe']")
			sleep(1)

			# 选择下一步
			click("xpath", "//span[text()='下一步']")
			sleep(1)

			switch_default()

			# 切入‘回款登记’的iframe窗体
			switch_to("xpath", "//iframe[@id='lendingsrepayment-tab-iframe']")
			sleep(1)

			switch_to("xpath", "//iframe[@id='addPayWin-iframe']")
			sleep(1)

			# 选择交易类型
			click("xpath", "//input[@id='combobox-input-paytypeid']")
			sleep(1)
			clear("xpath", "//input[@id='combobox-input-paytypeid']")
			sleep(1)
			input_down("xpath", "//input[@id='combobox-input-paytypeid']")
			input_enter("xpath", "//input[@id='combobox-input-paytypeid']")
			time.sleep(1)

			# 结算方式
			click("xpath", "//input[@id='combobox-input-settlementmodeid']")
			sleep(1)
			clear("xpath", "//input[@id='combobox-input-settlementmodeid']")
			sleep(1)
			input_down("xpath", "//input[@id='combobox-input-settlementmodeid']")
			input_enter("xpath", "//input[@id='combobox-input-settlementmodeid']")
			time.sleep(1)

			# 选择内部账户池
			click("xpath", "//input[@id='combobox-input-accountpoolid']")
			sleep(1)
			click("xpath", "//div[contains(text(),'Test_AccountPool')]")
			sleep(1)

			# 付方内部账户
			click("xpath", "//input[@id='combobox-input-ourinternalaccountid']")
			sleep(1)
			input_down("xpath", "//input[@id='combobox-input-ourinternalaccountid']")
			sleep(1)
			input_enter("xpath", "//input[@id='combobox-input-ourinternalaccountid']")
			time.sleep(1)

			# 收方内部账户
			click("xpath", "//input[@id='combobox-input-oppinternalaccountid']")
			sleep(1)
			input_down("xpath", "//input[@id='combobox-input-oppinternalaccountid']")
			sleep(1)
			input_down("xpath", "//input[@id='combobox-input-oppinternalaccountid']")
			sleep(1)
			input_enter("xpath", "//input[@id='combobox-input-oppinternalaccountid']")
			time.sleep(1)

			# 资金类别
			click("xpath", "//input[@id='combobox-input-capitalcategoryid']")
			# input("xpath", "//input[@id='combobox-input-capitalcategoryid']", "其他")
			input_down("xpath", "//input[@id='combobox-input-capitalcategoryid']")
			input_enter("xpath", "//input[@id='combobox-input-capitalcategoryid']")
			time.sleep(1)

			# 现金流量项目
			click("xpath", "//input[@id='combobox-input-cashflowitemid']")
			# input("xpath", "//input[@id='combobox-input-cashflowitemid']", "对外投资等到活动所支付的现金")
			input_down("xpath", "//input[@id='combobox-input-cashflowitemid']")
			input_enter("xpath", "//input[@id='combobox-input-cashflowitemid']")
			time.sleep(1)

			# 点击确认保存
			click("xpath", "//span[text()='保存']")

			# 退出所有的iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("回款登记，生成交易单保存成功！")
			sleep(3)

			# 按计划回款
			# 切入‘回款登记’的iframe窗体
			switch_to("xpath", "//iframe[@id='lendingsrepayment-tab-iframe']")

			# 用JS方便点击‘回款’按钮旁边的倒三角形
			js_click("xpath", "//span[text()='回款']/parent::*/following-sibling::*/child::*")
			sleep(1)

			# 点击开户按钮
			js_click("xpath", "//a[contains(text(),'按计划回款')]")
			sleep(1)

			switch_to("xpath", "//iframe[@id='modWin-iframe']")

			# 勾选
			click("xpath", "//div[@title='借入组织:002001-Mindy科技有限公司']/parent::*/preceding-sibling::*[6]/descendant::*[2]")
			sleep(1)

			# 点击确认回款按钮
			click("xpath", "//span[text()='确认回款']")
			sleep(1)

			switch_default()

			# 切入‘回款登记’的iframe窗体
			switch_to("xpath", "//iframe[@id='lendingsrepayment-tab-iframe']")

			switch_to("xpath", "//iframe[@id='modWin-iframe']")

			# 输入回款日期
			# 点击回款日期的日历按钮
			js_click("xpath", "//span[@id='repaydate-trigger']")
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

			# 切入回款登记的iframe窗体
			switch_to("xpath", "//iframe[@id='lendingsrepayment-tab-iframe']")

			# 进入确认回款的窗体
			switch_to("xpath", "//iframe[@id='modWin-iframe']")

			# 回款金额
			clear("xpath", "//input[@id='principal-input']")
			sleep(1)
			input("xpath", "//input[@id='principal-input']", "3000")
			sleep(1)

			# 点击保存按钮
			click("xpath", "//span[text()='保存']")

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("回款登记，按计划回款成功！")
			logging.info("回款登记，按计划回款成功！")
			time.sleep(3)

			# 切入‘回款登记’的iframe窗体
			switch_to("xpath", "//iframe[@id='lendingsrepayment-tab-iframe']")

			# # 选择已审批、未生成交易单的数据来生成交易单
			click("xpath", "//input[@id='combobox-input-approvestate']")
			sleep(1)
			click("xpath", "//div[@title='已审批']")
			sleep(1)
			click("xpath", "//div[@title='未审批']")
			sleep(1)

			# 点击查询
			click("xpath", "//span[text()='查询']")

			# 勾选
			click("xpath", "//div[@title='生成交易单状态:未生成']/parent::*/preceding-sibling::*[11]/descendant::*[2]")
			sleep(1)

			click("xpath", "//span[text()='删除']")

			# 点击弹出框的OK键
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
			sleep(1)

			# 退出所有的iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'删除成功:1笔!失败:0笔!')]")
			print("回款登记，删除成功！")
			sleep(3)

			# 切入‘回款登记’的iframe窗体
			switch_to("xpath", "//iframe[@id='lendingsrepayment-tab-iframe']")

			# 勾选
			click("xpath", "//div[@title='生成交易单状态:未生成']/parent::*/preceding-sibling::*[11]/descendant::*[2]")
			sleep(1)

			# 点击审核
			click("xpath", "//span[text()='审核']")
			sleep(1)

			# 点击弹出框的OK键
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
			sleep(1)

			# 退出所有的iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功!审核成功1笔，失败0笔')]")
			print("回款登记，审核成功！")
			sleep(3)

			# 切入‘回款登记’的iframe窗体
			switch_to("xpath", "//iframe[@id='lendingsrepayment-tab-iframe']")

			# 选择已审批、未生成交易单的数据来生成交易单
			click("xpath", "//input[@id='combobox-input-approvestate']")
			sleep(1)
			click("xpath", "//div[@title='未审批']")
			click("xpath", "//div[@title='已审批']")
			sleep(1)

			# 点击查询
			click("xpath", "//span[text()='查询']")

			# 勾选
			click("xpath", "//div[@title='生成交易单状态:未生成']/parent::*/preceding-sibling::*[11]/descendant::*[2]")
			sleep(1)

			click("xpath", "//span[text()='作废']")

			# 点击弹出框的OK键
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
			sleep(1)

			# 退出所有的iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'成功条数:1')]")
			print("回款登记，作废成功！")
			sleep(3)

			# 退出所有iframe窗体
			switch_default()

			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='回款登记']/child::*[1]")

			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//span[@title='借出方管理']")

			# 打印操作成功日志
			print("回款登记，操作成功!")
			logging.info("回款登记，操作成功!")
			time.sleep(2)

		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("回款登记,失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)

		# 借入合同登记
		# 测试内部借款管理--借入方管理
		try:
			# 点击借入方管理菜单
			click("xpath", "//span[@title='借入方管理']")
			# 点击借入合同登记菜单
			click("xpath", "//span[@title='借入合同登记']")
			# 退出所有的iframe窗体
			switch_default()

			logging.info("开始测试借入合同登记功能")
			for i in range(1, 4):
				# 切入‘借入合同登记’的iframe窗体
				switch_to("xpath", "//iframe[@id='loancontract-tab-iframe']")

				# 用JS的方法点击新增按钮
				js_click("xpath", "//span[text()='新增']")

				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='addWin-iframe']")
				sleep(1)

				# 借出组织
				click("xpath", "//input[@id='combobox-input-opporgid']")
				sleep(1)
				input("xpath", "//input[@id='combobox-input-opporgid']", "Mindy科技有限公司")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-opporgid']")
				input_enter("xpath", "//input[@id='combobox-input-opporgid']")
				sleep(1)

				# 借款类型
				click("xpath", "//input[@id='combobox-input-loantype']")
				sleep(1)
				# input("xpath", "//input[@id='combobox-input-loantype']", "一般借款")
				# sleep(1)
				input_down("xpath", "//input[@id='combobox-input-loantype']")
				sleep(1)
				input_enter("xpath", "//input[@id='combobox-input-loantype']")
				sleep(1)

				# 借款方式
				click("xpath", "//input[@id='combobox-input-loanmode']")
				sleep(1)
				input("xpath", "//input[@id='combobox-input-loanmode']", "现金")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-loanmode']")
				input_enter("xpath", "//input[@id='combobox-input-loanmode']")
				sleep(1)

				# 工程项目
				click("xpath", "//input[@id='combobox-input-projectitemid']")
				sleep(1)
				input("xpath", "//input[@id='combobox-input-projectitemid']", "自动化测试工程项目")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-projectitemid']")
				input_enter("xpath", "//input[@id='combobox-input-projectitemid']")
				sleep(1)

				# 合同编号
				temp1 = time.strftime("%H%M%S")
				# 合同编号
				input("xpath", "//input[@id='contractcode']", "ZDHLCHTH" + str(temp1))
				sleep(1)

				# 合同签订日
				today = date.today()
				sign_date = today - timedelta(days=20)
				click("xpath", "//input[@id='signeddate-input']")
				sleep(1)
				clear("xpath", "//input[@id='signeddate-input']")
				sleep(1)
				input("xpath", "//input[@id='signeddate-input']", str(sign_date))
				# 模拟回车键
				# keyDown('enter')
				# keyUp('enter')
				time.sleep(1)

				# 合同起始日
				today = date.today()
				sign_date = today - timedelta(days=20)
				click("xpath", "//input[@id='begindate-input']")
				sleep(1)
				clear("xpath", "//input[@id='begindate-input']")
				sleep(1)
				input("xpath", "//input[@id='begindate-input']", str(sign_date))
				# 模拟回车键
				# keyDown('enter')
				# keyUp('enter')
				time.sleep(1)

				# 合同到期日
				today = date.today()
				end_date = today + timedelta(days=20)
				click("xpath", "//input[@id='enddate-input']")
				sleep(1)
				clear("xpath", "//input[@id='enddate-input']")
				sleep(1)
				input("xpath", "//input[@id='enddate-input']", str(end_date))
				# 模拟回车键
				# keyDown('enter')
				# keyUp('enter')
				time.sleep(1)

				# 合同期限日
				input("xpath", "//input[@id='loantermday-input']", "40")
				sleep(1)

				# 币种
				click("xpath", "//input[@id='combobox-input-currencyid']")
				sleep(1)
				input("xpath", "//input[@id='combobox-input-currencyid']", "人民币")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-currencyid']")
				input_enter("xpath", "//input[@id='combobox-input-currencyid']")
				sleep(1)

				# 金额
				click("xpath", "//input[@id='amount-input']")
				sleep(1)
				# 清空内容
				clear("xpath", "//input[@id='amount-input']")
				sleep(1)
				# 输入金额
				input("xpath", "//input[@id='amount-input']", "100000")
				sleep(1)

				# 借款经办人
				input("xpath", "//input[@id='loanoperator']", "田遍地")
				sleep(1)

				# 费率
				click("xpath", "//input[@id='feerate-input']")
				sleep(1)
				# 清空内容
				clear("xpath", "//input[@id='feerate-input']")
				sleep(1)
				# 输入金额
				input("xpath", "//input[@id='feerate-input']", "30")
				sleep(1)

				# 计息开始日期
				today = date.today()
				start_date = today + timedelta(days=20)
				click("xpath", "//input[@id='intereststartdate-input']")
				sleep(1)
				clear("xpath", "//input[@id='intereststartdate-input']")
				sleep(1)
				input("xpath", "//input[@id='intereststartdate-input']", str(start_date))
				time.sleep(1)

				# 点击输入用途
				click("xpath", "//textarea[@id='abstracts']")
				sleep(1)
				input("xpath", "//textarea[@id='abstracts']", "自动化测试借出合同输入用途")
				sleep(1)

				# 计息方式中输入值
				# 点击计息方式插页
				# 1、选择还本方式
				click("xpath", "//input[@id='combobox-input-repaymode']")
				# 按键往下，选择‘按季还款’
				input_down("xpath", "//input[@id='combobox-input-repaymode']")
				input_enter("xpath", "//input[@id='combobox-input-repaymode']")
				time.sleep(1)

				# 2、选择计息方式
				click("xpath", "//input[@id='combobox-input-interestmode']")
				# 按键往下，选择利率方案
				sleep(2)
				input_down("xpath", "//input[@id='combobox-input-interestmode']")
				input_enter("xpath", "//input[@id='combobox-input-interestmode']")
				sleep(1)

				# 3、选择利率方案
				click("xpath", "//input[@id='combobox-input-interestrateschemeid']")
				# 按键往下，选择利率方案
				sleep(2)
				input_down("xpath", "//input[@id='combobox-input-interestrateschemeid']")
				input_enter("xpath", "//input[@id='combobox-input-interestrateschemeid']")
				sleep(1)

				# 4、选择浮动方式
				click("xpath", "//input[@id='combobox-input-interestratefloattype']")
				# 按键往下，选择利率方案
				sleep(2)
				input_down("xpath", "//input[@id='combobox-input-interestratefloattype']")
				input_enter("xpath", "//input[@id='combobox-input-interestratefloattype']")
				sleep(1)

				# 点击保存按钮
				click("xpath", "//span[text()='保存']")

				# 退出所有iframe窗体
				switch_default()

				# 用隐式等待方法等页面出现提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				print("借入合同第%s次新增成功" % i)
				logging.info("借入合同第%s次新增成功" % i)
				time.sleep(3)

				# 第一笔，就先修改，再删除新建的‘借入合同’
				if i == 1:
					# 切入‘借入合同’的iframe窗体
					switch_to("xpath", "//iframe[@id='loancontract-tab-iframe']")

					# 点击查看
					# 用JS的方法点击放大镜
					js_click("xpath", "//span[@class='f-contrac-close']")
					sleep(1)

					# 合同号查询
					input("xpath", "//input[@id='contractcode']", "ZDHLCHTH")
					sleep(1)

					# 点击查询
					click("xpath", "//span[text()='查询']")

					# 修改 # 勾选
					click("xpath", "//div[@title='借出单位:002001-Mindy科技有限公司']/parent::*/preceding-sibling::*[3]/descendant::*[2]")

					# 点击修改按钮
					click("xpath", "//span[text()='修改']")
					sleep(1)

					# 切入修改的iframe窗体
					switch_to("xpath", "//iframe[@id='modWin-iframe']")
					print("进入修改窗体")
					sleep(1)

					# 描述abstracts
					input("xpath", "//textarea[@id='abstracts']", "自动化测试借入合同备注框")
					sleep(1)

					# 备注框中输入新内容
					input("xpath", "//textarea[@id='description']", "自动化测试借入合同修改备注框")
					sleep(1)

					# 点击保存按钮
					click("xpath", "//span[text()='保存']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("借入合同，修改成功！")
					logging.info("借入合同，修改成功！")
					time.sleep(3)

					# 第一次审核
					# 切入‘借入合同登记’的iframe窗体
					switch_to("xpath", "//iframe[@id='loancontract-tab-iframe']")

					# 勾选
					click("xpath", "//div[@title='借出单位:002001-Mindy科技有限公司']/parent::*/preceding-sibling::*[3]/descendant::*[2]")

					# 点击审核按钮
					click("xpath", "//span[text()='审核']")

					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'成功审核1条记录')]")
					print("借入合同登记，第一次审批成功！")
					logging.info("借入合同登记，第一次审批成功！")
					time.sleep(3)

					# 切入‘借入合同登记’的iframe窗体
					switch_to("xpath", "//iframe[@id='loancontract-tab-iframe']")

					# 勾选
					click("xpath", "//div[@title='借出单位:002001-Mindy科技有限公司']/parent::*/preceding-sibling::*[3]/descendant::*[2]")

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
					implici_wait("xpath", "//span[contains(text(),'成功取消审核:1条')]")
					print("借入合同登记，取消审核成功！")
					logging.info("借入合同登记，取消审核成功！")
					time.sleep(3)

					# 切入‘借入合同登记’的iframe窗体
					switch_to("xpath", "//iframe[@id='loancontract-tab-iframe']")

					# 勾选
					click("xpath", "//div[@title='借出单位:002001-Mindy科技有限公司']/parent::*/preceding-sibling::*[3]/descendant::*[2]")

					# 点击删除按钮
					click("xpath", "//span[text()='删除']")

					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现删除的提示框
					implici_wait("xpath", "//span[contains(text(),'成功删除1条记录！')]")
					print("借入合同登记，删除成功！")
					logging.info("借入合同登记，删除成功！")
					time.sleep(3)

				# 第二笔，先审核、再继承、再放款、再回款、再利息登记
				elif i == 2:

					# 第二次审核
					# 切入‘借入合同登记’的iframe窗体
					switch_to("xpath", "//iframe[@id='loancontract-tab-iframe']")

					# 勾选
					click("xpath", "//div[@title='借出单位:002001-Mindy科技有限公司']/parent::*/preceding-sibling::*[3]/descendant::*[2]")

					# 点击审核按钮
					click("xpath", "//span[text()='审核']")

					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'成功审核1条记录')]")
					print("借入合同登记，第二次审批成功！")
					logging.info("借入合同登记，第二次审批成功！")
					time.sleep(3)

					# 借入合同放款申请
					# 切入‘借入合同登记’的iframe窗体
					switch_to("xpath", "//iframe[@id='loancontract-tab-iframe']")

					# 勾选
					click("xpath", "//div[@title='借出单位:002001-Mindy科技有限公司']/parent::*/preceding-sibling::*[3]/descendant::*[2]")

					# 点击取消审核按钮
					click("xpath", "//span[text()='提款']")
					sleep(1)

					switch_to("xpath", "//iframe[@id='lendPayWin-iframe']")

					# 输入提款日期
					# 点击提款日期的日历按钮
					js_click("xpath", "//span[@id='lenddate-trigger']")
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

					# 切入‘借出登记登记’的iframe窗体
					switch_to("xpath", "//iframe[@id='loancontract-tab-iframe']")
					# 切入新增的iframe窗体
					switch_to("xpath", "//iframe[@id='lendPayWin-iframe']")

					# 提款金额
					input("xpath", "//input[@id='amount-input']", "3000")
					sleep(1)

					# 提款账号
					click("xpath", "//input[@id='combobox-input-ourbankaccountid']")
					input_down("xpath", "//input[@id='combobox-input-ourbankaccountid']")
					sleep(1)
					input_enter("xpath", "//input[@id='combobox-input-ourbankaccountid']")
					time.sleep(1)

					# 点击保存按钮
					click("xpath", "//span[text()='保存']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("借入合同登记，申请提款成功！")
					logging.info("借入合同登记，申请提款成功！")
					time.sleep(3)

					# 退出所有iframe窗体

					switch_default()

					# 用JS的方法关闭当前页面
					js_click("xpath", "//a[@title='借入合同登记']/child::*[1]")

					# 点击理财合同登记菜单
					click("xpath", "//span[@title='提款登记']")

					# 退出所有的iframe窗体
					switch_default()

					logging.info("开始测试提款登记功能")

					# 切入‘提款登记’的iframe窗体
					switch_to("xpath", "//iframe[@id='loanlends-tab-iframe']")

					# # 点击提款按钮
					# click("xpath", "//span[text()='提款']")
					#
					# switch_to("xpath", "//iframe[@id='modWin-iframe']")
					#
					# 勾选
					click("xpath", "//div[@title='借出单位:002001-Mindy科技有限公司']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
					sleep(1)

					# 点击审核按钮
					click("xpath", "//span[text()='审核']")

					# 点击弹出框的OK键操作成功!审核成功1笔，失败0笔
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					sleep(1)

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功!审核成功1笔，失败0笔')]")
					print("借入合同登记，放款成功！")
					logging.info("借入合同登记，提款成功！")
					time.sleep(3)

					# 退出所有iframe窗体
					switch_default()

					# 用JS的方法关闭当前页面
					js_click("xpath", "//a[@title='提款登记']/child::*[1]")

					# 点击理财合同登记菜单
					click("xpath", "//span[@title='借入合同登记']")

					# 切入‘借入合同登记’的iframe窗体
					switch_to("xpath", "//iframe[@id='loancontract-tab-iframe']")

					# 用JS的方法点击高级查询按钮
					js_click("xpath", "//span[text()='高级查询']")

					click("xpath", "//input[@id='combobox-input-property_0']")
					sleep(1)
					clear("xpath", "//input[@id='combobox-input-property_0']")
					sleep(1)
					# 输入作废状态，通过模糊匹配搜索
					input("xpath", "//input[@id='combobox-input-property_0']", "合同编号")
					sleep(1)
					# 模拟回车
					click("xpath", "//div[contains(text(),'合同编号')]")
					sleep(1)

					click("xpath", "//input[@id='combobox-input-condition_0']")
					sleep(1)
					# 输入作废状态，通过模糊匹配搜索
					input("xpath", "//input[@id='combobox-input-condition_0']", "模糊")
					sleep(1)
					# 模拟回车
					click("xpath", "//div[contains(text(),'模糊')]")
					sleep(1)

					click("xpath", "//input[@id='value_0']")
					sleep(1)
					# 输入作废状态，通过模糊匹配搜索
					input("xpath", "//input[@id='value_0']", "ZDHLCHTH")
					sleep(1)
					# 模拟回车
					click("xpath", "//div[contains(text(),'ZDHLCHTH')]")
					sleep(1)

					# 放款状态
					click("xpath", "//input[@id='combobox-input-property_1']")
					sleep(1)
					clear("xpath", "//input[@id='combobox-input-property_1']")
					sleep(1)
					# 输入作废状态，通过模糊匹配搜索
					input("xpath", "//input[@id='combobox-input-property_1']", "提款状态")
					sleep(1)
					# 模拟回车
					click("xpath", "//div[contains(text(),'提款状态')]")
					sleep(1)

					click("xpath", "//input[@id='combobox-input-condition_1']")
					sleep(1)
					# 输入作废状态，通过模糊匹配搜索
					input("xpath", "//input[@id='combobox-input-condition_1']", "包含")
					sleep(1)
					# 模拟回车
					click("xpath", "//div[contains(text(),'包含')]")
					sleep(1)

					click("xpath", "//input[@id='combobox-input-value_1']")
					sleep(1)
					# 输入放款状态，通过模糊匹配搜索
					click("xpath", "//div[contains(text(),'全部提款')]/preceding-sibling::*[1]")
					sleep(1)

					click("xpath", "//div[contains(text(),'部分提款')]/preceding-sibling::*[1]")
					sleep(1)

					click("xpath", "//div[contains(text(),'查询')]")
					sleep(1)

					js_click("xpath", "//span[text()='自定义查询']/preceding-sibling::*[1]")
					sleep(1)

					# 勾选
					click("xpath", "//div[@title='借出单位:002001-Mindy科技有限公司']/parent::*/preceding-sibling::*[3]/descendant::*[2]")

					# 点击保存按钮
					click("xpath", "//span[text()='还款']")
					sleep(1)

					# 进入还款窗体
					switch_to("xpath", "//iframe[@id='lendPayWin-iframe']")
					sleep(1)

					# 输入还款日期
					# 点击还款日期的日历按钮
					js_click("xpath", "//span[@id='repaydate-trigger']")
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

					# 切入‘借入合同登记’的iframe窗体
					switch_to("xpath", "//iframe[@id='loancontract-tab-iframe']")

					# 进入还款的窗体
					switch_to("xpath", "//iframe[@id='lendPayWin-iframe']")

					# 还款金额
					click("xpath", "//input[@id='principal-input']")
					sleep(1)
					clear("xpath", "//input[@id='principal-input']")
					sleep(1)
					input("xpath", "//input[@id='principal-input']", "3000")
					sleep(1)

					# 点击保存按钮
					click("xpath", "//span[text()='保存']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("借入合同登记，还款成功！")
					logging.info("借入合同登记，还款成功！")
					time.sleep(3)

					# 利息登记
					# 切入‘借入合同登记’的iframe窗体
					switch_to("xpath", "//iframe[@id='loancontract-tab-iframe']")

					click("xpath", "//div[@title='借出单位:002001-Mindy科技有限公司']/parent::*/preceding-sibling::*[3]/descendant::*[2]")

					# 点击保存按钮
					click("xpath", "//span[text()='利息登记']")
					sleep(1)

					# 进入利息登记的窗体
					switch_to("xpath", "//iframe[@id='lendPayWin-iframe']")
					sleep(1)

					# 输入还款日期
					today = date.today()
					repay_date = today
					click("xpath", "//input[@id='repaydate-input']")
					sleep(1)
					clear("xpath", "//input[@id='repaydate-input']")
					sleep(1)
					input("xpath", "//input[@id='repaydate-input']", str(repay_date))
					# 模拟回车键
					keyDown('enter')
					keyUp('enter')
					time.sleep(2)

					# 还息金额
					click("xpath", "//input[@id='interest-input']")
					sleep(1)
					clear("xpath", "//input[@id='interest-input']")
					sleep(1)
					input("xpath", "//input[@id='interest-input']", "3000")
					sleep(1)

					# 点击保存按钮
					click("xpath", "//span[text()='保存']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("借入合同登记，利息登记成功！")
					logging.info("借入合同登记，利息登记成功！")
					time.sleep(3)

					# 应还利息
					# 切入‘借入合同登记’的iframe窗体
					switch_to("xpath", "//iframe[@id='loancontract-tab-iframe']")

					click("xpath", "//div[@title='借出单位:002001-Mindy科技有限公司']/parent::*/preceding-sibling::*[3]/descendant::*[2]")

					# 点击保存按钮
					click("xpath", "//span[text()='应还利息']")
					sleep(1)

					# 进入应还利息的窗体
					switch_to("xpath", "//iframe[@id='lendPayWin-iframe']")
					sleep(1)

					# 点击试算按钮
					click("xpath", "//span[text()='试算']")
					sleep(1)

					# 点击取消按钮
					click("xpath", "//span[text()='取消']")
					sleep(1)

					# 退出所有iframe窗体
					switch_default()

					# 打印成功日志
					print("借入合同登记，应还利息成功！")
					logging.info("借入合同登记，应还利息成功！")
					time.sleep(3)

					# 重新生成还款计息计划
					# 切入‘借入合同登记’的iframe窗体
					switch_to("xpath", "//iframe[@id='loancontract-tab-iframe']")

					# 勾选数据
					# click("xpath", "//div[@title='借出单位:002001-Mindy科技有限公司']/parent::*/preceding-sibling::*[3]/descendant::*[2]")

					# 点击重新生成还款计息计划按钮
					click("xpath", "//span[text()='重新生成还款计息计划']")

					# 点击确认按钮
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'成功重新计息:1条！')]")
					print("借入合同登记，重新生成还款计息计划成功！")
					logging.info("借入合同登记，重新生成还款计息计划成功！")
					time.sleep(3)

				# 第三笔，作废
				elif i == 3:

					# 第三次审核
					# 切入‘借入合同登记’的iframe窗体
					switch_to("xpath", "//iframe[@id='loancontract-tab-iframe']")

					# 勾选
					click("xpath", "//div[@title='借出单位:002001-Mindy科技有限公司']/parent::*/preceding-sibling::*[3]/descendant::*[2]")

					# 点击审核按钮
					click("xpath", "//span[text()='审核']")

					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'成功审核1条记录')]")
					print("借入合同登记，第三次审批成功！")
					logging.info("借入合同登记，第三次审批成功！")
					time.sleep(3)

					# 变更
					# 切入‘借入合同登记’的iframe窗体
					switch_to("xpath", "//iframe[@id='loancontract-tab-iframe']")

					click("xpath", "//div[@title='借出单位:002001-Mindy科技有限公司']/parent::*/preceding-sibling::*[3]/descendant::*[2]")

					# 点击变更按钮
					click("xpath", "//span[text()='变更']")
					sleep(1)

					# 切入变更的iframe窗体
					switch_to("xpath", "//iframe[@id='modWin-iframe']")
					print("进入变更窗体")
					sleep(1)

					# 描述abstracts
					input("xpath", "//textarea[@id='abstracts']", "自动化测试借入合同备注框")
					sleep(1)

					# 备注框中输入新内容
					input("xpath", "//textarea[@id='description']", "自动化测试借入合同变更备注框")
					sleep(1)

					# 点击保存按钮
					click("xpath", "//span[text()='保存']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("借入合同，变更成功！")
					logging.info("借入合同，变更成功！")
					time.sleep(3)

					# 作废	# 切入‘借入合同登记’的iframe窗体
					switch_to("xpath", "//iframe[@id='loancontract-tab-iframe']")
					# 勾选
					click("xpath", "//div[@title='借出单位:002001-Mindy科技有限公司']/parent::*/preceding-sibling::*[3]/descendant::*[2]")

					# 点击作废按钮
					click("xpath", "//span[text()='作废']")

					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'成功作废1条记录！')]")
					print("借入合同登记，作废成功！")
					logging.info("借入合同登记，作废成功！")
					time.sleep(3)

			# 退出所有iframe窗体
			switch_default()

			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='借入合同登记']/child::*[1]")

			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//span[@title='借出方管理']")

			# 打印操作成功日志
			print("借入合同登记，操作成功!")
			logging.info("借入合同登记，操作成功!")
			time.sleep(2)
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("借入合同登记,失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		
		# 测试内部借款管理--提款登记
		try:
			# 点击借出方管理菜单
			click("xpath", "//span[@title='借入方管理']")
			# 点击提款登记菜单
			click("xpath", "//span[@title='提款登记']")
			
			# 退出所有的iframe窗体
			switch_default()
			
			logging.info("开始测试提款登记功能")
			
			# 切入‘提款登记’的iframe窗体
			switch_to("xpath", "//iframe[@id='loanlends-tab-iframe']")
			sleep(1)
			
			# 点击提款按钮
			click("xpath", "//span[text()='提款']")
			
			switch_to("xpath", "//iframe[@id='modWin-iframe']")
			
			# 勾选
			click("xpath", "//div[@title='借出单位:002001-Mindy科技有限公司']/parent::*/preceding-sibling::*[3]/descendant::*[2]")
			sleep(1)
			
			# 点击确认提款按钮
			click("xpath", "//span[text()='确认提款']")
			sleep(1)
			
			switch_default()
			
			# 切入‘提款登记’的iframe窗体
			switch_to("xpath", "//iframe[@id='loanlends-tab-iframe']")
			
			switch_to("xpath", "//iframe[@id='modWin-iframe']")
			
			# 输入提款日期
			# 点击提款日期的日历按钮
			js_click("xpath", "//span[@id='lenddate-trigger']")
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
			
			# 切入提款登记的iframe窗体
			switch_to("xpath", "//iframe[@id='loanlends-tab-iframe']")
			
			# 进入确认提款的窗体
			switch_to("xpath", "//iframe[@id='modWin-iframe']")
			
			# 提款金额
			clear("xpath", "//input[@id='amount-input']")
			sleep(1)
			input("xpath", "//input[@id='amount-input']", "3000")
			sleep(1)
			
			# 点击保存按钮
			click("xpath", "//span[text()='保存']")
			
			# 退出所有iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("提款登记，提款成功！")
			logging.info("提款登记，提款成功！")
			time.sleep(3)
			
			# 切入‘提款登记’的iframe窗体
			switch_to("xpath", "//iframe[@id='loanlends-tab-iframe']")
			# 点击
			# 勾选
			click("xpath", "//div[@title='审批状态:未审批']/parent::*/preceding-sibling::*[8]/descendant::*[2]")
			sleep(1)
			
			# 点击审核
			click("xpath", "//span[text()='审核']")
			sleep(1)
			
			# 点击弹出框的OK键
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
			sleep(1)
			
			# 退出所有的iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功!审核成功1笔，失败0笔')]")
			print("提款登记，审核成功！")
			sleep(3)
			
			# 切入‘提款登记’的iframe窗体
			switch_to("xpath", "//iframe[@id='loanlends-tab-iframe']")
			
			# 勾选
			click("xpath", "//div[@title='审批状态:已审批']/parent::*/preceding-sibling::*[8]/descendant::*[2]")
			sleep(1)
			
			# 用JS方便点击‘审核’按钮旁边的倒三角形
			js_click("xpath", "//span[text()='审核']/parent::*/following-sibling::*/child::*")
			sleep(1)
			
			# 点击取消送审按钮
			js_click("xpath", "//a[contains(text(),'取消审核')]")
			sleep(1)
			
			# 点击弹出框的OK键
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
			sleep(1)
			
			# 退出所有的iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("提款登记，取消审核成功！")
			sleep(3)
			
			# 切入‘提款登记’的iframe窗体
			switch_to("xpath", "//iframe[@id='loanlends-tab-iframe']")
			
			# 勾选
			click("xpath", "//div[@title='审批状态:未审批']/parent::*/preceding-sibling::*[8]/descendant::*[2]")
			sleep(1)
			
			# 点击审核
			click("xpath", "//span[text()='审核']")
			sleep(1)
			
			# 点击弹出框的OK键
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
			sleep(1)
			
			# 退出所有的iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功!审核成功1笔，失败0笔')]")
			print("提款登记，审核成功！")
			sleep(3)
			
			# 切入‘提款登记’的iframe窗体
			switch_to("xpath", "//iframe[@id='loanlends-tab-iframe']")
			
			# 勾选
			click("xpath", "//div[@title='审批状态:已审批']/parent::*/preceding-sibling::*[8]/descendant::*[2]")
			sleep(1)
			
			# 点击变更
			click("xpath", "//span[text()='变更']")
			sleep(1)
			
			switch_to("xpath", "//iframe[@id='modWin-iframe']")
			
			# 点击保存
			click("xpath", "//span[text()='保存']")
			sleep(1)
			
			# 退出所有iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("提款登记，变更成功！")
			logging.info("提款登记，变更成功！")
			time.sleep(3)
			
			# 切入‘提款登记’的iframe窗体
			switch_to("xpath", "//iframe[@id='loanlends-tab-iframe']")
			
			# 勾选
			click("xpath", "//div[@title='审批状态:未审批']/parent::*/preceding-sibling::*[8]/descendant::*[2]")
			sleep(1)
			
			# 点击审核
			click("xpath", "//span[text()='审核']")
			sleep(1)
			
			# 点击弹出框的OK键
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
			sleep(1)
			
			# 退出所有的iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功!审核成功1笔，失败0笔')]")
			print("提款登记，审核成功！")
			sleep(3)
			
			# 切入‘提款登记’的iframe窗体
			switch_to("xpath", "//iframe[@id='loanlends-tab-iframe']")
			
			# 查询条件里增加过滤条件
			# 用JS的方法点击放大镜
			js_click("xpath", "//span[@class='f-contrac-close']")
			sleep(1)
			
			# 选择已审批、未生成交易单的数据来生成交易单
			click("xpath", "//input[@id='combobox-input-approvestate']")
			sleep(1)
			click("xpath", "//div[@title='已审批']")
			sleep(1)
			
			# 点击查询
			click("xpath", "//span[text()='查询']")
			
			# 勾选
			click("xpath", "//div[text()='未生成']/parent::*/preceding-sibling::*[10]/descendant::*[2]")
			sleep(1)
			
			# 点击生成交易单
			click("xpath", "//span[text()='生成交易单']")
			
			# 切入提款登记生成交易单的窗体
			switch_to("xpath", "//iframe[@id='lendGenRecWin-iframe']")
			sleep(1)
			
			# 选择支付类型
			# 选择其他
			click("xpath", "//input[@id='combobox-input-dealtype']")
			sleep(1)
			clear("xpath", "//input[@id='combobox-input-dealtype']")
			sleep(1)
			input("xpath", "//input[@id='combobox-input-dealtype']", "其他")
			sleep(1)
			input_enter("xpath", "//input[@id='combobox-input-dealtype']")
			time.sleep(1)
			
			# 选择下一步
			click("xpath", "//span[text()='下一步']")
			sleep(1)
			
			switch_default()
			
			# 切入‘提款登记’的iframe窗体
			switch_to("xpath", "//iframe[@id='loanlends-tab-iframe']")
			sleep(1)
			
			switch_to("xpath", "//iframe[@id='addRecWin-iframe']")
			sleep(1)
			
			# 部门
			click("xpath", "//input[@id='combobox-input-deptid']")
			# 输入银行名称，模糊查询
			input("xpath", "//input[@id='combobox-input-deptid']", "自动化测试部")
			sleep(1)
			input_down("xpath", "//input[@id='combobox-input-deptid']")
			input_enter("xpath", "//input[@id='combobox-input-deptid']")
			time.sleep(1)
			
			# 选择交易类型
			click("xpath", "//input[@id='combobox-input-paytypeid']")
			sleep(1)
			clear("xpath", "//input[@id='combobox-input-paytypeid']")
			sleep(1)
			click("xpath", "//div[@title='交易类型:202-内部收款']")
			sleep(1)
			
			# 结算方式
			click("xpath", "//input[@id='combobox-input-settlementmodeid']")
			sleep(1)
			clear("xpath", "//input[@id='combobox-input-settlementmodeid']")
			sleep(1)
			input_down("xpath", "//input[@id='combobox-input-settlementmodeid']")
			input_enter("xpath", "//input[@id='combobox-input-settlementmodeid']")
			time.sleep(1)
			
			# 收方账户
			# 输入银行名称，模糊查询
			click("xpath", "//input[@id='combobox-input-ourbankaccountid']")
			input("xpath", "//input[@id='combobox-input-ourbankaccountid']", "中国银行")
			sleep(1)
			input_down("xpath", "//input[@id='combobox-input-ourbankaccountid']")
			input_enter("xpath", "//input[@id='combobox-input-ourbankaccountid']")
			time.sleep(1)
			
			# 付方组织
			click("xpath", "//input[@id='combobox-input-opporgid']")
			input("xpath", "//input[@id='combobox-input-opporgid']", "亚唐科技")
			sleep(1)
			input_down("xpath", "//input[@id='combobox-input-opporgid']")
			input_enter("xpath", "//input[@id='combobox-input-opporgid']")
			time.sleep(1)
			
			# 计划项目
			click("xpath", "//input[@id='combobox-input-budgetitemid']")
			# 输入银行名称，模糊查询
			input("xpath", "//input[@id='combobox-input-budgetitemid']", "自动化计划项目")
			sleep(1)
			input_down("xpath", "//input[@id='combobox-input-budgetitemid']")
			input_enter("xpath", "//input[@id='combobox-input-budgetitemid']")
			time.sleep(1)
			
			# 资金类别
			click("xpath", "//input[@id='combobox-input-capitalcategoryid']")
			input("xpath", "//input[@id='combobox-input-capitalcategoryid']", "其他")
			input_down("xpath", "//input[@id='combobox-input-capitalcategoryid']")
			input_enter("xpath", "//input[@id='combobox-input-capitalcategoryid']")
			time.sleep(1)
			
			# 现金流量项目
			click("xpath", "//input[@id='combobox-input-cashflowitemid']")
			input("xpath", "//input[@id='combobox-input-cashflowitemid']", "对外投资等到活动所支付的现金")
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
			
			# 描述框中填入值
			input("xpath", "//textarea[@id='description']", "自动化测试生成交易单描述框")
			sleep(1)
			
			# 点击确认保存
			click("xpath", "//span[text()='保存']")
			
			# 退出所有的iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("提款登记，生成交易单保存成功！")
			sleep(3)
			
			# 切入‘提款登记’的iframe窗体
			switch_to("xpath", "//iframe[@id='loanlends-tab-iframe']")
			
			# # 选择已审批、未生成交易单的数据来生成交易单
			click("xpath", "//input[@id='combobox-input-approvestate']")
			sleep(1)
			click("xpath", "//div[@title='已审批']")
			sleep(1)
			click("xpath", "//div[@title='未审批']")
			sleep(1)
			
			# 点击查询
			click("xpath", "//span[text()='查询']")
			
			# 勾选
			click("xpath", "//div[text()='未生成']/parent::*/preceding-sibling::*[10]/descendant::*[2]")
			sleep(1)
			
			click("xpath", "//span[text()='删除']")
			
			# 点击弹出框的OK键
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
			sleep(1)
			
			# 退出所有的iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'成功删除1条记录！')]")
			print("提款登记，删除成功！")
			sleep(3)
			
			# 切入‘提款登记’的iframe窗体
			switch_to("xpath", "//iframe[@id='loanlends-tab-iframe']")
			
			# 勾选
			click("xpath", "//div[text()='未生成']/parent::*/preceding-sibling::*[10]/descendant::*[2]")
			sleep(1)
			
			# 点击审核
			click("xpath", "//span[text()='审核']")
			sleep(1)
			
			# 点击弹出框的OK键
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
			sleep(1)
			
			# 退出所有的iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功!审核成功1笔，失败0笔')]")
			print("提款登记，审核成功！")
			sleep(3)
			
			# 切入‘提款登记’的iframe窗体
			switch_to("xpath", "//iframe[@id='loanlends-tab-iframe']")
			
			# 选择已审批、未生成交易单的数据来生成交易单
			click("xpath", "//input[@id='combobox-input-approvestate']")
			sleep(1)
			click("xpath", "//div[@title='未审批']")
			click("xpath", "//div[@title='已审批']")
			sleep(1)
			
			# 点击查询
			click("xpath", "//span[text()='查询']")
			
			# 勾选
			click("xpath", "//div[text()='未生成']/parent::*/preceding-sibling::*[10]/descendant::*[2]")
			sleep(1)
			
			click("xpath", "//span[text()='作废']")
			
			# 点击弹出框的OK键
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
			sleep(1)
			
			# 退出所有的iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'成功作废1条记录！')]")
			print("提款登记，作废成功！")
			sleep(3)
			
			# 退出所有iframe窗体
			switch_default()
			
			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='提款登记']/child::*[1]")
			
			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//span[@title='借出方管理']")
			
			# 打印操作成功日志
			print("提款登记，操作成功!")
			logging.info("提款登记，操作成功!")
			time.sleep(2)
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("提款登记,失败！" + str(traceback.format_exc()))
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
