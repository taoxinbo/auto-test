# encoding=utf-8
# @Time : 2021/01/04 13:30
# @Author : zzg
# 此文件是测试MySql版本资金结算管理--结算中心收付（委托付款申请、委托付款受理）
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
class Test54_ZiJinJieSuanGuanLi_JSZXSF(unittest.TestCase):
	
	# 启动浏览器
	def setUp(self):
		# 启动浏览器的另外一个方法：通过封装启动浏览器的驱动，启动不同浏览器
		self.driver = get("chrome")
	
	# 登陆系统、对系统设置进行操作
	def test_trade(self):
		
		#💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
		login(G_Ora_Url, mindy, Password, "亚唐科技")
		# 💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
		
		# 将页面的滚动条滑动到‘资金结算管理’页面的地方
		js_gd("xpath", "//span[contains(text(),'资金结算管理')]")
		# 用JS的方法点击资金结算管理菜单按钮
		js_click("xpath", "//span[contains(text(),'资金结算管理')]")
		sleep(1)
		# 点击'外币收付结算'菜单
		click("xpath", "//span[text()='结算中心收付']")
		sleep(1)
		# 退出所有iframe窗体
		switch_default()
		'''
		# 测试结算中心收付-委托付款申请-收付分配确认-收款分配🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱
		try:
			logger.info("测试结算中心收付-委托付款申请-收付分配确认")
			click("xpath", "//span[text()='收付分配确认']")
			sleep(1)
			switch_default()
			
			#直联账户明细💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			click("xpath", "//span[text()='结算中心收付']")
			sleep(1)
			js_click("xpath", "//span[contains(text(),'资金结算管理')]")
			sleep(1)
			js_click("xpath", "//span[contains(text(),'账户资金监控')]")
			sleep(1)
			click("xpath", "//span[text()='直联账户查询']")
			sleep(1)
			#退出所有窗体
			switch_default()
			
			#切入直联账户查询窗体
			switch_to("xpath",'//*[@id="directBankAccountQuery-tab-iframe"]')
			switch_to("xpath",'//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			#查询
			click("xpath",'//*[@id="north"]/div[2]/span')
			sleep(1)
			input("xpath",'//*[@id="accountnumber"]','20211005')
			sleep(1)
			span_click("查询")
			#勾选按钮
			click("xpath",'//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
			sleep(1)
			span_click("今日明细查询")
			sleep(3)
			switch_default()
			
			#回到收付分配确认界面
			js_click("xpath", "//span[contains(text(),'账户资金监控')]")
			sleep(1)
			js_click("xpath", "//span[contains(text(),'资金结算管理')]")
			sleep(1)
			click("xpath", "//span[text()='结算中心收付']")
			sleep(1)
			click("xpath", "//span[text()='收付分配确认']")
			sleep(1)
			switch_default()
			
			#测试分配功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath",'//*[@id="settleCenterDistribution-tab-iframe"]')
			switch_to("xpath",'//*[@id="recdistribution-iframe"]')
			sleep(1)
			
			#查询数据
			click("xpath",'//*[@id="north"]/div[2]/span')
			sleep(1)
			input("xpath",'//*[@id="combobox-input-accountid"]','20211005')
			sleep(1)
			click("xpath",'//*[@id="accountid-combogrid-body-table"]/tbody/tr/td[2]/div/button')
			sleep(1)
			span_click("查询")
			#刷新、勾选按钮
			click("xpath",'//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath",'//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("分配")
			switch_to("xpath",'//*[@id="editWin-iframe"]')
			sleep(3)
			
			#交易类型
			input("xpath",'//*[@id="combobox-input-paytypeid"]','201-外部收款')
			sleep(1)
			click("xpath",'//*[@id="paytypeid-combogrid-body-table"]/tbody/tr/td[2]/div')
			sleep(1)
			
			#认领组织
			click("xpath",'//*[@id="combobox-input-claimorgname"]')
			sleep(1)
			click("xpath",'//*[@id="claimorgname-combogrid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("保存")
			# 退出所有窗体
			switch_default()
			print("结算中心收付-收付分配确认-收款分配，分配成功")
			time.sleep(3)
			click("xpath", "//span[text()='收付分配确认']")
			sleep(1)
			switch_default()
			
			# 测试终止分配功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="settleCenterDistribution-tab-iframe"]')
			switch_to("xpath", '//*[@id="recdistribution-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("终止分配")
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'1条成功0条失败!操作成功！')]")
			print("结算中心收付-收付分配确认-收款分配，终止分配成功")
			time.sleep(3)
			
			# 测试取消终止功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="settleCenterDistribution-tab-iframe"]')
			switch_to("xpath", '//*[@id="recdistribution-iframe"]')
			sleep(1)
			
			#查询不分配数据
			click("xpath",'//*[@id="north"]/div[2]/span')
			sleep(1)
			span_click("高级查询")
			#查询条件
			input_up_click('//*[@id="combobox-input-property_0"]','分配状态')
			
			click("xpath",'//*[@id="combobox-input-value_0"]')
			sleep(1)
			click("xpath",'//*[@id="f-combo-value_0-list-2"]/div[1]')
			sleep(1)
	
			click("xpath",'//*[@id="advQueryWin-btn-1"]/div[2]')
			sleep(1)
			
			#勾选按钮，取消终止
			click("xpath",'//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
			sleep(1)
			span_click("取消终止")
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'1条成功0条失败!')]")
			print("结算中心收付-收付分配确认-收款分配，取消终止成功")
			time.sleep(3)
			
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("收款分配失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)

			# def tearDown(self):
			#     self.driver.quit()
			print("结束时间：", time.strftime("%Y-%m-%d %H:%M:%S"))
		
		
		# 测试结算中心收付-委托付款申请-收付分配确认-付款分配🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱
		try:
			logger.info("测试结算中心收付-委托付款申请-收付分配确认-付款分配")
			click("xpath", "//span[text()='收付分配确认']")
			sleep(1)
			switch_default()
			
			# 切入付款分配窗体
			switch_to("xpath", '//*[@id="settleCenterDistribution-tab-iframe"]')
			span_click("付款分配")
			switch_to("xpath", '//*[@id="paydistribution-iframe"]')
			sleep(1)
			
			# 查询数据
			click("xpath", '//*[@id="north"]/div[2]/span')
			sleep(1)
			input("xpath", '//*[@id="combobox-input-accountid"]', '20211005')
			sleep(1)
			click("xpath", '//*[@id="accountid-combogrid-body-table"]/tbody/tr/td[2]/div/button')
			sleep(1)
			span_click("查询")
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("分配")
			switch_to("xpath", '//*[@id="editWin-iframe"]')
			sleep(3)
			
			#交易类型
			input_up_click('//*[@id="combobox-input-paytypeid"]','103-对外付款')
			
			#结算方式
			input_up_click('//*[@id="combobox-input-settlementmodeid"]','601-其他支付')
			
			#认领组织
			click("xpath",'//*[@id="combobox-input-claimorgname"]')
			sleep(1)
			click("xpath",'//*[@id="claimorgname-combogrid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("保存")
			# 退出所有窗体
			switch_default()
			print("结算中心收付-收付分配确认-付款分配，分配成功")
			time.sleep(3)
			click("xpath", "//span[text()='收付分配确认']")
			sleep(1)
			switch_default()
			
			# 测试终止分配功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="settleCenterDistribution-tab-iframe"]')
			span_click("付款分配")
			switch_to("xpath", '//*[@id="paydistribution-iframe"]')
			sleep(1)
			
			# 查询数据
			click("xpath", '//*[@id="north"]/div[2]/span')
			sleep(1)
			input("xpath", '//*[@id="combobox-input-accountid"]', '20211005')
			sleep(1)
			click("xpath", '//*[@id="accountid-combogrid-body-table"]/tbody/tr/td[2]/div/button')
			sleep(1)
			span_click("查询")
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("终止分配")
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'终止分配：1条，成功：1条')]")
			print("结算中心收付-收付分配确认-付款分配，终止分配成功")
			time.sleep(3)
			
			# 测试取消终止功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="settleCenterDistribution-tab-iframe"]')
			span_click("付款分配")
			switch_to("xpath", '//*[@id="paydistribution-iframe"]')
			sleep(1)
			
			# 查询不分配数据
			span_click("高级查询")
			# 查询条件
			input_up_click('//*[@id="combobox-input-property_0"]', '分配状态')
			
			click("xpath", '//*[@id="combobox-input-value_0"]')
			sleep(1)
			click("xpath", '//*[@id="f-combo-value_0-list-2"]/div[1]')
			sleep(1)
			
			click("xpath", '//*[@id="advQueryWin-btn-1"]/div[2]')
			sleep(1)
			
			# 勾选按钮，取消终止
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
			sleep(1)
			span_click("取消终止")
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'取消终止:1条，成功：1条')]")
			print("结算中心收付-收付分配确认-付款分配，取消终止成功")
			time.sleep(3)
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("付款分配失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)

			print("结束时间：", time.strftime("%Y-%m-%d %H:%M:%S"))
		
		
		
		# 测试结算中心收付-委托付款申请-收付分配确认-付款分配🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱
		try:
			logger.info("测试结算中心收付-委托付款申请-委托付款认领-收款认领")
			click("xpath", "//span[text()='委托收付认领']")
			sleep(1)
			switch_default()
			
			#去收款分配页面做数据💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			click("xpath", "//span[text()='收付分配确认']")
			sleep(1)
			switch_default()
			switch_to("xpath", '//*[@id="settleCenterDistribution-tab-iframe"]')
			switch_to("xpath", '//*[@id="recdistribution-iframe"]')
			sleep(1)
			
			# 查询数据
			click("xpath", '//*[@id="north"]/div[2]/span')
			sleep(1)
			input("xpath", '//*[@id="combobox-input-accountid"]', '20211005')
			sleep(1)
			click("xpath", '//*[@id="accountid-combogrid-body-table"]/tbody/tr/td[2]/div/button')
			sleep(1)
			span_click("查询")
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[3]/td[2]/div/button')
			sleep(1)
			
			span_click("分配")
			switch_to("xpath", '//*[@id="editWin-iframe"]')
			sleep(3)
			
			# 交易类型
			input("xpath", '//*[@id="combobox-input-paytypeid"]', '201-外部收款')
			sleep(1)
			click("xpath", '//*[@id="paytypeid-combogrid-body-table"]/tbody/tr/td[2]/div')
			sleep(1)
			
			# 认领组织
			click("xpath", '//*[@id="combobox-input-claimorgname"]')
			sleep(1)
			click("xpath", '//*[@id="claimorgname-combogrid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("保存")
			# 退出所有窗体
			switch_default()
			sleep(3)
			#回到委托收付认领界面
			click("xpath", "//span[text()='委托收付认领']")
			sleep(1)
			
			#测试认领功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath",'//*[@id="settleCenterClaim-tab-iframe"]')
			switch_to("xpath",'//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			#刷新、勾选按钮
			click("xpath",'//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath",'//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("认领")
			#切入认领窗体
			switch_to("xpath",'//*[@id="claimWin-iframe"]')
			
			#收款明细
			click("xpath","//div[@title='收款明细']")
			sleep(1)
			span_click("新增行")
			#金额
			input("xpath",'//*[@id="claimgrid-amount-0-input"]','100')
			sleep(1)
			#收方内部账户
			click_up_click('//*[@id="combobox-input-claimgrid-ourinternalaccountid-0"]')
			
			span_click("保存")
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("结算中心收付-委托付款认领-收款认领，认领成功")
			time.sleep(3)
			
			# 测试修改功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="settleCenterClaim-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("修改")
			# 切入修改窗体
			switch_to("xpath", '//*[@id="claimWin-iframe"]')
			span_click("保存")
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("结算中心收付-委托付款认领-收款认领，修改成功")
			time.sleep(3)
			
			# 测试取消认领功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="settleCenterClaim-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("取消认领")
			ok_click()
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'成功取消认领1条记录！')]")
			print("结算中心收付-委托付款认领-收款认领，取消认领成功")
			time.sleep(3)
			
			# 测试驳回功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="settleCenterClaim-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("驳回")
			ok_click()
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'成功驳回1条记录！')]")
			print("结算中心收付-委托付款认领-收款认领，驳回成功")
			time.sleep(3)
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("收款失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
			
			print("结束时间：", time.strftime("%Y-%m-%d %H:%M:%S"))
		
		
		# 测试结算中心收付-委托付款申请-收付分配确认-付款认领🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱
		try:
			logger.info("测试结算中心收付-委托付款申请-委托付款认领-收款认领")
			click("xpath", "//span[text()='委托收付认领']")
			sleep(1)
			switch_default()
			
			# 去付款分配页面做数据💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			click("xpath", "//span[text()='收付分配确认']")
			sleep(1)
			switch_default()
			# 切入付款分配窗体
			switch_to("xpath", '//*[@id="settleCenterDistribution-tab-iframe"]')
			span_click("付款分配")
			switch_to("xpath", '//*[@id="paydistribution-iframe"]')
			sleep(1)
			
			# 查询数据
			click("xpath", '//*[@id="north"]/div[2]/span')
			sleep(1)
			input("xpath", '//*[@id="combobox-input-accountid"]', '20211005')
			sleep(1)
			click("xpath", '//*[@id="accountid-combogrid-body-table"]/tbody/tr/td[2]/div/button')
			sleep(1)
			span_click("查询")
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[2]/td[2]/div/button')
			sleep(1)
			
			span_click("分配")
			switch_to("xpath", '//*[@id="editWin-iframe"]')
			sleep(3)
			
			# 交易类型
			input_up_click('//*[@id="combobox-input-paytypeid"]', '103-对外付款')
			
			# 结算方式
			input_up_click('//*[@id="combobox-input-settlementmodeid"]', '601-其他支付')
			
			# 认领组织
			click("xpath", '//*[@id="combobox-input-claimorgname"]')
			sleep(1)
			click("xpath", '//*[@id="claimorgname-combogrid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("保存")
			# 退出所有窗体
			switch_default()
			sleep(3)
			#回到委托付款认领界面
			click("xpath", "//span[text()='委托收付认领']")
			sleep(1)
			
			#测试认领功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			#切入付款认领窗体
			switch_to("xpath",'//*[@id="settleCenterClaim-tab-iframe"]')
			span_click("付款认领")
			switch_to("xpath",'//*[@id="subTabTwo-iframe"]')
			sleep(1)
			
			#刷新、勾选按钮
			click("xpath",'//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("认领")
			switch_to("xpath",'//*[@id="claimWin-iframe"]')
			span_click("付款明细")
			span_click("新增行")
			#金额
			input("xpath",'//*[@id="claimgrid-amount-0-input"]','100')
			sleep(1)
			#付方内部账户
			click_up_click('//*[@id="combobox-input-claimgrid-oppinternalaccountid-0"]')
			span_click("保存")
			
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("结算中心收付-委托付款认领-付款认领，认领成功")
			time.sleep(3)
			
			# 测试修改功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入付款认领窗体
			switch_to("xpath", '//*[@id="settleCenterClaim-tab-iframe"]')
			span_click("付款认领")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("修改")
			switch_to("xpath", '//*[@id="claimWin-iframe"]')
			span_click("保存")
			
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("结算中心收付-委托付款认领-付款认领，修改成功")
			time.sleep(3)
			
			# 测试取消认领功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入付款认领窗体
			switch_to("xpath", '//*[@id="settleCenterClaim-tab-iframe"]')
			span_click("付款认领")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("取消认领")
			ok_click()
			
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'成功取消认领1条记录！')]")
			print("结算中心收付-委托付款认领-付款认领，取消认领成功")
			time.sleep(3)
			
			# 测试驳回功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入付款认领窗体
			switch_to("xpath", '//*[@id="settleCenterClaim-tab-iframe"]')
			span_click("付款认领")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("驳回")
			ok_click()
			
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'成功驳回1条记录！')]")
			print("结算中心收付-委托付款认领-付款认领，驳回成功")
			time.sleep(3)
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("付款认领失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
			
			print("结束时间：", time.strftime("%Y-%m-%d %H:%M:%S"))
		
		
		# 测试结算中心收付-申请组织查看🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱
		try:
			logger.info("测试结算中心收付-申请组织查看")
			click("xpath", "//span[text()='申请组织查看']")
			sleep(1)
			switch_default()
			
			# 测试设置为不导出功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入申请组织查看
			switch_to("xpath", '//*[@id="settleCenterOrgCheck-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			sleep(1)
			
			#刷新、勾选按钮
			click("xpath",'//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("设置导出标识","设置为不导出")
			
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'设置导出标识操作成功!')]")
			print("结算中心收付-申请组织查看-付款查看，设置为不导出成功")
			time.sleep(3)
			
			# 测试设置为需导出功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入申请组织查看
			switch_to("xpath", '//*[@id="settleCenterOrgCheck-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("设置导出标识", "设置为需导出")
			
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'设置导出标识操作成功!')]")
			print("结算中心收付-申请组织查看-付款查看，设置为需导出成功")
			time.sleep(3)
			
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("付款认领失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
			
			print("结束时间：", time.strftime("%Y-%m-%d %H:%M:%S"))
		
		
		# 测试结算中心收付-内部管理费-管理费类别🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱
		try:
			logger.info("测试结算中心收付-内部管理费-管理费类别")
			click("xpath", "//span[text()='内部管理费']")
			sleep(1)
			switch_default()
			
			# 测试新增功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			for i in range (1,3):
				# 切入管理费类别窗体
				switch_to("xpath", '//*[@id="settleInternalManagementFee-tab-iframe"]')
				switch_to("xpath", '//*[@id="subTabOne-iframe"]')
				sleep(1)
				span_click("新增")
				switch_to("xpath", '//*[@id="addWin-iframe"]')
				
				# 代码
				code = time.strftime("%Y%m%d%H%M%S")
				input("xpath", '//*[@id="code"]', str(code))
				sleep(1)
				
				# 名称
				name = "GLF" + str(time.strftime("%Y%m%M%S"))
				input("xpath", '//*[@id="name"]', name)
				sleep(1)
				
				span_click("保存")
				# 退出所有窗体
				switch_default()
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				if i == 2 :
					print("结算中心收付-内部管理费-管理费类别，新增成功")
				time.sleep(3)
				
			# 测试修改功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入管理费类别窗体
			switch_to("xpath", '//*[@id="settleInternalManagementFee-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			#刷新、勾选按钮
			click("xpath",'//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath",'//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
			sleep(1)
			
			span_click("修改")
			switch_to("xpath",'//*[@id="modWin-iframe"]')
			input("xpath",'//*[@id="description"]','测试修改')
			sleep(1)
			span_click("保存")
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("结算中心收付-内部管理费-管理费类别，修改成功")
			time.sleep(3)
			
			# 测试删除功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入管理费类别窗体
			switch_to("xpath", '//*[@id="settleInternalManagementFee-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
			sleep(1)
			
			span_click("删除")
			ok_click()
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("结算中心收付-内部管理费-管理费类别，删除成功")
			time.sleep(3)
	
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("管理费类别失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
			
			print("结束时间：", time.strftime("%Y-%m-%d %H:%M:%S"))
		
		sleep(1)
		'''
		# 测试结算中心收付-内部管理费-管理费标准🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱
		try:
			logger.info("测试结算中心收付-内部管理费-管理费标准")
			click("xpath", "//span[text()='内部管理费']")
			sleep(1)
			switch_default()
			
			#去做管理费标准结算方式💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			click("xpath", "//span[text()='结算中心收付']")
			sleep(1)
			# 点击基础设置
			click("xpath",
			      '/html/body/div[1]/div[1]/div/div[2]/div/div[2]/div/div/div/div[4]/div/div/ul/li[1]/a/span[2]')
			sleep(1)
			click("xpath", "//span[text()='结算方式']")
			sleep(1)
			switch_default()
			
			switch_to("xpath", "//iframe[@id='settlementMode-tab-iframe']")
			# 用JS的方法点击新增按钮
			js_click("xpath", "//span[text()='新增']")
			sleep(1)
			# 切入新增的iframe窗体
			switch_to("xpath", "//iframe[@id='addWin-iframe']")
			# 输入代码
			coad = str(time.strftime("%Y%m%d%H%M%S"))
			input("xpath", "//input[@name='code']", coad)
			sleep(1)
			
			# 输入name
			name = "GLF"+ str(time.strftime("%Y%m%S"))
			input("xpath", "//input[@id='name']", name)
			sleep(1)
			
			# 输入交易方向
			input_up_click("//input[@id='combobox-input-moneyway']",'支出')
			
			# 输入支付类型
			input_up_click("//input[@id='combobox-input-dealtype']",'结算中心转账')
			
			# 点击保存按钮
			click("xpath", "//span[text()='保存']")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			time.sleep(3)
			
			# 创建直联批量付款的交易类型💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			click("xpath", "//span[text()='交易类型']")
			sleep(1)
			switch_to('xpath', '//*[@id="payType-tab-iframe"]')
			js_click("xpath", "//span[text()='新增']")
			sleep(1)
			# 切入新增的iframe窗体
			switch_to("xpath", "//iframe[@id='addWin-iframe']")
			# 输入代码
			code = str(time.strftime("%Y%m%d%H%M%S"))
			input("xpath", "//input[@id='code']", code)
			sleep(1)
			
			# 输入名称
			input("xpath", "//input[@id='name']", name)
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
			input("xpath", "//input[@id='combobox-input-settlementmoderange']", coad)
			sleep(1)
			# input("xpath", "//input[@id='combobox-input-settlementmoderange']", "101-直联单笔转账")
			# sleep(1)
			click("xpath", '//*[@id="settlementmoderange-combogrid-body-table"]/tbody/tr/td[2]/div/button')
			sleep(1)
			
			# 默认结算方式
			click("xpath", "//input[@id='combobox-input-defaultsettlementmodeid']")
			sleep(1)
			input_down("xpath", "//input[@id='combobox-input-defaultsettlementmodeid']")
			input_enter("xpath", "//input[@id='combobox-input-defaultsettlementmodeid']")
			sleep(1)
			
			# 对方对象类型
			click("xpath", "//input[@id='combobox-input-oppobjecttype']")
			sleep(1)
			input("xpath", "//input[@id='combobox-input-oppobjecttype']", "内部组织")
			sleep(1)
			input_down("xpath", "//input[@id='combobox-input-oppobjecttype']")
			input_enter("xpath", "//input[@id='combobox-input-oppobjecttype']")
			sleep(1)
			
			#组织范围
			click_up_click('//*[@id="combobox-input-opporgoption"]')
			
			# 计划项目必填类型
			click("xpath", "//input[@id='combobox-input-budgetitemrequiredtype']")
			sleep(1)
			input("xpath", "//input[@id='combobox-input-budgetitemrequiredtype']", "非必填")
			sleep(1)
			input_down("xpath", "//input[@id='combobox-input-budgetitemrequiredtype']")
			input_enter("xpath", "//input[@id='combobox-input-budgetitemrequiredtype']")
			sleep(1)
			# 点击保存按钮
			click("xpath", "//span[text()='保存']")
			print("管理费标准结算方式、交易类型创建成功")
			switch_default()
			
			#回到
			# 点击基础设置
			click("xpath",
			      '/html/body/div[1]/div[1]/div/div[2]/div/div[2]/div/div/div/div[4]/div/div/ul/li[1]/a/span[2]')
			sleep(1)
			click("xpath", "//span[text()='结算中心收付']")
			sleep(1)
			click("xpath", "//span[text()='内部管理费']")
			sleep(1)
			switch_default()
			
			# 测试新增功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			for i in range(1, 3):
				# 切入管理费标准窗体
				switch_to("xpath", '//*[@id="settleInternalManagementFee-tab-iframe"]')
				span_click("管理费标准")
				switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
				sleep(1)
				
				span_click("新增")
				switch_to("xpath", '//*[@id="addWin-iframe"]')
				
				#名称
				name = "GLFBZ"+str(time.strftime("%Y%m%M%S"))
				input("xpath",'//*[@id="name"]',name)
				sleep(1)
				
				span_click("收付交易信息")
				sleep(3)
				#js_click("xpath",
				        # '/html/body/form/div[2]/div[2]/ul/li[1]/div/div/div/div/ul/div[1]/div[3]/div/div[1]/table/tbody/tr/td[1]/span')
				sleep(1)
				
				
				#管理费类别
				click_up_click('//*[@id="combobox-input-confirmrules-managementfeecategoryid-0"]')
				
				#费率
				double_click("xpath",'//*[@id="confirmrules-feerate-0-input"]')
				sleep(1)
				input("xpath",'//*[@id="confirmrules-feerate-0-input"]','5')
				sleep(1)
				
				#交易类型
				click_up_click('//*[@id="combobox-input-confirmrules-paytypeid-0"]')
				
				#结算方式
				click_up_click('//*[@id="combobox-input-confirmrules-settlementmodeid-0"]')
				
				#收方内部账户
				click_up_click('//*[@id="combobox-input-confirmrules-recinternalaccountid-0"]')
				
				span_click("保存")
				# 退出所有窗体
				switch_default()
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				if i == 2:
					print("结算中心收付-内部管理费-管理费标准，新增成功")
				time.sleep(3)
				
			# 测试修改功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入管理费标准窗体
			switch_to("xpath", '//*[@id="settleInternalManagementFee-tab-iframe"]')
			span_click("管理费标准")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			sleep(1)
			
			#刷新、勾选按钮
			click("xpath",'//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
			sleep(1)
			
			span_click("修改")
			switch_to("xpath",'//*[@id="modWin-iframe"]')
			span_click("保存")
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("结算中心收付-内部管理费-管理费标准，修改成功")
			time.sleep(3)
			
			# 测试失效功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入管理费标准窗体
			switch_to("xpath", '//*[@id="settleInternalManagementFee-tab-iframe"]')
			span_click("管理费标准")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
			sleep(1)
			
			span_click("失效")
			
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'失效成功')]")
			print("结算中心收付-内部管理费-管理费标准，失效成功")
			time.sleep(3)
			
			# 测试生效功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入管理费标准窗体
			switch_to("xpath", '//*[@id="settleInternalManagementFee-tab-iframe"]')
			span_click("管理费标准")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
			sleep(1)
			
			span_click("生效")
			logger.info("")
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'生效成功')]")
			print("结算中心收付-内部管理费-管理费标准，生效成功")
			time.sleep(3)
			
			# 测试删除功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入管理费标准窗体
			switch_to("xpath", '//*[@id="settleInternalManagementFee-tab-iframe"]')
			span_click("管理费标准")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
			sleep(1)
			
			span_click("删除")
			ok_click()
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'成功删除1条数据！')]")
			print("结算中心收付-内部管理费-管理费标准，删除成功")
			time.sleep(3)
			
			# 测试执行功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入管理费标准窗体
			switch_to("xpath", '//*[@id="settleInternalManagementFee-tab-iframe"]')
			span_click("管理费标准")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
			sleep(1)
			
			span_click("执行")
			ok_click()
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("结算中心收付-内部管理费-管理费标准，执行成功")
			time.sleep(3)
			
			
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("管理费标准失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
			
			print("结束时间：", time.strftime("%Y-%m-%d %H:%M:%S"))
			
			
			
			
			
			
if __name__ == '__main__':
	#  启动单元测试
	unittest.main(verbosity=2)
