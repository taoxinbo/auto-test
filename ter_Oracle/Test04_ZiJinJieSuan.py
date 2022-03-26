# encoding=utf-8
# @Time : 2020/8/14 14:49
# @Author : Mindy
# 此文件是测试资金结算模块，包括基础设置、备案信息管理
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
class Test_Zjjs(unittest.TestCase):
	
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
		#login(G_Ora_Url, mindy, Password, "默认租户")
		# login( G_Mys_Url,TestUser,Password, "自动化测试租户")
		# login(G_Mys_Url, Tao, Password, "默认租户")
		# login(G_Mys_Url, mindy, Password, "亚唐科技")
		# login(G_Mys_Url, judy, Password, "默认租户")
		
		logging.info("开始测试资金结算管理的页面功能")
		# 将页面的滚动条滑动到‘资金结算管理’页面的地方
		js_gd("xpath", "//span[contains(text(),'资金结算管理')]")
		# 用JS的方法点击资金结算管理菜单按钮
		js_click("xpath", "//span[contains(text(),'资金结算管理')]")
		
		# 测试基础设置--交易对手类别
		
		try:
			# 点击基础设置菜单
			click("xpath", "//li[@f_value='settlementSetting']/descendant-or-self::*[5]")
			# 点击支票用途菜单
			click("xpath", "//span[text()='交易对手类别']")
			# 退出所有iframe窗体
			switch_default()
			
			for i in range(1, 3):
				# 切入支票作废原因的iframe窗体
				switch_to("xpath", "//iframe[@id='counterpartycategroy-tab-iframe']")
				logging.info("开始测试交易对手类别功能")
				
				# 用JS的方法点击新增按钮
				js_click("xpath", "//span[text()='新增']")
				
				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='addWin-iframe']")
				sleep(1)
				
				# 输入交易对手类别代码
				input("xpath", "//input[@name='code']", "TestCat")
				sleep(1)
				
				# 输入交易对手类别名称
				input("xpath", "//input[@id='name']", "自动化测试交易对手类别")
				sleep(1)
				
				# 描述框中填入值
				input("xpath", "//textarea[@id='description']", "自动化测试交易对手类别描述框")
				sleep(1)
				
				# 点击保存按钮
				click("xpath", "//span[text()='保存']")
				
				# 退出所有iframe窗体
				switch_default()
				
				# 用隐式等待方法等页面出现新增成功的提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				print("交易对手类别，保存成功！")
				time.sleep(3)
				
				if i == 1:
					# 删除功能
					# 切入交易对手类别的iframe窗体
					switch_to("xpath", "//iframe[@id='counterpartycategroy-tab-iframe']")
					
					# 点击查看
					# 用JS的方法点击放大镜
					js_click("xpath", "//span[@class='f-contrac-close']")
					sleep(1)
					
					# 输入代码：
					input("xpath", "//input[@id='code']", "TestCat")
					sleep(1)
					
					# 点击查询
					click("xpath", "//span[text()='查询']")
					
					# 勾选
					click("xpath", "//div[@title='名称:自动化测试交易对手类别']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
					
					# 点击删除按钮
					click("xpath", "//span[text()='删除']")
					
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现删除的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功')]")
					print("交易对手类别，删除成功！")
					time.sleep(3)
			
			# 切入‘交易对手类别’的iframe窗体
			switch_to("xpath", "//iframe[@id='counterpartycategroy-tab-iframe']")
			
			# 点击查看
			# 清空代码框的内容
			clear("xpath", "//input[@id='code']")
			sleep(1)
			
			# 输入代码：
			input("xpath", "//input[@id='code']", "TestCat")
			sleep(1)
			
			# 点击查询
			click("xpath", "//span[text()='查询']")
			
			# 修改
			# 勾选
			click("xpath", "//div[@title='名称:自动化测试交易对手类别']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
			
			# 点击修改按钮
			click("xpath", "//span[text()='修改']")
			
			# 切入修改的iframe窗体
			switch_to("xpath", "//iframe[@id='modWin-iframe']")
			sleep(1)
			
			# 修改描述框中的内容
			input("xpath", "//textarea[@id='description']", "自动化测试交易对手类别修改")
			sleep(1)
			
			# 点击保存按钮
			click("xpath", "//span[text()='保存']")
			
			# 退出所有iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("交易对手类别，修改成功！")
			time.sleep(3)
			
			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='交易对手类别']/child::*[1]")
			
			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//li[@f_value='settlementSetting']/descendant-or-self::*[5]")
			
			# 打印操作成功日志
			print("交易对手类别，操作成功!")
			logging.info("交易对手类别，操作成功!")
			time.sleep(2)
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("交易对手类别打印失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		
		# 测试基础设置--交易对手评级
		try:
			# 点击基础设置菜单
			click("xpath", "//li[@f_value='settlementSetting']/descendant-or-self::*[5]")
			# 点击支票用途菜单
			click("xpath", "//span[text()='交易对手评级']")
			# 退出所有iframe窗体
			switch_default()
			
			for i in range(1, 3):
				# 切入交易对手评级的iframe窗体
				switch_to("xpath", "//iframe[@id='counterpartygrade-tab-iframe']")
				logging.info("开始测试交易对手评级功能")
				
				# 用JS的方法点击新增按钮
				js_click("xpath", "//span[text()='新增']")
				
				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='addWin-iframe']")
				sleep(1)
				
				# 输入交易对手类别代码
				input("xpath", "//input[@name='code']", "TestGrade")
				sleep(1)
				
				# 输入交易对手类别名称
				input("xpath", "//input[@id='name']", "自动化测试交易对手评级")
				sleep(1)
				
				# 输入付款优先级
				click("xpath", "//input[@id='combobox-input-payprioritylevel']")
				sleep(1)
				input("xpath", "//input[@id='combobox-input-payprioritylevel']", "Ⅰ")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-payprioritylevel']")
				input_enter("xpath", "//input[@id='combobox-input-payprioritylevel']")
				sleep(1)
				
				# 描述框中填入值
				input("xpath", "//textarea[@id='description']", "自动化测试交易对手评级描述框")
				sleep(1)
				
				# 点击保存按钮
				click("xpath", "//span[text()='保存']")
				
				# 退出所有iframe窗体
				switch_default()
				
				# 用隐式等待方法等页面出现新增成功的提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				print("交易对手评级，保存成功！")
				time.sleep(3)
				
				if i == 1:
					# 删除功能
					# 切入交易对手类别的iframe窗体
					switch_to("xpath", "//iframe[@id='counterpartygrade-tab-iframe']")
					
					# 点击查看
					# 用JS的方法点击放大镜
					js_click("xpath", "//span[@class='f-contrac-close']")
					sleep(1)
					
					# 输入代码：
					input("xpath", "//input[@id='code']", "TestGrade")
					sleep(1)
					
					# 点击查询
					click("xpath", "//span[text()='查询']")
					
					# 勾选
					click("xpath", "//div[@title='代码:TestGrade']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
					
					# 点击删除按钮
					click("xpath", "//span[text()='删除']")
					
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现删除的提示框
					implici_wait("xpath", "//span[contains(text(),'删除成功1条，失败0条！')]")
					print("交易对手评级，删除成功！")
					time.sleep(3)
			
			# 切入‘交易对手类别’的iframe窗体
			switch_to("xpath", "//iframe[@id='counterpartygrade-tab-iframe']")
			
			# 点击查看
			# 清空代码框的内容
			clear("xpath", "//input[@id='code']")
			sleep(1)
			
			# 输入代码：
			input("xpath", "//input[@id='code']", "TestGrade")
			sleep(1)
			
			# 点击查询
			click("xpath", "//span[text()='查询']")
			
			# 修改
			# 勾选
			click("xpath", "//div[@title='代码:TestGrade']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
			
			# 点击修改按钮
			click("xpath", "//span[text()='修改']")
			
			# 切入修改的iframe窗体
			switch_to("xpath", "//iframe[@id='modWin-iframe']")
			sleep(1)
			
			# 修改描述框中的内容
			input("xpath", "//textarea[@id='description']", "自动化测试交易对手评级修改")
			sleep(1)
			
			# 点击保存按钮
			click("xpath", "//span[text()='保存']")
			
			# 退出所有iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("交易对手评级，修改成功！")
			time.sleep(3)
			
			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='交易对手评级']/child::*[1]")
			
			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//li[@f_value='settlementSetting']/descendant-or-self::*[5]")
			
			# 打印操作成功日志
			print("交易对手评级，操作成功!")
			logging.info("交易对手评级，操作成功!")
			time.sleep(2)
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("交易对手评级打印失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		
		# 测试基础设置--交易对手
		try:
			# 点击基础设置菜单
			click("xpath", "//li[@f_value='settlementSetting']/descendant-or-self::*[5]")
			# 点击交易对手菜单
			click("xpath", "//span[text()='交易对手']")
			# 退出所有iframe窗体
			switch_default()
			sleep(1)
			for i in range(1, 2):
				# 切入交易对手的iframe窗体
				switch_to("xpath", "//iframe[@id='counterparty-tab-iframe']")
				logging.info("开始测试交易对手功能")
				sleep(1)
				# 用JS的方法点击新增按钮
				#js_click("xpath", "//span[text()='新增交易对手']")
				click("xpath", "//span[text()='新增交易对手']")
				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='addWin-iframe']")
				sleep(1)
				
				# 输入名称
				input("xpath", "//input[@id='name']", "TestCouParty")
				sleep(1)
				
				# 输入交易对手类别
				click("xpath", "//input[@id='combobox-input-categoryid']")
				sleep(1)
				input("xpath", "//input[@id='combobox-input-categoryid']", "自动化测试交易对手类别")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-categoryid']")
				input_enter("xpath", "//input[@id='combobox-input-categoryid']")
				sleep(1)
				
				# 输入交易对手评级
				click("xpath", "//input[@id='combobox-input-counterpartygradeid']")
				sleep(1)
				input("xpath", "//input[@id='combobox-input-counterpartygradeid']", "自动化测试交易对手评级")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-counterpartygradeid']")
				input_enter("xpath", "//input[@id='combobox-input-counterpartygradeid']")
				sleep(1)
				
				# # 输入默认资金类别
				# click("xpath", "//input[@id='combobox-input-defaultcapitalcategoryid']")
				# sleep(1)
				# input_down("xpath", "//input[@id='combobox-input-defaultcapitalcategoryid']")
				# sleep(1)
				# input_enter("xpath", "//input[@id='combobox-input-defaultcapitalcategoryid']")
				# sleep(1)
				
				# 输入默认付款交易类别
				click("xpath", "//input[@id='combobox-input-defaultpaypaytypeid']")
				sleep(1)
				input("xpath", "//input[@id='combobox-input-defaultpaypaytypeid']", "对外付款")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-defaultpaypaytypeid']")
				input_enter("xpath", "//input[@id='combobox-input-defaultpaypaytypeid']")
				sleep(1)
				
				# 输入默认收款交易类型
				click("xpath", "//input[@id='combobox-input-defaultrecpaytypeid']")
				sleep(1)
				input("xpath", "//input[@id='combobox-input-defaultrecpaytypeid']", "外部收款")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-defaultrecpaytypeid']")
				input_enter("xpath", "//input[@id='combobox-input-defaultrecpaytypeid']")
				sleep(1)
				
				# 输入默认现金流量项目自动化测试现金流
				# click("xpath", "//input[@id='combobox-input-defaultcashflowid']")
				# sleep(1)
				# input_down("xpath", "//input[@id='combobox-input-defaultcashflowid']")
				# sleep(1)
				# input_enter("xpath", "//input[@id='combobox-input-defaultcashflowid']")
				# sleep(1)
				
				# 输入统驭科目代码
				input("xpath", "//input[@id='reconciliationaccount']", "Tykm001")
				sleep(1)
				
				# 输入风险控制
				click("xpath", "//input[@id='combobox-input-riskcontrol']")
				sleep(1)
				input("xpath", "//input[@id='combobox-input-riskcontrol']", "不控制")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-riskcontrol']")
				input_enter("xpath", "//input[@id='combobox-input-riskcontrol']")
				sleep(1)
				
				# 选择失效日期
				today = date.today()
				expireddate = today + timedelta(days=720)
				click("xpath", "//input[@id='expireddate-input']")
				sleep(1)
				clear("xpath", "//input[@id='expireddate-input']")
				sleep(1)
				input("xpath", "//input[@id='expireddate-input']", str(expireddate))
				# 模拟回车键
				keyDown('enter')
				keyUp('enter')
				time.sleep(2)
				
				# 输入交易对手手机号
				input("xpath", "//textarea[@id='counterpartyphone']", "10086")
				sleep(1)
				
				# 测试账户信息
				# 点击授新增行，新增第一行
				click("xpath", "//span[text()='新增行']")
				sleep(1)
				
				# 输入银行
				input("xpath", "//input[@id='counterpartyaccountsgrid-accountnumber-0']", "202004211437")
				sleep(1)
				
				# 输入账户名称
				input("xpath", "//input[@id='counterpartyaccountsgrid-accountname-0']", "Mindy自动化测试账户名称")
				sleep(1)
				
				# 输入币种
				click("xpath", "//input[@id='combobox-input-counterpartyaccountsgrid-currencyid-0']")
				sleep(1)
				input("xpath", "//input[@id='combobox-input-counterpartyaccountsgrid-currencyid-0']", "CNY-人民币")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-counterpartyaccountsgrid-currencyid-0']")
				input_enter("xpath", "//input[@id='combobox-input-counterpartyaccountsgrid-currencyid-0']")
				sleep(1)
				
				# 输入银行
				click("xpath", "//input[@id='combobox-input-counterpartyaccountsgrid-bankid-0']")
				sleep(1)
				input("xpath", "//input[@id='combobox-input-counterpartyaccountsgrid-bankid-0']", "中国银行")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-counterpartyaccountsgrid-bankid-0']")
				input_enter("xpath", "//input[@id='combobox-input-counterpartyaccountsgrid-bankid-0']")
				sleep(1)
				
				# 输入银行区域
				click("xpath", "//input[@id='combobox-input-counterpartyaccountsgrid-areaid-0']")
				sleep(1)
				input("xpath", "//input[@id='combobox-input-counterpartyaccountsgrid-areaid-0']", "大连")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-counterpartyaccountsgrid-areaid-0']")
				input_enter("xpath", "//input[@id='combobox-input-counterpartyaccountsgrid-areaid-0']")
				sleep(1)
				
				# 输入开户行
				click("xpath", "//input[@id='combobox-input-counterpartyaccountsgrid-cnaps-0']")
				sleep(1)
				input("xpath", "//input[@id='combobox-input-counterpartyaccountsgrid-cnaps-0']", "大连泡崖街")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-counterpartyaccountsgrid-cnaps-0']")
				input_enter("xpath", "//input[@id='combobox-input-counterpartyaccountsgrid-cnaps-0']")
				sleep(1)
				
				# 点击保存按钮
				click("xpath", "//span[text()='保存']")
				
				# 退出所有iframe窗体
				switch_default()
				
				# 用隐式等待方法等页面出现新增成功的提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				print("交易对手，保存成功！")
				time.sleep(3)
				
				if i == 1:
					# 新增交易对手账户功能
					# 切入交易对手的iframe窗体
					switch_to("xpath", "//iframe[@id='counterparty-tab-iframe']")
					
					# 点击查看
					# 用JS的方法点击放大镜
					js_click("xpath", "//span[@class='f-contrac-close']")
					sleep(1)
					
					# 输入代码：
					input("xpath", "//input[@id='name']", "TestCouParty")
					sleep(1)
					
					# 点击查询
					click("xpath", "//span[text()='查询']")
					sleep(1)
					
					# 勾选
					click("xpath",
					      "//span[text()='TestCouParty']/ancestor::*[7]/preceding-sibling::*[1]/descendant::*[19]")
					
					# 用JS方便点击‘审核’按钮旁边的倒三角形
					js_click("xpath", "//span[text()='新增交易对手']/parent::*/following-sibling::*/child::*")
					sleep(1)
					
					# 点击取消审核按钮
					js_click("xpath", "//a[contains(text(),'新增交易对手账户')]")
					sleep(1)
					
					# 切入新增的iframe窗体
					switch_to("xpath", "//iframe[@id='configAccountWin-iframe']")
					sleep(1)
					
					# 输入卡折类型
					click("xpath", "//input[@id='combobox-input-cardtype']")
					sleep(1)
					input("xpath", "//input[@id='combobox-input-cardtype']", "折")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-cardtype']")
					input_enter("xpath", "//input[@id='combobox-input-cardtype']")
					sleep(1)
					
					# 输入银行账号
					click("xpath", "//input[@id='combobox-input-cardtype']")
					sleep(1)
					input("xpath", "//input[@id='combobox-input-cardtype']", "折")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-cardtype']")
					input_enter("xpath", "//input[@id='combobox-input-cardtype']")
					sleep(1)
					
					# 输入银行账号
					input("xpath", "//input[@id='accountnumber']", "202004211854")
					sleep(1)
					
					# 输入银行
					click("xpath", "//input[@id='combobox-input-bankid']")
					sleep(1)
					input("xpath", "//input[@id='combobox-input-bankid']", "中国银行")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-bankid']")
					input_enter("xpath", "//input[@id='combobox-input-bankid']")
					sleep(1)
					
					# 输入币种
					click("xpath", "//input[@id='combobox-input-currencyid']")
					sleep(1)
					input("xpath", "//input[@id='combobox-input-currencyid']", "人民币")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-currencyid']")
					input_enter("xpath", "//input[@id='combobox-input-currencyid']")
					sleep(1)
					
					# 点击保存按钮
					click("xpath", "//span[text()='保存']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现删除的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功')]")
					print("交易对手，新增交易对手账户成功！")
					time.sleep(3)
					
					# 修改功能
					# 切入交易对手的iframe窗体
					switch_to("xpath", "//iframe[@id='counterparty-tab-iframe']")
					
					# 勾选
					click("xpath",
					      "//span[text()='TestCouParty']/ancestor::*[7]/preceding-sibling::*[1]/descendant::*[19]")
					
					# 点击修改按钮
					click("xpath", "//span[text()='修改']")
					sleep(1)
					
					# 切入新增的iframe窗体
					switch_to("xpath", "//iframe[@id='modWin-iframe']")
					sleep(1)
					
					# 输入交易对手手机号
					input("xpath", "//textarea[@id='counterpartyphone']", "10086自动化修改")
					sleep(1)
					
					# 点击保存按钮
					click("xpath", "//span[text()='保存']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现删除的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功')]")
					print("交易对手，修改成功！")
					time.sleep(3)
					
					# 失效功能
					# 切入交易对手的iframe窗体
					switch_to("xpath", "//iframe[@id='counterparty-tab-iframe']")
					
					# 勾选
					click("xpath",
					      "//span[text()='TestCouParty']/ancestor::*[7]/preceding-sibling::*[1]/descendant::*[19]")
					
					# 点击修改按钮
					click("xpath", "//span[text()='失效']")
					sleep(1)
					
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现删除的提示框
					implici_wait("xpath", "//span[contains(text(),'失效成功！')]")
					print("交易对手，失效成功！")
					time.sleep(3)
					
					# 生效功能
					# 切入交易对手的iframe窗体
					switch_to("xpath", "//iframe[@id='counterparty-tab-iframe']")
					
					# 勾选
					click("xpath",
					      "//span[text()='TestCouParty']/ancestor::*[7]/preceding-sibling::*[1]/descendant::*[19]")
					
					# 点击生按钮
					click("xpath", "//span[text()='生效']")
					sleep(1)
					
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现删除的提示框
					implici_wait("xpath", "//span[contains(text(),'生效成功！')]")
					print("交易对手，生效成功！")
					time.sleep(3)
					
					# 维护联系方式功能
					# 切入交易对手的iframe窗体
					switch_to("xpath", "//iframe[@id='counterparty-tab-iframe']")
					
					# 勾选
					click("xpath",
					      "//span[text()='TestCouParty']/ancestor::*[7]/preceding-sibling::*[1]/descendant::*[19]")
					
					# 点击维护联系方式按钮
					click("xpath", "//span[text()='维护联系方式']")
					sleep(1)
					
					switch_to("xpath", "//iframe[@id='contactMaintainWin-iframe']")
					sleep(1)
					
					# 输入交易对手手机号
					input("xpath", "//textarea[@id='counterpartyphone']", "WH10086")
					sleep(1)
					
					# 点击保存按钮
					click("xpath", "//span[text()='保存']")
					sleep(1)
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现删除的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("交易对手，维护联系方式成功！")
					time.sleep(3)
					
					# 删除功能
					# 切入交易对手的iframe窗体
					switch_to("xpath", "//iframe[@id='counterparty-tab-iframe']")
					
					# 勾选
					click("xpath",
					      "//span[text()='TestCouParty']/ancestor::*[7]/preceding-sibling::*[1]/descendant::*[19]")
					
					# 点击删除按钮
					click("xpath", "//span[text()='删除']")
					sleep(1)
					
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现删除的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("交易对手，删除成功！")
					time.sleep(3)
					
					# 导出账户变更日志
					# 切入交易对手的iframe窗体exportChangedLogWin-iframe
					switch_to("xpath", "//iframe[@id='counterparty-tab-iframe']")
					
					# 点击生按钮
					js_click("xpath", "//span[text()='导出账户变更日志']")
					sleep(1)
					
					switch_to("xpath", "//iframe[@id='exportChangedLogWin-iframe']")
					# 选择开始日期
					today = date.today()
					triggeonstartdate = today - timedelta(days=20)
					click("xpath", "//input[@id='triggeonstart-input']")
					sleep(1)
					clear("xpath", "//input[@id='triggeonstart-input']")
					sleep(1)
					input("xpath", "//input[@id='triggeonstart-input']", str(triggeonstartdate))
					# 模拟回车键
					keyDown('enter')
					keyUp('enter')
					time.sleep(2)
					
					# 选择结束日期
					today = date.today()
					triggeonenddate = today
					click("xpath", "//input[@id='triggeonend-input']")
					sleep(1)
					clear("xpath", "//input[@id='triggeonend-input']")
					sleep(1)
					input("xpath", "//input[@id='triggeonend-input']", str(triggeonenddate))
					# 模拟回车键
					keyDown('enter')
					keyUp('enter')
					time.sleep(2)
					# 点击保存按钮
					click("xpath", "//span[text()='导出']")
					sleep(1)
					
					print("交易对手，导出账户变更日志成功！")
					time.sleep(3)
			
			switch_default()
			
			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='交易对手']/child::*[1]")
			
			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//li[@f_value='settlementSetting']/descendant-or-self::*[5]")
			
			# 打印操作成功日志
			print("交易对手，操作成功!")
			logging.info("交易对手，操作成功!")
			time.sleep(2)
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("交易对手操作失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		
		# 交易对手删除后依次删除交易对手类别和交易对手评级
		# 测试基础设置--交易对手类别删除功能
		try:
			# 点击基础设置菜单
			click("xpath", "//li[@f_value='settlementSetting']/descendant-or-self::*[5]")
			# 点击支票用途菜单
			click("xpath", "//span[text()='交易对手类别']")
			# 退出所有iframe窗体
			switch_default()
			
			# 切入支票作废原因的iframe窗体
			switch_to("xpath", "//iframe[@id='counterpartycategroy-tab-iframe']")
			logging.info("开始测试交易对手类别删除功能")
			
			# 点击查看
			# 用JS的方法点击放大镜
			js_click("xpath", "//span[@class='f-contrac-close']")
			sleep(1)
			
			# 输入代码：
			input("xpath", "//input[@id='code']", "TestCat")
			sleep(1)
			
			# 点击查询
			click("xpath", "//span[text()='查询']")
			
			# 勾选
			click("xpath", "//div[@title='名称:自动化测试交易对手类别']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
			
			# 点击删除按钮
			click("xpath", "//span[text()='删除']")
			
			# 点击弹出框的OK键
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
			
			# 退出所有iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功')]")
			print("交易对手类别，删除成功！")
			time.sleep(3)
			
			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='交易对手类别']/child::*[1]")
			
			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//li[@f_value='settlementSetting']/descendant-or-self::*[5]")
			
			# 打印操作成功日志
			print("交易对手类别，删除操作成功!")
			logging.info("交易对手类别，删除操作成功!")
			time.sleep(2)
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("交易对手类别删除打印失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		
		# 测试基础设置--交易对手评级删除
		try:
			# 点击基础设置菜单
			click("xpath", "//li[@f_value='settlementSetting']/descendant-or-self::*[5]")
			# 点击支票用途菜单
			click("xpath", "//span[text()='交易对手评级']")
			# 退出所有iframe窗体
			switch_default()
			
			# 切入交易对手评级的iframe窗体
			switch_to("xpath", "//iframe[@id='counterpartygrade-tab-iframe']")
			logging.info("开始测试交易对手评级删除功能")
			
			# 点击查看
			# 用JS的方法点击放大镜
			js_click("xpath", "//span[@class='f-contrac-close']")
			sleep(1)
			
			# 输入代码：
			input("xpath", "//input[@id='code']", "TestGrade")
			sleep(1)
			
			# 点击查询
			click("xpath", "//span[text()='查询']")
			
			# 勾选
			click("xpath", "//div[@title='代码:TestGrade']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
			
			# 点击删除按钮
			click("xpath", "//span[text()='删除']")
			
			# 点击弹出框的OK键
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
			
			# 退出所有iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'删除成功1条，失败0条！')]")
			print("交易对手评级，删除成功！")
			time.sleep(3)
			
			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='交易对手评级']/child::*[1]")
			
			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//li[@f_value='settlementSetting']/descendant-or-self::*[5]")
			
			# 打印操作成功日志
			print("交易对手评级，删除操作成功!")
			logging.info("交易对手评级，删除操作成功!")
			time.sleep(2)
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("交易对手评级删除打印失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		
		# 测试基础设置--结算方式
		try:
			# 点击基础设置菜单
			click("xpath", "//li[@f_value='settlementSetting']/descendant-or-self::*[5]")
			# 点击支票用途菜单
			click("xpath", "//span[text()='结算方式']")
			# 退出所有iframe窗体
			switch_default()
			
			for i in range(1, 2):
				# 切入结算方式的iframe窗体
				switch_to("xpath", "//iframe[@id='settlementMode-tab-iframe']")
				logging.info("开始测试结算方式功能")
				
				# 用JS的方法点击新增按钮
				js_click("xpath", "//span[text()='新增']")
				
				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='addWin-iframe']")
				sleep(1)
				
				# 输入代码
				input("xpath", "//input[@name='code']", "TestSetmode")
				sleep(1)
				
				# 输入结算方式
				input("xpath", "//input[@id='name']", "自动化测试结算方式")
				sleep(1)
				
				# 输入交易方向
				click("xpath", "//input[@id='combobox-input-moneyway']")
				sleep(1)
				input("xpath", "//input[@id='combobox-input-moneyway']", "支出")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-moneyway']")
				input_enter("xpath", "//input[@id='combobox-input-moneyway']")
				sleep(1)
				
				# 输入支付类型
				click("xpath", "//input[@id='combobox-input-dealtype']")
				sleep(1)
				input("xpath", "//input[@id='combobox-input-dealtype']", "现金")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-dealtype']")
				input_enter("xpath", "//input[@id='combobox-input-dealtype']")
				sleep(1)
				# 描述框中填入值
				input("xpath", "//textarea[@id='description']", "自动化测试结算方式描述框")
				sleep(1)
				
				# 点击保存按钮
				click("xpath", "//span[text()='保存']")
				
				# 退出所有iframe窗体
				switch_default()
				
				# 用隐式等待方法等页面出现新增成功的提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				print("结算方式，保存成功！")
				time.sleep(3)
				
				if i == 1:
					# 修改功能
					# 切入结算方式的iframe窗体
					switch_to("xpath", "//iframe[@id='settlementMode-tab-iframe']")
					
					# 点击查看
					# 用JS的方法点击放大镜
					js_click("xpath", "//span[@class='f-contrac-close']")
					sleep(1)
					
					# 输入代码：
					input("xpath", "//input[@id='code']", "TestSetmode")
					sleep(1)
					
					# 点击查询
					click("xpath", "//span[text()='查询']")
					
					# 勾选
					click("xpath", "//div[@title='代码:TestSetmode']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
					
					# 点击修改按钮
					click("xpath", "//span[text()='修改']")
					
					# 切入修改的iframe窗体
					switch_to("xpath", "//iframe[@id='modWin-iframe']")
					sleep(1)
					
					# 修改描述框中的内容
					input("xpath", "//textarea[@id='description']", "自动化测试结算方式修改")
					sleep(1)
					
					# 点击保存按钮
					click("xpath", "//span[text()='保存']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现新增成功的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("结算方式，修改成功！")
					time.sleep(3)
					
					# 切入‘结算方式’的iframe窗体
					switch_to("xpath", "//iframe[@id='settlementMode-tab-iframe']")
					
					# 失效
					# 勾选
					click("xpath", "//div[@title='代码:TestSetmode']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
					
					# 点击修改按钮
					click("xpath", "//span[text()='失效']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现新增成功的提示框
					implici_wait("xpath", "//span[contains(text(),'失效成功！')]")
					print("结算方式，失效成功！")
					time.sleep(3)
					
					# 切入‘结算方式’的iframe窗体
					switch_to("xpath", "//iframe[@id='settlementMode-tab-iframe']")
					
					# 失效
					# 勾选
					click("xpath", "//div[@title='代码:TestSetmode']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
					
					# 点击修改按钮
					click("xpath", "//span[text()='生效']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现新增成功的提示框
					implici_wait("xpath", "//span[contains(text(),'生效成功！')]")
					print("结算方式，生效成功！")
					time.sleep(3)
			
			# 切入‘交易对手类别’的iframe窗体
			switch_to("xpath", "//iframe[@id='settlementMode-tab-iframe']")
			
			# 点击查看
			# 清空代码框的内容
			clear("xpath", "//input[@id='code']")
			sleep(1)
			
			# 输入代码：
			input("xpath", "//input[@id='code']", "TestSetmode")
			sleep(1)
			
			# 点击查询
			click("xpath", "//span[text()='查询']")
			
			# 删除
			# 勾选
			click("xpath", "//div[@title='代码:TestSetmode']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
			
			# 点击删除按钮
			click("xpath", "//span[text()='删除']")
			
			# 点击弹出框的OK键
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
			
			# 退出所有iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("结算方式，删除成功！")
			time.sleep(3)
			
			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='结算方式']/child::*[1]")
			
			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//li[@f_value='settlementSetting']/descendant-or-self::*[5]")
			
			# 打印操作成功日志
			print("结算方式，操作成功!")
			logging.info("结算方式，操作成功!")
			time.sleep(2)
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("结算方式打印失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		
		# 测试基础设置--支付限额
		try:
			# 点击基础设置菜单
			click("xpath", "//li[@f_value='settlementSetting']/descendant-or-self::*[5]")
			# 点击支票用途菜单
			click("xpath", "//span[text()='支付限额']")
			# 退出所有iframe窗体
			switch_default()
			
			for i in range(1, 2):
				# 切入结算方式的iframe窗体
				switch_to("xpath", "//iframe[@id='limitAmount-tab-iframe']")
				logging.info("开始测试支付限额功能")
				
				# 用JS的方法点击新增按钮
				js_click("xpath", "//span[text()='新增']")
				
				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='addWin-iframe']")
				sleep(1)
				
				# 支付限额新增行
				click("xpath", "//span[text()='新增行']")
				sleep(1)
				
				# 输入组织
				click("xpath", "//input[@id='combobox-input-limitAmountPay-orgid-0']")
				sleep(1)
				input("xpath", "//input[@id='combobox-input-limitAmountPay-orgid-0']", "亚唐科技")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-limitAmountPay-orgid-0']")
				input_enter("xpath", "//input[@id='combobox-input-limitAmountPay-orgid-0']")
				sleep(1)
				
				# 输入账户
				click("xpath", "//input[@id='combobox-input-limitAmountPay-accountid-0']")
				sleep(1)
				input("xpath", "//input[@id='combobox-input-limitAmountPay-accountid-0']", "CNY")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-limitAmountPay-accountid-0']")
				input_enter("xpath", "//input[@id='combobox-input-limitAmountPay-accountid-0']")
				sleep(1)
				
				# 输入支付限额
				input("xpath", "//input[@id='limitAmountPay-limitamount-0-input']", "4000000")
				sleep(1)
				
				# 点击保存按钮
				click("xpath", "//span[text()='保存']")
				
				# 退出所有iframe窗体
				switch_default()
				
				
				# 用隐式等待方法等页面出现新增成功的提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				print("支付限额，保存成功！")
				time.sleep(3)
				
				if i == 1:
					# 删除功能
					# 切入结算方式的iframe窗体
					switch_to("xpath", "//iframe[@id='limitAmount-tab-iframe']")
					
					# 点击查看
					# 用JS的方法点击放大镜
					js_click("xpath", "//span[@class='f-contrac-close']")
					sleep(1)
					
					# 输入代码：
					input("xpath", "//input[@id='combobox-input-orgid']", "亚唐科技")
					sleep(1)
					click("xpath",
					      "//div[contains(text(),'亚唐科技')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")
					sleep(1)
					
					# 点击查询
					click("xpath", "//span[text()='查询']")
					sleep(1)
					
					# 勾选
					click("xpath",
					      "//div[contains(text(),'亚唐科技')]/parent::*/preceding-sibling::*[2]/descendant::*[2]")
					
					# 点击修改按钮
					click("xpath", "//span[text()='修改']")
					
					switch_to("xpath", "//iframe[@id='modWin-iframe']")
					input("xpath", "//input[@id='limitAmountPay-description-0']", "自动化测试支付限额描述")
					sleep(1)
					
					# 点击保存按钮
					click("xpath", "//span[text()='保存']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现删除的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("支付限额，修改成功！")
					time.sleep(3)
			
			# 切入‘支付限额’的iframe窗体
			switch_to("xpath", "//iframe[@id='limitAmount-tab-iframe']")
			
			# 勾选
			click("xpath", "//div[contains(text(),'亚唐科技')]/parent::*/preceding-sibling::*[2]/descendant::*[2]")
			
			# 点击修改按钮
			click("xpath", "//span[text()='失效']")
			
			# 退出所有iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'成功失效1条记录！')]")
			print("支付限额，失效成功！")
			time.sleep(3)
			
			# 切入‘支付限额’的iframe窗体
			switch_to("xpath", "//iframe[@id='limitAmount-tab-iframe']")
			
			# 勾选
			click("xpath", "//div[contains(text(),'亚唐科技')]/parent::*/preceding-sibling::*[2]/descendant::*[2]")
			
			# 点击修改按钮
			click("xpath", "//span[text()='生效']")
			
			# 退出所有iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'成功生效1条记录！')]")
			print("支付限额，生效成功！")
			time.sleep(3)
			
			# 切入‘支付限额’的iframe窗体
			switch_to("xpath", "//iframe[@id='limitAmount-tab-iframe']")
			
			# 勾选
			click("xpath", "//div[contains(text(),'亚唐科技')]/parent::*/preceding-sibling::*[2]/descendant::*[2]")
			
			# 点击修改按钮
			click("xpath", "//span[text()='删除']")
			
			# 点击弹出框的OK键
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
			
			# 退出所有iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'成功删除1条记录！')]")
			print("支付限额，删除成功！")
			time.sleep(3)
			
			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='支付限额']/child::*[1]")
			
			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//li[@f_value='settlementSetting']/descendant-or-self::*[5]")
			
			# 打印操作成功日志
			print("支付限额，操作成功!")
			logging.info("支付限额，操作成功!")
			time.sleep(2)
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("支付限额打印失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		
		# 测试基础设置--交易类型
		try:
			# 点击基础设置菜单
			click("xpath", "//li[@f_value='settlementSetting']/descendant-or-self::*[5]")
			# 点击交易类型菜单
			click("xpath", "//span[text()='交易类型']")
			# 退出所有iframe窗体
			switch_default()
			
			for i in range(1, 2):
				# 切入交易类型的iframe窗体
				switch_to("xpath", "//iframe[@id='payType-tab-iframe']")
				logging.info("开始测试交易类型功能")
				
				# 用JS的方法点击新增按钮
				js_click("xpath", "//span[text()='新增']")
				
				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='addWin-iframe']")
				sleep(1)
				
				# 输入代码
				input("xpath", "//input[@id='code']", "TestPayType")
				sleep(1)
				
				# 输入名称
				input("xpath", "//input[@id='name']", "自动化测试交易类型名称")
				sleep(1)
				
				# 交易方向
				click("xpath", "//input[@id='combobox-input-moneyway']")
				sleep(1)
				input("xpath", "//input[@id='combobox-input-moneyway']", "支出")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-moneyway']")
				input_enter("xpath", "//input[@id='combobox-input-moneyway']")
				sleep(1)
				
				# 交易类型类别
				click("xpath", "//input[@id='combobox-input-paytypecategory']")
				sleep(1)
				input("xpath", "//input[@id='combobox-input-paytypecategory']", "普通")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-paytypecategory']")
				input_enter("xpath", "//input[@id='combobox-input-paytypecategory']")
				sleep(1)
				
				# 可选结算方式
				click("xpath", "//input[@id='combobox-input-settlementmoderange']")
				sleep(1)
				# input("xpath", "//input[@id='combobox-input-settlementmoderange']", "101-直联单笔转账")
				# sleep(1)
				click("xpath", "//div[@title='结算方式:101-直联单笔转账']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
				sleep(1)
				
				# 默认结算方式
				click("xpath", "//input[@id='combobox-input-defaultsettlementmodeid']")
				sleep(1)
				input("xpath", "//input[@id='combobox-input-defaultsettlementmodeid']", "101-直联单笔转账")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-defaultsettlementmodeid']")
				input_enter("xpath", "//input[@id='combobox-input-defaultsettlementmodeid']")
				sleep(1)
				
				# 对方对象类型
				click("xpath", "//input[@id='combobox-input-oppobjecttype']")
				sleep(1)
				input("xpath", "//input[@id='combobox-input-oppobjecttype']", "交易对手")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-oppobjecttype']")
				input_enter("xpath", "//input[@id='combobox-input-oppobjecttype']")
				sleep(1)
				
				# 计划项目必填类型
				click("xpath", "//input[@id='combobox-input-budgetitemrequiredtype']")
				sleep(1)
				input("xpath", "//input[@id='combobox-input-budgetitemrequiredtype']", "非必填")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-budgetitemrequiredtype']")
				input_enter("xpath", "//input[@id='combobox-input-budgetitemrequiredtype']")
				sleep(1)
				
				# 描述框中填入值
				input("xpath", "//textarea[@id='description']", "自动化测试交易类型描述框")
				sleep(1)
				
				# 点击保存按钮
				click("xpath", "//span[text()='保存']")
				
				# 退出所有iframe窗体
				switch_default()
				
				# 用隐式等待方法等页面出现新增成功的提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				print("交易类型，保存成功！")
				time.sleep(3)
				
				if i == 1:
					# 修改功能
					# 切入交易类型的iframe窗体
					switch_to("xpath", "//iframe[@id='payType-tab-iframe']")
					
					# 点击查看
					# 用JS的方法点击放大镜
					js_click("xpath", "//span[@class='f-contrac-close']")
					sleep(1)
					
					# 输入代码：
					input("xpath", "//input[@id='code']", "TestPayType")
					sleep(1)
					
					# 点击查询
					click("xpath", "//span[text()='查询']")
					sleep(1)
					
					# 勾选
					click("xpath",
					      "//div[contains(text(),'自动化测试交易类型名称')]/parent::*/preceding-sibling::*[2]/descendant::*[2]")
					sleep(1)
					
					# 点击失效按钮
					click("xpath", "//span[text()='失效']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现新增成功的提示框
					implici_wait("xpath", "//span[contains(text(),'失效成功！')]")
					print("交易类型，失效成功！")
					time.sleep(3)
					
					# 切入‘交易类型’的iframe窗体
					switch_to("xpath", "//iframe[@id='payType-tab-iframe']")
					
					# 勾选
					click("xpath",
					      "//div[contains(text(),'自动化测试交易类型名称')]/parent::*/preceding-sibling::*[2]/descendant::*[2]")
					sleep(1)
					
					# 点击生效按钮
					click("xpath", "//span[text()='生效']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现新增成功的提示框
					implici_wait("xpath", "//span[contains(text(),'生效成功！')]")
					print("交易类型，生效成功！")
					time.sleep(3)
					
					# 切入‘交易类型’的iframe窗体
					switch_to("xpath", "//iframe[@id='payType-tab-iframe']")
					
					# 勾选
					click("xpath",
					      "//div[contains(text(),'自动化测试交易类型名称')]/parent::*/preceding-sibling::*[2]/descendant::*[2]")
					sleep(1)
					
					# 点击修改按钮
					click("xpath", "//span[text()='修改']")
					
					switch_to("xpath", "//iframe[@id='modWin-iframe']")
					sleep(1)
					
					# 描述框中填入值
					input("xpath", "//textarea[@id='description']", "自动化测试交易类型描述框修改")
					sleep(1)
					
					# 点击修改按钮
					click("xpath", "//span[text()='保存']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现新增成功的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("交易类型，修改成功！")
					time.sleep(3)
			
			# 切入‘交易类型’的iframe窗体
			switch_to("xpath", "//iframe[@id='payType-tab-iframe']")
			
			# 删除 勾选
			click("xpath", "//div[contains(text(),'自动化测试交易类型名称')]/parent::*/preceding-sibling::*[2]/descendant::*[2]")
			sleep(1)
			
			# 点击修改按钮
			click("xpath", "//span[text()='删除']")
			
			# 点击弹出框的OK键
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
			
			# 退出所有iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("交易类型，删除成功！")
			time.sleep(3)
			
			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='交易类型']/child::*[1]")
			
			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//li[@f_value='settlementSetting']/descendant-or-self::*[5]")
			
			# 打印操作成功日志
			print("交易类型，操作成功!")
			logging.info("交易类型，操作成功!")
			time.sleep(2)
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("交易类型打印失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		
		# 测试基础设置--作废原因
		try:
			# 点击基础设置菜单
			click("xpath", "//li[@f_value='settlementSetting']/descendant-or-self::*[5]")
			# 点击支票用途菜单
			click("xpath", "//span[text()='作废原因']")
			# 退出所有iframe窗体
			switch_default()
			
			for i in range(1, 2):
				# 切入作废原因的iframe窗体
				switch_to("xpath", "//iframe[@id='cancelReason-tab-iframe']")
				logging.info("开始测试作废原因功能")
				
				# 用JS的方法点击新增按钮
				js_click("xpath", "//span[text()='新增']")
				
				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='addWin-iframe']")
				sleep(1)
				
				# 输入作废原因代码
				input("xpath", "//input[@name='code']", "TestCanRea")
				sleep(1)
				
				# 输入作废原因名称
				input("xpath", "//input[@id='name']", "自动化测试作废原因")
				sleep(1)
				
				# 输入作废类型
				click("xpath", "//input[@id='combobox-input-classification']")
				input_down("xpath", "//input[@id='combobox-input-classification']")
				sleep(1)
				input_enter("xpath", "//input[@id='combobox-input-classification']")
				sleep(1)
				
				# 备注框中填入值
				input("xpath", "//textarea[@id='description']", "自动化测试作废原因备注框")
				sleep(1)
				
				# 点击保存按钮
				click("xpath", "//span[text()='保存']")
				
				# 退出所有iframe窗体
				switch_default()
				
				# 用隐式等待方法等页面出现新增成功的提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				print("作废原因，保存成功！")
				time.sleep(3)
				
				if i == 1:
					# 切入作废原因的iframe窗体
					switch_to("xpath", "//iframe[@id='cancelReason-tab-iframe']")
					
					# 点击查看
					# 用JS的方法点击放大镜
					js_click("xpath", "//span[@class='f-contrac-close']")
					sleep(1)
					
					# 输入代码：
					input("xpath", "//input[@id='code']", "TestCanRea")
					sleep(1)
					
					# 点击查询
					click("xpath", "//span[text()='查询']")
					
					# 修改
					# 勾选
					click("xpath", "//div[@title='作废代码:TestCanRea']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
					
					# 点击修改按钮
					click("xpath", "//span[text()='修改']")
					
					# 切入修改的iframe窗体
					switch_to("xpath", "//iframe[@id='modWin-iframe']")
					sleep(1)
					
					# 修改描述框中的内容
					input("xpath", "//textarea[@id='description']", "自动化测试作废原因修改")
					sleep(1)
					
					# 点击保存按钮
					click("xpath", "//span[text()='保存']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现新增成功的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("作废原因，修改成功！")
					time.sleep(3)
			
			# 删除功能
			# 切入作废原因的iframe窗体
			switch_to("xpath", "//iframe[@id='cancelReason-tab-iframe']")
			
			# 点击查看
			# 清空代码框的内容
			clear("xpath", "//input[@id='code']")
			sleep(1)
			
			# 输入代码：
			input("xpath", "//input[@id='code']", "TestCanRea")
			sleep(1)
			
			# 点击查询
			click("xpath", "//span[text()='查询']")
			
			# 勾选
			click("xpath", "//div[@title='作废代码:TestCanRea']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
			
			# 点击删除按钮
			click("xpath", "//span[text()='删除']")
			
			# 点击弹出框的OK键
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
			
			# 退出所有iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功')]")
			print("作废原因，删除成功！")
			time.sleep(3)
			
			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='作废原因']/child::*[1]")
			
			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//li[@f_value='settlementSetting']/descendant-or-self::*[5]")
			
			# 打印操作成功日志
			print("作废原因，操作成功!")
			logging.info("作废原因，操作成功!")
			time.sleep(2)
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("作废原因打印失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		
		# 测试基础设置--退票原因
		try:
			# 点击基础设置菜单
			click("xpath", "//li[@f_value='settlementSetting']/descendant-or-self::*[5]")
			# 点击支票用途菜单
			click("xpath", "//span[text()='退票原因']")
			# 退出所有iframe窗体
			switch_default()
			
			for i in range(1, 2):
				# 切入退票原因的iframe窗体
				switch_to("xpath", "//iframe[@id='refundReason-tab-iframe']")
				logging.info("开始测试退票原因功能")
				
				# 用JS的方法点击新增按钮
				js_click("xpath", "//span[text()='新增']")
				
				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='addWin-iframe']")
				sleep(1)
				
				# 输入作废原因代码
				input("xpath", "//input[@name='code']", "TestRefRea")
				sleep(1)
				
				# 输入退票原因名称
				input("xpath", "//input[@id='name']", "自动化测试退票原因")
				sleep(1)
				
				# 备注框中填入值
				input("xpath", "//textarea[@id='description']", "自动化测试作废原因备注框")
				sleep(1)
				
				# 点击保存按钮
				click("xpath", "//span[text()='保存']")
				
				# 退出所有iframe窗体
				switch_default()
				
				# 用隐式等待方法等页面出现新增成功的提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				print("退票原因，保存成功！")
				time.sleep(3)
				
				if i == 1:
					# 切入退票原因的iframe窗体
					switch_to("xpath", "//iframe[@id='refundReason-tab-iframe']")
					
					# 点击查看
					# 用JS的方法点击放大镜
					js_click("xpath", "//span[@class='f-contrac-close']")
					sleep(1)
					
					# 输入代码：
					input("xpath", "//input[@id='code']", "TestRefRea")
					sleep(1)
					
					# 点击查询
					click("xpath", "//span[text()='查询']")
					
					# 修改
					# 勾选
					click("xpath", "//div[@title='退票代码:TestRefRea']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
					
					# 点击修改按钮
					click("xpath", "//span[text()='修改']")
					
					# 切入修改的iframe窗体
					switch_to("xpath", "//iframe[@id='modWin-iframe']")
					sleep(1)
					
					# 修改描述框中的内容
					input("xpath", "//textarea[@id='description']", "自动化测试退票原因修改")
					sleep(1)
					
					# 点击保存按钮
					click("xpath", "//span[text()='保存']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现新增成功的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("退票原因，修改成功！")
					time.sleep(3)
			
			# 删除功能
			# 切入退票原因的iframe窗体
			switch_to("xpath", "//iframe[@id='refundReason-tab-iframe']")
			
			# 勾选
			click("xpath", "//div[@title='退票代码:TestRefRea']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
			
			# 点击删除按钮
			click("xpath", "//span[text()='删除']")
			
			# 点击弹出框的OK键
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
			
			# 退出所有iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功')]")
			print("退票原因，删除成功！")
			time.sleep(3)
			
			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='退票原因']/child::*[1]")
			
			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//li[@f_value='settlementSetting']/descendant-or-self::*[5]")
			
			# 打印操作成功日志
			print("退票原因，操作成功!")
			logging.info("退票原因，操作成功!")
			time.sleep(2)
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("退票原因打印失败！" + str(traceback.format_exc()))
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
