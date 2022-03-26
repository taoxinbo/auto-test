# encoding=utf-8
# @Time : 2020/9/7 8:47
# @Author : Mindy
# 此文件用来测试融资管理模块，包括基础设置
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


class Test_Rzgl_Jcsz(unittest.TestCase):
	
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
		
		logging.info("开始测试融资管理的页面功能")
		# 将页面的滚动条滑动到‘融资管理’页面的地方
		js_gd("xpath", "//span[contains(text(),'融资管理')]")
		# 用JS的方法点击融资管理菜单按钮
		js_click("xpath", "//span[contains(text(),'融资管理')]")
		"""
		# 测试基础设置-发票登记
		try:
			# 点击基础设置菜单
			click("xpath", "//li[@f_value='loanSetting']/descendant-or-self::*[5]")
			# 点击发票登记菜单
			click("xpath", "//span[text()='发票登记']")
			# 退出所有iframe窗体
			switch_default()

			for i in range(1, 3):
				# 切入发票登记的iframe窗体
				switch_to("xpath", "//iframe[@id='collateralinvoices-tab-iframe']")
				logging.info("开始测试发票登记功能")

				# 用JS的方法点击新增按钮
				js_click("xpath", "//span[text()='新增']")

				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='addWin-iframe']")
				sleep(1)
				
				# 输入发票编号
				input("xpath", "//input[@name='code']", "TestCollaLin")
				sleep(1)
				
				# 输入发票日期
				today = date.today()
				invoice_date = today
				click("xpath", "//input[@id='invoicedate-input']")
				sleep(1)
				clear("xpath", "//input[@id='invoicedate-input']")
				sleep(1)
				input("xpath", "//input[@id='invoicedate-input']", str(invoice_date))
				# 模拟回车键
				keyDown('enter')
				keyUp('enter')
				time.sleep(1)

				# 输入票面金额
				clear("xpath", "//input[@id='amount-input']")
				sleep(1)
				input("xpath", "//input[@id='amount-input']", "30000")
				sleep(1)
				
				# 供应方
				input("xpath", "//input[@id='supplier']", "Mindy")
				sleep(1)
				
				# 销售方
				input("xpath", "//input[@id='seller']", "mindy")
				sleep(1)

				# 描述框中填入值
				input("xpath", "//textarea[@id='memo']", "自动化测试发票登记描述框")
				sleep(1)

				# 点击保存按钮
				click("xpath", "//span[text()='保存']")

				# 退出所有iframe窗体
				switch_default()

				# 用隐式等待方法等页面出现新增成功的提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				print("发票登记，保存成功！")
				time.sleep(3)

				if i == 1:
					# 删除功能
					# 切入发票登记的iframe窗体
					switch_to("xpath", "//iframe[@id='collateralinvoices-tab-iframe']")

					# 点击查看
					# 用JS的方法点击放大镜
					js_click("xpath", "//span[@class='f-contrac-close']")
					sleep(1)

					# 输入发票编码
					input("xpath", "//input[@id='code']", "TestCollaLin")
					sleep(1)

					# 点击查询
					click("xpath", "//span[text()='查询']")

					# 勾选
					click("xpath", "//div[@title='发票编号:TestCollaLin']/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 点击删除按钮
					click("xpath", "//span[text()='删除']")

					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现删除的提示框
					implici_wait("xpath", "//span[contains(text(),'成功删除1条记录')]")
					print("发票登记，删除成功！")
					time.sleep(3)

			# 切入‘发票登记’的iframe窗体
			switch_to("xpath", "//iframe[@id='collateralinvoices-tab-iframe']")

			# 点击查看
			# 清空代码框的内容
			clear("xpath", "//input[@id='code']")
			sleep(1)

			# 输入用途代码：
			input("xpath", "//input[@id='code']", "TestCollaLin")
			sleep(1)

			# 点击查询
			click("xpath", "//span[text()='查询']")

			# 修改
			# 勾选
			click("xpath", "//div[@title='发票编号:TestCollaLin']/parent::*/preceding-sibling::*[1]/descendant::*[2]")

			# 点击修改按钮
			click("xpath", "//span[text()='修改']")

			# 切入修改的iframe窗体
			switch_to("xpath", "//iframe[@id='modWin-iframe']")
			sleep(1)

			# 修改描述框中的内容
			input("xpath", "//textarea[@id='memo']", "自动化测试修改")
			sleep(1)

			# 点击保存按钮
			click("xpath", "//span[text()='保存']")

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("发票登记，修改成功！")
			time.sleep(3)

			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='发票登记']/child::*[1]")

			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//li[@f_value='billSetting']/descendant-or-self::*[5]")

			# 打印操作成功日志
			print("发票登记，操作成功!")
			logging.info("发票登记，操作成功!")
			time.sleep(2)
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("发票登记打印失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		
		# 测试基础设置-融资产品
		try:
			# 点击基础设置菜单
			click("xpath", "//li[@f_value='loanSetting']/descendant-or-self::*[5]")
			# 点击融资产品菜单
			click("xpath", "//span[text()='融资产品']")
			# 退出所有iframe窗体
			switch_default()
			
			for i in range(1, 3):
				# 切入融资产品的iframe窗体
				switch_to("xpath", "//iframe[@id='products-tab-iframe']")
				logging.info("开始测试融资产品功能")
				
				# 用JS的方法点击新增按钮
				js_click("xpath", "//span[text()='新增']")
				
				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='addproductsWin-iframe']")
				sleep(1)
				
				# 输入代码
				input("xpath", "//input[@name='code']", "TestCollProduct")
				sleep(1)
				
				# 输入的名称
				input("xpath", "//input[@id='name']", "自动化测试融资产品")
				sleep(1)
				
				# 选择融资机构
				click("xpath", "//input[@id='combobox-input-financialinstitutiontype']")
				sleep(1)
				input("xpath", "//input[@id='combobox-input-financialinstitutiontype']", "银行")
				sleep(1)
				input_enter("xpath", "//input[@id='combobox-input-financialinstitutiontype']")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-financialinstitutiontype']")
				sleep(1)
				input_enter("xpath", "//input[@id='combobox-input-financialinstitutiontype']")
				sleep(1)
				
				# 描述框中填入值
				input("xpath", "//textarea[@id='description']", "自动化测试融资产品描述框")
				sleep(1)
				
				# 点击保存按钮
				click("xpath", "//span[text()='保存']")
				
				# 退出所有iframe窗体
				switch_default()
				
				# 用隐式等待方法等页面出现新增成功的提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				print("融资产品，保存成功！")
				time.sleep(3)
				
				if i == 1:
					# 删除功能
					# 切入融资产品的iframe窗体
					switch_to("xpath", "//iframe[@id='products-tab-iframe']")
					
					# 点击查看
					# 用JS的方法点击放大镜
					js_click("xpath", "//span[@class='f-contrac-close']")
					sleep(1)
					
					# 输入代码：
					input("xpath", "//input[@id='code']", "TestCollProduct")
					sleep(1)
					
					# 点击查询
					click("xpath", "//span[text()='查询']")
					
					# 勾选
					click("xpath", "//div[@title='代码:TestCollProduct']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
					
					# 点击删除按钮
					click("xpath", "//span[text()='删除']")
					
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现删除的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("融资产品，删除成功！")
					time.sleep(3)
			
			# 切入‘融资产品’的iframe窗体
			switch_to("xpath", "//iframe[@id='products-tab-iframe']")
			
			# 点击查看
			# 清空代码框的内容
			clear("xpath", "//input[@id='code']")
			sleep(1)
			
			# 输入代码：
			input("xpath", "//input[@id='code']", "TestCollProduct")
			sleep(1)
			
			# 点击查询
			click("xpath", "//span[text()='查询']")
			
			# 修改
			# 勾选
			click("xpath", "//div[@title='代码:TestCollProduct']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
			
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
			print("融资产品，修改成功！")
			time.sleep(3)
			
			# 切入‘融资产品’的iframe窗体
			switch_to("xpath", "//iframe[@id='products-tab-iframe']")
			
			# 失效按钮
			# 勾选
			click("xpath", "//div[@title='代码:TestCollProduct']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
			
			# 点击失效按钮
			click("xpath", "//span[text()='失效']")
			
			# 退出所有iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'失效成功！')]")
			print("融资产品，点击失效成功！")
			time.sleep(3)
			
			# 切入‘融资产品’的iframe窗体
			switch_to("xpath", "//iframe[@id='products-tab-iframe']")
			
			# 生效按钮
			# 勾选
			click("xpath", "//div[@title='代码:TestCollProduct']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
			
			# 点击生效按钮
			click("xpath", "//span[text()='生效']")
			
			# 退出所有iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'生效成功！')]")
			print("融资产品，点击生效成功！")
			time.sleep(3)
			
			# 删除功能
			# 切入融资产品的iframe窗体
			switch_to("xpath", "//iframe[@id='products-tab-iframe']")
			
			# 勾选
			click("xpath", "//div[@title='代码:TestCollProduct']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
			
			# 点击删除按钮
			click("xpath", "//span[text()='删除']")
			
			# 点击弹出框的OK键
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
			
			# 退出所有iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功')]")
			print("融资产品，删除成功！")
			time.sleep(3)
			
			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='融资产品']/child::*[1]")
			
			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//li[@f_value='loanSetting']/descendant-or-self::*[5]")
			
			# 打印操作成功日志
			print("融资产品，操作成功!")
			logging.info("融资产品，操作成功!")
			time.sleep(2)
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("融资产品失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		
		# 测试基础设置-授信类别
		try:
			# 点击基础设置菜单
			click("xpath", "//li[@f_value='loanSetting']/descendant-or-self::*[5]")
			# 点击授信类别菜单
			click("xpath", "//span[text()='授信类别']")
			# 退出所有iframe窗体
			switch_default()
			
			for i in range(1, 3):
				# 切入授信类别的iframe窗体
				switch_to("xpath", "//iframe[@id='creditcategory-tab-iframe']")
				logging.info("开始测试授信类别功能")
				
				# 用JS的方法点击新增按钮
				js_click("xpath", "//span[text()='新增']")
				
				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='addcreditcategoryWin-iframe']")
				sleep(1)
				
				# 输入代码
				input("xpath", "//input[@id='code']", "TestCreditCategory")
				sleep(1)
				
				# 输入的名称
				input("xpath", "//input[@id='name']", "自动化测试授信类别")
				sleep(1)
				
				# 描述框中填入值
				input("xpath", "//textarea[@id='description']", "自动化测试授信类别描述框")
				sleep(1)
				
				# 点击保存按钮
				click("xpath", "//span[text()='保存']")
				
				# 退出所有iframe窗体
				switch_default()
				
				# 用隐式等待方法等页面出现新增成功的提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				print("授信类别，保存成功！")
				time.sleep(3)
				
				if i == 1:
					# 删除功能
					# 切入授信类别的iframe窗体
					switch_to("xpath", "//iframe[@id='creditcategory-tab-iframe']")
					
					# 点击查看
					# 用JS的方法点击放大镜
					js_click("xpath", "//span[@class='f-contrac-close']")
					sleep(1)
					
					# 输入代码：
					input("xpath", "//input[@id='code']", "TestCreditCategory")
					sleep(1)
					
					# 点击查询
					click("xpath", "//span[text()='查询']")
					
					# 勾选
					click("xpath", "//div[@title='代码:TestCreditCategory']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
					
					# 点击删除按钮
					click("xpath", "//span[text()='删除']")
					
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现删除的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("授信类别，删除成功！")
					time.sleep(3)
			
			# 切入‘授信类别’的iframe窗体
			switch_to("xpath", "//iframe[@id='creditcategory-tab-iframe']")
			
			# 点击查看
			# 清空代码框的内容
			clear("xpath", "//input[@id='code']")
			sleep(1)
			
			# 输入代码：
			input("xpath", "//input[@id='code']", "TestCreditCategory")
			sleep(1)
			
			# 点击查询
			click("xpath", "//span[text()='查询']")
			
			# 修改
			# 勾选
			click("xpath", "//div[@title='代码:TestCreditCategory']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
			
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
			print("授信类别，修改成功！")
			time.sleep(3)
			
			# 切入‘授信类别’的iframe窗体
			switch_to("xpath", "//iframe[@id='creditcategory-tab-iframe']")
			
			# 失效按钮
			# 勾选
			click("xpath", "//div[@title='代码:TestCreditCategory']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
			
			# 点击失效按钮
			click("xpath", "//span[text()='失效']")
			
			# 退出所有iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'失效成功！')]")
			print("授信类别，点击失效成功！")
			time.sleep(3)
			
			# 切入‘授信类别’的iframe窗体
			switch_to("xpath", "//iframe[@id='creditcategory-tab-iframe']")
			
			# 生效按钮
			# 勾选
			click("xpath", "//div[@title='代码:TestCreditCategory']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
			
			# 点击生效按钮
			click("xpath", "//span[text()='生效']")
			
			# 退出所有iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'生效成功！')]")
			print("授信类别，点击生效成功！")
			time.sleep(3)
			
			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='授信类别']/child::*[1]")
			
			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//li[@f_value='loanSetting']/descendant-or-self::*[5]")
			
			# 打印操作成功日志
			print("授信类别，操作成功!")
			logging.info("授信类别，操作成功!")
			time.sleep(2)
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("授信类别失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		
		# 测试基础设置-抵质押物类别
		try:
			# 点击基础设置菜单
			click("xpath", "//li[@f_value='loanSetting']/descendant-or-self::*[5]")
			# 点击抵质押物类别菜单
			click("xpath", "//span[text()='抵质押物类别']")
			# 退出所有iframe窗体
			switch_default()
			
			for i in range(1, 3):
				# 切入抵质押物类别的iframe窗体
				switch_to("xpath", "//iframe[@id='collateralcategory-tab-iframe']")
				logging.info("开始测试抵质押物类别功能")
				
				# 用JS的方法点击新增按钮
				js_click("xpath", "//span[text()='新增']")
				
				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='addcollateralcategoryWin-iframe']")
				sleep(1)
				
				# 输入代码
				input("xpath", "//input[@id='code']", "TestCollRalc")
				sleep(1)
				
				# 输入的名称
				input("xpath", "//input[@id='name']", "自动化测试抵质押物类别")
				sleep(1)
				
				# 业务类别
				click("xpath", "//input[@id='combobox-input-classification']")
				sleep(1)
				input("xpath", "//input[@id='combobox-input-classification']", "抵押类型")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-classification']")
				sleep(1)
				input_enter("xpath", "//input[@id='combobox-input-classification']")
				sleep(1)
				
				# 描述框中填入值
				input("xpath", "//textarea[@id='description']", "自动化测试抵质押物类别描述框")
				sleep(1)
				
				# 点击保存按钮
				click("xpath", "//span[text()='保存']")
				
				# 退出所有iframe窗体
				switch_default()
				
				# 用隐式等待方法等页面出现新增成功的提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				print("抵质押物类别，保存成功！")
				time.sleep(3)
				
				if i == 1:
					# 删除功能
					# 切入抵质押物类别的iframe窗体
					switch_to("xpath", "//iframe[@id='collateralcategory-tab-iframe']")
					
					# 点击查看
					# 用JS的方法点击放大镜
					js_click("xpath", "//span[@class='f-contrac-close']")
					sleep(1)
					
					# 输入代码：
					input("xpath", "//input[@id='code']", "TestCollRalc")
					sleep(1)
					
					# 点击查询
					click("xpath", "//span[text()='查询']")
					
					# 勾选
					click("xpath", "//div[@title='代码:TestCollRalc']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
					
					# 点击删除按钮
					click("xpath", "//span[text()='删除']")
					
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现删除的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功')]")
					print("抵质押物类别，删除成功！")
					time.sleep(3)
			
			# 切入‘抵质押物类别’的iframe窗体
			switch_to("xpath", "//iframe[@id='collateralcategory-tab-iframe']")
			
			# 点击查看
			# 清空代码框的内容
			clear("xpath", "//input[@id='code']")
			sleep(1)
			
			# 输入代码：
			input("xpath", "//input[@id='code']", "TestCollRalc")
			sleep(1)
			
			# 点击查询
			click("xpath", "//span[text()='查询']")
			
			# 修改
			# 勾选
			click("xpath", "//div[@title='代码:TestCollRalc']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
			
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
			print("抵质押物类别，修改成功！")
			time.sleep(3)
			
			# 切入‘抵质押物类别’的iframe窗体
			switch_to("xpath", "//iframe[@id='collateralcategory-tab-iframe']")
			
			# 失效按钮
			# 勾选
			click("xpath", "//div[@title='代码:TestCollRalc']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
			
			# 点击失效按钮
			click("xpath", "//span[text()='失效']")
			
			# 退出所有iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'失效成功！')]")
			print("抵质押物类别，点击失效成功！")
			time.sleep(3)
			
			# 切入‘抵质押物类别’的iframe窗体
			switch_to("xpath", "//iframe[@id='collateralcategory-tab-iframe']")
			
			# 生效按钮
			# 勾选
			click("xpath", "//div[@title='代码:TestCollRalc']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
			
			# 点击生效按钮
			click("xpath", "//span[text()='生效']")
			
			# 退出所有iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'生效成功！')]")
			print("抵质押物类别，点击生效成功！")
			time.sleep(3)
			
			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='抵质押物类别']/child::*[1]")
			
			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//li[@f_value='loanSetting']/descendant-or-self::*[5]")
			
			# 打印操作成功日志
			print("抵质押物类别，操作成功!")
			logging.info("抵质押物类别，操作成功!")
			time.sleep(2)
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("抵质押物类别失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		
		# 测试基础设置-组织融资额度
		try:
			# 点击基础设置菜单
			click("xpath", "//li[@f_value='loanSetting']/descendant-or-self::*[5]")
			# 点击组织融资额度菜单
			click("xpath", "//span[text()='组织融资额度']")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()

			for i in range(1, 3):
				# 切入组织融资额度的iframe窗体
				switch_to("xpath", "//iframe[@id='loanquotas-tab-iframe']")
				logging.info("开始测试组织融资额度功能")

				# 用JS的方法点击新增按钮
				js_click("xpath", "//span[text()='新增']")

				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='addWin-iframe']")
				sleep(1)

				# 组织
				click("xpath", "//input[@id='combobox-input-orgid']")
				sleep(1)
				input("xpath", "//input[@id='combobox-input-orgid']", "亚唐科技")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-orgid']")
				sleep(1)
				input_enter("xpath", "//input[@id='combobox-input-orgid']")
				sleep(1)
				
				# 融资年份
				click("xpath", "//input[@id='loanyear-input']")
				sleep(1)
				input_down("xpath", "//input[@id='loanyear-input']")
				sleep(1)
				input_enter("xpath", "//input[@id='loanyear-input']")
				sleep(1)
				
				# 币种
				click("xpath", "//input[@id='combobox-input-currencyid']")
				sleep(1)
				input("xpath", "//input[@id='combobox-input-currencyid']", "人民币")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-currencyid']")
				sleep(1)
				input_enter("xpath", "//input[@id='combobox-input-currencyid']")
				sleep(1)
				
				# 融资额度
				clear("xpath", "//input[@id='loanamount-input']")
				sleep(1)
				input("xpath", "//input[@id='loanamount-input']", "200000000")
				sleep(1)

				# 描述框中填入值
				input("xpath", "//textarea[@id='description']", "自动化测试组织融资额度描述框")
				sleep(1)

				# 点击保存按钮
				click("xpath", "//span[text()='保存']")

				# 退出所有iframe窗体
				switch_default()

				# 用隐式等待方法等页面出现新增成功的提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				print("组织融资额度，保存成功！")
				time.sleep(3)

				if i == 1:
					# 删除功能
					# 切入组织融资额度的iframe窗体
					switch_to("xpath", "//iframe[@id='loanquotas-tab-iframe']")

					# 勾选
					click("xpath", "//div[contains(text(),'亚唐科技')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 点击删除按钮
					click("xpath", "//span[text()='删除']")

					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现删除的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功')]")
					print("组织融资额度，删除成功！")
					time.sleep(3)

			# 切入‘组织融资额度’的iframe窗体
			switch_to("xpath", "//iframe[@id='loanquotas-tab-iframe']")

			# 修改
			# 勾选
			click("xpath", "//div[contains(text(),'亚唐科技')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

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
			print("组织融资额度，修改成功！")
			time.sleep(3)

			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='组织融资额度']/child::*[1]")

			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//li[@f_value='loanSetting']/descendant-or-self::*[5]")

			# 打印操作成功日志
			print("组织融资额度，操作成功!")
			logging.info("组织融资额度，操作成功!")
			time.sleep(2)
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("组织融资额度打印失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
			
		# 测试基础设置-贷款方式
		try:
			# 点击基础设置菜单
			click("xpath", "//li[@f_value='loanSetting']/descendant-or-self::*[5]")
			# 点击贷款方式菜单
			click("xpath", "//span[text()='贷款方式']")
			# 退出所有iframe窗体
			switch_default()
			
			for i in range(1, 3):
				# 切入贷款方式的iframe窗体
				switch_to("xpath", "//iframe[@id='loanmode-tab-iframe']")
				logging.info("开始测试贷款方式功能")
				
				# 用JS的方法点击新增按钮
				js_click("xpath", "//span[text()='新增']")
				
				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='addloanmodeWin-iframe']")
				sleep(1)
				
				# 输入代码
				input("xpath", "//input[@name='code']", "TestLoanMode")
				sleep(1)
				
				# 输入的名称
				input("xpath", "//input[@id='name']", "自动化测试贷款方式")
				sleep(1)
				
				# 描述框中填入值
				input("xpath", "//textarea[@id='description']", "自动化测试贷款方式描述框")
				sleep(1)
				
				# 点击保存按钮
				click("xpath", "//span[text()='保存']")
				
				# 退出所有iframe窗体
				switch_default()
				
				# 用隐式等待方法等页面出现新增成功的提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				print("贷款方式，保存成功！")
				time.sleep(3)
				
				if i == 1:
					# 删除功能
					# 切入贷款方式的iframe窗体
					switch_to("xpath", "//iframe[@id='loanmode-tab-iframe']")
					
					# 点击查看
					# 用JS的方法点击放大镜
					js_click("xpath", "//span[@class='f-contrac-close']")
					sleep(1)
					
					# 输入代码：
					input("xpath", "//input[@id='code']", "TestLoanMode")
					sleep(1)
					
					# 点击查询
					click("xpath", "//span[text()='查询']")
					
					# 勾选
					click("xpath", "//div[@title='代码:TestLoanMode']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
					
					# 点击删除按钮
					click("xpath", "//span[text()='删除']")
					
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现删除的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功')]")
					print("贷款方式，删除成功！")
					time.sleep(3)
			
			# 切入‘贷款方式’的iframe窗体
			switch_to("xpath", "//iframe[@id='loanmode-tab-iframe']")
			
			# 点击查看
			# 清空代码框的内容
			clear("xpath", "//input[@id='code']")
			sleep(1)
			
			# 输入代码：
			input("xpath", "//input[@id='code']", "TestLoanMode")
			sleep(1)
			
			# 点击查询
			click("xpath", "//span[text()='查询']")
			
			# 修改
			# 勾选
			click("xpath", "//div[@title='代码:TestLoanMode']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
			
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
			print("贷款方式，修改成功！")
			time.sleep(3)
			
			# 切入‘贷款方式’的iframe窗体
			switch_to("xpath", "//iframe[@id='loanmode-tab-iframe']")
			
			# 失效按钮
			# 勾选
			click("xpath", "//div[@title='代码:TestLoanMode']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
			
			# 点击失效按钮
			click("xpath", "//span[text()='失效']")
			
			# 退出所有iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'失效成功！')]")
			print("贷款方式，点击失效成功！")
			time.sleep(3)
			
			# 切入‘贷款方式’的iframe窗体
			switch_to("xpath", "//iframe[@id='loanmode-tab-iframe']")
			
			# 生效按钮
			# 勾选
			click("xpath", "//div[@title='代码:TestLoanMode']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
			
			# 点击生效按钮
			click("xpath", "//span[text()='生效']")
			
			# 退出所有iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'生效成功！')]")
			print("贷款方式，点击生效成功！")
			time.sleep(3)
			
			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='贷款方式']/child::*[1]")
			
			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//li[@f_value='loanSetting']/descendant-or-self::*[5]")
			
			# 打印操作成功日志
			print("贷款方式，操作成功!")
			logging.info("贷款方式，操作成功!")
			time.sleep(2)
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("贷款方式失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		
		# 测试基础设置-融资类别
		try:
			# 点击基础设置菜单
			click("xpath", "//li[@f_value='loanSetting']/descendant-or-self::*[5]")
			# 点击融资类别菜单
			click("xpath", "//span[text()='融资类别']")
			# 退出所有iframe窗体
			switch_default()
			
			for i in range(1, 3):
				# 切入融资类别的iframe窗体
				switch_to("xpath", "//iframe[@id='financingcategory-tab-iframe']")
				logging.info("开始测试融资类别功能")
				
				# 用JS的方法点击新增按钮
				js_click("xpath", "//span[text()='新增']")
				
				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='addfinancingcategoryWin-iframe']")
				sleep(1)
				
				# 输入代码
				input("xpath", "//input[@name='code']", "TestFinancCate")
				sleep(1)
				
				# 输入的名称
				input("xpath", "//input[@id='name']", "自动化测试融资类别")
				sleep(1)
				
				# 描述框中填入值
				input("xpath", "//textarea[@id='description']", "自动化测试融资类别描述框")
				sleep(1)
				
				# 点击保存按钮
				click("xpath", "//span[text()='保存']")
				
				# 退出所有iframe窗体
				switch_default()
				
				# 用隐式等待方法等页面出现新增成功的提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				print("融资类别，保存成功！")
				time.sleep(3)
				
				if i == 1:
					# 删除功能
					# 切入融资类别的iframe窗体
					switch_to("xpath", "//iframe[@id='financingcategory-tab-iframe']")
					
					# 点击查看
					# 用JS的方法点击放大镜
					js_click("xpath", "//span[@class='f-contrac-close']")
					sleep(1)
					
					# 输入代码：
					input("xpath", "//input[@id='code']", "TestFinancCate")
					sleep(1)
					
					# 点击查询
					click("xpath", "//span[text()='查询']")
					
					# 勾选
					click("xpath", "//div[@title='代码:TestFinancCate']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
					
					# 点击删除按钮
					click("xpath", "//span[text()='删除']")
					
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现删除的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功')]")
					print("融资类别，删除成功！")
					time.sleep(3)
			
			# 切入‘融资类别’的iframe窗体
			switch_to("xpath", "//iframe[@id='financingcategory-tab-iframe']")
			
			# 点击查看
			# 清空代码框的内容
			clear("xpath", "//input[@id='code']")
			sleep(1)
			
			# 输入代码：
			input("xpath", "//input[@id='code']", "TestFinancCate")
			sleep(1)
			
			# 点击查询
			click("xpath", "//span[text()='查询']")
			
			# 修改
			# 勾选
			click("xpath", "//div[@title='代码:TestFinancCate']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
			
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
			print("融资类别，修改成功！")
			time.sleep(3)
			
			# 切入‘融资类别’的iframe窗体
			switch_to("xpath", "//iframe[@id='financingcategory-tab-iframe']")
			
			# 失效按钮
			# 勾选
			click("xpath", "//div[@title='代码:TestFinancCate']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
			
			# 点击失效按钮
			click("xpath", "//span[text()='失效']")
			
			# 退出所有iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'失效成功！')]")
			print("融资类别，点击失效成功！")
			time.sleep(3)
			
			# 切入‘融资类别’的iframe窗体
			switch_to("xpath", "//iframe[@id='financingcategory-tab-iframe']")
			
			# 生效按钮
			# 勾选
			click("xpath", "//div[@title='代码:TestFinancCate']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
			
			# 点击生效按钮
			click("xpath", "//span[text()='生效']")
			
			# 退出所有iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'生效成功！')]")
			print("融资类别，点击生效成功！")
			time.sleep(3)
			
			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='融资类别']/child::*[1]")
			
			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//li[@f_value='loanSetting']/descendant-or-self::*[5]")
			
			# 打印操作成功日志
			print("融资类别，操作成功!")
			logging.info("融资类别，操作成功!")
			time.sleep(2)
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("融资类别失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		
		# 测试基础设置-附件查看
		# 测试基础设置-补充信息类型
		try:
			# 点击基础设置菜单
			click("xpath", "//li[@f_value='loanSetting']/descendant-or-self::*[5]")
			# 点击补充信息类型菜单
			click("xpath", "//span[text()='补充信息类型']")
			# 退出所有iframe窗体
			switch_default()

			for i in range(1, 3):
				# 切入补充信息类型的iframe窗体
				switch_to("xpath", "//iframe[@id='supplementinfotype-tab-iframe']")
				logging.info("开始测试补充信息类型功能")

				# 用JS的方法点击新增按钮
				js_click("xpath", "//span[text()='新增']")

				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='addproductsWin-iframe']")
				sleep(1)

				# 输入用途代码
				input("xpath", "//input[@name='code']", "TestSupInfoType")
				sleep(1)

				# 输入补充信息类型
				input("xpath", "//input[@id='name']", "自动化测试补充信息类型")
				sleep(1)

				# 描述框中填入值
				input("xpath", "//textarea[@id='description']", "自动化测试补充信息类型描述框")
				sleep(1)

				# 点击保存按钮
				click("xpath", "//span[text()='保存']")

				# 退出所有iframe窗体
				switch_default()

				# 用隐式等待方法等页面出现新增成功的提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				print("补充信息类型，保存成功！")
				time.sleep(3)

				if i == 1:
					# 删除功能
					# 切入补充信息类型的iframe窗体
					switch_to("xpath", "//iframe[@id='supplementinfotype-tab-iframe']")

					# 点击查看
					# 用JS的方法点击放大镜
					js_click("xpath", "//span[@class='f-contrac-close']")
					sleep(1)

					# 输入代码：
					input("xpath", "//input[@id='code']", "TestSupInfoType")
					sleep(1)

					# 点击查询
					click("xpath", "//span[text()='查询']")

					# 勾选
					click("xpath", "//div[@title='代码:TestSupInfoType']/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 点击删除按钮
					click("xpath", "//span[text()='删除']")

					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现删除的提示框
					implici_wait("xpath", "//span[contains(text(),'成功删除1条记录！')]")
					print("补充信息类型，删除成功！")
					time.sleep(3)

			# 切入‘补充信息类型’的iframe窗体
			switch_to("xpath", "//iframe[@id='supplementinfotype-tab-iframe']")

			# 修改
			# 勾选
			click("xpath", "//div[@title='代码:TestSupInfoType']/parent::*/preceding-sibling::*[1]/descendant::*[2]")

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
			print("补充信息类型，修改成功！")
			time.sleep(3)

			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='补充信息类型']/child::*[1]")

			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//li[@f_value='loanSetting']/descendant-or-self::*[5]")

			# 打印操作成功日志
			print("补充信息类型，操作成功!")
			logging.info("补充信息类型，操作成功!")
			time.sleep(2)
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("补充信息类型打印失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		
		# 测试基础设置-融资进度
		try:
			# 点击基础设置菜单
			click("xpath", "//li[@f_value='loanSetting']/descendant-or-self::*[5]")
			# 点击融资进度菜单
			click("xpath", "//span[text()='融资进度']")
			# 退出所有iframe窗体
			switch_default()
			
			for i in range(1, 3):
				# 切入融资进度的iframe窗体
				switch_to("xpath", "//iframe[@id='financingprogress-tab-iframe']")
				logging.info("开始测试融资进度功能")
				
				# 用JS的方法点击新增按钮
				js_click("xpath", "//span[text()='新增']")
				
				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='addWin-iframe']")
				sleep(1)
				
				# 输入编码
				input("xpath", "//input[@name='code']", "TestFinPro")
				sleep(1)
				
				# 输入名称
				input("xpath", "//input[@id='name']", "自动化测试融资进度")
				sleep(1)
				
				# 描述框中填入值
				input("xpath", "//textarea[@id='description']", "自动化测试融资进度描述框")
				sleep(1)
				
				# 点击保存按钮
				click("xpath", "//span[text()='保存']")
				
				# 退出所有iframe窗体
				switch_default()
				
				# 用隐式等待方法等页面出现新增成功的提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				print("融资进度，保存成功！")
				time.sleep(3)
				
				if i == 1:
					# 删除功能
					# 切入融资进度的iframe窗体
					switch_to("xpath", "//iframe[@id='financingprogress-tab-iframe']")
					
					# 点击查看
					# 用JS的方法点击放大镜
					js_click("xpath", "//span[@class='f-contrac-close']")
					sleep(1)
					
					# 输入代码：
					input("xpath", "//input[@id='code']", "TestFinPro")
					sleep(1)
					
					# 点击查询
					click("xpath", "//span[text()='查询']")
					
					# 勾选
					click("xpath", "//div[@title='编码:TestFinPro']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
					
					# 点击删除按钮
					click("xpath", "//span[text()='删除']")
					
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现删除的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功')]")
					print("融资进度，删除成功！")
					time.sleep(3)
			
			# 切入‘融资进度’的iframe窗体
			switch_to("xpath", "//iframe[@id='financingprogress-tab-iframe']")
			
			# 点击查看
			# 清空代码框的内容
			clear("xpath", "//input[@id='code']")
			sleep(1)
			
			# 输入代码：
			input("xpath", "//input[@id='code']", "TestFinPro")
			sleep(1)
			
			# 点击查询
			click("xpath", "//span[text()='查询']")
			
			# 修改
			# 勾选
			click("xpath", "//div[@title='编码:TestFinPro']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
			
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
			print("融资进度，修改成功！")
			time.sleep(3)
			
			# 切入‘融资进度’的iframe窗体
			switch_to("xpath", "//iframe[@id='financingprogress-tab-iframe']")
			
			# 失效按钮
			# 勾选
			click("xpath", "//div[@title='编码:TestFinPro']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
			
			# 点击失效按钮
			click("xpath", "//span[text()='失效']")
			
			# 退出所有iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'失效成功1条')]")
			print("融资进度，点击失效成功！")
			time.sleep(3)
			
			# 切入‘融资进度’的iframe窗体
			switch_to("xpath", "//iframe[@id='financingprogress-tab-iframe']")
			
			# 生效按钮
			# 勾选
			click("xpath", "//div[@title='编码:TestFinPro']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
			
			# 点击生效按钮
			click("xpath", "//span[text()='生效']")
			
			# 退出所有iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'生效成功1条')]")
			print("融资进度，点击生效成功！")
			time.sleep(3)
			
			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='融资进度']/child::*[1]")
			
			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//li[@f_value='loanSetting']/descendant-or-self::*[5]")
			
			# 打印操作成功日志
			print("融资进度，操作成功!")
			logging.info("融资进度，操作成功!")
			time.sleep(2)
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("融资进度失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		
		# 测试基础设置-款项类型
		try:
			# 点击基础设置菜单
			click("xpath", "//li[@f_value='loanSetting']/descendant-or-self::*[5]")
			# 点击款项类型菜单
			click("xpath", "//span[text()='款项类型']")
			# 退出所有iframe窗体
			switch_default()
			
			for i in range(1, 3):
				# 切入款项类型的iframe窗体
				switch_to("xpath", "//iframe[@id='supplychaincategory-tab-iframe']")
				logging.info("开始测试款项类型功能")
				
				# 用JS的方法点击新增按钮
				js_click("xpath", "//span[text()='新增']")
				
				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='modWin-iframe']")
				sleep(1)
				
				# 输入代码
				input("xpath", "//input[@name='code']", "TestSupplyChain")
				sleep(1)
				
				# 输入的名称
				input("xpath", "//input[@id='name']", "自动化测试款项类型")
				sleep(1)
				
				# 描述框中填入值
				input("xpath", "//textarea[@id='description']", "自动化测试款项类型描述框")
				sleep(1)
				
				# 点击保存按钮
				click("xpath", "//span[text()='保存']")
				
				# 退出所有iframe窗体
				switch_default()
				
				# 用隐式等待方法等页面出现新增成功的提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				print("款项类型，保存成功！")
				time.sleep(3)
				
				if i == 1:
					# 删除功能
					# 切入款项类型的iframe窗体
					switch_to("xpath", "//iframe[@id='supplychaincategory-tab-iframe']")
					
					# 点击查看
					# 用JS的方法点击放大镜
					js_click("xpath", "//span[@class='f-contrac-close']")
					sleep(1)
					
					# 输入代码：
					input("xpath", "//input[@id='code']", "TestSupplyChain")
					sleep(1)
					
					# 点击查询
					click("xpath", "//span[text()='查询']")
					
					# 勾选
					click("xpath", "//div[@title='代码:TestSupplyChain']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
					
					# 点击删除按钮
					click("xpath", "//span[text()='删除']")
					
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现删除的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("款项类型，删除成功！")
					time.sleep(3)
			
			# 切入‘款项类型’的iframe窗体
			switch_to("xpath", "//iframe[@id='supplychaincategory-tab-iframe']")
			
			# 点击查看
			# 清空代码框的内容
			clear("xpath", "//input[@id='code']")
			sleep(1)
			
			# 输入代码：
			input("xpath", "//input[@id='code']", "TestSupplyChain")
			sleep(1)
			
			# 点击查询
			click("xpath", "//span[text()='查询']")
			
			# 修改
			# 勾选
			click("xpath", "//div[@title='代码:TestSupplyChain']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
			
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
			print("款项类型，修改成功！")
			time.sleep(3)
			
			# 切入‘款项类型’的iframe窗体
			switch_to("xpath", "//iframe[@id='supplychaincategory-tab-iframe']")
			
			# 失效按钮
			# 勾选
			click("xpath", "//div[@title='代码:TestSupplyChain']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
			
			# 点击失效按钮
			click("xpath", "//span[text()='失效']")
			
			# 退出所有iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'失效成功！')]")
			print("款项类型，点击失效成功！")
			time.sleep(3)
			
			# 切入‘款项类型’的iframe窗体
			switch_to("xpath", "//iframe[@id='supplychaincategory-tab-iframe']")
			
			# 生效按钮
			# 勾选
			click("xpath", "//div[@title='代码:TestSupplyChain']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
			
			# 点击生效按钮
			click("xpath", "//span[text()='生效']")
			
			# 退出所有iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'生效成功！')]")
			print("款项类型，点击生效成功！")
			time.sleep(3)
			
			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='款项类型']/child::*[1]")
			
			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//li[@f_value='loanSetting']/descendant-or-self::*[5]")
			
			# 打印操作成功日志
			print("款项类型，操作成功!")
			logging.info("款项类型，操作成功!")
			time.sleep(2)
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("款项类型失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		"""
		# 测试基础设置-审批类型
		try:
			# 点击基础设置菜单
			click("xpath", "//li[@f_value='loanSetting']/descendant-or-self::*[5]")
			# 点击审批类型菜单
			click("xpath", "//span[text()='审批类型']")
			# 退出所有iframe窗体
			switch_default()

			for i in range(1, 3):
				# 切入审批类型的iframe窗体
				switch_to("xpath", "//iframe[@id='approvetype-tab-iframe']")
				logging.info("开始测试审批类型功能")

				# 用JS的方法点击新增按钮
				js_click("xpath", "//span[text()='新增']")

				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='addapprovetypeWin-iframe']")
				sleep(1)

				# 输入代码
				input("xpath", "//input[@name='code']", "TestApproveType")
				sleep(1)

				# 输入名称
				input("xpath", "//input[@id='name']", "自动化测试审批类型")
				sleep(1)
				
				# 输入共享模式
				click("xpath", "//input[@id='combobox-input-issharing']")
				input("xpath", "//input[@id='combobox-input-issharing']", "下属组织共享")
				sleep(1)
				input_enter("xpath", "//input[@id='combobox-input-issharing']")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-issharing']")
				sleep(1)
				input_enter("xpath", "//input[@id='combobox-input-issharing']")
				sleep(1)

				# 描述框中填入值
				input("xpath", "//textarea[@id='description']", "自动化测试审批类型描述框")
				sleep(1)

				# 点击保存按钮
				click("xpath", "//span[text()='保存']")

				# 退出所有iframe窗体
				switch_default()

				# 用隐式等待方法等页面出现新增成功的提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				print("审批类型，保存成功！")
				time.sleep(3)

				if i == 1:
					# 删除功能
					# 切入审批类型的iframe窗体
					switch_to("xpath", "//iframe[@id='approvetype-tab-iframe']")

					# 点击查看
					# 用JS的方法点击放大镜
					js_click("xpath", "//span[@class='f-contrac-close']")
					sleep(1)

					# 输入代码：
					input("xpath", "//input[@id='code']", "TestApproveType")
					sleep(1)

					# 点击查询
					click("xpath", "//span[text()='查询']")

					# 勾选
					click("xpath", "//div[@title='代码:TestApproveType']/parent::*/preceding-sibling::*[2]/descendant::*[2]")

					# 点击删除按钮
					click("xpath", "//span[text()='删除']")

					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现删除的提示框
					implici_wait("xpath", "//span[contains(text(),'成功删除1条记录！')]")
					print("审批类型，删除成功！")
					time.sleep(3)

			# 切入‘审批类型’的iframe窗体
			switch_to("xpath", "//iframe[@id='approvetype-tab-iframe']")

			# 点击查看
			# 清空代码框的内容
			clear("xpath", "//input[@id='code']")
			sleep(1)

			# 输入用途代码：
			input("xpath", "//input[@id='code']", "TestApproveType")
			sleep(1)

			# 点击查询
			click("xpath", "//span[text()='查询']")

			# 修改
			# 勾选
			click("xpath", "//div[@title='代码:TestApproveType']/parent::*/preceding-sibling::*[2]/descendant::*[2]")

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
			print("审批类型，修改成功！")
			time.sleep(3)

			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='审批类型']/child::*[1]")

			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//li[@f_value='loanSetting']/descendant-or-self::*[5]")

			# 打印操作成功日志
			print("审批类型，操作成功!")
			logging.info("审批类型，操作成功!")
			time.sleep(2)
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("审批类型打印失败！" + str(traceback.format_exc()))
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
