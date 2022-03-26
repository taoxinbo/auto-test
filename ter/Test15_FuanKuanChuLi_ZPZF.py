# encoding=utf-8
# @Time : 2020/10/19 14:49
# @Author : zzg
# 此文件是测试Mysql版本资金结算管理--资金系统收付--付款处理--支票支付
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


class Test15_FuanKuanChuLi_ZPZF(unittest.TestCase):
	
	# 启动浏览器
	def setUp(self):
		# 启动浏览器的另外一个方法：通过封装启动浏览器的驱动，启动不同浏览器
		self.driver = get("chrome")
	
	# 登陆系统、对系统设置进行操作
	def test_trade(self):
		
		login(G_Mys_Url, mindy, Password, "亚唐科技")
		
		
		logging.info("开始测试资金结算管理的页面功能")
		# 将页面的滚动条滑动到‘资金结算管理’页面的地方
		js_gd("xpath", "//span[contains(text(),'资金结算管理')]")
		# 用JS的方法点击资金结算管理菜单按钮
		js_click("xpath", "//span[contains(text(),'资金结算管理')]")
		sleep(1)
		# 点击'资金系统收付'菜单
		click("xpath", "//span[text()='资金系统收付']")
		sleep(1)
		# 点击付款处理菜单
		click("xpath", "//span[text()='付款处理']")
		sleep(1)
		# 退出所有iframe窗体
		switch_default()
		
		# 开始测试资金系统收付--付款处理--支票支付
		# 测试付款处理--支票支付
		try:

			#收回窗体
			click("xpath", "//span[text()='资金系统收付']")
			sleep(1)
			js_click("xpath", "//span[contains(text(),'资金结算管理')]")
			sleep(1)
			'''
			#开始创建支票支付的直联账号-------------------------------------------------------------------------
			# 将页面的滚动条滑动到‘票据管理’页面的地方
			js_gd("xpath", "//span[contains(text(),'账户资金监控')]")
			# 用JS的方法点击票据管理菜单按钮
			js_click("xpath", "//span[contains(text(),'账户资金监控')]")
			sleep(1)
			click("xpath", "//span[contains(text(),'账户生命周期')]")
			sleep(1)
			click("xpath", "//span[text()='账户维护']")
			sleep(1)
			switch_default()
			# 切入单币种账户窗体
			switch_to("xpath", '//*[@id="bankAccounts-tab-iframe"]')
			sleep(1)
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			click("xpath", "//span[text()='新增']")
			sleep(1)
			switch_to("xpath", '//*[@id="addWin-iframe"]')
			#银行
			click("xpath", "//input[@id='combobox-input-bankid']")
			sleep(1)
			# 模糊匹配报错，因此选择直接点击
			click("xpath", "//div[@title='代码-名称:BOC-中国银行']")
			sleep(1)

			# 选择开户行
			input("xpath", "//input[@id='combobox-input-banklocationid']", "大连泡崖")
			sleep(1)
			click("xpath", "//div[@title='联行号-开户行名:104222000965-中国银行股份有限公司大连泡崖街支行']")
			sleep(1)

			# 选择币种
			input("xpath", "//input[@id='combobox-input-currencyid']", "CNY")
			sleep(1)
			input_down("xpath", "//input[@id='combobox-input-currencyid']")
			input_enter("xpath", "//input[@id='combobox-input-currencyid']")
			time.sleep(1)

			# 选择账户性质
			input("xpath", "//input[@id='combobox-input-accounttypeid']", "基本户")
			sleep(1)
			input_down("xpath", "//input[@id='combobox-input-accounttypeid']")
			input_enter("xpath", "//input[@id='combobox-input-accounttypeid']")
			time.sleep(1)

			# # 选择银企直联户isbankdirect
			#click("xpath", "//input[@id='isbankdirect']")

			# 选择境内外
			input("xpath", "//input[@id='combobox-input-inorout']", "境内")
			sleep(1)
			input_down("xpath", "//input[@id='combobox-input-inorout']")
			input_enter("xpath", "//input[@id='combobox-input-inorout']")
			# 输入银行账号
			input("xpath", '//*[@id="accountnumber"]', '20211015')
			sleep(1)
			input("xpath", '//*[@id="accountname"]', '测试支票支付账户')

			# 点击保存按钮
			click("xpath", "//span[text()='保存']")
			# 退出所有iframe窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")

			sleep(1)
			# 切入窗体
			switch_to("xpath", '//*[@id="bankAccounts-tab-iframe"]')
			sleep(1)
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			
			# 点击查询放大镜
			js_click("xpath", "//span[@class='f-contrac-close']")
			sleep(1)
			# 输入账户，进行查询
			input("xpath", '//*[@id="accountnumber"]', '20211015')
			sleep(1)
			# 点击查询
			click("xpath", "//span[text()='查询']")
			sleep(1)
			
			# 勾选数据
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
			sleep(1)
			triangle_cick_and_element("维护", '开户')
			
			# 开户日期
			today = date.today()
			open_date = today - timedelta(days=20)
			click("xpath", "//input[@id='openeddatewin-input']")
			sleep(1)
			clear("xpath", "//input[@id='openeddatewin-input']")
			sleep(1)
			input("xpath", "//input[@id='openeddatewin-input']", str(open_date))
			time.sleep(1)
			
			#初始余额
			click("xpath",'//*[@id="initbalance-input"]')
			sleep(1)
			double_click("xpath",'//*[@id="initbalance-input"]')
			sleep(1)
			input("xpath",'//*[@id="initbalance-input"]','50000')
			sleep(1)
			
			# 日记账余额
			js_click("xpath", '//*[@id="journalbalance-input"]')
			sleep(1)
			clear("xpath", '//*[@id="journalbalance-input"]')
			sleep(1)
			input("xpath", '//*[@id="journalbalance-input"]', "5000")
			sleep(1)
			click("xpath", "//span[text()='确定']")
			sleep(1)
			
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("直联支票支付账户创建成功")
			js_click("xpath", "//span[contains(text(),'账户资金监控')]")
			sleep(1)
			'''
			js_gd("xpath", "//span[contains(text(),'资金结算管理')]")
			# 用JS的方法点击资金结算管理菜单按钮
			js_click("xpath", "//span[contains(text(),'资金结算管理')]")

			# 点击'资金系统收付'菜单
			click("xpath", "//span[text()='资金系统收付']")
			sleep(1)
			click("xpath", "//span[text()='付款处理']")
			# 退出所有iframe窗体
			switch_default()
			
			
			for i in range(1, 4):
				switch_to("xpath", "//iframe[@id='generalPayment-tab-iframe']")
				# 点击支票支付
				click("xpath", "//span[text()='支票支付']")
				sleep(1)
				# 切入支票支付窗体
				switch_to("xpath", "//iframe[@id='subTabFive-iframe']")
				
				# 点击新增
				click("xpath", "//span[text()='新增']")
				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='addWin-iframe']")
				
				# 输入交易类型
				input("xpath", "//input[@id='combobox-input-paytypeid']", "103-对外付款")
				sleep(2)
				input_down("xpath", "//input[@id='combobox-input-paytypeid']")
				sleep(1)
				input_enter("xpath", "//input[@id='combobox-input-paytypeid']")
				time.sleep(1)
				
				# 选择结算方式
				click("xpath", "//input[@id='combobox-input-settlementmodeid']")
				clear("xpath", "//input[@id='combobox-input-settlementmodeid']")
				sleep(1)
				# 输入开户行大连泡崖街支行名称，模糊查询
				input("xpath", "//input[@id='combobox-input-settlementmodeid']", "现金支票支付")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-settlementmodeid']")
				input_enter("xpath", "//input[@id='combobox-input-settlementmodeid']")
				time.sleep(1)
				
				# 付方账户
				click("xpath", "//input[@id='combobox-input-ourbankaccountid']")
				# 输入开户行大连泡崖街支行名称，模糊查询
				input("xpath", "//input[@id='combobox-input-ourbankaccountid']", "20211015")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-ourbankaccountid']")
				input_enter("xpath", "//input[@id='combobox-input-ourbankaccountid']")
				time.sleep(1)
				
				# 收方组织
				input("xpath", "//input[@id='combobox-input-oppcounterpartyid']", "浙江华语科技")
				sleep(1)
				# 双击清楚下拉框
				double_click("xpath", "//span[text()='卡折类型']")
				sleep(1)
				
				# 收方账户
				input("xpath", "//input[@id='combobox-input-oppcounterpartyaccountid']", "200848782767819")
				sleep(1)
				# 双击清楚下拉框
				double_click("xpath", "//span[text()='卡折类型']")
				sleep(1)
				
				# 收方开户银行
				click("xpath", "//input[@id='combobox-input-oppbanklocationid']")
				input_enter("xpath", "//input[@id='combobox-input-oppbanklocationid']")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-oppbanklocationid']")
				sleep(1)
				input_enter("xpath", "//input[@id='combobox-input-oppbanklocationid']")
				time.sleep(1)
				
				# 金额
				money = random.randint(100, 300)
				input("xpath", "//input[@id='ouramount-input']", money)
				sleep(1)
				
				# 用途
				input("xpath", "//input[@id='combobox-input-purpose']", "支票支付自动化测试")
				sleep(1)
				
				# 点击保存按钮
				click("xpath", "//span[text()='保存']")
				sleep(1)
				# 退出所有iframe窗体
				switch_default()
				
				# 用隐式等待方法等页面出现新增成功的提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				if i == 3:
					print("付款处理-支票支付，新增成功！")
				time.sleep(3)
			
			# 测试修改功能-------------------------------------------------------------------------------------
			switch_to("xpath", "//iframe[@id='generalPayment-tab-iframe']")
			# 点击支票支付
			click("xpath", "//span[text()='支票支付']")
			sleep(1)
			# 切入支票支付窗体
			switch_to("xpath", "//iframe[@id='subTabFive-iframe']")
			
			# 刷新后勾选数据
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			# 点击修改按钮
			click("xpath", "//span[text()='修改']")
			# 切入修改的iframe窗体
			switch_to("xpath", "//iframe[@id='modWin-iframe']")
			# 更改用途
			clear("xpath", "//input[@id='combobox-input-purpose']")
			input("xpath", "//input[@id='combobox-input-purpose']", "测试修改")
			sleep(1)
			# 双击消除下拉框
			double_click("xpath", "//span[text()='金额']")
			# 点击保存按钮
			click("xpath", "//span[text()='保存']")
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("付款处理-支票支付，修改成功！")
			time.sleep(3)
			
			# 测试删除功能-----------------------------------------------------------------------------------
			switch_to("xpath", "//iframe[@id='generalPayment-tab-iframe']")
			# 点击支票支付
			click("xpath", "//span[text()='支票支付']")
			sleep(1)
			# 切入支票支付窗体
			switch_to("xpath", "//iframe[@id='subTabFive-iframe']")
			
			# 刷新后勾选数据
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			# 点击删除按钮
			click("xpath", "//span[text()='删除']")
			sleep(1)
			# 点击弹出框的OK键
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("付款处理-支票支付，删除成功！")
			time.sleep(3)
			
			# 测试作废功能---------------------------------------------------------------------------------
			# 点击作废
			switch_to("xpath", "//iframe[@id='generalPayment-tab-iframe']")
			# 点击支票支付
			click("xpath", "//span[text()='支票支付']")
			sleep(1)
			# 切入支票支付窗体
			switch_to("xpath", "//iframe[@id='subTabFive-iframe']")
			
			# 刷新后勾选数据
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			click("xpath", "//span[text()='作废']")
			sleep(1)
			# 点击弹出框的OK键
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
			switch_default()
			# 用隐式等待方法等页面出现
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("支票支付，作废成功！")
			time.sleep(3)
			
			# 测试送审，撤销送审功能----------------------------------------------------------------------------
			switch_to("xpath", "//iframe[@id='generalPayment-tab-iframe']")
			# 点击支票支付
			click("xpath", "//span[text()='支票支付']")
			sleep(1)
			# 切入支票支付窗体
			switch_to("xpath", "//iframe[@id='subTabFive-iframe']")
			
			# 刷新后勾选数据
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			# 点击送审
			click("xpath", "//span[text()='送审']")
			sleep(1)
			# 点击弹出框的OK键
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
			sleep(1)
			
			# 退出所有iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！送审成功1笔，失败0笔。')]")
			print("付款处理-支票支付，送审成功！")
			time.sleep(3)
			
			# 测试撤销送审
			switch_to("xpath", "//iframe[@id='generalPayment-tab-iframe']")
			# 点击支票支付
			click("xpath", "//span[text()='支票支付']")
			sleep(1)
			# 切入支票支付窗体
			switch_to("xpath", "//iframe[@id='subTabFive-iframe']")
			
			# 刷新后勾选数据
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			# 用JS方便点击‘申请’按钮旁边的倒三角形
			js_click("xpath", "//span[text()='送审']/parent::*/following-sibling::*/child::*")
			sleep(1)
			
			# 点击撤销送审按钮
			js_click("xpath", "//a[contains(text(),'撤销送审')]")
			sleep(1)
			
			# 点击弹出框的OK键
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
			sleep(1)
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'撤销送审成功！')]")
			print("付款处理-支票支付，撤销送审成功！")
			time.sleep(3)
			
			# 测试审批历史功能----------------------------------------------------------------------------
			switch_to("xpath", "//iframe[@id='generalPayment-tab-iframe']")
			# 点击支票支付
			click("xpath", "//span[text()='支票支付']")
			sleep(1)
			# 切入支票支付窗体
			switch_to("xpath", "//iframe[@id='subTabFive-iframe']")
			
			# 刷新后勾选数据
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			# 点击审批历史
			click("xpath", "//span[text()='审批历史']")
			sleep(1)
			# 切入审批历史窗口
			switch_to("xpath", '//*[@id="flowwin-iframe"]')
			sleep(3)
			# 点击流程流转按钮
			click("xpath", "//span[text()='流程流转']")
			sleep(3)
			implici_wait("xpath", '//*[@id="wf_trace_info_grid-body-table"]/tbody/tr[1]/td[4]/div')
			print("付款处理-支票支付，审批历史查看成功！")
			switch_parent()
			click("xpath", '//*[@id="f-win-title-flowwin"]/div[1]/div')
			switch_default()
			time.sleep(3)
			
			# 测试领用功能-----------------------------------------------------------------------
			# 点击资金系统收付缩回窗口
			click("xpath", "//span[text()='资金系统收付']")
			sleep(1)
			js_click("xpath", "//span[contains(text(),'资金结算管理')]")
			js_gd("xpath", "//span[contains(text(),'票据管理')]")
			# 用JS的方法点击票据管理菜单按钮
			js_click("xpath", "//span[contains(text(),'票据管理')]")
			sleep(1)
			
			# 点击基础设置菜单
			click("xpath", "//li[@f_value='billSetting']/descendant-or-self::*[5]")
			# 点击支票用途菜单
			click("xpath", "//li[@f_value='chequePurpose']/descendant-or-self::*[5]")
			# 退出所有iframe窗体
			switch_default()
			
			# 切入支票用途的iframe窗体
			switch_to("xpath", "//iframe[@id='chequePurpose-tab-iframe']")
			# 用JS的方法点击新增按钮
			js_click("xpath", "//span[text()='新增']")
			sleep(1)
			# 切入新增的iframe窗体
			switch_to("xpath", "//iframe[@id='addWin-iframe']")
			sleep(1)
			# 设置时间的变成存储
			useCode = time.strftime("%Y%m%d%H%M%S")
			
			# 输入用途代码
			input("xpath", "//input[@name='code']", useCode)
			sleep(1)
			
			# 输入的支票用途
			input("xpath", "//input[@id='name']", "测试支票支付")
			sleep(1)
			# 点击保存按钮
			click("xpath", "//span[text()='保存']")
			
			# 退出所有iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			time.sleep(3)
			
			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='支票用途']/child::*[1]")
			
			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//li[@f_value='billSetting']/descendant-or-self::*[5]")
			sleep(2)
			
			# 点击支票管理菜单
			click("xpath", "//span[@title='支票管理']")
			# 点击应付支票登记菜单
			click("xpath", "//span[@title='应付支票登记']")
			# 退出所有的iframe窗体
			switch_default()
			
			# 切入应付支票登记iframe窗体
			switch_to("xpath", "//iframe[@id='chequeStorage-tab-iframe']")
			# 用JS的方法点击新增按钮
			js_click("xpath", "//span[text()='新增']")
			
			# 切入新增的iframe窗体
			switch_to("xpath", "//iframe[@id='addWin-iframe']")
			sleep(1)
			
			click("xpath", "//input[@id='combobox-input-booktype']")
			# 模糊匹配搜索
			input("xpath", "//input[@id='combobox-input-booktype']", "现金")
			sleep(1)
			# 模拟回车
			double_click("xpath", "//div[contains(text(),'现金')]")
			sleep(1)
			
			# 输入起始码
			starCoed = random.randint(1000, 10000)
			
			input("xpath", "//input[@id='codefrom']", starCoed)
			sleep(1)
			
			# 输入终止码
			input("xpath", "//input[@id='codeto']", starCoed)
			sleep(1)
			click("xpath", "//input[@id='combobox-input-bankid']")
			sleep(1)
			# 输入银行名称，通过模糊匹配搜索
			input("xpath", "//input[@id='combobox-input-bankid']", "中国银行")
			sleep(1)
			double_click("xpath", '//*[@id="bankid-combogrid-body-table"]/tbody/tr[1]/td[2]/div')
			sleep(1)
			
			# 输入银行账户
			input("xpath", "//input[@id='combobox-input-accountid']", "20211015")
			sleep(1)
			input_down("xpath", "//input[@id='combobox-input-accountid']")
			sleep(1)
			input_enter("xpath", "//input[@id='combobox-input-accountid']")
			time.sleep(1)
			
			# 点击保存按钮
			click("xpath", "//span[text()='保存']")
			sleep(1)
			# 点击弹出框的OK键
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			sleep(3)
			
			# 切回支票支付页面
			# 将页面的滚动条滑动到‘资金结算管理’页面的地方
			js_gd("xpath", "//span[contains(text(),'资金结算管理')]")
			# 用JS的方法点击资金结算管理菜单按钮
			js_click("xpath", "//span[contains(text(),'资金结算管理')]")
			
			# 点击'资金系统收付'菜单
			click("xpath", "//span[text()='资金系统收付']")
			# 点击付款处理菜单
			click("xpath", "//span[text()='付款处理']")
			# 退出所有iframe窗体
			switch_default()
			
			switch_to("xpath", "//iframe[@id='generalPayment-tab-iframe']")
			# 点击支票支付
			click("xpath", "//span[text()='支票支付']")
			sleep(1)
			# 切入支票支付窗体
			switch_to("xpath", "//iframe[@id='subTabFive-iframe']")
			
			# 刷新后勾选数据
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			# 复核一笔数据
			# 点击送审
			click("xpath", "//span[text()='送审']")
			sleep(1)
			# 点击弹出框的OK键
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
			sleep(1)
			
			# 退出所有iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！送审成功1笔，失败0笔。')]")
			# 二次审批
			switch_to("xpath", "//iframe[@id='generalPayment-tab-iframe']")
			# 点击支票支付
			click("xpath", "//span[text()='支票支付']")
			sleep(1)
			# 切入支票支付窗体
			switch_to("xpath", "//iframe[@id='subTabFive-iframe']")
			
			# 双击数据
			double_click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[3]/div')
			sleep(1)
			switch_to("xpath", '//*[@id="wf_taskProcessing_win-iframe"]')
			click("xpath", "//span[text()='同意']")
			switch_default()
			sleep(3)
			
			switch_to("xpath", "//iframe[@id='generalPayment-tab-iframe']")
			# 点击支票支付
			click("xpath", "//span[text()='支票支付']")
			sleep(1)
			# 切入支票支付窗体
			switch_to("xpath", "//iframe[@id='subTabFive-iframe']")
			
			# 刷新后勾选数据
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			# 点击领用按钮
			click("xpath", "//span[text()='领用']")
			sleep(1)
			
			# 切入领用窗体
			switch_to("xpath", '//*[@id="chequerecipientsWin-iframe"]')
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]')
			sleep(1)
			# 点击下一步
			click("xpath", "//span[text()='下一步']")
			sleep(1)
			
			# 切入下一步窗体
			switch_to("xpath", '//*[@id="applyWin-iframe"]')
			# 输入领用人
			input("xpath", '//*[@id="username"]', '测试支票支付账户')
			sleep(2)
			# 输入领用用途
			input("xpath", '//*[@id="combobox-input-chequepurposeid"]', '测试支票支付')
			sleep(2)
			click("xpath", '//*[@id="chequepurposeid-combogrid-body-table"]/tbody/tr/td[2]/div')
			# 点击领用
			click("xpath", "//span[text()='领用']")
			sleep(1)
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'领用成功！')]")
			print("付款处理-支票支付，领用成功")
			
			# 点击付款处理菜单,退出当前页面
			click("xpath", "//span[text()='付款处理']")
			# 退出所有iframe窗体
			switch_default()

			# 测试确认支付功能--------------------------------------------------------------------------------
			switch_to("xpath", "//iframe[@id='generalPayment-tab-iframe']")
			# 点击支票支付
			click("xpath", "//span[text()='支票支付']")
			sleep(1)
			# 切入支票支付窗体
			switch_to("xpath", "//iframe[@id='subTabFive-iframe']")
			
			# 刷新后勾选数据
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			# 点击确认支付
			click("xpath", "//span[text()='确认支付']")
			sleep(1)
			# 点击确认
			click("xpath", "//span[text()='确定']")
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！1笔进行了确认支付，0笔不允许确认支付。')]")
			print("支票支付，确认支付成功！")
			
			# 测试打印功能------------------------------------------------------------------------------------
			switch_to("xpath", "//iframe[@id='generalPayment-tab-iframe']")
			# 点击支票支付
			click("xpath", "//span[text()='支票支付']")
			sleep(1)
			# 切入支票支付窗体
			switch_to("xpath", "//iframe[@id='subTabFive-iframe']")
			
			# 刷新后勾选数据
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			# 点击打印
			click("xpath", "//span[text()='打印']")
			sleep(1)
			
			# 获取所有窗口句柄
			all_handles = self.driver.window_handles
			# 循环遍历所有新打开的窗口句柄，也就是说不包括主窗口
			now_handle = self.driver.current_window_handle
			for handle in all_handles:
				self.driver.switch_to.window(handle)
				if self.driver.title == u"payandrecsingleprint":
					implici_wait("xpath", "//td[contains(text(),'浙江华语科技')]")
					print("支票支付，打印成功!！")
					time.sleep(3)
					self.driver.switch_to.window(now_handle)
					switch_default()
			
			# 打印-打印记录
			# 切入‘支票支付’的iframe窗体
			switch_to("xpath", "//iframe[@id='generalPayment-tab-iframe']")
			# 点击支票支付
			click("xpath", "//span[text()='支票支付']")
			sleep(1)
			# 切入支票支付窗体
			switch_to("xpath", "//iframe[@id='subTabFive-iframe']")
			
			# 刷新后勾选数据
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			# 用JS方便点击‘支付’按钮旁边的倒三角形
			js_click("xpath", "//span[text()='打印']/parent::*/following-sibling::*/child::*")
			sleep(1)
			
			# 点击打印记录按钮
			js_click("xpath", "//a[contains(text(),'打印记录')]")
			sleep(1)
			
			switch_to("xpath", "//iframe[@id='printWin-iframe']")
			sleep(1)
			
			# 用隐式等待方法等页面出现  操作人:mindy
			implici_wait("xpath", "//div[@title='操作人:mindy']")
			print("支票支付，打印记录查看成功！")
			time.sleep(3)
			switch_parent()
			# 点击关闭页面
			click("xpath", "//span[text()='打印记录']/preceding-sibling::*[1]")
			sleep(1)
			switch_default()
			
			# 测试上传---------------------------------------------------------------------------------------
			switch_to("xpath", "//iframe[@id='generalPayment-tab-iframe']")
			# 点击支票支付
			click("xpath", "//span[text()='支票支付']")
			sleep(1)
			# 切入支票支付窗体
			switch_to("xpath", "//iframe[@id='subTabFive-iframe']")
			
			# 点击上传
			click("xpath", '//*[@id="gridtitle"]/div[3]/div[2]')
			sleep(1)
			switch_to("xpath", '//*[@id="importDataWin-iframe"]')
			click("xpath", '//*[@id="combobox-input-businessid"]')
			sleep(1)
			click("xpath", '//*[@id="businessid-combogrid-body-table"]/tbody/tr[1]/td[2]/div')
			sleep(1)
			click("xpath", '//*[@id="save"]/span/span')
			sleep(1)
			switch_to("xpath", '//*[@id="loadNextWin-iframe"]')
			input("xpath", '//*[@id="combobox-input-paytypeid"]', '对外付款')
			sleep(1)
			click("xpath", '//*[@id="paytypeid-combogrid-body-table"]/tbody/tr[1]/td[2]/div')
			sleep(1)
			input("xpath", '//*[@id="combobox-input-settlementmodeid"]', '现金支票支付')
			sleep(1)
			click("xpath", '//*[@id="settlementmodeid-combogrid-body-table"]/tbody/tr[1]/td[2]/div')
			sleep(1)
			# 点击上传文件
			# 附件上传
			upload_click("xpath", "//div[text()='上传文件']/parent::*[1]/descendant::*[4]",
			             'D:\FlieDownload', '"chequepay.xls"')
			sleep(3)
			# 点击保存按钮
			click("xpath", "//span[text()='上传']")
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功')]")
			print("付款处理-支票支付，导入成功！")
			time.sleep(3)
		
		
		
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("支票支付失败！" + str(traceback.format_exc()))
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
