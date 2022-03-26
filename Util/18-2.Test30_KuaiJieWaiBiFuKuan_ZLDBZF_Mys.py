# encoding=utf-8
# @Time : 2020/11/02 08:30
# @Author : zzg
# 此文件是测试MySQL版本资金结算管理--资金系统收付--外币收付结算--跨境外币汇款--直联单笔支付
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


class Test30_WaiBiShouFuJieSuan_KJWBFK_ZLDBZF(unittest.TestCase):
	
	# 启动浏览器
	def setUp(self):
		# 启动浏览器的另外一个方法：通过封装启动浏览器的驱动，启动不同浏览器
		self.driver = get("chrome")
	
	# 登陆系统、对系统设置进行操作
	def test_trade(self):
		
		# login(G_Ora_Url, mindy, Password, "亚唐科技")
		login(G_Mys_Url, mindy, Password, "亚唐科技")
		
		logging.info("开始测试资金结算管理-资金系统收付外币收付结算--跨境外币汇款--直联单笔支付")
		# 将页面的滚动条滑动到‘资金结算管理’页面的地方
		js_gd("xpath", "//span[contains(text(),'资金结算管理')]")
		# 用JS的方法点击资金结算管理菜单按钮
		js_click("xpath", "//span[contains(text(),'资金结算管理')]")
		sleep(1)
		# 点击'外币收付结算'菜单
		click("xpath", "//span[text()='外币收付结算']")
		sleep(1)
		# 点击收款处理菜单
		click("xpath", "//span[text()='跨境外币汇款']")
		sleep(1)
		# 退出所有iframe窗体
		switch_default()
		try:

			# 创建跨境外币汇款直联账户💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			##点击资金系统收付收回窗体
			click("xpath", "//span[text()='跨境外币汇款']")
			sleep(1)
			js_click("xpath", "//span[contains(text(),'资金结算管理')]")
			sleep(1)

			# 创建直联单笔收款账户
			js_gd("xpath", "//span[contains(text(),'账户资金监控')]")
			# 用JS的方法点击票据管理菜单按钮
			js_click("xpath", "//span[contains(text(),'账户资金监控')]")
			sleep(1)
			click("xpath",
			      '/html/body/div[1]/div[1]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div/ul/li[2]/a/span[2]')
			sleep(1)
			#点击账户维户
			click("xpath", "//span[text()='账户维护']")
			sleep(1)
			switch_default()
			
			# 切入单币种账户窗体
			switch_to("xpath", '//*[@id="bankAccounts-tab-iframe"]')
			sleep(1)
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			click("xpath", "//span[text()='新增']")
			switch_to("xpath", '//*[@id="addWin-iframe"]')
			sleep(1)
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
			sleep(1)
			
			#境内外
			# 输入开户行大连泡崖街支行名称，模糊查询
			input("xpath", "//input[@id='combobox-input-inorout']", "境内")
			sleep(1)
			input_down("xpath", "//input[@id='combobox-input-inorout']")
			input_enter("xpath", "//input[@id='combobox-input-inorout']")
			# 输入银行账号
			input("xpath", '//*[@id="accountnumber"]', '20211030')
			sleep(1)
			input("xpath", '//*[@id="accountname"]', '跨境外币汇款直联账户')
			
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
			
			# 点击查看
			js_click("xpath", "//span[@class='f-contrac-close']")
			sleep(1)
			# 输入银行：中国银行
			click("xpath", "//input[@id='combobox-input-bankid']")
			sleep(1)
			input("xpath", "//input[@id='combobox-input-bankid']", "中国银行")
			sleep(1)
			click("xpath", "//div[@title='代码-名称:BOC-中国银行']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
			sleep(1)
			input("xpath", '//*[@id="accountnumber"]', '20211030')
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
			print("跨境外币汇款直联账户创建成功")
		
			# 点击账户资金监控，收回窗体
			js_click("xpath", "//span[contains(text(),'账户资金监控')]")
			sleep(1)
			
			# 新增结算方式以及交易类型💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 开始创建直联批量付款的交易类型以及结算方式
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
			# 切入新增的iframe窗体
			switch_to("xpath", "//iframe[@id='addWin-iframe']")
			sleep(1)

			# 输入代码
			input("xpath", "//input[@name='code']", "2030")
			sleep(1)

			# 输入结算方式
			input("xpath", "//input[@id='name']", "直联跨境外币汇款")
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
			input("xpath", "//input[@id='combobox-input-dealtype']", "直联")
			sleep(1)
			input_down("xpath", "//input[@id='combobox-input-dealtype']")
			input_enter("xpath", "//input[@id='combobox-input-dealtype']")
			sleep(1)
			# 增加直联渠道
			click("xpath", "//span[text()='新增行']")
			#直联银行
			input("xpath", '//*[@id="combobox-input-editgrid-bankid-0"]', 'BOC-中国银行')
			click('xpath', '//*[@id="editgrid-bankid-0-combogrid-body-table"]/tbody/tr/td[2]/div')
			sleep(1)

			#交易场景
			clear("xpath",'//*[@id="combobox-input-editgrid-currencyscenarios-0"]')
			sleep(1)
			input("xpath",'//*[@id="combobox-input-editgrid-currencyscenarios-0"]','跨境同币')
			sleep(1)
			input_down("xpath",'//*[@id="combobox-input-editgrid-currencyscenarios-0"]')
			input_enter("xpath",'//*[@id="combobox-input-editgrid-currencyscenarios-0"]')
			sleep(1)

			# #币种
			# click("xpath",'//*[@id="combobox-input-editgrid-currencyid-0"]')
			# sleep(1)
			# input_down("xpath", '//*[@id="combobox-input-editgrid-currencyid-0"]')
			# input_enter("xpath", '//*[@id="combobox-input-editgrid-currencyid-0"]')
			# sleep(1)

			#结算场景
			input('xpath', '//*[@id="combobox-input-editgrid-settlementscenarios-0"]', '跨行默认')
			click('xpath', '//*[@id="f-combo-editgrid-settlementscenarios-0-list-0"]')
			sleep(1)
			#直联渠道
			click('xpath', '//*[@id="combobox-input-editgrid-directchannelid-0"]')
			sleep(1)
			click('xpath', '//*[@id="editgrid-directchannelid-0-combogrid-body-table"]/tbody/tr[1]/td[2]/div')
			sleep(1)
			#直联渠道指令
			input('xpath', '//*[@id="combobox-input-editgrid-directchannelcmdid-0"]','对外支付')
			sleep(1)
			click('xpath', '//*[@id="editgrid-directchannelcmdid-0-combogrid-body-table"]/tbody/tr[1]/td[2]/div')
			sleep(1)
			#跨行支付系统
			click('xpath', '//*[@id="combobox-input-editgrid-directinterbanksystemid-0"]')
			sleep(1)
			click('xpath', '//*[@id="editgrid-directinterbanksystemid-0-combogrid-body-table"]/tbody/tr[1]/td[2]/div')
			sleep(1)
			# 点击保存按钮
			click("xpath", "//span[text()='保存']")
			sleep(3)
			# 退出所有iframe窗体
			switch_default()

			# 创建直联单笔收款的交易类型💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			click("xpath", "//span[text()='交易类型']")

			switch_to('xpath', '//*[@id="payType-tab-iframe"]')
			js_click("xpath", "//span[text()='新增']")
			# 切入新增的iframe窗体
			switch_to("xpath", "//iframe[@id='addWin-iframe']")
			sleep(1)

			# 输入代码
			input("xpath", "//input[@id='code']", "3030")
			sleep(1)

			# 输入名称
			input("xpath", "//input[@id='name']", "直联跨境外币汇款交易类型")
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
			input("xpath", "//input[@id='combobox-input-settlementmoderange']", '2030')
			sleep(1)
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
			print("跨境外币汇款，结算方式创建成功")
			switch_default()

			# 返回直联单笔收款页面
			js_click("xpath", "//span[text()='基础设置']")
			sleep(1)
			js_click("xpath", "//span[text()='外币收付结算']")
			sleep(1)
			# 点击收款处理菜单
			js_gd("xpath", "//span[text()='跨境外币汇款']")
			js_click("xpath", "//span[text()='跨境外币汇款']")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			
			
			# 测试新增功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			for i in range(1,3):
				global use
				# 切入跨境外币汇款界面
				switch_to("xpath", '//*[@id="crossBorderPayment-tab-iframe"]')
				switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
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
				click("xpath",'//*[@id="oppbanklocationid-combogrid-body-table"]/tbody/tr/td[2]/div')
				sleep(1)
				
				# 用途
				if i ==1 :
					use = random.randint(1000, 10000)
					input("xpath", '//*[@id="combobox-input-purpose"]', use)
					sleep(1)
				if i ==2 :
					use2 = random.randint(1000, 10000)
					input("xpath", '//*[@id="combobox-input-purpose"]', use2)
					sleep(1)
				click("xpath", '//*[@title="加急"]')

				
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
				if i ==2 :
					print("跨境外币汇款-直联单笔支付，新增成功！")
				time.sleep(3)
			
			# 测试修改功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入跨境外币汇款界面
			switch_to("xpath", '//*[@id="crossBorderPayment-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			#刷新、勾选按钮
			click("xpath",'//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath",'//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			#修改
			span_click("修改")
			switch_to("xpath",'//*[@id="modWin-iframe"]')
			input("xpath",'//*[@id="ouraddress"]','浙江杭州')
			sleep(1)
			span_click("保存")
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("跨境外币汇款-直联单笔支付，修改成功！")
			time.sleep(3)
			
			# 测试删除功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入跨境外币汇款界面
			switch_to("xpath", '//*[@id="crossBorderPayment-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			#点击删除
			span_click("删除")
			sleep(1)
			ok_click()
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("跨境外币汇款-直联单笔支付，删除成功！")
			time.sleep(3)
			
			# 测试送审、撤销送审功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入跨境外币汇款界面
			switch_to("xpath", '//*[@id="crossBorderPayment-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("送审")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！送审成功1笔，失败0笔。')]")
			print("跨境外币汇款-直联单笔支付，送审成功！")
			time.sleep(3)
			
			#测试撤销送审
			# 切入跨境外币汇款界面
			switch_to("xpath", '//*[@id="crossBorderPayment-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			triangle_cick("送审")
			sleep(1)
			click("xpath","//a[contains(text(),'撤销送审')]")
			sleep(1)
			ok_click()
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'撤销送审成功！')]")
			print("跨境外币汇款-直联单笔支付，撤销送审成功！")
			time.sleep(3)
			
			# 测试支付功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入跨境外币汇款界面
			switch_to("xpath", '//*[@id="crossBorderPayment-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			span_click("送审")
			switch_default()
			time.sleep(3)
			#二审
			# 切入跨境外币汇款界面
			switch_to("xpath", '//*[@id="crossBorderPayment-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			double_click("xpath",'//*[@id="grid-body-table"]/tbody/tr/td[3]/div')
			sleep(1)
			switch_to("xpath",'//*[@id="wf_taskProcessing_win-iframe"]')
			span_click("同意")
			sleep(1)
			# 退出当前窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			time.sleep(3)
			
			#三审
			# 切入跨境外币汇款界面
			switch_to("xpath", '//*[@id="crossBorderPayment-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			double_click("xpath", '//*[@id="grid-body-table"]/tbody/tr/td[3]/div')
			sleep(1)
			switch_to("xpath", '//*[@id="wf_taskProcessing_win-iframe"]')
			span_click("同意")
			sleep(1)
			# 退出当前窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			time.sleep(3)
			
			#支付
			# 切入跨境外币汇款界面
			switch_to("xpath", '//*[@id="crossBorderPayment-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			span_click("支付")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！1笔进行了支付，0笔不允许支付。')]")
			print("跨境外币汇款-直联单笔支付，支付成功！")
			time.sleep(3)
			
			#测试余额检测💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入跨境外币汇款界面
			switch_to("xpath", '//*[@id="crossBorderPayment-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			#余额检测
			triangle_cick("支付")
			sleep(1)
			click("xpath", "//a[contains(text(),'余额检测')]")
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'余额充足')]")
			print("跨境外币汇款-直联单笔支付，余额检测成功！")
			time.sleep(3)
			
			# 测试查询状态💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入跨境外币汇款界面
			sql = "update t_se_payments set paystate = '7' where purpose = '" + str(use) + "'"
			my_sql(my_host, my_port, my_user, my_passwd, my_db,
			       sql)
			switch_to("xpath", '//*[@id="crossBorderPayment-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			# 查询状态
			triangle_cick("支付")
			sleep(1)
			click("xpath", "//a[contains(text(),'查询状态')]")
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'单据已查询状态，请查看相应结果！')]")
			print("跨境外币汇款-直联单笔支付，余额检测成功！")
			time.sleep(3)
			
			# 测试确认已支付💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入跨境外币汇款界面
			sql2 = "update t_se_payments set paystate = '7' where purpose = '" + str(use) + "'"
			my_sql(my_host, my_port, my_user, my_passwd, my_db,
			       sql2)
			switch_to("xpath", '//*[@id="crossBorderPayment-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			# 确认已支付
			triangle_cick("支付")
			sleep(1)
			click("xpath", "//a[contains(text(),'确认已支付')]")
			sleep(1)
			ok_click()
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功')]")
			print("跨境外币汇款-直联单笔支付，确认已支付成功！")
			time.sleep(3)
			
			# 测试非直联已支付💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入跨境外币汇款界面
			sql3 = "update t_se_payments set paystate = '3' where purpose = '" + str(use) + "'"
			my_sql(my_host, my_port, my_user, my_passwd, my_db,
			       sql3)
			switch_to("xpath", '//*[@id="crossBorderPayment-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			# 确认非直联已支付
			triangle_cick("支付")
			sleep(1)
			click("xpath", "//a[contains(text(),'确认非直联已支付')]")
			sleep(1)
			ok_click()
			sleep(1)
			switch_to("xpath",'//*[@id="confirmUndirectPayWin-iframe"]')
			input("xpath",'//*[@id="combobox-input-actualsettlementmodeid"]','601-其他支付')
			sleep(1)
			input_down("xpath",'//*[@id="combobox-input-actualsettlementmodeid"]')
			input_enter("xpath",'//*[@id="combobox-input-actualsettlementmodeid"]')
			sleep(1)
			
			span_click("确定")
			sleep(1)
			ok_click()
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'共1笔，处理成功1笔，失败0笔。')]")
			print("跨境外币汇款-直联单笔支付， 确认非直联已支付成功！")
			time.sleep(3)
			
			# 测日志查看💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入跨境外币汇款界面
			switch_to("xpath", '//*[@id="crossBorderPayment-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			# 日志查看
			triangle_cick("支付")
			sleep(1)
			click("xpath", "//a[contains(text(),'日志查看')]")
			sleep(1)
			switch_to("xpath",'//*[@id="logsWin-iframe"]')
			sleep(1)
			implici_wait("xpath", "//div[contains(text(),'查询状态')]")
			print("跨境外币汇款-直联单笔支付，日志查看成功！")
			# 退出所有iframe窗体
			switch_parent()
			click("xpath",'//*[@id="f-win-title-logsWin"]/div[1]/div')
			sleep(1)
			switch_default()
			time.sleep(3)
			
			# 测试审批历史功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入跨境外币汇款界面
			switch_to("xpath", '//*[@id="crossBorderPayment-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("审批历史")
			sleep(1)
			switch_to("xpath",'//*[@id="flowwin-iframe"]')
			sleep(3)
			span_click("流程流转")
			sleep(1)
			implici_wait("xpath", "//div[contains(text(),'开始')]")
			print("跨境外币汇款-直联单笔支付，审批历史查看成功！")
			switch_parent()
			click("xpath",'//*[@id="f-win-title-flowwin"]/div[1]/div')
			sleep(1)
			switch_default()
			time.sleep(3)
			
			#测试打印功能
			# 切入跨境外币汇款界面
			switch_to("xpath", '//*[@id="crossBorderPayment-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			# 用JS方便点击‘支付’按钮旁边的倒三角形
			js_click("xpath", "//span[text()='其他操作']/parent::*/following-sibling::*/child::*")
			sleep(1)
			
			# 点击打印按钮
			js_click("xpath", "//a[contains(text(),'打印')]")
			time.sleep(3)
			
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
		
			
			# 测试打印记录功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入跨境外币汇款界面
			switch_to("xpath", '//*[@id="crossBorderPayment-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			# 用JS方便点击‘其他操作’按钮旁边的倒三角形
			js_click("xpath", "//span[text()='其他操作']/parent::*/following-sibling::*/child::*")
			sleep(1)
			
			# 点击打印按钮
			js_click("xpath", "//a[contains(text(),'打印记录')]")
			time.sleep(3)
			switch_to("xpath",'//*[@id="printWin-iframe"]')
			# 用隐式等待方法等页面出现  操作人:mindy
			implici_wait("xpath", "//div[@title='操作人:mindy']")
			print("跨境外币汇款-直联单笔支付，打印记录查看成功！")
			switch_parent()
			click("xpath",'//*[@id="f-win-title-printWin"]/div[1]/div')
			sleep(1)
			switch_default()
			sleep(3)
			
			# 测试冲正功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入跨境外币汇款界面
			switch_to("xpath", '//*[@id="crossBorderPayment-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			# 用JS方便点击‘其他操作’按钮旁边的倒三角形
			js_click("xpath", "//span[text()='其他操作']/parent::*/following-sibling::*/child::*")
			sleep(1)
			
			# 点击冲正按钮
			js_click("xpath", "//a[contains(text(),'冲正')]")
			sleep(1)
			#切入冲正窗体
			switch_to("xpath",'//*[@id="reverseWin-iframe"]')
			#冲正日期
			today = date.today()
			we = str(today) + " " + "08:30:00"
			input("xpath",'//*[@id="reversedate-input"]',we)
			sleep(1)
			
			
			#冲正原因
			span_click("冲正日期")
			click("xpath",'//*[@id="reversalreason"]')
			input("xpath",'//*[@id="reversalreason"]','测试冲正')
			sleep(1)
			
			#生成付款单
			click("xpath",'//*[@id="iscreatenewtrade"]')
			sleep(1)
			span_click("确认冲正")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("跨境外币汇款-直联单笔支付，冲正成功成功！")
			time.sleep(3)
			
			# 测试作废功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入跨境外币汇款界面
			switch_to("xpath", '//*[@id="crossBorderPayment-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			# 用JS方便点击‘其他操作’按钮旁边的倒三角形
			js_click("xpath", "//span[text()='其他操作']/parent::*/following-sibling::*/child::*")
			sleep(1)
			
			# 点击冲正按钮
			js_click("xpath", "//a[contains(text(),'作废')]")
			sleep(1)
			ok_click()
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("跨境外币汇款-直联单笔支付，作废成功！")
			time.sleep(3)

			# 测试上传功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入跨境外币汇款界面
			switch_to("xpath", '//*[@id="crossBorderPayment-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			
			# 点击上传
			click("xpath", '//*[@id="gridtitle"]/div[3]/div[2]')
			sleep(1)
			switch_to("xpath", '//*[@id="importDataWin-iframe"]')
			
			# 业务
			clear("xpath", '//*[@id="combobox-input-businessid"]')
			sleep(1)
			input("xpath", '//*[@id="combobox-input-businessid"]', '跨境外币直联单笔付款单导入')
			sleep(1)
			
			# #对接方式
			# click("xpath",'//*[@id="combobox-input-converttypeid"]')
			# sleep(1)
			# input_down("xpath",'//*[@id="combobox-input-converttypeid"]')
			# sleep(1)
			# input_enter("xpath",'//*[@id="combobox-input-converttypeid"]')
			# sleep(1)
			
			span_click("下一步")
			sleep(1)
			switch_to("xpath", '//*[@id="loadNextWin-iframe"]')
			sleep(1)
			# 交易类型
			input("xpath", '//*[@id="combobox-input-paytypeid"]', '3030-直联跨境外币汇款交易类型')
			sleep(1)
			input_down("xpath", '//*[@id="combobox-input-paytypeid"]')
			input_enter("xpath", '//*[@id="combobox-input-paytypeid"]')
			sleep(2)
			# # 结算方式
			# input("xpath", '//*[@id="combobox-input-settlementmodeid"]', '601-其他支付')
			# sleep(1)
			# input_down("xpath", '//*[@id="combobox-input-settlementmodeid"]')
			# input_enter("xpath", '//*[@id="combobox-input-settlementmodeid"]')
			# sleep(1)
			
			# 附件上传
			upload_click("xpath", "//div[text()='上传文件']/parent::*[1]/descendant::*[4]",
			             'D:\FlieDownload', '"KuaJingWaiBiHuiKuan.xls"')
			sleep(3)
			# 点击保存按钮
			click("xpath", "//span[text()='上传']")
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功')]")
			print("其他结购换汇，导入成功！")
			time.sleep(3)
		
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("直联结购换汇失败！" + str(traceback.format_exc()))
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
