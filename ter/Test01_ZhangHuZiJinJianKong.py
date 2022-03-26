# encoding=utf-8
# @Time : 2020/8/14 14:49
# @Author :
# 此文件是测试账户Mindy资金监控模块，包含基础设置，账户生命周期，离线账户维护，直联账户查询，结构账户余额，账户余额查看，账户明细查看，离线账户日结
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


class Test_Zhzj(unittest.TestCase):
	
	# 启动浏览器
	def setUp(self):
		
		# 启动浏览器的另外一个方法：通过封装启动浏览器的驱动，启动不同浏览器
		self.driver = get("chrome")
	
	# 登陆系统、对系统设置进行操作
	def test_trade(self):
		
		# 通过登陆封装函数，进行登陆
		# login( G_Ora_Url,TestUser,Password, "自动化测试租户")
		# login( G_Ora_Url,Tao, Password,"默认租户")
		login(G_Mys_Url, mindy, Password, "亚唐科技")
		# login(G_Ora_Url, mindy, Password, "默认租户")
		# login( G_Mys_Url,TestUser,Password, "自动化测试租户")
		# login(G_Mys_Url, Tao, Password, "默认租户")
		# login(G_Mys_Url, mindy, Password, "默认租户")
		# login(G_Mys_Url, mindy, Password, "亚唐科技")
		# login(G_Mys_Url, judy, Password, "默认租户")
		
		logging.info("开始测试账户资金监控的页面功能")
		# 将页面的滚动条滑动到‘票据管理’页面的地方
		js_gd("xpath", "//span[contains(text(),'账户资金监控')]")
		# 用JS的方法点击票据管理菜单按钮
		js_click("xpath", "//span[contains(text(),'账户资金监控')]")
		
		# 开始测试账户资金监控--基础设置--账户性质
		# 测试基础设置--账户性质
		'''
		try:
			# 点击基础设置菜单
			click("xpath", "//li[@f_value='bankAccountSetting']/descendant-or-self::*[5]")
			# 点击账户性质菜单
			click("xpath", "//span[text()='账户性质']")
			# 退出所有iframe窗体
			switch_default()
			
			for i in range(1, 2):
				# 切入账户性质的iframe窗体
				switch_to("xpath", "//iframe[@id='bankAccountType-tab-iframe']")
				logging.info("开始测试账户性质功能")
				
				# 用JS的方法点击新增按钮
				js_click("xpath", "//span[text()='新增']")
				
				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='addWin-iframe']")
				sleep(1)
				
				# 输入用途代码
				input("xpath", "//input[@name='code']", "TestAccType")
				sleep(1)
				
				# 输入的账户性质
				input("xpath", "//input[@id='name']", "自动化测试账户性质")
				sleep(1)
				
				# 描述框中填入值
				input("xpath", "//textarea[@id='description']", "自动化测试账户性质描述框")
				sleep(1)
				
				# 点击保存按钮
				click("xpath", "//span[text()='保存']")
				
				# 退出所有iframe窗体
				switch_default()
				
				# 用隐式等待方法等页面出现新增成功的提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				print("账户性质，保存成功！")
				time.sleep(3)
				
				if i == 1:
					# 删除功能
					# 切入账户性质的iframe窗体
					switch_to("xpath", "//iframe[@id='bankAccountType-tab-iframe']")
					
					# 点击查看
					# 用JS的方法点击放大镜
					js_click("xpath", "//span[@class='f-contrac-close']")
					sleep(1)
					
					# 输入代码：
					input("xpath", "//input[@id='code']", "TestAccType")
					sleep(1)
					
					# 点击查询
					click("xpath", "//span[text()='查询']")
					
					# 修改
					# 勾选
					click("xpath", "//div[@title='代码:TestAccType']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
					
					# 点击修改按钮
					click("xpath", "//span[text()='修改']")
					
					# 切入修改的iframe窗体
					switch_to("xpath", "//iframe[@id='modWin-iframe']")
					sleep(1)
					
					# 修改描述框中的内容
					input("xpath", "//textarea[@id='description']", "自动化测试账户性质修改")
					sleep(1)
					
					# 点击保存按钮
					click("xpath", "//span[text()='保存']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现新增成功的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("账户性质，修改成功！")
					time.sleep(3)
			
			# 切入‘账户性质’的iframe窗体
			switch_to("xpath", "//iframe[@id='bankAccountType-tab-iframe']")
			
			# 点击查看
			# 清空代码框的内容
			clear("xpath", "//input[@id='code']")
			sleep(1)
			
			# 输入用途代码：
			input("xpath", "//input[@id='code']", "TestAccType")
			sleep(1)
			
			# 点击查询
			click("xpath", "//span[text()='查询']")
			
			# 勾选
			click("xpath", "//div[@title='代码:TestAccType']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
			
			# 点击删除按钮
			click("xpath", "//span[text()='删除']")
			
			# 点击弹出框的OK键
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
			
			# 退出所有iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功')]")
			print("账户性质，删除成功！")
			time.sleep(3)
			
			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='账户性质']/child::*[1]")
			
			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//li[@f_value='bankAccountSetting']/descendant-or-self::*[5]")
			# 打印操作成功日志
			print("账户性质，操作成功!")
			logging.info("账户性质，操作成功!")
			time.sleep(2)
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("账户性质失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		
		# 开始测试账户资金监控--基础设置--账户分组
		# 测试基础设置--账户分组
		try:
			# 点击基础设置菜单
			click("xpath", "//li[@f_value='bankAccountSetting']/descendant-or-self::*[5]")
			# 点击账户性质菜单
			click("xpath", "//span[text()='账户分组']")
			# 退出所有iframe窗体
			switch_default()
			
			for i in range(1, 2):
				# 切入账户分组的iframe窗体
				switch_to("xpath", "//iframe[@id='bankAccountGroup-tab-iframe']")
				logging.info("开始测试账户分组功能")
				
				# 用JS的方法点击新增按钮
				js_click("xpath", "//span[text()='新增']")
				
				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='addWin-iframe']")
				sleep(1)
				
				# 输入用途代码
				input("xpath", "//input[@name='code']", "TestAccGroup")
				sleep(1)
				
				# 输入的账户分组
				input("xpath", "//input[@id='name']", "自动化测试账户分组")
				sleep(1)
				
				# 描述框中填入值
				input("xpath", "//textarea[@id='description']", "自动化测试账户分组描述框")
				sleep(1)
				
				# 点击保存按钮
				click("xpath", "//span[text()='保存']")
				
				# 退出所有iframe窗体
				switch_default()
				
				# 用隐式等待方法等页面出现新增成功的提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				print("账户分组，保存成功！")
				time.sleep(3)
				
				if i == 1:
					# 修改功能
					# 切入账户分组的iframe窗体
					switch_to("xpath", "//iframe[@id='bankAccountGroup-tab-iframe']")
					
					# 点击查看
					# 用JS的方法点击放大镜
					js_click("xpath", "//span[@class='f-contrac-close']")
					sleep(1)
					
					# 输入代码：
					input("xpath", "//input[@id='code']", "TestAccGroup")
					sleep(1)
					
					# 点击查询
					click("xpath", "//span[text()='查询']")
					
					# 修改
					# 勾选
					click("xpath", "//div[@title='代码:TestAccGroup']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
					
					# 点击修改按钮
					click("xpath", "//span[text()='修改']")
					
					# 切入修改的iframe窗体
					switch_to("xpath", "//iframe[@id='modWin-iframe']")
					sleep(1)
					
					# 修改描述框中的内容
					input("xpath", "//textarea[@id='description']", "自动化测试账户分组修改")
					sleep(1)
					
					# 点击保存按钮
					click("xpath", "//span[text()='保存']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现新增成功的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("账户分组，修改成功！")
					time.sleep(3)
			
			# 切入‘账户分组’的iframe窗体
			switch_to("xpath", "//iframe[@id='bankAccountGroup-tab-iframe']")
			
			# 点击查看
			# 清空代码框的内容
			clear("xpath", "//input[@id='code']")
			sleep(1)
			
			# 输入用途代码：
			input("xpath", "//input[@id='code']", "TestAccGroup")
			sleep(1)
			
			# 点击查询
			click("xpath", "//span[text()='查询']")
			
			# 勾选
			click("xpath", "//div[@title='代码:TestAccGroup']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
			
			# 点击删除按钮
			click("xpath", "//span[text()='删除']")
			
			# 点击弹出框的OK键
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
			
			# 退出所有iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功')]")
			print("账户分组，删除成功！")
			time.sleep(3)
			
			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='账户分组']/child::*[1]")
			
			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//li[@f_value='bankAccountSetting']/descendant-or-self::*[5]")
			# 打印操作成功日志
			print("账户分组，操作成功!")
			logging.info("账户分组，操作成功!")
			time.sleep(2)
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("账户分组失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		
		# 开始测试账户资金监控--基础设置--账户分类
		
		# 开始测试账户资金监控--基础设置--账户分类
		# 测试基础设置--账户分类
		try:
			# 点击基础设置菜单
			click("xpath", "//li[@f_value='bankAccountSetting']/descendant-or-self::*[5]")
			# 点击账户性质菜单
			click("xpath", "//span[text()='受限原因']")
			# 退出所有iframe窗体
			switch_default()
			
			for i in range(1, 2):
				# 切入受限原因的iframe窗体
				switch_to("xpath", "//iframe[@id='bankAccountRestrictReason-tab-iframe']")
				logging.info("开始测试受限原因功能")
				
				# 用JS的方法点击新增按钮
				js_click("xpath", "//span[text()='新增']")
				
				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='addWin-iframe']")
				sleep(1)
				
				# 输入用途代码
				input("xpath", "//input[@name='code']", "TestAccRes")
				sleep(1)
				
				# 输入的账户分组
				input("xpath", "//input[@id='name']", "自动化测试受限原因")
				sleep(1)
				
				# 描述框中填入值
				input("xpath", "//textarea[@id='description']", "自动化测试受限原因描述框")
				sleep(1)
				
				# 点击保存按钮
				click("xpath", "//span[text()='保存']")
				
				# 退出所有iframe窗体
				switch_default()
				
				# 用隐式等待方法等页面出现新增成功的提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				print("受限原因，保存成功！")
				time.sleep(3)
				
				if i == 1:
					# 删除功能
					# 切入受限原因的iframe窗体
					switch_to("xpath", "//iframe[@id='bankAccountRestrictReason-tab-iframe']")
					
					# 点击查看
					# 用JS的方法点击放大镜
					js_click("xpath", "//span[@class='f-contrac-close']")
					sleep(1)
					
					# 输入代码：
					input("xpath", "//input[@id='code']", "TestAccRes")
					sleep(1)
					
					# 点击查询
					click("xpath", "//span[text()='查询']")
					sleep(3)
					
					# 修改 # 勾选
					click("xpath",
					      "//div[@title='代码:TestAccRes']/parent::*[1]/preceding-sibling::*[1]/descendant::*[2]")
					
					# 点击修改按钮
					click("xpath", "//span[text()='修改']")
					
					# 切入修改的iframe窗体
					switch_to("xpath", "//iframe[@id='modWin-iframe']")
					sleep(1)
					
					# 修改描述框中的内容
					input("xpath", "//textarea[@id='description']", "自动化测试受限原因修改")
					sleep(1)
					
					# 点击保存按钮
					click("xpath", "//span[text()='保存']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现新增成功的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("受限原因，修改成功！")
					time.sleep(3)
			
			# 切入‘受限原因’的iframe窗体
			switch_to("xpath", "//iframe[@id='bankAccountRestrictReason-tab-iframe']")
			
			# 勾选
			click("xpath", "//div[@title='代码:TestAccRes']/parent::*[1]/preceding-sibling::*[1]/descendant::*[2]")
			sleep(1)
			# 点击删除按钮
			click("xpath", "//span[text()='删除']")
			
			# 点击弹出框的OK键
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
			
			# 退出所有iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功')]")
			print("受限原因，删除成功！")
			time.sleep(3)
			
			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='受限原因']/child::*[1]")
			
			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//li[@f_value='bankAccountSetting']/descendant-or-self::*[5]")
			# 打印操作成功日志
			print("受限原因，操作成功!")
			logging.info("受限原因，操作成功!")
			time.sleep(2)
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("受限原因失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		'''
		# 数据要求，先做账户维护、再做账户申请
		# 开始测试账户资金监控--账户生命周期--账户维护
		# 测试账户生命周期--账户维护
		try:
			# 点击账户生命周期'菜单
			click("xpath", "//span[text()='账户生命周期']")
			# 点击账户申请菜单
			click("xpath", "//span[text()='账户维护']")
			# 退出所有iframe窗体
			switch_default()
			
			for i in range(1, 11):
				# 切入账户维护的iframe窗体
				switch_to("xpath", "//iframe[@id='bankAccounts-tab-iframe']")
				logging.info("开始测试账户维护单币种账户功能")
				sleep(1)
				
				switch_to("xpath", "//iframe[@id='subTabOne-iframe']")
				# 点击新增
				click("xpath", "//span[text()='新增']")
				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='addWin-iframe']")
				sleep(1)
				
				# 第一笔 BOC-中国银行 删除
				if i == 1:
					# 选择银行
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
					
					# 选择境内外
					click("xpath", "//input[@id='combobox-input-inorout']")
					# 输入开户行大连泡崖街支行名称，模糊查询
					input("xpath", "//input[@id='combobox-input-inorout']", "境内")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-inorout']")
					input_enter("xpath", "//input[@id='combobox-input-inorout']")
				
				# 第二笔 农业银行 现金虚拟户 组织转移
				if i == 2:
					# 选择银行
					click("xpath", "//input[@id='combobox-input-bankid']")
					# 模糊匹配报错，因此选择直接点击
					click("xpath", "//div[@title='代码-名称:ABC-农业银行']")
					sleep(1)
					
					# 选择开户行
					click("xpath", "//input[@id='combobox-input-banklocationid']")
					sleep(1)
					input("xpath", "//input[@id='combobox-input-banklocationid']", "彭泽县支行东门")
					sleep(1)
					click("xpath", "//div[@title='联行号-开户行名:103425134735-中国农业银行彭泽县支行东门分理处']")
					sleep(1)
					
					# 选择币种
					click("xpath", "//input[@id='combobox-input-currencyid']")
					# 输入开户行大连泡崖街支行名称，模糊查询
					input("xpath", "//input[@id='combobox-input-currencyid']", "USD")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-currencyid']")
					input_enter("xpath", "//input[@id='combobox-input-currencyid']")
					time.sleep(1)
					
					# 选择账户性质
					click("xpath", "//input[@id='combobox-input-accounttypeid']")
					# 输入开户行大连泡崖街支行名称，模糊查询
					input("xpath", "//input[@id='combobox-input-accounttypeid']", "一般户")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-accounttypeid']")
					input_enter("xpath", "//input[@id='combobox-input-accounttypeid']")
					time.sleep(1)
					
					# 选择现金虚拟户iscashvirtual
					click("xpath", "//input[@id='iscashvirtual']")
					
					# 选择境内外
					click("xpath", "//input[@id='combobox-input-inorout']")
					# 输入开户行大连泡崖街支行名称，模糊查询
					input("xpath", "//input[@id='combobox-input-inorout']", "境外")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-inorout']")
					input_enter("xpath", "//input[@id='combobox-input-inorout']")
				
				# 第三笔 工商银行 JPY  票据虚拟户
				if i == 3:
					# 选择银行
					click("xpath", "//input[@id='combobox-input-bankid']")
					# 模糊匹配报错，因此选择直接点击
					click("xpath", "//div[@title='代码-名称:ICBC-工商银行']")
					sleep(1)
					
					# 选择开户行
					click("xpath", "//input[@id='combobox-input-banklocationid']")
					input("xpath", "//input[@id='combobox-input-banklocationid']", "嫩江墨尔根支行")
					sleep(1)
					click("xpath", "//div[@title='联行号-开户行名:102278400027-中国工商银行股份有限公司嫩江墨尔根支行']")
					sleep(1)
					
					# 选择币种
					click("xpath", "//input[@id='combobox-input-currencyid']")
					# 输入开户行大连泡崖街支行名称，模糊查询
					input("xpath", "//input[@id='combobox-input-currencyid']", "JPY")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-currencyid']")
					input_enter("xpath", "//input[@id='combobox-input-currencyid']")
					time.sleep(1)
					
					# 选择账户性质
					click("xpath", "//input[@id='combobox-input-accounttypeid']")
					# 输入开户行大连泡崖街支行名称，模糊查询
					input("xpath", "//input[@id='combobox-input-accounttypeid']", "临时户")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-accounttypeid']")
					input_enter("xpath", "//input[@id='combobox-input-accounttypeid']")
					time.sleep(1)
					
					# # 选择票据虚拟户isbillvirtual
					click("xpath", "//input[@id='isbillvirtual']")
					
					# 选择境内外
					click("xpath", "//input[@id='combobox-input-inorout']")
					# 输入开户行大连泡崖街支行名称，模糊查询
					input("xpath", "//input[@id='combobox-input-inorout']", "境内")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-inorout']")
					input_enter("xpath", "//input[@id='combobox-input-inorout']")
				
				# 第四笔 建设银行 非直联 CNY
				
				if i == 4:
					# 选择银行
					click("xpath", "//input[@id='combobox-input-bankid']")
					# 模糊匹配报错，因此选择直接点击
					click("xpath", "//div[@title='代码-名称:CCB-建设银行']")
					sleep(1)
					
					# 选择开户行
					click("xpath", "//input[@id='combobox-input-banklocationid']")
					sleep(1)
					input("xpath", "//input[@id='combobox-input-banklocationid']", "巴林左旗支行")
					click("xpath", "//div[@title='联行号-开户行名:105194248432-中国建设银行股份有限公司巴林左旗支行']")
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
					
					# # 选择银企直联户/现金虚拟户/票据虚拟户 第一次选择银企直联户isbankdirect
					# click("xpath", "//input[@id='isbankdirect']")
					
					# 选择境内外
					click("xpath", "//input[@id='combobox-input-inorout']")
					# 输入开户行大连泡崖街支行名称，模糊查询
					input("xpath", "//input[@id='combobox-input-inorout']", "境内")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-inorout']")
					input_enter("xpath", "//input[@id='combobox-input-inorout']")
				
				# 第5笔 交通银行 CNY 非直联
				if i == 5:
					# 选择银行
					click("xpath", "//input[@id='combobox-input-bankid']")
					# 模糊匹配报错，因此选择直接点击
					click("xpath", "//div[@title='代码-名称:BOCOM-交通银行']")
					sleep(1)
					
					# 选择开户行
					click("xpath", "//input[@id='combobox-input-banklocationid']")
					input("xpath", "//input[@id='combobox-input-banklocationid']", "南通海门叠石桥支行")
					click("xpath", "//div[@title='联行号-开户行名:301306500025-交通银行股份有限公司南通海门叠石桥支行']")
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
					
					# 选择境内外
					click("xpath", "//input[@id='combobox-input-inorout']")
					# 输入开户行大连泡崖街支行名称，模糊查询
					input("xpath", "//input[@id='combobox-input-inorout']", "境内")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-inorout']")
					input_enter("xpath", "//input[@id='combobox-input-inorout']")
				
				# 第6笔 华夏银行 NOK 非直联
				if i == 6:
					# 选择银行
					click("xpath", "//input[@id='combobox-input-bankid']")
					# 模糊匹配报错，因此选择直接点击
					input("xpath", "//input[@id='combobox-input-bankid']", "华夏银行")
					sleep(1)
					click("xpath", "//div[@title='代码-名称:HXB-华夏银行']")
					sleep(1)
					
					# 选择开户行
					click("xpath", "//input[@id='combobox-input-banklocationid']")
					sleep(1)
					input("xpath", "//input[@id='combobox-input-banklocationid']", "大连泡崖")
					click("xpath", "//div[@title='联行号-开户行名:304222017837-华夏银行股份有限公司大连泡崖大街支行']")
					sleep(1)
					
					# 选择币种
					click("xpath", "//input[@id='combobox-input-currencyid']")
					# 输入开户行大连泡崖街支行名称，模糊查询
					input("xpath", "//input[@id='combobox-input-currencyid']", "NOK")
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
					
					# 选择境内外
					click("xpath", "//input[@id='combobox-input-inorout']")
					# 输入开户行大连泡崖街支行名称，模糊查询
					input("xpath", "//input[@id='combobox-input-inorout']", "境内")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-inorout']")
					input_enter("xpath", "//input[@id='combobox-input-inorout']")
				
				# 第7笔 BOC中国银行 直联
				if i == 7:
					# 选择银行
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
					
					# # 选择银企直联户/现金虚拟户/票据虚拟户 第一次选择银企直联户
					click("xpath", "//input[@id='isbankdirect']")
					
					# 选择境内外
					click("xpath", "//input[@id='combobox-input-inorout']")
					# 输入开户行大连泡崖街支行名称，模糊查询
					input("xpath", "//input[@id='combobox-input-inorout']", "境内")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-inorout']")
					input_enter("xpath", "//input[@id='combobox-input-inorout']")
				
				# 第8笔 ABC中国农业银行 直联
				if i == 8:
					# 选择银行
					click("xpath", "//input[@id='combobox-input-bankid']")
					# 模糊匹配报错，因此选择直接点击
					click("xpath", "//div[@title='代码-名称:ABC-农业银行']")
					sleep(1)
					
					# 选择开户行
					click("xpath", "//input[@id='combobox-input-banklocationid']")
					input("xpath", "//input[@id='combobox-input-banklocationid']", "彭泽县支行东门")
					sleep(1)
					click("xpath", "//div[@title='联行号-开户行名:103425134735-中国农业银行彭泽县支行东门分理处']")
					sleep(1)
					
					# 选择币种
					click("xpath", "//input[@id='combobox-input-currencyid']")
					# 输入开户行大连泡崖街支行名称，模糊查询
					input("xpath", "//input[@id='combobox-input-currencyid']", "USD")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-currencyid']")
					input_enter("xpath", "//input[@id='combobox-input-currencyid']")
					time.sleep(1)
					
					# 选择账户性质
					click("xpath", "//input[@id='combobox-input-accounttypeid']")
					# 输入开户行大连泡崖街支行名称，模糊查询
					input("xpath", "//input[@id='combobox-input-accounttypeid']", "一般户")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-accounttypeid']")
					input_enter("xpath", "//input[@id='combobox-input-accounttypeid']")
					time.sleep(1)
					
					# 选择直联账户 isbankdirect
					click("xpath", "//input[@id='isbankdirect']")
					
					# 选择境内外
					click("xpath", "//input[@id='combobox-input-inorout']")
					# 输入开户行大连泡崖街支行名称，模糊查询
					input("xpath", "//input[@id='combobox-input-inorout']", "境内")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-inorout']")
					input_enter("xpath", "//input[@id='combobox-input-inorout']")
				
				# 第9笔 BOC中国银行 非直联
				if i == 9:
					# 选择银行
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
					
					# 选择境内外
					click("xpath", "//input[@id='combobox-input-inorout']")
					# 输入开户行大连泡崖街支行名称，模糊查询
					input("xpath", "//input[@id='combobox-input-inorout']", "境内")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-inorout']")
					input_enter("xpath", "//input[@id='combobox-input-inorout']")
				
				# 第10笔 华夏银行 NOK 直联
				if i == 10:
					# 选择银行
					click("xpath", "//input[@id='combobox-input-bankid']")
					# 模糊匹配报错，因此选择直接点击
					input("xpath", "//input[@id='combobox-input-bankid']", "华夏银行")
					sleep(1)
					click("xpath", "//div[@title='代码-名称:HXB-华夏银行']")
					sleep(1)
					
					# 选择开户行
					click("xpath", "//input[@id='combobox-input-banklocationid']")
					sleep(1)
					input("xpath", "//input[@id='combobox-input-banklocationid']", "大连泡崖")
					click("xpath", "//div[@title='联行号-开户行名:304222017837-华夏银行股份有限公司大连泡崖大街支行']")
					sleep(1)
					
					# 选择币种
					click("xpath", "//input[@id='combobox-input-currencyid']")
					# 输入开户行大连泡崖街支行名称，模糊查询
					input("xpath", "//input[@id='combobox-input-currencyid']", "NOK")
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
					
					# 选择直联账户 isbankdirect
					click("xpath", "//input[@id='isbankdirect']")
					
					# 选择境内外
					click("xpath", "//input[@id='combobox-input-inorout']")
					# 输入开户行大连泡崖街支行名称，模糊查询
					input("xpath", "//input[@id='combobox-input-inorout']", "境内")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-inorout']")
					input_enter("xpath", "//input[@id='combobox-input-inorout']")
				
				# 设置时间的变成存储，变成
				temp1 = time.strftime("%H%M%S")
				# 输入银行账号
				click("xpath", "//input[@id='accountnumber']")
				sleep(1)
				input("xpath", "//input[@id='accountnumber']", "2020" + str(temp1))
				sleep(1)
				
				# 选择账户名称
				click("xpath", "//a[@id='importaccountname']")
				sleep(1)
				
				# 选择账户存款类型
				click("xpath", "//input[@id='combobox-input-deposittype']")
				# 输入开户行大连泡崖街支行名称，模糊查询
				input("xpath", "//input[@id='combobox-input-deposittype']", "活期")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-deposittype']")
				input_enter("xpath", "//input[@id='combobox-input-deposittype']")
				time.sleep(1)
				
				# 填写地址
				input("xpath", "//input[@id='accountaddress']", "甘肃定西")
				sleep(1)
				
				# 选择常驻国家性质
				click("xpath", "//input[@id='combobox-input-countrytype']")
				# 输入一般贸易区，模糊查询
				input("xpath", "//input[@id='combobox-input-countrytype']", "一般贸易区")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-countrytype']")
				input_enter("xpath", "//input[@id='combobox-input-countrytype']")
				time.sleep(1)
				
				# 选择账户分类
				click("xpath", "//input[@id='combobox-input-accountclassid']")
				# 输入开户行大连泡崖街支行名称，模糊查询
				input("xpath", "//input[@id='combobox-input-accountclassid']", "自动化测试账户分类")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-accountclassid']")
				input_enter("xpath", "//input[@id='combobox-input-accountclassid']")
				time.sleep(1)
				
				# 是否集团代管
				click("xpath", "//input[@id='istakeover']")
				sleep(1)
				
				# 选择收付属性
				click("xpath", "//input[@id='combobox-input-paymentattribute']")
				# 输入开户行大连泡崖街支行名称，模糊查询
				input("xpath", "//input[@id='combobox-input-paymentattribute']", "收入账户")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-paymentattribute']")
				input_enter("xpath", "//input[@id='combobox-input-paymentattribute']")
				
				# 点击保存按钮
				click("xpath", "//span[text()='保存']")
				
				# 退出所有iframe窗体
				switch_default()
				
				# 用隐式等待方法等页面出现提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				print("账户维护-单币种账户新增第%s次，保存成功！" % i)
				logging.info("账户维护-单币种账户新增第%s次，保存成功！" % i)
				time.sleep(3)
				
				# 第一笔，就先修改，再修改页面提交送审，再撤销送审，再删除
				if i == 1:
					# 切入‘账户申请’的iframe窗体
					switch_to("xpath", "//iframe[@id='bankAccounts-tab-iframe']")
					sleep(1)
					switch_to("xpath", "//iframe[@id='subTabOne-iframe']")
					sleep(1)
					
					# 点击查看
					# 用JS的方法点击放大镜
					js_click("xpath", "//span[@class='f-contrac-close']")
					sleep(1)
					
					# 输入银行：中国银行
					click("xpath", "//input[@id='combobox-input-bankid']")
					sleep(1)
					input("xpath", "//input[@id='combobox-input-bankid']", "中国银行")
					sleep(1)
					click("xpath", "//div[@title='代码-名称:BOC-中国银行']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
					sleep(1)
					
					# 点击查询
					click("xpath", "//span[text()='查询']")
					
					# 修改勾选数据
					click("xpath", '//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
					
					# 点击审核按钮
					click("xpath", "//span[text()='审核']")
					
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					sleep(1)
					
					# 退出所有iframe窗体
					switch_default()
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'账户成功审核1条！')]")
					print("账户维护-单币种账户第%s次，审核成功！" % i)
					logging.info("账户维护-单币种账户第%s次，审核成功！" % i)
					time.sleep(3)
					
					switch_to("xpath", "//iframe[@id='bankAccounts-tab-iframe']")
					sleep(1)
					switch_to("xpath", "//iframe[@id='subTabOne-iframe']")
					sleep(1)
					# 修改勾选数据
					click("xpath", '//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
					
					# 用JS方便点击‘申请’按钮旁边的倒三角形
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
					implici_wait("xpath", "//span[contains(text(),'账户成功取消审核1条！')]")
					print("账户维护-单币种账户，账户成功取消审核1条")
					logging.info("账户维护-单币种账户，账户成功取消审核1条")
					time.sleep(3)
					
					switch_to("xpath", "//iframe[@id='bankAccounts-tab-iframe']")
					sleep(1)
					switch_to("xpath", "//iframe[@id='subTabOne-iframe']")
					sleep(1)
					
					# 修改勾选数据
					click("xpath", '//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
					
					# 点击修改按钮
					click("xpath", "//span[text()='修改']")
					
					# 切入修改的iframe窗体
					switch_to("xpath", "//iframe[@id='modWin-iframe']")
					sleep(2)
					
					# 点击保存按钮
					click("xpath", "//span[text()='保存']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("账户维护-单币种账户，修改成功！")
					logging.info("账户维护-单币种账户，修改成功！")
					time.sleep(3)
					
					# 切入‘账户维护’的iframe窗体
					switch_to("xpath", "//iframe[@id='bankAccounts-tab-iframe']")
					sleep(1)
					switch_to("xpath", "//iframe[@id='subTabOne-iframe']")
					sleep(1)
					
					# 勾选数据
					click("xpath", '//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
					
					# 点击删除按钮
					click("xpath", "//span[text()='删除']")
					
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现删除的提示框
					implici_wait("xpath", "//span[contains(text(),'删除成功！')]")
					print("账户维护-单币种账户，删除成功！")
					logging.info("账户维护-单币种账户，删除成功！")
					time.sleep(3)
				
				# 第二笔，测试送审的流程，送审，双击页面同意，退回，送审，同意
				if i == 2:
					# 切入‘账户维护’的iframe窗体
					switch_to("xpath", "//iframe[@id='bankAccounts-tab-iframe']")
					sleep(1)
					switch_to("xpath", "//iframe[@id='subTabOne-iframe']")
					sleep(1)
					
					# 输入银行：农业银行
					click("xpath", "//input[@id='combobox-input-bankid']")
					sleep(1)
					# click("xpath", "//div[@title='代码-名称:BOC-中国银行']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
					# sleep(1)
					clear("xpath", "//input[@id='combobox-input-bankid']")
					sleep(1)
					input("xpath", "//input[@id='combobox-input-bankid']", "农业银行")
					sleep(1)
					click("xpath", "//div[@title='代码-名称:ABC-农业银行']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
					sleep(1)
					
					# 点击查询
					click("xpath", "//span[text()='查询']")
					#
					# 修改勾选数据
					click("xpath", '//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
					
					# 点击送审按钮
					click("xpath", "//span[text()='审核']")
					
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					sleep(1)
					
					# 退出所有iframe窗体
					switch_default()
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'账户成功审核1条！')]")
					print("账户维护-单币种账户第%s次，审核成功！" % i)
					logging.info("账户维护-单币种账户第%s次，审核成功！" % i)
					time.sleep(3)
					
					# 切入‘账户维护’的iframe窗体
					switch_to("xpath", "//iframe[@id='bankAccounts-tab-iframe']")
					sleep(1)
					switch_to("xpath", "//iframe[@id='subTabOne-iframe']")
					sleep(1)
					
					# 修改勾选数据
					click("xpath", '//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
					
					# 用JS方便点击‘申请’按钮旁边的倒三角形
					js_click("xpath", "//span[text()='维护']/parent::*/following-sibling::*/child::*")
					sleep(1)
					
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
					
					click("xpath", "//input[@id='initbalance-input']")
					sleep(1)
					clear("xpath", "//input[@id='initbalance-input']")
					sleep(1)
					input("xpath", "//input[@id='initbalance-input']", "30000")
					sleep(1)
					
					click("xpath", "//span[text()='确定']")
					sleep(1)
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("账户维护-单币种账户第%s次，开户成功！" % i)
					logging.info("账户维护-单币种账户第%s次，开户成功！" % i)
					time.sleep(3)
					
					# 切入‘账户维护’的iframe窗体
					switch_to("xpath", "//iframe[@id='bankAccounts-tab-iframe']")
					sleep(1)
					switch_to("xpath", "//iframe[@id='subTabOne-iframe']")
					sleep(1)
					
					# 修改勾选数据
					click("xpath", "//div[@title='账户状态:开户']/parent::*/preceding-sibling::*[7]/descendant::*[2]")
					
					# 用JS方便点击‘申请’按钮旁边的倒三角形
					js_click("xpath", "//span[text()='维护']/parent::*/following-sibling::*/child::*")
					sleep(1)
					
					js_click("xpath", "//a[contains(text(),'变更')]")
					sleep(1)
					
					switch_to("xpath", "//iframe[@id='updateAccountWin-iframe']")
					sleep(2)
					
					# # 选择会计科目
					# click("xpath", "//input[@id='combobox-input-extend1']")
					# input_down("xpath", "//input[@id='combobox-input-extend1']")
					# input_enter("xpath", "//input[@id='combobox-input-extend1']")
					# time.sleep(1)
					
					# # 缺少附件上传
					
					# 点击确定按钮
					click("xpath", "//span[text()='保存']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("账户维护，变更成功！")
					logging.info("账户维护，变更成功！")
					sleep(3)
					
					# 切入‘账户维护’的iframe窗体
					switch_to("xpath", "//iframe[@id='bankAccounts-tab-iframe']")
					sleep(1)
					switch_to("xpath", "//iframe[@id='subTabOne-iframe']")
					sleep(1)
					
					# 修改勾选数据
					click("xpath", "//div[@title='账户状态:开户']/parent::*/preceding-sibling::*[7]/descendant::*[2]")
					
					# 用JS方便点击‘申请’按钮旁边的倒三角形
					js_click("xpath", "//span[text()='维护']/parent::*/following-sibling::*/child::*")
					sleep(1)
					
					# 点击申请开户按钮
					js_click("xpath", "//a[contains(text(),'冻结')]")
					sleep(1)
					
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					sleep(1)
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("账户维护-单币种账户，冻结成功！")
					logging.info("账户维护-单币种账户，冻结成功！")
					sleep(3)
					
					# 切入‘账户维护’的iframe窗体
					switch_to("xpath", "//iframe[@id='bankAccounts-tab-iframe']")
					sleep(1)
					switch_to("xpath", "//iframe[@id='subTabOne-iframe']")
					sleep(1)
					
					# 修改勾选数据
					click("xpath", "//div[@title='账户状态:冻结']/parent::*/preceding-sibling::*[7]/descendant::*[2]")
					
					# 用JS方便点击‘申请’按钮旁边的倒三角形
					js_click("xpath", "//span[text()='维护']/parent::*/following-sibling::*/child::*")
					sleep(1)
					
					# 点击申请开户按钮
					js_click("xpath", "//a[contains(text(),'解冻')]")
					sleep(1)
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("账户维护-单币种账户，解冻成功！")
					logging.info("账户维护-单币种账户，解冻成功！")
					sleep(3)
					
					# 切入‘账户维护’的iframe窗体
					switch_to("xpath", "//iframe[@id='bankAccounts-tab-iframe']")
					sleep(1)
					switch_to("xpath", "//iframe[@id='subTabOne-iframe']")
					sleep(1)
					
					# 修改勾选数据
					click("xpath", "//div[@title='账户状态:开户']/parent::*/preceding-sibling::*[7]/descendant::*[2]")
					
					# 用JS方便点击‘申请’按钮旁边的倒三角形
					js_click("xpath", "//span[text()='维护']/parent::*/following-sibling::*/child::*")
					sleep(1)
					
					# 点击申请开户按钮
					js_click("xpath", "//a[contains(text(),'编辑账户事件')]")
					sleep(1)
					
					# 所属组织转移accountOrgChangeWin-iframe
					
					switch_to("xpath", "//iframe[@id='accountMaintainEventWin-iframe']")
					sleep(1)
					
					# 填写账户事件
					# 点击账户事件，新增第一行
					click("xpath", "//span[text()='新增行']")
					sleep(1)
					# 输入授信方式
					input("xpath", "//input[@id='editgrid-description-4']", "其他")
					sleep(1)
					input_down("xpath", "//input[@id='editgrid-description-4']")
					input_enter("xpath", "//input[@id='editgrid-description-4']")
					time.sleep(1)
					
					click("xpath", "//span[text()='保存']")
					sleep(1)
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("账户维护，编辑账户事件成功！")
					logging.info("账户维护，编辑账户事件成功！")
					sleep(3)
					
					# 切入‘账户维护’的iframe窗体
					switch_to("xpath", "//iframe[@id='bankAccounts-tab-iframe']")
					sleep(1)
					switch_to("xpath", "//iframe[@id='subTabOne-iframe']")
					sleep(1)
					
					# 修改勾选数据
					click("xpath", "//div[@title='账户状态:开户']/parent::*/preceding-sibling::*[7]/descendant::*[2]")
					
					# 用JS方便点击‘申请’按钮旁边的倒三角形
					js_click("xpath", "//span[text()='维护']/parent::*/following-sibling::*/child::*")
					sleep(1)
					
					# 点击申请开户按钮
					js_click("xpath", "//a[contains(text(),'所属组织转移')]")
					sleep(1)
					
					# 所属组织转移accountOrgChangeWin-iframe
					
					switch_to("xpath", "//iframe[@id='accountOrgChangeWin-iframe']")
					sleep(1)
					
					# 选择银行
					click("xpath", "//input[@id='combobox-input-orgid']")
					sleep(1)
					clear("xpath", "//input[@id='combobox-input-orgid']")
					sleep(1)
					# 输入银行名称，模糊查询
					input("xpath", "//input[@id='combobox-input-orgid']", "Mindy科技有限公司")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-orgid']")
					input_enter("xpath", "//input[@id='combobox-input-orgid']")
					time.sleep(1)
					
					click("xpath", "//span[text()='保存']")
					sleep(1)
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("账户维护-单币种账户，所属组织转移成功！")
					logging.info("账户维护-单币种账户，所属组织转移成功！")
					sleep(3)
				
				if i == 3:
					# 切入‘账户维护’的iframe窗体
					switch_to("xpath", "//iframe[@id='bankAccounts-tab-iframe']")
					sleep(1)
					switch_to("xpath", "//iframe[@id='subTabOne-iframe']")
					sleep(1)
					
					# 输入银行：农业银行
					click("xpath", "//input[@id='combobox-input-bankid']")
					sleep(1)
					# click("xpath", "//div[@title='代码-名称:ABC-农业银行']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
					# sleep(1)
					clear("xpath", "//input[@id='combobox-input-bankid']")
					sleep(1)
					input("xpath", "//input[@id='combobox-input-bankid']", "工商银行")
					sleep(1)
					click("xpath", "//div[@title='代码-名称:ICBC-工商银行']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
					sleep(1)
					
					# 点击查询
					click("xpath", "//span[text()='查询']")
					#
					# 修改勾选数据
					click("xpath", '//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
					
					# 点击送审按钮
					click("xpath", "//span[text()='审核']")
					
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					sleep(1)
					
					# 退出所有iframe窗体
					switch_default()
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'账户成功审核1条！')]")
					print("账户维护-单币种账户第%s次，审核成功！" % i)
					logging.info("账户维护-单币种账户第%s次，审核成功！" % i)
					time.sleep(3)
					
					# 切入‘账户维护’的iframe窗体
					switch_to("xpath", "//iframe[@id='bankAccounts-tab-iframe']")
					sleep(1)
					switch_to("xpath", "//iframe[@id='subTabOne-iframe']")
					sleep(1)
					
					# 修改勾选数据
					click("xpath", '//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
					
					# 用JS方便点击‘申请’按钮旁边的倒三角形
					js_click("xpath", "//span[text()='维护']/parent::*/following-sibling::*/child::*")
					sleep(1)
					
					js_click("xpath", "//a[contains(text(),'开户')]")
					sleep(1)
					
					# 选择开户日期
					today = date.today()
					open_date = today - timedelta(days=10)
					click("xpath", "//input[@id='openeddatewin-input']")
					sleep(1)
					clear("xpath", "//input[@id='openeddatewin-input']")
					sleep(1)
					input("xpath", "//input[@id='openeddatewin-input']", str(open_date))
					time.sleep(1)
					
					click("xpath", "//input[@id='initbalance-input']")
					sleep(1)
					clear("xpath", "//input[@id='initbalance-input']")
					sleep(1)
					input("xpath", "//input[@id='initbalance-input']", "30000")
					sleep(1)
					
					click("xpath", "//span[text()='确定']")
					sleep(1)
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("账户维护-单币种账户第%s次，开户成功！" % i)
					logging.info("账户维护-单币种账户第%s次，开户成功！" % i)
					time.sleep(3)
				
				if i == 4:
					# 切入‘账户维护’的iframe窗体
					switch_to("xpath", "//iframe[@id='bankAccounts-tab-iframe']")
					sleep(1)
					switch_to("xpath", "//iframe[@id='subTabOne-iframe']")
					sleep(1)
					
					# 输入银行：农业银行
					click("xpath", "//input[@id='combobox-input-bankid']")
					sleep(1)
					click("xpath", "//div[@title='代码-名称:ICBC-工商银行']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
					sleep(1)
					clear("xpath", "//input[@id='combobox-input-bankid']")
					sleep(1)
					input("xpath", "//input[@id='combobox-input-bankid']", "建设银行")
					sleep(1)
					click("xpath", "//div[@title='代码-名称:CCB-建设银行']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
					sleep(1)
					
					# 点击查询
					click("xpath", "//span[text()='查询']")
					#
					# 修改勾选数据
					click("xpath", '//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
					
					# 点击送审按钮
					click("xpath", "//span[text()='审核']")
					
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					sleep(1)
					
					# 退出所有iframe窗体
					switch_default()
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'账户成功审核1条！')]")
					print("账户维护-单币种账户第%s次，审核成功！" % i)
					logging.info("账户维护-单币种账户第%s次，审核成功！" % i)
					time.sleep(3)
					
					# 切入‘账户维护’的iframe窗体
					switch_to("xpath", "//iframe[@id='bankAccounts-tab-iframe']")
					sleep(1)
					switch_to("xpath", "//iframe[@id='subTabOne-iframe']")
					sleep(1)
					
					# 修改勾选数据
					click("xpath", '//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
					
					# 用JS方便点击‘申请’按钮旁边的倒三角形
					js_click("xpath", "//span[text()='维护']/parent::*/following-sibling::*/child::*")
					sleep(1)
					
					js_click("xpath", "//a[contains(text(),'开户')]")
					sleep(1)
					
					# 选择开户日期
					today = date.today()
					open_date = today - timedelta(days=10)
					click("xpath", "//input[@id='openeddatewin-input']")
					sleep(1)
					clear("xpath", "//input[@id='openeddatewin-input']")
					sleep(1)
					input("xpath", "//input[@id='openeddatewin-input']", str(open_date))
					time.sleep(1)
					
					click("xpath", "//input[@id='initbalance-input']")
					sleep(1)
					clear("xpath", "//input[@id='initbalance-input']")
					sleep(1)
					input("xpath", "//input[@id='initbalance-input']", "30000")
					sleep(1)
					
					click("xpath", "//span[text()='确定']")
					sleep(1)
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("账户维护-单币种账户第%s次，开户成功！" % i)
					logging.info("账户维护-单币种账户第%s次，开户成功！" % i)
					time.sleep(3)
				
				if i == 5:
					# 切入‘账户维护’的iframe窗体
					switch_to("xpath", "//iframe[@id='bankAccounts-tab-iframe']")
					sleep(1)
					switch_to("xpath", "//iframe[@id='subTabOne-iframe']")
					sleep(1)
					
					# 输入银行：农业银行
					click("xpath", "//input[@id='combobox-input-bankid']")
					sleep(1)
					click("xpath", "//div[@title='代码-名称:CCB-建设银行']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
					sleep(1)
					clear("xpath", "//input[@id='combobox-input-bankid']")
					sleep(1)
					input("xpath", "//input[@id='combobox-input-bankid']", "交通银行")
					sleep(1)
					click("xpath",
					      "//div[@title='代码-名称:BOCOM-交通银行']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
					sleep(1)
					
					# 点击查询
					click("xpath", "//span[text()='查询']")
					#
					# 修改勾选数据
					click("xpath", '//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
					
					# 点击送审按钮
					click("xpath", "//span[text()='审核']")
					
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					sleep(1)
					
					# 退出所有iframe窗体
					switch_default()
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'账户成功审核1条！')]")
					print("账户维护-单币种账户第%s次，审核成功！" % i)
					logging.info("账户维护-单币种账户第%s次，审核成功！" % i)
					time.sleep(3)
					
					# 切入‘账户维护’的iframe窗体
					switch_to("xpath", "//iframe[@id='bankAccounts-tab-iframe']")
					sleep(1)
					switch_to("xpath", "//iframe[@id='subTabOne-iframe']")
					sleep(1)
					
					# 修改勾选数据
					click("xpath", '//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
					
					# 用JS方便点击‘申请’按钮旁边的倒三角形
					js_click("xpath", "//span[text()='维护']/parent::*/following-sibling::*/child::*")
					sleep(1)
					
					js_click("xpath", "//a[contains(text(),'开户')]")
					sleep(1)
					
					# 选择开户日期
					today = date.today()
					open_date = today - timedelta(days=10)
					click("xpath", "//input[@id='openeddatewin-input']")
					sleep(1)
					clear("xpath", "//input[@id='openeddatewin-input']")
					sleep(1)
					input("xpath", "//input[@id='openeddatewin-input']", str(open_date))
					time.sleep(1)
					
					click("xpath", "//input[@id='initbalance-input']")
					sleep(1)
					clear("xpath", "//input[@id='initbalance-input']")
					sleep(1)
					input("xpath", "//input[@id='initbalance-input']", "30000")
					sleep(1)
					
					click("xpath", "//span[text()='确定']")
					sleep(1)
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("账户维护-单币种账户第%s次，开户成功！" % i)
					logging.info("账户维护-单币种账户第%s次，开户成功！" % i)
					time.sleep(3)
				
				if i == 6:
					# 切入‘账户维护’的iframe窗体
					switch_to("xpath", "//iframe[@id='bankAccounts-tab-iframe']")
					sleep(1)
					switch_to("xpath", "//iframe[@id='subTabOne-iframe']")
					sleep(1)
					
					# 输入银行：农业银行
					click("xpath", "//input[@id='combobox-input-bankid']")
					sleep(1)
					click("xpath",
					      "//div[@title='代码-名称:BOCOM-交通银行']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
					sleep(1)
					clear("xpath", "//input[@id='combobox-input-bankid']")
					sleep(1)
					input("xpath", "//input[@id='combobox-input-bankid']", "华夏银行")
					sleep(1)
					click("xpath", "//div[@title='代码-名称:HXB-华夏银行']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
					sleep(1)
					
					# 点击查询
					click("xpath", "//span[text()='查询']")
					#
					# 修改勾选数据
					click("xpath", '//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
					
					# 点击送审按钮
					click("xpath", "//span[text()='审核']")
					
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					sleep(1)
					
					# 退出所有iframe窗体
					switch_default()
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'账户成功审核1条！')]")
					print("账户维护第%s次，审核成功！" % i)
					logging.info("账户维护第%s次，审核成功！" % i)
					time.sleep(3)
					
					# 切入‘账户维护’的iframe窗体
					switch_to("xpath", "//iframe[@id='bankAccounts-tab-iframe']")
					sleep(1)
					switch_to("xpath", "//iframe[@id='subTabOne-iframe']")
					sleep(1)
					
					# 修改勾选数据
					click("xpath", '//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
					
					# 用JS方便点击‘申请’按钮旁边的倒三角形
					js_click("xpath", "//span[text()='维护']/parent::*/following-sibling::*/child::*")
					sleep(1)
					
					js_click("xpath", "//a[contains(text(),'开户')]")
					sleep(1)
					
					# 选择开户日期
					today = date.today()
					open_date = today - timedelta(days=10)
					click("xpath", "//input[@id='openeddatewin-input']")
					sleep(1)
					clear("xpath", "//input[@id='openeddatewin-input']")
					sleep(1)
					input("xpath", "//input[@id='openeddatewin-input']", str(open_date))
					time.sleep(1)
					
					# 输入初始余额
					click("xpath", "//input[@id='initbalance-input']")
					sleep(1)
					clear("xpath", "//input[@id='initbalance-input']")
					sleep(1)
					input("xpath", "//input[@id='initbalance-input']", "30000")
					sleep(1)
					
					click("xpath", "//span[text()='确定']")
					sleep(1)
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("账户维护-单币种账户第%s次，开户成功！" % i)
					logging.info("账户维护-单币种账户第%s次，开户成功！" % i)
					time.sleep(3)
				if i == 7:
					# 切入‘账户维护’的iframe窗体
					switch_to("xpath", "//iframe[@id='bankAccounts-tab-iframe']")
					sleep(1)
					switch_to("xpath", "//iframe[@id='subTabOne-iframe']")
					sleep(1)
					
					# # 输入银行：农业银行
					# click("xpath", "//input[@id='combobox-input-bankid']")
					# sleep(1)
					# click("xpath",
					# 	  "//div[@title='代码-名称:HXB-华夏银行']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
					# sleep(1)
					# clear("xpath", "//input[@id='combobox-input-bankid']")
					# sleep(1)
					# input("xpath", "//input[@id='combobox-input-bankid']", "中国银行")
					# sleep(1)
					# click("xpath", "//div[@title='代码-名称:BOC-中国银行']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
					# sleep(1)
					
					# 点击查询
					click("xpath", "//span[text()='查询']")
					#
					# 修改勾选数据
					click("xpath", '//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
					
					# 点击送审按钮
					click("xpath", "//span[text()='审核']")
					
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					sleep(1)
					
					# 退出所有iframe窗体
					switch_default()
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'账户成功审核1条！')]")
					print("账户维护第%s次，审核成功！" % i)
					logging.info("账户维护第%s次，审核成功！" % i)
					time.sleep(3)
					
					# 切入‘账户维护’的iframe窗体
					switch_to("xpath", "//iframe[@id='bankAccounts-tab-iframe']")
					sleep(1)
					switch_to("xpath", "//iframe[@id='subTabOne-iframe']")
					sleep(1)
					
					# 修改勾选数据
					click("xpath", '//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
					
					# 用JS方便点击‘申请’按钮旁边的倒三角形
					js_click("xpath", "//span[text()='维护']/parent::*/following-sibling::*/child::*")
					sleep(1)
					
					js_click("xpath", "//a[contains(text(),'开户')]")
					sleep(1)
					
					# 选择开户日期
					today = date.today()
					open_date = today - timedelta(days=10)
					click("xpath", "//input[@id='openeddatewin-input']")
					sleep(1)
					clear("xpath", "//input[@id='openeddatewin-input']")
					sleep(1)
					input("xpath", "//input[@id='openeddatewin-input']", str(open_date))
					time.sleep(1)
					
					click("xpath", "//input[@id='journalbalance-input']")
					sleep(1)
					clear("xpath", "//input[@id='journalbalance-input']")
					sleep(1)
					input("xpath", "//input[@id='journalbalance-input']", "30000")
					sleep(1)
					
					click("xpath", "//span[text()='确定']")
					sleep(1)
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("账户维护-单币种账户第%s次，开户成功！" % i)
					logging.info("账户维护-单币种账户第%s次，开户成功！" % i)
					time.sleep(3)
				
				if i == 8:
					# 切入‘账户维护’的iframe窗体
					switch_to("xpath", "//iframe[@id='bankAccounts-tab-iframe']")
					sleep(1)
					switch_to("xpath", "//iframe[@id='subTabOne-iframe']")
					sleep(1)
					
					# 输入银行：农业银行
					click("xpath", "//input[@id='combobox-input-bankid']")
					sleep(1)
					click("xpath", "//div[@title='代码-名称:BOC-中国银行']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
					sleep(1)
					clear("xpath", "//input[@id='combobox-input-bankid']")
					sleep(1)
					input("xpath", "//input[@id='combobox-input-bankid']", "农业银行")
					sleep(1)
					# click("xpath", "//div[@title='代码-名称:ABC-农业银行']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
					# sleep(1)
					
					# 点击查询
					click("xpath", "//span[text()='查询']")
					
					# 修改勾选数据
					click("xpath", '//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
					
					# 点击送审按钮
					click("xpath", "//span[text()='审核']")
					
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					sleep(1)
					
					# 退出所有iframe窗体
					switch_default()
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'账户成功审核1条！')]")
					print("账户维护-单币种账户第%s次，审核成功！" % i)
					logging.info("账户维护-单币种账户第%s次，审核成功！" % i)
					time.sleep(3)
					
					# 切入‘账户维护’的iframe窗体
					switch_to("xpath", "//iframe[@id='bankAccounts-tab-iframe']")
					sleep(1)
					switch_to("xpath", "//iframe[@id='subTabOne-iframe']")
					sleep(1)
					
					# 修改勾选数据
					click("xpath", '//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
					
					# 用JS方便点击‘申请’按钮旁边的倒三角形
					js_click("xpath", "//span[text()='维护']/parent::*/following-sibling::*/child::*")
					sleep(1)
					
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
					
					click("xpath", "//input[@id='journalbalance-input']")
					sleep(1)
					clear("xpath", "//input[@id='journalbalance-input']")
					sleep(1)
					input("xpath", "//input[@id='journalbalance-input']", "30000")
					sleep(1)
					
					click("xpath", "//span[text()='确定']")
					sleep(1)
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("账户维护-单币种账户第%s次，开户成功！" % i)
					logging.info("账户维护-单币种账户第%s次，开户成功！" % i)
					time.sleep(3)
				
				if i == 9:
					# 切入‘账户维护’的iframe窗体
					switch_to("xpath", "//iframe[@id='bankAccounts-tab-iframe']")
					sleep(1)
					switch_to("xpath", "//iframe[@id='subTabOne-iframe']")
					sleep(1)
					
					# 输入银行：农业银行
					click("xpath", "//input[@id='combobox-input-bankid']")
					sleep(1)
					click("xpath", "//div[@title='代码-名称:ABC-农业银行']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
					sleep(1)
					clear("xpath", "//input[@id='combobox-input-bankid']")
					sleep(1)
					input("xpath", "//input[@id='combobox-input-bankid']", "中国银行")
					sleep(1)
					click("xpath", "//div[@title='代码-名称:BOC-中国银行']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
					sleep(1)
					
					# 点击查询
					click("xpath", "//span[text()='查询']")
					
					# 修改勾选数据
					click("xpath", '//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
					
					# 点击送审按钮
					click("xpath", "//span[text()='审核']")
					
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					sleep(1)
					
					# 退出所有iframe窗体
					switch_default()
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'账户成功审核1条！')]")
					print("账户维护第%s次，审核成功！" % i)
					logging.info("账户维护第%s次，审核成功！" % i)
					time.sleep(3)
					
					# 切入‘账户维护’的iframe窗体
					switch_to("xpath", "//iframe[@id='bankAccounts-tab-iframe']")
					sleep(1)
					switch_to("xpath", "//iframe[@id='subTabOne-iframe']")
					sleep(1)
					
					# 修改勾选数据
					click("xpath", '//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
					
					# 用JS方便点击‘申请’按钮旁边的倒三角形
					js_click("xpath", "//span[text()='维护']/parent::*/following-sibling::*/child::*")
					sleep(1)
					
					js_click("xpath", "//a[contains(text(),'开户')]")
					sleep(1)
					
					# 选择开户日期
					today = date.today()
					open_date = today - timedelta(days=10)
					click("xpath", "//input[@id='openeddatewin-input']")
					sleep(1)
					clear("xpath", "//input[@id='openeddatewin-input']")
					sleep(1)
					input("xpath", "//input[@id='openeddatewin-input']", str(open_date))
					time.sleep(1)
					
					# 输入初始余额
					click("xpath", "//input[@id='initbalance-input']")
					sleep(1)
					clear("xpath", "//input[@id='initbalance-input']")
					sleep(1)
					input("xpath", "//input[@id='initbalance-input']", "30000")
					sleep(1)
					
					click("xpath", "//span[text()='确定']")
					sleep(1)
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("账户维护-单币种账户第%s次，开户成功！" % i)
					logging.info("账户维护-单币种账户第%s次，开户成功！" % i)
					time.sleep(3)
				
				if i == 10:
					# 切入‘账户维护’的iframe窗体
					switch_to("xpath", "//iframe[@id='bankAccounts-tab-iframe']")
					sleep(1)
					switch_to("xpath", "//iframe[@id='subTabOne-iframe']")
					sleep(1)
					
					# 输入银行：农业银行
					click("xpath", "//input[@id='combobox-input-bankid']")
					sleep(1)
					click("xpath", "//div[@title='代码-名称:BOC-中国银行']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
					sleep(1)
					clear("xpath", "//input[@id='combobox-input-bankid']")
					sleep(1)
					input("xpath", "//input[@id='combobox-input-bankid']", "华夏银行")
					sleep(1)
					click("xpath", "//div[@title='代码-名称:HXB-华夏银行']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
					sleep(1)
					
					# 点击查询
					click("xpath", "//span[text()='查询']")
					#
					# 修改勾选数据
					click("xpath", '//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
					
					# 点击送审按钮
					click("xpath", "//span[text()='审核']")
					
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					sleep(1)
					
					# 退出所有iframe窗体
					switch_default()
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'账户成功审核1条！')]")
					print("账户维护第%s次，审核成功！" % i)
					logging.info("账户维护第%s次，审核成功！" % i)
					time.sleep(3)
					
					# 切入‘账户维护’的iframe窗体
					switch_to("xpath", "//iframe[@id='bankAccounts-tab-iframe']")
					sleep(1)
					switch_to("xpath", "//iframe[@id='subTabOne-iframe']")
					sleep(1)
					
					# 修改勾选数据
					click("xpath", '//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
					
					# 用JS方便点击‘申请’按钮旁边的倒三角形
					js_click("xpath", "//span[text()='维护']/parent::*/following-sibling::*/child::*")
					sleep(1)
					
					js_click("xpath", "//a[contains(text(),'开户')]")
					sleep(1)
					
					# 选择开户日期
					today = date.today()
					open_date = today - timedelta(days=10)
					click("xpath", "//input[@id='openeddatewin-input']")
					sleep(1)
					clear("xpath", "//input[@id='openeddatewin-input']")
					sleep(1)
					input("xpath", "//input[@id='openeddatewin-input']", str(open_date))
					time.sleep(1)
					
					# 输入初始余额
					click("xpath", "//input[@id='journalbalance-input']")
					sleep(1)
					clear("xpath", "//input[@id='journalbalance-input']")
					sleep(1)
					input("xpath", "//input[@id='journalbalance-input']", "30000")
					sleep(1)
					
					click("xpath", "//span[text()='确定']")
					sleep(1)
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("账户维护-单币种账户第%s次，开户成功！" % i)
					logging.info("账户维护-单币种账户第%s次，开户成功！" % i)
					time.sleep(3)
			
			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='账户维护']/child::*[1]")
			
			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//span[text()='账户生命周期']")
			# 打印操作成功日志
			print("账户维护-单币种账户，操作成功!")
			logging.info("账户维护-单币种账户，操作成功!")
			time.sleep(2)
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("账户维护-单币种账户失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		
		# 开始测试账户资金监控--账户生命周期--账户申请
		
		# 测试账户生命周期--账户申请
		try:
			# 点击账户生命周期'菜单
			click("xpath", "//span[text()='账户生命周期']")
			# 点击账户申请菜单
			click("xpath", "//span[text()='账户申请']")
			# 退出所有iframe窗体
			switch_default()
			
			for i in range(1, 3):
				
				# 切入账户申请的iframe窗体
				switch_to("xpath", "//iframe[@id='bankAccountApply-tab-iframe']")
				logging.info("开始测试账户申请功能")
				
				# 用JS方便点击‘申请’按钮旁边的倒三角形
				js_click("xpath", "//span[text()='申请']/parent::*/following-sibling::*/child::*")
				sleep(1)
				
				# 点击申请开户按钮
				js_click("xpath", "//a[contains(text(),'申请开户')]")
				sleep(1)
				
				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='kaihuWin-iframe']")
				sleep(1)
				
				# 第一次选择中国银行/第二次选择工商银行/第三次选择农业银行
				
				if i == 1:
					# 选择银行
					click("xpath", "//input[@id='combobox-input-bankid']")
					# 输入银行名称，模糊查询
					input("xpath", "//input[@id='combobox-input-bankid']", "中国银行")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-bankid']")
					input_enter("xpath", "//input[@id='combobox-input-bankid']")
					time.sleep(1)
					
					# 选择开户行
					click("xpath", "//input[@id='combobox-input-banklocationid']")
					# 输入开户行大连泡崖街支行名称，模糊查询
					input("xpath", "//input[@id='combobox-input-banklocationid']", "大连泡崖")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-banklocationid']")
					input_enter("xpath", "//input[@id='combobox-input-banklocationid']")
					time.sleep(1)
					
					# 选择币种id="combobox-input-currencyid"
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
					
					# 选择账户存款类型combobox-input-deposittype
					click("xpath", "//input[@id='combobox-input-deposittype']")
					# 输入开户行大连泡崖街支行名称，模糊查询
					input("xpath", "//input[@id='combobox-input-deposittype']", "活期")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-deposittype']")
					input_enter("xpath", "//input[@id='combobox-input-deposittype']")
					time.sleep(1)
					
					# 填写地址
					input("xpath", "//input[@id='accountaddress']", "甘肃定西")
					sleep(1)
					
					# 选择常驻国家性质
					click("xpath", "//input[@id='combobox-input-countrytype']")
					# 输入开户行大连泡崖街支行名称，模糊查询
					input("xpath", "//input[@id='combobox-input-countrytype']", "一般贸易区")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-countrytype']")
					input_enter("xpath", "//input[@id='combobox-input-countrytype']")
					time.sleep(1)
					
					# 选择账户分类
					click("xpath", "//input[@id='combobox-input-accountclassid']")
					# 输入开户行大连泡崖街支行名称，模糊查询
					input("xpath", "//input[@id='combobox-input-accountclassid']", "自动化测试账户分类")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-accountclassid']")
					input_enter("xpath", "//input[@id='combobox-input-accountclassid']")
					time.sleep(1)
					
					# 选择收付属性
					click("xpath", "//input[@id='combobox-input-paymentattribute']")
					# 输入开户行大连泡崖街支行名称，模糊查询
					input("xpath", "//input[@id='combobox-input-paymentattribute']", "自动化测试账户分类")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-paymentattribute']")
					input_enter("xpath", "//input[@id='combobox-input-paymentattribute']")
					
					# 选择银企直联户/现金虚拟户/票据虚拟户
					# 第一次选择银企直联户
					click("xpath", "//input[@id='isbankdirect']")
					
					# 是否集团代管
					click("xpath", "//input[@id='istakeover']")
					sleep(1)
					# 选择境内外
					click("xpath", "//input[@id='combobox-input-inorout']")
					# 输入开户行大连泡崖街支行名称，模糊查询
					input("xpath", "//input[@id='combobox-input-inorout']", "境内")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-inorout']")
					input_enter("xpath", "//input[@id='combobox-input-inorout']")
					
					# 输入申请原因
					input("xpath", "//textarea[@id='applyreason']", "自动化测试申请原因")
					sleep(1)
					
					# 选择账户到期日
					today = date.today()
					accountdatedue = today + timedelta(days=720)
					click("xpath", "//input[@id='accountdatedue-input']")
					sleep(1)
					clear("xpath", "//input[@id='accountdatedue-input']")
					sleep(1)
					input("xpath", "//input[@id='accountdatedue-input']", str(accountdatedue))
					# 模拟回车键
					keyDown('enter')
					keyUp('enter')
					time.sleep(2)
					
					# 点击保存按钮
					click("xpath", "//span[text()='保存']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("申请开户第%s次，保存成功！" % i)
					logging.info("申请开户第%s次，保存成功！" % i)
					time.sleep(3)
				
				else:
					# 选择银行
					click("xpath", "//input[@id='combobox-input-bankid']")
					# 输入银行名称，模糊查询
					input("xpath", "//input[@id='combobox-input-bankid']", "农业银行")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-bankid']")
					input_enter("xpath", "//input[@id='combobox-input-bankid']")
					time.sleep(1)
					
					# 选择开户行
					click("xpath", "//input[@id='combobox-input-banklocationid']")
					# 输入开户行大连泡崖街支行名称，模糊查询
					input("xpath", "//input[@id='combobox-input-banklocationid']", "彭泽县支行")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-banklocationid']")
					input_enter("xpath", "//input[@id='combobox-input-banklocationid']")
					time.sleep(1)
					
					# 选择币种id="combobox-input-currencyid"
					click("xpath", "//input[@id='combobox-input-currencyid']")
					# 输入开户行大连泡崖街支行名称，模糊查询
					input("xpath", "//input[@id='combobox-input-currencyid']", "USD")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-currencyid']")
					input_enter("xpath", "//input[@id='combobox-input-currencyid']")
					time.sleep(1)
					
					# 选择账户性质
					click("xpath", "//input[@id='combobox-input-accounttypeid']")
					# 输入开户行大连泡崖街支行名称，模糊查询
					input("xpath", "//input[@id='combobox-input-accounttypeid']", "一般户")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-accounttypeid']")
					input_enter("xpath", "//input[@id='combobox-input-accounttypeid']")
					time.sleep(1)
					
					# 选择账户存款类型combobox-input-deposittype
					click("xpath", "//input[@id='combobox-input-deposittype']")
					# 输入开户行大连泡崖街支行名称，模糊查询
					input("xpath", "//input[@id='combobox-input-deposittype']", "定期")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-deposittype']")
					input_enter("xpath", "//input[@id='combobox-input-deposittype']")
					time.sleep(1)
					
					# 填写地址
					input("xpath", "//input[@id='accountaddress']", "甘肃定西")
					sleep(1)
					
					# # 选择常驻国家性质
					# click("xpath", "//input[@id='combobox-input-countrytype']")
					# # 输入开户行大连泡崖街支行名称，模糊查询
					# input("xpath", "//input[@id='combobox-input-countrytype']", "保税区")
					# sleep(1)
					# input_down("xpath", "//input[@id='combobox-input-countrytype']")
					# input_enter("xpath", "//input[@id='combobox-input-countrytype']")
					# time.sleep(1)
					
					# 选择账户分类
					click("xpath", "//input[@id='combobox-input-accountclassid']")
					# 输入开户行大连泡崖街支行名称，模糊查询
					input("xpath", "//input[@id='combobox-input-accountclassid']", "自动化测试账户分类")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-accountclassid']")
					input_enter("xpath", "//input[@id='combobox-input-accountclassid']")
					time.sleep(1)
					
					# 选择收付属性
					click("xpath", "//input[@id='combobox-input-paymentattribute']")
					# 输入开户行大连泡崖街支行名称，模糊查询
					input("xpath", "//input[@id='combobox-input-paymentattribute']", "支出账户")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-paymentattribute']")
					input_enter("xpath", "//input[@id='combobox-input-paymentattribute']")
					
					# 选择银企直联户/现金虚拟户/票据虚拟户
					# 第二次选择现金虚拟户
					click("xpath", "//input[@id='iscashvirtual']")
					
					# 是否集团代管
					click("xpath", "//input[@id='istakeover']")
					sleep(1)
					# 选择境内外
					click("xpath", "//input[@id='combobox-input-inorout']")
					# 输入开户行大连泡崖街支行名称，模糊查询
					input("xpath", "//input[@id='combobox-input-inorout']", "境外")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-inorout']")
					input_enter("xpath", "//input[@id='combobox-input-inorout']")
					
					# 输入申请原因
					input("xpath", "//textarea[@id='applyreason']", "自动化测试申请原因")
					sleep(1)
					
					# 选择账户到期日
					today = date.today()
					accountdatedue = today + timedelta(days=720)
					click("xpath", "//input[@id='accountdatedue-input']")
					sleep(1)
					clear("xpath", "//input[@id='accountdatedue-input']")
					sleep(1)
					input("xpath", "//input[@id='accountdatedue-input']", str(accountdatedue))
					# 模拟回车键
					keyDown('enter')
					keyUp('enter')
					time.sleep(2)
					
					# 点击保存按钮
					click("xpath", "//span[text()='保存']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("申请开户第%s次，保存成功！" % i)
					logging.info("申请开户第%s次，保存成功！" % i)
					time.sleep(3)
				
				# 第一笔，就先修改，再修改页面提交送审，再撤销送审，再删除
				if i == 1:
					# 切入‘账户申请’的iframe窗体
					switch_to("xpath", "//iframe[@id='bankAccountApply-tab-iframe']")
					
					# 点击查看
					# 用JS的方法点击放大镜
					js_click("xpath", "//span[@class='f-contrac-close']")
					sleep(1)
					
					# 输入银行：中国银行
					click("xpath", "//input[@id='combobox-input-bankid']")
					sleep(1)
					input("xpath", "//input[@id='combobox-input-bankid']", "中国银行")
					sleep(1)
					click("xpath", "//div[@title='代码-名称:BOC-中国银行']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
					sleep(1)
					
					# 审批状态：未审批
					click("xpath", "//input[@id='combobox-input-approvestate']")
					sleep(1)
					input("xpath", "//input[@id='combobox-input-approvestate']", "未审批")
					sleep(1)
					click("xpath", "//div[@title='未审批']")
					sleep(1)
					
					# 点击查询
					click("xpath", "//span[text()='查询']")
					
					# 修改勾选数据
					click("xpath", "//div[@title='审批状态:未审批']/parent::*/preceding-sibling::*[2]/descendant::*[2]")
					
					# 点击修改按钮
					click("xpath", "//span[text()='修改']")
					
					# 切入修改的iframe窗体
					switch_to("xpath", "//iframe[@id='eidteWin-iframe']")
					sleep(1)
					
					# 输入申请原因
					input("xpath", "//textarea[@id='applyreason']", "自动化测试申请原因修改原因")
					sleep(1)
					
					# 点击保存按钮
					click("xpath", "//span[text()='保存']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("申请开户，修改成功！")
					logging.info("申请开户，修改成功！")
					time.sleep(3)
					
					# 切入‘账户申请’的iframe窗体
					switch_to("xpath", "//iframe[@id='bankAccountApply-tab-iframe']")
					
					# 修改勾选数据
					click("xpath", "//div[@title='审批状态:未审批']/parent::*/preceding-sibling::*[2]/descendant::*[2]")
					
					# 点击删除按钮
					click("xpath", "//span[text()='删除']")
					
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现删除的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("申请开户，删除成功！")
					logging.info("申请开户，删除成功！")
					time.sleep(3)
				
				# 第二笔，测试送审的流程，送审，双击页面同意，退回，送审，同意
				if i == 2:
					# 切入‘账户申请’的iframe窗体
					switch_to("xpath", "//iframe[@id='bankAccountApply-tab-iframe']")
					
					# 输入银行：中国银行
					click("xpath", "//input[@id='combobox-input-bankid']")
					sleep(1)
					# click("xpath", "//div[@title='代码-名称:BOC-中国银行']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
					# sleep(1)
					clear("xpath", "//input[@id='combobox-input-bankid']")
					sleep(1)
					input("xpath", "//input[@id='combobox-input-bankid']", "农业银行")
					sleep(1)
					click("xpath", "//div[@title='代码-名称:ABC-农业银行']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
					sleep(1)
					
					# 取消已勾选的未审核条件
					click("xpath", "//input[@id='combobox-input-approvestate']")
					sleep(1)
					click("xpath", "//div[@title='未审批']")
					sleep(1)
					
					# 点击查询
					click("xpath", "//span[text()='查询']")
					
					# 勾选未审批数据
					click("xpath", "//div[@title='审批状态:未审批']/parent::*/preceding-sibling::*[2]/descendant::*[2]")
					
					# 点击送审按钮
					click("xpath", "//span[text()='送审']")
					
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					sleep(1)
					
					# 退出所有iframe窗体
					switch_default()
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'送审成功！')]")
					print("申请开户，第一次送审成功！")
					logging.info("申请开户，第一次送审成功！")
					time.sleep(3)
					
					# 切入‘账户申请’的iframe窗体
					switch_to("xpath", "//iframe[@id='bankAccountApply-tab-iframe']")
					
					# 双击勾选数据
					double_click("xpath", "//div[@title='审批状态:审批中']/parent::*/preceding-sibling::*[2]/descendant::*[2]")
					sleep(1)
					
					switch_to("xpath", "//iframe[@id='wf_taskProcessing_win-iframe']")
					sleep(3)
					
					click("xpath", "//span[text()='同意']")
					sleep(1)
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("申请开户，第一次审批同意成功！")
					logging.info("申请开户，第一次审批同意成功！")
					time.sleep(3)
					
					# 切入‘账户申请’的iframe窗体
					switch_to("xpath", "//iframe[@id='bankAccountApply-tab-iframe']")
					
					# 双击勾选数据
					double_click("xpath", "//div[@title='审批状态:审批中']/parent::*/preceding-sibling::*[2]/descendant::*[2]")
					sleep(1)
					
					switch_to("xpath", "//iframe[@id='wf_taskProcessing_win-iframe']")
					sleep(2)
					
					click("xpath", "//span[text()='终审']")
					sleep(1)
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("申请开户，第一次终审成功！")
					logging.info("申请开户，第一次终审成功！")
					time.sleep(3)
					
					# 切入账户申请的iframe窗体
					switch_to("xpath", "//iframe[@id='bankAccountApply-tab-iframe']")
					
					# 修改勾选数据
					click("xpath", "//div[@title='审批状态:已审批']/parent::*/preceding-sibling::*[2]/descendant::*[2]")
					
					# 用JS方便点击‘申请’按钮旁边的倒三角形
					js_click("xpath", "//span[text()='申请']/parent::*/following-sibling::*/child::*")
					sleep(1)
					
					# 点击申请开户按钮
					js_click("xpath", "//a[contains(text(),'申请变更')]")
					sleep(1)
					
					switch_to("xpath", "//iframe[@id='biangengWin-iframe']")
					
					# 选择银行
					click("xpath", "//input[@id='combobox-input-bankid']")
					# 输入银行名称，模糊查询
					input("xpath", "//input[@id='combobox-input-bankid']", "ABC-农业银行")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-bankid']")
					input_enter("xpath", "//input[@id='combobox-input-bankid']")
					time.sleep(1)
					
					# 选择银行账户
					click("xpath", "//input[@id='combobox-input-accountid']")
					# 输入银行名称，模糊查询
					input("xpath", "//input[@id='combobox-input-accountid']", "中国农业银行")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-accountid']")
					input_enter("xpath", "//input[@id='combobox-input-accountid']")
					time.sleep(1)
					
					# 描述框中填入值
					input("xpath", "//textarea[@id='applyreason']", "自动化测试账户申请变更申请原因框")
					sleep(1)
					
					# 点击其它信息
					click("xpath", "//span[contains(text(),'其它信息')]")
					sleep(1)
					
					# 填写财务系统总账科目
					input("xpath", "//input[@id='otherglaccount']", "自动化测试财务系统总账科目")
					sleep(1)
					
					# 填写财务系统银行账号
					input("xpath", "//input[@id='otheraccountnumber']", "202004051530")
					sleep(1)
					
					# # 点击扩展信息
					# click("xpath", "//span[contains(text(),'扩展信息')]")
					# sleep(1)
					#
					# # 勾选第一条扩展信息
					# click("xpath", "//input[@id='extend1']")
					# sleep(1)
					
					# 勾选扩展信息日期
					# 缺少扩展信息
					
					# 点击清算条件
					click("xpath", "//span[contains(text(),'清算条件')]")
					sleep(1)
					
					# 填写满额上划金额
					click("xpath", "//input[@id='miniuptransferamount-input']")
					sleep(1)
					clear("xpath", "//input[@id='miniuptransferamount-input']")
					sleep(1)
					input("xpath", "//input[@id='miniuptransferamount-input']", "1")
					sleep(1)
					
					# 填写最小划拨金额
					clear("xpath", "//input[@id='minitransferamount-input']")
					sleep(1)
					input("xpath", "//input[@id='minitransferamount-input']", "1")
					sleep(1)
					
					# 缺少附件上传
					
					# 点击确定按钮
					click("xpath", "//span[text()='保存']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("账户申请，申请变更成功！")
					logging.info("账户申请，申请变更成功！")
					sleep(3)
					
					# 切入账户申请的iframe窗体
					switch_to("xpath", "//iframe[@id='bankAccountApply-tab-iframe']")
					
					# 修改勾选数据
					# click("xpath", "//div[@title='审批状态:已审批']/parent::*/preceding-sibling::*[2]/descendant::*[2]")
					#
					# 用JS方便点击‘申请’按钮旁边的倒三角形
					js_click("xpath", "//span[text()='申请']/parent::*/following-sibling::*/child::*")
					sleep(1)
					
					# 点击申请开户按钮
					js_click("xpath", "//a[contains(text(),'申请冻结')]")
					sleep(1)
					
					switch_to("xpath", "//iframe[@id='dongjieWin-iframe']")
					sleep(1)
					
					# 选择银行
					click("xpath", "//input[@id='combobox-input-bankid']")
					# 输入银行名称，模糊查询
					input("xpath", "//input[@id='combobox-input-bankid']", "ABC-农业银行")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-bankid']")
					input_enter("xpath", "//input[@id='combobox-input-bankid']")
					time.sleep(1)
					
					# 选择银行账户
					click("xpath", "//input[@id='combobox-input-accountid']")
					# 输入银行名称，模糊查询
					input("xpath", "//input[@id='combobox-input-accountid']", "USD")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-accountid']")
					input_enter("xpath", "//input[@id='combobox-input-accountid']")
					time.sleep(1)
					
					# 描述框中填入值
					input("xpath", "//textarea[@id='applyreason']", "自动化测试账户申请冻结申请原因框")
					sleep(1)
					
					# 点击确定按钮
					click("xpath", "//span[text()='保存']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("账户申请，申请冻结成功！")
					logging.info("账户申请，申请冻结成功！")
					sleep(3)
					
					# 切入‘账户申请’的iframe窗体
					switch_to("xpath", "//iframe[@id='bankAccountApply-tab-iframe']")
					
					# # 输入银行：中国银行
					# click("xpath", "//input[@id='combobox-input-bankid']")
					# sleep(1)
					# click("xpath", "//div[@title='代码-名称:ABC-农业银行']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
					# sleep(1)
					# clear("xpath", "//input[@id='combobox-input-bankid']")
					# sleep(1)
					# input("xpath", "//input[@id='combobox-input-bankid']", "工商银行")
					# sleep(1)
					# click("xpath", "//div[@title='代码-名称:ICBC-工商银行']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
					# sleep(1)
					
					# 取消已勾选的未审核条件
					click("xpath", "//input[@id='combobox-input-maintainflag']")
					sleep(1)
					click("xpath", "//div[@title='冻结']")
					sleep(1)
					
					# 点击查询
					click("xpath", "//span[text()='查询']")
					
					# 勾选未审批数据
					click("xpath", "//div[@title='申请类型:冻结']/parent::*/preceding-sibling::*[4]/descendant::*[2]")
					sleep(1)
					# 点击送审按钮
					click("xpath", "//span[text()='送审']")
					sleep(1)
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					sleep(1)
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'送审成功！')]")
					print("申请冻结，送审成功！")
					logging.info("申请冻结，送审成功！")
					time.sleep(3)
					
					# 切入‘账户申请’的iframe窗体
					switch_to("xpath", "//iframe[@id='bankAccountApply-tab-iframe']")
					
					# 双击勾选数据
					double_click("xpath", "//div[@title='审批状态:审批中']/parent::*/preceding-sibling::*[2]/descendant::*[2]")
					sleep(1)
					
					switch_to("xpath", "//iframe[@id='wf_taskProcessing_win-iframe']")
					sleep(3)
					
					click("xpath", "//span[text()='同意']")
					sleep(1)
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("申请冻结，第一次审批同意成功！")
					logging.info("申请冻结，第一次审批同意成功！")
					time.sleep(3)
					
					# 切入‘账户申请’的iframe窗体
					switch_to("xpath", "//iframe[@id='bankAccountApply-tab-iframe']")
					
					# 双击勾选数据
					double_click("xpath", "//div[@title='审批状态:审批中']/parent::*/preceding-sibling::*[2]/descendant::*[2]")
					sleep(1)
					
					switch_to("xpath", "//iframe[@id='wf_taskProcessing_win-iframe']")
					sleep(2)
					
					click("xpath", "//span[text()='同意']")
					sleep(1)
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("申请冻结，第二次审批同意成功！")
					logging.info("申请冻结，第二次审批同意成功！")
					time.sleep(3)
					
					# 申请解冻
					# 切入账户申请的iframe窗体
					switch_to("xpath", "//iframe[@id='bankAccountApply-tab-iframe']")
					
					# 用JS方便点击‘申请’按钮旁边的倒三角形
					js_click("xpath", "//span[text()='申请']/parent::*/following-sibling::*/child::*")
					sleep(1)
					
					# 点击申请开户按钮
					js_click("xpath", "//a[contains(text(),'申请解冻')]")
					sleep(1)
					
					switch_to("xpath", "//iframe[@id='jiedongWin-iframe']")
					
					# 选择银行
					click("xpath", "//input[@id='combobox-input-bankid']")
					# 输入银行名称，模糊查询
					input("xpath", "//input[@id='combobox-input-bankid']", "农业银行")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-bankid']")
					input_enter("xpath", "//input[@id='combobox-input-bankid']")
					time.sleep(1)
					
					# 选择银行账户
					click("xpath", "//input[@id='combobox-input-accountid']")
					# 输入银行名称，模糊查询
					input("xpath", "//input[@id='combobox-input-accountid']", "USD")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-accountid']")
					input_enter("xpath", "//input[@id='combobox-input-accountid']")
					time.sleep(1)
					
					# 描述框中填入值
					input("xpath", "//textarea[@id='applyreason']", "自动化测试账户申请解冻申请原因框")
					sleep(1)
					
					# 点击确定按钮
					click("xpath", "//span[text()='保存']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("账户申请，申请解冻成功！")
					logging.info("账户申请，申请解冻成功！")
					sleep(3)
					
					# 切入‘账户申请’的iframe窗体
					switch_to("xpath", "//iframe[@id='bankAccountApply-tab-iframe']")
					
					# 取消已勾选的未审核条件
					click("xpath", "//input[@id='combobox-input-maintainflag']")
					sleep(1)
					click("xpath", "//div[@title='冻结']")
					sleep(1)
					click("xpath", "//div[@title='解冻']")
					sleep(1)
					
					# 点击查询
					click("xpath", "//span[text()='查询']")
					
					# 勾选未审批数据
					click("xpath", "//div[@title='申请类型:解冻']/parent::*/preceding-sibling::*[4]/descendant::*[2]")
					
					# 点击送审按钮
					click("xpath", "//span[text()='送审']")
					
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					sleep(1)
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'送审成功！')]")
					print("申请解冻，送审成功！")
					logging.info("申请解冻，送审成功！")
					time.sleep(3)
					
					# 切入‘账户申请’的iframe窗体
					switch_to("xpath", "//iframe[@id='bankAccountApply-tab-iframe']")
					
					# 双击勾选数据
					double_click("xpath", "//div[@title='审批状态:审批中']/parent::*/preceding-sibling::*[2]/descendant::*[2]")
					sleep(1)
					
					switch_to("xpath", "//iframe[@id='wf_taskProcessing_win-iframe']")
					sleep(3)
					
					click("xpath", "//span[text()='同意']")
					sleep(1)
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("申请解冻，审批同意成功！")
					logging.info("申请解冻，审批同意成功！")
					time.sleep(3)
					
					# 申请销户
					# 切入账户申请的iframe窗体
					switch_to("xpath", "//iframe[@id='bankAccountApply-tab-iframe']")
					
					# 用JS方便点击‘申请’按钮旁边的倒三角形
					js_click("xpath", "//span[text()='申请']/parent::*/following-sibling::*/child::*")
					sleep(1)
					
					# 点击申请开户按钮
					js_click("xpath", "//a[contains(text(),'申请销户')]")
					sleep(1)
					
					switch_to("xpath", "//iframe[@id='xiaohuWin-iframe']")
					
					# 选择银行
					click("xpath", "//input[@id='combobox-input-bankid']")
					# 输入银行名称，模糊查询
					input("xpath", "//input[@id='combobox-input-bankid']", "农业银行")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-bankid']")
					input_enter("xpath", "//input[@id='combobox-input-bankid']")
					time.sleep(1)
					
					# 选择银行账户
					click("xpath", "//input[@id='combobox-input-accountid']")
					# 输入银行名称，模糊查询
					input("xpath", "//input[@id='combobox-input-accountid']", "USD")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-accountid']")
					input_enter("xpath", "//input[@id='combobox-input-accountid']")
					time.sleep(1)
					
					# 描述框中填入值
					input("xpath", "//textarea[@id='applyreason']", "自动化测试账户申请销户申请原因框")
					sleep(1)
					
					# 点击确定按钮
					click("xpath", "//span[text()='保存']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("账户申请，申请销户成功！")
					logging.info("账户申请，申请销户成功！")
					sleep(3)
			
			# # 切入‘账户申请’的iframe窗体
			# switch_to("xpath", "//iframe[@id='bankAccountApply-tab-iframe']")
			#
			# # 取消已勾选的未审核条件
			# click("xpath", "//input[@id='combobox-input-maintainflag']")
			# sleep(1)
			# click("xpath", "//div[@title='销户']")
			# sleep(1)
			#
			# # 点击查询
			# click("xpath", "//span[text()='查询']")
			#
			# # 勾选未审批数据
			# click("xpath", "//div[@title='申请类型:销户']/parent::*/preceding-sibling::*[4]/descendant::*[2]")
			#
			# # 点击送审按钮
			# click("xpath", "//span[text()='送审']")
			#
			# # 点击弹出框的OK键
			# click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
			# sleep(1)
			#
			# # 退出所有iframe窗体
			# switch_default()
			#
			# # 用隐式等待方法等页面出现审核的提示框
			# implici_wait("xpath", "//span[contains(text(),'送审成功！')]")
			# print("申请销户，送审成功！")
			# logging.info("申请销户，送审成功！")
			# time.sleep(3)
			#
			# # 切入‘账户申请’的iframe窗体
			# switch_to("xpath", "//iframe[@id='bankAccountApply-tab-iframe']")
			#
			# # 双击勾选数据
			# double_click("xpath", "//div[@title='审批状态:审批中']/parent::*/preceding-sibling::*[2]/descendant::*[2]")
			# sleep(1)
			#
			# switch_to("xpath", "//iframe[@id='wf_taskProcessing_win-iframe']")
			# sleep(3)
			#
			# click("xpath", "//span[text()='同意']")
			# sleep(1)
			#
			# # 退出所有iframe窗体
			# switch_default()
			#
			# # 用隐式等待方法等页面出现审核的提示框
			# implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			# print("申请销户，第一次审批同意成功！")
			# logging.info("申请销户，第一次审批同意成功！")
			# time.sleep(3)
			#
			# # 切入‘账户申请’的iframe窗体
			# switch_to("xpath", "//iframe[@id='bankAccountApply-tab-iframe']")
			#
			# # 双击勾选数据
			# double_click("xpath", "//div[@title='审批状态:审批中']/parent::*/preceding-sibling::*[2]/descendant::*[2]")
			# sleep(1)
			#
			# switch_to("xpath", "//iframe[@id='wf_taskProcessing_win-iframe']")
			# sleep(2)
			#
			# click("xpath", "//span[text()='终审']")
			# sleep(1)
			#
			# # 退出所有iframe窗体
			# switch_default()
			#
			# # 用隐式等待方法等页面出现审核的提示框
			# implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			# print("申请销户，第二次审批同意成功！")
			# logging.info("申请销户，第二次审批同意成功！")
			# time.sleep(3)
			
			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='账户申请']/child::*[1]")
			
			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//span[text()='账户生命周期']")
			# 打印操作成功日志
			print("账户申请，操作成功!")
			logging.info("账户申请，操作成功!")
			time.sleep(2)
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("账户申请失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		
		# 开始测试账户资金监控--账户生命周期--账户维护-多币种账户
		# 测试账户生命周期--账户维护-多币种账户
		try:
			# 点击账户生命周期'菜单
			click("xpath", "//span[text()='账户生命周期']")
			# 点击账户维护-多币种账户菜单
			click("xpath", "//span[text()='账户维护']")
			# 退出所有iframe窗体
			switch_default()
			
			for i in range(1, 3):
				# 切入账户维护的iframe窗体
				switch_to("xpath", "//iframe[@id='bankAccounts-tab-iframe']")
				logging.info("开始测试账户维护功能")
				sleep(1)
				
				# 切入多币种账户
				click("xpath", "//span[text()='多币种账户']")
				sleep(1)
				
				switch_to("xpath", "//iframe[@id='subTabTwo-iframe']")
				# 点击新增
				click("xpath", "//span[text()='新增']")
				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='addWin-iframe']")
				sleep(1)
				
				if i == 1:
					# 选择银行
					click("xpath", "//input[@id='combobox-input-bankid']")
					# 模糊匹配报错，因此选择直接点击
					input("xpath", "//input[@id='combobox-input-bankid']", "中国银行")
					sleep(1)
					click("xpath", "//div[@title='代码-名称:BOC-中国银行']")
					sleep(1)
					
					# 选择开户行
					click("xpath", "//input[@id='combobox-input-banklocationid']")
					input("xpath", "//input[@id='combobox-input-banklocationid']", "大连泡崖街支行")
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
					
					# # 选择银企直联户/现金虚拟户/票据虚拟户 第一次选择银企直联户
					click("xpath", "//input[@id='isbankdirect']")
					
					# 选择境内外
					click("xpath", "//input[@id='combobox-input-inorout']")
					# 输入开户行大连泡崖街支行名称，模糊查询
					input("xpath", "//input[@id='combobox-input-inorout']", "境内")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-inorout']")
					input_enter("xpath", "//input[@id='combobox-input-inorout']")
				
				if i == 2:
					# 选择银行
					click("xpath", "//input[@id='combobox-input-bankid']")
					# 模糊匹配报错，因此选择直接点击
					input("xpath", "//input[@id='combobox-input-bankid']", "农业银行")
					sleep(1)
					click("xpath", "//div[@title='代码-名称:ABC-农业银行']")
					sleep(1)
					
					# 选择开户行
					click_up_click("//input[@id='combobox-input-banklocationid']")
					
					# 选择币种
					click("xpath", "//input[@id='combobox-input-currencyid']")
					# 输入开户行大连泡崖街支行名称，模糊查询
					input("xpath", "//input[@id='combobox-input-currencyid']", "USD")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-currencyid']")
					input_enter("xpath", "//input[@id='combobox-input-currencyid']")
					time.sleep(1)
					
					# 选择账户性质
					click("xpath", "//input[@id='combobox-input-accounttypeid']")
					# 输入开户行大连泡崖街支行名称，模糊查询
					input("xpath", "//input[@id='combobox-input-accounttypeid']", "一般户")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-accounttypeid']")
					input_enter("xpath", "//input[@id='combobox-input-accounttypeid']")
					time.sleep(1)
					
					# 选择境内外
					click("xpath", "//input[@id='combobox-input-inorout']")
					# 输入开户行大连泡崖街支行名称，模糊查询
					input("xpath", "//input[@id='combobox-input-inorout']", "境外")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-inorout']")
					input_enter("xpath", "//input[@id='combobox-input-inorout']")
				
				# 设置时间的变成存储，变成
				temp1 = time.strftime("%H%M%S")
				# 输入银行账号
				click("xpath", "//input[@id='accountnumber']")
				sleep(1)
				input("xpath", "//input[@id='accountnumber']", "2020" + str(temp1))
				sleep(1)
				
				# 选择账户名称
				click("xpath", "//a[@id='importaccountname']")
				sleep(1)
				
				# 选择账户存款类型
				click("xpath", "//input[@id='combobox-input-deposittype']")
				# 输入开户行大连泡崖街支行名称，模糊查询
				input("xpath", "//input[@id='combobox-input-deposittype']", "活期")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-deposittype']")
				input_enter("xpath", "//input[@id='combobox-input-deposittype']")
				time.sleep(1)
				
				# 填写地址
				input("xpath", "//input[@id='accountaddress']", "甘肃定西")
				sleep(1)
				
				# 选择常驻国家性质
				click("xpath", "//input[@id='combobox-input-countrytype']")
				# 输入一般贸易区，模糊查询
				input("xpath", "//input[@id='combobox-input-countrytype']", "一般贸易区")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-countrytype']")
				input_enter("xpath", "//input[@id='combobox-input-countrytype']")
				time.sleep(1)
				
				# 选择账户分类
				click("xpath", "//input[@id='combobox-input-accountclassid']")
				# 输入开户行大连泡崖街支行名称，模糊查询
				input("xpath", "//input[@id='combobox-input-accountclassid']", "自动化测试账户分类")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-accountclassid']")
				input_enter("xpath", "//input[@id='combobox-input-accountclassid']")
				time.sleep(1)
				
				# 是否集团代管
				click("xpath", "//input[@id='istakeover']")
				sleep(1)
				
				# 选择收付属性
				click("xpath", "//input[@id='combobox-input-paymentattribute']")
				# 输入开户行大连泡崖街支行名称，模糊查询
				input("xpath", "//input[@id='combobox-input-paymentattribute']", "收入账户")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-paymentattribute']")
				input_enter("xpath", "//input[@id='combobox-input-paymentattribute']")
				
				# 点击保存按钮
				click("xpath", "//span[text()='保存']")
				
				# 退出所有iframe窗体
				switch_default()
				
				# 用隐式等待方法等页面出现提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				print("账户维护-多币种账户新增第%s次，保存成功！" % i)
				logging.info("账户维护-多币种账户新增第%s次，保存成功！" % i)
				time.sleep(3)
				
				# 第一笔，就先修改，再修改页面提交送审，再撤销送审，再删除
				if i == 1:
					# 切入‘账户申请’的iframe窗体
					switch_to("xpath", "//iframe[@id='bankAccounts-tab-iframe']")
					sleep(1)
					switch_to("xpath", "//iframe[@id='subTabTwo-iframe']")
					sleep(1)
					
					# 点击查看
					# 用JS的方法点击放大镜
					click("xpath", "//span[@class='f-contrac-close']")
					sleep(2)
					
					# 输入银行：中国银行
					click("xpath", "//input[@id='combobox-input-bankid']")
					sleep(1)
					input("xpath", "//input[@id='combobox-input-bankid']", "中国银行")
					sleep(1)
					click("xpath", "//div[@title='代码-名称:BOC-中国银行']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
					sleep(1)
					
					# 点击查询
					click("xpath", "//span[text()='查询']")
					sleep(2)
					
					# 修改勾选数据
					click("xpath", "//span[text()='新建']//ancestor::*[8]/descendant::*[1]/descendant::*[19]")
					
					# 点击审核按钮
					click("xpath", "//span[text()='审核']")
					
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					sleep(1)
					
					# 退出所有iframe窗体
					switch_default()
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'账户成功审核1条！')]")
					print("账户维护-多币种账户第%s次，审核成功！" % i)
					logging.info("账户维护-多币种账户第%s次，审核成功！" % i)
					time.sleep(3)
					
					switch_to("xpath", "//iframe[@id='bankAccounts-tab-iframe']")
					sleep(1)
					switch_to("xpath", "//iframe[@id='subTabTwo-iframe']")
					sleep(2)
					# 修改勾选数据
					click("xpath", "//span[text()='新建']//ancestor::*[8]/descendant::*[1]/descendant::*[19]")
					
					# 用JS方便点击‘申请’按钮旁边的倒三角形
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
					implici_wait("xpath", "//span[contains(text(),'账户成功取消审核1条！')]")
					print("账户维护-多币种账户，账户成功取消审核1条")
					logging.info("账户维护-多币种账户，账户成功取消审核1条")
					time.sleep(3)
					
					switch_to("xpath", "//iframe[@id='bankAccounts-tab-iframe']")
					sleep(1)
					switch_to("xpath", "//iframe[@id='subTabTwo-iframe']")
					sleep(1)
					
					# 修改勾选数据
					click("xpath", "//span[text()='新建']//ancestor::*[8]/descendant::*[1]/descendant::*[19]")
					
					# 点击修改按钮
					click("xpath", "//span[text()='修改']")
					
					# 切入修改的iframe窗体
					switch_to("xpath", "//iframe[@id='modWin-iframe']")
					sleep(2)
					
					# 点击保存按钮
					click("xpath", "//span[text()='保存']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("账户维护-多币种账户，修改成功！")
					logging.info("账户维护-多币种账户，修改成功！")
					time.sleep(3)
					
					# 切入‘账户维护-多币种账户’的iframe窗体
					switch_to("xpath", "//iframe[@id='bankAccounts-tab-iframe']")
					sleep(1)
					switch_to("xpath", "//iframe[@id='subTabTwo-iframe']")
					sleep(1)
					
					# 勾选数据
					click("xpath", "//span[text()='新建']//ancestor::*[8]/descendant::*[1]/descendant::*[19]")
					
					# 点击删除按钮
					click("xpath", "//span[text()='删除']")
					
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现删除的提示框
					implici_wait("xpath", "//span[contains(text(),'删除成功！')]")
					print("账户维护-多币种账户，删除成功！")
					logging.info("账户维护-多币种账户，删除成功！")
					time.sleep(3)
				
				# 第二笔，测试送审的流程，送审，双击页面同意，退回，送审，同意
				if i == 2:
					# 切入‘账户维护’的iframe窗体
					switch_to("xpath", "//iframe[@id='bankAccounts-tab-iframe']")
					sleep(1)
					switch_to("xpath", "//iframe[@id='subTabTwo-iframe']")
					sleep(1)
					
					# 输入银行：农业银行
					click("xpath", "//input[@id='combobox-input-bankid']")
					sleep(1)
					click("xpath", "//div[@title='代码-名称:BOC-中国银行']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
					sleep(1)
					clear("xpath", "//input[@id='combobox-input-bankid']")
					sleep(1)
					input("xpath", "//input[@id='combobox-input-bankid']", "农业银行")
					sleep(1)
					click("xpath", "//div[@title='代码-名称:ABC-农业银行']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
					sleep(1)
					
					# 点击查询
					click("xpath", "//span[text()='查询']")
					sleep(1)
					# 修改勾选数据
					click("xpath", "//span[text()='新建']/ancestor::*[8]/descendant::*[1]/descendant::*[19]")
					
					# 点击送审按钮
					click("xpath", "//span[text()='审核']")
					
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					sleep(1)
					
					# 退出所有iframe窗体
					switch_default()
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'账户成功审核1条！')]")
					print("账户维护-多币种账户第%s次，审核成功！" % i)
					logging.info("账户维护-多币种账户第%s次，审核成功！" % i)
					time.sleep(3)
					
					# 切入‘账户维护’的iframe窗体
					switch_to("xpath", "//iframe[@id='bankAccounts-tab-iframe']")
					sleep(1)
					switch_to("xpath", "//iframe[@id='subTabTwo-iframe']")
					sleep(1)
					
					# 修改勾选数据
					click("xpath", "//span[text()='新建']//ancestor::*[8]/descendant::*[1]/descendant::*[19]")
					
					# 用JS方便点击‘申请’按钮旁边的倒三角形
					js_click("xpath", "//span[text()='维护']/parent::*/following-sibling::*/child::*")
					sleep(1)
					
					js_click("xpath", "//a[contains(text(),'开户')]")
					sleep(1)
					
					switch_to("xpath", "//iframe[@id='openAccountWin-iframe']")
					sleep(1)
					
					# 选择开户日期
					today = date.today()
					open_date = today - timedelta(days=20)
					click("xpath", "//input[@id='openeddate-input']")
					sleep(1)
					clear("xpath", "//input[@id='openeddate-input']")
					sleep(1)
					input("xpath", "//input[@id='openeddate-input']", str(open_date))
					time.sleep(1)
					
					# 选择日期
					today = date.today()
					accountdue_date = today + timedelta(days=20)
					click("xpath", "//input[@id='accountdatedue-input']")
					sleep(1)
					clear("xpath", "//input[@id='accountdatedue-input']")
					sleep(1)
					input("xpath", "//input[@id='accountdatedue-input']", str(accountdue_date))
					time.sleep(1)
					
					# 日记账余额
					click("xpath", "//input[@id='journalbalance1-input']")
					sleep(1)
					clear("xpath", "//input[@id='journalbalance1-input']")
					sleep(1)
					input("xpath", "//input[@id='journalbalance1-input']", "30000")
					sleep(1)
					
					# 初始余额
					click("xpath", "//input[@id='initbalance1-input']")
					sleep(1)
					clear("xpath", "//input[@id='initbalance1-input']")
					sleep(1)
					input("xpath", "//input[@id='initbalance1-input']", "30000")
					sleep(1)
					
					click("xpath", "//span[text()='确定']")
					sleep(1)
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("账户维护-多币种账户第%s次，开户成功！" % i)
					logging.info("账户维护-多币种账户第%s次，开户成功！" % i)
					time.sleep(3)
					
					# 切入‘账户维护’的iframe窗体
					switch_to("xpath", "//iframe[@id='bankAccounts-tab-iframe']")
					sleep(1)
					switch_to("xpath", "//iframe[@id='subTabTwo-iframe']")
					sleep(1)
					
					# 修改勾选数据
					click("xpath", "//span[text()='开户']//ancestor::*[8]/descendant::*[1]/descendant::*[19]")
					
					# 用JS方便点击‘申请’按钮旁边的倒三角形
					js_click("xpath", "//span[text()='维护']/parent::*/following-sibling::*/child::*")
					sleep(1)
					
					js_click("xpath", "//a[contains(text(),'变更')]")
					sleep(1)
					
					switch_to("xpath", "//iframe[@id='updateAccountWin-iframe']")
					sleep(2)
					
					# # 选择会计科目
					# click("xpath", "//input[@id='combobox-input-extend1']")
					# input_down("xpath", "//input[@id='combobox-input-extend1']")
					# input_enter("xpath", "//input[@id='combobox-input-extend1']")
					# time.sleep(1)
					
					# # 缺少附件上传
					
					# 点击确定按钮
					click("xpath", "//span[text()='保存']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("账户维护-多币种账户，变更成功！")
					logging.info("账户维护-多币种账户，变更成功！")
					sleep(3)
					
					# 切入‘账户维护’的iframe窗体
					switch_to("xpath", "//iframe[@id='bankAccounts-tab-iframe']")
					sleep(1)
					switch_to("xpath", "//iframe[@id='subTabTwo-iframe']")
					sleep(1)
					
					# 修改勾选数据
					click("xpath", "//span[text()='开户']//ancestor::*[8]/descendant::*[1]/descendant::*[19]")
					
					# 用JS方便点击‘申请’按钮旁边的倒三角形
					js_click("xpath", "//span[text()='维护']/parent::*/following-sibling::*/child::*")
					sleep(1)
					
					# 点击申请开户按钮
					js_click("xpath", "//a[contains(text(),'冻结')]")
					sleep(1)
					
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					sleep(1)
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("账户维护-多币种账户，冻结成功！")
					logging.info("账户维护-多币种账户，冻结成功！")
					sleep(3)
					
					# 切入‘账户维护’的iframe窗体
					switch_to("xpath", "//iframe[@id='bankAccounts-tab-iframe']")
					sleep(1)
					switch_to("xpath", "//iframe[@id='subTabTwo-iframe']")
					sleep(1)
					
					# 修改勾选数据
					click("xpath", "//span[text()='冻结']//ancestor::*[8]/descendant::*[1]/descendant::*[19]")
					
					# 用JS方便点击‘申请’按钮旁边的倒三角形
					js_click("xpath", "//span[text()='维护']/parent::*/following-sibling::*/child::*")
					sleep(1)
					
					# 点击申请开户按钮
					js_click("xpath", "//a[contains(text(),'解冻')]")
					sleep(1)
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("账户维护-多币种账户，解冻成功！")
					logging.info("账户维护-多币种账户，解冻成功！")
					sleep(3)
					
					# 切入‘账户维护’的iframe窗体
					switch_to("xpath", "//iframe[@id='bankAccounts-tab-iframe']")
					sleep(1)
					switch_to("xpath", "//iframe[@id='subTabTwo-iframe']")
					sleep(1)
					
					# 修改勾选数据
					click("xpath", "//span[text()='开户']//ancestor::*[8]/descendant::*[1]/descendant::*[19]")
					
					# 用JS方便点击‘申请’按钮旁边的倒三角形
					js_click("xpath", "//span[text()='维护']/parent::*/following-sibling::*/child::*")
					sleep(1)
					
					# 点击申请开户按钮
					js_click("xpath", "//a[contains(text(),'编辑账户事件')]")
					sleep(1)
					
					# 所属组织转移accountOrgChangeWin-iframe
					
					switch_to("xpath", "//iframe[@id='accountMaintaineventWin-iframe']")
					sleep(1)
					
					# 填写账户事件
					# 点击账户事件，新增第一行
					click("xpath", "//span[text()='新增行']")
					sleep(1)
					# 输入授信方式
					input("xpath", "//input[@id='editgrid-description-4']", "其他")
					sleep(1)
					input_down("xpath", "//input[@id='editgrid-description-4']")
					input_enter("xpath", "//input[@id='editgrid-description-4']")
					time.sleep(1)
					
					click("xpath", "//span[text()='保存']")
					sleep(1)
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("账户维护-多币种账户，编辑账户事件成功！")
					logging.info("账户维护-多币种账户，编辑账户事件成功！")
					sleep(3)
			
			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='账户维护']/child::*[1]")
			
			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//span[text()='账户生命周期']")
			# 打印操作成功日志
			print("账户维护-多币种账户，操作成功!")
			logging.info("账户维护-多币种账户，操作成功!")
			time.sleep(2)
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("账户维护-多币种账户失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		
		# 开始测试银行账户结构
		try:
			# 点击账户生命周期'菜单
			click("xpath", "//span[text()='账户生命周期']")
			# 点击账户申请菜单
			click("xpath", "//span[text()='银行账户结构']")
			# 退出所有iframe窗体
			switch_default()
			
			# 切入银行账户结构的iframe窗体
			switch_to("xpath", "//iframe[@id='bankAccountStructures-tab-iframe']")
			logging.info("开始测试银行账户结构功能")
			sleep(1)
			
			# 点击添加账户结构树
			click("xpath", "//span[text()='添加账户结构树']")
			# 切入添加账户结构树的iframe窗体
			switch_to("xpath", "//iframe[@id='addstructureaccountWin-iframe']")
			sleep(1)
			
			# 选择结构账户类型
			click("xpath", "//input[@id='combobox-input-accountstructuretype']")
			# 输入企业账户结构，模糊查询
			input("xpath", "//input[@id='combobox-input-accountstructuretype']", "企业账户结构")
			sleep(1)
			input_down("xpath", "//input[@id='combobox-input-accountstructuretype']")
			input_enter("xpath", "//input[@id='combobox-input-accountstructuretype']")
			time.sleep(1)
			
			# 填写名称
			# 设置时间的变成存储，变成
			temp1 = time.strftime("%H%M%S")
			# 输入名称
			input("xpath", "//input[@id='tname']", "ZDHMC" + str(temp1))
			sleep(1)
			
			# 填写描述
			input("xpath", "//textarea[@id='description']", "自动化测试添加账户树描述框")
			sleep(1)
			
			# 点击保存按钮
			click("xpath", "//span[text()='保存']")
			
			# 退出所有iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("银行账户结构添加账户结构树，保存成功！")
			logging.info("银行账户结构添加账户结构树，保存成功！")
			time.sleep(3)
			
			# 切入‘银行账户结构’的iframe窗体
			switch_to("xpath", "//iframe[@id='bankAccountStructures-tab-iframe']")
			sleep(1)
			# 点击查看
			# 用JS的方法点击放大镜
			click("xpath", "//span[@class='f-contrac-close']")
			sleep(1)
			
			# 输入结构账户树
			click("xpath", "//input[@id='combobox-input-urid']")
			sleep(1)
			click("xpath", "//div[contains(text(),'ZDHMC')]")
			sleep(1)
			
			# 点击查询
			click("xpath", "//span[text()='查询']")
			sleep(1)
			
			# 修改勾选数据
			click("xpath", "//span[contains(text(),'ZDHMC')]/ancestor::*[8]/descendant::*[20]")
			
			# 点击修改按钮
			click("xpath", "//span[text()='修改']")
			
			switch_to("xpath", "//iframe[@id='modWin-iframe']")
			sleep(1)
			
			# 填写描述
			input("xpath", "//textarea[@id='description']", "自动化测试添加账户树描述框修改描述类型")
			sleep(1)
			
			# 点击保存按钮
			click("xpath", "//span[text()='保存']")
			
			# 退出所有iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("银行结构账户，修改成功！")
			logging.info("银行结构账户，修改成功！")
			time.sleep(3)
			
			# 切入‘'银行账户结构’的iframe窗体
			switch_to("xpath", "//iframe[@id='bankAccountStructures-tab-iframe']")
			sleep(1)
			
			# # 用JS方便点击‘查询’按钮旁边的倒三角形
			# js_click("xpath", "//span[text()='查询']/parent::*/following-sibling::*/child::*")
			# sleep(1)
			
			# 修改勾选数据
			click("xpath", "//span[contains(text(),'ZDHMC')]/ancestor::*[8]/descendant::*[20]")
			
			# 点击送审按钮
			click("xpath", "//span[text()='添加下级账户']")
			
			switch_to("xpath", "//iframe[@id='addlowaccountWin-iframe']")
			sleep(1)
			
			# 选择账户
			click("xpath", "//input[@id='combobox-input-accountOrganid']")
			# 输入币种，模糊查询
			input("xpath", "//input[@id='combobox-input-accountOrganid']", "亚唐科技")
			sleep(1)
			input_down("xpath", "//input[@id='combobox-input-accountOrganid']")
			input_enter("xpath", "//input[@id='combobox-input-accountOrganid']")
			time.sleep(1)
			
			# 选择账户
			click("xpath", "//input[@id='combobox-input-accountid']")
			sleep(1)
			# 输入币种，模糊查询
			input("xpath", "//input[@id='combobox-input-accountid']", "JPY")
			time.sleep(1)
			input_down("xpath", "//input[@id='combobox-input-accountid']")
			input_enter("xpath", "//input[@id='combobox-input-accountid']")
			time.sleep(1)
			# click("xpath", "//div[contains(text(),'JPY-临时户')]")
			# sleep(1)
			
			# 填写描述
			input("xpath", "//textarea[@id='description']", "ZDHXJ001")
			sleep(1)
			
			click("xpath", "//span[text()='保存']")
			sleep(1)
			
			# 退出所有iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("银行账户结构添加下级账户成功！")
			logging.info("银行账户结构添加下级账户成功！")
			time.sleep(3)
			
			switch_to("xpath", "//iframe[@id='bankAccountStructures-tab-iframe']")
			sleep(1)
			
			# 修改勾选数据
			click("xpath", "//span[contains(text(),'亚唐科技')]/ancestor::*[8]/descendant::*[1]/descendant::*[27]")
			
			# 点击添加同级账户
			click("xpath", "//span[text()='添加同级账户']")
			
			switch_to("xpath", "//iframe[@id='addsameaccountWin-iframe']")
			sleep(1)
			
			# 选择账户组织
			click("xpath", "//input[@id='combobox-input-accountOrganid']")
			# 输入币种，模糊查询
			input("xpath", "//input[@id='combobox-input-accountOrganid']", "002001-Mindy科技有限公司")
			sleep(1)
			input_down("xpath", "//input[@id='combobox-input-accountOrganid']")
			input_enter("xpath", "//input[@id='combobox-input-accountOrganid']")
			time.sleep(1)
			
			# 选择账户
			click("xpath", "//input[@id='combobox-input-accountid']")
			sleep(1)
			# 输入币种，模糊查询
			input("xpath", "//input[@id='combobox-input-accountid']", "USD")
			sleep(1)
			input_down("xpath", "//input[@id='combobox-input-accountid']")
			input_enter("xpath", "//input[@id='combobox-input-accountid']")
			time.sleep(1)
			
			click("xpath", "//span[text()='保存']")
			sleep(1)
			
			# 退出所有iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("银行账户结构添加同级级账户成功！")
			logging.info("银行账户结构添加同级级账户成功！")
			time.sleep(3)
			
			switch_default()
			
			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='银行账户结构']/child::*[1]")
			
			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//span[text()='账户生命周期']")
			# 打印操作成功日志
			print("银行账户结构，操作成功!")
			logging.info("银行账户结构，操作成功!")
			time.sleep(2)
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("银行账户结构失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		
		# 测试银行账户查看
		try:
			# 点击账户生命周期'菜单
			click("xpath", "//span[text()='账户生命周期']")
			# 点击银行账户查看菜单
			click("xpath", "//span[text()='银行账户查看']")
			# 退出所有iframe窗体
			switch_default()
			
			logging.info("开始测试当前以及下级组织银行账户查看功能")
			# 切入‘银行账户查看’的iframe窗体
			switch_to("xpath", "//iframe[@id='bankAccountsView-tab-iframe']")
			sleep(1)
			switch_to("xpath", "//iframe[@id='subTabOne-iframe']")
			sleep(1)
			
			# 点击查看
			# 用JS的方法点击放大镜
			js_click("xpath", "//span[@class='f-contrac-close']")
			sleep(1)
			
			click("xpath", "//input[@id='combobox-input-bankid']")
			# 输入内容
			input("xpath", "//input[@id='combobox-input-bankid']", "华夏银行")
			sleep(1)
			click("xpath", "//div[@title='代码-名称:HXB-华夏银行']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
			sleep(1)
			
			# 点击查询
			click("xpath", "//span[text()='查询']")
			
			# 用隐式等待方法等页面出现预期数据：币种:NOK-挪威克朗
			implici_wait("xpath", "//div[@title='币种:NOK-挪威克朗']")
			print("银行账户查看，银行账户查看成功！")
			time.sleep(3)
			
			# 退出所有iframe窗体
			switch_default()
			
			logging.info("现在开始测试所有可操作组织银行账户查看功能")
			# 切入‘应收票据查看’的iframe窗体
			switch_to("xpath", "//iframe[@id='bankAccountsView-tab-iframe']")
			sleep(1)
			
			click("xpath", "//span[text()='所有可操作组织查询']")
			sleep(1)
			
			switch_to("xpath", "//iframe[@id='subTabTwo-iframe']")
			sleep(1)
			# 点击查看
			# 用JS的方法点击放大镜
			js_click("xpath", "//span[@class='f-contrac-close']")
			sleep(1)
			
			click("xpath", "//input[@id='combobox-input-bankid']")
			# 输入内容
			input("xpath", "//input[@id='combobox-input-bankid']", "华夏银行")
			sleep(1)
			click("xpath", "//div[@title='代码-名称:HXB-华夏银行']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
			sleep(1)
			
			# 点击查询
			click("xpath", "//span[text()='查询']")
			
			# 用隐式等待方法等页面出现预期数据：币种:NOK-挪威克朗
			implici_wait("xpath", "//div[@title='币种:NOK-挪威克朗']")
			print("银行账户查看，银行账户查看成功！")
			time.sleep(3)
			
			# 退出所有iframe窗体
			switch_default()
			
			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='银行账户查看']/child::*[1]")
			
			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//span[@title='账户生命周期']")
			
			# 打印操作成功日志
			print("银行账户查看，操作成功!")
			logging.info("银行账户查看，操作成功!")
			time.sleep(2)
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("银行账户查看,失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		
		# 测试账户申请查看
		try:
			# 点击账户生命周期'菜单
			click("xpath", "//span[text()='账户生命周期']")
			# 点击账户申请查看菜单
			click("xpath", "//span[text()='账户申请查看']")
			# 退出所有iframe窗体
			switch_default()
			logging.info("开始测试账户申请查看功能")
			
			# 切入‘账户申请查看’的iframe窗体
			switch_to("xpath", "//iframe[@id='bankAccountApplyView-tab-iframe']")
			
			# 点击查看
			# 用JS的方法点击放大镜
			js_click("xpath", "//span[@class='f-contrac-close']")
			sleep(1)
			
			click("xpath", "//input[@id='combobox-input-bankid']")
			# 输入内容
			input("xpath", "//input[@id='combobox-input-bankid']", "农业银行")
			sleep(1)
			click("xpath", "//div[@title='代码-名称:ABC-农业银行']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
			sleep(1)
			
			# 点击查询
			click("xpath", "//span[text()='查询']")
			
			# 用隐式等待方法等页面出现预期数据：描述:自动化测试描述
			implici_wait("xpath", "//div[@title='银行:ABC-农业银行']")
			print("账户申请查看成功！")
			time.sleep(3)
			
			# 退出所有iframe窗体
			switch_default()
			
			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='账户申请查看']/child::*[1]")
			
			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//span[@title='账户生命周期']")
			
			# 打印操作成功日志
			print("账户申请查看，操作成功!")
			logging.info("账户申请查看，操作成功!")
			time.sleep(2)
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("账户申请查看,失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		
		# 开始测试账户资金监控--离线账户维护
		try:
			# 点击离线账户维护'菜单
			click("xpath", "//span[text()='离线账户维护']")
			switch_default()
			logging.info("开始测试离线账户维护功能")
			
			for i in range(1, 3):
				
				if i == 1:
					# 切入‘离线账户维护’的iframe窗体
					switch_to("xpath", "//iframe[@id='bankTransNonDirect-tab-iframe']")
					sleep(1)
					
					# 切入明细维护
					switch_to("xpath", "//iframe[@id='subTab1-iframe']")
					sleep(1)
					logging.info("开始测试离线账户维护功能")
					
					# 用JS的方法点击新增按钮
					js_click("xpath", "//span[text()='新增']")
					
					# 切入新增的iframe窗体
					switch_to("xpath", "//iframe[@id='addWin-iframe']")
					sleep(1)
					
					# 选择银行
					click("xpath", "//input[@id='combobox-input-bankid']")
					sleep(1)
					input("xpath", "//input[@id='combobox-input-bankid']", "中国银行")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-bankid']")
					input_enter("xpath", "//input[@id='combobox-input-bankid']")
					sleep(1)
					
					# 选择银行账户
					click("xpath", "//input[@id='combobox-input-accountid']")
					sleep(1)
					input("xpath", "//input[@id='combobox-input-accountid']", "CNY")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-accountid']")
					input_enter("xpath", "//input[@id='combobox-input-accountid']")
					sleep(1)
					
					# 输入交易日期
					today = date.today()
					trade_date = today
					click("xpath", "//input[@id='tradedate-input']")
					sleep(1)
					input("xpath", "//input[@id='tradedate-input']", str(trade_date))
					# 模拟回车键
					keyDown('enter')
					keyUp('enter')
					time.sleep(2)
					
					# 输入交易时间
					click("xpath", "//input[@id='tradedatetime-input']")
					sleep(1)
					# 按键往下，选择
					input_down("xpath", "//input[@id='tradedatetime-input']")
					input_enter("xpath", "//input[@id='tradedatetime-input']")
					time.sleep(1)
					
					# 选择交易方向
					click("xpath", "//input[@id='combobox-input-moneyway']")
					sleep(1)
					input("xpath", "//input[@id='combobox-input-moneyway']", "支出")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-moneyway']")
					input_enter("xpath", "//input[@id='combobox-input-moneyway']")
					sleep(1)
					
					# 输入交易金额
					click("xpath", "//input[@id='amount-input']")
					sleep(1)
					clear("xpath", "//input[@id='amount-input']")
					sleep(1)
					input("xpath", "//input[@id='amount-input']", "3000")
					sleep(1)
					
					# 用途框中填入值
					input("xpath", "//input[@id='purpose']", "自动化测试明细维护用途")
					sleep(1)
					
					# 业务类型
					input("xpath", "//input[@id='bustype']", "自动化测试明细维护业务类型")
					sleep(1)
					
					# 描述框
					input("xpath", "//textarea[@id='comments']", "自动化测试明细维护描述框")
					sleep(1)
					
					# 对方银行
					input("xpath", "//input[@id='oppositebank']", "中国银行")
					sleep(1)
					
					# 对方户名
					input("xpath", "//input[@id='oppositeaccountname']", "Mindy")
					sleep(1)
					
					# 对方账号
					input("xpath", "//input[@id='oppositeaccountnumber']", "ZDHDFZH001")
					sleep(1)
					
					# 点击保存按钮
					click("xpath", "//span[text()='保存']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现新增成功的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("明细维护，保存成功！")
					time.sleep(3)
				if i == 2:
					# 切入‘离线账户维护’的iframe窗体
					switch_to("xpath", "//iframe[@id='bankTransNonDirect-tab-iframe']")
					sleep(1)
					
					# 点击冻结明细维护文本
					click("xpath", "//span[text()='冻结明细维护']")
					sleep(1)
					
					# 切入明细维护
					switch_to("xpath", "//iframe[@id='subTab4-iframe']")
					sleep(1)
					logging.info("开始测试离线账户维护-冻结明细维护功能")
					
					# 用JS的方法点击新增按钮
					js_click("xpath", "//span[text()='新增']")
					
					# 切入新增的iframe窗体
					switch_to("xpath", "//iframe[@id='addWin-iframe']")
					sleep(1)
					
					# 选择银行
					click("xpath", "//input[@id='combobox-input-bankid']")
					sleep(1)
					input("xpath", "//input[@id='combobox-input-bankid']", "中国银行")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-bankid']")
					input_enter("xpath", "//input[@id='combobox-input-bankid']")
					sleep(1)
					
					# 选择银行账户
					click("xpath", "//input[@id='combobox-input-accountid']")
					sleep(1)
					input("xpath", "//input[@id='combobox-input-accountid']", "CNY")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-accountid']")
					input_enter("xpath", "//input[@id='combobox-input-accountid']")
					sleep(1)
					
					# 输入交易日期
					today = date.today()
					trade_date = today
					click("xpath", "//input[@id='tradedate-input']")
					sleep(1)
					input("xpath", "//input[@id='tradedate-input']", str(trade_date))
					# 模拟回车键
					keyDown('enter')
					keyUp('enter')
					time.sleep(2)
					
					# 输入交易时间
					click("xpath", "//input[@id='tradedatetime-input']")
					sleep(1)
					# 按键往下，选择
					input_down("xpath", "//input[@id='tradedatetime-input']")
					input_enter("xpath", "//input[@id='tradedatetime-input']")
					time.sleep(1)
					
					# 冻结解冻类别
					click("xpath", "//input[@id='combobox-input-freezetype']")
					sleep(1)
					input("xpath", "//input[@id='combobox-input-freezetype']", "冻结")
					# 按键往下，选择
					input_down("xpath", "//input[@id='combobox-input-freezetype']")
					sleep(1)
					input_enter("xpath", "//input[@id='combobox-input-freezetype']")
					time.sleep(1)
					
					# 输入交易金额
					click("xpath", "//input[@id='amount-input']")
					sleep(1)
					clear("xpath", "//input[@id='amount-input']")
					sleep(1)
					input("xpath", "//input[@id='amount-input']", "3000")
					sleep(1)
					
					# 输入原因
					input("xpath", "//input[@id='freezereason']", "自动化测试冻结明细维护原因")
					sleep(1)
					
					# 输入业务类型
					input("xpath", "//input[@id='bustype']", "自动化测试冻结明细维护业务类型")
					sleep(1)
					
					# 用途框中填入值
					input("xpath", "//textarea[@id='description']", "自动化测试冻结账户明细备注框")
					sleep(1)
					
					# 点击保存按钮
					click("xpath", "//span[text()='保存']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现新增成功的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("冻结明细维护，保存成功！")
					time.sleep(3)
				
				if i == 1:
					# 删除功能
					# 切入‘离线账户维护’的iframe窗体
					switch_to("xpath", "//iframe[@id='bankTransNonDirect-tab-iframe']")
					sleep(1)
					
					# 切入明细维护
					switch_to("xpath", "//iframe[@id='subTab1-iframe']")
					sleep(1)
					# 点击查看
					# 用JS的方法点击放大镜
					js_click("xpath", "//span[@class='f-contrac-close']")
					sleep(1)
					
					# 选择银行
					click("xpath", "//input[@id='combobox-input-bankid']")
					# 输入银行名称，模糊查询
					input("xpath", "//input[@id='combobox-input-bankid']", "中国银行")
					sleep(1)
					click("xpath", "//div[@title='代码-名称:BOC-中国银行']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
					sleep(1)
					
					# 选择交易日期从
					today = date.today()
					tradedatestart = today - timedelta(days=2)
					click("xpath", "//input[@id='tradedatestart-input']")
					sleep(1)
					clear("xpath", "//input[@id='tradedatestart-input']")
					sleep(1)
					input("xpath", "//input[@id='tradedatestart-input']", str(tradedatestart))
					# 模拟回车键
					keyDown('enter')
					keyUp('enter')
					time.sleep(2)
					
					# 选择交易日期到
					today = date.today()
					tradedateend = today + timedelta(days=2)
					click("xpath", "//input[@id='tradedateend-input']")
					sleep(1)
					clear("xpath", "//input[@id='tradedateend-input']")
					sleep(1)
					input("xpath", "//input[@id='tradedateend-input']", str(tradedateend))
					# 模拟回车键
					keyDown('enter')
					keyUp('enter')
					time.sleep(2)
					
					# 点击查询
					click("xpath", "//span[text()='查询']")
					
					# 修改
					# 勾选
					click("xpath", "//div[@title='对方户名:Mindy']/parent::*/preceding-sibling::*[9]/descendant::*[2]")
					
					# 点击修改按钮
					click("xpath", "//span[text()='修改']")
					
					# 切入修改的iframe窗体
					switch_to("xpath", "//iframe[@id='modWin-iframe']")
					sleep(1)
					
					# 描述框
					input("xpath", "//textarea[@id='comments']", "自动化测试明细维护描述框修改备注框内容")
					sleep(1)
					
					# 点击保存按钮
					click("xpath", "//span[text()='保存']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现新增成功的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("明细维护，修改成功！")
					time.sleep(3)
					
					switch_to("xpath", "//iframe[@id='bankTransNonDirect-tab-iframe']")
					sleep(1)
					
					# 切入明细维护
					switch_to("xpath", "//iframe[@id='subTab1-iframe']")
					sleep(1)
					
					# 删除
					# 勾选
					click("xpath", "//div[@title='对方户名:Mindy']/parent::*/preceding-sibling::*[9]/descendant::*[2]")
					
					# 点击删除按钮
					click("xpath", "//span[text()='删除']")
					
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现删除的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功')]")
					print("明细维护，删除成功！")
					time.sleep(3)
					
					# 余额重新生成功能
					# 切入‘离线账户维护’的iframe窗体
					switch_to("xpath", "//iframe[@id='bankTransNonDirect-tab-iframe']")
					sleep(1)
					
					# 切入明细维护
					switch_to("xpath", "//iframe[@id='subTab1-iframe']")
					sleep(1)
					
					# 点击余额重新生成按钮reGenerateWinow-iframe
					click("xpath", "//span[text()='余额重新生成']")
					sleep(1)
					
					switch_to("xpath", "//iframe[@id='reGenerateWinow-iframe']")
					
					# 选择银行
					click("xpath", "//input[@id='combobox-input-bankid']")
					# 输入银行名称，模糊查询
					input("xpath", "//input[@id='combobox-input-bankid']", "中国银行")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-bankid']")
					input_enter("xpath", "//input[@id='combobox-input-bankid']")
					sleep(1)
					
					# 选择银行账户
					click("xpath", "//input[@id='combobox-input-accountid']")
					# 输入银行名称，模糊查询
					input("xpath", "//input[@id='combobox-input-accountid']", "CNY")
					sleep(1)
					input_enter("xpath", "//input[@id='combobox-input-accountid']")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-accountid']")
					input_enter("xpath", "//input[@id='combobox-input-accountid']")
					sleep(1)
					
					# 选择交易日期从
					today = date.today()
					tradedatestart = today + timedelta(days=2)
					click("xpath", "//input[@id='startdate-input']")
					sleep(1)
					clear("xpath", "//input[@id='startdate-input']")
					sleep(1)
					input("xpath", "//input[@id='startdate-input']", str(tradedatestart))
					# 模拟回车键
					keyDown('enter')
					keyUp('enter')
					time.sleep(2)
					
					# 点击保存按钮
					click("xpath", "//span[text()='余额重新生成']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现新增成功的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("明细维护，余额重新生成成功！")
					time.sleep(3)
					
					switch_to("xpath", "//iframe[@id='bankTransNonDirect-tab-iframe']")
					sleep(1)
					
					click("xpath", "//span[text()='余额维护']")
					
					# 切入明细维护
					switch_to("xpath", "//iframe[@id='subTab2-iframe']")
					sleep(1)
					
					# 点击查看
					# 用JS的方法点击放大镜
					js_click("xpath", "//span[@class='f-contrac-close']")
					sleep(1)
					
					click("xpath", "//input[@id='combobox-input-bankid']")
					# 输入内容
					input("xpath", "//input[@id='combobox-input-bankid']", "华夏银行")
					sleep(1)
					click("xpath", "//div[@title='代码-名称:HXB-华夏银行']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
					sleep(1)
					
					# 点击查询
					click("xpath", "//span[text()='查询']")
					
					# 用隐式等待方法等页面出现预期数据：币种:NOK-挪威克朗
					implici_wait("xpath", "//div[@title='币种:NOK-挪威克朗']")
					print("余额维护查看成功！")
					time.sleep(3)
					
					switch_default()
					
					switch_to("xpath", "//iframe[@id='bankTransNonDirect-tab-iframe']")
					sleep(1)
					
					click("xpath", "//span[text()='集中余额维护']")
					
					# 切入明细维护
					switch_to("xpath", "//iframe[@id='subTab3-iframe']")
					sleep(1)
					
					# 点击查看
					# 用JS的方法点击放大镜
					js_click("xpath", "//span[@class='f-contrac-close']")
					sleep(1)
					
					click("xpath", "//input[@id='combobox-input-bankid']")
					# 输入内容
					input("xpath", "//input[@id='combobox-input-bankid']", "华夏银行")
					sleep(1)
					click("xpath", "//div[@title='代码-名称:HXB-华夏银行']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
					sleep(1)
					
					# 点击查询
					click("xpath", "//span[text()='查询']")
					
					# 用隐式等待方法等页面出现预期数据：币种:NOK-挪威克朗
					implici_wait("xpath", "//div[@title='币种:NOK-挪威克朗']")
					print("集中余额维护查看成功！")
					time.sleep(3)
					switch_default()
				
				if i == 2:
					# 删除功能
					# 切入‘离线账户维护’的iframe窗体
					switch_to("xpath", "//iframe[@id='bankTransNonDirect-tab-iframe']")
					sleep(1)
					
					# 点击冻结明细维护文本
					click("xpath", "//span[text()='冻结明细维护']")
					sleep(1)
					
					# 切入明细维护
					switch_to("xpath", "//iframe[@id='subTab4-iframe']")
					sleep(1)
					
					# 点击查看
					# 用JS的方法点击放大镜
					js_click("xpath", "//span[@class='f-contrac-close']")
					sleep(1)
					
					# 选择银行
					click("xpath", "//input[@id='combobox-input-bankid']")
					# 输入银行名称，模糊查询
					input("xpath", "//input[@id='combobox-input-bankid']", "中国银行")
					sleep(1)
					click("xpath", "//div[@title='代码-名称:BOC-中国银行']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
					sleep(1)
					
					# 选择交易日期从
					today = date.today()
					tradedatestart = today - timedelta(days=2)
					click("xpath", "//input[@id='tradedatestart-input']")
					sleep(1)
					clear("xpath", "//input[@id='tradedatestart-input']")
					sleep(1)
					input("xpath", "//input[@id='tradedatestart-input']", str(tradedatestart))
					# 模拟回车键
					keyDown('enter')
					keyUp('enter')
					time.sleep(2)
					
					# 选择交易日期到
					today = date.today()
					tradedateend = today + timedelta(days=2)
					click("xpath", "//input[@id='tradedateend-input']")
					sleep(1)
					clear("xpath", "//input[@id='tradedateend-input']")
					sleep(1)
					input("xpath", "//input[@id='tradedateend-input']", str(tradedateend))
					# 模拟回车键
					keyDown('enter')
					keyUp('enter')
					time.sleep(2)
					
					# 点击查询
					click("xpath", "//span[text()='查询']")
					
					# 修改
					# 勾选
					click("xpath", "//div[@title='冻结解冻类别:冻结']/parent::*/preceding-sibling::*[7]/descendant::*[2]")
					
					# 点击修改按钮
					click("xpath", "//span[text()='修改']")
					
					# 切入修改的iframe窗体
					switch_to("xpath", "//iframe[@id='modWin-iframe']")
					sleep(1)
					
					# 描述框
					input("xpath", "//textarea[@id='description']", "自动化测试明细维护描述框修改备注框内容")
					sleep(1)
					
					# 点击保存按钮
					click("xpath", "//span[text()='保存']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现新增成功的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("冻结明细维护，修改成功！")
					time.sleep(3)
					
					# 余额重新生成功能
					switch_to("xpath", "//iframe[@id='bankTransNonDirect-tab-iframe']")
					sleep(1)
					
					# 点击冻结明细维护文本
					click("xpath", "//span[text()='冻结明细维护']")
					sleep(1)
					
					# 切入明细维护
					switch_to("xpath", "//iframe[@id='subTab4-iframe']")
					sleep(1)
					
					# 点击余额重新生成按钮reGenerateWinow-iframe
					click("xpath", "//span[text()='余额重新生成']")
					sleep(1)
					
					switch_to("xpath", "//iframe[@id='reGenerateWinow-iframe']")
					
					# 选择银行
					click("xpath", "//input[@id='combobox-input-bankid']")
					# 输入银行名称，模糊查询
					input("xpath", "//input[@id='combobox-input-bankid']", "中国银行")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-bankid']")
					input_enter("xpath", "//input[@id='combobox-input-bankid']")
					sleep(1)
					
					# 选择银行账户
					click("xpath", "//input[@id='combobox-input-accountid']")
					# 输入银行名称，模糊查询
					input("xpath", "//input[@id='combobox-input-accountid']", "CNY")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-accountid']")
					input_enter("xpath", "//input[@id='combobox-input-accountid']")
					sleep(1)
					
					# 选择交易日期从
					today = date.today()
					tradedatestart = today + timedelta(days=2)
					click("xpath", "//input[@id='startdate-input']")
					sleep(1)
					clear("xpath", "//input[@id='startdate-input']")
					sleep(1)
					input("xpath", "//input[@id='startdate-input']", str(tradedatestart))
					# 模拟回车键
					keyDown('enter')
					keyUp('enter')
					time.sleep(2)
					
					# 点击保存按钮
					click("xpath", "//span[text()='余额重新生成']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现新增成功的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("冻结明细维护，余额重新生成成功！")
					time.sleep(3)
					
					# 切入‘离线账户维护’的iframe窗体
					switch_to("xpath", "//iframe[@id='bankTransNonDirect-tab-iframe']")
					sleep(1)
					
					# 点击冻结明细维护文本
					click("xpath", "//span[text()='冻结明细维护']")
					sleep(1)
					
					# 切入明细维护
					switch_to("xpath", "//iframe[@id='subTab4-iframe']")
					sleep(1)
					
					# 修改
					# 勾选
					click("xpath", "//div[@title='冻结解冻类别:冻结']/parent::*/preceding-sibling::*[7]/descendant::*[2]")
					
					# 点击删除按钮
					click("xpath", "//span[text()='删除']")
					
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现删除的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功')]")
					print("冻结明细维护，删除成功！")
					time.sleep(3)
			
			switch_default()
			# 再次点击基础设置菜单，使之关闭
			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='离线账户维护']/child::*[1]")
			
			# 打印操作成功日志
			print("离线账户维护，操作成功!")
			logging.info("离线账户维护，操作成功!")
			time.sleep(2)
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("离线账户维护,失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		
		# 更改系统参数
		try:
			
			# 点击系统参数
			click("xpath", "//div[@class='sysconfigset']")
			switch_to("xpath", "//iframe[@id='systemconfig-tab-iframe']")
			sleep(1)
			click("xpath", "//span[text()='系统参数']")
			switch_to("xpath", "//iframe[@id='tabs3-gen-2-iframe']")
			
			# 用JS的方法点击放大镜
			js_click("xpath", "//span[@class='f-contrac-close']")
			sleep(1)
			click("xpath", "//input[@id='combobox-input-paramurids']")
			sleep(1)
			input("xpath", "//input[@id='combobox-input-paramurids']", "非直联账户明细和收付交易生成模式")
			sleep(1)
			click("xpath", "//div[@title='代码-名称:非直联账户明细和收付交易生成模式']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
			# 点击查询
			click("xpath", "//span[text()='查询']")
			sleep(1)
			
			click("xpath", "//span[text()='非直联账户明细和收付交易生成模式']/ancestor::*[8]/descendant::*[28]")
			
			click("xpath", "//span[text()='修改']")
			
			# 切入修改的iframe窗体
			switch_to("xpath", "//iframe[@id='modWin-iframe']")
			sleep(1)
			
			click("xpath", "//input[@id='combobox-input-value_combo']")
			sleep(1)
			clear("xpath", "//input[@id='combobox-input-value_combo']")
			sleep(1)
			input("xpath", "//input[@id='combobox-input-value_combo']", "0:分别维护明细和收付款单，二者不关联生成")
			sleep(1)
			input_down("xpath", "//input[@id='combobox-input-value_combo']")
			input_enter("xpath", "//input[@id='combobox-input-value_combo']")
			sleep(1)
			
			click("xpath", "//input[@id='combobox-input-value67']")
			sleep(1)
			clear("xpath", "//input[@id='combobox-input-value67']")
			sleep(1)
			input("xpath", "//input[@id='combobox-input-value67']", "直接录入余额信息")
			sleep(1)
			input_down("xpath", "//input[@id='combobox-input-value67']")
			input_enter("xpath", "//input[@id='combobox-input-value67']")
			sleep(1)
			
			click("xpath", "//span[text()='保存']")
			
			switch_default()
			
			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功')]")
			print("系统参数，修改成功！")
			time.sleep(3)
			
			# 再次点击基础设置菜单，使之关闭
			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='系统设置']/child::*[1]")
			
			# 打印操作成功日志
			print("修改系统参数，操作成功!")
			logging.info("修改系统参数，操作成功!")
			time.sleep(2)
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("修改系统参数,失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		# 开始测试账户资金监控--更改参数后再次离线账户维护
		try:
			
			# 点击离线账户维护'菜单
			click("xpath", "//span[text()='离线账户维护']")
			switch_default()
			logging.info("开始测试离线账户维护功能")
			
			for i in range(1, 2):
				
				# 切入‘离线账户维护’的iframe窗体
				switch_to("xpath", "//iframe[@id='bankTransNonDirect-tab-iframe']")
				sleep(1)
				
				# 切入明细维护
				switch_to("xpath", "//iframe[@id='subTab1-iframe']")
				sleep(1)
				logging.info("开始测试离线账户维护功能")
				
				# 用JS的方法点击新增按钮
				js_click("xpath", "//span[text()='新增']")
				
				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='addWin-iframe']")
				sleep(1)
				
				# 选择银行
				click("xpath", "//input[@id='combobox-input-bankid']")
				sleep(1)
				input("xpath", "//input[@id='combobox-input-bankid']", "中国银行")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-bankid']")
				input_enter("xpath", "//input[@id='combobox-input-bankid']")
				sleep(1)
				
				# 选择银行账户
				click("xpath", "//input[@id='combobox-input-accountid']")
				sleep(1)
				input("xpath", "//input[@id='combobox-input-accountid']", "CNY")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-accountid']")
				input_enter("xpath", "//input[@id='combobox-input-accountid']")
				sleep(1)
				
				# 输入交易日期
				today = date.today()
				trade_date = today
				click("xpath", "//input[@id='tradedate-input']")
				sleep(1)
				input("xpath", "//input[@id='tradedate-input']", str(trade_date))
				# 模拟回车键
				keyDown('enter')
				keyUp('enter')
				time.sleep(2)
				
				# 输入交易时间
				click("xpath", "//input[@id='tradedatetime-input']")
				sleep(1)
				# 按键往下，选择
				input_down("xpath", "//input[@id='tradedatetime-input']")
				input_enter("xpath", "//input[@id='tradedatetime-input']")
				time.sleep(1)
				
				# 选择交易方向
				click("xpath", "//input[@id='combobox-input-moneyway']")
				sleep(1)
				input("xpath", "//input[@id='combobox-input-moneyway']", "支出")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-moneyway']")
				input_enter("xpath", "//input[@id='combobox-input-moneyway']")
				sleep(1)
				
				# 输入交易金额
				click("xpath", "//input[@id='amount-input']")
				sleep(1)
				clear("xpath", "//input[@id='amount-input']")
				sleep(1)
				input("xpath", "//input[@id='amount-input']", "3000")
				sleep(1)
				
				# 用途框中填入值
				input("xpath", "//input[@id='purpose']", "自动化测试明细维护用途")
				sleep(1)
				
				# 业务类型
				input("xpath", "//input[@id='bustype']", "自动化测试明细维护业务类型")
				sleep(1)
				
				# 描述框
				input("xpath", "//textarea[@id='comments']", "自动化测试明细维护描述框")
				sleep(1)
				
				# 对方银行
				input("xpath", "//input[@id='oppositebank']", "中国银行")
				sleep(1)
				
				# 对方户名
				input("xpath", "//input[@id='oppositeaccountname']", "Mindy")
				sleep(1)
				
				# 对方账号
				input("xpath", "//input[@id='oppositeaccountnumber']", "ZDHDFZH001")
				sleep(1)
				
				# 点击保存按钮
				click("xpath", "//span[text()='保存']")
				
				# 退出所有iframe窗体
				switch_default()
				
				# 用隐式等待方法等页面出现新增成功的提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				print("明细维护，保存成功！")
				time.sleep(3)
				
				if i == 1:
					# 删除功能
					# 切入‘离线账户维护’的iframe窗体
					switch_to("xpath", "//iframe[@id='bankTransNonDirect-tab-iframe']")
					sleep(1)
					
					# 切入明细维护
					switch_to("xpath", "//iframe[@id='subTab1-iframe']")
					sleep(1)
					# 点击查看
					# 用JS的方法点击放大镜
					js_click("xpath", "//span[@class='f-contrac-close']")
					sleep(1)
					
					# 选择银行
					click("xpath", "//input[@id='combobox-input-bankid']")
					# 输入银行名称，模糊查询
					input("xpath", "//input[@id='combobox-input-bankid']", "中国银行")
					sleep(1)
					click("xpath", "//div[@title='代码-名称:BOC-中国银行']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
					sleep(1)
					
					# 选择交易日期从
					today = date.today()
					tradedatestart = today - timedelta(days=2)
					click("xpath", "//input[@id='tradedatestart-input']")
					sleep(1)
					clear("xpath", "//input[@id='tradedatestart-input']")
					sleep(1)
					input("xpath", "//input[@id='tradedatestart-input']", str(tradedatestart))
					# 模拟回车键
					time.sleep(2)
					
					# 选择交易日期到
					today = date.today()
					tradedateend = today + timedelta(days=10)
					click("xpath", "//input[@id='tradedateend-input']")
					sleep(1)
					clear("xpath", "//input[@id='tradedateend-input']")
					sleep(1)
					input("xpath", "//input[@id='tradedateend-input']", str(tradedateend))
					# 模拟回车键
					time.sleep(2)
					
					# 点击查询
					click("xpath", "//span[text()='查询']")
					
					# 修改
					# 勾选
					click("xpath", "//div[@title='对方户名:Mindy']/parent::*/preceding-sibling::*[9]/descendant::*[2]")
					
					# 点击修改按钮
					click("xpath", "//span[text()='修改']")
					
					# 切入修改的iframe窗体
					switch_to("xpath", "//iframe[@id='modWin-iframe']")
					sleep(1)
					
					# 描述框
					input("xpath", "//textarea[@id='comments']", "自动化测试明细维护描述框修改备注框内容")
					sleep(1)
					
					# 点击保存按钮
					click("xpath", "//span[text()='保存']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现新增成功的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("明细维护，修改成功！")
					time.sleep(3)
					
					switch_to("xpath", "//iframe[@id='bankTransNonDirect-tab-iframe']")
					sleep(1)
					
					# 切入明细维护
					switch_to("xpath", "//iframe[@id='subTab1-iframe']")
					sleep(1)
					
					# 修改
					# 勾选
					click("xpath", "//div[@title='对方户名:Mindy']/parent::*/preceding-sibling::*[9]/descendant::*[2]")
					#
					# 点击删除按钮
					click("xpath", "//span[text()='删除']")
					
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现删除的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功')]")
					print("明细维护，删除成功！")
					time.sleep(3)
					
					# 余额维护页面
					switch_to("xpath", "//iframe[@id='bankTransNonDirect-tab-iframe']")
					sleep(1)
					
					click("xpath", "//span[text()='余额维护']")
					
					# 切入明细维护
					switch_to("xpath", "//iframe[@id='subTab2-iframe']")
					sleep(1)
					
					# 用JS的方法点击新增按钮
					js_click("xpath", "//span[text()='新增']")
					
					# 切入新增的iframe窗体
					switch_to("xpath", "//iframe[@id='addWin-iframe']")
					sleep(1)
					
					# 选择银行
					click("xpath", "//input[@id='combobox-input-bankid']")
					sleep(1)
					input("xpath", "//input[@id='combobox-input-bankid']", "CCB-建设银行")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-bankid']")
					input_enter("xpath", "//input[@id='combobox-input-bankid']")
					sleep(1)
					
					# 选择银行账户
					click("xpath", "//input[@id='combobox-input-accountid']")
					sleep(1)
					input_enter("xpath", "//input[@id='combobox-input-accountid']")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-accountid']")
					sleep(1)
					input_enter("xpath", "//input[@id='combobox-input-accountid']")
					sleep(1)
					
					# 输入交易日期
					today = date.today()
					trade_date = today + timedelta(days=2)
					click("xpath", "//input[@id='tradedate-input']")
					sleep(1)
					input("xpath", "//input[@id='tradedate-input']", str(trade_date))
					# 模拟回车键
					keyDown('enter')
					keyUp('enter')
					time.sleep(2)
					
					# 输入当前余额
					click("xpath", "//input[@id='currentamount-input']")
					sleep(1)
					clear("xpath", "//input[@id='currentamount-input']")
					sleep(1)
					input("xpath", "//input[@id='currentamount-input']", "40000")
					sleep(1)
					
					# 描述框
					input("xpath", "//textarea[@id='comments']", "自动化测试余额维护描述框")
					sleep(1)
					
					# 点击保存按钮
					click("xpath", "//span[text()='保存']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现新增成功的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("余额维护，保存成功！")
					time.sleep(3)
					
					if i == 1:
						# 删除功能
						# 切入‘离线账户维护’的iframe窗体
						switch_to("xpath", "//iframe[@id='bankTransNonDirect-tab-iframe']")
						sleep(1)
						
						# 切入余额维护
						switch_to("xpath", "//iframe[@id='subTab2-iframe']")
						sleep(1)
						
						# 点击查看
						# 用JS的方法点击放大镜
						js_click("xpath", "//span[@class='f-contrac-close']")
						sleep(1)
						
						# 选择银行
						click("xpath", "//input[@id='combobox-input-bankid']")
						# 输入银行名称，模糊查询
						input("xpath", "//input[@id='combobox-input-bankid']", "CCB-建设银行")
						sleep(1)
						click("xpath",
						      "//div[@title='代码-名称:CCB-建设银行']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
						sleep(1)
						
						# 输入交易日期
						today = date.today()
						trade_date = today + timedelta(days=2)
						click("xpath", "//input[@id='reportdate-input']")
						sleep(1)
						clear("xpath", "//input[@id='reportdate-input']")
						sleep(1)
						input("xpath", "//input[@id='reportdate-input']", str(trade_date))
						# 模拟回车键
						
						time.sleep(2)
						
						# 点击查询
						click("xpath", "//span[text()='查询']")
						
						# 修改
						# 勾选
						click("xpath", "//div[@title='银行:CCB-建设银行']/parent::*/preceding-sibling::*[2]/descendant::*[2]")
						
						# 点击修改按钮
						click("xpath", "//span[text()='修改']")
						
						# 切入修改的iframe窗体
						switch_to("xpath", "//iframe[@id='modWin-iframe']")
						sleep(1)
						
						# 描述框
						input("xpath", "//textarea[@id='comments']", "自动化测试余额维护描述框修改备注框内容")
						sleep(1)
						
						# 点击保存按钮
						click("xpath", "//span[text()='保存']")
						
						# 退出所有iframe窗体
						switch_default()
						
						# 用隐式等待方法等页面出现新增成功的提示框
						implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
						print("余额维护，修改成功！")
						time.sleep(3)
						
						switch_to("xpath", "//iframe[@id='bankTransNonDirect-tab-iframe']")
						sleep(1)
						
						# 切入明细维护
						switch_to("xpath", "//iframe[@id='subTab2-iframe']")
						sleep(1)
						
						# 修改
						# 勾选
						click("xpath",
						      "//div[@title='余额:40,000.00']/parent::*/preceding-sibling::*[7]/descendant::*[2]")
						
						# 点击删除按钮
						click("xpath", "//span[text()='删除']")
						
						# 点击弹出框的OK键
						click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
						
						# 退出所有iframe窗体
						switch_default()
						
						# 用隐式等待方法等页面出现删除的提示框
						implici_wait("xpath", "//span[contains(text(),'操作成功')]")
						print("余额维护，删除成功！")
						time.sleep(3)
						
						# 更改系统参数后集中余额维护功能测试
						
						switch_to("xpath", "//iframe[@id='bankTransNonDirect-tab-iframe']")
						sleep(1)
						
						click("xpath", "//span[text()='集中余额维护']")
						
						# 切入明细维护
						switch_to("xpath", "//iframe[@id='subTab3-iframe']")
						sleep(1)
						# 用JS的方法点击新增按钮
						js_click("xpath", "//span[text()='新增']")
						
						# 切入新增的iframe窗体
						switch_to("xpath", "//iframe[@id='addWin-iframe']")
						sleep(1)
						
						# 选择组织
						click("xpath", "//input[@id='combobox-input-orgid']")
						sleep(1)
						input("xpath", "//input[@id='combobox-input-orgid']", "亚唐科技")
						sleep(1)
						input_down("xpath", "//input[@id='combobox-input-orgid']")
						input_enter("xpath", "//input[@id='combobox-input-orgid']")
						sleep(1)
						
						# 选择银行
						click("xpath", "//input[@id='combobox-input-bankid']")
						sleep(1)
						input("xpath", "//input[@id='combobox-input-bankid']", "BOCOM-交通银行")
						sleep(1)
						input_enter("xpath", "//input[@id='combobox-input-bankid']")
						sleep(1)
						input_down("xpath", "//input[@id='combobox-input-bankid']")
						sleep(1)
						input_enter("xpath", "//input[@id='combobox-input-bankid']")
						sleep(1)
						
						# 选择银行账户
						click("xpath", "//input[@id='combobox-input-accountid']")
						sleep(1)
						input_enter("xpath", "//input[@id='combobox-input-accountid']")
						sleep(1)
						input_down("xpath", "//input[@id='combobox-input-accountid']")
						sleep(1)
						input_enter("xpath", "//input[@id='combobox-input-accountid']")
						sleep(1)
						
						# 输入余额日期
						today = date.today()
						trade_date = today + timedelta(days=2)
						click("xpath", "//input[@id='tradedate-input']")
						sleep(1)
						input("xpath", "//input[@id='tradedate-input']", str(trade_date))
						# 模拟回车键
						keyDown('enter')
						keyUp('enter')
						time.sleep(2)
						
						# 输入当前余额
						click("xpath", "//input[@id='currentamount-input']")
						sleep(1)
						clear("xpath", "//input[@id='currentamount-input']")
						sleep(1)
						input("xpath", "//input[@id='currentamount-input']", "40000")
						sleep(1)
						
						# 描述框
						input("xpath", "//textarea[@id='comments']", "自动化测试明细维护描述框")
						sleep(1)
						
						# 点击保存按钮
						click("xpath", "//span[text()='保存']")
						
						# 退出所有iframe窗体
						switch_default()
						
						# 用隐式等待方法等页面出现新增成功的提示框
						implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
						print("集中余额维护，保存成功！")
						time.sleep(3)
						
						if i == 1:
							# 删除功能
							# 切入‘离线账户维护’的iframe窗体
							switch_to("xpath", "//iframe[@id='bankTransNonDirect-tab-iframe']")
							sleep(1)
							
							# 切入余额维护
							switch_to("xpath", "//iframe[@id='subTab3-iframe']")
							sleep(1)
							
							# 点击查看
							# 用JS的方法点击放大镜
							js_click("xpath", "//span[@class='f-contrac-close']")
							sleep(1)
							
							# 选择银行
							click("xpath", "//input[@id='combobox-input-bankid']")
							# 输入银行名称，模糊查询
							input("xpath", "//input[@id='combobox-input-bankid']", "BOCOM-交通银行")
							sleep(1)
							click("xpath",
							      "//div[@title='代码-名称:BOCOM-交通银行']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
							sleep(1)
							
							# 输入余额日期
							today = date.today()
							trade_date = today + timedelta(days=2)
							click("xpath", "//input[@id='reportdate-input']")
							sleep(1)
							clear("xpath", "//input[@id='reportdate-input']")
							sleep(1)
							input("xpath", "//input[@id='reportdate-input']", str(trade_date))
							# 模拟回车键
							
							time.sleep(2)
							
							# 点击查询
							click("xpath", "//span[text()='查询']")
							
							# 修改 # 勾选
							click("xpath",
							      "//div[@title='余额:40,000.00']/parent::*/preceding-sibling::*[7]/descendant::*[2]")
							
							# 点击修改按钮
							click("xpath", "//span[text()='修改']")
							
							# 切入修改的iframe窗体
							switch_to("xpath", "//iframe[@id='modWin-iframe']")
							sleep(1)
							
							# 描述框
							input("xpath", "//textarea[@id='comments']", "自动化测试明细维护描述框修改备注框内容")
							sleep(1)
							
							# 点击保存按钮
							click("xpath", "//span[text()='保存']")
							
							# 退出所有iframe窗体
							switch_default()
							
							# 用隐式等待方法等页面出现新增成功的提示框
							implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
							print("集中余额维护，修改成功！")
							time.sleep(3)
							
							switch_to("xpath", "//iframe[@id='bankTransNonDirect-tab-iframe']")
							sleep(1)
							
							# 切入明细维护
							switch_to("xpath", "//iframe[@id='subTab3-iframe']")
							sleep(1)
							
							# 修改
							# 勾选
							click("xpath",
							      "//div[@title='余额:40,000.00']/parent::*/preceding-sibling::*[7]/descendant::*[2]")
							
							# 点击删除按钮
							click("xpath", "//span[text()='删除']")
							
							# 点击弹出框的OK键
							click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
							
							# 退出所有iframe窗体
							switch_default()
							
							# 用隐式等待方法等页面出现删除的提示框
							implici_wait("xpath", "//span[contains(text(),'操作成功')]")
							print("集中余额维护，删除成功！")
							time.sleep(3)
							
							# 更改系统参数后的冻结明细维护功能测试
							# 切入‘离线账户维护’的iframe窗体
							switch_to("xpath", "//iframe[@id='bankTransNonDirect-tab-iframe']")
							sleep(1)
							
							# 点击冻结明细维护文本
							click("xpath", "//span[text()='冻结明细维护']")
							sleep(1)
							
							# 切入明细维护
							switch_to("xpath", "//iframe[@id='subTab4-iframe']")
							sleep(1)
							logging.info("开始测试离线账户维护-冻结明细维护功能")
							
							# 用JS的方法点击新增按钮
							js_click("xpath", "//span[text()='新增']")
							
							# 切入新增的iframe窗体
							switch_to("xpath", "//iframe[@id='addWin-iframe']")
							sleep(1)
							
							# 选择银行
							click("xpath", "//input[@id='combobox-input-bankid']")
							sleep(1)
							input("xpath", "//input[@id='combobox-input-bankid']", "中国银行")
							sleep(1)
							input_down("xpath", "//input[@id='combobox-input-bankid']")
							input_enter("xpath", "//input[@id='combobox-input-bankid']")
							sleep(1)
							
							# 选择银行账户
							click("xpath", "//input[@id='combobox-input-accountid']")
							sleep(1)
							input("xpath", "//input[@id='combobox-input-accountid']", "CNY")
							sleep(1)
							input_enter("xpath", "//input[@id='combobox-input-accountid']")
							sleep(1)
							input_down("xpath", "//input[@id='combobox-input-accountid']")
							input_enter("xpath", "//input[@id='combobox-input-accountid']")
							sleep(1)
							
							# 输入交易日期
							today = date.today()
							trade_date = today
							click("xpath", "//input[@id='tradedate-input']")
							sleep(1)
							input("xpath", "//input[@id='tradedate-input']", str(trade_date))
							# 模拟回车键
							keyDown('enter')
							keyUp('enter')
							time.sleep(2)
							
							# 输入交易时间
							click("xpath", "//input[@id='tradedatetime-input']")
							sleep(1)
							# 按键往下，选择
							input_down("xpath", "//input[@id='tradedatetime-input']")
							input_enter("xpath", "//input[@id='tradedatetime-input']")
							time.sleep(1)
							
							# 冻结解冻类别
							click("xpath", "//input[@id='combobox-input-freezetype']")
							sleep(1)
							input("xpath", "//input[@id='combobox-input-freezetype']", "冻结")
							# 按键往下，选择
							input_down("xpath", "//input[@id='combobox-input-freezetype']")
							sleep(1)
							input_enter("xpath", "//input[@id='combobox-input-freezetype']")
							time.sleep(1)
							
							# 输入交易金额
							click("xpath", "//input[@id='amount-input']")
							sleep(1)
							clear("xpath", "//input[@id='amount-input']")
							sleep(1)
							input("xpath", "//input[@id='amount-input']", "3000")
							sleep(1)
							
							# 输入原因
							input("xpath", "//input[@id='freezereason']", "自动化测试冻结明细维护原因")
							sleep(1)
							
							# 输入业务类型
							input("xpath", "//input[@id='bustype']", "自动化测试冻结明细维护业务类型")
							sleep(1)
							
							# 用途框中填入值
							input("xpath", "//textarea[@id='description']", "自动化测试冻结账户明细备注框")
							sleep(1)
							
							# 点击保存按钮
							click("xpath", "//span[text()='保存']")
							
							# 退出所有iframe窗体
							switch_default()
							
							# 用隐式等待方法等页面出现新增成功的提示框
							implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
							print("明细维护，保存成功！")
							time.sleep(3)
							
							if i == 1:
								# 删除功能
								# 切入‘离线账户维护’的iframe窗体
								switch_to("xpath", "//iframe[@id='bankTransNonDirect-tab-iframe']")
								sleep(1)
								
								# 点击冻结明细维护文本
								click("xpath", "//span[text()='冻结明细维护']")
								sleep(1)
								
								# 切入明细维护
								switch_to("xpath", "//iframe[@id='subTab4-iframe']")
								sleep(1)
								
								# 点击查看
								# 用JS的方法点击放大镜
								js_click("xpath", "//span[@class='f-contrac-close']")
								sleep(1)
								
								# 选择银行
								click("xpath", "//input[@id='combobox-input-bankid']")
								# 输入银行名称，模糊查询
								input("xpath", "//input[@id='combobox-input-bankid']", "中国银行")
								sleep(1)
								click("xpath",
								      "//div[@title='代码-名称:BOC-中国银行']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
								sleep(1)
								
								# 选择交易日期从
								today = date.today()
								tradedatestart = today - timedelta(days=2)
								click("xpath", "//input[@id='tradedatestart-input']")
								sleep(1)
								clear("xpath", "//input[@id='tradedatestart-input']")
								sleep(1)
								input("xpath", "//input[@id='tradedatestart-input']", str(tradedatestart))
								# 模拟回车键
								keyDown('enter')
								keyUp('enter')
								time.sleep(2)
								
								# 选择交易日期到
								today = date.today()
								tradedateend = today + timedelta(days=2)
								click("xpath", "//input[@id='tradedateend-input']")
								sleep(1)
								clear("xpath", "//input[@id='tradedateend-input']")
								sleep(1)
								input("xpath", "//input[@id='tradedateend-input']", str(tradedateend))
								# 模拟回车键
								keyDown('enter')
								keyUp('enter')
								time.sleep(2)
								
								# 点击查询
								click("xpath", "//span[text()='查询']")
								
								# 修改
								# 勾选
								click("xpath",
								      "//div[@title='冻结解冻类别:冻结']/parent::*/preceding-sibling::*[7]/descendant::*[2]")
								
								# 点击修改按钮
								click("xpath", "//span[text()='修改']")
								
								# 切入修改的iframe窗体
								switch_to("xpath", "//iframe[@id='modWin-iframe']")
								sleep(1)
								
								# 描述框
								input("xpath", "//textarea[@id='description']", "自动化测试明细维护描述框修改备注框内容")
								sleep(1)
								
								# 点击保存按钮
								click("xpath", "//span[text()='保存']")
								
								# 退出所有iframe窗体
								switch_default()
								
								# 用隐式等待方法等页面出现新增成功的提示框
								implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
								print("冻结明细维护，修改成功！")
								time.sleep(3)
								
								# 切入‘离线账户维护’的iframe窗体
								switch_to("xpath", "//iframe[@id='bankTransNonDirect-tab-iframe']")
								sleep(1)
								
								# 点击冻结明细维护文本
								click("xpath", "//span[text()='冻结明细维护']")
								sleep(1)
								
								# 切入明细维护
								switch_to("xpath", "//iframe[@id='subTab4-iframe']")
								sleep(1)
								
								# 修改
								# 勾选
								click("xpath",
								      "//div[@title='冻结解冻类别:冻结']/parent::*/preceding-sibling::*[7]/descendant::*[2]")
								
								# 点击删除按钮
								click("xpath", "//span[text()='删除']")
								
								# 点击弹出框的OK键
								click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
								
								# 退出所有iframe窗体
								switch_default()
								
								# 用隐式等待方法等页面出现删除的提示框
								implici_wait("xpath", "//span[contains(text(),'操作成功')]")
								print("冻结明细维护，删除成功！")
								time.sleep(3)
			switch_default()
			# 再次点击基础设置菜单，使之关闭
			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='离线账户维护']/child::*[1]")
			
			# 打印操作成功日志
			print("第二次离线账户维护，操作成功!")
			logging.info("第二次离线账户维护，操作成功!")
			time.sleep(2)
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("第二次离线账户维护,失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		
		# 在非默认租户下直联账户查询步骤
		# 1. 登录211，在DSP里配置数据,配置当前租户的ID
		# 2. 重启DSP
		# 3. 运行文件
		# 开始测试账户资金监控--直联账户查询
		
		try:
			# 点击账户生命周期'菜单
			click("xpath", "//span[text()='直联账户查询']")
			# 退出所有iframe窗体
			switch_default()
			
			for i in range(1, 2):
				# 切入直联账户查询的iframe窗体
				switch_to("xpath", "//iframe[@id='directBankAccountQuery-tab-iframe']")
				logging.info("开始测试直联账户查询-当前操作组织查询功能")
				sleep(1)
				
				switch_to("xpath", "//iframe[@id='subTabOne-iframe']")
				
				# 点击查看
				# 用JS的方法点击放大镜
				js_click("xpath", "//span[@class='f-contrac-close']")
				sleep(1)
				
				# 输入银行：中国银行
				click("xpath", "//input[@id='combobox-input-bankid']")
				sleep(1)
				input("xpath", "//input[@id='combobox-input-bankid']", "中国银行")
				sleep(1)
				click("xpath", "//div[@title='代码-名称:BOC-中国银行']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
				sleep(1)
				
				# 币种
				click("xpath", "//input[@id='combobox-input-currencyid']")
				# 输入银行名称，模糊查询
				input("xpath", "//input[@id='combobox-input-currencyid']", "CNY")
				sleep(1)
				click("xpath", "//div[@title='代码-名称:CNY-人民币']")
				sleep(1)
				
				# 点击查询
				click("xpath", "//span[text()='查询']")
				
				# 修改勾选数据
				click("xpath", "//div[@title='银行:中国银行']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
				
				# 点击余额查询按钮
				click("xpath", "//span[text()='余额查询']")
				
				# 用隐式等待方法等页面出现审核的提示框
				implici_wait("xpath", "//span[contains(text(),'余额查询-查询成功')]")
				print("余额查询成功！")
				logging.info("余额查询成功！")
				time.sleep(3)
				
				# 点击今日明细查询
				click("xpath", "//span[text()='今日明细查询']")
				
				# 用隐式等待方法等页面出现审核的提示框
				implici_wait("xpath", "//a[contains(text(),'明细查看')]")
				print("今日明细查询成功！")
				logging.info("今日明细查询成功！")
				time.sleep(3)
				
				# 点击历史明细查询
				click("xpath", "//span[text()='历史明细查询']")
				
				# 查询起始日期
				today = date.today()
				begin_date = today - timedelta(days=30)
				click("xpath", "//input[@id='begindate-input']")
				sleep(1)
				clear("xpath", "//input[@id='begindate-input']")
				sleep(1)
				input("xpath", "//input[@id='begindate-input']", str(begin_date))
				# 模拟回车键
				# keyDown('enter')
				# keyUp('enter')
				time.sleep(1)
				
				# 查询截止日期
				today = date.today()
				end_date = today - timedelta(days=1)
				click("xpath", "//input[@id='enddate-input']")
				sleep(1)
				clear("xpath", "//input[@id='enddate-input']")
				sleep(1)
				input("xpath", "//input[@id='enddate-input']", str(end_date))
				# keyDown('enter')
				# keyUp('enter')
				time.sleep(1)
				
				double_click("xpath", "//span[text()='查询起始日期']")
				sleep(1)
				
				click("xpath", "//span[text()='确定']")
				
				# 用隐式等待方法等页面出现审核的提示框
				implici_wait("xpath", "//a[contains(text(),'历史明细')]")
				print("历史明细查询成功！")
				logging.info("历史明细查询成功！")
				time.sleep(3)
				
				# 点击余额查询按钮
				click("xpath", "//span[text()='近7天历史明细查询']")
				
				# 用隐式等待方法等页面出现审核的提示框
				implici_wait("xpath", "//span[contains(text(),'历史明细查询-查询成功')]")
				print("近7天历史明细查询成功！")
				logging.info("近7天历史明细查询成功！")
				time.sleep(3)
				
				# 近7天历史余额查询
				# 点击余额查询按钮
				click("xpath", "//span[text()='近7天历史余额查询']")
				
				switch_default()
				# 用隐式等待方法等页面出现审核的提示框
				implici_wait("xpath", "//span[contains(text(),'账户查询成功！')]")
				print("近7天历史余额查询成功！")
				logging.info("近7天历史余额查询成功！")
				time.sleep(3)
				
				switch_to("xpath", "//iframe[@id='directBankAccountQuery-tab-iframe']")
				logging.info("开始测试直联账户查询-当前操作组织查询功能")
				sleep(1)
				
				switch_to("xpath", "//iframe[@id='subTabOne-iframe']")
				
				# 余额调整
				click("xpath", "//span[text()='余额调整']")
				
				# 当前余额
				click("xpath", "//input[@id='balancevalue-input']")
				sleep(1)
				clear("xpath", "//input[@id='balancevalue-input']")
				sleep(1)
				input("xpath", "//input[@id='balancevalue-input']", "30000")
				sleep(1)
				
				input("xpath", "//input[@id='adjustreason']", "自动化测试")
				sleep(1)
				
				click("xpath", "//span[text()='确定' and@class='f-new-btn-text hisensureclick_icon1']")
				sleep(1)
				
				switch_default()
				
				# 用隐式等待方法等页面出现审核的提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				print("余额调整成功")
				logging.info("余额调整成功")
				time.sleep(3)
				
				switch_to("xpath", "//iframe[@id='directBankAccountQuery-tab-iframe']")
				sleep(1)
				
				switch_to("xpath", "//iframe[@id='subTabOne-iframe']")
				
				# 用JS方便点击‘审核’按钮旁边的倒三角形
				js_click("xpath", "//span[text()='余额调整']/parent::*/following-sibling::*/child::*")
				sleep(1)
				
				# 点击取消审核按钮
				js_click("xpath", "//a[contains(text(),'调整历史查看')]")
				sleep(1)
				
				switch_to("xpath", "//iframe[@id='printWin-iframe']")
				sleep(1)
				
				# 用隐式等待方法等页面出现审核的提示框
				implici_wait("xpath", "//div[contains(text(),'mindy')]")
				print("调整历史查看成功！")
				logging.info("调整历史查看成功！")
				time.sleep(3)
				
				switch_default()
				
				switch_to("xpath", "//iframe[@id='directBankAccountQuery-tab-iframe']")
				sleep(1)
				
				switch_to("xpath", "//iframe[@id='subTabOne-iframe']")
				
				click("xpath", "//div[@id='f-win-title-printWin']/descendant::*[2]")
				
				switch_default()
				
				switch_to("xpath", "//iframe[@id='directBankAccountQuery-tab-iframe']")
				sleep(1)
				
				switch_to("xpath", "//iframe[@id='subTabOne-iframe']")
				
				# 修改勾选数据
				click("xpath", "//div[@title='银行:中国银行']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
				
				# 点击昨日明细查看
				click("xpath", "//span[text()='昨日明细查看']")
				switch_to("xpath", "//iframe[@id='detail-iframe']")
				sleep(1)
				
				click("xpath", "//span[text()='账号']/ancestor::*[3]/preceding-sibling::*[2]/descendant::*[2]")
				sleep(1)
				
				click("xpath", "//span[text()='核准']")
				sleep(1)
				
				switch_to("xpath", "//iframe[@id='matchWin-iframe']")
				sleep(1)
				
				click("xpath", "//input[@id='combobox-input-bankid']")
				sleep(1)
				input("xpath", "//input[@id='combobox-input-bankid']", "中国银行")
				sleep(1)
				input_enter("xpath", "//input[@id='combobox-input-bankid']")
				sleep(1)
				click("xpath", "//div[@title='代码-名称:BOC-中国银行']")
				sleep(1)
				
				click("xpath", "//input[@id='combobox-input-accountid']")
				sleep(1)
				click("xpath", "//span[text()='账号-币种-账户性质-银行']/ancestor::*[3]/preceding-sibling::*[1]/descendant::*[2]")
				sleep(1)
				
				double_click("xpath", "//span[text()='日期从']")
				sleep(1)
				
				# 查询起始日期
				today = date.today()
				begin_date = today - timedelta(days=30)
				click("xpath", "//input[@id='begindate-input']")
				sleep(1)
				clear("xpath", "//input[@id='begindate-input']")
				sleep(1)
				input("xpath", "//input[@id='begindate-input']", str(begin_date))
				# 模拟回车键
				# keyDown('enter')
				# keyUp('enter')
				time.sleep(1)
				
				# 查询截止日期
				today = date.today()
				end_date = today - timedelta(days=1)
				click("xpath", "//input[@id='enddate-input']")
				sleep(1)
				clear("xpath", "//input[@id='enddate-input']")
				sleep(1)
				input("xpath", "//input[@id='enddate-input']", str(end_date))
				# keyDown('enter')
				# keyUp('enter')
				time.sleep(1)
				
				# 点击核准
				click("xpath", "//span[text()='核准']")
				sleep(1)
				
				switch_default()
				# 用隐式等待方法等页面出现审核的提示框
				implici_wait("xpath", "//span[contains(text(),'核准结果')]")
				print("昨日明细核准成功！")
				logging.info("昨日明细核准成功！")
				time.sleep(3)
			
			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='直联账户查询']/child::*[1]")
			
			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//span[text()='账户生命周期']")
			# 打印操作成功日志
			print("直联账户查询成功，操作成功!")
			logging.info("直联账户查询成功，操作成功!")
			time.sleep(2)
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("直联账户查询失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		
		# 测试结构账户余额
		try:
			# 点击账户生命周期'菜单
			click("xpath", "//span[text()='账户生命周期']")
			# 点击银行账户查看菜单
			click("xpath", "//span[text()='结构账户余额']")
			# 退出所有iframe窗体
			switch_default()
			
			logging.info("开始测试结构账户余额功能")
			# 切入‘银行账户查看’的iframe窗体
			switch_to("xpath", "//iframe[@id='bankAccountStructuresBalance-tab-iframe']")
			sleep(1)
			
			# 修改
			# 勾选
			click("xpath", "//span[contains(text(),'亚唐科技')]/ancestor::*[8]/descendant::*[1]/descendant::*[35]")
			sleep(1)
			
			click("xpath", "//span[text()='直联余额查询']")
			sleep(1)
			
			switch_default()
			
			# 用隐式等待方法等页面出现预期数据：币种:NOK-挪威克朗
			implici_wait("xpath", "//span[contains(text(),'直联余额查询成功！')]")
			print("结构账户余额，结构账户余额查看成功！")
			time.sleep(3)
			
			# 退出所有iframe窗体
			switch_default()
			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='结构账户余额']/child::*[1]")
			
			# 打印操作成功日志
			print("结构账户余额，操作成功!")
			logging.info("结构账户余额，操作成功!")
			time.sleep(2)
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("结构账户余额,失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		
		# 返回删除银行账户结构的数据
		# 开始测试银行账户结构
		try:
			# 点击账户生命周期'菜单
			js_click("xpath", "//span[text()='账户生命周期']")
			# 点击账户申请菜单
			click("xpath", "//span[text()='银行账户结构']")
			# 退出所有iframe窗体
			switch_default()
			
			# 切入银行账户结构的iframe窗体
			switch_to("xpath", "//iframe[@id='bankAccountStructures-tab-iframe']")
			logging.info("开始测试删除银行账户结构功能")
			sleep(1)
			
			# 点击查看
			# 用JS的方法点击放大镜
			click("xpath", "//span[@class='f-contrac-close']")
			sleep(1)
			
			# 输入结构账户树
			click("xpath", "//input[@id='combobox-input-urid']")
			sleep(1)
			click("xpath", "//div[contains(text(),'ZDHMC')]")
			sleep(1)
			
			# 修改勾选数据
			click("xpath", "//span[contains(text(),'亚唐科技')]/ancestor::*[8]/descendant::*[1]/descendant::*[35]")
			
			# 点击修改按钮
			click("xpath", "//span[text()='删除']")
			
			# 点击弹出框的OK键
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
			
			# 退出所有iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("银行账户结构，删除成功！")
			logging.info("银行账户结构，删除成功！")
			time.sleep(3)
			
			# 切入‘银行账户结构’的iframe窗体
			switch_to("xpath", "//iframe[@id='bankAccountStructures-tab-iframe']")
			sleep(1)
			
			# 修改勾选数据
			click("xpath", "//span[contains(text(),'亚唐科技')]/ancestor::*[8]/descendant::*[1]/descendant::*[27]")
			
			# 点击修改按钮
			click("xpath", "//span[text()='删除']")
			
			# 点击弹出框的OK键
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
			
			# 退出所有iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("银行账户结构，删除成功！")
			logging.info("银行账户结构，删除成功！")
			time.sleep(3)
			
			# 切入‘银行账户结构’的iframe窗体
			switch_to("xpath", "//iframe[@id='bankAccountStructures-tab-iframe']")
			sleep(1)
			
			# 修改勾选数据
			click("xpath", "//span[contains(text(),'ZDHMC')]/ancestor::*[8]/descendant::*[20]")
			
			# 点击修改按钮
			click("xpath", "//span[text()='删除']")
			
			# 点击弹出框的OK键
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
			
			# 退出所有iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("银行账户结构，删除成功！")
			logging.info("银行账户结构，删除成功！")
			time.sleep(3)
			
			switch_default()
			
			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='银行账户结构']/child::*[1]")
			
			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//span[text()='账户生命周期']")
			# 打印操作成功日志
			print("银行账户结构，操作成功!")
			logging.info("银行账户结构，操作成功!")
			time.sleep(2)
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("银行账户结构失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		
		# 测试账户余额查看
		try:
			# 点击账户生命周期'菜单
			click("xpath", "//span[text()='账户余额查看']")
			# 退出所有iframe窗体
			switch_default()
			
			logging.info("开始测试当前以及下级组织余额查看功能")
			# 切入‘银行账户查看’的iframe窗体
			switch_to("xpath", "//iframe[@id='bankAccountBalanceView-tab-iframe']")
			sleep(1)
			switch_to("xpath", "//iframe[@id='subTab1-iframe']")
			sleep(1)
			
			# 点击查看
			# 用JS的方法点击放大镜
			js_click("xpath", "//span[@class='f-contrac-close']")
			sleep(1)
			
			click("xpath", "//input[@id='combobox-input-bankid']")
			# 输入内容
			input("xpath", "//input[@id='combobox-input-bankid']", "华夏银行")
			sleep(1)
			click("xpath", "//div[@title='代码-名称:HXB-华夏银行']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
			sleep(1)
			
			# 点击查询
			click("xpath", "//span[text()='查询']")
			
			# 用隐式等待方法等页面出现预期数据：币种:NOK-挪威克朗
			implici_wait("xpath", "//div[@title='币种:NOK-挪威克朗']")
			print("账户余额查看，账户余额查看成功！")
			time.sleep(3)
			
			# 退出所有iframe窗体
			switch_default()
			
			logging.info("现在开始测试可操作组织账户余额查看功能")
			# 切入‘应收票据查看’的iframe窗体
			switch_to("xpath", "//iframe[@id='bankAccountBalanceView-tab-iframe']")
			sleep(1)
			
			click("xpath", "//span[text()='可操作组织余额查看']")
			sleep(1)
			
			switch_to("xpath", "//iframe[@id='subTab2-iframe']")
			sleep(1)
			# 点击查看
			# 用JS的方法点击放大镜
			js_click("xpath", "//span[@class='f-contrac-close']")
			sleep(1)
			
			click("xpath", "//input[@id='combobox-input-bankid']")
			# 输入内容
			input("xpath", "//input[@id='combobox-input-bankid']", "华夏银行")
			sleep(1)
			click("xpath", "//div[@title='代码-名称:HXB-华夏银行']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
			sleep(1)
			
			# 点击查询
			click("xpath", "//span[text()='查询']")
			
			# 用隐式等待方法等页面出现预期数据：币种:NOK-挪威克朗
			implici_wait("xpath", "//div[@title='币种:NOK-挪威克朗']")
			print("可操作组织余额查看，可操作组织余额查看成功！")
			time.sleep(3)
			
			# 退出所有iframe窗体
			switch_default()
			
			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='账户余额查看']/child::*[1]")
			# 打印操作成功日志
			print("银行账户查看，操作成功!")
			logging.info("账户余额查看，操作成功!")
			time.sleep(2)
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("账户余额查看,失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		
		# 测试账户明细查看
		try:
			# 点击账户生命周期'菜单
			click("xpath", "//span[text()='账户明细查看']")
			# 退出所有iframe窗体
			switch_default()
			
			logging.info("开始测试当前以及下级组织明细查看功能")
			# 切入‘银行账户查看’的iframe窗体
			switch_to("xpath", "//iframe[@id='accountDetailView-tab-iframe']")
			sleep(1)
			switch_to("xpath", "//iframe[@id='subTab1-iframe']")
			sleep(1)
			
			# 点击查看
			# 用JS的方法点击放大镜
			js_click("xpath", "//span[@class='f-contrac-close']")
			sleep(1)
			
			click("xpath", "//input[@id='combobox-input-bankid']")
			sleep(1)
			# 输入内容oppositeaccountname
			input("xpath", "//input[@id='combobox-input-bankid']", "中国银行")
			sleep(1)
			click("xpath", "//div[@title='代码-名称:BOC-中国银行']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
			sleep(1)
			
			input("xpath", "//input[@id='oppositeaccountname']", "秦燕")
			sleep(1)
			
			clear("xpath", '//*[@id="tradedatestart-input"]')
			sleep(1)
			clear("xpath", '//*[@id="tradedateend-input"]')
			sleep(1)
			
			# 点击查询
			click("xpath", "//span[text()='查询']")
			sleep(1)
			# 用隐式等待方法等页面出现预期数据：当前余额:32,784,989.82
			implici_wait("xpath", "//div[@title='当前余额:32,784,989.82']")
			print("当前以及下级组织明细查看，当前以及下级组织明细查看成功！")
			time.sleep(3)
			
			# 退出所有iframe窗体
			switch_default()
			
			logging.info("现在开始测试可操作组织明细查看功能")
			# 切入‘应收票据查看’的iframe窗体
			switch_to("xpath", "//iframe[@id='accountDetailView-tab-iframe']")
			sleep(1)
			
			click("xpath", "//span[text()='可操作组织明细查看']")
			sleep(1)
			
			switch_to("xpath", "//iframe[@id='subTab2-iframe']")
			sleep(1)
			# 点击查看
			# 用JS的方法点击放大镜
			js_click("xpath", "//span[@class='f-contrac-close']")
			sleep(1)
			
			click("xpath", "//input[@id='combobox-input-bankid']")
			# 输入内容
			input("xpath", "//input[@id='combobox-input-bankid']", "中国银行")
			sleep(1)
			click("xpath", "//div[@title='代码-名称:BOC-中国银行']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
			sleep(1)
			
			input("xpath", "//input[@id='oppositeaccountname']", "秦燕")
			sleep(1)
			
			# 点击查询
			click("xpath", "//span[text()='查询']")
			
			# 用隐式等待方法等页面出现预期数据：当前余额:32,784,989.82
			implici_wait("xpath", "//div[@title='当前余额:32,784,989.82']")
			print("可操作组织明细查看，可操作组织明细查看成功！")
			time.sleep(3)
			
			# 退出所有iframe窗体
			switch_default()
			
			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='账户明细查看']/child::*[1]")
			# 打印操作成功日志
			print("账户明细查看，操作成功!")
			logging.info("账户明细查看，操作成功!")
			time.sleep(2)
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("账户明细查看,失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		
		# 测试离线账户日结
		try:
			# 点击账户生命周期'菜单
			click("xpath", "//span[text()='离线账户日结']")
			# 退出所有iframe窗体
			switch_default()
			
			logging.info("开始测试离线账户日结功能")
			# 切入‘银行账户查看’的iframe窗体
			switch_to("xpath", "//iframe[@id='knotDates-tab-iframe']")
			sleep(1)
			switch_to("xpath", "//iframe[@id='subTabOne-iframe']")
			sleep(1)
			
			click("xpath", "//span[text()='日结']")
			sleep(1)
			click("xpath", "//span[text()='确定']")
			sleep(1)
			
			# 退出所有iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'成功日结')]")
			print("离线账户日结，日结成功！")
			logging.info("离线账户日结，日结成功！")
			time.sleep(3)
			
			switch_default()
			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='离线账户日结']/child::*[1]")
			
			# 打印操作成功日志
			print("离线账户日结，操作成功!")
			logging.info("离线账户日结，操作成功!")
			time.sleep(2)
			
			# 离线账户日结后通过付款单查看日结对非直联账户的影响
			# 切换到付款处理页面
			# 支票登记后去付款处理新增该账户的付款单
			logging.info("开始测试资金结算管理的页面功能")
			# 将页面的滚动条滑动到‘资金结算管理’页面的地方
			js_gd("xpath", "//span[contains(text(),'资金结算管理')]")
			# 用JS的方法点击资金结算管理菜单按钮
			js_click("xpath", "//span[contains(text(),'资金结算管理')]")
			
			# 付款处理--其他支付
			try:
				
				# 点击资金系统收付菜单
				js_click("xpath", "//span[@title='资金系统收付']")
				# 点击应付支票领用菜单
				js_click("xpath", "//span[@title='付款处理']")
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
				input("xpath", "//input[@id='combobox-input-settlementmodeid']", "其他支付")
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
				
				# 用隐式等待方法等页面出现审核的提示框
				
				implici_wait("xpath", "//span[contains(text(),'不允许维护该日之前的数据！！')]")
				print("其他支付，非直联账户日结影响查看成功！")
				logging.info("其他支付，非直联账户日结影响查看成功！")
				time.sleep(3)
			
			except Exception as err:
				# 发生其他异常时，打印异常堆栈信息
				print(traceback.print_exc())
				logging.debug("其他支付，非直联账户日结影响查看失败！" + str(traceback.format_exc()))
				# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
				dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
				dir_path = make_current_hour_dir(dir_path + "\\")
				pic_path = os.path.join(dir_path, get_current_time() + ".png")
				capture(pic_path)
			
			logging.info("开始测试账户资金监控的页面功能")
			# 将页面的滚动条滑动到‘票据管理’页面的地方
			js_gd("xpath", "//span[contains(text(),'账户资金监控')]")
			# 用JS的方法点击票据管理菜单按钮
			js_click("xpath", "//span[contains(text(),'账户资金监控')]")
			
			# 点击账户生命周期'菜单
			click("xpath", "//span[text()='离线账户日结']")
			
			# 退出所有iframe窗体
			switch_default()
			
			switch_to("xpath", "//iframe[@id='knotDates-tab-iframe']")
			sleep(1)
			click("xpath", "//span[text()='日结记录']")
			sleep(1)
			
			switch_to("xpath", "//iframe[@id='subTabTwo-iframe']")
			sleep(1)
			# 点击查看
			# 用JS的方法点击放大镜
			js_click("xpath", "//span[@class='f-contrac-close']")
			sleep(1)
			
			# 点击查询
			click("xpath", "//span[text()='查询']")
			
			# 用隐式等待方法等页面出现预期数据：Mindy科技有限公司
			implici_wait("xpath", "//div[contains(text(),'Mindy科技有限公司')]")
			print("日结记录，日结记录查看成功！")
			time.sleep(3)
			
			switch_default()
			logging.info("开始测试离线账户反日结功能")
			# 切入‘银行账户查看’的iframe窗体
			switch_to("xpath", "//iframe[@id='knotDates-tab-iframe']")
			sleep(1)
			click("xpath", "//span[text()='日结']")
			sleep(1)
			switch_to("xpath", "//iframe[@id='subTabOne-iframe']")
			sleep(1)
			click("xpath", "//span[text()='反日结']")
			sleep(1)
			
			# 选择日结日期
			today = date.today()
			knotdat = today
			click("xpath", "//input[@id='knotdatewin-input']")
			sleep(1)
			input("xpath", "//input[@id='knotdatewin-input']", str(knotdat))
			# 模拟回车键
			keyDown('enter')
			keyUp('enter')
			time.sleep(2)
			
			double_click("xpath", "//input[@id='includesub']")
			sleep(1)
			
			click("xpath", "//span[text()='确定']")
			sleep(1)
			
			# 退出所有iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'成功反日结')]")
			print("离线账户反日结，反日结成功！")
			logging.info("离线账户反日结，反日结成功！")
			time.sleep(3)
			
			logging.info("现在开始测试日结记录功能")
			# 切入‘应收票据查看’的iframe窗体
			switch_to("xpath", "//iframe[@id='knotDates-tab-iframe']")
			sleep(1)
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("离线账户日结,失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)


# # # def tearDown(self):
# # #     self.driver.quit()
# print("结束时间：", time.strftime("%Y-%m-%d %H:%M:%S"))


if __name__ == '__main__':
	#  启动单元测试
	unittest.main(verbosity=2)

