# encoding=utf-8
# @Time : 2020/11/19 13:30
# @Author : zzg
# 此文件是测试Mysql版本外币业务对接
import os
import sys, pytest
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)),".."))
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
import random
# print("开始时间：",time.strftime("%Y-%m-%d %H:%M:%S"))

driver = ""


@pytest.mark.flaky(reruns=pytest_flaky, reruns_delay=10)
class Test56_WaiBiYeWuDuiJie(unittest.TestCase):
	
	# 启动浏览器
	def setUp(self):
		# 启动浏览器的另外一个方法：通过封装启动浏览器的驱动，启动不同浏览器
		self.driver = get("chrome")
	
	# 登陆系统、对系统设置进行操作
	def test_trade(self):
		
		# login(G_Ora_Url, mindy, Password, "亚唐科技")
		login(G_Ora_Url, mindy, Password, "亚唐科技")
		
		logging.info("开始测试资金结算管理--外币业务对接")
		# 将页面的滚动条滑动到‘资金结算管理’页面的地方
		js_gd("xpath", "//span[contains(text(),'资金结算管理')]")
		# 用JS的方法点击资金结算管理菜单按钮
		js_click("xpath", "//span[contains(text(),'资金结算管理')]")
		sleep(1)
		# 点击'外币收付结算'菜单
		click("xpath", "//span[text()='外币业务对接']")
		sleep(1)
		# 退出所有iframe窗体
		switch_default()
		'''
		#测试外币收付结算--快捷付款申请🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱
		try:
			logger.info("测试外币收付结算--快捷付款申请")
			switch_default()
			sleep(3)
			click("xpath", "//span[text()='快捷付款申请']")
			sleep(1)
			
			#去跨境外币汇款页面做数据💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 点击'外币收付结算'菜单
			click("xpath", "//span[text()='外币业务对接']")
			sleep(1)
			click("xpath", "//span[text()='外币收付结算']")
			sleep(1)
			click("xpath", "//span[text()='跨境外币汇款']")
			sleep(1)
			switch_default()
			for i in range(1, 3):
				# 切入跨境外币汇款界面
				switch_to("xpath", '//*[@id="crossBorderPayment-tab-iframe"]')
				switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
				sleep(3)
				# 点击新增
				span_click("新增")
				sleep(1)
				# 切入新增窗体
				switch_to("xpath", '//*[@id="addWin-iframe"]')
				# 组织机构代码
				input("xpath", '//*[@id="ourregorgcode"]', '001010')
				sleep(1)
				
				# 交易类型
				input("xpath", '//*[@id="combobox-input-paytypeid"]', '3030-直联跨境外币汇款交易类型')
				sleep(3)
				input_down("xpath", '//*[@id="combobox-input-paytypeid"]')
				input_enter("xpath", '//*[@id="combobox-input-paytypeid"]')
				sleep(1)
				
				# 汇款币种
				input("xpath", '//*[@id="combobox-input-ourcurrencyid"]', 'CNY')
				sleep(1)
				input_down("xpath", '//*[@id="combobox-input-ourcurrencyid"]')
				input_enter("xpath", '//*[@id="combobox-input-ourcurrencyid"]')
				sleep(1)
				
				# 汇款金额
				money = random.randint(100, 300)
				double_click("xpath", '//*[@id="ouramount-input"]')
				sleep(1)
				input("xpath", '//*[@id="ouramount-input"]', money)
				sleep(1)
				
				# 汇款银行
				input("xpath", '//*[@id="combobox-input-paybankid"]', 'BOC-中国银行')
				sleep(1)
				input_down("xpath", '//*[@id="combobox-input-paybankid"]')
				input_enter("xpath", '//*[@id="combobox-input-paybankid"]')
				sleep(1)
				
				# 购汇账户
				input("xpath", '//*[@id="combobox-input-purchasebankaccountid"]', '20211030')
				sleep(3)
				input_down("xpath", '//*[@id="combobox-input-purchasebankaccountid"]')
				input_enter("xpath", '//*[@id="combobox-input-purchasebankaccountid"]')
				sleep(1)
				
				# 购汇汇率
				double_click("xpath", '//*[@id="purchaseexchangerate-input"]')
				sleep(1)
				input("xpath", '//*[@id="purchaseexchangerate-input"]', '1')
				# 去除下拉框
				double_click("xpath", '//*[@id="feeaccountinfo"]')
				sleep(1)
				
				# 收方名称
				input("xpath", '//*[@id="combobox-input-oppcounterpartyid"]', '浙江彩旗科技')
				sleep(1)
				# 清除下拉框
				double_click("xpath", '//*[@id="feeaccountinfo"]')
				sleep(1)
				
				# 收方账户
				click("xpath", '//*[@id="combobox-input-oppcounterpartyaccountid"]')
				sleep(1)
				input("xpath", '//*[@id="combobox-input-oppcounterpartyaccountid"]', '200848199612')
				sleep(1)
				# 清除下拉框
				double_click("xpath", '//*[@id="feeaccountinfo"]')
				sleep(1)
				
				# 收方类型
				click("xpath", '//*[@id="combobox-input-oppresidenttype"]')
				sleep(1)
				input_down("xpath", '//*[@id="combobox-input-oppresidenttype"]')
				input_enter("xpath", '//*[@id="combobox-input-oppresidenttype"]')
				sleep(1)
				
				# 收方地址
				input("xpath", '//*[@id="oppaddress"]', '浙江杭州')
				sleep(1)
				
				# 收方开户银行
				input("xpath", '//*[@id="combobox-input-oppbanklocationid"]', '（韩国地区）中国农业银行首尔支行')
				sleep(1)
				click("xpath", '//*[@id="oppbanklocationid-combogrid-body-table"]/tbody/tr/td[2]/div')
				sleep(1)
				
				# 用途
				input("xpath", '//*[@id="combobox-input-purpose"]', "外币业务对接快捷付款申请")
				sleep(1)
				
				# 付款方式
				click("xpath", '//*[@id="combobox-input-paymentmethod"]')
				sleep(1)
				input_down("xpath", '//*[@id="combobox-input-paymentmethod"]')
				input_enter("xpath", '//*[@id="combobox-input-paymentmethod"]')
				sleep(1)
				
				# 国内外费用承担人
				click("xpath", '//*[@id="combobox-input-intermediatecostmode"]')
				sleep(1)
				input_down("xpath", '//*[@id="combobox-input-intermediatecostmode"]')
				input_enter("xpath", '//*[@id="combobox-input-intermediatecostmode"]')
				sleep(1)
				
				# 付汇性质
				click("xpath", '//*[@id="combobox-input-paymentproperty"]')
				sleep(1)
				input_down("xpath", '//*[@id="combobox-input-paymentproperty"]')
				input_enter("xpath", '//*[@id="combobox-input-paymentproperty"]')
				sleep(1)
				
				# 交易编码
				click("xpath", '//*[@id="combobox-input-transactioncode1"]')
				sleep(1)
				input_down("xpath", '//*[@id="combobox-input-transactioncode1"]')
				input_enter("xpath", '//*[@id="combobox-input-transactioncode1"]')
				sleep(1)
				
				# 保存
				span_click("保存")
				sleep(1)
				# 退出所有iframe窗体
				switch_default()
				# 用隐式等待方法等页面出现新增成功的提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功')]")
				time.sleep(3)
			sql = "update t_se_payments set RECORDSOURCE = '4' where purpose = '外币业务对接快捷付款申请'"
			ora_sql(ora_ip, ora_sid, ora_user, ora_pwd,
			       sql)
			
			# 回到快捷付款申请页面
			click("xpath", "//span[text()='外币收付结算']")
			sleep(1)
			click("xpath", "//span[text()='外币业务对接']")
			sleep(1)
			click("xpath", "//span[text()='快捷付款申请']")
			sleep(1)
			switch_default()
			
			#测试修改功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath",'//*[@id="externalPaymentsApply-tab-iframe"]')
			sleep(1)
			#刷新、勾选按钮
			click("xpath",'//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath",'//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("修改")
			switch_to("xpath",'//*[@id="singleModWin-iframe"]')
			sleep(3)
			span_click("保存")
			
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("外币业务对接-快捷付款申请，修改成功")
			time.sleep(3)
			
			# 测试批量变更功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="externalPaymentsApply-tab-iframe"]')
			sleep(1)
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			click("xpath",'//*[@id="grid-body-table"]/tbody/tr[2]/td[2]/div/button')
			sleep(1)
			
			
			span_click("批量变更")
			switch_to("xpath", '//*[@id="batchModWin_General-iframe"]')
			click_up_click('//*[@id="combobox-input-purchasebankaccountid"]')
			
			span_click("保存")
			
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("外币业务对接-快捷付款申请，批量变更成功")
			time.sleep(3)
			
			# 测试作废功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="externalPaymentsApply-tab-iframe"]')
			sleep(1)
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
		
			
			span_click("作废")
			ok_click()
			span_click("确定")
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("外币业务对接-快捷付款申请，作废成功")
			time.sleep(3)

		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("快捷付款申请失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
			
			# def tearDown(self):
			#     self.driver.quit()
			print("结束时间：", time.strftime("%Y-%m-%d %H:%M:%S"))
		
		# 测试外币收付结算--跨境外币汇款-直联跨境外币汇款🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱
		
		try:
			logger.info("测试外币收付结算--跨境外币汇款-直联跨境外币汇款")
			switch_default()
			sleep(3)
			click("xpath",'/html/body/div[1]/div[1]/div/div[2]/div/div[2]/div/div/div/div[4]/div/div/ul/li[10]/ul/li[2]/a/span[2]')
			sleep(1)
			
			# 去跨境外币汇款页面做数据💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 点击'外币收付结算'菜单
			click("xpath", "//span[text()='外币业务对接']")
			sleep(1)
			click("xpath", "//span[text()='外币收付结算']")
			sleep(1)
			click("xpath", "//span[text()='跨境外币汇款']")
			sleep(1)
			switch_default()
			
			for i in range(1, 3):
				# 切入跨境外币汇款界面
				switch_to("xpath", '//*[@id="crossBorderPayment-tab-iframe"]')
				switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
				sleep(3)
				# 点击新增
				span_click("新增")
				sleep(1)
				# 切入新增窗体
				switch_to("xpath", '//*[@id="addWin-iframe"]')
				# 组织机构代码
				input("xpath", '//*[@id="ourregorgcode"]', '001010')
				sleep(1)
				
				# 交易类型
				input("xpath", '//*[@id="combobox-input-paytypeid"]', '3030-直联跨境外币汇款交易类型')
				sleep(1)
				input_down("xpath", '//*[@id="combobox-input-paytypeid"]')
				input_enter("xpath", '//*[@id="combobox-input-paytypeid"]')
				sleep(1)
				
				# 汇款币种
				input("xpath", '//*[@id="combobox-input-ourcurrencyid"]', 'CNY')
				sleep(1)
				input_down("xpath", '//*[@id="combobox-input-ourcurrencyid"]')
				input_enter("xpath", '//*[@id="combobox-input-ourcurrencyid"]')
				sleep(1)
				
				# 汇款金额
				money = random.randint(100, 300)
				double_click("xpath", '//*[@id="ouramount-input"]')
				sleep(1)
				input("xpath", '//*[@id="ouramount-input"]', money)
				sleep(1)
				
				# 汇款银行
				input("xpath", '//*[@id="combobox-input-paybankid"]', 'BOC-中国银行')
				sleep(1)
				input_down("xpath", '//*[@id="combobox-input-paybankid"]')
				input_enter("xpath", '//*[@id="combobox-input-paybankid"]')
				sleep(1)
				
				# 购汇账户
				input("xpath", '//*[@id="combobox-input-purchasebankaccountid"]', '20211030')
				sleep(1)
				input_down("xpath", '//*[@id="combobox-input-purchasebankaccountid"]')
				input_enter("xpath", '//*[@id="combobox-input-purchasebankaccountid"]')
				sleep(1)
				
				# 购汇汇率
				double_click("xpath", '//*[@id="purchaseexchangerate-input"]')
				sleep(1)
				input("xpath", '//*[@id="purchaseexchangerate-input"]', '1')
				# 去除下拉框
				double_click("xpath", '//*[@id="feeaccountinfo"]')
				sleep(1)
				
				# 收方名称
				input("xpath", '//*[@id="combobox-input-oppcounterpartyid"]', '浙江彩旗科技')
				sleep(1)
				# 清除下拉框
				double_click("xpath", '//*[@id="feeaccountinfo"]')
				sleep(1)
				
				# 收方账户
				click("xpath", '//*[@id="combobox-input-oppcounterpartyaccountid"]')
				sleep(1)
				input("xpath", '//*[@id="combobox-input-oppcounterpartyaccountid"]', '200848199612')
				sleep(1)
				# 清除下拉框
				double_click("xpath", '//*[@id="feeaccountinfo"]')
				sleep(1)
				
				# 收方类型
				click("xpath", '//*[@id="combobox-input-oppresidenttype"]')
				sleep(1)
				input_down("xpath", '//*[@id="combobox-input-oppresidenttype"]')
				input_enter("xpath", '//*[@id="combobox-input-oppresidenttype"]')
				sleep(1)
				
				# 收方地址
				input("xpath", '//*[@id="oppaddress"]', '浙江杭州')
				sleep(1)
				
				# 收方开户银行
				input("xpath", '//*[@id="combobox-input-oppbanklocationid"]', '（韩国地区）中国农业银行首尔支行')
				sleep(1)
				click("xpath", '//*[@id="oppbanklocationid-combogrid-body-table"]/tbody/tr/td[2]/div')
				sleep(1)
				
				# 用途
				input("xpath", '//*[@id="combobox-input-purpose"]', "外币业务对接快捷付款申请")
				sleep(1)
				
				# 付款方式
				click("xpath", '//*[@id="combobox-input-paymentmethod"]')
				sleep(1)
				input_down("xpath", '//*[@id="combobox-input-paymentmethod"]')
				input_enter("xpath", '//*[@id="combobox-input-paymentmethod"]')
				sleep(1)
				
				# 国内外费用承担人
				click("xpath", '//*[@id="combobox-input-intermediatecostmode"]')
				sleep(1)
				input_down("xpath", '//*[@id="combobox-input-intermediatecostmode"]')
				input_enter("xpath", '//*[@id="combobox-input-intermediatecostmode"]')
				sleep(1)
				
				# 付汇性质
				click("xpath", '//*[@id="combobox-input-paymentproperty"]')
				sleep(1)
				input_down("xpath", '//*[@id="combobox-input-paymentproperty"]')
				input_enter("xpath", '//*[@id="combobox-input-paymentproperty"]')
				sleep(1)
				
				# 交易编码
				click("xpath", '//*[@id="combobox-input-transactioncode1"]')
				sleep(1)
				input_down("xpath", '//*[@id="combobox-input-transactioncode1"]')
				input_enter("xpath", '//*[@id="combobox-input-transactioncode1"]')
				sleep(1)
				
				# 保存
				span_click("保存")
				sleep(1)
				# 退出所有iframe窗体
				switch_default()
				# 用隐式等待方法等页面出现新增成功的提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功')]")
				time.sleep(3)
			sql = "update t_se_payments set RECORDSOURCE = '4' where purpose = '外币业务对接快捷付款申请'"
			ora_sql(ora_ip, ora_sid, ora_user, ora_pwd,
			       sql)
			
			# 回到快捷付款申请页面
			click("xpath", "//span[text()='外币收付结算']")
			sleep(1)
			click("xpath", "//span[text()='外币业务对接']")
			sleep(1)
			switch_default()
			click("xpath", '/html/body/div[1]/div[1]/div/div[2]/div/div[2]/div/div/div/div[4]/div/div/ul/li[10]/ul/li[2]/a/span[2]')
			sleep(1)
			
			# 测试修改功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入跨境外币汇款界面
			switch_to("xpath", '//*[@id="externalCrossBorderPayments-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			# 修改
			span_click("修改")
			switch_to("xpath", '//*[@id="modWin-iframe"]')
			span_click("保存")
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("外币业务对接--跨境外币汇款，修改成功！")
			time.sleep(3)
			
			# 测试送审功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入跨境外币汇款界面
			switch_to("xpath", '//*[@id="externalCrossBorderPayments-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			# 送审
			span_click("送审")
			ok_click()
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("外币业务对接--跨境外币汇款，送审成功！")
			time.sleep(3)
			
			# 测试撤销送审功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入跨境外币汇款界面
			switch_to("xpath", '//*[@id="externalCrossBorderPayments-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			# 修改
			triangle_cick_and_element("送审",'撤销送审')
			ok_click()
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'撤销送审成功！')]")
			print("外币业务对接--跨境外币汇款，送审成功！")
			time.sleep(3)
			
			# 测试余额检测💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入跨境外币汇款界面
			switch_to("xpath", '//*[@id="externalCrossBorderPayments-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			# 送审
			span_click("余额检测")
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'余额充足')]")
			print("外币业务对接--跨境外币汇款，余额检测成功！")
			time.sleep(3)
			
			# 测试作废💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入跨境外币汇款界面
			switch_to("xpath", '//*[@id="externalCrossBorderPayments-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("作废")
			ok_click()
			span_click("确定")
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("外币业务对接--跨境外币汇款，作废成功！")
			time.sleep(3)
			
			# 测试支付功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入跨境外币汇款界面
			switch_to("xpath", '//*[@id="externalCrossBorderPayments-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			# 送审
			span_click("送审")
			ok_click()
			sleep(3)
			
			double_click("xpath",'//*[@id="grid-body-table"]/tbody/tr[1]/td[3]/div')
			sleep(1)
			switch_to("xpath",'//*[@id="wf_taskProcessing_win-iframe"]')
			span_click("同意")
			switch_parent()
			
			double_click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[3]/div')
			sleep(1)
			switch_to("xpath", '//*[@id="wf_taskProcessing_win-iframe"]')
			span_click("同意")
			switch_parent()
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("支付")
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！1笔进行了支付，0笔不允许支付。')]")
			print("外币业务对接--跨境外币汇款，支付成功！")
			time.sleep(3)
			
			# 测试查询支付状态功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			sql = "update t_se_payments set paystate = '7' where purpose = '外币业务对接快捷付款申请'"
			ora_sql(ora_ip, ora_sid, ora_user, ora_pwd,
			       sql)
			# 切入跨境外币汇款界面
			switch_to("xpath", '//*[@id="externalCrossBorderPayments-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			# 送审
			span_click("查询支付状态")
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'单据已查询状态，请查看相应结果！')]")
			print("外币业务对接--跨境外币汇款，查询支付状态成功！")
			time.sleep(3)
			
			# 测试确认已支付功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			sql = "update t_se_payments set paystate = '7' where purpose = '外币业务对接快捷付款申请'"
			ora_sql(ora_ip, ora_sid, ora_user, ora_pwd,
			       sql)
			# 切入跨境外币汇款界面
			switch_to("xpath", '//*[@id="externalCrossBorderPayments-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			# 送审
			span_click("确认已支付")
			ok_click()
			ok_click()
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("外币业务对接--跨境外币汇款，确认已支付成功！")
			time.sleep(3)
			
			
			
			# 测试审批历史💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入跨境外币汇款界面
			switch_to("xpath", '//*[@id="externalCrossBorderPayments-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			# 送审
			span_click("审批历史")
			switch_to("xpath", '//*[@id="flowwin-iframe"]')
			sleep(3)
			span_click("流程流转")
			sleep(1)
			implici_wait("xpath", "//div[contains(text(),'开始')]")
			print("外币业务对接--跨境外币汇款，审批历史查看成功！")
			switch_parent()
			click("xpath", '//*[@id="f-win-title-flowwin"]/div[1]/div')
			sleep(1)
			switch_default()
			time.sleep(3)
			
			# 测试支付日志查看💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入跨境外币汇款界面
			switch_to("xpath", '//*[@id="externalCrossBorderPayments-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			# 送审
			span_click("支付日志查看")
			switch_to("xpath",'//*[@id="logsWin-iframe"]')
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//div[contains(text(),'支付')]")
			print("外币业务对接--跨境外币汇款，支付日志查看成功！")
			switch_parent()
			click("xpath",'//*[@id="f-win-title-logsWin"]/div[1]/div')
			sleep(1)
			switch_default()
			sleep(3)
			
			# 测试确认非直联已支付功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			sql = "update t_se_payments set paystate = '3' where purpose = '外币业务对接快捷付款申请'"
			ora_sql(ora_ip, ora_sid, ora_user, ora_pwd,
			       sql)
			# 切入跨境外币汇款界面
			switch_to("xpath", '//*[@id="externalCrossBorderPayments-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			# 送审
			span_click("确认非直联已支付")
			ok_click()
			switch_to("xpath", '//*[@id="confirmUndirectPayWin-iframe"]')
			input("xpath", '//*[@id="combobox-input-actualsettlementmodeid"]', '601-其他支付')
			sleep(1)
			input_down("xpath", '//*[@id="combobox-input-actualsettlementmodeid"]')
			input_enter("xpath", '//*[@id="combobox-input-actualsettlementmodeid"]')
			sleep(1)
			
			span_click("确定")
			ok_click()
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'共1笔，处理成功1笔，失败0笔。')]")
			print("外币业务对接--跨境外币汇款，确认非直联已支付成功！")
			time.sleep(3)
			
			# 测试打印功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入跨境外币汇款界面
			switch_to("xpath", '//*[@id="externalCrossBorderPayments-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("打印")
			# 获取所有窗口句柄
			all_handles = self.driver.window_handles
			# 循环遍历所有新打开的窗口句柄，也就是说不包括主窗口
			now_handle = self.driver.current_window_handle
			for handle in all_handles:
				self.driver.switch_to.window(handle)
				if self.driver.title == u"payandrecsingleprint":
					implici_wait("xpath", "//td[contains(text(),'韩国_首尔')]")
					print("跨境外币汇款-直联单笔支付，打印成功!！")
					time.sleep(3)
					self.driver.switch_to.window(now_handle)
					switch_default()
			
			# 测试打印记录功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入跨境外币汇款界面
			switch_to("xpath", '//*[@id="externalCrossBorderPayments-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			# 送审
			triangle_cick_and_element("打印",'打印记录')
			switch_to("xpath", '//*[@id="printWin-iframe"]')
			# 用隐式等待方法等页面出现  操作人:mindy
			implici_wait("xpath", "//div[@title='操作人:mindy']")
			print("外币业务对接--跨境外币汇款，打印记录查看成功！")
			switch_parent()
			click("xpath", '//*[@id="f-win-title-printWin"]/div[1]/div')
			sleep(1)
			switch_default()
			sleep(3)
			
			# 测试冲正💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			sql = "update t_se_payments set paystate = '2' where purpose = '外币业务对接快捷付款申请'"
			ora_sql(ora_ip, ora_sid, ora_user, ora_pwd,
			       sql)
			# 切入跨境外币汇款界面
			switch_to("xpath", '//*[@id="externalCrossBorderPayments-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			# 送审
			span_click("冲正")
			# 切入冲正窗体
			switch_to("xpath", '//*[@id="reverseWin-iframe"]')
			# 冲正日期
			today = date.today()
			we = str(today) + " " + "08:30:00"
			input("xpath", '//*[@id="reversedate-input"]', we)
			sleep(1)
			
			# 冲正原因
			span_click("冲正日期")
			input("xpath", '//*[@id="reversalreason"]', '测试冲正')
			sleep(1)
			
			# 生成付款单
			click("xpath",'//*[@id="save"]/span/span')
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("外币业务对接--跨境外币汇款，冲正成功！")
			time.sleep(3)
			
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("直联跨境汇款失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
			
			# def tearDown(self):
			#     self.driver.quit()
			print("结束时间：", time.strftime("%Y-%m-%d %H:%M:%S"))
		
	
		# 测试外币收付结算--跨境外币汇款-离线跨境汇款🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱
		try:
			logger.info("测试外币收付结算--跨境外币汇款-离线跨境汇款")
			switch_default()
			sleep(3)
			click("xpath", "//span[text()='跨境外币汇款']")
			sleep(1)
			
			#添加结算方式💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			click("xpath", "//span[text()='外币业务对接']")
			sleep(1)
			# 点击基础设置
			click("xpath",
			      '/html/body/div[1]/div[1]/div/div[2]/div/div[2]/div/div/div/div[4]/div/div/ul/li[1]/a/span[2]')
			sleep(1)
			
			click("xpath", "//span[text()='结算方式']")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			
			switch_to("xpath", "//iframe[@id='settlementMode-tab-iframe']")
			# 用JS的方法点击新增按钮
			js_click("xpath", "//span[text()='新增']")
			sleep(1)
			# 切入新增的iframe窗体
			switch_to("xpath", "//iframe[@id='addWin-iframe']")
	
			# 输入代码
			input("xpath", "//input[@name='code']", "2056")
			sleep(1)
			
			# 输入名称
			input("xpath", "//input[@id='name']", "离线跨境汇款交易证")
			sleep(1)
			
			# 输入交易方向
			input_up_click('//*[@id="combobox-input-moneyway"]','支出')
			
			# 输入交易类型
			input_up_click('//*[@id="combobox-input-dealtype"]','信用证')
			
			span_click("保存")
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功')]")
			time.sleep(3)
			
			click("xpath", "//span[text()='交易类型']")
			sleep(1)
			switch_to('xpath', '//*[@id="payType-tab-iframe"]')
			
			#查询
			click("xpath",'//*[@id="north"]/div[2]/span')
			sleep(1)
			input("xpath",'//*[@id="code"]','3031')
			sleep(1)
			span_click("查询")
			click("xpath",'//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
			sleep(1)
			span_click("修改")
			
			switch_to("xpath",'//*[@id="modWin-iframe"]')
			click("xpath",'//*[@id="combobox-input-settlementmoderange"]')
			sleep(1)
			input("xpath",'//*[@id="combobox-input-settlementmoderange"]',"2056")
			sleep(1)
			click("xpath",'//*[@id="settlementmoderange-combogrid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			span_click("保存")
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功')]")
			time.sleep(3)
			
			#回到离线跨境汇款页面
			# 点击基础设置
			click("xpath",
			      '/html/body/div[1]/div[1]/div/div[2]/div/div[2]/div/div/div/div[4]/div/div/ul/li[1]/a/span[2]')
			sleep(1)
			click("xpath", "//span[text()='外币业务对接']")
			sleep(1)
			click("xpath",
			      '/html/body/div[1]/div[1]/div/div[2]/div/div[2]/div/div/div/div[4]/div/div/ul/li[10]/ul/li[2]/a/span[2]')
			sleep(1)
			switch_default()
			
			# 去跨境外币汇款页面做数据💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 点击'外币收付结算'菜单
			click("xpath", "//span[text()='外币业务对接']")
			sleep(1)
			click("xpath", "//span[text()='外币收付结算']")
			sleep(1)
			click("xpath", "//span[text()='跨境外币汇款']")
			sleep(1)
			switch_default()
			
			for i in range(1, 6):
				# 切入跨境外币汇款窗体
				switch_to("xpath", '//*[@id="crossBorderPayment-tab-iframe"]')
				# 点击其他支付
				span_click("其他支付")
				sleep(1)
				# 进入其他支付窗体
				switch_to("xpath", '//*[@id="subTabThree-iframe"]')
				
				# 点击新增按钮
				span_click("新增")
				sleep(1)
				# 切入新增窗体
				switch_to("xpath", '//*[@id="addWin-iframe"]')
				
				# 组织机构代码
				input("xpath", '//*[@id="ourregorgcode"]', "001010")
				sleep(1)
				
				# 交易类型
				if i ==1 :
					input("xpath", '//*[@id="combobox-input-paytypeid"]', '3031-直联跨境外币汇款-其他支付')
					sleep(1)
					up_enter_click('//*[@id="combobox-input-paytypeid"]')
					input_up_click('//*[@id="combobox-input-settlementmodeid"]','2056')
				else :
					input("xpath", '//*[@id="combobox-input-paytypeid"]', '3031-直联跨境外币汇款-其他支付')
					sleep(1)
					up_enter_click('//*[@id="combobox-input-paytypeid"]')
					input_up_click('//*[@id="combobox-input-settlementmodeid"]', '601')
				# 汇款币种
				input("xpath", '//*[@id="combobox-input-ourcurrencyid"]', "CNY")
				sleep(1)
				up_enter_click('//*[@id="combobox-input-ourcurrencyid"]')
				
				# 汇款金额
				money = random.randint(100, 300)
				double_click("xpath", '//*[@id="ouramount-input"]')
				sleep(1)
				input("xpath", '//*[@id="ouramount-input"]', money)
				sleep(1)
				
				# 购汇账户
				input("xpath", '//*[@id="combobox-input-purchasebankaccountid"]', '20211031')
				sleep(1)
				up_enter_click('//*[@id="combobox-input-purchasebankaccountid"]')
				
				# 购汇汇率
				double_click("xpath", '//*[@id="purchaseexchangerate-input"]')
				sleep(1)
				input("xpath", '//*[@id="purchaseexchangerate-input"]', "1")
				sleep(1)
				# 去除下拉框
				double_click("xpath", '//*[@id="feeaccountinfo"]')
				sleep(1)
				
				# 收方名称
				input("xpath", '//*[@id="combobox-input-oppcounterpartyid"]', '浙江彩旗科技')
				sleep(1)
				# 清除下拉框
				double_click("xpath", '//*[@id="feeaccountinfo"]')
				sleep(1)
				
				# 收方账户
				click("xpath", '//*[@id="combobox-input-oppcounterpartyaccountid"]')
				sleep(1)
				input("xpath", '//*[@id="combobox-input-oppcounterpartyaccountid"]', '200848199612')
				sleep(1)
				# 清除下拉框
				double_click("xpath", '//*[@id="feeaccountinfo"]')
				sleep(1)
				
				# 收方类型
				click("xpath", '//*[@id="combobox-input-oppresidenttype"]')
				sleep(1)
				input_down("xpath", '//*[@id="combobox-input-oppresidenttype"]')
				input_enter("xpath", '//*[@id="combobox-input-oppresidenttype"]')
				sleep(1)
				
				# 收方地址
				input("xpath", '//*[@id="oppaddress"]', '浙江杭州')
				sleep(1)
				
				# 收方开户银行
				input("xpath", '//*[@id="combobox-input-oppbanklocationid"]', '（韩国地区）中国农业银行首尔支行')
				sleep(1)
				click("xpath", '//*[@id="oppbanklocationid-combogrid-body-table"]/tbody/tr/td[2]/div')
				sleep(1)
				
				# 用途
				input("xpath", '//*[@id="combobox-input-purpose"]', "跨境外币汇款离线跨境汇款")
				sleep(1)
				
				# 付款方式
				click("xpath", '//*[@id="combobox-input-paymentmethod"]')
				sleep(1)
				input_down("xpath", '//*[@id="combobox-input-paymentmethod"]')
				input_enter("xpath", '//*[@id="combobox-input-paymentmethod"]')
				sleep(1)
				
				# 国内外费用承担人
				click("xpath", '//*[@id="combobox-input-intermediatecostmode"]')
				sleep(1)
				input_down("xpath", '//*[@id="combobox-input-intermediatecostmode"]')
				input_enter("xpath", '//*[@id="combobox-input-intermediatecostmode"]')
				sleep(1)
				
				# 付汇性质
				click("xpath", '//*[@id="combobox-input-paymentproperty"]')
				sleep(1)
				input_down("xpath", '//*[@id="combobox-input-paymentproperty"]')
				input_enter("xpath", '//*[@id="combobox-input-paymentproperty"]')
				sleep(1)
				
				# 交易编码
				click("xpath", '//*[@id="combobox-input-transactioncode1"]')
				sleep(1)
				input_down("xpath", '//*[@id="combobox-input-transactioncode1"]')
				input_enter("xpath", '//*[@id="combobox-input-transactioncode1"]')
				sleep(1)
				
				# 保存
				span_click("保存")
				sleep(1)
				# 退出所有iframe窗体
				switch_default()
				# 用隐式等待方法等页面出现新增成功的提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功')]")
				time.sleep(3)
			sql = "update t_se_payments set RECORDSOURCE = '4' where purpose = '跨境外币汇款离线跨境汇款'"
			ora_sql(ora_ip, ora_sid, ora_user, ora_pwd,
			       sql)
			
			# 回到快捷付款申请页面
			click("xpath", "//span[text()='外币收付结算']")
			sleep(1)
			click("xpath", "//span[text()='外币业务对接']")
			sleep(1)
			switch_default()
			click("xpath",
			      '/html/body/div[1]/div[1]/div/div[2]/div/div[2]/div/div/div/div[4]/div/div/ul/li[10]/ul/li[2]/a/span[2]')
			sleep(1)
			
			# 测试修改功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入跨境外币汇款界面
			switch_to("xpath", '//*[@id="externalCrossBorderPayments-tab-iframe"]')
			span_click("离线跨境汇款")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
	
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			# 修改
			span_click("修改")
			switch_to("xpath", '//*[@id="modWin-iframe"]')
			span_click("保存")
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("外币业务对接--离线跨境汇款，修改成功！")
			time.sleep(3)
			
			# 测试送审功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入跨境外币汇款界面
			switch_to("xpath", '//*[@id="externalCrossBorderPayments-tab-iframe"]')
			span_click("离线跨境汇款")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			# 修改
			span_click("送审")
			ok_click()
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("外币业务对接--离线跨境汇款，送审成功！")
			time.sleep(3)
			
			# 测试撤销送审功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入跨境外币汇款界面
			switch_to("xpath", '//*[@id="externalCrossBorderPayments-tab-iframe"]')
			span_click("离线跨境汇款")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("送审",'撤销送审')
			ok_click()
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'撤销送审成功！')]")
			print("外币业务对接--离线跨境汇款，撤销送审成功！")
			time.sleep(3)
			
			# 测试确认支付功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入跨境外币汇款界面
			switch_to("xpath", '//*[@id="externalCrossBorderPayments-tab-iframe"]')
			span_click("离线跨境汇款")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("送审")
			ok_click()
			sleep(3)
			double_click("xpath",'//*[@id="t1_t0"]/td[1]/div/span')
			sleep(1)
			switch_to("xpath",'//*[@id="wf_taskProcessing_win-iframe"]')
			span_click("同意")
			switch_parent()
			sleep(3)
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("确认支付")
			span_click("确定")
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("外币业务对接--离线跨境汇款，确认支付成功！")
			time.sleep(3)
	
			# 测试打印功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入跨境外币汇款界面
			switch_to("xpath", '//*[@id="externalCrossBorderPayments-tab-iframe"]')
			span_click("离线跨境汇款")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("打印")
			# 获取所有窗口句柄
			all_handles = self.driver.window_handles
			# 循环遍历所有新打开的窗口句柄，也就是说不包括主窗口
			now_handle = self.driver.current_window_handle
			for handle in all_handles:
				self.driver.switch_to.window(handle)
				if self.driver.title == u"payandrecsingleprint":
					implici_wait("xpath", "//td[contains(text(),'韩国_首尔')]")
					print("外币业务对接--离线跨境汇款，打印成功！")
					time.sleep(3)
					self.driver.switch_to.window(now_handle)
					switch_default()
					
			
			# 测试审批历史功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入跨境外币汇款界面
			switch_to("xpath", '//*[@id="externalCrossBorderPayments-tab-iframe"]')
			span_click("离线跨境汇款")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("审批历史")
			switch_to("xpath", '//*[@id="flowwin-iframe"]')
			sleep(3)
			span_click("流程流转")
			sleep(1)
			implici_wait("xpath", "//div[contains(text(),'开始')]")
			print("外币业务对接--离线跨境汇款，审批历史查看成功！")
			switch_parent()
			click("xpath", '//*[@id="f-win-title-flowwin"]/div[1]/div')
			switch_default()
			sleep(3)
		
			# 测试终止功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入跨境外币汇款界面
			switch_to("xpath", '//*[@id="externalCrossBorderPayments-tab-iframe"]')
			span_click("离线跨境汇款")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t3-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("终止")
			ok_click()
			input("xpath",'//*[@id="terminateReason"]','测试终止')
			sleep(1)
			click("xpath","//div[contains(text(),'终止原因')]")
			sleep(1)
			click("xpath",'/html/body/div[5]/div[16]/div/div[2]/div[1]/div/form/div[3]/a[1]/span/span')
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("外币业务对接--离线跨境汇款，终止成功！")
			time.sleep(3)
			
			# 测试拆分功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入跨境外币汇款界面
			switch_to("xpath", '//*[@id="externalCrossBorderPayments-tab-iframe"]')
			span_click("离线跨境汇款")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t2-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("拆分")
			ok_click()
			switch_to("xpath",'//*[@id="splitWin-iframe"]')
			
			#拆分金额
			double_click("xpath",'//*[@id="splitingamount-input"]')
			sleep(1)
			input("xpath",'//*[@id="splitingamount-input"]','15')
			sleep(1)
			span_click("保存")
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("外币业务对接--离线跨境汇款，拆分成功！")
			time.sleep(3)
			
			# 测试审核功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入跨境外币汇款界面
			switch_to("xpath", '//*[@id="externalCrossBorderPayments-tab-iframe"]')
			span_click("离线跨境汇款")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t1-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("审核")
			ok_click()
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("外币业务对接--离线跨境汇款，审核成功！")
			time.sleep(3)
			
			# 测试撤销审核功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入跨境外币汇款界面
			switch_to("xpath", '//*[@id="externalCrossBorderPayments-tab-iframe"]')
			span_click("离线跨境汇款")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t1-fixed"]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("审核","取消审核")
			ok_click()
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'取消审核成功！')]")
			print("外币业务对接--离线跨境汇款，取消审核成功！")
			time.sleep(3)
			
			# 测试核对并确认付款功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入跨境外币汇款界面
			switch_to("xpath", '//*[@id="externalCrossBorderPayments-tab-iframe"]')
			span_click("离线跨境汇款")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t1-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("审核")
			ok_click()
			sleep(1)
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t1-fixed"]/td[2]/div/button')
			sleep(1)
			triangle_cick_and_element("确认支付",'核对并确认付款')
			switch_to("xpath",'//*[@id="confirmPayWin-iframe"]')
			click("xpath",'//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			span_click("确认")
			ok_click()
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("外币业务对接--离线跨境汇款，核对并确认付款成功！")
			time.sleep(3)
			
			# 测试冲正功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入跨境外币汇款界面
			switch_to("xpath", '//*[@id="externalCrossBorderPayments-tab-iframe"]')
			span_click("离线跨境汇款")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			# 点击冲正按钮
			span_click("冲正")
			# 切入冲正窗体
			switch_to("xpath", '//*[@id="reverseWin-iframe"]')
			sleep(1)
			# 冲正日期
			we = str(date.today())
			input("xpath", '//*[@id="reversedate-input"]', we)
			sleep(1)
			
			# 冲正原因
			span_click("冲正日期")
			input("xpath", '//*[@id="reversalreason"]', '测试冲正')
			sleep(1)
			
			# 生成付款单
			span_click("提交")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("外币业务对接--离线跨境汇款，冲正成功！")
			time.sleep(3)
			
			# 测试作废功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入跨境外币汇款界面
			switch_to("xpath", '//*[@id="externalCrossBorderPayments-tab-iframe"]')
			span_click("离线跨境汇款")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t3_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("作废")
			ok_click()
			click("xpath",'/html/body/div[5]/div[17]/div/div[2]/div[1]/div/form/div[3]/a[1]/span/span')
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("外币业务对接--离线跨境汇款，作废成功！")
			time.sleep(3)
			
			# 测试开证功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入跨境外币汇款界面
			switch_to("xpath", '//*[@id="externalCrossBorderPayments-tab-iframe"]')
			span_click("离线跨境汇款")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t5-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("开证")
			switch_to("xpath",'//*[@id="implocredits-iframe"]')
			sleep(3)
			#融资产品
			click("xpath",'//*[@id="combobox-input-credittypeid"]')
			sleep(1)
			click("xpath", '//*[@id="credittypeid-combogrid-body-table"]/tbody/tr/td[2]/div')
			sleep(1)
			
			
			#信用证号码
			coad=str(time.strftime("%Y%m%d%H%M%S"))
			input("xpath",'//*[@id="creditnumber"]',coad)
			sleep(1)
			
			#开证银行
			input_up_click('//*[@id="combobox-input-issuingbankid"]','中国银行')
			
			span_click("保存")
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("外币业务对接--离线跨境汇款，开证成功！")
			time.sleep(3)
			
			# 测试开证信息功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入跨境外币汇款界面
			switch_to("xpath", '//*[@id="externalCrossBorderPayments-tab-iframe"]')
			span_click("离线跨境汇款")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t5-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("查看开证信息")
			switch_to("xpath",'//*[@id="lookimplocredits-iframe"]')
		
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'组织')]")
			print("外币业务对接--离线跨境汇款，查看开证信息成功！")
			click("xpath",'/html/body/div[1]/div[1]/div/div[2]/div/div[2]/div/div/div/div[4]/div/div/ul/li[10]/ul/li[2]/a/span[2]')
			sleep(1)
			time.sleep(3)

		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("直联跨境汇款失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
			
			# def tearDown(self):
			#     self.driver.quit()
			print("结束时间：", time.strftime("%Y-%m-%d %H:%M:%S"))
		
		
		# 测试外币收付结算--全球外币汇款-直联全球汇款🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱
		try:
			logger.info("测试外币收付结算--全球外币汇款-直联全球汇款")
			switch_default()
			sleep(3)
			click("xpath", "//span[text()='全球外币汇款']")
			sleep(1)
		
			# 去直联全球汇款页面做数据💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 点击'外币收付结算'菜单
			click("xpath", "//span[text()='外币业务对接']")
			sleep(1)
			click("xpath", "//span[text()='外币收付结算']")
			sleep(1)
			click("xpath", "//span[text()='全球汇款']")
			sleep(1)
			switch_default()
			
			for i in range(1, 3):
				# 切入全球汇款界面
				switch_to("xpath", '//*[@id="outsidePayment-tab-iframe"]')
				switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
				# 点击新增
				span_click("新增")
				sleep(1)
				switch_to("xpath", '//*[@id="addWin-iframe"]')
				
				# 组织机构代码
				input("xpath", '//*[@id="ourregorgcode"]', '001010')
				sleep(1)
				
				# 交易类型
				input("xpath", '//*[@id="combobox-input-paytypeid"]', '3032-全球汇款直联单笔交易类型')
				sleep(1)
				input_down("xpath", '//*[@id="combobox-input-paytypeid"]')
				input_enter("xpath", '//*[@id="combobox-input-paytypeid"]')
				sleep(1)
				
				# 汇款币种
				input("xpath", '//*[@id="combobox-input-ourcurrencyid"]', 'USD')
				sleep(1)
				input_down("xpath", '//*[@id="combobox-input-ourcurrencyid"]')
				input_enter("xpath", '//*[@id="combobox-input-ourcurrencyid"]')
				sleep(1)
				
				# 汇款金额
				money = random.randint(100, 300)
				double_click("xpath", '//*[@id="ouramount-input"]')
				sleep(1)
				input("xpath", '//*[@id="ouramount-input"]', money)
				sleep(1)
				
				# 汇款银行
				input("xpath", '//*[@id="combobox-input-paybankid"]', 'BOC-中国银行')
				sleep(1)
				input_down("xpath", '//*[@id="combobox-input-paybankid"]')
				input_enter("xpath", '//*[@id="combobox-input-paybankid"]')
				sleep(1)
				
				# 付款账户
				input("xpath", '//*[@id="combobox-input-ourbankaccountid"]', '20211032')
				sleep(1)
				input_down("xpath", '//*[@id="combobox-input-ourbankaccountid"]')
				input_enter("xpath", '//*[@id="combobox-input-ourbankaccountid"]')
				sleep(1)
				
				# 收方名称
				input("xpath", '//*[@id="combobox-input-oppcounterpartyid"]', '浙江蓝旗科技')
				sleep(1)
				# 清除下拉框
				double_click("xpath", '//*[@id="cashaccountinfo"]')
				sleep(1)
				
				# 收方账户
				click("xpath", '//*[@id="combobox-input-oppcounterpartyaccountid"]')
				sleep(1)
				input("xpath", '//*[@id="combobox-input-oppcounterpartyaccountid"]', '200848199613')
				sleep(1)
				# 清除下拉框
				double_click("xpath", '//*[@id="cashaccountinfo"]')
				sleep(1)
				
				# 收方地址
				input("xpath", '//*[@id="oppaddress"]', '浙江杭州')
				sleep(1)
				
				# 收方开户银行
				input("xpath", '//*[@id="combobox-input-oppbanklocationid"]', '中国人民银行寿县支行')
				sleep(1)
				click("xpath", '//*[@id="oppbanklocationid-combogrid-body-table"]/tbody/tr/td[2]/div')
				sleep(1)
				
				# 用途
				input("xpath", '//*[@id="combobox-input-purpose"]', "全球外币汇款直联全球汇款")
				sleep(1)
				
				# 国内外费用承担人
				click("xpath", '//*[@id="combobox-input-intermediatecostmode"]')
				sleep(1)
				input_down("xpath", '//*[@id="combobox-input-intermediatecostmode"]')
				input_enter("xpath", '//*[@id="combobox-input-intermediatecostmode"]')
				sleep(1)
				
				# 保存
				span_click("保存")
				sleep(1)
				# 退出所有iframe窗体
				switch_default()
				# 用隐式等待方法等页面出现新增成功的提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功')]")
				time.sleep(3)
			
			sql = "update t_se_payments set RECORDSOURCE = '4' where purpose = '全球外币汇款直联全球汇款'"
			ora_sql(ora_ip, ora_sid, ora_user, ora_pwd,
			       sql)
			
			# 回到快捷付款申请页面
			click("xpath", "//span[text()='外币收付结算']")
			sleep(1)
			click("xpath", "//span[text()='外币业务对接']")
			sleep(1)
			click("xpath", "//span[text()='全球外币汇款']")
			sleep(1)
			switch_default()
			
			# 测试修改功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			#切入直联全球汇款页面
			switch_to("xpath",'//*[@id="externalOutsidePayments-tab-iframe"]')
			switch_to("xpath",'//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			#刷新、勾选按钮
			click("xpath",'//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath",'//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("修改")
			switch_to("xpath",'//*[@id="modWin-iframe"]')
			span_click("保存")
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("全球外币汇款--直联全球汇款，修改成功！")
			time.sleep(3)
			
			# 测试送审功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入直联全球汇款页面
			switch_to("xpath", '//*[@id="externalOutsidePayments-tab-iframe"]')
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
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("全球外币汇款--直联全球汇款，送审成功！")
			time.sleep(3)
			
			# 测试撤销送审功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入直联全球汇款页面
			switch_to("xpath", '//*[@id="externalOutsidePayments-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("送审","撤销送审")
			ok_click()
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'撤销送审成功！')]")
			print("全球外币汇款--直联全球汇款，撤销送审成功！")
			time.sleep(3)
			
			# 测试审批历史功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入直联全球汇款页面
			switch_to("xpath", '//*[@id="externalOutsidePayments-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("审批历史")
			
			switch_to("xpath", '//*[@id="flowwin-iframe"]')
			sleep(3)
			span_click("流程流转")
			sleep(1)
			implici_wait("xpath", "//div[contains(text(),'开始')]")
			print("全球外币汇款--直联全球汇款，审批历史查看成功！")
			switch_parent()
			click("xpath", '//*[@id="f-win-title-flowwin"]/div[1]/div')
			sleep(1)
			switch_default()
			time.sleep(3)
			
			# 测试余额检测功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入直联全球汇款页面
			switch_to("xpath", '//*[@id="externalOutsidePayments-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("余额检测")
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'余额充足')]")
			print("全球外币汇款--直联全球汇款，余额检测成功！")
			time.sleep(3)
			
			# 测试支付功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入直联全球汇款页面
			switch_to("xpath", '//*[@id="externalOutsidePayments-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
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
			span_click("同意")
			switch_parent()
			
			double_click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[3]/div')
			sleep(1)
			switch_to("xpath",'//*[@id="wf_taskProcessing_win-iframe"]')
			span_click("同意")
			switch_parent()
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("支付")
	
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("全球外币汇款--直联全球汇款，支付成功！")
			time.sleep(3)
			
			# 测试作废功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入直联全球汇款页面
			switch_to("xpath", '//*[@id="externalOutsidePayments-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[2]/td[2]/div/button')
			sleep(1)
			
			span_click("作废")
			ok_click()
			span_click("确定")
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("全球外币汇款--直联全球汇款，作废成功！")
			time.sleep(3)
			
			
			
			# 测试查询支付状态功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			sql = "update t_se_payments set paystate = '7' where purpose = '全球外币汇款直联全球汇款'"
			ora_sql(ora_ip, ora_sid, ora_user, ora_pwd,
			       sql)
			# 切入直联全球汇款页面
			switch_to("xpath", '//*[@id="externalOutsidePayments-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("查询支付状态")
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'单据已查询状态，请查看相应结果！')]")
			print("全球外币汇款--直联全球汇款，查询支付状态成功！")
			time.sleep(3)
			
			# 测试确认已支付功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			sql = "update t_se_payments set paystate = '7' where purpose = '全球外币汇款直联全球汇款'"
			ora_sql(ora_ip, ora_sid, ora_user, ora_pwd,
			       sql)
			# 切入直联全球汇款页面
			switch_to("xpath", '//*[@id="externalOutsidePayments-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("确认已支付")
			ok_click()
			ok_click()
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("全球外币汇款--直联全球汇款，确认已支付成功！")
			time.sleep(3)
			
			# 测试打印功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入直联全球汇款页面
			switch_to("xpath", '//*[@id="externalOutsidePayments-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("打印")
			# 获取所有窗口句柄
			all_handles = self.driver.window_handles
			# 循环遍历所有新打开的窗口句柄，也就是说不包括主窗口
			now_handle = self.driver.current_window_handle
			for handle in all_handles:
				self.driver.switch_to.window(handle)
				if self.driver.title == u"payandrecsingleprint":
					implici_wait("xpath", "//td[contains(text(),'韩国_安山')]")
					print("全球外币汇款--直联全球汇款，打印成功！")
					time.sleep(3)
					self.driver.switch_to.window(now_handle)
					switch_default()
			
			
			# 测试打印记录功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入直联全球汇款页面
			switch_to("xpath", '//*[@id="externalOutsidePayments-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("打印",'打印记录')
			switch_to("xpath", '//*[@id="printWin-iframe"]')
			# 用隐式等待方法等页面出现  操作人:mindy
			implici_wait("xpath", "//div[@title='操作人:mindy']")
			print("全球外币汇款--直联全球汇款，打印记录查看成功！")
			switch_parent()
			click("xpath", '//*[@id="f-win-title-printWin"]/div[1]/div')
			sleep(1)
			switch_default()
			sleep(3)
			
			# 测试支付日志查看功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入直联全球汇款页面
			switch_to("xpath", '//*[@id="externalOutsidePayments-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("支付日志查看")
			switch_to("xpath", '//*[@id="logsWin-iframe"]')
			# 用隐式等待方法等页面出现  操作人:mindy
			implici_wait("xpath", "//div[contains(text(),'支付')]")
			print("全球外币汇款--直联全球汇款，支付日志查看成功！")
			switch_parent()
			click("xpath", '//*[@id="f-win-title-logsWin"]/div[1]/div')
			sleep(1)
			switch_default()
			sleep(3)
			
			# 测试非直联已支付💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			sql = "update t_se_payments set paystate = '3' where purpose = '全球外币汇款直联全球汇款'"
			ora_sql(ora_ip, ora_sid, ora_user, ora_pwd,
			       sql)
			# 切入直联全球汇款页面
			switch_to("xpath", '//*[@id="externalOutsidePayments-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("确认非直联已支付")
			ok_click()
			switch_to("xpath",'//*[@id="confirmUndirectPayWin-iframe"]')
			click_up_click('//*[@id="combobox-input-actualsettlementmodeid"]')
			span_click("确定")
			ok_click()
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'共1笔，处理成功1笔，失败0笔。')]")
			print("全球外币汇款--直联全球汇款，确认非直联已支付成功！")
			time.sleep(3)
			
			# 测试冲正💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入直联全球汇款页面
			switch_to("xpath", '//*[@id="externalOutsidePayments-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("冲正")
			
			switch_to("xpath", '//*[@id="reverseWin-iframe"]')
			# 冲正日期
			today = date.today()
			we = str(today) + " " + "08:30:00"
			input("xpath", '//*[@id="reversedate-input"]', we)
			sleep(1)
			
			# 冲正原因
			span_click("冲正日期")
			input("xpath", '//*[@id="reversalreason"]', '测试冲正')
			sleep(1)
			
			# 生成付款单
			span_click("确认冲正")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("全球外币汇款--直联全球汇款，冲正成功！")
			time.sleep(3)
			
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("直联全球汇款失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
			
			# def tearDown(self):
			#     self.driver.quit()
			print("结束时间：", time.strftime("%Y-%m-%d %H:%M:%S"))
		
		
		# 测试外币收付结算--全球外币汇款-离线全球汇款🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱
		try:
			logger.info("测试外币收付结算--全球外币汇款-离线全球汇款")
			switch_default()
			sleep(3)
			click("xpath", "//span[text()='全球外币汇款']")
			sleep(1)
			
			# 去直联全球汇款页面做数据💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 点击'外币收付结算'菜单
			click("xpath", "//span[text()='外币业务对接']")
			sleep(1)
			click("xpath", "//span[text()='外币收付结算']")
			sleep(1)
			click("xpath", "//span[text()='全球汇款']")
			sleep(1)
			switch_default()
			
			for i in range(1, 4):
				# 切入全球汇款界面
				switch_to("xpath", '//*[@id="outsidePayment-tab-iframe"]')
				span_click("其他支付")
				sleep(1)
				switch_to("xpath", '//*[@id="subTabThree-iframe"]')
				# 点击新增
				span_click("新增")
				sleep(1)
				switch_to("xpath", '//*[@id="addWin-iframe"]')
				
				# 组织机构代码
				input("xpath", '//*[@id="ourregorgcode"]', '001010')
				sleep(1)
				
				# 交易类型
				input("xpath", '//*[@id="combobox-input-paytypeid"]', '3034-全球汇款其他支付交易类型')
				sleep(1)
				input_down("xpath", '//*[@id="combobox-input-paytypeid"]')
				input_enter("xpath", '//*[@id="combobox-input-paytypeid"]')
				sleep(1)
				
				# 汇款币种
				input("xpath", '//*[@id="combobox-input-ourcurrencyid"]', 'USD')
				sleep(1)
				input_down("xpath", '//*[@id="combobox-input-ourcurrencyid"]')
				input_enter("xpath", '//*[@id="combobox-input-ourcurrencyid"]')
				sleep(1)
				
				# 汇款金额
				money = random.randint(100, 300)
				double_click("xpath", '//*[@id="ouramount-input"]')
				sleep(1)
				input("xpath", '//*[@id="ouramount-input"]', money)
				sleep(1)
				
				# 付款账户
				click("xpath", '//*[@id="combobox-input-ourbankaccountid"]')
				sleep(1)
				input("xpath", '//*[@id="combobox-input-ourbankaccountid"]', '20211034')
				sleep(1)
				input_down("xpath", '//*[@id="combobox-input-ourbankaccountid"]')
				input_enter("xpath", '//*[@id="combobox-input-ourbankaccountid"]')
				sleep(1)
				
				# 收方名称
				input("xpath", '//*[@id="combobox-input-oppcounterpartyid"]', '浙江蓝旗科技')
				sleep(1)
				# 清除下拉框
				double_click("xpath", '//*[@id="cashaccountinfo"]')
				sleep(1)
				
				# 收方账户
				click("xpath", '//*[@id="combobox-input-oppcounterpartyaccountid"]')
				sleep(1)
				input("xpath", '//*[@id="combobox-input-oppcounterpartyaccountid"]', '200848199613')
				sleep(1)
				# 清除下拉框
				double_click("xpath", '//*[@id="cashaccountinfo"]')
				sleep(1)
				
				# 收方地址
				input("xpath", '//*[@id="oppaddress"]', '浙江杭州')
				sleep(1)
				
				# 收方开户银行
				input("xpath", '//*[@id="combobox-input-oppbanklocationid"]', '中国人民银行寿县支行')
				sleep(1)
				click("xpath", '//*[@id="oppbanklocationid-combogrid-body-table"]/tbody/tr/td[2]/div')
				sleep(1)
				
				# 用途
				input("xpath", '//*[@id="combobox-input-purpose"]', "全球外币汇款离线全球汇款")
				sleep(1)
				
				# 保存
				span_click("保存")
				sleep(1)
				# 退出所有iframe窗体
				switch_default()
				# 用隐式等待方法等页面出现新增成功的提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功')]")
				time.sleep(3)
			
			
			sql = "update t_se_payments set RECORDSOURCE = '4' where purpose = '全球外币汇款离线全球汇款'"
			ora_sql(ora_ip, ora_sid, ora_user, ora_pwd,
			       sql)
			
			# 回到快捷付款申请页面
			click("xpath", "//span[text()='外币收付结算']")
			sleep(1)
			click("xpath", "//span[text()='外币业务对接']")
			sleep(1)
			click("xpath", "//span[text()='全球外币汇款']")
			sleep(1)
			switch_default()
			
			# 测试修改功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入直联全球汇款页面
			switch_to("xpath", '//*[@id="externalOutsidePayments-tab-iframe"]')
			span_click("离线全球汇款")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("修改")
			switch_to("xpath",'//*[@id="modWin-iframe"]')
			span_click("保存")
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("全球外币汇款--离线全球汇款，修改成功！")
			time.sleep(3)
			
			# 测试送审功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入直联全球汇款页面
			switch_to("xpath", '//*[@id="externalOutsidePayments-tab-iframe"]')
			span_click("离线全球汇款")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
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
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("全球外币汇款--离线全球汇款，送审成功！")
			time.sleep(3)
			
			# 测试撤销送审功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入直联全球汇款页面
			switch_to("xpath", '//*[@id="externalOutsidePayments-tab-iframe"]')
			span_click("离线全球汇款")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("送审","撤销送审")
			ok_click()
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'撤销送审成功！')]")
			print("全球外币汇款--离线全球汇款，撤销送审成功！")
			time.sleep(3)
			
			# 测试审批历史功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入直联全球汇款页面
			switch_to("xpath", '//*[@id="externalOutsidePayments-tab-iframe"]')
			span_click("离线全球汇款")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("审批历史")
			switch_to("xpath", '//*[@id="flowwin-iframe"]')
			sleep(3)
			span_click("流程流转")
			sleep(1)
			implici_wait("xpath", "//div[contains(text(),'开始')]")
			sleep(3)
			print("全球外币汇款--离线全球汇款，审批历史查看成功！")
			switch_parent()
			click("xpath", '//*[@id="f-win-title-flowwin"]/div[1]/div')
			sleep(1)
			switch_default()
			time.sleep(3)
			
			# 测试作废功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入直联全球汇款页面
			switch_to("xpath", '//*[@id="externalOutsidePayments-tab-iframe"]')
			span_click("离线全球汇款")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("作废")
			ok_click()
			span_click("确定")
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("全球外币汇款--离线全球汇款，作废成功！")
			time.sleep(3)
			
			# 测试审核功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入直联全球汇款页面
			switch_to("xpath", '//*[@id="externalOutsidePayments-tab-iframe"]')
			span_click("离线全球汇款")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
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
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("全球外币汇款--离线全球汇款，审核成功！")
			time.sleep(3)
			
			# 测试取消审核功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入直联全球汇款页面
			switch_to("xpath", '//*[@id="externalOutsidePayments-tab-iframe"]')
			span_click("离线全球汇款")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
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
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'取消审核成功！')]")
			print("全球外币汇款--离线全球汇款，取消审核成功！")
			time.sleep(3)
			
			# 测试确认支付功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入直联全球汇款页面
			switch_to("xpath", '//*[@id="externalOutsidePayments-tab-iframe"]')
			span_click("离线全球汇款")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("审核")
			ok_click()
			sleep(3)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			span_click("确认支付")
			span_click("确定")
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("全球外币汇款--离线全球汇款，确定支付成功！")
			time.sleep(3)
			
			# 测试打印功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入直联全球汇款页面
			switch_to("xpath", '//*[@id="externalOutsidePayments-tab-iframe"]')
			span_click("离线全球汇款")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			# 点击打印按钮
			span_click("打印")
			# 获取所有窗口句柄
			all_handles = self.driver.window_handles
			# 循环遍历所有新打开的窗口句柄，也就是说不包括主窗口
			now_handle = self.driver.current_window_handle
			for handle in all_handles:
				self.driver.switch_to.window(handle)
				if self.driver.title == u"payandrecsingleprint":
					implici_wait("xpath", "//td[contains(text(),'浙江蓝旗科技')]")
					print("全球外币汇款--离线全球汇款，打印成功！")
					time.sleep(3)
					self.driver.switch_to.window(now_handle)
					switch_default()
			
			# 测试冲正功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入直联全球汇款页面
			switch_to("xpath", '//*[@id="externalOutsidePayments-tab-iframe"]')
			span_click("离线全球汇款")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("冲正")
			# 切入冲正窗体
			switch_to("xpath", '//*[@id="reverseWin-iframe"]')
			# 冲正日期
			today = date.today()
			we = str(today)
			input("xpath", '//*[@id="reversedate-input"]', we)
			sleep(1)
			
			# 冲正原因
			span_click("冲正原因")
			input("xpath", '//*[@id="reversalreason"]', '测试冲正')
			sleep(1)
			
			# 生成付款单
			span_click("提交")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("全球外币汇款--离线全球汇款，冲正成功！")
			time.sleep(3)
			
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("离线全球汇款失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
			
			# def tearDown(self):
			#     self.driver.quit()
			print("结束时间：", time.strftime("%Y-%m-%d %H:%M:%S"))
		
		
		
		# 测试外币收付结算--结购换汇处理--直联结购换汇🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱
		try:
			logger.info("测试外币收付结算--结购换汇处理--直联结购换汇")
			switch_default()
			sleep(3)
			click("xpath", "//span[text()='结购换汇处理']")
			sleep(1)
			
			# 去直联结购换汇页面做数据💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 点击'外币收付结算'菜单
			click("xpath", "//span[text()='外币业务对接']")
			sleep(1)
			click("xpath", "//span[text()='资金系统收付']")
			sleep(1)
			click("xpath", "//span[text()='结购换汇']")
			sleep(1)
			switch_default()
			
			for i in range(1, 3):
				
				switch_to("xpath", "//iframe[@id='exchangePay-tab-iframe']")
				switch_to("xpath", "//iframe[@id='subTabOne-iframe']")
				# 点击新增
				click("xpath", "//span[text()='新增']")
				sleep(1)
				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='addWin-iframe']")
				# 输入结构代码
				input("xpath", "//input[@id='ourregorgcode']", "001010")
				sleep(1)
				
				# 交易类型
				click("xpath", "//input[@id='combobox-input-paytypeid']")
				# 输入开户行大连泡崖街支行名称，模糊查询
				input("xpath", "//input[@id='combobox-input-paytypeid']", "3028-购汇交易类型")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-paytypeid']")
				input_enter("xpath", "//input[@id='combobox-input-paytypeid']")
				time.sleep(2)
				
				# 购汇账户
				input("xpath", "//input[@id='combobox-input-ourbankaccountid']", "20211028")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-ourbankaccountid']")
				input_enter("xpath", "//input[@id='combobox-input-ourbankaccountid']")
				sleep(1)
				
				# 收方账户
				input("xpath", "//input[@id='combobox-input-oppbankaccountid']", "2021102801")
				sleep(1)
				input_enter("xpath", "//input[@id='combobox-input-oppbankaccountid']")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-oppbankaccountid']")
				sleep(1)
				input_enter("xpath", "//input[@id='combobox-input-oppbankaccountid']")
				sleep(1)
				
				# 输入结汇金额
				money = random.randint(100, 300)
				clear("xpath", "//input[@id='amount-input']")
				sleep(1)
				input("xpath", "//input[@id='amount-input']", money)
				sleep(1)
				
				# 用途
				input("xpath", "//input[@id='combobox-input-purpose']", "结购换汇处理直联结购换汇")
				sleep(1)
				
				# 点击保存按钮
				click("xpath", "//span[text()='保存']")
				sleep(1)
				# 退出所有iframe窗体
				switch_default()
				# 用隐式等待方法等页面出现新增成功的提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				time.sleep(3)
			
			sql = "update t_se_payments set RECORDSOURCE = '4' where purpose = '结购换汇处理直联结购换汇'"
			ora_sql(ora_ip, ora_sid, ora_user, ora_pwd,
			       sql)
			
			# 回到快捷付款申请页面
			click("xpath", "//span[text()='资金系统收付']")
			sleep(1)
			click("xpath", "//span[text()='外币业务对接']")
			sleep(1)
			click("xpath", "//span[text()='结购换汇处理']")
			sleep(1)
			switch_default()
		
			# 测试修改功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入直联全球汇款页面
			switch_to("xpath",'//*[@id="externalExchangePay-tab-iframe"]')
			switch_to("xpath",'//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			#刷新、勾选按钮
			click("xpath",'//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath",'//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("修改")
			switch_to("xpath",'//*[@id="modWin-iframe"]')
			sleep(3)
			span_click("保存")
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("结购换汇处理--直联结购换汇，修改成功！")
			time.sleep(3)
			
			# 测试送审功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入直联全球汇款页面
			switch_to("xpath", '//*[@id="externalExchangePay-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("送审")
		
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("结购换汇处理--直联结购换汇，送审成功！")
			time.sleep(3)
			
			# 测试撤销送审功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入直联全球汇款页面
			switch_to("xpath", '//*[@id="externalExchangePay-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("送审","撤销送审")
			ok_click()
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'撤销送审成功！')]")
			print("结购换汇处理--直联结购换汇，撤销送审成功！")
			time.sleep(3)
			
			# 测试作废功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入直联全球汇款页面
			switch_to("xpath", '//*[@id="externalExchangePay-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[2]/td[2]/div/button')
			sleep(1)
			
			span_click("作废")
			ok_click()
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("结购换汇处理--直联结购换汇，作废成功！")
			time.sleep(3)
			
			# 测试余额检测功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入直联全球汇款页面
			switch_to("xpath", '//*[@id="externalExchangePay-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("支付", "余额检测")
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'当前余额为')]")
			print("结购换汇处理--直联结购换汇，余额检测成功！")
			time.sleep(3)
			
			# 测试支付功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入直联全球汇款页面
			switch_to("xpath", '//*[@id="externalExchangePay-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("送审")
			sleep(3)
			double_click("xpath",'//*[@id="grid-body-table"]/tbody/tr/td[3]/div')
			sleep(1)
			switch_to("xpath",'//*[@id="wf_taskProcessing_win-iframe"]')
			span_click("同意")
			switch_parent()
			sleep(3)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("支付")
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("结购换汇处理--联直结购换汇，支付成功！")
			time.sleep(3)
			
			# 测试查询状态功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			sql = "update t_se_payments set paystate = '7' where purpose = '结购换汇处理直联结购换汇'"
			ora_sql(ora_ip, ora_sid, ora_user, ora_pwd,
			       sql)
			# 切入直联全球汇款页面
			switch_to("xpath", '//*[@id="externalExchangePay-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			
			triangle_cick_and_element("支付",'查询状态')
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'单据已查询状态，请查看相应结果！')]")
			print("结购换汇处理--直联结购换汇，查询支付状态成功！")
			time.sleep(3)
			
			
			# 测试确认已支付功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			sql = "update t_se_payments set paystate = '7' where purpose = '结购换汇处理直联结购换汇'"
			ora_sql(ora_ip, ora_sid, ora_user, ora_pwd,
			       sql)
			# 切入直联全球汇款页面
			switch_to("xpath", '//*[@id="externalExchangePay-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("支付", "确认已支付")
			ok_click()
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'共1笔，处理成功1笔，失败0笔。')]")
			print("结购换汇处理--直联结购换汇，确认已支付成功！")
			time.sleep(3)
			
			# 测试确认非直联已支付功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			sql = "update t_se_payments set paystate = '3' where purpose = '结购换汇处理直联结购换汇'"
			ora_sql(ora_ip, ora_sid, ora_user, ora_pwd,
			       sql)
			# 切入直联全球汇款页面
			switch_to("xpath", '//*[@id="externalExchangePay-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("支付", "确认非直联已支付")
			ok_click()
			switch_to("xpath",'//*[@id="confirmUndirectPayWin-iframe"]')
			click_up_click('//*[@id="combobox-input-actualsettlementmodeid"]')
			span_click("确定")
			ok_click()
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'共1笔，处理成功1笔，失败0笔。')]")
			print("结购换汇处理--直联结购换汇，确认非直联已支付成功！")
			time.sleep(3)
			
			# 测试日志查看功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入直联全球汇款页面
			switch_to("xpath", '//*[@id="externalExchangePay-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("支付", "日志查看")
			
			# 退出所有iframe窗体
			switch_to("xpath",'//*[@id="logsWin-iframe"]')
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//div[contains(text(),'支付')]")
			print("结购换汇处理--直联结购换汇，查看日志成功！")
			time.sleep(3)
			switch_parent()
			click("xpath",'//*[@id="f-win-title-logsWin"]/div[1]/div')
			sleep(1)
			switch_default()
			
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("直联结购换汇！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
			
			# def tearDown(self):
			#     self.driver.quit()
			print("结束时间：", time.strftime("%Y-%m-%d %H:%M:%S"))
		
		'''
		# 测试外币收付结算--结购换汇处理--离线结购换汇🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱
		try:
			logger.info("测试外币收付结算--结购换汇处理--离线结购换汇")
			switch_default()
			sleep(3)
			click("xpath", "//span[text()='结购换汇处理']")
			sleep(1)
			'''
			# 去直联结购换汇页面做数据💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 点击'外币收付结算'菜单
			click("xpath", "//span[text()='外币业务对接']")
			sleep(1)
			click("xpath", "//span[text()='资金系统收付']")
			sleep(1)
			click("xpath", "//span[text()='结购换汇']")
			sleep(1)
			switch_default()
			
			for i in range(1, 3):
				# 切入结购换汇的iframe窗体
				switch_to("xpath", "//iframe[@id='exchangePay-tab-iframe']")
				# 点击其他结购换汇
				click("xpath", "//span[text()='其他结购换汇']")
				sleep(1)
				switch_to("xpath", "//iframe[@id='subTabTwo-iframe']")
				# 点击新增
				click("xpath", "//span[text()='新增']")
				sleep(1)
				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='addWin-iframe']")
				# 交易类型
				click("xpath", "//input[@id='combobox-input-paytypeid']")
				# 输入开户行大连泡崖街支行名称，模糊查询
				input("xpath", "//input[@id='combobox-input-paytypeid']", "3029-其他购汇交易类型")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-paytypeid']")
				input_enter("xpath", "//input[@id='combobox-input-paytypeid']")
				time.sleep(1)
				
				# 选择结算方式
				click("xpath", "//input[@id='combobox-input-settlementmodeid']")
				clear("xpath", "//input[@id='combobox-input-settlementmodeid']")
				sleep(1)
				# 输入开户行大连泡崖街支行名称，模糊查询
				input("xpath", "//input[@id='combobox-input-settlementmodeid']", "601-其他支付")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-settlementmodeid']")
				input_enter("xpath", "//input[@id='combobox-input-settlementmodeid']")
				time.sleep(1)
				
				# 购汇账户
				input("xpath", '//*[@id="combobox-input-lbankaccountid"]', "20211029")
				sleep(1)
				input_down("xpath", '//*[@id="combobox-input-lbankaccountid"]')
				input_enter("xpath", '//*[@id="combobox-input-lbankaccountid"]')
				sleep(1)
				
				# 输入购汇金额
				money = random.randint(100, 300)
				double_click("xpath", '//*[@id="lamount-input"]')
				sleep(1)
				input("xpath", '//*[@id="lamount-input"]', money)
				sleep(1)
				
				# 收方账户
				input("xpath", '//*[@id="combobox-input-fbankaccountid"]', "2021102901")
				sleep(1)
				input_down("xpath", '//*[@id="combobox-input-fbankaccountid"]')
				sleep(1)
				input_enter("xpath", '//*[@id="combobox-input-fbankaccountid"]')
				sleep(1)
				
				# 输入收方金额
				double_click("xpath", '//*[@id="famount-input"]')
				sleep(1)
				input("xpath", '//*[@id="famount-input"]', money * 6)
				sleep(1)
				
				# 用途
				input("xpath", "//input[@id='combobox-input-purpose']", "结购换汇处理离线结购换汇")
				sleep(1)
				
				# 点击保存按钮
				click("xpath", "//span[text()='保存']")
				sleep(1)
				# 退出所有iframe窗体
				switch_default()
				
				# 用隐式等待方法等页面出现新增成功的提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				time.sleep(3)
			
			
			sql = "update t_se_payments set RECORDSOURCE = '4' where purpose = '结购换汇处理离线结购换汇'"
			ora_sql(ora_ip, ora_sid, ora_user, ora_pwd,
			       sql)
			
			# 回到快捷付款申请页面
			click("xpath", "//span[text()='资金系统收付']")
			sleep(1)
			click("xpath", "//span[text()='外币业务对接']")
			sleep(1)
			click("xpath", "//span[text()='结购换汇处理']")
			sleep(1)
			switch_default()
			
			# 测试修改功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入直联全球汇款页面
			switch_to("xpath", '//*[@id="externalExchangePay-tab-iframe"]')
			span_click("离线结购换汇")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("修改")
			switch_to("xpath", '//*[@id="modWin-iframe"]')
			sleep(3)
			span_click("保存")
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("结购换汇处理--离线结购换汇，修改成功！")
			time.sleep(3)
			
			# 测试送审功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入直联全球汇款页面
			switch_to("xpath", '//*[@id="externalExchangePay-tab-iframe"]')
			span_click("离线结购换汇")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("送审")
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("结购换汇处理--离线结购换汇，送审成功！")
			time.sleep(3)
			
			# 测试撤销送审功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入直联全球汇款页面
			switch_to("xpath", '//*[@id="externalExchangePay-tab-iframe"]')
			span_click("离线结购换汇")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
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
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'撤销送审成功！')]")
			print("结购换汇处理--离线结购换汇，撤销送审成功！")
			time.sleep(3)
			
			# 测试作废功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入直联全球汇款页面
			switch_to("xpath", '//*[@id="externalExchangePay-tab-iframe"]')
			span_click("离线结购换汇")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[2]/td[2]/div/button')
			sleep(1)
			
			span_click("作废")
			ok_click()
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("结购换汇处理--离线结购换汇，作废成功！")
			time.sleep(3)
			
			# 测试支付功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入直联全球汇款页面
			switch_to("xpath", '//*[@id="externalExchangePay-tab-iframe"]')
			span_click("离线结购换汇")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("送审")
			sleep(3)
			double_click("xpath",'//*[@id="grid-body-table"]/tbody/tr/td[3]/div')
			sleep(1)
			switch_to("xpath",'//*[@id="wf_taskProcessing_win-iframe"]')
			span_click("同意")
			switch_parent()
			sleep(3)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			span_click("支付")
			span_click("确定")
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'确认支付成功！')]")
			print("结购换汇处理--离线结购换汇，支付成功！")
			time.sleep(3)
			'''
			# 测试审批历史功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入直联全球汇款页面
			switch_to("xpath", '//*[@id="externalExchangePay-tab-iframe"]')
			span_click("离线结购换汇")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("审批历史")
			switch_to("xpath",'//*[@id="flowwin-iframe"]')
			sleep(3)
			span_click("流程流转")
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//div[contains(text(),'张中国')]")
			print("结购换汇处理--离线结购换汇，审批历史查看成功！")
			switch_parent()
			click("xpath",'//*[@id="f-win-title-flowwin"]/div[1]/div')
			time.sleep(3)
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("离线结购换汇！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
			
			# def tearDown(self):
			#     self.driver.quit()
			print("结束时间：", time.strftime("%Y-%m-%d %H:%M:%S"))
			
		
		
		# 测试外币收付结算--境内外币汇款--直联境内外币汇款🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱
		try:
			logger.info("测试外币收付结算--境内外币汇款--直联境内外币汇款")
			switch_default()
			sleep(3)
			click("xpath", "//span[text()='境内外币汇款']")
			sleep(1)
			
			# 去直联结购换汇页面做数据💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 点击'外币收付结算'菜单
			click("xpath", "//span[text()='外币业务对接']")
			sleep(1)
			click("xpath", "//span[text()='外币收付结算']")
			sleep(1)
			click("xpath", "//span[text()='境内外币汇款']")
			sleep(1)
			switch_default()
			
			for i in range(1, 3):
				# 切入境内外币汇款界面
				switch_to("xpath", '//*[@id="domiticpayment-tab-iframe"]')
				switch_to("xpath", '//*[@id="subTabOne-iframe"]')
				# 点击新增
				span_click("新增")
				sleep(1)
				# 切入新增窗体
				switch_to("xpath", '//*[@id="addWin-iframe"]')
				# 组织机构代码
				input("xpath", '//*[@id="ourregorgcode"]', '001010')
				sleep(1)
				
				# 交易类型
				input("xpath", '//*[@id="combobox-input-paytypeid"]', '3035')
				sleep(1)
				input_down("xpath", '//*[@id="combobox-input-paytypeid"]')
				input_enter("xpath", '//*[@id="combobox-input-paytypeid"]')
				sleep(1)
				
				# 汇款币种
				input("xpath", '//*[@id="combobox-input-ourcurrencyid"]', 'USD')
				sleep(1)
				input_down("xpath", '//*[@id="combobox-input-ourcurrencyid"]')
				input_enter("xpath", '//*[@id="combobox-input-ourcurrencyid"]')
				sleep(1)
				
				# 汇款金额
				money = random.randint(100, 300)
				double_click("xpath", '//*[@id="ouramount-input"]')
				sleep(1)
				input("xpath", '//*[@id="ouramount-input"]', money)
				sleep(1)
				
				# 汇款银行
				input("xpath", '//*[@id="combobox-input-paybankid"]', 'BOC-中国银行')
				sleep(1)
				input_down("xpath", '//*[@id="combobox-input-paybankid"]')
				input_enter("xpath", '//*[@id="combobox-input-paybankid"]')
				sleep(1)
				
				# 购汇账户
				input("xpath", '//*[@id="combobox-input-purchasebankaccountid"]', '20211035')
				sleep(1)
				input_down("xpath", '//*[@id="combobox-input-purchasebankaccountid"]')
				input_enter("xpath", '//*[@id="combobox-input-purchasebankaccountid"]')
				sleep(1)
				
				# 购汇汇率
				double_click("xpath", '//*[@id="purchaseexchangerate-input"]')
				sleep(1)
				input("xpath", '//*[@id="purchaseexchangerate-input"]', '1')
				# 去除下拉框
				double_click("xpath", '//*[@id="feeaccountinfo"]')
				sleep(1)
				
				# 收方名称
				input("xpath", '//*[@id="combobox-input-oppcounterpartyid"]', '浙江紫旗科技')
				sleep(1)
				# 清除下拉框
				double_click("xpath", '//*[@id="feeaccountinfo"]')
				sleep(1)
				
				# 收方账户
				click("xpath", '//*[@id="combobox-input-oppcounterpartyaccountid"]')
				sleep(1)
				input("xpath", '//*[@id="combobox-input-oppcounterpartyaccountid"]', '200848199614')
				sleep(1)
				# 清除下拉框
				double_click("xpath", '//*[@id="feeaccountinfo"]')
				sleep(1)
				
				# 收方类型
				click("xpath", '//*[@id="combobox-input-oppresidenttype"]')
				sleep(1)
				input_down("xpath", '//*[@id="combobox-input-oppresidenttype"]')
				input_enter("xpath", '//*[@id="combobox-input-oppresidenttype"]')
				sleep(1)
				
				# 收方地址
				input("xpath", '//*[@id="oppaddress"]', '浙江杭州')
				sleep(1)
				
				# 收方开户银行
				input("xpath", '//*[@id="combobox-input-oppbanklocationid"]', '中国人民银行寿县支行')
				sleep(1)
				click("xpath", '//*[@id="oppbanklocationid-combogrid-body-table"]/tbody/tr/td[2]/div')
				sleep(1)
				
				# 收方SWIFT代码
				input("xpath", '//*[@id="oppbranchswiftcode"]', '8781731')
				sleep(1)
				
				# 收方SWIFT名称
				input("xpath", '//*[@id="oppbranchswiftname"]', 'SWIFT')
				sleep(1)
				# 用途
				input("xpath", '//*[@id="combobox-input-purpose"]', "境内外币汇款直联境内外币汇款")
				sleep(1)
				
				# 付款方式
				click("xpath", '//*[@id="combobox-input-paymentmethod"]')
				sleep(1)
				input_down("xpath", '//*[@id="combobox-input-paymentmethod"]')
				input_enter("xpath", '//*[@id="combobox-input-paymentmethod"]')
				sleep(1)
				
				# 国内外费用承担人
				click("xpath", '//*[@id="combobox-input-intermediatecostmode"]')
				sleep(1)
				input_down("xpath", '//*[@id="combobox-input-intermediatecostmode"]')
				input_enter("xpath", '//*[@id="combobox-input-intermediatecostmode"]')
				sleep(1)
				
				# 付汇性质
				click("xpath", '//*[@id="combobox-input-paymentproperty"]')
				sleep(1)
				input_down("xpath", '//*[@id="combobox-input-paymentproperty"]')
				input_enter("xpath", '//*[@id="combobox-input-paymentproperty"]')
				sleep(1)
				
				# 交易编码
				click("xpath", '//*[@id="combobox-input-transactioncode1"]')
				sleep(1)
				input_down("xpath", '//*[@id="combobox-input-transactioncode1"]')
				input_enter("xpath", '//*[@id="combobox-input-transactioncode1"]')
				sleep(1)
				
				# 保存
				span_click("保存")
				sleep(1)
				# 退出所有iframe窗体
				switch_default()
				# 用隐式等待方法等页面出现新增成功的提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功')]")
				time.sleep(3)
			
			sql = "update t_se_payments set RECORDSOURCE = '4' where purpose = '境内外币汇款直联境内外币汇款'"
			ora_sql(ora_ip, ora_sid, ora_user, ora_pwd,
			       sql)
			
			# 回到快捷付款申请页面
			click("xpath", "//span[text()='外币收付结算']")
			sleep(1)
			click("xpath", "//span[text()='外币业务对接']")
			sleep(1)
			click("xpath", "/html/body/div[1]/div[1]/div/div[2]/div/div[2]/div/div/div/div[4]/div/div/ul/li[10]/ul/li[5]/a/span[2]")
			sleep(1)
			switch_default()
			
			# 测试修改功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入直联境内外币汇款页面
			switch_to("xpath", '//*[@id="externalDomesticPay-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("修改")
			switch_to("xpath", '//*[@id="modWin-iframe"]')
			sleep(3)
			span_click("保存")
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("境内外币汇款--直联境内外币汇款，修改成功！")
			time.sleep(3)
			
			# 测试送审功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入直联境内外币汇款页面
			switch_to("xpath", '//*[@id="externalDomesticPay-tab-iframe"]')
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
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("境内外币汇款--直联境内外币汇款，送审成功！")
			time.sleep(3)
			
			# 测试撤销送审功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入直联境内外币汇款页面
			switch_to("xpath", '//*[@id="externalDomesticPay-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("送审","撤销送审")
			ok_click()
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'撤销送审成功！')]")
			print("境内外币汇款--直联境内外币汇款，撤销送审成功！")
			time.sleep(3)
			
			# 测试作废功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入直联境内外币汇款页面
			switch_to("xpath", '//*[@id="externalDomesticPay-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("作废")
			ok_click()
			span_click("确定")
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("境内外币汇款--直联境内外币汇款，作废成功！")
			time.sleep(3)
			
			# 测试余额检测功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入直联境内外币汇款页面
			switch_to("xpath", '//*[@id="externalDomesticPay-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("余额检测")
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'余额充足')]")
			print("境内外币汇款--直联境内外币汇款，余额检测成功！")
			time.sleep(3)
			
			# 测试支付功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入直联境内外币汇款页面
			switch_to("xpath", '//*[@id="externalDomesticPay-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
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
			span_click("同意")
			switch_parent()
			sleep(3)
			
			double_click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[3]/div')
			sleep(1)
			switch_to("xpath", '//*[@id="wf_taskProcessing_win-iframe"]')
			span_click("同意")
			switch_parent()
			sleep(3)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("支付")
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("境内外币汇款--直联境内外币汇款，支付成功！")
			time.sleep(3)
			
			# 测试查询支付状态功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			sql = "update t_se_payments set paystate = '7' where purpose = '境内外币汇款直联境内外币汇款'"
			ora_sql(ora_ip, ora_sid, ora_user, ora_pwd,
			       sql)
			# 切入直联境内外币汇款页面
			switch_to("xpath", '//*[@id="externalDomesticPay-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("查询支付状态")
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'单据已查询状态，请查看相应结果！')]")
			print("境内外币汇款--直联境内外币汇款，查询支付状态成功！")
			time.sleep(3)
			
			# 测试确认已支付功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			sql = "update t_se_payments set paystate = '7' where purpose = '境内外币汇款直联境内外币汇款'"
			ora_sql(ora_ip, ora_sid, ora_user, ora_pwd,
			       sql)
			# 切入直联境内外币汇款页面
			switch_to("xpath", '//*[@id="externalDomesticPay-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("确认已支付")
			ok_click()
			ok_click()
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("境内外币汇款--直联境内外币汇款，确认已支付成功！")
			time.sleep(3)
			
			# 测试打印功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入直联境内外币汇款页面
			switch_to("xpath", '//*[@id="externalDomesticPay-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("打印")
			# 获取所有窗口句柄
			all_handles = self.driver.window_handles
			# 循环遍历所有新打开的窗口句柄，也就是说不包括主窗口
			now_handle = self.driver.current_window_handle
			for handle in all_handles:
				self.driver.switch_to.window(handle)
				if self.driver.title == u"payandrecsingleprint":
					implici_wait("xpath", "//td[contains(text(),'浙江紫旗科技')]")
					print("境内外币汇款--直联境内外币汇款，打印成功！")
					time.sleep(3)
					self.driver.switch_to.window(now_handle)
					switch_default()
			
			
			# 测试打印记录功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入直联境内外币汇款页面
			switch_to("xpath", '//*[@id="externalDomesticPay-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("打印","打印记录")
			switch_to("xpath",'//*[@id="printWin-iframe"]')
			
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//div[contains(text(),'mindy')]")
			print("境内外币汇款--直联境内外币汇款，打印记录查看成功！")
			switch_parent()
			click("xpath",'//*[@id="f-win-title-printWin"]/div[1]/div')
			sleep(1)
			switch_default()
			sleep(3)
			
			# 测试审批历史功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入直联境内外币汇款页面
			switch_to("xpath", '//*[@id="externalDomesticPay-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("审批历史")
			switch_to("xpath",'//*[@id="flowwin-iframe"]')
			sleep(3)
			span_click("流程流转")
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//div[contains(text(),'开始')]")
			print("境内外币汇款--直联境内外币汇款，审批历史查看成功！")
			switch_parent()
			click("xpath",'//*[@id="f-win-title-flowwin"]/div[1]/div')
			sleep(1)
			switch_default()
			time.sleep(3)
			
			# 测试支付日志查看功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入直联境内外币汇款页面
			switch_to("xpath", '//*[@id="externalDomesticPay-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("支付日志查看")
			switch_to("xpath", '//*[@id="logsWin-iframe"]')
			
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//div[contains(text(),'支付')]")
			print("境内外币汇款--直联境内外币汇款，支付日志查看成功！")
			switch_parent()
			click("xpath", '//*[@id="f-win-title-logsWin"]/div[1]/div')
			sleep(1)
			switch_default()
			time.sleep(3)
			
			
			
			# 测试非直联已支付功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			sql = "update t_se_payments set paystate = '3' where purpose = '境内外币汇款直联境内外币汇款'"
			ora_sql(ora_ip, ora_sid, ora_user, ora_pwd,
			       sql)
			# 切入直联境内外币汇款页面
			switch_to("xpath", '//*[@id="externalDomesticPay-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("确认非直联已支付")
			ok_click()
			switch_to("xpath",'//*[@id="confirmUndirectPayWin-iframe"]')
			click_up_click('//*[@id="combobox-input-actualsettlementmodeid"]')
			span_click("确定")
			ok_click()
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'共1笔，处理成功1笔，失败0笔。')]")
			print("境内外币汇款--直联境内外币汇款，确认非直联已支付成功！")
			time.sleep(3)
			
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("离线结购换汇！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
			
			# def tearDown(self):
			#     self.driver.quit()
			print("结束时间：", time.strftime("%Y-%m-%d %H:%M:%S"))
		
		
		# 测试外币收付结算--境内外币汇款--离线境内外币汇款🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱
		try:
			logger.info("测试外币收付结算--境内外币汇款--离线境内外币汇款")
			switch_default()
			sleep(3)
			click("xpath", "//span[text()='境内外币汇款']")
			sleep(1)
			
			# 去直联结购换汇页面做数据💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 点击'外币收付结算'菜单
			click("xpath", "//span[text()='外币业务对接']")
			sleep(1)
			click("xpath", "//span[text()='外币收付结算']")
			sleep(1)
			click("xpath", "//span[text()='境内外币汇款']")
			sleep(1)
			switch_default()
			
			for i in range(1, 5):
				# 切入境内外币汇款窗体
				switch_to("xpath", '//*[@id="domiticpayment-tab-iframe"]')
				# 点击其他支付
				span_click("其他支付")
				sleep(1)
				# 进入其他支付窗体
				switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
				
				# 点击新增按钮
				span_click("新增")
				sleep(1)
				# 切入新增窗体
				switch_to("xpath", '//*[@id="addWin-iframe"]')
				
				# 组织机构代码
				input("xpath", '//*[@id="ourregorgcode"]', "001010")
				sleep(1)
				
				# 交易类型
				input("xpath", '//*[@id="combobox-input-paytypeid"]', '3036-境内外币汇款其他支付')
				sleep(1)
				up_enter_click('//*[@id="combobox-input-paytypeid"]')
				
				# 汇款币种
				input("xpath", '//*[@id="combobox-input-ourcurrencyid"]', "USD")
				sleep(1)
				up_enter_click('//*[@id="combobox-input-ourcurrencyid"]')
				
				# 汇款金额
				money = random.randint(100, 300)
				double_click("xpath", '//*[@id="ouramount-input"]')
				sleep(1)
				input("xpath", '//*[@id="ouramount-input"]', money)
				sleep(1)
				
				# 购汇账户
				input("xpath", '//*[@id="combobox-input-purchasebankaccountid"]', '20211036')
				sleep(1)
				up_enter_click('//*[@id="combobox-input-purchasebankaccountid"]')
				
				# 购汇汇率
				double_click("xpath", '//*[@id="purchaseexchangerate-input"]')
				sleep(1)
				input("xpath", '//*[@id="purchaseexchangerate-input"]', "1")
				sleep(1)
				# 去除下拉框
				double_click("xpath", '//*[@id="feeaccountinfo"]')
				sleep(1)
				
				# 收方名称
				input("xpath", '//*[@id="combobox-input-oppcounterpartyid"]', '浙江彩旗科技')
				sleep(1)
				# 清除下拉框
				double_click("xpath", '//*[@id="feeaccountinfo"]')
				sleep(1)
				
				# 收方账户
				click("xpath", '//*[@id="combobox-input-oppcounterpartyaccountid"]')
				sleep(1)
				input("xpath", '//*[@id="combobox-input-oppcounterpartyaccountid"]', '200848199612')
				sleep(1)
				# 清除下拉框
				double_click("xpath", '//*[@id="feeaccountinfo"]')
				sleep(1)
				
				# 收方类型
				click("xpath", '//*[@id="combobox-input-oppresidenttype"]')
				sleep(1)
				input_down("xpath", '//*[@id="combobox-input-oppresidenttype"]')
				input_enter("xpath", '//*[@id="combobox-input-oppresidenttype"]')
				sleep(1)
				
				# 收方地址
				input("xpath", '//*[@id="oppaddress"]', '浙江杭州')
				sleep(1)
				
				# 收方开户银行
				input("xpath", '//*[@id="combobox-input-oppbanklocationid"]', '中国人民银行寿县支行')
				sleep(1)
				click("xpath", '//*[@id="oppbanklocationid-combogrid-body-table"]/tbody/tr/td[2]/div')
				sleep(1)
				
				# 收方SWIFT代码
				input("xpath", '//*[@id="oppbranchswiftcode"]', '8781731')
				sleep(1)
				
				# 收方SWIFT名称
				input("xpath", '//*[@id="oppbranchswiftname"]', 'SWIFT')
				sleep(1)
				
				# 用途
				input("xpath", '//*[@id="combobox-input-purpose"]', "境内外币汇款离线境内外币汇款")
				sleep(1)
				
				# 付款方式
				click("xpath", '//*[@id="combobox-input-paymentmethod"]')
				sleep(1)
				input_down("xpath", '//*[@id="combobox-input-paymentmethod"]')
				input_enter("xpath", '//*[@id="combobox-input-paymentmethod"]')
				sleep(1)
				
				# 国内外费用承担人
				click("xpath", '//*[@id="combobox-input-intermediatecostmode"]')
				sleep(1)
				input_down("xpath", '//*[@id="combobox-input-intermediatecostmode"]')
				input_enter("xpath", '//*[@id="combobox-input-intermediatecostmode"]')
				sleep(1)
				
				# 付汇性质
				click("xpath", '//*[@id="combobox-input-paymentproperty"]')
				sleep(1)
				input_down("xpath", '//*[@id="combobox-input-paymentproperty"]')
				input_enter("xpath", '//*[@id="combobox-input-paymentproperty"]')
				sleep(1)
				
				# 交易编码
				click("xpath", '//*[@id="combobox-input-transactioncode1"]')
				sleep(1)
				input_down("xpath", '//*[@id="combobox-input-transactioncode1"]')
				input_enter("xpath", '//*[@id="combobox-input-transactioncode1"]')
				sleep(1)
				
				# 保存
				span_click("保存")
				sleep(1)
				# 退出所有iframe窗体
				switch_default()
				# 用隐式等待方法等页面出现新增成功的提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功')]")
				time.sleep(3)
			
			sql = "update t_se_payments set RECORDSOURCE = '4' where purpose = '境内外币汇款离线境内外币汇款'"
			ora_sql(ora_ip, ora_sid, ora_user, ora_pwd,
			       sql)
			
			# 回到快捷付款申请页面
			click("xpath", "//span[text()='外币收付结算']")
			sleep(1)
			click("xpath", "//span[text()='外币业务对接']")
			sleep(1)
			click("xpath",
			      "/html/body/div[1]/div[1]/div/div[2]/div/div[2]/div/div/div/div[4]/div/div/ul/li[10]/ul/li[5]/a/span[2]")
			sleep(1)
			switch_default()
			
			# 测试修改功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入直联境内外币汇款页面
			switch_to("xpath", '//*[@id="externalDomesticPay-tab-iframe"]')
			span_click("离线境内外币汇款")
			switch_to("xpath", '//*[@id="subTabtwo-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("修改")
			switch_to("xpath", '//*[@id="modWin-iframe"]')
			sleep(3)
			span_click("保存")
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("境内外币汇款--离线境内外币汇款，修改成功！")
			time.sleep(3)
			
			# 测试送审功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入直联境内外币汇款页面
			switch_to("xpath", '//*[@id="externalDomesticPay-tab-iframe"]')
			span_click("离线境内外币汇款")
			switch_to("xpath", '//*[@id="subTabtwo-iframe"]')
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
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("境内外币汇款--离线境内外币汇款，送审成功！")
			time.sleep(3)
			
			# 测试撤销送审功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入直联境内外币汇款页面
			switch_to("xpath", '//*[@id="externalDomesticPay-tab-iframe"]')
			span_click("离线境内外币汇款")
			switch_to("xpath", '//*[@id="subTabtwo-iframe"]')
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
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'撤销送审成功！')]")
			print("境内外币汇款--离线境内外币汇款，撤销送审成功！")
			time.sleep(3)
			
			# 测试审批历史功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入直联境内外币汇款页面
			switch_to("xpath", '//*[@id="externalDomesticPay-tab-iframe"]')
			span_click("离线境内外币汇款")
			switch_to("xpath", '//*[@id="subTabtwo-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("审批历史")
			switch_to("xpath",'//*[@id="flowwin-iframe"]')
			sleep(3)
			span_click("流程流转")
			implici_wait("xpath", "//div[contains(text(),'开始')]")
			print("境内外币汇款--离线境内外币汇款，审批历史查看成功！")
			switch_parent()
			click("xpath",'//*[@id="f-win-title-flowwin"]/div[1]/div')
			sleep(1)
			switch_default()
			time.sleep(3)
			
			# 测试作废功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入直联境内外币汇款页面
			switch_to("xpath", '//*[@id="externalDomesticPay-tab-iframe"]')
			span_click("离线境内外币汇款")
			switch_to("xpath", '//*[@id="subTabtwo-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("作废")
			ok_click()
			span_click("确定")
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("境内外币汇款--离线境内外币汇款，作废成功！")
			time.sleep(3)
			
			# 测试审核功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入直联境内外币汇款页面
			switch_to("xpath", '//*[@id="externalDomesticPay-tab-iframe"]')
			span_click("离线境内外币汇款")
			switch_to("xpath", '//*[@id="subTabtwo-iframe"]')
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
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("境内外币汇款--离线境内外币汇款，审核成功！")
			time.sleep(3)
			
			# 测试取消审核功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入直联境内外币汇款页面
			switch_to("xpath", '//*[@id="externalDomesticPay-tab-iframe"]')
			span_click("离线境内外币汇款")
			switch_to("xpath", '//*[@id="subTabtwo-iframe"]')
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
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'取消审核成功！')]")
			print("境内外币汇款--离线境内外币汇款，取消审核成功！")
			time.sleep(3)
			
			# 测试确认支付功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入直联境内外币汇款页面
			switch_to("xpath", '//*[@id="externalDomesticPay-tab-iframe"]')
			span_click("离线境内外币汇款")
			switch_to("xpath", '//*[@id="subTabtwo-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("审核")
			ok_click()
			sleep(3)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			span_click("确认支付")
			span_click("确定")
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功')]")
			print("境内外币汇款--离线境内外币汇款，确认支付成功！")
			time.sleep(3)
			
			# 测终止功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入直联境内外币汇款页面
			switch_to("xpath", '//*[@id="externalDomesticPay-tab-iframe"]')
			span_click("离线境内外币汇款")
			switch_to("xpath", '//*[@id="subTabtwo-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t1-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("终止")
			ok_click()
			input("xpath",'//*[@id="terminateReason"]','测试终止')
			sleep(1)
			click("xpath",'//*[@id="determineTerminate"]/span/span')
			sleep(1)
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("境内外币汇款--离线境内外币汇款，终止成功！")
			time.sleep(3)
			
			# 测试打印功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入直联境内外币汇款页面
			switch_to("xpath", '//*[@id="externalDomesticPay-tab-iframe"]')
			span_click("离线境内外币汇款")
			switch_to("xpath", '//*[@id="subTabtwo-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("打印")
			# 获取所有窗口句柄
			all_handles = self.driver.window_handles
			# 循环遍历所有新打开的窗口句柄，也就是说不包括主窗口
			now_handle = self.driver.current_window_handle
			for handle in all_handles:
				self.driver.switch_to.window(handle)
				if self.driver.title == u"payandrecsingleprint":
					implici_wait("xpath", "//td[contains(text(),'浙江')]")
					print("境内外币汇款--离线境内外币汇款，打印成功！")
					time.sleep(3)
					self.driver.switch_to.window(now_handle)
					switch_default()
			
			# 测试冲正功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入直联境内外币汇款页面
			switch_to("xpath", '//*[@id="externalDomesticPay-tab-iframe"]')
			span_click("离线境内外币汇款")
			switch_to("xpath", '//*[@id="subTabtwo-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("冲正")
			# 切入冲正窗体
			switch_to("xpath", '//*[@id="reverseWin-iframe"]')
			# 冲正日期
			today = date.today()
			we = str(today)
			input("xpath", '//*[@id="reversedate-input"]', we)
			sleep(1)
			
			# 冲正原因
			span_click("冲正原因")
			input("xpath", '//*[@id="reversalreason"]', '测试冲正')
			sleep(1)
			
			# 生成付款单
			span_click("提交")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("境内外币汇款--离线境内外币汇款，冲正成功！")
			time.sleep(3)
			
			# 测试拆分功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入直联境内外币汇款页面
			switch_to("xpath", '//*[@id="externalDomesticPay-tab-iframe"]')
			span_click("离线境内外币汇款")
			switch_to("xpath", '//*[@id="subTabtwo-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t3-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("拆分")
			ok_click()
			switch_to("xpath",'//*[@id="splitWin-iframe"]')
			double_click("xpath",'//*[@id="splitingamount-input"]')
			sleep(1)
			input("xpath",'//*[@id="splitingamount-input"]','5')
			sleep(1)
			span_click("保存")
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("境内外币汇款--离线境内外币汇款，拆分成功！")
			time.sleep(3)
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("离线境内外币汇款失败！" + str(traceback.format_exc()))
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
