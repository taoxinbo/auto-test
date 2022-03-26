# encoding=utf-8
# @Time : 2020/11/11 08:30
# @Author : zzg
# 此文件是测试MySQL版本资金结算管理--业务系统对接--快捷付款--直联批量付款处理
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


class Test39_KuaiJieFuKuan_ZLPLFKCL(unittest.TestCase):
	
	# 启动浏览器
	def setUp(self):
		# 启动浏览器的另外一个方法：通过封装启动浏览器的驱动，启动不同浏览器
		self.driver = get("chrome")
	
	# 登陆系统、对系统设置进行操作
	def test_trade(self):
		
		# login(G_Ora_Url, mindy, Password, "亚唐科技")
		login(G_Mys_Url, mindy, Password, "亚唐科技")
		
		logging.info("开始测试资金结算管理--业务系统对接--快捷付款--直联批量付款处理")
		# 将页面的滚动条滑动到‘资金结算管理’页面的地方
		js_gd("xpath", "//span[contains(text(),'资金结算管理')]")
		# 用JS的方法点击资金结算管理菜单按钮
		js_click("xpath", "//span[contains(text(),'资金结算管理')]")
		sleep(1)
		# 点击'外币收付结算'菜单
		click("xpath", "//span[text()='业务系统对接']")
		sleep(1)
		# 点击收款处理菜单
		click("xpath", "//span[text()='快捷付款']")
		sleep(1)
		# 退出所有iframe窗体
		switch_default()
		try:

			#创建快捷付款--直联批量付款处理账户💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			#收回窗体
			click("xpath", "//span[text()='业务系统对接']")
			sleep(1)
			js_click("xpath", "//span[contains(text(),'资金结算管理')]")
			sleep(1)
			
			# 将页面的滚动条滑动到‘票据管理’页面的地方
			js_gd("xpath", "//span[contains(text(),'账户资金监控')]")
			# 用JS的方法点击账户资金监控菜单按钮
			js_click("xpath", "//span[contains(text(),'账户资金监控')]")
			sleep(1)
			click("xpath",
			      '/html/body/div[1]/div[1]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div/ul/li[2]/a/span[2]')
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
			
			# 选择境内外
			
			click("xpath", "//input[@id='combobox-input-inorout']")
			# 输入开户行大连泡崖街支行名称，模糊查询
			input("xpath", "//input[@id='combobox-input-inorout']", "境内")
			sleep(1)
			input_down("xpath", "//input[@id='combobox-input-inorout']")
			input_enter("xpath", "//input[@id='combobox-input-inorout']")
			# 输入银行账号
			input("xpath", '//*[@id="accountnumber"]', '20211039')
			sleep(1)
			input("xpath", '//*[@id="accountname"]', '快捷付款-直联批量付款账户')
			
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
			input("xpath", '//*[@id="accountnumber"]', '20211039')
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
			js_click("xpath", "//span[contains(text(),'账户资金监控')]")
			sleep(1)
			
			# 开始创建直联批量付款的交易类型以及结算方式💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
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
			input("xpath", "//input[@name='code']", "2039")
			sleep(1)
			
			# 输入结算方式
			input("xpath", "//input[@id='name']", "快捷付款直联批量付款")
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
			input("xpath", '//*[@id="combobox-input-editgrid-bankid-0"]', 'BOC-中国银行')
			click('xpath', '//*[@id="editgrid-bankid-0-combogrid-body-table"]/tbody/tr/td[2]/div')
			sleep(1)
			input('xpath', '//*[@id="combobox-input-editgrid-settlementscenarios-0"]', '代发代扣默认')
			click('xpath', '//*[@id="f-combo-editgrid-settlementscenarios-0-list-0"]')
			sleep(1)
			click('xpath', '//*[@id="combobox-input-editgrid-directchannelid-0"]')
			click('xpath', '//*[@id="editgrid-directchannelid-0-combogrid-body-table"]/tbody/tr[1]/td[2]/div')
			sleep(1)
			input('xpath', '//*[@id="combobox-input-editgrid-directchannelcmdid-0"]', '批量代付')
			click('xpath', '//*[@id="editgrid-directchannelcmdid-0-combogrid-body-table"]/tbody/tr[1]/td[2]/div')
			sleep(1)
			click('xpath', '//*[@id="combobox-input-editgrid-directinterbanksystemid-0"]')
			click('xpath', '//*[@id="editgrid-directinterbanksystemid-0-combogrid-body-table"]/tbody/tr[1]/td[2]/div')
			sleep(1)
			# 点击保存按钮
			click("xpath", "//span[text()='保存']")
			# 退出所有iframe窗体
			switch_default()
			sleep(3)
			# 创建直联批量付款的交易类型
			click("xpath", "//span[text()='交易类型']")
			switch_to('xpath', '//*[@id="payType-tab-iframe"]')
			js_click("xpath", "//span[text()='新增']")
			# 切入新增的iframe窗体
			switch_to("xpath", "//iframe[@id='addWin-iframe']")
			sleep(1)
			
			# 输入代码
			input("xpath", "//input[@id='code']", "3039")
			sleep(1)
			
			# 输入名称
			input("xpath", "//input[@id='name']", "快捷付款直联批量付款")
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
			input("xpath", "//input[@id='combobox-input-settlementmoderange']", '2039')
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
			sleep(1)
			switch_default()
			

			# 回到批量付款页面做数据💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			click("xpath", "//span[text()='资金系统收付']")
			sleep(1)
			# 点击付款处理菜单
			click("xpath", "//span[text()='付款处理']")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			for i in range(1, 3):
				global use1
				
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
				input("xpath", "//input[@id='combobox-input-paytypeid']", "3039-快捷付款直联批量付款")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-paytypeid']")
				input_enter("xpath", "//input[@id='combobox-input-paytypeid']")
				time.sleep(1)
				# 付方账户
				input("xpath", "//input[@id='combobox-input-ourbankaccountid']", '20211039')
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
				money =random.randint(100,1000)
				input("xpath", "//input[@id='ouramount-input']", money)
				sleep(1)
				# 用途
				if i == 1:
					use1 = "快捷付款直联批量付款处理数据导入" + str(random.randint(100, 1000))
					input("xpath", "//input[@id='combobox-input-purpose']", use1)
					sleep(1)
				if i == 2:
					input("xpath", "//input[@id='combobox-input-purpose']", '快捷付款直联批量付款处理数据导入')
					sleep(1)
				# 点击保存按钮
				click("xpath", "//span[text()='保存']")
				# 退出所有iframe窗体
				switch_default()
				# 用隐式等待方法等页面出现新增成功的提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				time.sleep(3)
				
			# 更改数据库单据来源
			sql = "update t_se_payments set RECORDSOURCE = '4' where purpose like '%快捷付款直联批量付款处理数据导入%'"
			my_sql(my_host, my_port, my_user, my_passwd, my_db,
			       sql)
				
			# 返回快捷付款-付款申请页面
			click("xpath", "//span[text()='资金系统收付']")
			sleep(1)
			click("xpath", "//span[text()='业务系统对接']")
			sleep(1)
			click("xpath", "//span[text()='快捷付款']")
			sleep(1)
	
			#测试变更功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			#切入快捷付款窗体
			switch_to("xpath",'//*[@id="externalPayments-tab-iframe"]')
			span_click("直联批量付款处理")
			sleep(1)
			switch_to("xpath",'//*[@id="subTabFor-iframe"]')
			
			#刷新、勾选按钮
			click("xpath",'//*[@id="gridbar-page-refresh"]')
			sleep(2)
			click("xpath",'//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("变更")
			sleep(1)
			#切入变更窗体
			switch_to("xpath",'//*[@id="settlementWin-iframe"]')
			#变更付方账户
			clear("xpath",'//*[@id="combobox-input-ourbankaccountid"]')
			sleep(1)
			input("xpath",'//*[@id="combobox-input-ourbankaccountid"]','20211039')
			sleep(1)
			up_enter_click('//*[@id="combobox-input-ourbankaccountid"]')
			span_click("保存")
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("直联批量付款处理，变更成功")
			time.sleep(3)
			
			# 测试送审、撤销送审功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入快捷付款窗体
			switch_to("xpath", '//*[@id="externalPayments-tab-iframe"]')
			span_click("直联批量付款处理")
			sleep(1)
			switch_to("xpath", '//*[@id="subTabFor-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(2)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("送审")
			sleep(1)
			ok_click()
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！送审成功1笔，失败0笔。')]")
			print("直联批量付款处理，送审成功")
			time.sleep(3)
			
			# 撤销送审功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入快捷付款窗体
			switch_to("xpath", '//*[@id="externalPayments-tab-iframe"]')
			span_click("直联批量付款处理")
			sleep(1)
			switch_to("xpath", '//*[@id="subTabFor-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(2)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("送审", '撤销送审')
			ok_click()
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'撤销送审成功！')]")
			print("直联批量付款处理，撤销送审成功")
			time.sleep(3)
			
			# 测试审核、撤销审核功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入快捷付款窗体
			switch_to("xpath", '//*[@id="externalPayments-tab-iframe"]')
			span_click("直联批量付款处理")
			sleep(1)
			switch_to("xpath", '//*[@id="subTabFor-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(2)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[2]/td[2]/div/button')
			sleep(1)
			
			span_click("审核")
			sleep(1)
			ok_click()
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！审核成功1笔，失败0笔。')]")
			print("批量付款处理，审核成功")
			time.sleep(3)
			
			# 测试撤销审核功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入快捷付款窗体
			switch_to("xpath", '//*[@id="externalPayments-tab-iframe"]')
			span_click("直联批量付款处理")
			sleep(1)
			switch_to("xpath", '//*[@id="subTabFor-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(2)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[2]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("审核", '取消审核')
			ok_click()
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'取消审核成功！')]")
			print("直联批量付款处理，审核成功")
			time.sleep(3)
			
			# 测试审批历史功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入快捷付款窗体
			switch_to("xpath", '//*[@id="externalPayments-tab-iframe"]')
			span_click("直联批量付款处理")
			sleep(1)
			switch_to("xpath", '//*[@id="subTabFor-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(2)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("送审")
			sleep(1)
			ok_click()
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！送审成功1笔，失败0笔。')]")
			time.sleep(3)
			
			# 二审💨💨💨
			# 切入快捷付款窗体
			switch_to("xpath", '//*[@id="externalPayments-tab-iframe"]')
			span_click("直联批量付款处理")
			sleep(1)
			switch_to("xpath", '//*[@id="subTabFor-iframe"]')
			
			double_click("xpath",'//*[@id="grid-body-table"]/tbody/tr[1]/td[3]/div')
			sleep(1)
			switch_to("xpath",'//*[@id="wf_taskProcessing_win-iframe"]')
			span_click("同意")
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			time.sleep(3)
			
			# 三审💨💨💨
			# 切入快捷付款窗体
			switch_to("xpath", '//*[@id="externalPayments-tab-iframe"]')
			span_click("直联批量付款处理")
			sleep(1)
			switch_to("xpath", '//*[@id="subTabFor-iframe"]')
			
			double_click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[3]/div')
			sleep(1)
			switch_to("xpath",'//*[@id="wf_taskProcessing_win-iframe"]')
			span_click("同意")
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			time.sleep(3)
			
			
			# 切入快捷付款窗体
			switch_to("xpath", '//*[@id="externalPayments-tab-iframe"]')
			span_click("直联批量付款处理")
			sleep(1)
			switch_to("xpath", '//*[@id="subTabFor-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(2)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("审批历史")
			switch_to("xpath",'//*[@id="flowwin-iframe"]')
			sleep(3)
			span_click("流程流转")
			implici_wait("xpath", "//div[contains(text(),'开始')]")
			print("批量付款处理，审批历史查看成功")
			sleep(3)
			switch_parent()
			# 点击叉号
			click("xpath", '//*[@id="f-win-title-flowwin"]/div[1]/div')
			sleep(1)
			switch_default()
			
			# 测试支付功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入快捷付款窗体
			switch_to("xpath", '//*[@id="externalPayments-tab-iframe"]')
			span_click("直联批量付款处理")
			sleep(1)
			switch_to("xpath", '//*[@id="subTabFor-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(2)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("支付")
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！1批进行了支付，0批不允许支付')]")
			print("批量付款处理，支付成功")
			time.sleep(3)
			
			# 测试查询支付状态功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入快捷付款窗体
			
			sql = "update t_se_payments set paystate = '7' where purpose = '" + str("快捷付款直联批量付款处理数据导入") + "'"
			my_sql(my_host, my_port, my_user, my_passwd, my_db,
			       sql)
			switch_to("xpath", '//*[@id="externalPayments-tab-iframe"]')
			span_click("直联批量付款处理")
			sleep(1)
			switch_to("xpath", '//*[@id="subTabFor-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(2)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("查询支付状态")
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'请查看相应结果!')]")
			print("批量付款处理，查询支付状态成功")
			time.sleep(3)
			
			# 测试打印功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入快捷付款窗体
			switch_to("xpath", '//*[@id="externalPayments-tab-iframe"]')
			span_click("直联批量付款处理")
			sleep(1)
			switch_to("xpath", '//*[@id="subTabFor-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(2)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)

			# 点击打印按钮
			span_click("打印")
			time.sleep(3)
			# 获取所有窗口句柄
			all_handles = self.driver.window_handles
			# 循环遍历所有新打开的窗口句柄，也就是说不包括主窗口
			now_handle = self.driver.current_window_handle
			for handle in all_handles:
				self.driver.switch_to.window(handle)
				if self.driver.title == u"payandrecbatchprint":
					implici_wait("xpath", "//td[contains(text(),'浙江华语科技')]")
					print("批量付款处理，打印成功!！")
					time.sleep(3)
					self.driver.switch_to.window(now_handle)
					switch_default()

			# 测试打印记录功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入快捷付款窗体
			switch_to("xpath", '//*[@id="externalPayments-tab-iframe"]')
			span_click("直联批量付款处理")
			sleep(1)
			switch_to("xpath", '//*[@id="subTabFor-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(2)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("打印", '打印记录')
			switch_to("xpath", '//*[@id="printWin-iframe"]')
			
			# 用隐式等待方法等页面出现  操作人:mindy
			implici_wait("xpath", "//div[@title='操作人:mindy']")
			print("批量付款处理，打印记录查看成功！")
			switch_parent()
			click("xpath", '//*[@id="f-win-title-printWin"]/div[1]/div')
			sleep(1)
			switch_default()
			sleep(3)
			
			# 测试确认已支付💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入快捷付款窗体
			sql = "update t_se_payments set paystate = '7' where purpose = '" + str("快捷付款直联批量付款处理数据导入") + "'"
			my_sql(my_host, my_port, my_user, my_passwd, my_db,
			       sql)
			switch_to("xpath", '//*[@id="externalPayments-tab-iframe"]')
			span_click("直联批量付款处理")
			sleep(1)
			switch_to("xpath", '//*[@id="subTabFor-iframe"]')
			
			double_click("xpath",'//*[@id="grid-body-table"]/tbody/tr[1]/td[3]/div')
			sleep(1)
			# 切入详情窗体
			switch_to('xpath', '//*[@id="flowwin-iframe"]')
			switch_to('xpath', '//*[@id="subTabOne-iframe"]')
			sleep(1)
			# 勾选数据
			click('xpath', '//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
			sleep(1)
			# 点击确认已支付
			span_click("确认已支付")
			sleep(1)
			# 点击ok
			click("xpath", '//*[@id="f-message-webgen-0-okBnt"]')
			sleep(1)
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'共1笔，处理成功1笔，失败0笔。')]")
			print("直联批量支付，测试确认已支付成功！")
			span_click("快捷付款")
			sleep(3)
			
			# 测试非直联💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入快捷付款窗体
			sql = "update t_se_payments set paystate = '3' where purpose = '" + str("快捷付款直联批量付款处理数据导入") + "'"
			my_sql(my_host, my_port, my_user, my_passwd, my_db,
			       sql)
			switch_to("xpath", '//*[@id="externalPayments-tab-iframe"]')
			span_click("直联批量付款处理")
			sleep(1)
			switch_to("xpath", '//*[@id="subTabFor-iframe"]')
			
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
			span_click("确认非直联已支付")
			sleep(1)
			# 点击ok
			click("xpath", '//*[@id="f-message-webgen-0-okBnt"]')
			sleep(1)
			# 切入新增窗体
			switch_to("xpath", '//*[@id="confirmUndirectPayWin-iframe"]')
			click("xpath", '//*[@id="combobox-input-actualsettlementmodeid"]')
			sleep(1)
			click("xpath", '//*[@id="actualsettlementmodeid-combogrid-body-table"]/tbody/tr/td[2]/div')
			sleep(1)
			# 点击确定
			click("xpath", '//*[@id="determineConfirmUndirectPay"]/span/span')
			sleep(1)
			click("xpath", '//*[@id="f-message-webgen-0-okBnt"]')
			sleep(1)
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'共1笔，处理成功1笔，失败0笔。')]")
			print("直联批量支付，确认非直联已支付成功！")
			span_click("快捷付款")
			sleep(3)
			
			# 测试支付日志查看💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入快捷付款窗体
			switch_to("xpath", '//*[@id="externalPayments-tab-iframe"]')
			span_click("直联批量付款处理")
			sleep(1)
			switch_to("xpath", '//*[@id="subTabFor-iframe"]')
			
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
			span_click("支付日志查看")
			sleep(1)
			print("直联批量支付，测试日志查看成功！")
			switch_default()
			span_click("快捷付款")
			sleep(3)
			
			# 测试修改💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入快捷付款窗体
			switch_to("xpath", '//*[@id="externalPayments-tab-iframe"]')
			span_click("直联批量付款处理")
			sleep(1)
			switch_to("xpath", '//*[@id="subTabFor-iframe"]')
			double_click("xpath", '//*[@id="grid-body-table"]/tbody/tr[2]/td[3]/div')
			sleep(1)
			# 切入新增窗体
			switch_to("xpath",'//*[@id="detailWin-iframe"]')
			sleep(2)
			# 勾选数据
			click('xpath', '//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
			sleep(1)
			# 点击修改
			span_click("修改")
			sleep(1)
			switch_to("xpath",'//*[@id="singleModWin-iframe"]')
			span_click("保存")
			print("直联批量支付，修改成功！")
			switch_default()
			span_click("快捷付款")
			sleep(3)
			
			
			
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("跨境外币汇款-其他支付失败！" + str(traceback.format_exc()))
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
