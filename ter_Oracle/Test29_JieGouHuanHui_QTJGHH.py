# encoding=utf-8
# @Time : 2020/11/03 08:30
# @Author : zzg
# 此文件是测试Oracle版本资金结算管理--资金系统收付--结购换汇--其他结购换汇
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
class Test29_JieGouHuanHui_QTJGHH(unittest.TestCase):
	
	# 启动浏览器
	def setUp(self):
		# 启动浏览器的另外一个方法：通过封装启动浏览器的驱动，启动不同浏览器
		self.driver = get("chrome")
	
	# 登陆系统、对系统设置进行操作
	def test_trade(self):
		
		# login(G_Ora_Url, mindy, Password, "亚唐科技")
		login(G_Ora_Url, mindy, Password, "亚唐科技")
		
		logging.info("开始测试资金结算管理-资金系统收付-结购换汇-其他结购换汇")
		# 将页面的滚动条滑动到‘资金结算管理’页面的地方
		js_gd("xpath", "//span[contains(text(),'资金结算管理')]")
		# 用JS的方法点击资金结算管理菜单按钮
		js_click("xpath", "//span[contains(text(),'资金结算管理')]")
		sleep(1)
		# 点击'资金系统收付'菜单
		click("xpath", "//span[text()='资金系统收付']")
		sleep(1)
		# 点击收款处理菜单
		click("xpath", "//span[text()='结购换汇']")
		sleep(1)
		# 退出所有iframe窗体
		switch_default()
		try:
			'''
			# 创建其他结构换汇账户💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			##点击资金系统收付收回窗体
			click("xpath", "//span[text()='资金系统收付']")
			sleep(1)
			js_click("xpath", "//span[contains(text(),'资金结算管理')]")
			sleep(1)

			# 创建其他结购换汇账户
			js_gd("xpath", "//span[contains(text(),'账户资金监控')]")
			# 用JS的方法点击票据管理菜单按钮
			js_click("xpath", "//span[contains(text(),'账户资金监控')]")
			sleep(1)
			click("xpath", "//span[text()='账户生命周期']")
			sleep(1)
			#点击账户维户
			click("xpath", "//span[text()='账户维护']")
			sleep(1)
			switch_default()

			for i in range(1,3):
				# 切入单币种账户窗体
				switch_to("xpath", '//*[@id="bankAccounts-tab-iframe"]')
				switch_to("xpath", '//*[@id="subTabOne-iframe"]')
				#点击新增按钮
				click("xpath", "//span[text()='新增']")
				sleep(1)
				switch_to("xpath", '//*[@id="addWin-iframe"]')
				click("xpath", "//input[@id='combobox-input-bankid']")
				sleep(1)
				# 模糊匹配报错，因此选择直接点击
				click("xpath", "//div[@title='代码-名称:BOC-中国银行']")
				sleep(1)

				# 选择开户行
				click("xpath", "//input[@id='combobox-input-banklocationid']")
				sleep(1)
				input("xpath", "//input[@id='combobox-input-banklocationid']", "104611010734-中国银行股份有限公司南宁市江南支行")
				sleep(1)
				click("xpath", '//*[@id="banklocationid-combogrid-body-table"]/tbody/tr[1]/td[2]/div')
				sleep(1)

				# 选择币种
				click("xpath", "//input[@id='combobox-input-currencyid']")
				# 输入开户行大连泡崖街支行名称，模糊查询
				if i == 1:
					input("xpath", "//input[@id='combobox-input-currencyid']", "CNY")
					sleep(1)
				if i == 2:
					input("xpath", "//input[@id='combobox-input-currencyid']", "USD")
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
				if i==2 :
					click("xpath", "//input[@id='isbankdirect']")
					sleep(1)
				#选择境内外
				click("xpath", "//input[@id='combobox-input-inorout']")
				sleep(1)
				input("xpath", "//input[@id='combobox-input-inorout']", "境内")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-inorout']")
				input_enter("xpath", "//input[@id='combobox-input-inorout']")
				sleep(1)
				# 输入银行账号
				if i == 1:
					input("xpath", '//*[@id="accountnumber"]', '20211029')
					sleep(1)
					input("xpath", '//*[@id="accountname"]', '其他购汇账户')
				if i == 2:
					input("xpath", '//*[@id="accountnumber"]', '2021102901')
					sleep(1)
					input("xpath", '//*[@id="accountname"]', '美元直联账户2号')

				# 点击保存按钮
				click("xpath", "//span[text()='保存']")
				# 退出所有iframe窗体
				switch_default()
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")

				sleep(1)
				# 切入窗体
				switch_to("xpath", '//*[@id="bankAccounts-tab-iframe"]')
				switch_to("xpath", '//*[@id="subTabOne-iframe"]')
				sleep(1)
				# 点击查看
				if i ==1 :
					js_click("xpath", "//span[@class='f-contrac-close']")
					sleep(1)
				if i == 1:
					input("xpath", '//*[@id="accountnumber"]', '20211029')
					sleep(1)
				if i == 2:
					clear("xpath",'//*[@id="accountnumber"]')
					sleep(1)
					input("xpath", '//*[@id="accountnumber"]', '2021102901')
					sleep(1)
				# 点击查询
				click("xpath", "//span[text()='查询']")
				sleep(1)

				# 勾选数据
				click("xpath", '//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
				sleep(1)
				click("xpath", '/html/body/div[1]/div[3]/div[1]/div[1]/a/em')
				click("xpath", '/html/body/div[1]/div[3]/div[1]/div[2]/ul/li[1]/a')
				click("xpath", "//input[@id='openeddatewin-input']")
				sleep(2)
				if i == 1 :
					today = date.today()
					open_date = today - timedelta(days=20)
					click("xpath", "//input[@id='openeddatewin-input']")
					sleep(1)
					clear("xpath", "//input[@id='openeddatewin-input']")
					sleep(1)
					input("xpath", "//input[@id='openeddatewin-input']", str(open_date))
					time.sleep(1)
					# 输入初始余额
					clear("xpath", '//*[@id="initbalance-input"]')
					sleep(1)
					input("xpath", '//*[@id="initbalance-input"]', "30000")
					sleep(1)
					click("xpath", '//*[@id="initbalance-input"]')
					sleep(1)
					click("xpath", "//span[text()='确定']")
					sleep(1)
					switch_default()
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("其他购汇账户创建成功")


				if i == 2 :
					today = date.today()
					open_date = today - timedelta(days=20)
					click("xpath", "//input[@id='openeddatewin-input']")
					sleep(1)
					clear("xpath", "//input[@id='openeddatewin-input']")
					sleep(1)
					input("xpath", "//input[@id='openeddatewin-input']", str(open_date))
					time.sleep(1)
					click("xpath", '//*[@id="journalbalance-input"]')
					sleep(1)
					clear("xpath", '//*[@id="journalbalance-input"]')
					sleep(1)
					input("xpath", '//*[@id="journalbalance-input"]', "30000")
					sleep(1)
					click("xpath", "//span[text()='确定']")
					sleep(1)
					switch_default()
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("美元账户创建成功")

			# 点击账户资金监控，收回窗体
			js_click("xpath", "//span[contains(text(),'账户资金监控')]")
			sleep(1)
			
			
			# 新增交易类型💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 开始创建直联批量付款的交易类型以及结算方式
			# js_gd("xpath", "//span[contains(text(),'资金结算管理')]")
			# # 用JS的方法点击资金结算管理菜单按钮
			# js_click("xpath", "//span[contains(text(),'资金结算管理')]")
			# sleep(1)
			# 点击基础设置
			click("xpath", "//li[@f_value='settlementSetting']/descendant-or-self::*[5]")

			sleep(1)

			# 创建直联单笔收款的交易类型💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			click("xpath", "//span[text()='交易类型']")
			sleep(1)
			switch_to('xpath', '//*[@id="payType-tab-iframe"]')
			js_click("xpath", "//span[text()='新增']")
			# 切入新增的iframe窗体
			switch_to("xpath", "//iframe[@id='addWin-iframe']")
			sleep(1)

			# 输入代码
			input("xpath", "//input[@id='code']", "3029")
			sleep(1)

			# 输入名称
			input("xpath", "//input[@id='name']", "其他购汇交易类型")
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
			input("xpath", "//input[@id='combobox-input-paytypecategory']", "购汇")
			sleep(1)
			input_down("xpath", "//input[@id='combobox-input-paytypecategory']")
			input_enter("xpath", "//input[@id='combobox-input-paytypecategory']")
			sleep(1)

			# 可选结算方式
			input("xpath", "//input[@id='combobox-input-settlementmoderange']", '601')
			sleep(1)
			click("xpath", '//*[@id="settlementmoderange-combogrid-body-table"]/tbody/tr/td[2]/div/button')
			sleep(1)
			#清楚下拉框
			click("xpath",'//*[@id="combobox-input-defaultsettlementmodeid"]')
			sleep(1)
			click("xpath",'//*[@id="combobox-input-oppobjecttype"]')
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
			print("结购换汇-直联结购换汇，结算方式创建成功")
			switch_default()

			# 返回结购换汇页面
			js_click("xpath", "//span[text()='基础设置']")
			sleep(1)
			js_click("xpath", "//span[text()='资金系统收付']")
			sleep(1)
			# 点击收款处理菜单
			js_click("xpath", "//span[text()='结购换汇']")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			'''
			
			# 测试新增功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			for i in range(1,4):
				global use
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
				input_down("xpath",'//*[@id="combobox-input-lbankaccountid"]')
				input_enter("xpath",'//*[@id="combobox-input-lbankaccountid"]')
				sleep(1)

				# 输入购汇金额
				money = random.randint(100,300)
				double_click("xpath", '//*[@id="lamount-input"]')
				sleep(1)
				input("xpath",'//*[@id="lamount-input"]',money)
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
				input("xpath", '//*[@id="famount-input"]', money*6)
				sleep(1)

				# 用途
				if i ==1 :
					use = random.randint(1000,10000)
					input("xpath", "//input[@id='combobox-input-purpose']", use)
					sleep(1)
				if i ==2 :
					use2 = random.randint(1000,10000)
					input("xpath", "//input[@id='combobox-input-purpose']", use2)
					sleep(1)
				if i ==3 :
					use3 = random.randint(1000,10000)
					input("xpath", "//input[@id='combobox-input-purpose']", use3)
					sleep(1)

				# 点击保存按钮
				click("xpath", "//span[text()='保存']")
				sleep(1)
				# 退出所有iframe窗体
				switch_default()

				# 用隐式等待方法等页面出现新增成功的提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				if i ==3 :
					print("其他结购换汇，新增成功" )
				time.sleep(3)

			# 测试修改功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入结购换汇的iframe窗体
			switch_to("xpath", "//iframe[@id='exchangePay-tab-iframe']")
			# 点击其他结购换汇
			click("xpath", "//span[text()='其他结购换汇']")
			sleep(1)
			switch_to("xpath", "//iframe[@id='subTabTwo-iframe']")
			#刷新、勾选按钮
			click("xpath",'//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath",'//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)

			#点击修改
			span_click("修改")
			sleep(1)
			# 切入修改的iframe窗体
			switch_to("xpath", "//iframe[@id='modWin-iframe']")
			input("xpath",'//*[@id="memo"]','测试修改')
			sleep(1)
			# 点击保存按钮
			click("xpath", "//span[text()='保存']")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("结购换汇-其他结购换汇，修改成功！")
			time.sleep(3)

			# 测试删除功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入结购换汇的iframe窗体
			switch_to("xpath", "//iframe[@id='exchangePay-tab-iframe']")
			# 点击其他结购换汇
			click("xpath", "//span[text()='其他结购换汇']")
			sleep(1)
			switch_to("xpath", "//iframe[@id='subTabTwo-iframe']")
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)

			span_click("删除")
			sleep(1)
			# 点击弹出框的OK键
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("结购换汇-其他结购换汇，删除成功！")
			time.sleep(3)

			# 测试作废功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入结购换汇的iframe窗体
			switch_to("xpath", "//iframe[@id='exchangePay-tab-iframe']")
			# 点击其他结购换汇
			click("xpath", "//span[text()='其他结购换汇']")
			sleep(1)
			switch_to("xpath", "//iframe[@id='subTabTwo-iframe']")
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)

			# 点击作废按钮
			click("xpath", "//span[text()='作废']")
			sleep(1)
			# 点击弹出框的OK键
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("结购换汇-其他结购换汇，作废成功！")
			time.sleep(3)

			# 测试送审、撤销送审功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入结购换汇的iframe窗体
			switch_to("xpath", "//iframe[@id='exchangePay-tab-iframe']")
			# 点击其他结购换汇
			click("xpath", "//span[text()='其他结购换汇']")
			sleep(1)
			switch_to("xpath", "//iframe[@id='subTabTwo-iframe']")
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)

			# 点击审核按钮
			click("xpath", "//span[text()='送审']")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！送审成功1笔，失败0笔。')]")
			print("结购换汇-其他结购换汇，送审成功！")
			time.sleep(3)

			#测试撤销送审
			# 切入结购换汇的iframe窗体
			switch_to("xpath", "//iframe[@id='exchangePay-tab-iframe']")
			# 点击其他结购换汇
			click("xpath", "//span[text()='其他结购换汇']")
			sleep(1)
			switch_to("xpath", "//iframe[@id='subTabTwo-iframe']")
			# 刷新、勾选按钮
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
			print("结购换汇-其他结购换汇，撤销送审成功！")
			time.sleep(3)
			
			
			# 测试支付功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入结购换汇的iframe窗体
			switch_to("xpath", "//iframe[@id='exchangePay-tab-iframe']")
			# 点击其他结购换汇
			click("xpath", "//span[text()='其他结购换汇']")
			sleep(1)
			switch_to("xpath", "//iframe[@id='subTabTwo-iframe']")
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)

			# 点击审核按钮
			click("xpath", "//span[text()='送审']")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			time.sleep(3)

			#二审
			# 切入结购换汇的iframe窗体
			switch_to("xpath", "//iframe[@id='exchangePay-tab-iframe']")
			# 点击其他结购换汇
			click("xpath", "//span[text()='其他结购换汇']")
			sleep(1)
			switch_to("xpath", "//iframe[@id='subTabTwo-iframe']")
			double_click("xpath",'//*[@id="grid-body-table"]/tbody/tr[1]/td[3]/div')
			sleep(1)
			switch_to("xpath",'//*[@id="wf_taskProcessing_win-iframe"]')
			span_click("同意")
			switch_default()
			sleep(3)
			# 切入结购换汇的iframe窗体
			switch_to("xpath", "//iframe[@id='exchangePay-tab-iframe']")
			# 点击其他结购换汇
			click("xpath", "//span[text()='其他结购换汇']")
			sleep(1)
			switch_to("xpath", "//iframe[@id='subTabTwo-iframe']")
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			#点击支付
			click("xpath", "//span[text()='支付']")
			sleep(1)
			click("xpath", "//span[text()='确定']")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'确认支付成功！')]")
			print("结购换汇-其他结购换汇，支付成功！")
			time.sleep(3)

			# 测试上传功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入结购换汇的iframe窗体
			switch_to("xpath", "//iframe[@id='exchangePay-tab-iframe']")
			# 点击其他结购换汇
			click("xpath", "//span[text()='其他结购换汇']")
			sleep(1)
			switch_to("xpath", "//iframe[@id='subTabTwo-iframe']")
			
			# 点击上传
			click("xpath", '//*[@id="gridtitle"]/div[3]/div[2]')
			sleep(1)
			switch_to("xpath", '//*[@id="importDataWin-iframe"]')
			# 业务
			
			clear("xpath", '//*[@id="combobox-input-businessid"]')
			sleep(1)
			input("xpath", '//*[@id="combobox-input-businessid"]', '其他结购换汇导入')
			sleep(1)
			span_click("下一步")
			sleep(1)
			switch_to("xpath", '//*[@id="loadNextWin-iframe"]')
			sleep(1)
			# 交易类型
			input("xpath", '//*[@id="combobox-input-paytypeid"]', '3029-其他购汇交易类型')
			sleep(1)
			input_down("xpath", '//*[@id="combobox-input-paytypeid"]')
			input_enter("xpath", '//*[@id="combobox-input-paytypeid"]')
			sleep(1)
			# 结算方式
			input("xpath", '//*[@id="combobox-input-settlementmodeid"]', '601-其他支付')
			sleep(1)
			input_down("xpath", '//*[@id="combobox-input-settlementmodeid"]')
			input_enter("xpath", '//*[@id="combobox-input-settlementmodeid"]')
			sleep(1)
			
			# 附件上传
			upload_click("xpath", "//div[text()='上传文件']/parent::*[1]/descendant::*[4]",
			             'D:\FlieDownload', '"exchangepay1.xls"')
			sleep(3)
			# 点击保存按钮
			click("xpath", "//span[text()='上传']")
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功')]")
			print("结购换汇-其他结购换汇，导入成功！")
			time.sleep(3)
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("其他结购换汇失败！" + str(traceback.format_exc()))
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
