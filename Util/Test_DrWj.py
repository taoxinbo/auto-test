# encoding=utf-8
# @Time : 2020/8/14 14:49
# @Author : Mindy
# 此文件是测试系统文件导入功能，包含账户维护导入，离线账户导入，交易对手导入，支付限额导入
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


class Test_DrWj(unittest.TestCase):
	
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
		# login(G_Mys_Url, mindy, Password, "默认租户")
		# login(G_Mys_Url, mindy, Password, "亚唐科技")
		# login(G_Mys_Url, judy, Password, "默认租户")
		
		logging.info("开始测试账户资金监控的页面功能")
		# 将页面的滚动条滑动到‘票据管理’页面的地方
		js_gd("xpath", "//span[contains(text(),'账户资金监控')]")
		# 用JS的方法点击票据管理菜单按钮
		js_click("xpath", "//span[contains(text(),'账户资金监控')]")
		"""
		#  测试账户维护-导入功能
		# 测试账户生命周期--账户维护
		try:
			# 点击账户生命周期'菜单
			click("xpath", "//span[text()='账户生命周期']")
			# 点击账户申请菜单
			click("xpath", "//span[text()='账户维护']")
			# 退出所有iframe窗体
			switch_default()

			for i in range(1, 2):
				# 切入账户维护的iframe窗体
				switch_to("xpath", "//iframe[@id='bankAccounts-tab-iframe']")
				logging.info("开始测试账户维护单币种账户功能")
				sleep(1)

				# 进入单币种账户的iframe 窗体
				switch_to("xpath", "//iframe[@id='subTabOne-iframe']")

				# 用JS的方法点击列表导入
				js_click("xpath", "//div[@title='列表导入']")

				# 进入导入详情页面窗体
				switch_to("xpath", "//iframe[@id='importDataWin-iframe']")
				sleep(1)

				# 点击下一步
				click("xpath", "//span[text()='下一步']")
				sleep(1)
	
				# 进入上传详情页窗体
				switch_to("xpath", "//iframe[@id='loadNextWin-iframe']")
				sleep(1)

				# 选择附件上传
				upload_click("xpath", "//div[text()='选择文件']/parent::*[1]/descendant::*[4]", 'D:\Download\Account _Maintenance', '"account.xls"')
				sleep(2)

				# 点击保存按钮
				click("xpath", "//span[text()='上传']")

				# 退出所有iframe窗体
				switch_default()

				# 用隐式等待方法等页面出现新增成功的提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功,共导入1条数据，成功1条，失败0条，未处理0条。')]")
				print("单币种账户维护导入，保存成功！")
				time.sleep(3)

				switch_to("xpath", "//iframe[@id='bankAccounts-tab-iframe']")
				sleep(1)

				# 进入单币种账户的iframe 窗体
				switch_to("xpath", "//iframe[@id='subTabOne-iframe']")

				# 点击关闭当前页面
				click("xpath", "//div[@id='f-win-title-importDataWin']/descendant::*[2]")
				sleep(1)

				switch_default()

				# 删除功能
				# 切入单币种账户维护导入的iframe窗体
				switch_to("xpath", "//iframe[@id='bankAccounts-tab-iframe']")
				sleep(1)

				# 进入单币种账户的iframe 窗体
				switch_to("xpath", "//iframe[@id='subTabOne-iframe']")

				# 点击查看
				# 用JS的方法点击放大镜
				js_click("xpath", "//span[@class='f-contrac-close']")
				sleep(1)

				# 银行账号
				input("xpath", "//input[@id='accountnumber']", "DRZH00001")
				sleep(1)

				# 点击查询
				click("xpath", "//span[text()='查询']")

				# 勾选
				click("xpath", "//div[contains(text(),'DRZH00001')]/parent::*/preceding-sibling::*[3]/descendant::*[2]")
				sleep(1)

				# 点击删除按钮
				click("xpath", "//span[text()='删除']")
				sleep(1)

				# 点击弹出框的OK键
				click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

				# 退出所有iframe窗体
				switch_default()

				# 用隐式等待方法等页面出现删除的提示框
				implici_wait("xpath", "//span[contains(text(),'账户DRZH00001，删除成功！')]")
				print("单币种账户维护导入，删除成功！")
				time.sleep(3)

				switch_default()

				switch_to("xpath", "//iframe[@id='bankAccounts-tab-iframe']")
				logging.info("开始测试账户维护功能")
				sleep(1)

				# 切入多币种账户
				click("xpath", "//span[text()='多币种账户']")
				sleep(1)

				switch_to("xpath", "//iframe[@id='subTabTwo-iframe']")

				# 用JS的方法点击列表导入
				js_click("xpath", "//div[@title='列表导入']")

				# 进入导入详情页面窗体
				switch_to("xpath", "//iframe[@id='importDataWin-iframe']")
				sleep(1)

				# 点击下一步
				click("xpath", "//span[text()='下一步']")
				sleep(1)
		
				# 进入上传详情页窗体
				switch_to("xpath", "//iframe[@id='loadNextWin-iframe']")
				sleep(1)

				# 选择附件上传
				upload_click("xpath", "//div[text()='选择文件']/parent::*[1]/descendant::*[4]", 'D:\Download\Account _Maintenance', '"account1.xls"')
				sleep(2)

				# 点击保存按钮
				click("xpath", "//span[text()='上传']")

				# 退出所有iframe窗体
				switch_default()

				# 用隐式等待方法等页面出现新增成功的提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功,共导入1条数据，成功1条，失败0条，未处理0条。')]")
				print("多币种账户维护导入，保存成功！")
				time.sleep(3)

				switch_to("xpath", "//iframe[@id='bankAccounts-tab-iframe']")
				logging.info("开始测试账户维护功能")
				sleep(1)

				# 切入多币种账户
				click("xpath", "//span[text()='多币种账户']")
				sleep(1)

				switch_to("xpath", "//iframe[@id='subTabTwo-iframe']")

				# 点击关闭当前页面
				click("xpath", "//div[@id='f-win-title-importDataWin']/descendant::*[2]")
				sleep(1)

				switch_default()

				# 删除功能
				switch_to("xpath", "//iframe[@id='bankAccounts-tab-iframe']")
				logging.info("开始测试账户维护功能")
				sleep(1)

				# 切入多币种账户
				click("xpath", "//span[text()='多币种账户']")
				sleep(1)

				switch_to("xpath", "//iframe[@id='subTabTwo-iframe']")

				# 点击查看
				# 用JS的方法点击放大镜
				js_click("xpath", "//span[@class='f-contrac-close']")
				sleep(1)

				# 银行账号
				input("xpath", "//input[@id='accountnumber']", "DRZH00002")
				sleep(1)

				# 点击查询
				click("xpath", "//span[text()='查询']")

				# 勾选
				click("xpath", "//div[contains(text(),'DRZH00002')]/parent::*/preceding-sibling::*[2]/descendant::*[2]")
				sleep(1)

				# 点击删除按钮
				click("xpath", "//span[text()='删除']")
				sleep(1)

				# 点击弹出框的OK键
				click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

				# 退出所有iframe窗体
				switch_default()

				# 用隐式等待方法等页面出现删除的提示框
				implici_wait("xpath", "//span[contains(text(),'账户DRZH00002，删除成功！')]")
				print("多币种账户维护导入，删除成功！")
				time.sleep(3)

				# 用JS的方法关闭当前页面
				js_click("xpath", "//a[@title='账户维护']/child::*[1]")

				# 再次点击基础设置菜单，使之关闭
				js_click("xpath", "//span[contains(text(),'账户资金监控')]")

				# 打印操作成功日志
				print("账户维护导入，操作成功!")
				logging.info("账户维护导入，操作成功!")
				time.sleep(2)

		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("账户维护导入操作失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		
		# 离线账户维护文件导入
		# 测试明细维护文件导入
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
				
				# 用JS的方法点击列表导入
				js_click("xpath", "//div[@title='列表导入']")
				
				# 进入导入详情页面窗体
				switch_to("xpath", "//iframe[@id='importDataWin-iframe']")
				sleep(1)
				
				# 选择导入文件类型
				click("xpath", "//input[@id='combobox-input-businessid']")
				sleep(1)
				input("xpath", "//input[@id='combobox-input-businessid']", "离线信息导入")
				sleep(1)
				input_enter("xpath", "//input[@id='combobox-input-businessid']")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-businessid']")
				sleep(1)
				input_enter("xpath", "//input[@id='combobox-input-businessid']")
				sleep(1)
				
				# 点击下一步
				click("xpath", "//span[text()='下一步']")
				sleep(1)
				
				# 进入上传详情页窗体
				switch_to("xpath", "//iframe[@id='loadNextWin-iframe']")
				sleep(1)
				
				# 选择附件上传
				upload_click("xpath", "//div[text()='选择文件']/parent::*[1]/descendant::*[4]", 'D:\Download\Offline_Account_Maintenance', '"banktransaction.xls"')
				sleep(2)
				
				# 点击保存按钮
				click("xpath", "//span[text()='上传']")
				
				# 退出所有iframe窗体
				switch_default()
				
				# 用隐式等待方法等页面出现新增成功的提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功,共导入1条数据，成功1条，失败0条，未处理0条。')]")
				print("明细维护导入，保存成功！")
				time.sleep(3)
				
				switch_to("xpath", "//iframe[@id='bankTransNonDirect-tab-iframe']")
				sleep(1)
				
				# 切入明细维护
				switch_to("xpath", "//iframe[@id='subTab1-iframe']")
				sleep(1)
				
				# 点击关闭当前页面
				click("xpath", "//div[@id='f-win-title-importDataWin']/descendant::*[2]")
				sleep(1)
				
				switch_default()
				
				# 删除功能
				switch_to("xpath", "//iframe[@id='bankTransNonDirect-tab-iframe']")
				sleep(1)
				
				# 切入明细维护
				switch_to("xpath", "//iframe[@id='subTab1-iframe']")
				sleep(1)
				
				# # 点击查看
				# # 用JS的方法点击放大镜
				# js_click("xpath", "//span[@class='f-contrac-close']")
				# sleep(1)

				# # 银行账号
				# input("xpath", "//input[@id='accountnumber']", "DRZH00001")
				# sleep(1)
				#
				# # 点击查询
				# click("xpath", "//span[text()='查询']")
				
				# 勾选
				click("xpath", "//div[contains(text(),'2020103834')]/parent::*/preceding-sibling::*[2]/descendant::*[2]")
				sleep(1)
				
				# 点击删除按钮
				click("xpath", "//span[text()='删除']")
				sleep(1)
				
				# 点击弹出框的OK键
				click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
				
				# 退出所有iframe窗体
				switch_default()
				
				# 用隐式等待方法等页面出现删除的提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功')]")
				print("明细维护导入，删除成功！")
				time.sleep(3)
				
				switch_default()
				# 开始测试余额维护
				# 切入‘离线账户维护’的iframe窗体
				# 余额维护页面
				switch_to("xpath", "//iframe[@id='bankTransNonDirect-tab-iframe']")
				sleep(1)
				
				click("xpath", "//span[text()='余额维护']")
				
				# 切入明细维护
				switch_to("xpath", "//iframe[@id='subTab2-iframe']")
				sleep(1)
				logging.info("开始测试离线账户余额维护功能")
				
				# 用JS的方法点击列表导入
				js_click("xpath", "//div[@title='列表导入']")
				
				# 进入导入详情页面窗体
				switch_to("xpath", "//iframe[@id='importDataWin-iframe']")
				sleep(1)
				
				# 点击下一步
				click("xpath", "//span[text()='下一步']")
				sleep(1)
				
				# 进入上传详情页窗体
				switch_to("xpath", "//iframe[@id='loadNextWin-iframe']")
				sleep(1)
				
				# 选择附件上传
				upload_click("xpath", "//div[text()='选择文件']/parent::*[1]/descendant::*[4]", 'D:\Download\Offline_Account_Maintenance', '"undirectaccountbalance.xlsx"')
				sleep(2)
				
				# 点击保存按钮
				click("xpath", "//span[text()='上传']")
				
				# 退出所有iframe窗体
				switch_default()
				
				# 用隐式等待方法等页面出现新增成功的提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功,共导入1条数据，成功1条，失败0条，未处理0条。')]")
				print("余额维护导入，保存成功！")
				time.sleep(3)
				
				switch_to("xpath", "//iframe[@id='bankTransNonDirect-tab-iframe']")
				sleep(1)
				
				click("xpath", "//span[text()='余额维护']")
				
				# 切入明细维护
				switch_to("xpath", "//iframe[@id='subTab2-iframe']")
				
				# 点击关闭当前页面
				click("xpath", "//div[@id='f-win-title-importDataWin']/descendant::*[2]")
				sleep(1)
				
				switch_default()
				
				# 删除功能
				switch_to("xpath", "//iframe[@id='bankTransNonDirect-tab-iframe']")
				sleep(1)
				
				click("xpath", "//span[text()='余额维护']")
				
				# 切入明细维护
				switch_to("xpath", "//iframe[@id='subTab2-iframe']")
				sleep(1)
				
				# # 点击查看
				# # 用JS的方法点击放大镜
				# js_click("xpath", "//span[@class='f-contrac-close']")
				# sleep(1)
				
				# # 银行账号
				# input("xpath", "//input[@id='accountnumber']", "DRZH00001")
				# sleep(1)
				#
				# # 点击查询
				# click("xpath", "//span[text()='查询']")
				
				# 勾选
				click("xpath", "//div[contains(text(),'2020103834')]/parent::*/preceding-sibling::*[3]/descendant::*[2]")
				sleep(1)
				
				# 点击删除按钮
				click("xpath", "//span[text()='删除']")
				sleep(1)
				
				# 点击弹出框的OK键
				click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
				
				# 退出所有iframe窗体
				switch_default()
				
				# 用隐式等待方法等页面出现删除的提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功')]")
				print("余额维护导入，删除成功！")
				time.sleep(3)
				
				# 开始测试冻结明细维护导入
				# 开始测试余额维护
				# 切入‘离线账户维护’的iframe窗体
				# 余额维护页面
				switch_to("xpath", "//iframe[@id='bankTransNonDirect-tab-iframe']")
				sleep(1)
				
				# 点击冻结明细维护文本
				click("xpath", "//span[text()='冻结明细维护']")
				sleep(1)
				
				# 切入明细维护
				switch_to("xpath", "//iframe[@id='subTab4-iframe']")
				sleep(1)
				logging.info("开始测试离线账户余额维护功能")
				
				# 用JS的方法点击列表导入
				js_click("xpath", "//div[@title='列表导入']")
				
				# 进入导入详情页面窗体
				switch_to("xpath", "//iframe[@id='importDataWin-iframe']")
				sleep(1)
				
				# 点击下一步
				click("xpath", "//span[text()='下一步']")
				sleep(1)
				
				# 进入上传详情页窗体
				switch_to("xpath", "//iframe[@id='loadNextWin-iframe']")
				sleep(1)
				
				# 选择附件上传
				upload_click("xpath", "//div[text()='选择文件']/parent::*[1]/descendant::*[4]", 'D:\Download\Offline_Account_Maintenance', '"bankfreezetrans.xlsx"')
				sleep(2)
				
				# 点击保存按钮
				click("xpath", "//span[text()='上传']")
				
				# 退出所有iframe窗体
				switch_default()
				
				# 用隐式等待方法等页面出现新增成功的提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功,共导入1条数据，成功1条，失败0条，未处理0条。')]")
				print("冻结明细维护导入，保存成功！")
				time.sleep(3)
				
				switch_to("xpath", "//iframe[@id='bankTransNonDirect-tab-iframe']")
				sleep(1)
				
				# 点击冻结明细维护文本
				click("xpath", "//span[text()='冻结明细维护']")
				sleep(1)
				
				# 切入明细维护
				switch_to("xpath", "//iframe[@id='subTab4-iframe']")
				sleep(1)
				
				# 点击关闭当前页面
				click("xpath", "//div[@id='f-win-title-importDataWin']/descendant::*[2]")
				sleep(1)
				
				switch_default()
				
				# 删除功能
				switch_to("xpath", "//iframe[@id='bankTransNonDirect-tab-iframe']")
				sleep(1)
				
				# 点击冻结明细维护文本
				click("xpath", "//span[text()='冻结明细维护']")
				sleep(1)
				
				# 切入明细维护
				switch_to("xpath", "//iframe[@id='subTab4-iframe']")
				sleep(1)
				
				# # 点击查看
				# # 用JS的方法点击放大镜
				# js_click("xpath", "//span[@class='f-contrac-close']")
				# sleep(1)
				
				# # 银行账号
				# input("xpath", "//input[@id='accountnumber']", "DRZH00001")
				# sleep(1)
				#
				# # 点击查询
				# click("xpath", "//span[text()='查询']")
				
				# 勾选
				click("xpath", "//div[contains(text(),'2020103834')]/parent::*/preceding-sibling::*[2]/descendant::*[2]")
				sleep(1)
				
				# 点击删除按钮
				click("xpath", "//span[text()='删除']")
				sleep(1)
				
				# 点击弹出框的OK键
				click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
				
				# 退出所有iframe窗体
				switch_default()
				
				# 用隐式等待方法等页面出现删除的提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功')]")
				print("冻结明细维护导入，删除成功！")
				time.sleep(3)
				
				# 用JS的方法关闭当前页面
				js_click("xpath", "//a[@title='离线账户维护']/child::*[1]")
				
				# 再次点击基础设置菜单，使之关闭
				js_click("xpath", "//span[contains(text(),'账户资金监控')]")
				
				# 打印操作成功日志
				print("离线账户维护导入，操作成功!")
				logging.info("离线账户维护导入，操作成功!")
				time.sleep(2)
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("离线账户维护导入操作失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		"""
		logging.info("开始测试资金结算管理页面的导入功能")
		# 将页面的滚动条滑动到‘资金结算管理’页面的地方
		# js_gd("xpath", "//span[contains(text(),'资金结算管理')]")
		# 用JS的方法点击资金结算管理菜单按钮
		js_click("xpath", "//span[contains(text(),'资金结算管理')]")
		
		# #  测试资金结算管理-交易对手导入功能
		# try:
		# 	# 点击基础设置菜单
		# 	click("xpath", "//li[@f_value='settlementSetting']/descendant-or-self::*[5]")
		# 	# 点击支票用途菜单
		# 	click("xpath", "//span[text()='交易对手']")
		# 	# 退出所有iframe窗体
		# 	switch_default()
		#
		# 	for i in range(1, 2):
		# 		# 切入交易对手的iframe窗体
		# 		switch_to("xpath", "//iframe[@id='counterparty-tab-iframe']")
		# 		logging.info("开始测试交易对手导入功能")
		#
		# 		# 用JS的方法点击列表导入
		# 		js_click("xpath", "//div[@title='列表导入']")
		#
		# 		# 进入导入详情页面窗体
		# 		switch_to("xpath", "//iframe[@id='importDataWin-iframe']")
		# 		sleep(1)
		#
		# 		# 点击下一步
		# 		click("xpath", "//span[text()='下一步']")
		# 		sleep(1)
		#
		# 		# 进入上传详情页窗体
		# 		switch_to("xpath", "//iframe[@id='loadNextWin-iframe']")
		# 		sleep(1)
		#
		# 		# 选择附件上传
		# 		upload_click("xpath", "//div[text()='选择文件']/parent::*[1]/descendant::*[4]", 'D:\Download\CounterParty', '"counterparty.xls"')
		# 		sleep(2)
		#
		# 		# 点击保存按钮
		# 		click("xpath", "//span[text()='上传']")
		#
		# 		# 退出所有iframe窗体
		# 		switch_default()
		#
		# 		# 用隐式等待方法等页面出现新增成功的提示框
		# 		implici_wait("xpath", "//span[contains(text(),'操作成功,共导入1条数据，成功1条，失败0条，未处理0条。')]")
		# 		print("交易对手入，保存成功！")
		# 		time.sleep(3)
		#
		# 		switch_to("xpath", "//iframe[@id='counterparty-tab-iframe']")
		#
		# 		# 点击关闭当前页面
		# 		click("xpath", "//div[@id='f-win-title-importDataWin']/descendant::*[2]")
		# 		sleep(1)
		#
		# 		switch_default()
		#
		# 		# 删除功能
		# 		switch_to("xpath", "//iframe[@id='counterparty-tab-iframe']")
		#
		# 		# 点击查看
		# 		# 用JS的方法点击放大镜
		# 		js_click("xpath", "//span[@class='f-contrac-close']")
		# 		sleep(1)
		#
		# 		# 代码
		# 		input("xpath", "//input[@id='name']", "集团公司1")
		# 		sleep(1)
		#
		# 		# 点击查询
		# 		click("xpath", "//span[text()='查询']")
		# 		sleep(1)
		#
		# 		# 勾选
		# 		click("xpath", "//span[text()='集团公司1']/ancestor::*[8]/descendant::*[20]")
		# 		sleep(1)
		#
		# 		# 点击删除按钮
		# 		click("xpath", "//span[text()='删除']")
		# 		sleep(1)
		#
		# 		# 点击弹出框的OK键
		# 		click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
		#
		# 		# 退出所有iframe窗体
		# 		switch_default()
		#
		# 		# 用隐式等待方法等页面出现删除的提示框
		# 		implici_wait("xpath", "//span[contains(text(),'操作成功')]")
		# 		print("交易对手导入，删除成功！")
		# 		time.sleep(3)
		#
		# 		# 用JS的方法关闭当前页面
		# 		js_click("xpath", "//a[@title='交易对手']/child::*[1]")
		#
		# 		# 再次点击基础设置菜单，使之关闭
		# 		click("xpath", "//li[@f_value='settlementSetting']/descendant-or-self::*[5]")
		#
		# 		# 打印操作成功日志
		# 		print("交易对手，操作成功!")
		# 		logging.info("交易对手，操作成功!")
		# 		time.sleep(2)
		#
		# except Exception as err:
		# 	# 发生其他异常时，打印异常堆栈信息
		# 	print(traceback.print_exc())
		# 	logging.debug("交易对手操作失败！" + str(traceback.format_exc()))
		# 	# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
		# 	dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
		# 	dir_path = make_current_hour_dir(dir_path + "\\")
		# 	pic_path = os.path.join(dir_path, get_current_time() + ".png")
		# 	capture(pic_path)
		
		#  测试资金结算管理-支付限额导入功能
		try:
			# 点击基础设置菜单
			click("xpath", "//li[@f_value='settlementSetting']/descendant-or-self::*[5]")
			# 点击支付限额菜单
			click("xpath", "//span[text()='支付限额']")
			# 退出所有iframe窗体
			switch_default()
			
			for i in range(1, 2):
				# 切入支付限额的iframe窗体
				switch_to("xpath", "//iframe[@id='limitAmount-tab-iframe']")
				logging.info("开始测试支付限额导入功能")
				
				# 用JS的方法点击列表导入
				js_click("xpath", "//div[@title='列表导入']")
				
				# 进入导入详情页面窗体
				switch_to("xpath", "//iframe[@id='importDataWin-iframe']")
				sleep(1)
				
				# 点击下一步
				click("xpath", "//span[text()='下一步']")
				sleep(1)
				
				# 进入上传详情页窗体
				switch_to("xpath", "//iframe[@id='loadNextWin-iframe']")
				sleep(1)
				
				# 选择附件上传
				upload_click("xpath", "//div[text()='选择文件']/parent::*[1]/descendant::*[4]", 'D:\Download\Limitamounts', '"limitamounts.xls"')
				sleep(2)
				
				# 点击保存按钮
				click("xpath", "//span[text()='上传']")
				
				# 退出所有iframe窗体
				switch_default()
				
				# 用隐式等待方法等页面出现新增成功的提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功,共导入1条数据，成功1条，失败0条，未处理0条。')]")
				print("支付限额导入，保存成功！")
				time.sleep(3)
				
				switch_to("xpath", "//iframe[@id='limitAmount-tab-iframe']")
				
				# 点击关闭当前页面
				click("xpath", "//div[@id='f-win-title-importDataWin']/descendant::*[2]")
				sleep(1)
				
				switch_default()
				
				# 删除功能
				switch_to("xpath", "//iframe[@id='limitAmount-tab-iframe']")
				
				# 点击查看
				# 用JS的方法点击放大镜
				js_click("xpath", "//span[@class='f-contrac-close']")
				sleep(1)
				
				# 代码
				click("xpath", "//input[@id='combobox-input-orgid']")
				sleep(1)
				input("xpath", "//input[@id='combobox-input-orgid']", "亚唐科技")
				sleep(1)
				click("xpath", "//div[contains(text(),'亚唐科技') ]/parent::*[1]/preceding-sibling::*[1]/descendant::*[2]")
				sleep(1)
				
				# 点击查询
				click("xpath", "//span[text()='查询']")
				sleep(1)
				
				# 勾选//div[contains(text(),'亚唐科技')]/parent::*/preceding-sibling::*[2]/descendant::*[2]")
				click("xpath", "//div[contains(text(),'亚唐科技')]/parent::*/preceding-sibling::*[2]/descendant::*[2]")
				sleep(1)
				
				# 点击删除按钮
				click("xpath", "//span[text()='删除']")
				sleep(1)
				
				# 点击弹出框的OK键
				click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
				
				# 退出所有iframe窗体
				switch_default()
				
				# 用隐式等待方法等页面出现删除的提示框
				implici_wait("xpath", "//span[contains(text(),'成功删除1条记录')]")
				print("支付限额导入，删除成功！")
				time.sleep(3)
				
				# 用JS的方法关闭当前页面
				js_click("xpath", "//a[@title='支付限额']/child::*[1]")
				
				# 再次点击基础设置菜单，使之关闭
				click("xpath", "//li[@f_value='settlementSetting']/descendant-or-self::*[5]")
				
				# 打印操作成功日志
				print("支付限额导入，操作成功!")
				logging.info("支付限额导入，操作成功!")
				time.sleep(2)
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("支付限额导入操作失败！" + str(traceback.format_exc()))
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

