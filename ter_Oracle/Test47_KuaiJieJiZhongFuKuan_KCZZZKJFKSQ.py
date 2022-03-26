# encoding=utf-8
# @Time : 2020/11/17 08:30
# @Author : zzg
# 此文件是测试Oracle版本资金结算管理--业务系统对接--快捷集中收款--可操作组织快捷付款申请
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
class Test47_KuaiJieJiZhongFuKuan_KCZZZKJFKSQ(unittest.TestCase):
	
	# 启动浏览器
	def setUp(self):
		# 启动浏览器的另外一个方法：通过封装启动浏览器的驱动，启动不同浏览器
		self.driver = get("chrome")
	
	# 登陆系统、对系统设置进行操作
	def test_trade(self):
		
		# login(G_Ora_Url, mindy, Password, "亚唐科技")
		login(G_Ora_Url, mindy, Password, "亚唐科技")
		
		logging.info("开始测试资金结算管理--业务系统对接--快捷集中收款--可操作组织快捷付款申请")
		# 将页面的滚动条滑动到‘资金结算管理’页面的地方
		js_gd("xpath", "//span[contains(text(),'资金结算管理')]")
		# 用JS的方法点击资金结算管理菜单按钮
		js_click("xpath", "//span[contains(text(),'资金结算管理')]")
		sleep(1)
		# 点击'外币收付结算'菜单
		click("xpath", "//span[text()='业务系统对接']")
		sleep(1)
		# 点击收款处理菜单
		click("xpath", "//span[text()='快捷集中付款']")
		sleep(1)
		# 退出所有iframe窗体
		switch_default()
		try:
			'''
			# 创建可z'w操作组织快捷付款申请账户💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 收回窗体
			click("xpath", "//span[text()='业务系统对接']")
			sleep(1)
			js_click("xpath", "//span[contains(text(),'资金结算管理')]")
			sleep(1)

			# 将页面的滚动条滑动到‘账户资金监控’页面的地方
			js_gd("xpath", "//span[contains(text(),'账户资金监控')]")
			# 用JS的方法点击票据管理菜单按钮
			js_click("xpath", "//span[contains(text(),'账户资金监控')]")
			sleep(1)
			click("xpath", "//span[contains(text(),'账户生命周期')]")
			sleep(1)
			click("xpath", "//span[text()='账户维护']")
			sleep(1)
			# 切入单币种账户窗体
			switch_default()
			switch_to("xpath", '//*[@id="bankAccounts-tab-iframe"]')
			sleep(1)
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			#点击新增
			click("xpath", "//span[text()='新增']")
			sleep(1)
			switch_to("xpath", '//*[@id="addWin-iframe"]')

			#银行
			click("xpath", "//input[@id='combobox-input-bankid']")
			sleep(1)
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
			input("xpath", '//*[@id="accountnumber"]', '20211047')
			sleep(1)
			input("xpath", '//*[@id="accountname"]', '快捷集中付款-付款申请账户')

			# 点击保存按钮
			click("xpath", "//span[text()='保存']")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			sleep(3)

			# 对新增账户进行开户
			switch_to("xpath", '//*[@id="bankAccounts-tab-iframe"]')
			sleep(1)
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')

			# 点击查看
			js_click("xpath", "//span[@class='f-contrac-close']")
			sleep(1)
			# 输入账户
			input("xpath", '//*[@id="accountnumber"]', '20211047')
			sleep(1)
			# 点击查询
			click("xpath", "//span[text()='查询']")
			sleep(1)

			# 勾选数据,点击开户
			click("xpath",'//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
			sleep(1)
			triangle_cick_and_element("维护",'开户')

			#开户日期
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

			#日记账金额
			clear("xpath", '//*[@id="journalbalance-input"]')
			sleep(1)
			input("xpath", '//*[@id="journalbalance-input"]', "5000")
			sleep(1)
			click("xpath", "//span[text()='确定']")
			sleep(1)
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")

			#点击账户资金监控，收回窗体
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
			sleep(1)
			# 切入新增的iframe窗体
			switch_to("xpath", "//iframe[@id='addWin-iframe']")
			
			# 输入代码
			input("xpath", "//input[@name='code']", "2047")
			sleep(1)
			
			# 输入结算方式
			input("xpath", "//input[@id='name']", "快捷集中付款可操作组织快捷付款申请")
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
			# 直联银行
			input("xpath", '//*[@id="combobox-input-editgrid-bankid-0"]', 'BOC-中国银行')
			click('xpath', '//*[@id="editgrid-bankid-0-combogrid-body-table"]/tbody/tr/td[2]/div')
			sleep(1)
			
			# 结算场景
			input('xpath', '//*[@id="combobox-input-editgrid-settlementscenarios-0"]', '代发代扣默认')
			click('xpath', '//*[@id="f-combo-editgrid-settlementscenarios-0-list-0"]')
			sleep(1)
			
			# 直联渠道
			click('xpath', '//*[@id="combobox-input-editgrid-directchannelid-0"]')
			sleep(1)
			click('xpath', '//*[@id="editgrid-directchannelid-0-combogrid-body-table"]/tbody/tr[1]/td[2]/div')
			sleep(1)
			
			# 直联渠道指令
			input('xpath', '//*[@id="combobox-input-editgrid-directchannelcmdid-0"]', '批量代付')
			sleep(1)
			click('xpath', '//*[@id="editgrid-directchannelcmdid-0-combogrid-body-table"]/tbody/tr[1]/td[2]/div')
			sleep(1)
			
			# 跨行支付系统
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
			sleep(1)
			switch_to('xpath', '//*[@id="payType-tab-iframe"]')
			js_click("xpath", "//span[text()='新增']")
			# 切入新增的iframe窗体
			switch_to("xpath", "//iframe[@id='addWin-iframe']")
			sleep(1)
			
			# 输入代码
			input("xpath", "//input[@id='code']", "3047")
			sleep(1)
			
			# 输入名称
			input("xpath", "//input[@id='name']", "快捷集中付款可操作组织快捷付款申请")
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
			input("xpath", "//input[@id='combobox-input-settlementmoderange']", '2047')
			sleep(1)
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
			
			# 点击基础设置收回窗体
			click("xpath",
			      '/html/body/div[1]/div[1]/div/div[2]/div/div[2]/div/div/div/div[4]/div/div/ul/li[1]/a/span[2]')
			sleep(1)
			js_click("xpath", "//span[contains(text(),'资金结算管理')]")
			sleep(1)
			'''

			# 回到直联单笔付款界面做数据💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			js_gd("xpath", "//span[contains(text(),'资金结算管理')]")
			# 用JS的方法点击资金结算管理菜单按钮
			js_click("xpath", "//span[contains(text(),'资金结算管理')]")
			sleep(1)
			click("xpath", "//span[text()='资金系统收付']")
			sleep(1)
			click("xpath", "//span[text()='付款处理']")
			# 退出所有iframe窗体
			switch_default()
			
			for i in range(1, 8):
				switch_to("xpath", '//*[@id="generalPayment-tab-iframe"]')
				switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
				sleep(1)
				# 切入新增窗体
				span_click("新增")
				sleep(1)
				switch_to('xpath', '//*[@id="addWin-iframe"]')

				# 交易类型
				input("xpath", '//*[@id="combobox-input-paytypeid"]', "103-对外付款")
				sleep(1)
				click("xpath", '//*[@id="paytypeid-combogrid-body-table"]/tbody/tr/td[2]/div')
				sleep(1)

				# 结算方式
				clear("xpath", '//*[@id="combobox-input-settlementmodeid"]')
				sleep(1)
				input("xpath", '//*[@id="combobox-input-settlementmodeid"]', "101-直联单笔转账")
				sleep(1)
				up_enter_click('//*[@id="combobox-input-settlementmodeid"]')
				sleep(1)

				# 点击付方账户
				input("xpath", '//*[@id="combobox-input-ourbankaccountid"]', "20211047")
				sleep(1)
				click("xpath", '//*[@id="ourbankaccountid-combogrid-body-table"]/tbody/tr/td[2]/div')
				sleep(1)

				# 输入收方名称
				input("xpath", '//*[@id="combobox-input-oppcounterpartyid"]', "浙江华语科技")
				sleep(1)
				click("xpath", '//*[@id="oppprivateflag"]')
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
				input("xpath", "//input[@id='combobox-input-oppbanklocationid']",'中国银行股份有限公司南宁市江南支行')
				sleep(1)
				click("xpath",'//*[@id="oppbanklocationid-combogrid-body-table"]/tbody/tr/td[2]/div')
				sleep(1)

				# 金额
				if i == 4:
					input("xpath", "//input[@id='ouramount-input']", "300")
					sleep(1)
				else:
					money = random.randint(100, 1000)
					input("xpath", "//input[@id='ouramount-input']", money)
					sleep(1)
				# 用途
				input("xpath", "//input[@id='combobox-input-purpose']", "快捷集中付款可操作组织快捷付款申请数据导入")
				sleep(1)
				# 双击清楚下拉框
				double_click("xpath", "//span[text()='卡折类型']")
				sleep(1)

				#保存
				click("xpath", '//*[@id="save"]/span/span')
				sleep(1)
				switch_default()
				time.sleep(3)
			# 更改数据库单据来源
			sql = "update t_se_payments set RECORDSOURCE = '4' where purpose = '快捷集中付款可操作组织快捷付款申请数据导入'"
			ora_sql(ora_ip, ora_sid, ora_user, ora_pwd,
			       sql)

			# 返回快捷付款-付款申请页面
			click("xpath", "//span[text()='资金系统收付']")
			sleep(1)
			click("xpath", "//span[text()='业务系统对接']")
			sleep(1)
			click("xpath", "//span[text()='快捷集中付款']")
			sleep(1)
			
			# 测试修改功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入可操作组织快捷付款申请窗体
			switch_to("xpath", '//*[@id="externalMassPayments-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			# 刷新、勾选数据
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)

			span_click("修改")
			switch_to("xpath",'//*[@id="singleModWin-iframe"]')
			#点击查询余额
			click("xpath",'//*[@id="checkBalance"]')
			sleep(1)
			span_click("保存")

			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("快捷集中付款，修改成功")
			time.sleep(3)

			# 测试批量变更功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入可操作组织快捷付款申请窗体
			switch_to("xpath", '//*[@id="externalMassPayments-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			# 刷新、勾选数据
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)

			triangle_cick_and_element("修改",'批量变更')
			switch_to("xpath",'//*[@id="batchModWin_General-iframe"]')
			#付方账户
			input("xpath",'//*[@id="combobox-input-ourbankaccountid"]',"20211047")
			sleep(1)
			up_enter_click('//*[@id="combobox-input-ourbankaccountid"]')
			span_click("保存")

			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("快捷集中付款，批量变更成功")
			time.sleep(3)

			# 测试作废功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入可操作组织快捷付款申请窗体
			switch_to("xpath", '//*[@id="externalMassPayments-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			# 刷新、勾选数据
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t6-fixed"]/td[2]/div/button')
			sleep(1)

			span_click("作废")
			ok_click()
			input("xpath", '//*[@id="combobox-input-cancelReason"]', '测试作废')
			sleep(1)
			js_click("xpath", "//span[text()='确定']")
			sleep(1)

			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("快捷集中付款，作废成功")
			time.sleep(3)
			
			# 测试终止功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入可操作组织快捷付款申请窗体
			switch_to("xpath", '//*[@id="externalMassPayments-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			# 刷新、勾选数据
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t5-fixed"]/td[2]/div/button')
			sleep(1)

			span_click("终止")
			ok_click()
			input("xpath", '//*[@id="terminateReason"]', '测试终止')
			sleep(1)
			span_click("确定")

			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("快捷集中付款，终止成功")
			time.sleep(3)

			# 测试送审、撤销送审功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入可操作组织快捷付款申请窗体
			switch_to("xpath", '//*[@id="externalMassPayments-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			# 刷新、勾选数据
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)

			span_click("送审")
			ok_click()
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！送审成功1笔，失败0笔。')]")
			print("快捷集中付款，送审成功")
			time.sleep(3)

			# 撤销送审功能💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入可操作组织快捷付款申请窗体
			switch_to("xpath", '//*[@id="externalMassPayments-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			# 刷新、勾选数据
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)

			triangle_cick_and_element("送审",'撤销送审')
			ok_click()
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'撤销送审成功！')]")
			print("快捷集中付款，撤销送审成功")
			time.sleep(3)

			# 审核、撤销审核功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入可操作组织快捷付款申请窗体
			switch_to("xpath", '//*[@id="externalMassPayments-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			# 刷新、勾选数据
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t1-fixed"]/td[2]/div/button')
			sleep(1)

			span_click("审核")
			ok_click()
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！审核成功1笔，失败0笔。')]")
			print("快捷集中付款，审核成功")
			time.sleep(3)
			
			# 撤销审核功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入可操作组织快捷付款申请窗体
			switch_to("xpath", '//*[@id="externalMassPayments-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			# 刷新、勾选数据
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t1-fixed"]/td[2]/div/button')
			sleep(1)

			triangle_cick_and_element("审核",'取消审核')
			ok_click()
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'取消审核成功！')]")
			print("快捷集中付款，取消审核成功")
			time.sleep(3)

			# 测试余额检测功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入快捷付款-付款申请窗体
			switch_to("xpath", '//*[@id="externalMassPayments-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			# 刷新、勾选数据
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)

			span_click("余额检测")
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'余额充足')]")
			print("快捷集中付款，余额检测成功")
			time.sleep(3)
			
			# 测试审批历史💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入快捷付款-付款申请窗体
			switch_to("xpath", '//*[@id="externalMassPayments-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			# 刷新、勾选数据
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("送审")
			ok_click()
			sleep(3)
			
			double_click("xpath", '//*[@id="t1_t0"]/td[1]')
			sleep(2)
			switch_to("xpath", '//*[@id="wf_taskProcessing_win-iframe"]')
			span_click("同意")
			switch_parent()
			sleep(3)
			
			double_click("xpath", '//*[@id="t1_t0"]/td[1]')
			sleep(2)
			switch_to("xpath", '//*[@id="wf_taskProcessing_win-iframe"]')
			span_click("提交")
			switch_parent()
			sleep(3)
			
			double_click("xpath", '//*[@id="t1_t0"]/td[1]')
			sleep(2)
			switch_to("xpath", '//*[@id="wf_taskProcessing_win-iframe"]')
			span_click("同意")
			switch_parent()
			sleep(3)
			
			# 刷新、勾选数据
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			span_click("审批历史")
			
			#切入审批历史窗体
			switch_to("xpath",'//*[@id="flowwin-iframe"]')
			sleep(2)
			span_click("流程流转")
			implici_wait("xpath", "//div[contains(text(),'开始')]")
			print("快捷集中付款，审批历史查看成功")
			sleep(3)
			switch_parent()
			click("xpath",'//*[@id="f-win-title-flowwin"]/div[1]/div')
			sleep(1)
			switch_default()
			
			# 测试拆分功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入可操作组织快捷付款申请窗体
			switch_to("xpath", '//*[@id="externalMassPayments-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			# 刷新、勾选数据
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t1-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("拆分")
			ok_click()
			switch_to("xpath",'//*[@id="splitWin-iframe"]')
			
			#付方账户
			input("xpath",'//*[@id="combobox-input-ourbankaccountid"]','20211047')
			sleep(1)
			up_enter_click('//*[@id="combobox-input-ourbankaccountid"]')
			
			#拆分金额
			double_click("xpath",'//*[@id="splitingamount-input"]')
			sleep(1)
			input("xpath",'//*[@id="splitingamount-input"]','10')
			sleep(1)
			span_click("保存")
			
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功')]")
			print("快捷集中付款，拆分成功")
			time.sleep(3)
			
			# 测试批量拆分功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入可操作组织快捷付款申请窗体
			switch_to("xpath", '//*[@id="externalMassPayments-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			# 刷新、勾选数据
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t3-fixed"]/td[2]/div')
			sleep(1)
			
			triangle_cick_and_element("拆分",'批量拆分')
			ok_click()
			switch_to("xpath",'//*[@id="batchSplitWin-iframe"]')
			
			# 业务
			clear("xpath", '//*[@id="combobox-input-businessid"]')
			sleep(1)
			input("xpath", '//*[@id="combobox-input-businessid"]', '快捷集中付款批量拆分导入')
			sleep(1)
			click("xpath", '//*[@id="businessid-combogrid-body-table"]/tbody/tr/td[2]/div')
			sleep(1)
			span_click("下一步")
			
			switch_to("xpath", '//*[@id="loadNextWin-iframe"]')
			sleep(1)
			# 附件上传
			upload_click("xpath", "//div[text()='上传文件']/parent::*[1]/descendant::*[4]",
			             'D:\FlieDownload', '"KuaiJieJiZhongFuKuanKCZZZKHFKSQ.xls"')
			sleep(3)
			# 点击保存按钮
			click("xpath", "//span[text()='上传']")
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功,共导入3条数据，成功3条，失败0条，未处理0条。')]")
			print("可操作组织快捷付款申请，批量拆分成功！")
			# 返回页面
			span_click("快捷集中付款")
			sleep(1)
			
			# 测试批量拆分日志功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入可操作组织快捷付款申请窗体
			switch_to("xpath", '//*[@id="externalMassPayments-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			# 刷新、勾选数据
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t3-fixed"]/td[2]/div')
			sleep(1)
			
			triangle_cick_and_element("拆分", '批量拆分日志')
			switch_to("xpath",'//*[@id="batchSplitImportLogsWin-iframe"]')
			implici_wait("xpath", "//div[contains(text(),'文件导入')]")
			sleep(1)
			print("可操作组织快捷付款申请，批量拆分日志查看成功！")
			switch_parent()
			click("xpath",'//*[@id="f-win-title-batchSplitImportLogsWin"]/div[1]/div')
			sleep(1)
			switch_default()
			
			# 测试合并功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入可操作组织快捷付款申请窗体
			switch_to("xpath", '//*[@id="externalMassPayments-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			# 刷新、勾选数据
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t2-fixed"]/td[2]/div/button')
			sleep(1)
			click("xpath", '//*[@id="t1_t4-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("合并")
			ok_click()
			
			#切入合并窗体
			switch_to("xpath",'//*[@id="mergeWin-iframe"]')
			#付方账户
			input("xpath",'//*[@id="combobox-input-ourbankaccountid"]','20211047')
			sleep(1)
			up_enter_click('//*[@id="combobox-input-ourbankaccountid"]')
			span_click('保存')
			
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("快捷集中付款，合并成功")
			time.sleep(3)
			
			# 测试组批功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 点击业务系统对接收回菜单
			click("xpath", "//span[text()='业务系统对接']")
			sleep(1)
			click("xpath", "//span[text()='资金系统收付']")
			sleep(1)
			click("xpath", "//span[text()='付款处理']")
			sleep(1)
			for i in range(1, 3):
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
				sleep(3)
				input("xpath", "//input[@id='combobox-input-paytypeid']", "3047-快捷集中付款可操作组织快捷付款申请")
				sleep(3)
				up_enter_click("//input[@id='combobox-input-paytypeid']")
				
				# 付方账户
				input("xpath", "//input[@id='combobox-input-ourbankaccountid']", '20211047')
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
				input("xpath","//input[@id='combobox-input-oppbanklocationid']",'104611010734-中国银行股份有限公司南宁市江南支行')
				sleep(1)
				up_enter_click("//input[@id='combobox-input-oppbanklocationid']")
				# 金额
				input("xpath", "//input[@id='ouramount-input']", "100")
				sleep(1)
				# 用途
				input("xpath", "//input[@id='combobox-input-purpose']", "可操作组织快捷付款申请组批数据来源")
				sleep(1)
				# 点击保存按钮
				click("xpath", "//span[text()='保存']")
				# 退出所有iframe窗体
				switch_default()
				# 用隐式等待方法等页面出现新增成功的提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				time.sleep(3)
			#修改sql
			sql2 = "update t_se_payments set RECORDSOURCE = '4' where purpose = '可操作组织快捷付款申请组批数据来源'"
			ora_sql(ora_ip, ora_sid, ora_user, ora_pwd,
			       sql2)
			sql3 = "update t_se_payments set PASSELNO = '' where purpose = '可操作组织快捷付款申请组批数据来源'"
			ora_sql(ora_ip, ora_sid, ora_user, ora_pwd,
			       sql3)
			#返回快捷付款-批量付款页面
			click("xpath", "//span[text()='资金系统收付']")
			sleep(1)
			click("xpath", "//span[text()='业务系统对接']")
			sleep(1)
			click("xpath", "//span[text()='快捷集中付款']")
			sleep(1)
			
			# 切入可操作组织快捷付款申请窗体
			switch_to("xpath", '//*[@id="externalMassPayments-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			# 刷新、勾选数据
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			click("xpath", '//*[@id="t1_t1-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("审核")
			sleep(1)
			ok_click()
			sleep(3)
			
			# 刷新、勾选数据
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			click("xpath", '//*[@id="t1_t1-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("组批")
			ok_click()
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功')]")
			print("可操作组织快捷付款申请，组批成功")
			time.sleep(3)
		
		
		
		
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
