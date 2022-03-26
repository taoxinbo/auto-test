# encoding=utf-8
# @Time : 2020/8/14 14:49
# @Author : Mindy
# 此文件是测试投资管理模块，包含基础设置，理财投资，投资项目，投资理财，定期存单，现金投资计划，专户理财
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


class Test_Tzgl(unittest.TestCase):
	
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
		# login(G_Mys_Url, Tao, Password, "默认租户")
		# login(G_Mys_Url, mindy, Password, "亚唐科技")
		# login(G_Mys_Url, mindy, Password, "Mindy")
		# login(G_Mys_Url, judy, Password, "默认租户")
		
		logging.info("开始测试投资管理的页面功能")
		# 将页面的滚动条滑动到‘资金结算管理’页面的地方
		js_gd("xpath", "//span[contains(text(),'投资管理')]")
		# 用JS的方法点击资金结算管理菜单按钮
		js_click("xpath", "//span[contains(text(),'投资管理')]")
		
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
			input("xpath", "//input[@name='code']", "L05")
			sleep(1)
			
			# 输入名称
			input("xpath", "//input[@id='name']", "内部定期存款利率方案")
			sleep(1)
			# 单据对象
			click("xpath", "//input[@id='combobox-input-noteobjectid']")
			sleep(1)
			input("xpath", "//input[@id='combobox-input-noteobjectid']", "内部定期存款")
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
		
		# # 测试投资管理--基础设置--内部存款产品
		try:
			# 点击基础设置菜单
			click("xpath", "//li[@f_value='investmentSetting']/descendant-or-self::*[5]")
			# 点击内部存款产品菜单
			click("xpath", "//span[text()='内部存款产品']")
			# 退出所有iframe窗体
			switch_default()

			for i in range(1, 3):
				# 切入担保管理的iframe窗体
				switch_to("xpath", "//iframe[@id='internaldepositproducts-tab-iframe']")
				logging.info("开始测试内部存款产品功能")

				# 用JS的方法点击新增按钮
				js_click("xpath", "//span[text()='新增']")

				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='addWin-iframe']")
				sleep(1)

				# 输入代码
				input("xpath", "//input[@id='code']", "TestDepsPro")
				sleep(1)

				# 输入名称
				input("xpath", "//input[@id='name']", "自动化测试内部存款产品")
				sleep(1)

				# 下拉选择利率方案
				click("xpath", "//input[@id='combobox-input-interestrateschemeid']")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-interestrateschemeid']")
				input_enter("xpath", "//input[@id='combobox-input-interestrateschemeid']")
				sleep(1)

				# 选择币种
				click("xpath", "//input[@id='combobox-input-currencyid']")
				sleep(1)
				input("xpath", "//input[@id='combobox-input-currencyid']", "CNY")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-currencyid']")
				input_enter("xpath", "//input[@id='combobox-input-currencyid']")
				sleep(1)

				# 选择产品性质
				click("xpath", "//input[@id='combobox-input-depositproducttype']")
				sleep(1)
				input("xpath", "//input[@id='combobox-input-depositproducttype']", "定存")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-depositproducttype']")
				input_enter("xpath", "//input[@id='combobox-input-depositproducttype']")
				sleep(1)

				# 描述框中填入值
				input("xpath", "//textarea[@id='description']", "自动化测试内部存款产品备注框")
				sleep(1)

				# 点击保存按钮
				click("xpath", "//span[text()='保存']")

				# 退出所有iframe窗体
				switch_default()

				# 用隐式等待方法等页面出现新增成功的提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				print("内部存款产品，保存成功！")
				time.sleep(3)

				if i == 1:

					# 切入组织担保额度的iframe窗体
					switch_to("xpath", "//iframe[@id='internaldepositproducts-tab-iframe']")
					sleep(1)

					# 点击查看
					# 用JS的方法点击放大镜
					js_click("xpath", "//span[@class='f-contrac-close']")
					sleep(1)

					# 输入代码
					input("xpath", "//input[@id='code']", "TestDepsPro")
					sleep(1)

					# 点击查询
					click("xpath", "//span[text()='查询']")
					sleep(1)

					# 勾选
					click("xpath", "//div[contains(text(),'TestDepsPro')]/parent::*/preceding-sibling::*[3]/descendant::*[2]")
					# 点击保存按钮

					click("xpath", "//span[text()='删除']")
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现删除的提示框
					implici_wait("xpath", "//span[contains(text(),'成功删除1条记录！')]")
					print("组织担保额度，删除成功！")
					time.sleep(3)

			# 修改功能
			# 切入组织担保额度的iframe窗体
			switch_to("xpath", "//iframe[@id='internaldepositproducts-tab-iframe']")

			# 勾选
			click("xpath", "//div[contains(text(),'TestDepsPro')]/parent::*/preceding-sibling::*[3]/descendant::*[2]")

			# 点击修改按钮
			click("xpath", "//span[text()='修改']")
			sleep(1)

			# 切入新增的iframe窗体
			switch_to("xpath", "//iframe[@id='modWin-iframe']")
			sleep(1)

			# 描述框中填入值
			input("xpath", "//textarea[@id='description']", "自动化测试内部存款产品备注修改")
			sleep(1)

			# 点击保存按钮
			click("xpath", "//span[text()='保存']")

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功')]")
			print("内部存款产品，修改成功！")
			time.sleep(3)

			# 失效功能
			# 切入组织担保额度的iframe窗体
			switch_to("xpath", "//iframe[@id='internaldepositproducts-tab-iframe']")

			# 勾选
			click("xpath", "//div[contains(text(),'TestDepsPro')]/parent::*/preceding-sibling::*[3]/descendant::*[2]")

			# 点击修改按钮
			click("xpath", "//span[text()='失效']")
			sleep(1)

			# 点击弹出框的OK键
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'成功失效1条记录！')]")
			print("组织担保额度，失效成功！")
			time.sleep(3)

			# 生效功能
			# 切入组织担保额度的iframe窗体
			switch_to("xpath", "//iframe[@id='internaldepositproducts-tab-iframe']")

			# 勾选
			click("xpath", "//div[contains(text(),'TestDepsPro')]/parent::*/preceding-sibling::*[3]/descendant::*[2]")

			# 点击生按钮
			click("xpath", "//span[text()='生效']")
			sleep(1)

			# 点击弹出框的OK键
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'成功生效1条记录！')]")
			print("内部存款产品，生效成功！")
			time.sleep(3)

			switch_default()

			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='内部存款产品']/child::*[1]")

			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//li[@f_value='investmentSetting']/descendant-or-self::*[5]")

			# 打印操作成功日志
			print("内部存款产品，操作成功!")
			logging.info("内部存款产品，操作成功!")
			time.sleep(2)

		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("内部存款产品操作失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)

		# # 测试投资管理--基础设置--理财产品类别
		try:
			# 点击基础设置菜单
			click("xpath", "//li[@f_value='investmentSetting']/descendant-or-self::*[5]")
			# 点击内部存款产品菜单
			click("xpath", "//span[text()='理财产品类别']")
			# 退出所有iframe窗体
			switch_default()

			for i in range(1, 3):
				# 切入担保管理的iframe窗体
				switch_to("xpath", "//iframe[@id='bankfinancialType-tab-iframe']")
				logging.info("开始测试理财产品类别功能")

				# 用JS的方法点击新增按钮
				js_click("xpath", "//span[text()='新增']")

				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='addcollateralcategoryWin-iframe']")
				sleep(1)

				# 输入代码
				input("xpath", "//input[@id='code']", "TestColGory")
				sleep(1)

				# 输入名称
				input("xpath", "//input[@id='name']", "自动化测试理财产品类别")
				sleep(1)


				# 描述框中填入值
				input("xpath", "//textarea[@id='description']", "自动化测试理财产品类别备注框")
				sleep(1)

				# 点击保存按钮
				click("xpath", "//span[text()='保存']")

				# 退出所有iframe窗体
				switch_default()

				# 用隐式等待方法等页面出现新增成功的提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				print("理财产品类别，保存成功！")
				time.sleep(3)

				if i == 1:

					# 切入组织担保额度的iframe窗体
					switch_to("xpath", "//iframe[@id='bankfinancialType-tab-iframe']")
					sleep(1)

					# 点击查看
					# 用JS的方法点击放大镜
					js_click("xpath", "//span[@class='f-contrac-close']")
					sleep(1)

					# 输入代码
					input("xpath", "//input[@id='code']", "TestColGory")
					sleep(1)

					# 点击查询
					click("xpath", "//span[text()='查询']")
					sleep(1)

					# 勾选
					# click("xpath", "//div[contains(text(),'TestColGory')]/parent::*/preceding-sibling::*[3]/descendant::*[2]")
					# # 点击保存按钮
					click("xpath",
					      "//div[contains(text(),'TestColGory')]/parent::*/preceding-sibling::*[2]/descendant::*[2]")
					# 点击保存按钮

					click("xpath", "//span[text()='删除']")
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现删除的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("理财产品类别，删除成功！")
					time.sleep(3)

			# 修改功能
			# 切入理财产品类别的iframe窗体
			switch_to("xpath", "//iframe[@id='bankfinancialType-tab-iframe']")

			# 勾选
			# click("xpath", "//div[contains(text(),'TestColGory')]/parent::*/preceding-sibling::*[3]/descendant::*[2]")
			click("xpath",
			      "//div[contains(text(),'TestColGory')]/parent::*/preceding-sibling::*[2]/descendant::*[2]")

			# 点击修改按钮
			click("xpath", "//span[text()='修改']")
			sleep(1)

			# 切入新增的iframe窗体
			switch_to("xpath", "//iframe[@id='modWin-iframe']")
			sleep(1)

			# 描述框中填入值
			input("xpath", "//textarea[@id='description']", "自动化测试理财产品类别备注修改")
			sleep(1)

			# 点击保存按钮
			click("xpath", "//span[text()='保存']")

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功')]")
			print("理财产品类别，修改成功！")
			time.sleep(3)

			# 失效功能
			# 切入组织担保额度的iframe窗体
			switch_to("xpath", "//iframe[@id='bankfinancialType-tab-iframe']")

			# 勾选
			click("xpath",
			      "//div[contains(text(),'TestColGory')]/parent::*/preceding-sibling::*[2]/descendant::*[2]")
			# 点击修改按钮
			click("xpath", "//span[text()='失效']")
			sleep(1)

			# # 点击弹出框的OK键
			# click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'代码为TestColGory的失效成功！')]")
			print("理财产品类别，失效成功！")
			time.sleep(3)

			# 生效功能
			# 切入组织担保额度的iframe窗体
			switch_to("xpath", "//iframe[@id='bankfinancialType-tab-iframe']")

			# 勾选
			click("xpath",
			      "//div[contains(text(),'TestColGory')]/parent::*/preceding-sibling::*[2]/descendant::*[2]")
			# 点击生按钮
			click("xpath", "//span[text()='生效']")
			sleep(1)

			# # 点击弹出框的OK键
			# click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'代码为TestColGory的生效成功！')]")
			print("理财产品类别，生效成功！")
			time.sleep(3)

			switch_default()

			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='理财产品类别']/child::*[1]")

			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//li[@f_value='investmentSetting']/descendant-or-self::*[5]")

			# 打印操作成功日志
			print("理财产品类别，操作成功!")
			logging.info("理财产品类别，操作成功!")
			time.sleep(2)

		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("理财产品类别操作失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
	
		# # 测试投资管理--基础设置--年度理财额度
		try:
			# 点击基础设置菜单
			click("xpath", "//li[@f_value='investmentSetting']/descendant-or-self::*[5]")
			# 点击内部存款产品菜单
			click("xpath", "//span[text()='年度理财额度']")
			# 退出所有iframe窗体
			switch_default()

			for i in range(1, 3):
				# 切入年度理财额度的iframe窗体
				switch_to("xpath", "//iframe[@id='bankFinProdQuotas-tab-iframe']")
				logging.info("开始测试年度理财额度功能")

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
				input_enter("xpath", "//input[@id='combobox-input-orgid']")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-orgid']")
				sleep(1)
				input_enter("xpath", "//input[@id='combobox-input-orgid']")
				sleep(1)
				# 选择投资年份
				click("xpath", "//input[@id='loanyear-input']")
				sleep(1)
				input("xpath", "//input[@id='loanyear-input']", "2018")
				sleep(1)

				# 选择币种
				click("xpath", "//input[@id='combobox-input-currencyid']")
				sleep(1)
				input("xpath", "//input[@id='combobox-input-currencyid']", "CNY")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-currencyid']")
				input_enter("xpath", "//input[@id='combobox-input-currencyid']")
				sleep(1)

				# 输入投资额度
				click("xpath", "//input[@id='loanamount-input']")
				sleep(1)
				clear("xpath", "//input[@id='loanamount-input']")
				sleep(1)
				input("xpath", "//input[@id='loanamount-input']", "100000000")
				sleep(1)

				# 选择理财产品类别
				click("xpath", "//input[@id='combobox-input-investcategoryid']")
				sleep(1)
				input("xpath", "//input[@id='combobox-input-investcategoryid']", "自动化测试理财产品")
				sleep(1)
				click("xpath", "//div[@title='代码-名称:TestColGory-自动化测试理财产品类别']")
				sleep(1)

				# 描述框中填入值
				input("xpath", "//textarea[@id='description']", "自动化测试年度理财额度备注框")
				sleep(1)

				# 点击保存按钮
				click("xpath", "//span[text()='保存']")

				# 退出所有iframe窗体
				switch_default()

				# 用隐式等待方法等页面出现新增成功的提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				print("年度理财额度，保存成功！")
				time.sleep(3)

				if i == 1:
					# 切入年度理财额度的iframe窗体
					switch_to("xpath", "//iframe[@id='bankFinProdQuotas-tab-iframe']")
					sleep(1)

					# 点击查看
					# 用JS的方法点击放大镜
					js_click("xpath", "//span[@class='f-contrac-close']")
					sleep(1)

					# 输入投资年份
					input("xpath", "//input[@id='loanyear-input']", "2018")
					sleep(1)

					# 点击查询
					click("xpath", "//span[text()='查询']")
					sleep(1)

					# 勾选
					click("xpath", "//div[contains(text(),'2018')]/parent::*/preceding-sibling::*[2]/descendant::*[2]")
					# 点击保存按钮

					click("xpath", "//span[text()='删除']")
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现删除的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("年度理财额度，删除成功！")
					time.sleep(3)

			# 修改功能
			# 切入组织担保额度的iframe窗体
			switch_to("xpath", "//iframe[@id='bankFinProdQuotas-tab-iframe']")

			# 勾选
			click("xpath", "//div[contains(text(),'2018')]/parent::*/preceding-sibling::*[2]/descendant::*[2]")

			# 点击修改按钮
			click("xpath", "//span[text()='修改']")
			sleep(1)

			# 切入新增的iframe窗体
			switch_to("xpath", "//iframe[@id='modWin-iframe']")
			sleep(1)

			# 描述框中填入值
			input("xpath", "//textarea[@id='description']", "自动化测试年度理财额度备注修改")
			sleep(1)

			# 点击保存按钮
			click("xpath", "//span[text()='保存']")

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功')]")
			print("年度理财额度，修改成功！")
			time.sleep(3)

			switch_default()

			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='年度理财额度']/child::*[1]")

			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//li[@f_value='investmentSetting']/descendant-or-self::*[5]")

			# 打印操作成功日志
			print("年度理财额度，操作成功!")
			logging.info("年度理财额度，操作成功!")
			time.sleep(2)

		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("年度理财额度操作失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)

		# # 测试投资管理--基础设置--风险评估级别
		try:
			# 点击基础设置菜单
			click("xpath", "//li[@f_value='investmentSetting']/descendant-or-self::*[5]")
			# 点击内部存款产品菜单
			click("xpath", "//span[text()='风险评估级别']")
			# 退出所有iframe窗体
			switch_default()

			for i in range(1, 3):
				# 切入风险评估级别的iframe窗体
				switch_to("xpath", "//iframe[@id='riskasmtcategory-tab-iframe']")
				logging.info("开始测试风险评估级别功能")

				# 用JS的方法点击新增按钮
				js_click("xpath", "//span[text()='新增']")

				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='addWin-iframe']")
				sleep(1)

				# 输入代码
				input("xpath", "//input[@id='code']", "TestRisCat")
				sleep(1)

				# 输入名称
				input("xpath", "//input[@id='name']", "自动化测试风险评估级别")
				sleep(1)

				# 描述框中填入值
				input("xpath", "//textarea[@id='description']", "自动化测试风险评估级别备注框")
				sleep(1)

				# 点击保存按钮
				click("xpath", "//span[text()='保存']")

				# 退出所有iframe窗体
				switch_default()

				# 用隐式等待方法等页面出现新增成功的提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				print("风险评估级别，保存成功！")
				time.sleep(3)

				if i == 1:
					# 切入组织担保额度的iframe窗体
					switch_to("xpath", "//iframe[@id='riskasmtcategory-tab-iframe']")
					sleep(1)

					# 点击查看
					# 用JS的方法点击放大镜
					js_click("xpath", "//span[@class='f-contrac-close']")
					sleep(1)

					# 输入代码
					input("xpath", "//input[@id='code']", "TestRisCat")
					sleep(1)

					# 点击查询
					click("xpath", "//span[text()='查询']")
					sleep(1)

					# 勾选
					click("xpath", "//div[contains(text(),'TestRisCat')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")
					# 点击保存按钮

					click("xpath", "//span[text()='删除']")
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现删除的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("风险评估级别，删除成功！")
					time.sleep(3)

			# 修改功能
			# 切入理财产品类别的iframe窗体
			switch_to("xpath", "//iframe[@id='riskasmtcategory-tab-iframe']")

			# 勾选
			click("xpath", "//div[contains(text(),'TestRisCat')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

			# 点击修改按钮
			click("xpath", "//span[text()='修改']")
			sleep(1)

			# 切入新增的iframe窗体
			switch_to("xpath", "//iframe[@id='modWin-iframe']")
			sleep(1)

			# 描述框中填入值
			input("xpath", "//textarea[@id='description']", "自动化测试风险评估级别备注修改")
			sleep(1)

			# 点击保存按钮
			click("xpath", "//span[text()='保存']")

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功')]")
			print("风险评估级别，修改成功！")
			time.sleep(3)

			# 失效功能
			# 切入风险评估级别的iframe窗体
			switch_to("xpath", "//iframe[@id='riskasmtcategory-tab-iframe']")

			# 勾选
			click("xpath", "//div[contains(text(),'TestRisCat')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

			# 点击修改按钮
			click("xpath", "//span[text()='失效']")
			sleep(1)

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'失效成功！')]")
			print("风险评估级别，失效成功！")
			time.sleep(3)

			# 生效功能
			# 切入风险评估级别的iframe窗体
			switch_to("xpath", "//iframe[@id='riskasmtcategory-tab-iframe']")

			# 勾选
			click("xpath", "//div[contains(text(),'TestRisCat')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

			# 点击生按钮
			click("xpath", "//span[text()='生效']")
			sleep(1)

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'生效成功！')]")
			print("风险评估级别，生效成功！")
			time.sleep(3)

			switch_default()

			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='风险评估级别']/child::*[1]")

			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//li[@f_value='investmentSetting']/descendant-or-self::*[5]")

			# 打印操作成功日志
			print("风险评估级别，操作成功!")
			logging.info("风险评估级别，操作成功!")
			time.sleep(2)

		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("风险评估级别操作失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)

		# # 测试投资管理--基础设置--投资类别
		try:
			# 点击基础设置菜单
			click("xpath", "//li[@f_value='investmentSetting']/descendant-or-self::*[5]")
			# 点击投资类别菜单
			click("xpath", "//span[text()='投资类别']")
			# 退出所有iframe窗体
			switch_default()

			for i in range(1, 3):
				# 切入投资类别的iframe窗体
				switch_to("xpath", "//iframe[@id='investcategory-tab-iframe']")
				logging.info("开始测试投资类别功能")

				# 用JS的方法点击新增按钮
				js_click("xpath", "//span[text()='新增']")

				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='addWin-iframe']")
				sleep(1)

				# 输入代码
				input("xpath", "//input[@id='code']", "TestInvCat")
				sleep(1)

				# 输入名称
				input("xpath", "//input[@id='name']", "自动化测试投资类别")
				sleep(1)

				# 选择交易方向
				click("xpath", "//input[@id='combobox-input-moneyway']")
				sleep(1)
				input("xpath", "//input[@id='combobox-input-moneyway']", "支出")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-moneyway']")
				input_enter("xpath", "//input[@id='combobox-input-moneyway']")
				sleep(1)

				# 选择组织
				click("xpath", "//input[@id='combobox-input-orgid']")
				sleep(1)
				input("xpath", "//input[@id='combobox-input-orgid']", "亚唐科技")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-orgid']")
				input_enter("xpath", "//input[@id='combobox-input-orgid']")
				sleep(1)

				# 描述框中填入值
				input("xpath", "//textarea[@id='description']", "自动化测试投资类别描述框")
				sleep(1)

				# 点击保存按钮
				click("xpath", "//span[text()='保存']")

				# 退出所有iframe窗体
				switch_default()

				# 用隐式等待方法等页面出现新增成功的提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				print("投资类别，保存成功！")
				time.sleep(3)

				if i == 1:
					# 切入投资类别的iframe窗体
					switch_to("xpath", "//iframe[@id='investcategory-tab-iframe']")
					sleep(1)

					# 点击查看
					# 用JS的方法点击放大镜
					js_click("xpath", "//span[@class='f-contrac-close']")
					sleep(1)

					# 输入代码
					input("xpath", "//input[@id='codelrlike']", "TestInvCat")
					sleep(1)

					# 点击查询
					click("xpath", "//span[text()='查询']")
					sleep(1)

					# 勾选
					click("xpath", "//span[contains(text(),'TestInvCat')]/ancestor::*[8]/descendant::*[1]/descendant::*[19]")
					# 点击保存按钮

					click("xpath", "//span[text()='删除']")
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现删除的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("投资类别，删除成功！")
					time.sleep(3)

			# 修改功能
			# 切入投资类别的iframe窗体
			switch_to("xpath", "//iframe[@id='investcategory-tab-iframe']")

			# 勾选
			click("xpath",
			      "//span[contains(text(),'TestInvCat')]/ancestor::*[8]/descendant::*[1]/descendant::*[19]")

			# 点击修改按钮
			click("xpath", "//span[text()='修改']")
			sleep(1)

			# 切入新增的iframe窗体
			switch_to("xpath", "//iframe[@id='modWin-iframe']")
			sleep(1)

			# 描述框中填入值
			input("xpath", "//textarea[@id='description']", "自动化测试投资类别备注修改")
			sleep(1)

			# 点击保存按钮
			click("xpath", "//span[text()='保存']")

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功')]")
			print("投资类别，修改成功！")
			time.sleep(3)

			# 失效功能
			# 切入投资类别的iframe窗体
			switch_to("xpath", "//iframe[@id='investcategory-tab-iframe']")

			# 勾选
			click("xpath",
			      "//span[contains(text(),'TestInvCat')]/ancestor::*[8]/descendant::*[1]/descendant::*[19]")

			# 点击修改按钮
			click("xpath", "//span[text()='失效']")
			sleep(1)

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("投资类别，失效成功！")
			time.sleep(3)

			# 生效功能
			# 切入投资类别的iframe窗体
			switch_to("xpath", "//iframe[@id='investcategory-tab-iframe']")

			# 勾选
			click("xpath",
			      "//span[contains(text(),'TestInvCat')]/ancestor::*[8]/descendant::*[1]/descendant::*[19]")

			# 点击生按钮
			click("xpath", "//span[text()='生效']")
			sleep(1)

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("投资类别，生效成功！")
			time.sleep(3)

			# 添加下级类别功能
			# 切入投资类别的iframe窗体
			switch_to("xpath", "//iframe[@id='investcategory-tab-iframe']")

			# 勾选
			click("xpath", "//span[contains(text(),'TestInvCat')]/ancestor::*[8]/descendant::*[1]/descendant::*[19]")

			# 点击生按钮
			click("xpath", "//span[text()='添加下级类别']")
			sleep(1)

			switch_to("xpath", "//iframe[@id='addWin-iframe']")
			sleep(1)

			# 输入代码
			input("xpath", "//input[@id='code']", "TestInvCat01")
			sleep(1)

			# 输入名称
			input("xpath", "//input[@id='name']", "自动化测试投资类别")
			sleep(1)

			# 选择组织
			click("xpath", "//input[@id='combobox-input-orgid']")
			sleep(1)
			input("xpath", "//input[@id='combobox-input-orgid']", "亚唐科技")
			sleep(1)
			input_down("xpath", "//input[@id='combobox-input-orgid']")
			input_enter("xpath", "//input[@id='combobox-input-orgid']")
			sleep(1)

			# 描述框中填入值
			input("xpath", "//textarea[@id='description']", "自动化测试投资类别描述框")
			sleep(1)

			# 点击保存按钮
			click("xpath", "//span[text()='保存']")

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("投资类别，添加下级类别成功！")
			time.sleep(3)

			# 添加同级级类别功能
			# 切入投资类别的iframe窗体
			switch_to("xpath", "//iframe[@id='investcategory-tab-iframe']")
			sleep(1)

			# 勾选
			click("xpath", "//span[contains(text(),'TestInvCat')]/ancestor::*[8]/descendant::*[1]/descendant::*[19]")

			# 点击生按钮
			click("xpath", "//span[text()='添加同级类别']")
			sleep(1)

			switch_to("xpath", "//iframe[@id='addWin-iframe']")
			sleep(1)

			# 输入代码
			input("xpath", "//input[@id='code']", "TestInvCat02")
			sleep(1)

			# 输入名称
			input("xpath", "//input[@id='name']", "自动化测试投资类别")
			sleep(1)

			# 选择交易方向
			click("xpath", "//input[@id='combobox-input-moneyway']")
			sleep(1)
			input("xpath", "//input[@id='combobox-input-moneyway']", "收入")
			sleep(1)
			input_down("xpath", "//input[@id='combobox-input-moneyway']")
			input_enter("xpath", "//input[@id='combobox-input-moneyway']")
			sleep(1)

			# 选择组织
			click("xpath", "//input[@id='combobox-input-orgid']")
			sleep(1)
			input("xpath", "//input[@id='combobox-input-orgid']", "亚唐科技")
			sleep(1)
			input_down("xpath", "//input[@id='combobox-input-orgid']")
			input_enter("xpath", "//input[@id='combobox-input-orgid']")
			sleep(1)

			# 描述框中填入值
			input("xpath", "//textarea[@id='description']", "自动化测试投资类别描述框")
			sleep(1)

			# 点击保存按钮
			click("xpath", "//span[text()='保存']")

			switch_default()

			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("投资类别，添加同级类别成功！")
			time.sleep(3)

			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='投资类别']/child::*[1]")

			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//li[@f_value='investmentSetting']/descendant-or-self::*[5]")

			# 打印操作成功日志
			print("投资类别，操作成功!")
			logging.info("投资类别，操作成功!")
			time.sleep(2)

		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("投资类别操作失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		
		# # 测试投资管理--基础设置--期限结构
		try:
			# 点击基础设置菜单
			click("xpath", "//li[@f_value='investmentSetting']/descendant-or-self::*[5]")
			# 点击内部存款产品菜单
			click("xpath", "//span[text()='期限结构']")
			# 退出所有iframe窗体
			switch_default()

			for i in range(1, 3):
				# 切入风险评估级别的iframe窗体
				switch_to("xpath", "//iframe[@id='investtermstructures-tab-iframe']")
				logging.info("开始测试期限结构功能")

				# 用JS的方法点击新增按钮
				js_click("xpath", "//span[text()='新增']")

				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='addWin-iframe']")
				sleep(1)

				# 输入代码
				input("xpath", "//input[@id='code']", "TestTermStr")
				sleep(1)

				# 输入名称
				input("xpath", "//input[@id='name']", "自动化测试期限结构")
				sleep(1)

				# 产品期限开始
				input("xpath", "//input[@id='begindate-input']", "1")
				sleep(1)

				# 产品期限结束
				input("xpath", "//input[@id='enddate-input']", "1")
				sleep(1)

				# 描述框中填入值
				input("xpath", "//textarea[@id='description']", "自动化测试期限结构备注框")
				sleep(1)

				# 点击保存按钮
				click("xpath", "//span[text()='保存']")

				# 退出所有iframe窗体
				switch_default()

				# 用隐式等待方法等页面出现新增成功的提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				print("期限结构，保存成功！")
				time.sleep(3)

				if i == 1:
					# 切入期限结构的iframe窗体
					switch_to("xpath", "//iframe[@id='investtermstructures-tab-iframe']")
					sleep(1)

					# 点击查看
					# 用JS的方法点击放大镜
					js_click("xpath", "//span[@class='f-contrac-close']")
					sleep(1)

					# 输入代码
					input("xpath", "//input[@id='code']", "TestTermStr")
					sleep(1)

					# 点击查询
					click("xpath", "//span[text()='查询']")
					sleep(1)

					# 勾选
					click("xpath", "//div[contains(text(),'TestTermStr')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")
					# 点击保存按钮

					click("xpath", "//span[text()='删除']")
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现删除的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("期限结构，删除成功！")
					time.sleep(3)

			# 修改功能
			# 切入期限结构的iframe窗体
			switch_to("xpath", "//iframe[@id='investtermstructures-tab-iframe']")

			# 勾选
			click("xpath", "//div[contains(text(),'TestTermStr')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

			# 点击修改按钮
			click("xpath", "//span[text()='修改']")
			sleep(1)

			# 切入新增的iframe窗体
			switch_to("xpath", "//iframe[@id='modWin-iframe']")
			sleep(1)
			
			# 输入代码
			clear("xpath", "//input[@id='code']")
			sleep(1)
			input("xpath", "//input[@id='code']", "1")
			sleep(1)

			# 输入名称
			clear("xpath", "//input[@id='name']")
			sleep(1)
			input("xpath", "//input[@id='name']", "1")
			sleep(1)
			
			# 输入代码
			clear("xpath", "//input[@id='begindate-input']")
			sleep(1)
			
			# 输入名称
			clear("xpath", "//input[@id='enddate-input']")
			sleep(1)
			
			# 描述框中填入值
			input("xpath", "//textarea[@id='description']", "自动化测试期限结构描述修改")
			sleep(1)

			# 点击保存按钮
			click("xpath", "//span[text()='保存']")

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功')]")
			print("期限结构，修改成功！")
			time.sleep(3)

			# 失效功能
			# 切入期限结构的iframe窗体
			switch_to("xpath", "//iframe[@id='investtermstructures-tab-iframe']")
			
			# 输入代码
			clear("xpath", "//input[@id='code']")
			sleep(1)
			input("xpath", "//input[@id='code']", "1")
			sleep(1)
			
			# 点击查询
			click("xpath", "//span[text()='查询']")
			sleep(1)

			# 勾选
			click("xpath", "//div[contains(text(),'1')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

			# 点击修改按钮
			click("xpath", "//span[text()='失效']")
			sleep(1)

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'失效1条')]")
			print("期限结构，失效成功！")
			time.sleep(3)

			# 生效功能
			# 切入期限结构的iframe窗体
			switch_to("xpath", "//iframe[@id='investtermstructures-tab-iframe']")

			# 勾选
			click("xpath", "//div[contains(text(),'1')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

			# 点击生按钮
			click("xpath", "//span[text()='生效']")
			sleep(1)

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'生效1条')]")
			print("期限结构，生效成功！")
			time.sleep(3)

			switch_default()

			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='期限结构']/child::*[1]")

			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//li[@f_value='investmentSetting']/descendant-or-self::*[5]")

			# 打印操作成功日志
			print("期限结构，操作成功!")
			logging.info("期限结构，操作成功!")
			time.sleep(2)

		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("期限结构操作失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		
		# 测试投资管理--基础设置--投资品种
		try:
			# 点击基础设置菜单
			click("xpath", "//li[@f_value='investmentSetting']/descendant-or-self::*[5]")
			# 点击投资产品菜单
			click("xpath", "//span[text()='投资品种']")
			# 退出所有iframe窗体
			switch_default()

			for i in range(1, 3):
				# 切入投资产品的iframe窗体
				switch_to("xpath", "//iframe[@id='investvarietys-tab-iframe']")
				logging.info("开始测试投资品种功能")

				# 用JS的方法点击新增按钮
				js_click("xpath", "//span[text()='新增']")

				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='addWin-iframe']")
				sleep(1)

				# 输入代码
				input("xpath", "//input[@id='code']", "TestInvVar")
				sleep(1)

				# 输入名称
				input("xpath", "//input[@id='name']", "自动化测试投资品种")
				sleep(1)

				# 分类
				click("xpath", "//input[@id='combobox-input-category']")
				sleep(1)
				input("xpath", "//input[@id='combobox-input-category']", "随时可用")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-category']")
				input_enter("xpath", "//input[@id='combobox-input-category']")
				sleep(1)

				# 默认期限结构
				click("xpath", "//input[@id='combobox-input-defaultterm']")
				sleep(1)
				input_enter("xpath", "//input[@id='combobox-input-defaultterm']")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-defaultterm']")
				sleep(1)
				input_enter("xpath", "//input[@id='combobox-input-defaultterm']")
				sleep(1)

				# 理财性质
				click("xpath", "//input[@id='combobox-input-financytype']")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-financytype']")
				input_enter("xpath", "//input[@id='combobox-input-financytype']")
				sleep(1)

				# 描述框中填入值
				input("xpath", "//textarea[@id='description']", "自动化测试投资品种备注框")
				sleep(1)

				# 缺少附件上传

				# 点击保存按钮
				click("xpath", "//span[text()='保存']")

				# 退出所有iframe窗体
				switch_default()

				# 用隐式等待方法等页面出现新增成功的提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				print("投资品种，保存成功！")
				time.sleep(3)

				if i == 1:
					# 切入投资品种的iframe窗体
					switch_to("xpath", "//iframe[@id='investvarietys-tab-iframe']")
					sleep(1)

					# 点击查看
					# 用JS的方法点击放大镜
					js_click("xpath", "//span[@class='f-contrac-close']")
					sleep(1)

					# 输入代码
					input("xpath", "//input[@id='code']", "TestInvVar")
					sleep(1)

					# 点击查询
					click("xpath", "//span[text()='查询']")
					sleep(1)

					# 勾选
					click("xpath",  "//div[contains(text(),'TestInvVar')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")
					# 点击保存按钮

					click("xpath", "//span[text()='删除']")
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现删除的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("投资品种，删除成功！")
					time.sleep(3)

			# 修改功能
			# 切入投资品种的iframe窗体
			switch_to("xpath", "//iframe[@id='investvarietys-tab-iframe']")

			# 勾选
			click("xpath", "//div[contains(text(),'TestInvVar')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

			# 点击修改按钮
			click("xpath", "//span[text()='修改']")
			sleep(1)

			# 切入新增的iframe窗体
			switch_to("xpath", "//iframe[@id='modWin-iframe']")
			sleep(1)

			# 描述框中填入值
			input("xpath", "//textarea[@id='description']", "自动化测试投资品种描述修改")
			sleep(1)

			# 点击保存按钮
			click("xpath", "//span[text()='保存']")

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功')]")
			print("投资品种，修改成功！")
			time.sleep(3)

			# 失效功能
			# 切入投资产品的iframe窗体
			switch_to("xpath", "//iframe[@id='investvarietys-tab-iframe']")

			# 勾选
			click("xpath", "//div[contains(text(),'TestInvVar')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

			# 点击修改按钮
			click("xpath", "//span[text()='失效']")
			sleep(1)

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'失效1条')]")
			print("投资品种，失效成功！")
			time.sleep(3)

			# 生效功能
			# 切入投资品种的iframe窗体
			switch_to("xpath", "//iframe[@id='investvarietys-tab-iframe']")

			# 勾选
			click("xpath", "//div[contains(text(),'TestInvVar')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

			# 点击生按钮
			click("xpath", "//span[text()='生效']")
			sleep(1)

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'生效1条')]")
			print("投资品种，生效成功！")
			time.sleep(3)

			switch_default()

			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='投资品种']/child::*[1]")

			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//li[@f_value='investmentSetting']/descendant-or-self::*[5]")

			# 打印操作成功日志
			print("投资品种，操作成功!")
			logging.info("投资品种，操作成功!")
			time.sleep(2)

		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("投资品种操作失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)

		# 测试投资管理--基础设置--投资产品
		try:
			# 点击基础设置菜单
			click("xpath", "//li[@f_value='investmentSetting']/descendant-or-self::*[5]")
			# 点击投资产品菜单
			click("xpath", "//span[text()='投资产品']")
			# 退出所有iframe窗体
			switch_default()

			for i in range(1, 3):
				# 切入投资产品的iframe窗体
				switch_to("xpath", "//iframe[@id='investproducts-tab-iframe']")
				logging.info("开始测试投资产品功能")

				# 用JS的方法点击新增按钮
				js_click("xpath", "//span[text()='新增']")

				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='addWin-iframe']")
				sleep(1)

				# 输入代码
				input("xpath", "//input[@id='code']", "TestInvPro")
				sleep(1)

				# 输入名称
				input("xpath", "//input[@id='name']", "自动化测试投资产品")
				sleep(1)

				# 理财网查询结果
				click("xpath", "//input[@id='combobox-input-isfromfinancial']")
				sleep(1)
				input("xpath", "//input[@id='combobox-input-isfromfinancial']", "TRUE")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-isfromfinancial']")
				input_enter("xpath", "//input[@id='combobox-input-isfromfinancial']")
				sleep(1)

				# 投资品种
				click("xpath", "//input[@id='combobox-input-investvarietys']")
				sleep(1)
				# input("xpath", "//input[@id='combobox-input-isfromfinancial']", "TRUE")
				# sleep(1)
				input_down("xpath", "//input[@id='combobox-input-investvarietys']")
				input_enter("xpath", "//input[@id='combobox-input-investvarietys']")
				sleep(1)

				# 理财产品类别
				click("xpath", "//input[@id='combobox-input-investcategoryid']")
				sleep(1)
				input("xpath", "//input[@id='combobox-input-investcategoryid']", "自动化测试理财产品类别")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-investcategoryid']")
				input_enter("xpath", "//input[@id='combobox-input-investcategoryid']")
				sleep(1)

				# 描述框中填入值
				input("xpath", "//textarea[@id='description']", "自动化测试投资产品备注框")
				sleep(1)

				# 缺少附件上传

				# 点击保存按钮
				click("xpath", "//span[text()='保存']")

				# 退出所有iframe窗体
				switch_default()

				# 用隐式等待方法等页面出现新增成功的提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				print("投资产品，保存成功！")
				time.sleep(3)

				if i == 1:
					# 切入投资产品的iframe窗体
					switch_to("xpath", "//iframe[@id='investproducts-tab-iframe']")
					sleep(1)

					# 点击查看
					# 用JS的方法点击放大镜
					js_click("xpath", "//span[@class='f-contrac-close']")
					sleep(1)

					# 输入代码
					input("xpath", "//input[@id='code']", "TestInvPro")
					sleep(1)

					# 点击查询
					click("xpath", "//span[text()='查询']")
					sleep(1)

					# 勾选
					click("xpath",
					      "//div[contains(text(),'TestInvPro')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")
					# 点击保存按钮

					click("xpath", "//span[text()='删除']")
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现删除的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("投资产品，删除成功！")
					time.sleep(3)

			# 修改功能
			# 切入投资产品的iframe窗体
			switch_to("xpath", "//iframe[@id='investproducts-tab-iframe']")

			# 勾选
			click("xpath",
			      "//div[contains(text(),'TestInvPro')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

			# 点击修改按钮
			click("xpath", "//span[text()='修改']")
			sleep(1)

			# 切入新增的iframe窗体
			switch_to("xpath", "//iframe[@id='modWin-iframe']")
			sleep(1)

			# 描述框中填入值
			input("xpath", "//textarea[@id='description']", "自动化测试投资产品描述修改")
			sleep(1)

			# 点击保存按钮
			click("xpath", "//span[text()='保存']")

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功')]")
			print("投资产品，修改成功！")
			time.sleep(3)

			# 失效功能
			# 切入投资产品的iframe窗体
			switch_to("xpath", "//iframe[@id='investproducts-tab-iframe']")

			# 勾选
			click("xpath", "//div[contains(text(),'TestInvPro')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

			# 点击修改按钮
			click("xpath", "//span[text()='失效']")
			sleep(1)

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'失效1条')]")
			print("投资产品，失效成功！")
			time.sleep(3)

			# 生效功能
			# 切入投资产品的iframe窗体
			switch_to("xpath", "//iframe[@id='investproducts-tab-iframe']")

			# 勾选
			click("xpath", "//div[contains(text(),'TestInvPro')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

			# 点击生按钮
			click("xpath", "//span[text()='生效']")
			sleep(1)

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'生效1条')]")
			print("投资产品，生效成功！")
			time.sleep(3)

			switch_default()

			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='投资产品']/child::*[1]")

			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//li[@f_value='investmentSetting']/descendant-or-self::*[5]")

			# 打印操作成功日志
			print("投资产品，操作成功!")
			logging.info("投资产品，操作成功!")
			time.sleep(2)

		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("投资产品操作失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		
		# 添加理财合同利率方案
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
			input("xpath", "//input[@name='code']", "L06")
			sleep(1)
			
			# 输入名称
			input("xpath", "//input[@id='name']", "理财投资")
			sleep(1)
			# 单据对象
			click("xpath", "//input[@id='combobox-input-noteobjectid']")
			sleep(1)
			input("xpath", "//input[@id='combobox-input-noteobjectid']", "LCTZ-理财投资")
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
		
		# 测试理财投资-理财合同
		try:
			# 点击理财投资菜单
			click("xpath", "//span[@title='理财投资']")
			# 点击理财合同登记菜单
			click("xpath", "//span[@title='理财合同']")
			# 退出所有的iframe窗体
			switch_default()

			logging.info("开始测试理财合同功能")
			for i in range(1, 4):
				# 切入‘理财合同’的iframe窗体
				switch_to("xpath", "//iframe[@id='productsManage-tab-iframe']")

				# 用JS的方法点击新增按钮
				js_click("xpath", "//span[text()='新增']")

				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='addWin-iframe']")
				sleep(1)

				# 合同号
				temp1 = time.strftime("%H%M%S")
				# 合同号查询
				input("xpath", "//input[@id='contractcode']", "ZDHLCHTH" + str(temp1))
				sleep(1)

				# 理财产品类别
				click("xpath", "//input[@id='combobox-input-investcategoryid']")
				sleep(1)
				input("xpath", "//input[@id='combobox-input-investcategoryid']", "自动化测试理财产品类别")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-investcategoryid']")
				input_enter("xpath", "//input[@id='combobox-input-investcategoryid']")
				sleep(1)

				# 投资品种
				click("xpath", "//input[@id='combobox-input-investvarietys']")
				sleep(1)
				input_enter("xpath", "//input[@id='combobox-input-investvarietys']")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-investvarietys']")
				sleep(1)
				input_enter("xpath", "//input[@id='combobox-input-investvarietys']")
				sleep(1)

				# 投资产品
				click("xpath", "//input[@id='combobox-input-investproductid']")
				sleep(1)
				input("xpath", "//input[@id='combobox-input-investproductid']", "自动化测试投资产品")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-investproductid']")
				input_enter("xpath", "//input[@id='combobox-input-investproductid']")
				sleep(1)

				# 风险评估级别
				click("xpath", "//input[@id='combobox-input-riskasmtcategoryid']")
				sleep(1)
				input("xpath", "//input[@id='combobox-input-riskasmtcategoryid']", "自动化测试风险评估级别")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-riskasmtcategoryid']")
				input_enter("xpath", "//input[@id='combobox-input-riskasmtcategoryid']")
				sleep(1)

				# 投资机构类型
				click("xpath", "//input[@id='combobox-input-financialinstitutiontype']")
				sleep(1)
				input("xpath", "//input[@id='combobox-input-financialinstitutiontype']", "银行")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-financialinstitutiontype']")
				input_enter("xpath", "//input[@id='combobox-input-financialinstitutiontype']")
				sleep(1)

				# 输入投资机构
				click("xpath", "//input[@id='combobox-input-bankid']")
				sleep(1)
				input("xpath", "//input[@id='combobox-input-bankid']", "中国银行")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-bankid']")
				input_enter("xpath", "//input[@id='combobox-input-bankid']")
				time.sleep(1)

				# 币种
				click("xpath", "//input[@id='combobox-input-currencyid']")
				sleep(1)
				input("xpath", "//input[@id='combobox-input-currencyid']", "CNY")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-currencyid']")
				input_enter("xpath", "//input[@id='combobox-input-currencyid']")
				sleep(1)

				# 购买银行账户
				click("xpath", "//input[@id='combobox-input-accountid']")
				sleep(1)
				click("xpath", "//div[contains(text(),'CNY-基本户')]")
				sleep(1)

				# 输入理财金额
				click("xpath", "//input[@id='amount-input']")
				sleep(1)
				# 清空内容
				clear("xpath", "//input[@id='amount-input']")
				sleep(1)
				# 输入金额
				input("xpath", "//input[@id='amount-input']", "100000")
				sleep(1)

				# 输入购买日
				today = date.today()
				begin_date = today - timedelta(days=20)
				click("xpath", "//input[@id='begindate-input']")
				sleep(1)
				clear("xpath", "//input[@id='begindate-input']")
				sleep(1)
				input("xpath", "//input[@id='begindate-input']", str(begin_date))
				# 模拟回车键
				keyDown('enter')
				keyUp('enter')
				time.sleep(1)

				# 输入起息日
				today = date.today()
				begin_date = today - timedelta(days=20)
				click("xpath", "//input[@id='intereststartdate-input']")
				sleep(1)
				clear("xpath", "//input[@id='intereststartdate-input']")
				sleep(1)
				input("xpath", "//input[@id='intereststartdate-input']", str(begin_date))
				# 模拟回车键
				keyDown('enter')
				keyUp('enter')
				time.sleep(1)

				# 输入到期日
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

				# 期限结构
				click("xpath", "//input[@id='combobox-input-termstructureid']")
				sleep(1)
				input_enter("xpath", "//input[@id='combobox-input-termstructureid']")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-termstructureid']")
				sleep(1)
				input_enter("xpath", "//input[@id='combobox-input-termstructureid']")
				sleep(1)

				if i == 1:
					# 第一次未实际收付
					double_click("xpath", "//input[@id='paystate']")
					sleep(1)

				else:
					# 其他新增已实际收付
					click("xpath", "//input[@id='paystate']")
					sleep(1)

					# 实际收付日期
					today = date.today()
					pay_date = today
					click("xpath", "//input[@id='paymadedate-input']")
					sleep(1)
					clear("xpath", "//input[@id='paymadedate-input']")
					sleep(1)
					input("xpath", "//input[@id='paymadedate-input']", str(pay_date))
					# 模拟回车键
					# keyDown('enter')
					# keyUp('enter')
					time.sleep(1)

				# 计息方式中输入值
				# 点击计息方式插页
				# 1、选择还本方式
				click("xpath", "//input[@id='combobox-input-interestmode']")
				# 按键往下，选择‘按季还款’
				input_down("xpath", "//input[@id='combobox-input-interestmode']")
				input_enter("xpath", "//input[@id='combobox-input-interestmode']")
				time.sleep(1)

				# 2、选择利率方案
				click("xpath", "//input[@id='combobox-input-interestrateschemeid']")
				# 按键往下，选择利率方案
				sleep(2)
				input_down("xpath", "//input[@id='combobox-input-interestrateschemeid']")
				input_enter("xpath", "//input[@id='combobox-input-interestrateschemeid']")
				sleep(1)

				# 3、选择浮动方式
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
				print("理财合同第%s次新增成功" % i)
				logging.info("理财合同第%s次新增成功" % i)
				time.sleep(3)

				# 第一笔，就先修改，再删除新建的‘理财合同’
				if i == 1:
					# 切入‘理财合同’的iframe窗体
					switch_to("xpath", "//iframe[@id='productsManage-tab-iframe']")

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
					click("xpath",
					      "//div[contains(text(),'ZDHLCHTH')]/parent::*/preceding-sibling::*[3]/descendant::*[2]")

					# 点击修改按钮
					click("xpath", "//span[text()='修改']")
					sleep(1)

					# 切入修改的iframe窗体
					switch_to("xpath", "//iframe[@id='editWin-iframe']")
					print("进入修改窗体")
					sleep(1)

					implici_wait("xpath", "//span[contains(text(),'保存')]")

					# 备注框中输入新内容
					input("xpath", "//textarea[@id='description']", "自动化测试理财合同修改备注框")
					sleep(1)

					# 点击保存按钮
					click("xpath", "//span[text()='保存']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("理财合同，修改成功！")
					logging.info("理财合同，修改成功！")
					time.sleep(3)

					# 第一次审核
					# 切入‘理财合同’的iframe窗体
					switch_to("xpath", "//iframe[@id='productsManage-tab-iframe']")

					# 送审 # 勾选
					click("xpath",
					      "//div[contains(text(),'ZDHLCHTH')]/parent::*/preceding-sibling::*[3]/descendant::*[2]")

					# 点击审核按钮
					click("xpath", "//span[text()='审核']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'审批成功！')]")
					print("理财合同，第一次审批成功！")
					logging.info("理财合同，第一次审批成功！")
					time.sleep(3)

					# 切入‘理财合同’的iframe窗体
					switch_to("xpath", "//iframe[@id='productsManage-tab-iframe']")

					# 勾选
					click("xpath",
					      "//div[contains(text(),'ZDHLCHTH')]/parent::*/preceding-sibling::*[3]/descendant::*[2]")

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
					print("理财合同，取消审核成功！")
					logging.info("理财合同，取消审核成功！")
					time.sleep(3)

					# 切入‘理财合同’的iframe窗体
					switch_to("xpath", "//iframe[@id='productsManage-tab-iframe']")

					# 勾选
					click("xpath",
					      "//div[contains(text(),'ZDHLCHTH')]/parent::*/preceding-sibling::*[3]/descendant::*[2]")

					# 点击删除按钮
					click("xpath", "//span[text()='删除']")

					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现删除的提示框
					implici_wait("xpath", "//span[contains(text(),'成功删除1条记录！')]")
					print("理财合同，删除成功！")
					logging.info("理财合同，删除成功！")
					time.sleep(3)

				# 第二笔，先审核、再取消审核、再托收、再托收到账
				elif i == 2:

					# 第二次审核
					# 切入‘理财合同’的iframe窗体
					switch_to("xpath", "//iframe[@id='productsManage-tab-iframe']")

					# 勾选
					click("xpath",
					      "//div[contains(text(),'ZDHLCHTH')]/parent::*/preceding-sibling::*[3]/descendant::*[2]")

					# 点击审核按钮
					click("xpath", "//span[text()='审核']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'审批成功！')]")
					print("理财合同，第二次审批成功！")
					logging.info("理财合同，第二次审批成功！")
					time.sleep(3)

					# 理财合同赎回申请
					# 切入‘理财申请’的iframe窗体
					switch_to("xpath", "//iframe[@id='productsManage-tab-iframe']")

					# 勾选
					click("xpath",
					      "//div[contains(text(),'ZDHLCHTH')]/parent::*/preceding-sibling::*[3]/descendant::*[2]")

					# 点击取消审核按钮
					click("xpath", "//span[text()='赎回']")
					sleep(1)

					switch_to("xpath", "//iframe[@id='redeemWin-iframe']")

					# 输入赎回日期
					# 点击赎回日期的日历按钮
					js_click("xpath", "//span[@id='operatedate-trigger']")
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
					switch_to("xpath", "//iframe[@id='productsManage-tab-iframe']")
					# 切入新增的iframe窗体
					switch_to("xpath", "//iframe[@id='redeemWin-iframe']")

					# 赎回金额
					input("xpath", "//input[@id='amount-input']", "3000")
					sleep(1)

					# 点击保存按钮
					click("xpath", "//span[text()='保存']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("理财合同，赎回成功！")
					logging.info("理财合同，赎回成功！")
					time.sleep(3)

					# 收益登记
					# 切入‘理财合同’的iframe窗体
					switch_to("xpath", "//iframe[@id='productsManage-tab-iframe']")

					# 勾选
					click("xpath",
					      "//div[contains(text(),'ZDHLCHTH')]/parent::*/preceding-sibling::*[3]/descendant::*[2]")

					# 用JS方便点击‘审核’按钮旁边的倒三角形
					js_click("xpath", "//span[text()='赎回']/parent::*/following-sibling::*/child::*")
					sleep(1)

					# 点击收益登记按钮
					js_click("xpath", "//a[contains(text(),'收益登记')]")
					sleep(1)

					switch_to("xpath", "//iframe[@id='markWin-iframe']")

					# 收益金额
					input("xpath", "//input[@id='amount-input']", "2000")
					sleep(1)

					# 收方账户
					click("xpath", "//input[@id='combobox-input-recaccountid']")
					sleep(1)
					input_enter("xpath", "//input[@id='combobox-input-recaccountid']")
					input_down("xpath", "//input[@id='combobox-input-recaccountid']")
					sleep(1)

					# 点击保存按钮
					click("xpath", "//span[text()='保存']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("理财合同，收益登记成功！")
					logging.info("理财合同，收益登记成功！")
					time.sleep(3)

					# 续购
					# 切入‘理财合同’的iframe窗体
					switch_to("xpath", "//iframe[@id='productsManage-tab-iframe']")
					sleep(1)

					# 用JS方便点击‘审核’按钮旁边的倒三角形
					js_click("xpath", "//span[text()='赎回']/parent::*/following-sibling::*/child::*")
					sleep(1)

					# 点击续购按钮
					js_click("xpath", "//a[contains(text(),'续购')]")
					sleep(1)

					switch_to("xpath", "//iframe[@id='repurchseWin-iframe']")

					# 续购金额
					click("xpath", "//input[@id='amount-input']")
					sleep(1)
					clear("xpath", "//input[@id='amount-input']")
					sleep(1)
					input("xpath", "//input[@id='amount-input']", "20000")
					sleep(1)

					# 预期续购收益
					input("xpath", "//input[@id='interest-input']", "2000")
					sleep(1)

					# 收方账户
					click("xpath", "//input[@id='combobox-input-paytypeid']")
					sleep(1)
					input("xpath", "//input[@id='combobox-input-paytypeid']", "对外付款")
					input_enter("xpath", "//input[@id='combobox-input-paytypeid']")
					input_down("xpath", "//input[@id='combobox-input-paytypeid']")
					sleep(1)

					# 点击保存按钮
					click("xpath", "//span[text()='保存']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("理财合同，续购成功！")
					logging.info("理财合同，续购成功!")
					time.sleep(3)

					# 操作记录查看
					# 切入‘理财合同’的iframe窗体
					switch_to("xpath", "//iframe[@id='productsManage-tab-iframe']")

					# 勾选
					click("xpath", "//div[contains(text(),'ZDHLCHTH')]/parent::*/preceding-sibling::*[3]/descendant::*[2]")

					# 用JS方便点击‘审核’按钮旁边的倒三角形
					js_click("xpath", "//span[text()='操作记录查看']")
					sleep(1)

					switch_to("xpath", "//iframe[@id='operationWin-iframe']")

					click("xpath", "//div[@title='操作标志:赎回']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
					sleep(1)
					click("xpath", "//span[text()='取消赎回']")
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

					# 用隐式等待方法等页面出现审核的提示框
					print("理财合同，取消赎回成功！")
					logging.info("理财合同，取消赎回成功!")
					time.sleep(3)

					click("xpath", "//div[@title='操作标志:续购']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
					sleep(1)
					click("xpath", "//span[text()='取消续购']")
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

					# 用隐式等待方法等页面出现审核的提示框
					print("理财合同，取消续购成功！")
					logging.info("理财合同，取消续购成功!")
					time.sleep(3)

					click("xpath", "//div[@title='操作标志:收益登记']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
					sleep(1)
					click("xpath", "//span[text()='取消收益登记']")
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

					# 用隐式等待方法等页面出现审核的提示框
					print("理财合同，取消收益登记成功！")
					logging.info("理财合同，取消收益登记成功!")
					time.sleep(3)

					switch_parent()
					print("退出当前页面")
					sleep(1)

					# switch_to("xpath", "//iframe[@id='productsManage-tab-iframe']")
					print("进入理财合同页面")
					# 关闭操作做记录查看页面
					click("xpath", "//span[text()='操作记录查看' and @class='f-win-title ']/preceding-sibling::*[1]")

					sleep(1)
					switch_default()

					# 重新生成收益
					switch_to("xpath", "//iframe[@id='productsManage-tab-iframe']")

					# # 勾选
					# click("xpath",
					#       "//div[contains(text(),'ZDHLCHTH')]/parent::*/preceding-sibling::*[3]/descendant::*[2]")
					#
					# 用JS点击重新生成收益
					click("xpath", "//span[text()='重新生成收益']")
					sleep(1)

					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

					switch_default()

					# 重新生成计息：1条！
					implici_wait("xpath", "//span[contains(text(),'重新生成计息：1条！')]")
					print("理财合同，重新生成收益成功！")
					logging.info("理财合同，重新生成收益成功！")
					time.sleep(3)

					# 重新生成收益
					switch_to("xpath", "//iframe[@id='productsManage-tab-iframe']")

					# 勾选
					click("xpath",
					      "//div[contains(text(),'ZDHLCHTH')]/parent::*/preceding-sibling::*[3]/descendant::*[2]")

					# 用JS方便点击‘重新生成收益’按钮旁边的倒三角形
					js_click("xpath", "//span[text()='重新生成收益']/parent::*/following-sibling::*/child::*")
					sleep(1)

					# 点击票据出票按钮
					click("xpath", "//a[contains(text(),'重新生成计提收益')]")
					sleep(1)

					switch_default()

					# 重新生成计息：1条！
					implici_wait("xpath", "//span[contains(text(),'重新生成计息：1条！')]")
					print("理财合同，重新生成计提收益成功！")
					logging.info("理财合同，重新生成计提收益成功！")
					time.sleep(3)

					# 利息试算
					switch_to("xpath", "//iframe[@id='productsManage-tab-iframe']")

					# # 勾选
					# click("xpath",
					#       "//div[contains(text(),'ZDHLCHTH')]/parent::*/preceding-sibling::*[3]/descendant::*[2]")

					click("xpath", "//span[text()='利息试算']")
					sleep(1)

					switch_to("xpath", "//iframe[@id='editWin-iframe']")
					sleep(1)

					click("xpath", "//span[text()='试算']")
					print("理财合同，利息试算试算成功！")
					sleep(1)

					click("xpath", "//span[text()='取消']")
					sleep(1)
					print("理财合同，利息试算取消成功！")

					switch_default()

				# 第三笔，变更然后作废
				elif i == 3:

					# 第三次审核
					# 切入‘理财合同’的iframe窗体
					switch_to("xpath", "//iframe[@id='productsManage-tab-iframe']")

					# 勾选
					click("xpath",
					      "//div[contains(text(),'ZDHLCHTH')]/parent::*/preceding-sibling::*[3]/descendant::*[2]")

					# 点击审核按钮
					click("xpath", "//span[text()='审核']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'审批成功！')]")
					print("理财合同，第二次审批成功！")
					logging.info("理财合同，第二次审批成功！")
					time.sleep(3)

					# # 变更
					# # 切入‘理财申请’的iframe窗体
					# switch_to("xpath", "//iframe[@id='productsManage-tab-iframe']")
					#
					# # 勾选
					# click("xpath", "//div[contains(text(),'ZDHLCHTH')]/parent::*/preceding-sibling::*[3]/descendant::*[2]")
					#
					# # 点击审核按钮
					# click("xpath", "//span[text()='变更']")
					#
					# switch_to("xpath", "//iframe[@id='editWin-iframe']")
					# print("进入变更窗体")
					# sleep(2)
					#
					# # implici_wait("xpath", "//span[contains(text(),'保存')]")
					# # time.sleep(2)
					#
					# # # 备注框中输入新内容
					# # input("xpath", "//textarea[@id='description']", "自动化测试理财合同变更备注框")
					# # sleep(1)
					#
					# # 点击保存按钮
					# click("xpath", "//span[text()='保存']")
					#
					# # 退出所有iframe窗体
					# switch_default()
					#
					# # 用隐式等待方法等页面出现提示框
					# implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					# print("理财合同，变更成功！")
					# logging.info("理财合同，变更成功！")
					# time.sleep(3)
					#
					switch_to("xpath", "//iframe[@id='productsManage-tab-iframe']")

					# 勾选
					click("xpath",
					      "//div[contains(text(),'ZDHLCHTH')]/parent::*/preceding-sibling::*[3]/descendant::*[2]")

					# 点击审核按钮
					click("xpath", "//span[text()='作废']")

					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'成功作废1条记录！')]")
					print("理财合同，作废成功！")
					logging.info("理财合同，作废成功！")
					time.sleep(3)

			# 退出所有iframe窗体
			switch_default()

			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='理财合同']/child::*[1]")

			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//span[@title='理财投资']")

			# 打印操作成功日志
			print("理财合同，操作成功!")
			logging.info("理财合同，操作成功!")
			time.sleep(2)
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("理财合同,失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)

		# 测试理财投资-理财申请
		try:

			# 点击理财投资菜单
			click("xpath", "//span[@title='理财投资']")
			# 点击应付支票登记菜单
			click("xpath", "//span[@title='理财申请']")
			# 退出所有的iframe窗体
			switch_default()

			logging.info("开始测试理财申请功能")
			for i in range(1, 4):
				# 切入‘理财申请’的iframe窗体
				switch_to("xpath", "//iframe[@id='bankFinancialProdApplys-tab-iframe']")

				# 用JS的方法点击新增按钮
				js_click("xpath", "//span[text()='理财申请']")

				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='modWin-iframe']")
				sleep(1)

				# 输入投资机构类型
				click("xpath", "//input[@id='combobox-input-financialinstitutiontype']")
				sleep(1)
				input("xpath", "//input[@id='combobox-input-financialinstitutiontype']", "银行")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-financialinstitutiontype']")
				input_enter("xpath", "//input[@id='combobox-input-financialinstitutiontype']")
				sleep(1)

				# 输入投资机构
				click("xpath", "//input[@id='combobox-input-bankid']")
				sleep(1)
				input("xpath", "//input[@id='combobox-input-bankid']", "中国银行")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-bankid']")
				input_enter("xpath", "//input[@id='combobox-input-bankid']")
				sleep(1)

				# 理财产品类别
				click("xpath", "//input[@id='combobox-input-producttypeid']")
				sleep(1)
				input("xpath", "//input[@id='combobox-input-producttypeid']", "自动化测试理财产品类别")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-producttypeid']")
				input_enter("xpath", "//input[@id='combobox-input-producttypeid']")
				sleep(1)

				# 理财产品名称
				input("xpath", "//input[@id='projectname']", "ZDHLCSQPRODUCT")
				sleep(1)

				# 输入理财金额
				click("xpath", "//input[@id='amount-input']")
				sleep(1)
				# 清空内容
				clear("xpath", "//input[@id='amount-input']")
				sleep(1)
				# 输入金额
				input("xpath", "//input[@id='amount-input']", "100000")
				sleep(1)

				# 币种
				click("xpath", "//input[@id='combobox-input-currencyid']")
				sleep(1)
				input("xpath", "//input[@id='combobox-input-currencyid']", "CNY")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-currencyid']")
				input_enter("xpath", "//input[@id='combobox-input-currencyid']")
				sleep(1)

				# 输入年
				click("xpath", "//input[@id='loantermyear-input']")
				sleep(1)
				# 清空内容
				clear("xpath", "//input[@id='loantermyear-input']")
				sleep(1)
				# 输入金额
				input("xpath", "//input[@id='loantermyear-input']", "5")
				sleep(1)

				# 输入开始日期
				today = date.today()
				begin_date = today - timedelta(days=20)
				click("xpath", "//input[@id='begindate-input']")
				sleep(1)
				clear("xpath", "//input[@id='begindate-input']")
				sleep(1)
				input("xpath", "//input[@id='begindate-input']", str(begin_date))
				# 模拟回车键
				# keyDown('enter')
				# keyUp('enter')
				time.sleep(1)

				# 预期收益率
				click("xpath", "//input[@id='interestrate-input']")
				sleep(1)
				# 清空内容
				clear("xpath", "//input[@id='interestrate-input']")
				sleep(1)
				# 输入金额
				input("xpath", "//input[@id='interestrate-input']", "2")
				sleep(1)

				# 风险评估级别
				click("xpath", "//input[@id='combobox-input-riskassessmentid']")
				sleep(1)
				input("xpath", "//input[@id='combobox-input-riskassessmentid']", "自动化测试风险评估级别")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-riskassessmentid']")
				input_enter("xpath", "//input[@id='combobox-input-riskassessmentid']")
				sleep(1)

				# 备注框中输入新内容
				input("xpath", "//textarea[@id='memo']", "自动化测试理财申请备注框")
				sleep(1)

				# 点击保存按钮
				click("xpath", "//span[text()='保存']")

				# 退出所有iframe窗体
				switch_default()

				# 用隐式等待方法等页面出现提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				print("理财申请第%s次，保存成功！" % i)
				logging.info("理财申请第%s次，保存成功！" % i)
				time.sleep(3)

				# 第一笔，就先修改，再删除新建的‘应收支票管理’
				if i == 1:
					# 切入‘理财申请’的iframe窗体
					switch_to("xpath", "//iframe[@id='bankFinancialProdApplys-tab-iframe']")

					# 点击查看
					# 用JS的方法点击放大镜
					js_click("xpath", "//span[@class='f-contrac-close']")
					sleep(1)

					# 理财产品类别
					click("xpath", "//input[@id='combobox-input-producttypeid']")
					sleep(1)
					input("xpath", "//input[@id='combobox-input-producttypeid']", "自动化测试理财产品类别")
					sleep(1)
					click("xpath", "//div[@title='代码-名称:TestColGory-自动化测试理财产品类别']")
					sleep(1)

					# 点击查询
					click("xpath", "//span[text()='查询']")

					# 修改 # 勾选
					click("xpath",
					      "//div[contains(text(),'ZDHLCSQPRODUCT')]/parent::*/preceding-sibling::*[7]/descendant::*[2]")

					# 点击修改按钮
					click("xpath", "//span[text()='修改']")
					sleep(1)

					# 切入修改的iframe窗体
					switch_to("xpath", "//iframe[@id='modWin-iframe']")
					print("进入窗体")
					sleep(1)

					implici_wait("xpath", "//span[contains(text(),'保存')]")

					# 备注框中输入新内容
					input("xpath", "//textarea[@id='memo']", "自动化测试理财申请修改备注框")
					sleep(1)

					# 点击保存按钮
					click("xpath", "//span[text()='保存']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("理财申请，修改成功！")
					logging.info("理财申请，修改成功！")
					time.sleep(3)

					# 第二次审核
					# 切入‘理财申请’的iframe窗体
					switch_to("xpath", "//iframe[@id='bankFinancialProdApplys-tab-iframe']")

					# 删除 # 勾选
					click("xpath",
					      "//div[contains(text(),'ZDHLCSQPRODUCT')]/parent::*/preceding-sibling::*[7]/descendant::*[2]")

					# 点击审核按钮
					click("xpath", "//span[text()='送审']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'送审成功！')]")
					print("理财申请，第二次送审成功！")
					logging.info("理财申请，第二次送审成功！")
					time.sleep(3)

					# 第一次审批
					# 切入‘理财申请’的iframe窗体
					switch_to("xpath", "//iframe[@id='bankFinancialProdApplys-tab-iframe']")

					# 点击审核按钮
					double_click("xpath",
					             "//div[contains(text(),'ZDHLCSQPRODUCT')]/parent::*/preceding-sibling::*[7]/descendant::*[2]")
					sleep(1)

					switch_to("xpath", "//iframe[@id='wf_taskProcessing_win-iframe']")
					sleep(1)

					click("xpath", "//span[text()='同意']")
					sleep(1)

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("理财申请，第一次审批成功！")
					logging.info("理财申请，第一次审批成功！")
					time.sleep(3)

					# 第二次审批
					# 切入‘理财申请’的iframe窗体
					switch_to("xpath", "//iframe[@id='bankFinancialProdApplys-tab-iframe']")

					# 点击审核按钮
					double_click("xpath",
					             "//div[contains(text(),'ZDHLCSQPRODUCT')]/parent::*/preceding-sibling::*[7]/descendant::*[2]")
					sleep(1)

					switch_to("xpath", "//iframe[@id='wf_taskProcessing_win-iframe']")
					sleep(1)

					click("xpath", "//span[text()='同意']")
					sleep(1)

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("理财申请，第二次审批成功！")
					logging.info("理财申请，第二次审批成功！")
					time.sleep(3)

					# 切入‘理财申请’的iframe窗体
					switch_to("xpath", "//iframe[@id='bankFinancialProdApplys-tab-iframe']")

					# 删除 # 勾选
					click("xpath",
					      "//div[contains(text(),'ZDHLCSQPRODUCT')]/parent::*/preceding-sibling::*[7]/descendant::*[2]")

					# 点击删除按钮
					click("xpath", "//span[text()='取消审批']")

					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现删除的提示框
					implici_wait("xpath", "//span[contains(text(),'理财申请成功取消审批1条！')]")
					print("理财申请，取消审批成功！")
					logging.info("理财申请，取消审批成功！")
					time.sleep(3)

					# 切入‘理财申请’的iframe窗体
					switch_to("xpath", "//iframe[@id='bankFinancialProdApplys-tab-iframe']")

					# 删除 # 勾选
					click("xpath",
					      "//div[contains(text(),'ZDHLCSQPRODUCT')]/parent::*/preceding-sibling::*[7]/descendant::*[2]")

					# 点击删除按钮
					click("xpath", "//span[text()='删除']")

					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现删除的提示框
					implici_wait("xpath", "//span[contains(text(),'理财申请成功删除1条！')]")
					print("理财申请，删除成功！")
					logging.info("理财申请，删除成功！")
					time.sleep(3)

				# 第二笔，先审核、再取消审核、再托收、再托收到账
				elif i == 2:

					# 第二次审核
					# 切入‘理财申请’的iframe窗体
					switch_to("xpath", "//iframe[@id='bankFinancialProdApplys-tab-iframe']")

					# 删除 # 勾选
					click("xpath", "//div[contains(text(),'ZDHLCSQPRODUCT')]/parent::*/preceding-sibling::*[7]/descendant::*[2]")

					# 点击审核按钮
					click("xpath", "//span[text()='送审']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'送审成功！')]")
					print("理财申请，第二次送审成功！")
					logging.info("理财申请，第二次送审成功！")
					time.sleep(3)

					# 第一次审批
					# 切入‘理财申请’的iframe窗体
					switch_to("xpath", "//iframe[@id='bankFinancialProdApplys-tab-iframe']")

					# 点击审核按钮
					double_click("xpath",  "//div[contains(text(),'ZDHLCSQPRODUCT')]/parent::*/preceding-sibling::*[7]/descendant::*[2]")
					sleep(1)

					switch_to("xpath", "//iframe[@id='wf_taskProcessing_win-iframe']")
					sleep(1)

					click("xpath", "//span[text()='同意']")
					sleep(1)

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("理财申请，第一次审批成功！")
					logging.info("理财申请，第一次审批成功！")
					time.sleep(3)

					# 第二次审批
					# 切入‘理财申请’的iframe窗体
					switch_to("xpath", "//iframe[@id='bankFinancialProdApplys-tab-iframe']")

					# 点击审核按钮
					double_click("xpath", "//div[contains(text(),'ZDHLCSQPRODUCT')]/parent::*/preceding-sibling::*[7]/descendant::*[2]")
					sleep(1)

					switch_to("xpath", "//iframe[@id='wf_taskProcessing_win-iframe']")
					sleep(1)

					click("xpath", "//span[text()='同意']")
					sleep(1)

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("理财申请，第二次审批成功！")
					logging.info("理财申请，第二次审批成功！")
					time.sleep(3)

					# 第一次审核
					# 切入‘理财申请’的iframe窗体
					switch_to("xpath", "//iframe[@id='bankFinancialProdApplys-tab-iframe']")

					# 删除 # 勾选
					click("xpath", "//div[contains(text(),'ZDHLCSQPRODUCT')]/parent::*/preceding-sibling::*[7]/descendant::*[2]")

					# 点击审核按钮
					click("xpath", "//span[text()='合同登记']")

					switch_to("xpath", "//iframe[@id='contractregistrationWin-iframe']")

					# 投资产品
					click("xpath", "//input[@id='combobox-input-investproductid']")
					sleep(1)
					input("xpath", "//input[@id='combobox-input-investproductid']", "自动化测试投资产品")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-investproductid']")
					input_enter("xpath", "//input[@id='combobox-input-investproductid']")
					sleep(1)

					# 购买银行账户
					click("xpath", "//input[@id='combobox-input-accountid']")
					sleep(1)
					click("xpath", "//div[contains(text(),'CNY-基本户')]")
					sleep(1)

					# 输入购买日
					today = date.today()
					begin_date = today - timedelta(days=20)
					click("xpath", "//input[@id='begindate-input']")
					sleep(1)
					clear("xpath", "//input[@id='begindate-input']")
					sleep(1)
					input("xpath", "//input[@id='begindate-input']", str(begin_date))
					# 模拟回车键
					keyDown('enter')
					keyUp('enter')
					time.sleep(1)

					# 输入起息日
					today = date.today()
					begin_date = today - timedelta(days=20)
					click("xpath", "//input[@id='intereststartdate-input']")
					sleep(1)
					clear("xpath", "//input[@id='intereststartdate-input']")
					sleep(1)
					input("xpath", "//input[@id='intereststartdate-input']", str(begin_date))
					# 模拟回车键
					keyDown('enter')
					keyUp('enter')
					time.sleep(1)

					# 输入到期日
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

					# 期限结构
					click("xpath", "//input[@id='combobox-input-termstructureid']")
					sleep(1)
					input_enter("xpath", "//input[@id='combobox-input-termstructureid']")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-termstructureid']")
					sleep(1)
					input_enter("xpath", "//input[@id='combobox-input-termstructureid']")
					sleep(1)

					# 计息方式中输入值
					# 点击计息方式插页
					# 1、选择还本方式
					click("xpath", "//input[@id='combobox-input-interestmode']")
					# 按键往下，选择‘按季还款’
					input_down("xpath", "//input[@id='combobox-input-interestmode']")
					input_enter("xpath", "//input[@id='combobox-input-interestmode']")
					time.sleep(1)

					# 2、选择利率方案
					click("xpath", "//input[@id='combobox-input-interestrateschemeid']")
					# 按键往下，选择利率方案
					sleep(2)
					input_down("xpath", "//input[@id='combobox-input-interestrateschemeid']")
					input_enter("xpath", "//input[@id='combobox-input-interestrateschemeid']")
					sleep(1)

					# 3、选择浮动方式
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
					print("理财申请，合同登记成功")
					logging.info("理财申请，合同登记成功")
					time.sleep(3)

					# 理财合同变更申请
					# 切入‘理财申请’的iframe窗体
					switch_to("xpath", "//iframe[@id='bankFinancialProdApplys-tab-iframe']")

					# 删除 # 勾选
					click("xpath", "//div[contains(text(),'ZDHLCSQPRODUCT')]/parent::*/preceding-sibling::*[7]/descendant::*[2]")

					# 用JS方便点击‘送审’按钮旁边的倒三角形
					js_click("xpath", "//span[text()='理财申请']/parent::*/following-sibling::*/child::*")
					sleep(1)

					# 点击取消审核按钮
					js_click("xpath", "//a[contains(text(),'理财合同变更申请')]")
					sleep(1)

					switch_to("xpath", "//iframe[@id='modWin-iframe']")

					click("xpath", "//input[@id='combobox-input-notecode']")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-notecode']")
					input_enter("xpath", "//input[@id='combobox-input-notecode']")
					sleep(1)

					# 申请原因
					input("xpath", "//textarea[@id='applyreason']", "自动化测试理财申请合同变更申请原因")
					sleep(1)

					# 点击下一步
					click("xpath", "//span[text()='下一步']")
					sleep(1)

					switch_to("xpath", "//iframe[@id='contractWin-iframe']")
					sleep(1)

					# 备注框中输入新内容
					input("xpath", "//textarea[@id='description']", "自动化测试理财合同变更申请备注框")
					sleep(1)

					# 点击保存按钮
					click("xpath", "//span[text()='保存']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("理财申请，理财合同变更申请成功！")
					logging.info("理财申请，理财合同变更申请成功！")
					time.sleep(3)

				# 第三笔，作废
				elif i == 3:

					# 第二次审核
					# 切入‘理财申请’的iframe窗体
					switch_to("xpath", "//iframe[@id='bankFinancialProdApplys-tab-iframe']")

					# 删除 # 勾选
					click("xpath",
					      "//div[contains(text(),'ZDHLCSQPRODUCT')]/parent::*/preceding-sibling::*[7]/descendant::*[2]")

					# 点击审核按钮
					click("xpath", "//span[text()='送审']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'送审成功！')]")
					print("理财申请，第二次送审成功！")
					logging.info("理财申请，第二次送审成功！")
					time.sleep(3)

					# 第一次审批
					# 切入‘理财申请’的iframe窗体
					switch_to("xpath", "//iframe[@id='bankFinancialProdApplys-tab-iframe']")

					# 点击审核按钮
					double_click("xpath",
					             "//div[contains(text(),'ZDHLCSQPRODUCT')]/parent::*/preceding-sibling::*[7]/descendant::*[2]")
					sleep(1)

					switch_to("xpath", "//iframe[@id='wf_taskProcessing_win-iframe']")
					sleep(1)

					click("xpath", "//span[text()='同意']")
					sleep(1)

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("理财申请，第一次审批成功！")
					logging.info("理财申请，第一次审批成功！")
					time.sleep(3)

					# 第二次审批
					# 切入‘理财申请’的iframe窗体
					switch_to("xpath", "//iframe[@id='bankFinancialProdApplys-tab-iframe']")

					# 点击审核按钮
					double_click("xpath",
					             "//div[contains(text(),'ZDHLCSQPRODUCT')]/parent::*/preceding-sibling::*[7]/descendant::*[2]")
					sleep(1)

					switch_to("xpath", "//iframe[@id='wf_taskProcessing_win-iframe']")
					sleep(1)

					click("xpath", "//span[text()='同意']")
					sleep(1)

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("理财申请，第二次审批成功！")
					logging.info("理财申请，第二次审批成功！")
					time.sleep(3)

					# 切入‘理财申请’的iframe窗体
					switch_to("xpath", "//iframe[@id='bankFinancialProdApplys-tab-iframe']")

					# 勾选
					click("xpath", "//div[contains(text(),'ZDHLCSQPRODUCT')]/parent::*/preceding-sibling::*[7]/descendant::*[2]")

					# 点击审核按钮
					click("xpath", "//span[text()='作废']")

					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'理财申请成功作废1条！')]")
					print("理财申请，作废成功！")
					logging.info("理财申请，作废成功！")
					time.sleep(3)

			# 退出所有iframe窗体
			switch_default()

			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='理财申请']/child::*[1]")

			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//span[@title='理财投资']")

			# 打印操作成功日志
			print("理财申请，操作成功!")
			logging.info("理财申请，操作成功!")
			time.sleep(2)
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("理财申请,失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		
		# 理财申请查看
		# 测试理财申请查看
		try:
			# 点击理财投资菜单
			click("xpath", "//span[@title='理财投资']")
			# 点击理财合同登记菜单
			click("xpath", "//span[@title='理财申请查看']")
			# 退出所有的iframe窗体
			switch_default()
			logging.info("开始测试理财申请查看功能")

			# 切入‘理财申请查看’的iframe窗体
			switch_to("xpath", "//iframe[@id='bankFinancialProdApplysView-tab-iframe']")

			# 点击查看
			# 用JS的方法点击放大镜
			js_click("xpath", "//span[@class='f-contrac-close']")
			sleep(1)

			click("xpath", "//input[@id='combobox-input-producttypeid']")
			# 输入自动化测试理财产品类别,，模糊查询
			input("xpath", "//input[@id='combobox-input-producttypeid']", "自动化测试理财产品类别")
			sleep(1)
			click("xpath", "//div[@title='代码-名称:TestColGory-自动化测试理财产品类别']")
			time.sleep(1)

			# 点击查询
			click("xpath", "//span[text()='查询']")

			# 用隐式等待方法等页面出现预期数据：理财产品名称:ZDHLCSQPRODUCT
			implici_wait("xpath", "//div[@title='理财产品名称:ZDHLCSQPRODUCT']")
			print("理财申请查看成功！")
			time.sleep(3)

			# 退出所有iframe窗体
			switch_default()

			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='理财申请查看']/child::*[1]")

			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//span[@title='理财投资']")

			# 打印操作成功日志
			print("理财申请查看，操作成功!")
			logging.info("理财申请查看，操作成功!")
			time.sleep(2)
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("理财申请查看,失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)

		# 理财合同查看
		# 测试理财申请查看
		try:
			# 点击理财投资菜单
			click("xpath", "//span[@title='理财投资']")
			# 点击理财合同查看菜单
			click("xpath", "//span[@title='理财合同查看']")
			# 退出所有的iframe窗体
			switch_default()
			logging.info("开始测试理财合同查看功能")

			# 切入‘理财合同查看’的iframe窗体
			switch_to("xpath", "//iframe[@id='productsView-tab-iframe']")

			# 点击查看
			# 用JS的方法点击放大镜
			js_click("xpath", "//span[@class='f-contrac-close']")
			sleep(1)

			click("xpath", "//input[@id='combobox-input-investcategoryid']")
			# 输入自动化测试理财产品类别,，模糊查询
			input("xpath", "//input[@id='combobox-input-investcategoryid']", "自动化测试理财产品类别")
			sleep(1)
			click("xpath", "//div[@title='代码-名称:TestColGory-自动化测试理财产品类别']")
			time.sleep(1)

			# 点击查询
			click("xpath", "//span[text()='查询']")

			click("xpath", "//div[contains(text(),'ZDHLCHTH')]/parent::*/preceding-sibling::*[3]/descendant::*[2]")

			click("xpath", "//span[text()='操作记录查看']")

			switch_to("xpath", "//iframe[@id='operationWin-iframe']")

			# 用隐式等待方法等页面出现预期数据：理财产品名称:ZDHLCSQPRODUCT
			implici_wait("xpath", "//div[@title='操作标志:取消赎回']")
			print("理财合同查看，操作记录查看成功！")
			time.sleep(3)

			switch_parent()
			sleep(1)

			click("xpath", "//span[text()='操作记录查看' and @class='f-win-title ']/preceding-sibling::*[1]")
			sleep(1)

			# 退出所有iframe窗体
			switch_default()

			# 切入‘理财合同查看’的iframe窗体
			switch_to("xpath", "//iframe[@id='productsView-tab-iframe']")

			click("xpath", "//span[text()='可操作组织查看']")

			# 用隐式等待方法等页面出现预期数据：投资产品:TestInvPro-自动化测试投资产品
			implici_wait("xpath", "//div[@title='投资产品:TestInvPro-自动化测试投资产品']")
			print("理财合同查看，可操作组织查看成功！")
			time.sleep(3)

			click("xpath", "//span[text()='本级及下级查看']")

			# 用隐式等待方法等页面出现预期数据：投资产品:TestInvPro-自动化测试投资产品
			implici_wait("xpath", "//div[@title='投资产品:TestInvPro-自动化测试投资产品']")
			print("理财合同查看，本级及下级查看成功！")
			time.sleep(3)

			switch_default()

			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='理财合同查看']/child::*[1]")

			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//span[@title='理财投资']")

			# 打印操作成功日志
			print("理财合同查看，操作成功!")
			logging.info("理财合同查看，操作成功!")
			time.sleep(2)
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("理财合同查看,失败！" + str(traceback.format_exc()))
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
			input("xpath", "//input[@name='code']", "L07")
			sleep(1)
			
			# 输入名称
			input("xpath", "//input[@id='name']", "活期投资")
			sleep(1)
			# 单据对象
			click("xpath", "//input[@id='combobox-input-noteobjectid']")
			sleep(1)
			input("xpath", "//input[@id='combobox-input-noteobjectid']", "活期投资")
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
		
		# 投资理财--活期投资
		try:
			click("xpath", "//span[@title='投资理财']")
			# 点击理财合同查看菜单
			click("xpath", "//span[@title='活期投资']")
			# 退出所有iframe窗体
			switch_default()

			# 切入投资理财的iframe窗体
			switch_to("xpath", "//iframe[@id='currentinvestcontract-tab-iframe']")
			logging.info("开始测试投资理财功能")

			# 用JS的方法点击新增按钮
			js_click("xpath", "//span[text()='账户引入']")
			sleep(1)

			click("xpath", "//span[text()='确定']")

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'账户引入成功！')]")
			print("投资理财，账户引入成功！")
			time.sleep(3)

			switch_to("xpath", "//iframe[@id='currentinvestcontract-tab-iframe']")

			# 点击查看
			# 用JS的方法点击放大镜
			js_click("xpath", "//span[@class='f-contrac-close']")
			sleep(1)

			# 选择银行
			click("xpath", "//input[@id='combobox-input-bankid']")
			sleep(1)
			input("xpath", "//input[@id='combobox-input-bankid']", "华夏银行")
			click("xpath", "//div[@title='代码-名称:HXB-华夏银行']")
			sleep(1)

			# 选择审核状态
			click("xpath", "//input[@id='combobox-input-approvestate']")
			sleep(1)
			input("xpath", "//input[@id='combobox-input-approvestate']", "未审核")
			click("xpath", "//div[@title='未审核']")
			sleep(1)

			# 点击查询
			click("xpath", "//span[text()='查询']")
			sleep(1)

			# 勾选
			click("xpath", "//div[contains(text(),'HXB-华夏银行')]/parent::*/preceding-sibling::*[4]/descendant::*[2]")
			# 点击保存按钮

			# 点击修改按钮
			click("xpath", "//span[text()='投资确认']")
			sleep(1)

			# 切入新增的iframe窗体
			switch_to("xpath", "//iframe[@id='modWin-iframe']")
			sleep(1)

			# 计息方式中输入值
			# 点击计息方式插页
			# 1、选择还本方式
			click("xpath", "//input[@id='combobox-input-interestmode']")
			# 按键往下，选择‘按季还款’
			input_down("xpath", "//input[@id='combobox-input-interestmode']")
			input_enter("xpath", "//input[@id='combobox-input-interestmode']")
			time.sleep(1)

			# 2、选择利率方案
			click("xpath", "//input[@id='combobox-input-interestrateschemeid']")
			# 按键往下，选择利率方案
			sleep(2)
			input_down("xpath", "//input[@id='combobox-input-interestrateschemeid']")
			input_enter("xpath", "//input[@id='combobox-input-interestrateschemeid']")
			sleep(1)

			# 3、选择浮动方式
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
			print("活期投资，投资确认成功")
			logging.info("活期投资，投资确认成功")
			time.sleep(3)

			# 变更
			switch_to("xpath", "//iframe[@id='currentinvestcontract-tab-iframe']")

			# 选择审核状态
			click("xpath", "//input[@id='combobox-input-approvestate']")
			sleep(1)
			click("xpath", "//div[@title='未审核']")
			input("xpath", "//input[@id='combobox-input-approvestate']", "已审核")
			click("xpath", "//div[@title='已审核']")
			sleep(1)

			# 点击查询
			click("xpath", "//span[text()='查询']")
			sleep(1)

			# 勾选
			click("xpath", "//div[contains(text(),'HXB-华夏银行')]/parent::*/preceding-sibling::*[4]/descendant::*[2]")

			# 点击修改按钮
			click("xpath", "//span[text()='变更']")
			sleep(1)

			# 切入新增的iframe窗体
			switch_to("xpath", "//iframe[@id='modWin-iframe']")
			sleep(1)

			# 描述框中填入值
			input("xpath", "//textarea[@id='description']", "自动化测试活期投资备注修改")
			sleep(1)

			# 点击保存按钮
			click("xpath", "//span[text()='保存']")

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功')]")
			print("活期投资，变更成功")
			logging.info("活期投资，变更成功")
			time.sleep(3)

			# 收益登记
			switch_to("xpath", "//iframe[@id='currentinvestcontract-tab-iframe']")

			# 勾选
			click("xpath", "//div[contains(text(),'HXB-华夏银行')]/parent::*/preceding-sibling::*[4]/descendant::*[2]")

			# 点击修改按钮
			click("xpath", "//span[text()='收益登记']")
			sleep(1)

			# 切入新增的iframe窗体
			switch_to("xpath", "//iframe[@id='markWin-iframe']")
			sleep(1)

			# 收益金额
			input("xpath", "//input[@id='amount-input']", "30000")
			sleep(1)

			# 点击保存按钮
			click("xpath", "//span[text()='保存']")

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功')]")
			print("活期投资，收益登记成功")
			logging.info("活期投资，收益登记成功")
			time.sleep(3)

			# 重新生成收益
			switch_to("xpath", "//iframe[@id='currentinvestcontract-tab-iframe']")

			# # 勾选
			# click("xpath", "//div[contains(text(),'HXB-华夏银行')]/parent::*/preceding-sibling::*[4]/descendant::*[2]")
			#
			# 点击修改按钮
			click("xpath", "//span[text()='重新生成收益']")
			sleep(1)

			click("xpath", "//span[text()='重新生成收益' and @class='f-new-btn-text ']")
			sleep(1)

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功')]")
			print("活期投资，重新生成收益成功")
			logging.info("活期投资，重新生成收益成功")
			time.sleep(3)

			# 终止
			switch_to("xpath", "//iframe[@id='currentinvestcontract-tab-iframe']")

			# 勾选
			click("xpath", "//div[contains(text(),'HXB-华夏银行')]/parent::*/preceding-sibling::*[4]/descendant::*[2]")

			# 点击终止按钮
			click("xpath", "//span[text()='终止']")
			sleep(1)

			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

			# 到期日选择
			today = date.today()
			cend_date = today
			click("xpath", "//input[@id='cEndDate-input']")
			sleep(1)
			clear("xpath", "//input[@id='cEndDate-input']")
			sleep(1)
			input("xpath", "//input[@id='cEndDate-input']", str(cend_date))
			# 模拟回车键
			# keyDown('enter')
			# keyUp('enter')
			time.sleep(1)

			click("xpath", "//div[contains(text(),'到期日选择')]")

			# 点击确定按钮
			click("xpath",
			      "//div[contains(text(),'到期日选择')]/parent::*/descendant::*[2]/following-sibling::*[1]/descendant::*[4]")

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("活期投资，终止成功")
			logging.info("活期投资，终止成功")
			time.sleep(3)

			# 删除功能
			switch_to("xpath", "//iframe[@id='currentinvestcontract-tab-iframe']")

			# 选择审核状态
			click("xpath", "//input[@id='combobox-input-approvestate']")
			sleep(1)
			click("xpath", "//div[@title='已审核']")
			input("xpath", "//input[@id='combobox-input-approvestate']", "未审核")
			click("xpath", "//div[@title='未审核']")
			sleep(1)

			# 点击查询
			click("xpath", "//span[text()='查询']")
			sleep(1)

			# 勾选
			click("xpath", "//div[contains(text(),'HXB-华夏银行')]/parent::*/preceding-sibling::*[4]/descendant::*[2]")

			# 点击终止按钮
			click("xpath", "//span[text()='删除']")
			sleep(1)

			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("活期投资，删除成功")
			logging.info("活期投资，删除成功")
			time.sleep(3)

			switch_default()

			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='活期投资']/child::*[1]")

			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//span[@title='投资理财']")

			# 打印操作成功日志
			print("活期投资，操作成功!")
			logging.info("活期投资，操作成功!")
			time.sleep(2)

		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("活期投资操作失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)

		# 活期投资查看
		# 测试活期投资查看
		try:
			# 点击投资理财菜单
			click("xpath", "//span[@title='投资理财']")
			# 点击理财合同登记菜单
			click("xpath", "//span[@title='活期投资查看']")
			# 退出所有的iframe窗体
			switch_default()
			logging.info("开始测试活期投资查看功能")

			# 切入‘活期投资查看’的iframe窗体
			switch_to("xpath", "//iframe[@id='currentinvestcontractview-tab-iframe']")

			# 点击查看
			# 用JS的方法点击放大镜
			js_click("xpath", "//span[@class='f-contrac-close']")
			sleep(1)

			# 通过银行查找
			click("xpath", "//input[@id='combobox-input-bankid']")
			# 输入自动化测试理财产品类别,，模糊查询
			input("xpath", "//input[@id='combobox-input-bankid']", "华夏银行")
			sleep(1)
			click("xpath", "//div[@title='代码-名称:HXB-华夏银行']")
			time.sleep(1)

			# 点击查询
			click("xpath", "//span[text()='查询']")

			# 用隐式等待方法等页面出现预期数据：理财产品类别:TestColGory-自动化测试理财产品类别
			implici_wait("xpath", "//div[@title='理财产品类别:TestColGory-自动化测试理财产品类别']")
			print("活期投资查看成功！")
			time.sleep(3)

			# 退出所有iframe窗体
			switch_default()

			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='活期投资查看']/child::*[1]")

			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//span[@title='投资理财']")

			# 打印操作成功日志
			print("活期投资查看，操作成功!")
			logging.info("活期投资查看，操作成功!")
			time.sleep(2)
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("活期投资查看,失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		
		# 开始测试定期存单
		try:

			# 点击‘定期存单'菜单
			click("xpath", "//span[text()='定期存单']")
			switch_default()
			logging.info("开始测试定期存单功能")

			for i in range(1, 2):

				# 切入‘定期存单’的iframe窗体
				switch_to("xpath", "//iframe[@id='bankTermDeposits-tab-iframe']")
				sleep(1)

				# 切入直联存款管理
				switch_to("xpath", "//iframe[@id='subTabOne-iframe']")
				sleep(1)
				logging.info("开始测试直联存款管理功能")

				# 用JS的方法点击新增按钮
				js_click("xpath", "//span[text()='新增']")

				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='addWin-iframe']")
				sleep(1)

				# 选择银行账户
				click("xpath", "//input[@id='combobox-input-accountid']")
				sleep(1)
				input("xpath", "//input[@id='combobox-input-accountid']", "NOK")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-accountid']")
				input_enter("xpath", "//input[@id='combobox-input-accountid']")
				sleep(1)

				# 描述框
				input("xpath", "//textarea[@id='memo']", "自动化测试直联存款管理备注框")
				sleep(1)

				# 点击保存按钮
				click("xpath", "//span[text()='保存']")

				# 退出所有iframe窗体
				switch_default()

				# 用隐式等待方法等页面出现新增成功的提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				print("直联存款管理，保存成功！")
				time.sleep(3)

				if i == 1:
					# 修改功能
					# 切入‘定期存单’的iframe窗体
					switch_to("xpath", "//iframe[@id='bankTermDeposits-tab-iframe']")
					sleep(1)

					# 切入直联存款管理
					switch_to("xpath", "//iframe[@id='subTabOne-iframe']")
					sleep(1)

					# 点击查看
					# 用JS的方法点击放大镜
					js_click("xpath", "//span[@class='f-contrac-close']")
					sleep(1)

					# 选择银行
					click("xpath", "//input[@id='combobox-input-bankid']")
					# 输入银行名称，模糊查询
					input("xpath", "//input[@id='combobox-input-bankid']", "华夏银行")
					sleep(1)
					click("xpath", "//div[@title='代码-名称:HXB-华夏银行']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
					sleep(1)

					# 点击查询
					click("xpath", "//span[text()='查询']")

					# 修改
					# 勾选
					click("xpath", "//div[@title='银行:HXB-华夏银行']/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 点击修改按钮
					click("xpath", "//span[text()='修改']")

					# 切入修改的iframe窗体
					switch_to("xpath", "//iframe[@id='modWin-iframe']")
					sleep(1)

					# 描述框
					input("xpath", "//textarea[@id='memo']", "自动化测试修改直联存款管理备注框")
					sleep(1)

					# 点击保存按钮
					click("xpath", "//span[text()='保存']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现新增成功的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("直联存款管理，修改成功！")
					time.sleep(3)

					# 查询
					switch_to("xpath", "//iframe[@id='bankTermDeposits-tab-iframe']")
					sleep(1)

					# 切入直联存款管理
					switch_to("xpath", "//iframe[@id='subTabOne-iframe']")
					sleep(1)

					# 查询
					# 勾选
					click("xpath", "//div[@title='银行:HXB-华夏银行']/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 点击查询按钮
					click("xpath", "//span[text()='删除']/ancestor::*[2]/following-sibling::*[2]/descendant::*[2]")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现新增成功的提示框
					# implici_wait("xpath", "//a[contains(text(),'NOK-挪威克朗: 0')]")
					print("直联存款管理，查询成功！")
					time.sleep(3)

					# 删除
					# 勾选
					switch_to("xpath", "//iframe[@id='bankTermDeposits-tab-iframe']")
					sleep(1)

					# 切入直联存款管理
					switch_to("xpath", "//iframe[@id='subTabOne-iframe']")
					sleep(1)

					# 查询
					# 勾选
					# click("xpath", "//div[@title='银行:HXB-华夏银行']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
					#
					# 点击删除按钮
					click("xpath", "//span[text()='删除']")

					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现删除的提示框
					implici_wait("xpath", "//span[contains(text(),'共处理1个记录;删除成功1个;删除失败0个;')]")
					print("直联存款管理，删除成功！")
					time.sleep(3)

					# 非直联存单维护
					# 切入‘定期存单’的iframe窗体
					switch_to("xpath", "//iframe[@id='bankTermDeposits-tab-iframe']")
					sleep(1)

					click("xpath", "//span[text()='非直联存单维护']")

					# 切入非直联存单维护
					switch_to("xpath", "//iframe[@id='subTabTwo-iframe']")
					sleep(1)
					logging.info("开始测试非直联存单维护功能")

					# 用JS的方法点击新增按钮
					js_click("xpath", "//span[text()='新增']")

					# 切入新增的iframe窗体
					switch_to("xpath", "//iframe[@id='addWin-iframe']")
					sleep(1)

					# 选择银行账户
					click("xpath", "//input[@id='combobox-input-accountid']")
					sleep(1)
					input("xpath", "//input[@id='combobox-input-accountid']", "NOK")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-accountid']")
					input_enter("xpath", "//input[@id='combobox-input-accountid']")
					sleep(1)

					# 存单号
					# 设置时间的变成存储
					temp = time.strftime("%Y%m%d%H%M%S")
					input("xpath", "//input[@id='depositcode']", str(temp))
					sleep(1)

					# 金额
					input("xpath", "//input[@id='notemoney-input']", "30000")
					sleep(1)

					# 利率
					input("xpath", "//input[@id='rate-input']", "30")
					sleep(1)

					# 到期处理方式
					click("xpath", "//input[@id='combobox-input-dumpflag']")
					sleep(1)
					input("xpath", "//input[@id='combobox-input-dumpflag']", "不转存")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-dumpflag']")
					input_enter("xpath", "//input[@id='combobox-input-dumpflag']")
					sleep(1)

					# 转存期限
					input("xpath", "//input[@id='transferyear-input']", "3")
					sleep(1)

					# 点击保存按钮
					click("xpath", "//span[text()='保存']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现新增成功的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("非直联存单维护，保存成功！")
					time.sleep(3)

					if i == 1:
						# 修改功能
						# 切入‘定期存单’的iframe窗体
						switch_to("xpath", "//iframe[@id='bankTermDeposits-tab-iframe']")
						sleep(1)

						# 切入非直联存单维护
						switch_to("xpath", "//iframe[@id='subTabTwo-iframe']")
						sleep(1)

						# 点击查看
						# 用JS的方法点击放大镜
						js_click("xpath", "//span[@class='f-contrac-close']")
						sleep(1)

						# 选择银行
						click("xpath", "//input[@id='combobox-input-bankid']")
						# 输入银行名称，模糊查询
						input("xpath", "//input[@id='combobox-input-bankid']", "华夏银行")
						sleep(1)
						click("xpath",
						      "//div[@title='代码-名称:HXB-华夏银行']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
						sleep(1)

						# 点击查询
						click("xpath", "//span[text()='查询']")

						# 修改
						# 勾选
						click("xpath", "//div[@title='银行:HXB-华夏银行']/parent::*/preceding-sibling::*[1]/descendant::*[2]")

						# 点击修改按钮
						click("xpath", "//span[text()='修改']")

						# 切入修改的iframe窗体
						switch_to("xpath", "//iframe[@id='modWin-iframe']")
						sleep(1)

						# 描述框
						input("xpath", "//textarea[@id='memo']", "自动化测试修改非直联存单维护备注框")
						sleep(1)

						# 点击保存按钮
						click("xpath", "//span[text()='保存']")

						# 退出所有iframe窗体
						switch_default()

						# 用隐式等待方法等页面出现新增成功的提示框
						implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
						print("非直联存单维护，修改成功！")
						time.sleep(3)

						# 支取
						switch_to("xpath", "//iframe[@id='bankTermDeposits-tab-iframe']")
						sleep(1)

						# 切入非直联存单维护
						switch_to("xpath", "//iframe[@id='subTabTwo-iframe']")
						sleep(1)

						# 支取
						# 勾选
						click("xpath", "//div[@title='银行:HXB-华夏银行']/parent::*/preceding-sibling::*[1]/descendant::*[2]")

						# 点击查询按钮
						click("xpath", "//span[text()='支取']")

						# 切入非直联存单维护
						switch_to("xpath", "//iframe[@id='drawWin-iframe']")
						sleep(1)

						# 点击查询按钮
						click("xpath", "//span[text()='确认']")

						# 退出所有iframe窗体
						switch_default()

						# 用隐式等待方法等页面出现新增成功的提示框
						implici_wait("xpath", "//span[contains(text(),'共支取成功1条,失败0条定存单!')]")
						print("非直联存单维护，支取成功！")
						time.sleep(3)

						# 删除
						# 勾选
						switch_to("xpath", "//iframe[@id='bankTermDeposits-tab-iframe']")
						sleep(1)

						# 切入直联存款管理
						switch_to("xpath", "//iframe[@id='subTabTwo-iframe']")
						sleep(1)

						# 删除
						# 勾选
						click("xpath", "//div[@title='银行:HXB-华夏银行']/parent::*/preceding-sibling::*[1]/descendant::*[2]")

						# 点击删除按钮
						click("xpath", "//span[text()='删除']")

						# 点击弹出框的OK键
						click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

						# 退出所有iframe窗体
						switch_default()

						# 用隐式等待方法等页面出现删除的提示框
						implici_wait("xpath", "//span[contains(text(),'共处理1个记录;删除成功1个;删除失败0个;')]")
						print("非直联存单维护，删除成功！")
						time.sleep(3)

			switch_default()
			# 再次点击基础设置菜单，使之关闭
			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='定期存单']/child::*[1]")

			# 打印操作成功日志
			print("非直联存单维护，操作成功!")
			logging.info("非直联存单维护，操作成功!")
			time.sleep(2)

		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("非直联存单维护,失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		
		# 测试现金投资计划编制
		try:

			# 点击支票管理菜单
			click("xpath", "//span[@title='现金投资计划']")
			# 点击应付支票登记菜单

			click("xpath", "//span[@title='现金投资计划编制']")
			# 退出所有的iframe窗体
			switch_default()

			logging.info("开始测试现金投资计划编制功能")
			for i in range(1, 4):
				# 切入‘现金投资计划编制’的iframe窗体
				switch_to("xpath", "//iframe[@id='cashinvestmentbudget-tab-iframe']")

				# 用JS的方法点击新增按钮
				js_click("xpath", "//span[text()='新增']")

				# 设置时间的变成存储
				temp = time.strftime("%Y%m%d%H%M%S")

				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='addWin-iframe']")
				sleep(1)

				# 填报周期
				click("xpath", "//input[@id='reportperiod-input']")
				sleep(1)
				input("xpath", "//input[@id='reportperiod-input']", "2020-07")
				sleep(1)
				# input_down("xpath", "//input[@id='reportperiod-input']")
				# input_enter("xpath", "//input[@id='reportperiod-input']")
				sleep(1)

				# 点击保存按钮
				click("xpath", "//span[text()='下一步']")
				sleep(2)

				switch_parent()
				sleep(1)

				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='addWin-iframe']")
				sleep(1)

				click("xpath", "//span[text()='新增行']")
				sleep(1)

				# 选择银行
				click("xpath", "//input[@id='combobox-input-detailgrid-orgid-0']")
				sleep(1)
				input("xpath", "//input[@id='combobox-input-detailgrid-orgid-0']", "亚唐科技")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-detailgrid-orgid-0']")
				input_enter("xpath", "//input[@id='combobox-input-detailgrid-orgid-0']")
				sleep(1)

				# 币种
				click("xpath", "//input[@id='combobox-input-detailgrid-currencyid-0']")
				sleep(1)
				input("xpath", "//input[@id='combobox-input-detailgrid-currencyid-0']", "CNY")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-detailgrid-currencyid-0']")
				input_enter("xpath", "//input[@id='combobox-input-detailgrid-currencyid-0']")
				sleep(1)

				# 输入到期日期
				today = date.today()
				collection_date = today + timedelta(days=70)
				click("xpath", "//input[@id='detailgrid-terminatedate-0-input']")
				sleep(1)
				clear("xpath", "//input[@id='detailgrid-terminatedate-0-input']")
				sleep(1)
				input("xpath", "//input[@id='detailgrid-terminatedate-0-input']", str(collection_date))
				
				time.sleep(2)

				# 预计操作日期
				# 点击预计操作日期的日历按钮
				click("xpath", "//span[@id='detailgrid-planoperdate-0-trigger']")
				time.sleep(1)
				
				# 退出所有iframe窗体
				switch_default()
				# 切入日历框的iframe
				switch_to("xpath", "//iframe[@hidefocus='true']")
				sleep(1)
				# 点击日历框中今天的按钮
				click("xpath", "//input[@id='dpOkInput']")
				time.sleep(1)
				# 退出当前日历框的iframe窗体
				switch_default()
				
				# 切入‘应现金计划投资编制’的iframe窗体
				switch_to("xpath", "//iframe[@id='cashinvestmentbudget-tab-iframe']")
				sleep(1)
				
				switch_to("xpath", "//iframe[@id='addWin-iframe']")
				sleep(1)
				
				# 操作后投资品种
				click("xpath", "//input[@id='combobox-input-detailgrid-aftervarietyid-0']")
				sleep(1)
				input_enter("xpath", "//input[@id='combobox-input-detailgrid-aftervarietyid-0']")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-detailgrid-aftervarietyid-0']")
				input_enter("xpath", "//input[@id='combobox-input-detailgrid-aftervarietyid-0']")
				sleep(1)

				# 操作后投资品种分类
				click("xpath", "//input[@id='combobox-input-detailgrid-investcategoryid-0']")
				sleep(1)
				input("xpath", "//input[@id='combobox-input-detailgrid-investcategoryid-0']", "自动化测试理财产品类别")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-detailgrid-investcategoryid-0']")
				input_enter("xpath", "//input[@id='combobox-input-detailgrid-investcategoryid-0']")
				sleep(1)

				# 操作后金融机构
				click("xpath", "//input[@id='combobox-input-detailgrid-afterbankid-0']")
				sleep(1)
				input("xpath", "//input[@id='combobox-input-detailgrid-afterbankid-0']", "中国银行")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-detailgrid-afterbankid-0']")
				input_enter("xpath", "//input[@id='combobox-input-detailgrid-afterbankid-0']")
				sleep(1)

				# 操作后金额
				input("xpath", "//input[@id='detailgrid-afteramount-0-input']", "3000")
				sleep(1)

				# 预计收益率
				input("xpath", "//input[@id='detailgrid-interestrate-0-input']", "20")
				sleep(1)

				# 预计天数
				input("xpath", "//input[@id='detailgrid-plandays-0-input']", "20")
				sleep(1)

				# 操作后结束日期
				today = date.today()
				collection_date = today + timedelta(days=70)
				click("xpath", "//input[@id='detailgrid-afterenddate-0-input']")
				sleep(1)
				clear("xpath", "//input[@id='detailgrid-afterenddate-0-input']")
				sleep(1)
				input("xpath", "//input[@id='detailgrid-afterenddate-0-input']", str(collection_date))
				# 模拟回车键
				# keyDown('enter')
				# keyUp('enter')
				time.sleep(2)

				# 点击查询
				click("xpath", "//span[text()='保存']")
				sleep(1)

				# 退出所有iframe窗体
				switch_default()

				# 用隐式等待方法等页面出现提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				print("现金投资计划编制第%s次，保存成功！" % i)
				logging.info("现金投资计划编制第%s次，保存成功！" % i)
				time.sleep(3)

				# 第一笔，就先修改，再删除新建的‘现金投资计划编制’
				if i == 1:
					# 切入‘现金投资计划编制’的iframe窗体
					switch_to("xpath", "//iframe[@id='cashinvestmentbudget-tab-iframe']")

					# 点击查看
					# 用JS的方法点击放大镜
					js_click("xpath", "//span[@class='f-contrac-close']")
					sleep(1)

					# 填报周期
					click("xpath", "//input[@id='reportperiod-input']")
					sleep(1)
					input("xpath", "//input[@id='reportperiod-input']", "2020-07")
					sleep(1)
					# input_down("xpath", "//input[@id='reportperiod-input']")
					# input_enter("xpath", "//input[@id='reportperiod-input']")
					# sleep(1)

					# 点击查询
					click("xpath", "//span[text()='查询']")

					# 修改
					# 勾选
					click("xpath", "//div[@title='填报周期:2020-07-01']/parent::*/preceding-sibling::*[3]/descendant::*[2]")

					# 点击修改按钮
					click("xpath", "//span[text()='修改']")

					# 切入修改的iframe窗体
					switch_to("xpath", "//iframe[@id='modWin-iframe']")
					sleep(1)

					# 修改预计天数
					click("xpath", "//input[@id='detailgrid-plandays-0-input']")
					sleep(1)
					# 清空内容
					clear("xpath", "//input[@id='detailgrid-plandays-0-input']")
					sleep(1)
					# 预计天数
					input("xpath", "//input[@id='detailgrid-plandays-0-input']", "30")
					sleep(1)

					# 点击保存按钮
					click("xpath", "//span[text()='保存']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("现金投资计划编制，修改成功！")
					logging.info("现金投资计划编制，修改成功！")
					time.sleep(3)

					# 切入‘现金投资计划编制’的iframe窗体
					switch_to("xpath", "//iframe[@id='cashinvestmentbudget-tab-iframe']")

					# 删除 # 勾选
					click("xpath", "//div[@title='填报周期:2020-07-01']/parent::*/preceding-sibling::*[3]/descendant::*[2]")

					# 点击删除按钮
					click("xpath", "//span[text()='删除']")

					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现删除的提示框
					implici_wait("xpath", "//span[contains(text(),'成功删除1条记录！')]")
					print("现金投资计划编制，删除成功！")
					logging.info("现金投资计划编制.，删除成功！")
					time.sleep(3)

				# 第二笔，先审核、再取消审核、再变更、再作废
				elif i == 2:

					# 第一次审核
					# 切入‘现金投资计划编制’的iframe窗体
					switch_to("xpath", "//iframe[@id='cashinvestmentbudget-tab-iframe']")

					# 删除 # 勾选
					click("xpath", "//div[@title='填报周期:2020-07-01']/parent::*/preceding-sibling::*[3]/descendant::*[2]")

					# 点击审核按钮
					click("xpath", "//span[text()='审核']")

					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'成功审核1条记录')]")
					print("现金投资计划编制，第一次审核成功！")
					logging.info("现金投资计划编制，第一次审核成功！")
					time.sleep(3)

					# 取消审核
					# 切入‘现金投资计划编制’的iframe窗体
					switch_to("xpath", "//iframe[@id='cashinvestmentbudget-tab-iframe']")

					# 删除 # 勾选
					click("xpath", "//div[@title='填报周期:2020-07-01']/parent::*/preceding-sibling::*[3]/descendant::*[2]")

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
					print("现金投资计划编制，取消审核成功！")
					logging.info("现金投资计划编制，取消审核成功！")
					time.sleep(3)

					# 第二次审核
					# 切入‘现金投资计划编制’的iframe窗体
					switch_to("xpath", "//iframe[@id='cashinvestmentbudget-tab-iframe']")

					# 删除 # 勾选
					click("xpath", "//div[@title='填报周期:2020-07-01']/parent::*/preceding-sibling::*[3]/descendant::*[2]")

					# 点击审核按钮
					click("xpath", "//span[text()='审核']")

					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'成功审核1条记录')]")
					print("现金投资计划编制，第二次审核成功！")
					logging.info("现金投资计划编制，第二次审核成功！")
					time.sleep(3)

					# 缺少变更

					# # 变更
					# # 切入‘现金投资计划编制’的iframe窗体
					# switch_to("xpath", "//iframe[@id='cashinvestmentbudget-tab-iframe']")
					#
					# click("xpath", "//div[@title='填报周期:2020-07-01']/parent::*/preceding-sibling::*[3]/descendant::*[2]")
					#
					# # 点击修改按钮
					# click("xpath", "//span[text()='变更']")
					#
					# # 切入修改的iframe窗体
					# switch_to("xpath", "//iframe[@id='modWin-iframe']")
					# sleep(1)
					#
					# # # 修改预计天数
					# # click("xpath", "//input[@id='detailgrid-plandays-0-input']")
					# # sleep(1)
					# # # 清空内容
					# # clear("xpath", "//input[@id='detailgrid-plandays-0-input']")
					# # sleep(1)
					# # # 预计天数
					# # input("xpath", "//input[@id='detailgrid-plandays-0-input']", "30")
					# # sleep(1)
					# #
					# # 点击保存按钮
					# click("xpath", "//span[text()='保存']")
					#
					# # 退出所有iframe窗体
					# switch_default()
					#
					# # 用隐式等待方法等页面出现提示框
					# implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					# print("现金投资计划编制，变更成功！")
					# logging.info("现金投资计划编制，变更成功！")
					# time.sleep(3)

					# 作废
					# 切入‘现金投资计划编制’的iframe窗体
					switch_to("xpath", "//iframe[@id='cashinvestmentbudget-tab-iframe']")

					click("xpath", "//div[@title='填报周期:2020-07-01']/parent::*/preceding-sibling::*[3]/descendant::*[2]")

					# 点击修改按钮
					click("xpath", "//span[text()='作废']")

					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'成功作废1条记录！')]")
					print("现金投资计划编制，作废成功！")
					logging.info("现金投资计划编制，作废成功！")
					time.sleep(3)
				# 第三笔，审核
				elif i == 3:
					# 切入‘现金投资计划编制’的iframe窗体
					switch_to("xpath", "//iframe[@id='cashinvestmentbudget-tab-iframe']")

					# 删除 # 勾选
					click("xpath", "//div[@title='填报周期:2020-07-01']/parent::*/preceding-sibling::*[3]/descendant::*[2]")

					# 点击审核按钮
					click("xpath", "//span[text()='审核']")

					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'成功审核1条记录')]")
					print("现金投资计划编制，第三次审核成功！")
					logging.info("现金投资计划编制，第三次审核成功！")
					time.sleep(3)

			# 退出所有iframe窗体
			switch_default()

			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='现金投资计划编制']/child::*[1]")

			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//span[@title='现金投资计划']")

			# 打印操作成功日志
			print("现金投资计划编制，操作成功!")
			logging.info("现金投资计划编制，操作成功!")
			time.sleep(2)
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("现金投资计划编制,失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)

		# 测试现金投资计划执行登记
		try:

			# 点击现金投资计划菜单
			click("xpath", "//span[@title='现金投资计划']")
			# 点击应付支票登记菜单

			click("xpath", "//span[@title='现金投资计划执行登记']")
			# 退出所有的iframe窗体
			switch_default()

			logging.info("开始测试现金投资计划执行登记功能")

			# 切入‘现金投资计划登记’的iframe窗体
			switch_to("xpath", "//iframe[@id='cashinvestexecute-tab-iframe']")

			# 点击查看
			# 用JS的方法点击放大镜
			js_click("xpath", "//span[@class='f-contrac-close']")
			sleep(1)

			# 填报周期
			click("xpath", "//input[@id='reportperiod-input']")
			sleep(1)
			input("xpath", "//input[@id='reportperiod-input']", "2020-07")
			sleep(1)

			# 点击查询
			click("xpath", "//span[text()='查询']")

			# 勾选
			click("xpath", "//div[@title='填报周期:2020-07-01']/parent::*/preceding-sibling::*[3]/descendant::*[2]")

			# 点击修改按钮
			click("xpath", "//span[text()='执行']")

			# 切入执行的iframe窗体
			switch_to("xpath", "//iframe[@id='executeWin-iframe']")
			sleep(1)

			# 输入发行日期
			# 点击发行日期的日历按钮
			js_click("xpath", "//span[@id='exedate-trigger']")
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
			switch_to("xpath", "//iframe[@id='cashinvestexecute-tab-iframe']")
			# 切入新增的iframe窗体
			switch_to("xpath", "//iframe[@id='executeWin-iframe']")
			sleep(1)

			# 点击保存按钮
			click("xpath", "//span[text()='执行']")

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'成功执行1条投资明细！')]")
			print("现金投资计划执行登记，执行成功！")
			logging.info("现金投资计划执行登记，执行成功！")
			time.sleep(3)

			# 切入‘现金投资计划登记’的iframe窗体
			switch_to("xpath", "//iframe[@id='cashinvestexecute-tab-iframe']")

			# 勾选
			click("xpath", "//div[@title='填报周期:2020-07-01']/parent::*/preceding-sibling::*[3]/descendant::*[2]")

			# 点击修改按钮
			click("xpath", "//span[text()='取消执行']")

			# 点击弹出框的OK键
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'成功取消执行1条')]")
			print("现金投资计划执行登记，取消执行成功！")
			logging.info("现金投资计划执行登记，取消执行成功！")
			time.sleep(3)

			# 退出所有iframe窗体
			switch_default()

			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='现金投资计划执行登记']/child::*[1]")

			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//span[@title='现金投资计划']")

			# 打印操作成功日志
			print("现金投资计划执行登记，操作成功!")
			logging.info("现金投资计划执行登记，操作成功!")
			time.sleep(2)
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("现金投资计划执行登记,失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		
		# 添加计划项目
		logging.info("开始测试资金计划的页面功能")
		# 将页面的滚动条滑动到‘资金计划’页面的地方
		js_gd("xpath", "//span[contains(text(),'资金计划')]")
		# 用JS的方法点击资金计划菜单按钮
		js_click("xpath", "//span[contains(text(),'资金计划')]")
		
		try:
			# 点击基础设置菜单
			click("xpath", "//li[@f_value='budgetSetting']/descendant-or-self::*[5]")
			# 点击计划项目菜单
			click("xpath", "//span[text()='计划项目']")
			# 退出所有iframe窗体
			switch_default()
			
			for i in range(1, 3):
				# 切入计划项目的iframe窗体
				switch_to("xpath", "//iframe[@id='budgetItem-tab-iframe']")
				logging.info("开始测试计划项目功能")
				
				# 用JS的方法点击新增按钮
				js_click("xpath", "//span[text()='新增']")
				
				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='addbudgetitemsWin-iframe']")
				sleep(1)
				
				if i == 1:
					# 输入代码
					input("xpath", "//input[@id='code']", "TestSrJhxm")
					sleep(1)
					
					# 输入名称
					input("xpath", "//input[@id='name']", "自动化测试收入计划项目")
					sleep(1)
					
					# 交易方向
					click("xpath", "//input[@id='combobox-input-moneyWay']")
					sleep(1)
					input("xpath", "//input[@id='combobox-input-moneyWay']", "收入")
					sleep(1)
					input_enter("xpath", "//input[@id='combobox-input-moneyWay']")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-moneyWay']")
					input_enter("xpath", "//input[@id='combobox-input-moneyWay']")
					sleep(1)
				if i == 2:
					# 输入代码
					input("xpath", "//input[@id='code']", "TestZcJhxm")
					sleep(1)
					
					# 输入名称
					input("xpath", "//input[@id='name']", "自动化测试支出计划项目")
					sleep(1)
					
					# 交易方向
					click("xpath", "//input[@id='combobox-input-moneyWay']")
					sleep(1)
					input("xpath", "//input[@id='combobox-input-moneyWay']", "支出")
					sleep(1)
					input_enter("xpath", "//input[@id='combobox-input-moneyWay']")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-moneyWay']")
					input_enter("xpath", "//input[@id='combobox-input-moneyWay']")
					sleep(1)
					
				# 组织
				click("xpath", "//input[@id='combobox-input-orgid']")
				sleep(1)
				input("xpath", "//input[@id='combobox-input-orgid']", "亚唐科技")
				sleep(1)
				input_enter("xpath", "//input[@id='combobox-input-orgid']")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-orgid']")
				input_enter("xpath", "//input[@id='combobox-input-orgid']")
				sleep(1)
				
				# 填报方式
				click("xpath", "//input[@id='combobox-input-fillreportmode']")
				sleep(1)
				input("xpath", "//input[@id='combobox-input-fillreportmode']", "汇总填报")
				sleep(1)
				input_enter("xpath", "//input[@id='combobox-input-fillreportmode']")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-fillreportmode']")
				input_enter("xpath", "//input[@id='combobox-input-fillreportmode']")
				sleep(1)
				
				# 设置单据对象
				js_click("xpath", "//span[text()='分配单据']/parent::*/descendant::*[3]")
				sleep(1)
				click("xpath", "//div[text()='选择全部']")
				sleep(1)
				
				# 点击设置交易类型
				click("xpath", "//span[text()='设置交易类型']")
				sleep(1)
				js_click("xpath", "//span[text()='分配交易类型']/parent::*/descendant::*[3]")
				sleep(1)
				click("xpath", "//div[text()='选择全部']")
				sleep(1)
				
				# 点击保存按钮
				click("xpath", "//span[text()='保存']")
				
				# 退出所有iframe窗体
				switch_default()
				
				# 用隐式等待方法等页面出现新增成功的提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				print("计划项目，保存成功！")
				time.sleep(3)
				
			switch_default()
			
			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='计划项目']/child::*[1]")
			
			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//li[@f_value='budgetSetting']/descendant-or-self::*[5]")
			
			# 打印操作成功日志
			print("计划项目，操作成功!")
			logging.info("计划项目，操作成功!")
			time.sleep(2)
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("计划项目操作失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		
		logging.info("开始测试投资管理的页面功能")
		# 将页面的滚动条滑动到‘资金结算管理’页面的地方
		# js_gd("xpath", "//span[contains(text(),'投资管理')]")
		# 用JS的方法点击资金结算管理菜单按钮
		js_click("xpath", "//span[contains(text(),'投资管理')]")
		
		#  测试投资项目-项目投资登记功能
		try:
			# 点击投资项目菜单
			click("xpath", "//span[@title='投资项目']")
			js_gd("xpath", "//span[@title='项目投资登记']")
			# 点击项目投资登记菜单
			click("xpath", "//span[@title='项目投资登记']")
			# 退出所有iframe窗体
			switch_default()

			for i in range(1, 3):
				# 切入项目投资登记的iframe窗体
				switch_to("xpath", "//iframe[@id='projectinvest-tab-iframe']")
				logging.info("开始测试项目投资登记功能")

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

				# 输入名称
				# 设置时间的变成存储，设置唯一性
				temp1 = time.strftime("%H%M%S")
				input("xpath", "//input[@id='name']", "TestProInv" + str(temp1))
				sleep(1)

				# 选择投资分类
				click("xpath", "//input[@id='combobox-input-investclassification']")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-investclassification']")
				input_enter("xpath", "//input[@id='combobox-input-investclassification']")
				sleep(1)

				# 选择收入计划项目
				click("xpath", "//input[@id='combobox-input-recbudgetitemid']")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-recbudgetitemid']")
				input_enter("xpath", "//input[@id='combobox-input-recbudgetitemid']")
				sleep(1)

				# 选择支出计划项目
				click("xpath", "//input[@id='combobox-input-paybudgetitemid']")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-paybudgetitemid']")
				input_enter("xpath", "//input[@id='combobox-input-paybudgetitemid']")
				sleep(1)
				# 选择工程项目
				click("xpath", "//input[@id='combobox-input-projectitemid']")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-projectitemid']")
				input_enter("xpath", "//input[@id='combobox-input-projectitemid']")
				sleep(1)

				# 点击附件信息
				click("xpath", "//span[text()='附件信息']")
				sleep(1)

				# 上传附件
				upload_click("xpath", "//div[@class='webuploader-pick']/parent::*/descendant::*[4]", 'e:', '"data.txt"')

				sleep(5)

				# 点击保存按钮
				click("xpath", "//span[text()='保存']")

				# 退出所有iframe窗体
				switch_default()

				# 用隐式等待方法等页面出现新增成功的提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				print("项目投资登记功能，保存成功！")
				time.sleep(3)

				if i == 1:

					# 切入项目投资登记的iframe窗体
					switch_to("xpath", "//iframe[@id='projectinvest-tab-iframe']")
					sleep(1)

					# 点击查看
					# 用JS的方法点击放大镜
					js_click("xpath", "//span[@class='f-contrac-close']")
					sleep(1)

					# 输入名称
					input("xpath", "//input[@id='namelrlike']", "TestProInv")
					sleep(1)

					# 点击查询
					click("xpath", "//span[text()='查询']")
					sleep(1)

					# 勾选
					click("xpath", "//div[contains(text(),'TestProInv')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")
					sleep(1)

					click("xpath", "//span[text()='删除']")
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现删除的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("项目投资登记，删除成功！")
					time.sleep(3)

			# 修改功能
			# 切入项目投资登记的iframe窗体
			switch_to("xpath", "//iframe[@id='projectinvest-tab-iframe']")
			sleep(1)

			# 勾选
			click("xpath", "//div[contains(text(),'TestProInv')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")
			sleep(1)

			# 点击修改按钮
			click("xpath", "//span[text()='修改']")
			sleep(1)

			# 切入新增的iframe窗体
			switch_to("xpath", "//iframe[@id='modWin-iframe']")
			sleep(1)

			# 备注框中填入值
			input("xpath", "//textarea[@id='description']", "自动化测试项目投资登记备注框修改")
			sleep(1)

			# 点击保存按钮
			click("xpath", "//span[text()='保存']")

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功')]")
			print("项目投资登记，修改成功！")
			time.sleep(3)

			# 切入项目投资登记的iframe窗体
			switch_to("xpath", "//iframe[@id='projectinvest-tab-iframe']")
			sleep(1)

			# 勾选
			click("xpath", "//div[contains(text(),'TestProInv')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")
			sleep(1)

			# 点击审核按钮
			click("xpath", "//span[text()='审核']")

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功')]")
			print("项目投资登记，第一次审核成功！")
			logging.info("项目投资登记，第一次审核成功！")
			time.sleep(3)

			# 取消审核
			# 切入项目投资登记的iframe窗体
			switch_to("xpath", "//iframe[@id='projectinvest-tab-iframe']")
			sleep(1)

			# 勾选
			click("xpath", "//div[contains(text(),'TestProInv')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")
			sleep(1)

			# 用JS方便点击‘审核’按钮旁边的倒三角形
			js_click("xpath", "//span[text()='审核']/parent::*/following-sibling::*/child::*")
			sleep(1)

			# 点击取消送审按钮
			js_click("xpath", "//a[contains(text(),'取消审核')]")
			sleep(1)

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("项目投资登记，取消审核成功！")
			logging.info("项目投资登记，取消审核成功！")
			time.sleep(3)

			# 切入项目投资登记的iframe窗体
			switch_to("xpath", "//iframe[@id='projectinvest-tab-iframe']")
			sleep(1)

			# 勾选
			click("xpath", "//div[contains(text(),'TestProInv')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")
			sleep(1)

			# 点击审核按钮
			click("xpath", "//span[text()='审核']")

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("项目投资登记，审核成功！")
			logging.info("项目投资登记，审核成功！")
			time.sleep(3)

			# 作废功能
			switch_to("xpath", "//iframe[@id='projectinvest-tab-iframe']")
			sleep(1)

			# 勾选
			click("xpath", "//div[contains(text(),'TestProInv')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")
			sleep(1)

			# 点击生按钮
			click("xpath", "//span[text()='作废']")
			sleep(1)

			# 点击弹出框的OK键
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("项目投资登记，成功作废1条!！")
			time.sleep(3)

			switch_default()

			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='项目投资登记']/child::*[1]")

			# 打印操作成功日志
			print("项目投资登记，操作成功!")
			logging.info("项目投资登记，操作成功!")
			time.sleep(2)

		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("项目投资登记操作失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		
		# 专户理财--资产管理
		try:
			# 点击专户理财菜单
			click("xpath", "//span[@title='专户理财']")
			# 点击资产管理菜单
			click("xpath", "//span[@title='资产管理']")
			# 退出所有的iframe窗体
			switch_default()
			
			logging.info("开始测试资产管理功能")
			for i in range(1, 4):
				# 切入‘资产管理’的iframe窗体
				switch_to("xpath", "//iframe[@id='assetsManage-tab-iframe']")
				
				# 用JS的方法点击新增按钮
				js_click("xpath", "//span[text()='新增']")
				
				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='addWin-iframe']")
				sleep(1)
				
				# 投资品种
				click("xpath", "//input[@id='combobox-input-investvarietys']")
				sleep(1)
				input_enter("xpath", "//input[@id='combobox-input-investvarietys']")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-investvarietys']")
				input_enter("xpath", "//input[@id='combobox-input-investvarietys']")
				sleep(1)
				
				# 投资产品
				click("xpath", "//input[@id='combobox-input-investproductid']")
				sleep(1)
				input_enter("xpath", "//input[@id='combobox-input-investproductid']")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-investproductid']")
				input_enter("xpath", "//input[@id='combobox-input-investproductid']")
				sleep(1)
				
				# 资产类别
				input("xpath", "//input[@id='assetscategory']", "自动化测试资产")
				sleep(1)
				
				# 资产名称
				input("xpath", "//input[@id='name']", "TestAssets")
				sleep(1)
				
				# 币种
				click("xpath", "//input[@id='combobox-input-currencyid']")
				sleep(1)
				input("xpath", "//input[@id='combobox-input-currencyid']", "CNY")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-currencyid']")
				input_enter("xpath", "//input[@id='combobox-input-currencyid']")
				sleep(1)
				
				# 票面利率
				click("xpath", "//input[@id='couponrate-input']")
				sleep(1)
				# 清空内容
				clear("xpath", "//input[@id='couponrate-input']")
				sleep(1)
				# 输入金额
				input("xpath", "//input[@id='couponrate-input']", "20")
				sleep(1)
				
				# 输入购买日
				today = date.today()
				begin_date = today - timedelta(days=20)
				click("xpath", "//input[@id='tradedate-input']")
				sleep(1)
				clear("xpath", "//input[@id='tradedate-input']")
				sleep(1)
				input("xpath", "//input[@id='tradedate-input']", str(begin_date))
				# 模拟回车键
				keyDown('enter')
				keyUp('enter')
				time.sleep(1)
				
				# 输入起息日
				today = date.today()
				begin_date = today - timedelta(days=20)
				click("xpath", "//input[@id='intereststartdate-input']")
				sleep(1)
				clear("xpath", "//input[@id='intereststartdate-input']")
				sleep(1)
				input("xpath", "//input[@id='intereststartdate-input']", str(begin_date))
				# 模拟回车键
				keyDown('enter')
				keyUp('enter')
				time.sleep(1)
				
				# 输入到期日
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
				
				# 份额
				click("xpath", "//input[@id='buyshare-input']")
				sleep(1)
				# 清空内容
				clear("xpath", "//input[@id='buyshare-input']")
				sleep(1)
				# 输入金额
				input("xpath", "//input[@id='buyshare-input']", "20")
				sleep(1)
				
				# 单价
				click("xpath", "//input[@id='price-input']")
				sleep(1)
				# 清空内容
				clear("xpath", "//input[@id='price-input']")
				sleep(1)
				# 输入金额
				input("xpath", "//input[@id='price-input']", "200")
				sleep(1)
				
				# 缺少附件上传
				
				# 点击保存按钮
				click("xpath", "//span[text()='保存']")
				
				# 退出所有iframe窗体
				switch_default()
				
				# 用隐式等待方法等页面出现提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				print("资产管理第%s次新增成功" % i)
				logging.info("资产管理第%s次新增成功" % i)
				time.sleep(3)
				
				# 第一笔，就先修改，再删除新建的‘资产管理’
				if i == 1:
					# 切入‘资产管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='assetsManage-tab-iframe']")
					
					# 点击查看
					# 用JS的方法点击放大镜
					js_click("xpath", "//span[@class='f-contrac-close']")
					sleep(1)
					
					# 资产名称
					input("xpath", "//input[@id='name']", "TestAssets")
					sleep(1)
					
					# 点击查询
					click("xpath", "//span[text()='查询']")
					
					# 修改 # 勾选
					click("xpath", "//div[@title='资产名称:TestAssets']/parent::*/preceding-sibling::*[3]/descendant::*[2]")
					
					# 点击修改按钮
					click("xpath", "//span[text()='修改']")
					sleep(1)
					
					# 切入修改的iframe窗体
					switch_to("xpath", "//iframe[@id='editWin-iframe']")
					print("进入修改窗体")
					sleep(1)
					
					implici_wait("xpath", "//span[contains(text(),'保存')]")
					
					# 备注框中输入新内容
					input("xpath", "//textarea[@id='description']", "自动化测试理财合同修改备注框")
					sleep(1)
					
					# 点击保存按钮
					click("xpath", "//span[text()='保存']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("资产管理，修改成功！")
					logging.info("资产管理，修改成功！")
					time.sleep(3)
					
					# 第一次审核
					# 切入‘资产管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='assetsManage-tab-iframe']")
					
					# 审核 # 勾选
					click("xpath", "//div[@title='资产名称:TestAssets']/parent::*/preceding-sibling::*[3]/descendant::*[2]")
					
					# 点击审核按钮
					click("xpath", "//span[text()='审核']")
					
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'成功审核1条记录')]")
					print("资产管理，第一次审批成功！")
					logging.info("资产管理，第一次审批成功！")
					time.sleep(3)
					
					switch_to("xpath", "//iframe[@id='assetsManage-tab-iframe']")
					
					# 审核 # 勾选
					click("xpath", "//div[@title='资产名称:TestAssets']/parent::*/preceding-sibling::*[3]/descendant::*[2]")
					
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
					print("资产管理，取消审核成功！")
					logging.info("资产管理，取消审核成功！")
					time.sleep(3)
					
					# 切入‘理财合同’的iframe窗体
					switch_to("xpath", "//iframe[@id='assetsManage-tab-iframe']")
					
					# 审核 # 勾选
					click("xpath", "//div[@title='资产名称:TestAssets']/parent::*/preceding-sibling::*[3]/descendant::*[2]")
					
					# 点击删除按钮
					click("xpath", "//span[text()='删除']")
					
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现删除的提示框
					implici_wait("xpath", "//span[contains(text(),'成功删除1条记录！')]")
					print("资产管理，删除成功！")
					logging.info("资产管理，删除成功！")
					time.sleep(3)
				
				# 第二笔，先审核、再取消审核、再托收、再托收到账
				elif i == 2:
					
					# 第二次审核
					switch_to("xpath", "//iframe[@id='assetsManage-tab-iframe']")
					
					# 审核 # 勾选
					click("xpath", "//div[@title='资产名称:TestAssets']/parent::*/preceding-sibling::*[3]/descendant::*[2]")
					
					# 点击审核按钮
					click("xpath", "//span[text()='审核']")
					
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'成功审核1条记录')]")
					print("资产管理，第二次审批成功！")
					logging.info("资产管理，第二次审批成功！")
					time.sleep(3)
					
					# 资产管理买入
					# 切入‘资产管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='assetsManage-tab-iframe']")
					
					# 审核 # 勾选
					click("xpath", "//div[@title='资产名称:TestAssets']/parent::*/preceding-sibling::*[3]/descendant::*[2]")
					
					# 点击取消审核按钮
					click("xpath", "//span[text()='买入']")
					sleep(1)
					
					switch_to("xpath", "//iframe[@id='assetsTransactionWin-iframe']")
					
					# 输入赎回日期
					# 点击赎回日期的日历按钮
					js_click("xpath", "//span[@id='tradedate-trigger']")
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
					
					# 切入‘资产管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='assetsManage-tab-iframe']")
					# 切入买入的iframe窗体
					switch_to("xpath", "//iframe[@id='assetsTransactionWin-iframe']")
					
					# 交易份额
					click("xpath", "//input[@id='buyshare-input']")
					sleep(1)
					clear("xpath", "//input[@id='buyshare-input']")
					input("xpath", "//input[@id='buyshare-input']", "30")
					sleep(1)
					
					# 单价
					click("xpath", "//input[@id='price-input']")
					sleep(1)
					clear("xpath", "//input[@id='price-input']")
					input("xpath", "//input[@id='price-input']", "3000")
					sleep(1)
					
					# 点击保存按钮
					click("xpath", "//span[text()='保存']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("资产管理，买入成功！")
					logging.info("资产管理，买入成功！")
					time.sleep(3)
					
					# 资产管理卖出
					# 切入‘资产管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='assetsManage-tab-iframe']")
					
					# 审核 # 勾选
					click("xpath", "//div[@title='资产名称:TestAssets']/parent::*/preceding-sibling::*[3]/descendant::*[2]")
					
					# 点击卖出按钮
					click("xpath", "//span[text()='卖出']")
					sleep(1)
					
					switch_to("xpath", "//iframe[@id='assetsTransactionWin2-iframe']")
					
					# 输入赎回日期
					# 点击赎回日期的日历按钮
					js_click("xpath", "//span[@id='tradedate-trigger']")
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
					
					# 切入‘资产管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='assetsManage-tab-iframe']")
					# 切入买入的iframe窗体
					switch_to("xpath", "//iframe[@id='assetsTransactionWin2-iframe']")
					
					# 交易份额
					click("xpath", "//input[@id='buyshare-input']")
					sleep(1)
					clear("xpath", "//input[@id='buyshare-input']")
					input("xpath", "//input[@id='buyshare-input']", "30")
					sleep(1)
					
					# 单价
					click("xpath", "//input[@id='price-input']")
					sleep(1)
					clear("xpath", "//input[@id='price-input']")
					input("xpath", "//input[@id='price-input']", "3000")
					sleep(1)
					
					# 点击保存按钮
					click("xpath", "//span[text()='保存']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("资产管理，卖出成功！")
					logging.info("资产管理，卖出成功！")
					time.sleep(3)
				
				# 第三笔，变更然后作废
				elif i == 3:
					
					# 第三次审核
					# 切入‘资产管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='assetsManage-tab-iframe']")
					
					# 审核 # 勾选
					click("xpath", "//div[@title='资产名称:TestAssets']/parent::*/preceding-sibling::*[3]/descendant::*[2]")
					
					# 点击审核按钮
					click("xpath", "//span[text()='审核']")
					
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'成功审核1条记录')]")
					print("理财合同，第三次审批成功！")
					logging.info("理财合同，第三次审批成功！")
					time.sleep(3)
					
					# # 变更
					# # 切入‘资产管理’的iframe窗体
					# switch_to("xpath", "//iframe[@id='assetsManage-tab-iframe']")
					#
					# # 审核 # 勾选
					# click("xpath", "//div[@title='资产名称:TestAssets']/parent::*/preceding-sibling::*[3]/descendant::*[2]")
					#
					# # 点击审核按钮
					# click("xpath", "//span[text()='变更']")
					#
					# switch_to("xpath", "//iframe[@id='editWin-iframe']")
					# print("进入变更窗体")
					# sleep(2)
					#
					# # implici_wait("xpath", "//span[contains(text(),'保存')]")
					# # time.sleep(2)
					#
					# # # 备注框中输入新内容
					# # input("xpath", "//textarea[@id='description']", "自动化测试理财合同变更备注框")
					# # sleep(1)
					#
					# # 点击保存按钮
					# click("xpath", "//span[text()='保存']")
					#
					# # 退出所有iframe窗体
					# switch_default()
					#
					# # 用隐式等待方法等页面出现提示框
					# implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					# print("理财合同，变更成功！")
					# logging.info("理财合同，变更成功！")
					# time.sleep(3)
					#
					# 切入‘资产管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='assetsManage-tab-iframe']")
					
					# 审核 # 勾选
					click("xpath", "//div[@title='资产名称:TestAssets']/parent::*/preceding-sibling::*[3]/descendant::*[2]")
					
					# 点击审核按钮
					click("xpath", "//span[text()='作废']")
					
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'成功作废1条记录！')]")
					print("资产管理，作废成功！")
					logging.info("资产管理，作废成功！")
					time.sleep(3)
			
			# 退出所有iframe窗体
			switch_default()
			
			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='资产管理']/child::*[1]")
			
			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//span[@title='专户理财']")
			
			# 打印操作成功日志
			print("资产管理，操作成功!")
			logging.info("资产管理，操作成功!")
			time.sleep(2)
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("资产管理,失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		
		# 测试资产信息查看
		try:
			# 专户理财
			click("xpath", "//span[@title='专户理财']")
			# 点击资产管理菜单
			click("xpath", "//span[@title='资产信息查看']")
			# 退出所有的iframe窗体
			switch_default()
			logging.info("开始测试资产信息查看功能")
			
			# 切入‘资产信息查看’的iframe窗体
			switch_to("xpath", "//iframe[@id='assetsinfoview-tab-iframe']")
			
			# 点击查看
			# 用JS的方法点击放大镜
			js_click("xpath", "//span[@class='f-contrac-close']")
			sleep(1)
			
			# 输入资产名称
			input("xpath", "//input[@id='name']", "TestAssets")
			sleep(1)
			
			# 点击查询
			click("xpath", "//span[text()='查询']")
			
			# 审核 # 勾选
			click("xpath", "//div[@title='资产名称:TestAssets']/parent::*/preceding-sibling::*[3]/descendant::*[2]")
			sleep(1)
			
			click("xpath", "//span[text()='交易记录查看']")
			
			# 切入‘资产信息查看’的iframe窗体
			switch_to("xpath", "//iframe[@id='detailWin-iframe']")
			
			# 用隐式等待方法等页面出现预期数据：交易方向:赎回
			implici_wait("xpath", "//div[@title='交易方向:赎回']")
			print("资产信息查看成功！")
			time.sleep(3)
			
			# 退出所有iframe窗体
			switch_default()
			
			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='资产信息查看']/child::*[1]")
			
			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//span[@title='专户理财']")
			
			# 打印操作成功日志
			print("资产信息查看，操作成功!")
			logging.info("资产信息查看，操作成功!")
			time.sleep(2)
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("资产信息查看,失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		
		# # 测试投资管理--专户理财--净值信息维护
		try:
			# 	专户理财
			click("xpath", "//span[@title='专户理财']")
			# 点击资产管理菜单
			click("xpath", "//span[@title='净值信息维护']")
			# 退出所有iframe窗体
			switch_default()
			
			for i in range(1, 3):
				# 切入净值信息维护的iframe窗体
				switch_to("xpath", "//iframe[@id='networthmanage-tab-iframe']")
				logging.info("开始测试净值信息维护功能")
				
				# 用JS的方法点击新增按钮
				js_click("xpath", "//span[text()='新增']")
				
				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='addWin-iframe']")
				sleep(1)
				
				# 投资产品
				click("xpath", "//input[@id='combobox-input-productid']")
				sleep(1)
				input("xpath", "//input[@id='combobox-input-productid']", "自动化测试投资产品")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-productid']")
				input_enter("xpath", "//input[@id='combobox-input-productid']")
				sleep(1)
				
				# 输入到期日
				today = date.today()
				end_date = today + timedelta(days=20)
				click("xpath", "//input[@id='reportdate-input']")
				sleep(1)
				clear("xpath", "//input[@id='reportdate-input']")
				sleep(1)
				input("xpath", "//input[@id='reportdate-input']", str(end_date))
				# 模拟回车键
				# keyDown('enter')
				# keyUp('enter')
				time.sleep(1)
				
				# 输入净值
				click("xpath", "//input[@id='networth-input']")
				sleep(1)
				clear("xpath", "//input[@id='networth-input']")
				sleep(1)
				input("xpath", "//input[@id='networth-input']", "2000")
				sleep(1)
				
				# 描述框中填入值
				input("xpath", "//textarea[@id='description']", "自动化测试净值信息维护描述框")
				sleep(1)
				
				# 点击保存按钮
				click("xpath", "//span[text()='保存']")
				
				# 退出所有iframe窗体
				switch_default()
				
				# 用隐式等待方法等页面出现新增成功的提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				print("净值信息维护，保存成功！")
				time.sleep(3)
				
				if i == 1:
					# 切入净值信息维护的iframe窗体
					switch_to("xpath", "//iframe[@id='networthmanage-tab-iframe']")
					sleep(1)
					
					# 点击查看
					# 用JS的方法点击放大镜
					js_click("xpath", "//span[@class='f-contrac-close']")
					sleep(1)
					
					# 输入代码
					click("xpath", "//input[@id='combobox-input-productid']")
					sleep(1)
					input("xpath", "//input[@id='combobox-input-productid']", "自动化测试投资产品")
					sleep(1)
					click("xpath", "//div[@title='代码-名称:TestInvPro-自动化测试投资产品']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
					sleep(1)
					
					# 点击查询
					click("xpath", "//span[text()='查询']")
					sleep(1)
					
					# 勾选
					click("xpath",
					      "//div[@title='投资产品:TestInvPro-自动化测试投资产品']/parent::*/preceding-sibling::*[2]/descendant::*[2]")
					# 点击保存按钮
					
					click("xpath", "//span[text()='删除']")
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现删除的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("净值信息维护，删除成功！")
					time.sleep(3)
			
			# 修改功能
			# 切入净值信息维护的iframe窗体
			switch_to("xpath", "//iframe[@id='networthmanage-tab-iframe']")
			sleep(1)
			# 勾选
			click("xpath",
			      "//div[@title='投资产品:TestInvPro-自动化测试投资产品']/parent::*/preceding-sibling::*[2]/descendant::*[2]")
			
			# 点击修改按钮
			click("xpath", "//span[text()='修改']")
			sleep(1)
			
			# 切入新增的iframe窗体
			switch_to("xpath", "//iframe[@id='modWin-iframe']")
			sleep(1)
			
			# 描述框中填入值
			input("xpath", "//textarea[@id='description']", "自动化测试净值信息维护描述修改")
			sleep(1)
			
			# 点击保存按钮
			click("xpath", "//span[text()='保存']")
			
			# 退出所有iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功')]")
			print("净值信息维护，修改成功！")
			time.sleep(3)
			
			switch_default()
			
			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='净值信息维护']/child::*[1]")
			
			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//span[@title='专户理财']")
			
			# 打印操作成功日志
			print("净值信息维护，操作成功!")
			logging.info("净值信息维护，操作成功!")
			time.sleep(2)
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("净值信息维护操作失败！" + str(traceback.format_exc()))
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
