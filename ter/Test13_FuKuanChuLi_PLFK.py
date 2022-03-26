# encoding=utf-8
# @Time : 2020/10/14 14:49
# @Author : zzg
# 此文件是测试Mysql版本资金结算管理--资金系统收付--付款处理--直联批量付款
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


class Test13_FuKuanChuLi_PLFK(unittest.TestCase):
	
	# 启动浏览器
	def setUp(self):
		# 启动浏览器的另外一个方法：通过封装启动浏览器的驱动，启动不同浏览器
		self.driver = get("chrome")
	
	# 登陆系统、对系统设置进行操作
	def test_trade(self):
		
		login(G_Mys_Url, mindy, Password, "亚唐科技")
		
		logging.info("开始测试直联批量付款")
		
		# 滚动到直联单笔界面
		js_gd("xpath", "//span[contains(text(),'资金结算管理')]")
		# 用JS的方法点击资金结算管理菜单按钮
		js_click("xpath", "//span[contains(text(),'资金结算管理')]")
		sleep(1)
		click("xpath", "//span[text()='资金系统收付']")
		sleep(1)
		click("xpath", "//span[text()='付款处理']")
		# 退出所有iframe窗体
		switch_default()
		
		# 开始测试资金系统收付--付款处理--直联批量付款
		# 测试付款处理--直联批量付款
		try:
			'''
			# 创建直联批量付款账户💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 收回窗体
			click("xpath", "//span[text()='资金系统收付']")
			sleep(1)
			js_click("xpath", "//span[contains(text(),'资金结算管理')]")
			sleep(1)
			
			# 将页面的滚动条滑动到‘账户资金监控’页面的地方
			js_gd("xpath", "//span[contains(text(),'账户资金监控')]")
			# 用JS的方法点击账户资金监控菜单
			js_click("xpath", "//span[contains(text(),'账户资金监控')]")
			sleep(1)
			# 点击账户生命周期
			click("xpath", "//span[contains(text(),'账户生命周期')]")
			sleep(1)
			click("xpath", "//span[text()='账户维护']")
			sleep(1)
			switch_default()
			# 切入单币种账户窗体，新增账户
			switch_to("xpath", '//*[@id="bankAccounts-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			click("xpath", "//span[text()='新增']")
			sleep(1)
			# 切入新增窗体
			switch_to("xpath", '//*[@id="addWin-iframe"]')
			
			# 银行
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
			click("xpath", "//input[@id='isbankdirect']")
			sleep(1)
			
			# 选择境内外
			input("xpath", "//input[@id='combobox-input-inorout']", "境内")
			sleep(1)
			input_down("xpath", "//input[@id='combobox-input-inorout']")
			input_enter("xpath", "//input[@id='combobox-input-inorout']")
			# 输入银行账号
			input("xpath", '//*[@id="accountnumber"]', '20211013')
			sleep(1)
			input("xpath", '//*[@id="accountname"]', '付款处理-直联批量支付账户')
			sleep(1)
			# 点击保存按钮
			click("xpath", "//span[text()='保存']")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			sleep(1)
			
			# 对新增账户进行开户
			# 切入窗体
			switch_to("xpath", '//*[@id="bankAccounts-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			# 点击查询放大镜
			js_click("xpath", "//span[@class='f-contrac-close']")
			sleep(1)
			# 输入账户，进行查询
			input("xpath", '//*[@id="accountnumber"]', '20211013')
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
			# 日记账余额
			click("xpath", '//*[@id="journalbalance-input"]')
			sleep(1)
			clear("xpath", '//*[@id="journalbalance-input"]')
			sleep(1)
			input("xpath", '//*[@id="journalbalance-input"]', "5000")
			sleep(1)
			click("xpath", "//span[text()='确定']")
			sleep(1)
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			
			js_click("xpath", "//span[contains(text(),'账户资金监控')]")
			sleep(1)
			
			# 开始创建直联批量付款的交易类型以及结算方式=============================================================
			js_gd("xpath", "//span[contains(text(),'资金结算管理')]")
			# 用JS的方法点击资金结算管理菜单按钮
			js_click("xpath", "//span[contains(text(),'资金结算管理')]")
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
			input("xpath", "//input[@name='code']", "2013")
			sleep(1)
			
			# 输入结算方式
			input("xpath", "//input[@id='name']", "付款处理批量付款")
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
			input("xpath", "//input[@id='combobox-input-dealtype']", "直联")
			sleep(1)
			input_down("xpath", "//input[@id='combobox-input-dealtype']")
			input_enter("xpath", "//input[@id='combobox-input-dealtype']")
			sleep(1)
			# 增加直联渠道
			click("xpath", "//span[text()='新增行']")
			sleep(1)
			input("xpath", '//*[@id="combobox-input-editgrid-bankid-0"]', 'BOC-中国银行')
			sleep(1)
			click('xpath', '//*[@id="editgrid-bankid-0-combogrid-body-table"]/tbody/tr/td[2]/div')
			sleep(1)
			input('xpath', '//*[@id="combobox-input-editgrid-settlementscenarios-0"]', '代发代扣默认')
			sleep(1)
			click('xpath', '//*[@id="f-combo-editgrid-settlementscenarios-0-list-0"]')
			sleep(1)
			click('xpath', '//*[@id="combobox-input-editgrid-directchannelid-0"]')
			sleep(1)
			click('xpath', '//*[@id="editgrid-directchannelid-0-combogrid-body-table"]/tbody/tr[1]/td[2]/div')
			sleep(1)
			input('xpath', '//*[@id="combobox-input-editgrid-directchannelcmdid-0"]', '批量代付')
			sleep(1)
			click('xpath', '//*[@id="editgrid-directchannelcmdid-0-combogrid-body-table"]/tbody/tr[1]/td[2]/div')
			sleep(1)
			click('xpath', '//*[@id="combobox-input-editgrid-directinterbanksystemid-0"]')
			click('xpath', '//*[@id="editgrid-directinterbanksystemid-0-combogrid-body-table"]/tbody/tr[1]/td[2]/div')
			sleep(1)
			# 点击保存按钮
			click("xpath", "//span[text()='保存']")
			# 退出所有iframe窗体
			switch_default()
			time.sleep(3)
			
			# 创建直联批量付款的交易类型==================
			click("xpath", "//span[text()='交易类型']")
			sleep(1)
			switch_to('xpath', '//*[@id="payType-tab-iframe"]')
			js_click("xpath", "//span[text()='新增']")
			sleep(1)
			# 切入新增的iframe窗体
			switch_to("xpath", "//iframe[@id='addWin-iframe']")
			# 输入代码
			input("xpath", "//input[@id='code']", "3013")
			sleep(1)
			
			# 输入名称
			input("xpath", "//input[@id='name']", "付款处理批量付款交易类型")
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
			input("xpath", "//input[@id='combobox-input-settlementmoderange']", '2013')
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
			
			# 勾选代发代扣
			click('xpath', '//*[@id="isagentpayoff"]')
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
			# 点击保存按钮
			click("xpath", "//span[text()='保存']")
			print("直联批量付款交易方式，结算方式创建成功")
			switch_default()
			
			# 回到批量付款页面
			click("xpath", "//span[text()='资金系统收付']")
			# 点击付款处理菜单
			click("xpath", "//span[text()='付款处理']")
			# 退出所有iframe窗体
			switch_default()
			'''
			# 测试新增功能================================================================================
			for i in range(1, 4):
				switch_to("xpath", "//iframe[@id='generalPayment-tab-iframe']")
				# 点击直联批量付款
				click("xpath", "//span[text()='直联批量付款']")
				sleep(1)
				# 进入直联批量付款的iframe窗体
				switch_to("xpath", "//iframe[@id='subTabThree-iframe']")
				click("xpath", "//span[text()='新增']")
				sleep(1)
				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='addWin-iframe']")
				# 交易类型
				click("xpath", "//input[@id='combobox-input-paytypeid']")
				sleep(1)
				input("xpath", "//input[@id='combobox-input-paytypeid']", "3013-付款处理批量付款交易类型")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-paytypeid']")
				input_enter("xpath", "//input[@id='combobox-input-paytypeid']")
				time.sleep(1)
				# 付方账户
				input("xpath", "//input[@id='combobox-input-ourbankaccountid']", '20211013')
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-ourbankaccountid']")
				input_enter("xpath", "//input[@id='combobox-input-ourbankaccountid']")
				time.sleep(1)
				# 收方名称
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
				sleep(1)
				input_enter("xpath", "//input[@id='combobox-input-oppbanklocationid']")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-oppbanklocationid']")
				sleep(1)
				input_enter("xpath", "//input[@id='combobox-input-oppbanklocationid']")
				time.sleep(1)
				# 金额
				input("xpath", "//input[@id='ouramount-input']", "300")
				sleep(1)
				# 用途
				input("xpath", "//input[@id='combobox-input-purpose']", "付款处理直联批量付款")
				sleep(1)
				# 点击保存按钮
				click("xpath", "//span[text()='保存']")
				sleep(1)
				# 退出所有iframe窗体
				switch_default()
				# 用隐式等待方法等页面出现新增成功的提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				print("直联批量付款，新增成功")
				time.sleep(3)
			# 测试删除功能======================================================================================
			switch_to("xpath", "//iframe[@id='generalPayment-tab-iframe']")
			sleep(1)
			# 点击直联批量付款
			click("xpath", "//span[text()='直联批量付款']")
			# 进入直联批量付款的iframe窗体
			switch_to("xpath", "//iframe[@id='subTabThree-iframe']")
			sleep(1)
			
			# 勾选数据，点击删除按钮
			click('xpath', '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click('xpath', '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			click("xpath", '//*[@id="custButton6"]/span/span')
			sleep(1)
			switch_default()
			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'成功删除1条记录！')]")
			print("付款处理-直联批量支付，删除成功！")
			time.sleep(3)
			
			##测试作废功能--------------------------------------------------------------------------------------
			switch_to("xpath", "//iframe[@id='generalPayment-tab-iframe']")
			sleep(1)
			# 点击直联批量付款
			click("xpath", "//span[text()='直联批量付款']")
			# 进入直联批量付款的iframe窗体
			switch_to("xpath", "//iframe[@id='subTabThree-iframe']")
			sleep(1)
			
			# 勾选数据点击作废按钮
			click('xpath', '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[2]/td[2]/div/button')
			sleep(1)
			click("xpath", '//*[@id="custButton7"]/span/span')
			sleep(1)
			# 点击ok按钮
			click("xpath", '//*[@id="f-message-webgen-0-okBnt"]')
			sleep(1)
			switch_default()
			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'成功作废1条记录！')]")
			print("付款处理-直联批量支付，作废成功！")
			time.sleep(3)
			
			# 测试送审，撤销送审功能--------------------------------------------------------------------------
			switch_to("xpath", "//iframe[@id='generalPayment-tab-iframe']")
			sleep(1)
			# 点击直联批量付款
			click("xpath", "//span[text()='直联批量付款']")
			# 进入直联批量付款的iframe窗体
			switch_to("xpath", "//iframe[@id='subTabThree-iframe']")
			sleep(1)
			
			# 勾选数据，点击送审按钮
			click('xpath', '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			click("xpath", "//span[text()='送审']")
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！送审成功1笔，失败0笔。')]")
			print("付款处理-直联批量支付，送审成功！")
			time.sleep(3)
			# 测试撤销送审功能
			switch_to("xpath", "//iframe[@id='generalPayment-tab-iframe']")
			sleep(1)
			# 点击直联批量付款
			click("xpath", "//span[text()='直联批量付款']")
			# 进入直联批量付款的iframe窗体
			switch_to("xpath", "//iframe[@id='subTabThree-iframe']")
			sleep(1)
			
			# 勾选数据，点击撤销送审按钮
			click('xpath', '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			# 用JS方便点击‘申请’按钮旁边的倒三角形
			js_click("xpath", "//span[text()='送审']/parent::*/following-sibling::*/child::*")
			sleep(1)
			js_click("xpath", "//a[contains(text(),'撤销送审')]")
			sleep(1)
			# 点击弹出框的OK键
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'撤销送审成功！')]")
			print("付款处理-直联批量支付，撤销送审成功！")
			time.sleep(3)
			
			# 测试支付功能-------------------------------------------------------------------------------
			# 勾选一笔数据送审
			switch_to("xpath", "//iframe[@id='generalPayment-tab-iframe']")
			sleep(1)
			# 点击直联批量付款
			click("xpath", "//span[text()='直联批量付款']")
			# 进入直联批量付款的iframe窗体
			switch_to("xpath", "//iframe[@id='subTabThree-iframe']")
			sleep(1)
			
			# 勾选数据，点击送审按钮
			click('xpath', '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			click("xpath", "//span[text()='送审']")
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！送审成功1笔，失败0笔。')]")
			
			# 对数据二次审批
			switch_to("xpath", "//iframe[@id='generalPayment-tab-iframe']")
			# 点击直联批量付款
			click("xpath", "//span[text()='直联批量付款']")
			sleep(1)
			# 进入直联批量付款的iframe窗体
			switch_to("xpath", "//iframe[@id='subTabThree-iframe']")
			sleep(1)
			# 勾选数据
			double_click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[3]/div')
			sleep(1)
			switch_to("xpath", '//*[@id="wf_taskProcessing_win-iframe"]')
			# 点击同意按钮
			click("xpath", '//*[@id="wf_btn_submit_1"]/span/span')
			sleep(1)
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("数据二审成功")
			
			# 对数据三审
			switch_to("xpath", "//iframe[@id='generalPayment-tab-iframe']")
			# 点击直联批量付款
			click("xpath", "//span[text()='直联批量付款']")
			sleep(1)
			# 进入直联批量付款的iframe窗体
			switch_to("xpath", "//iframe[@id='subTabThree-iframe']")
			sleep(1)
			# 勾选数据
			double_click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[3]/div')
			sleep(1)
			switch_to("xpath", '//*[@id="wf_taskProcessing_win-iframe"]')
			# 点击同意按钮
			click("xpath", '//*[@id="wf_btn_submit_0"]/span/span')
			sleep(1)
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("数据三审成功")
			
			# 勾选数据点击支付
			switch_to("xpath", "//iframe[@id='generalPayment-tab-iframe']")
			# 点击直联批量付款
			click("xpath", "//span[text()='直联批量付款']")
			sleep(1)
			# 进入直联批量付款的iframe窗体
			switch_to("xpath", "//iframe[@id='subTabThree-iframe']")
			sleep(1)
			
			# 支付
			click('xpath', '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			click("xpath", '//*[@id="custButton2"]/span/span')
			
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！1批进行了支付，0批不允许支付')]")
			print("直联批量支付，支付成功！")
			sleep(3)
			
			# 测试查询支付状态-------------------------------------------------------------------------------------
			# 操作数据库修改付款单状态
			my_sql(my_host, my_port, my_user, my_passwd, my_db,
			        "update T_SE_PAYMENTS a set a.paystate='7' where  a.purpose = '付款处理直联批量付款'")
			switch_to("xpath", "//iframe[@id='generalPayment-tab-iframe']")
			sleep(1)
			# 点击直联批量付款
			click("xpath", "//span[text()='直联批量付款']")
			# 进入直联批量付款的iframe窗体
			switch_to("xpath", "//iframe[@id='subTabThree-iframe']")
			sleep(1)
			
			# 勾选数据，点击查询支付状态按钮
			click('xpath', '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			click("xpath", '//*[@id="custButton3"]/span/span')
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'数据已处理,请查看相应结果!')]")
			print("直联批量支付，查询支付状态成功！")
			sleep(3)
			
			# 测试打印功能--------------------------------------------------------------------------
			my_sql(my_host, my_port, my_user, my_passwd, my_db,
			        "update T_SE_PAYMENTS a set a.paystate='2' where  a.purpose = '付款处理直联批量付款'")
			my_sql(my_host, my_port, my_user, my_passwd, my_db,
			        "update t_se_payments set APPROVESTATE = '2' where purpose = '付款处理直联批量付款'")
			switch_to("xpath", "//iframe[@id='generalPayment-tab-iframe']")
			sleep(1)
			# 点击直联批量付款
			click("xpath", "//span[text()='直联批量付款']")
			# 进入直联批量付款的iframe窗体
			switch_to("xpath", "//iframe[@id='subTabThree-iframe']")
			sleep(1)
			
			# 勾选数据，点击打印按钮
			click('xpath', '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			click("xpath", "//span[text()='打印']")
			sleep(1)
			all_handles = self.driver.window_handles
			# 循环遍历所有新打开的窗口句柄，也就是说不包括主窗口
			now_handle = self.driver.current_window_handle
			for handle in all_handles:
				self.driver.switch_to.window(handle)
				if self.driver.title == u"payandrecbatchprint":
					implici_wait("xpath", "//td[contains(text(),'浙江华语科技')]")
					time.sleep(3)
					self.driver.switch_to.window(now_handle)
					switch_default()
			print("直联批量支付，打印成功!！")
			
		
			# 打印记录==================================================================================
			# 切入‘直联批量付款’的iframe窗体
			switch_to("xpath", "//iframe[@id='generalPayment-tab-iframe']")
			sleep(1)
			# 点击直联批量付款
			click("xpath", "//span[text()='直联批量付款']")
			# 进入直联批量付款的iframe窗体
			switch_to("xpath", "//iframe[@id='subTabThree-iframe']")
			sleep(1)
			
			# 勾选数据，点击按钮
			click('xpath', '//*[@id="gridbar-page-refresh"]')
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
			print("直联批量支付，打印记录查看成功！")
			time.sleep(3)
			switch_parent()
			
			# 点击关闭页面
			click("xpath", "//span[text()='打印记录']/preceding-sibling::*[1]")
			sleep(1)
			switch_default()
			print("直联批量支付，打印记录查看成功!")
			time.sleep(2)
			
			# 测试审批历史-------------------------------------------------------------------------------
			# 切入‘直联批量付款’的iframe窗体
			switch_to("xpath", "//iframe[@id='generalPayment-tab-iframe']")
			sleep(1)
			# 点击直联批量付款
			click("xpath", "//span[text()='直联批量付款']")
			# 进入直联批量付款的iframe窗体
			switch_to("xpath", "//iframe[@id='subTabThree-iframe']")
			sleep(1)
			# 勾选数据，点击按钮
			click('xpath', '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			click('xpath', "//span[text()='审批历史']")
			sleep(3)
			switch_to('xpath', '//*[@id="flowwin-iframe"]')
			click('xpath', "//span[text()='流程流转']")
			sleep(3)
			switch_parent()
			click('xpath', '//*[@id="f-win-title-flowwin"]/div[1]/div')
			print("直联批量支付，审批历史查看成功!")
			switch_default()
			
			# 测试确认已支付----------------------------------------------------------------------
			my_sql(my_host, my_port, my_user, my_passwd, my_db,
			        "update T_SE_PAYMENTS a set a.paystate='7' where  a.purpose = '付款处理直联批量付款'")
			# 切入‘直联批量付款’的iframe窗体
			switch_to("xpath", "//iframe[@id='generalPayment-tab-iframe']")
			sleep(1)
			# 点击直联批量付款
			click("xpath", "//span[text()='直联批量付款']")
			# 进入直联批量付款的iframe窗体
			switch_to("xpath", "//iframe[@id='subTabThree-iframe']")
			sleep(1)
			# 勾选数据，点击按钮
			click('xpath', '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			# 双击数据
			double_click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[3]/div')
			sleep(1)
			# 切入新增窗体
			switch_to('xpath', '//*[@id="flowwin-iframe"]')
			switch_to('xpath', '//*[@id="subTabOne-iframe"]')
			sleep(1)
			# 勾选数据
			click('xpath', '//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
			sleep(1)
			# 点击确认已支付
			click("xpath", '//*[@id="custButton2"]/span/span')
			sleep(1)
			# 点击ok
			click("xpath", '//*[@id="f-message-webgen-0-okBnt"]')
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("直联批量支付，测试确认已支付成功！")
			switch_to("xpath", "//iframe[@id='generalPayment-tab-iframe']")
			sleep(1)
			# 点击直联批量付款
			click("xpath", "//span[text()='直联批量付款']")
			# 进入直联批量付款的iframe窗体
			switch_to("xpath", "//iframe[@id='subTabThree-iframe']")
			click("xpath", '//*[@id="f-win-title-flowwin"]/div[1]/div')
			sleep(3)
			switch_default()
			
			# 测试确认支付失败需要付款单在一个小时之后，故手工测试
			
			# 测试确认非直联已支付----------------------------------------------------------------------
			my_sql(my_host, my_port, my_user, my_passwd, my_db,
			        "update T_SE_PAYMENTS a set a.paystate='3' where  a.purpose = '付款处理直联批量付款'")
			# 切入‘直联批量付款’的iframe窗体
			switch_to("xpath", "//iframe[@id='generalPayment-tab-iframe']")
			sleep(1)
			# 点击直联批量付款
			click("xpath", "//span[text()='直联批量付款']")
			# 进入直联批量付款的iframe窗体
			switch_to("xpath", "//iframe[@id='subTabThree-iframe']")
			sleep(1)
			# 勾选数据，点击按钮
			click('xpath', '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			# 双击数据
			double_click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[3]/div')
			sleep(1)
			# 切入新增窗体
			switch_to('xpath', '//*[@id="flowwin-iframe"]')
			switch_to('xpath', '//*[@id="subTabOne-iframe"]')
			sleep(1)
			# 勾选数据
			click('xpath', '//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
			sleep(1)
			# 点击非直联已支付
			click("xpath", '//*[@id="custButton5"]/span/span')
			sleep(1)
			# 点击ok
			click("xpath", '//*[@id="f-message-webgen-0-okBnt"]')
			sleep(1)
			# 切入新增窗体
			switch_to("xpath", '//*[@id="confirmUndirectPayWin-iframe"]')
			click("xpath", '//*[@id="combobox-input-actualsettlementmodeid"]')
			click("xpath", '//*[@id="actualsettlementmodeid-combogrid-body-table"]/tbody/tr/td[2]/div')
			# 点击确定
			click("xpath", '//*[@id="determineConfirmUndirectPay"]/span/span')
			click("xpath", '//*[@id="f-message-webgen-0-okBnt"]')
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'共1笔，处理成功1笔，失败0笔。')]")
			print("直联批量支付，测试确认非直联已支付成功！")
			switch_to("xpath", "//iframe[@id='generalPayment-tab-iframe']")
			sleep(1)
			# 点击直联批量付款
			click("xpath", "//span[text()='直联批量付款']")
			# 进入直联批量付款的iframe窗体
			switch_to("xpath", "//iframe[@id='subTabThree-iframe']")
			click("xpath", '//*[@id="f-win-title-flowwin"]/div[1]/div')
			sleep(3)
			switch_default()
			
			# 测试日志查看----------------------------------------------------------------------
			# 切入‘直联批量付款’的iframe窗体
			switch_to("xpath", "//iframe[@id='generalPayment-tab-iframe']")
			sleep(1)
			# 点击直联批量付款
			click("xpath", "//span[text()='直联批量付款']")
			# 进入直联批量付款的iframe窗体
			switch_to("xpath", "//iframe[@id='subTabThree-iframe']")
			sleep(1)
			# 勾选数据，点击按钮
			click('xpath', '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			# 双击数据
			double_click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[3]/div')
			sleep(1)
			# 切入新增窗体
			switch_to('xpath', '//*[@id="flowwin-iframe"]')
			switch_to('xpath', '//*[@id="subTabOne-iframe"]')
			sleep(2)
			# 勾选数据
			click('xpath', '//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
			sleep(1)
			# 点击日志查看
			click("xpath", '//*[@id="custButton4"]/span/span')
			
			implici_wait("xpath", '//*[@id="grid-body-table"]/tbody/tr/td[9]/div')
			print("直联批量支付，测试日志查看成功！")
			print("直联批量支付，测试成功！")
			sleep(1)
			my_sql(my_host, my_port, my_user, my_passwd, my_db,
			       "update T_SE_PAYMENTS a set a.paystate='2' where  a.purpose = '付款处理直联批量付款'")
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("直联批量支付失败！" + str(traceback.format_exc()))
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