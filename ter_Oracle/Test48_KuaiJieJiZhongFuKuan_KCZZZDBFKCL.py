# encoding=utf-8
# @Time : 2020/11/17 13:30
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
class Test48_KuaiJieJiZhongFuKuan_KCZZZDBFKCL(unittest.TestCase):
	
	# 启动浏览器
	def setUp(self):
		# 启动浏览器的另外一个方法：通过封装启动浏览器的驱动，启动不同浏览器
		self.driver = get("chrome")
	
	# 登陆系统、对系统设置进行操作
	def test_trade(self):
		
		# login(G_Ora_Url, mindy, Password, "亚唐科技")
		login(G_Ora_Url, mindy, Password, "亚唐科技")
		
		logging.info("开始测试资金结算管理--业务系统对接--快捷集中收款--可操作组织单笔付款处理")
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
			# 创建可操作组织单笔付款处理账户💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
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
			# 点击新增
			click("xpath", "//span[text()='新增']")
			sleep(1)
			switch_to("xpath", '//*[@id="addWin-iframe"]')
			
			# 银行
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
			input("xpath", '//*[@id="accountnumber"]', '20211048')
			sleep(1)
			input("xpath", '//*[@id="accountname"]', '快捷集中付款-可操作组织单笔付款处理账户')
			sleep(1)
			
			# 点击保存按钮
			click("xpath", "//span[text()='保存']")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			sleep(3)
			
			# 对新增账户进行开户
			switch_to("xpath", '//*[@id="bankAccounts-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			# 点击查看
			js_click("xpath", "//span[@class='f-contrac-close']")
			sleep(1)
			# 输入账户
			input("xpath", '//*[@id="accountnumber"]', '20211048')
			sleep(1)
			# 点击查询
			click("xpath", "//span[text()='查询']")
			sleep(1)
			
			# 勾选数据,点击开户
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
			click("xpath", '//*[@id="journalbalance-input"]')
			sleep(1)
			
			# 日记账金额
			clear("xpath", '//*[@id="journalbalance-input"]')
			sleep(1)
			input("xpath", '//*[@id="journalbalance-input"]', "50000")
			sleep(1)
			click("xpath", "//span[text()='确定']")
			sleep(1)
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			
			# 点击账户资金监控，收回窗体
			js_click("xpath", "//span[contains(text(),'账户资金监控')]")
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
			for i in range(1, 4):
				global use3
				switch_to("xpath", '//*[@id="generalPayment-tab-iframe"]')
				switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
				sleep(1)
				# 切入新增窗体
				span_click("新增")
				sleep(1)
				switch_to('xpath', '//*[@id="addWin-iframe"]')
				# 点击对外付款
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
				input("xpath", '//*[@id="combobox-input-ourbankaccountid"]', "20211048")
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
				click("xpath", "//input[@id='combobox-input-oppbanklocationid']")
				sleep(1)
				input_enter("xpath", "//input[@id='combobox-input-oppbanklocationid']")
				input_down("xpath", "//input[@id='combobox-input-oppbanklocationid']")
				sleep(1)
				input_enter("xpath", "//input[@id='combobox-input-oppbanklocationid']")
				time.sleep(1)
				
				# 金额
				money = random.randint(100, 1000)
				input("xpath", "//input[@id='ouramount-input']", money)
				sleep(1)
				
				# 用途
				if i == 1:
					use1 = "快捷集中可操作组织单笔付款处理数据导入" + str(random.randint(100, 1000))
					input("xpath", "//input[@id='combobox-input-purpose']", use1)
					sleep(1)
				if i == 2:
					use2 = "快捷集中可操作组织单笔付款处理数据导入" + str(random.randint(100, 1000))
					input("xpath", "//input[@id='combobox-input-purpose']", use2)
					sleep(1)
				if i == 3:
					
					input("xpath", "//input[@id='combobox-input-purpose']", "快捷集中可操作组织单笔付款处理数据导入1")
					sleep(1)
				# 双击清楚下拉框
				double_click("xpath", "//span[text()='卡折类型']")
				sleep(1)
				click("xpath", '//*[@id="save"]/span/span')
				switch_default()
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				
				time.sleep(3)
			# 更改数据库单据来源
			sql = "update t_se_payments set RECORDSOURCE = '4' where purpose like '%快捷集中可操作组织单笔付款处理数据导入%'"
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
			# 切入可操作组织单笔付款处理窗体
			switch_to("xpath",'//*[@id="externalMassPayments-tab-iframe"]')
			span_click("可操作组织快捷单笔付款处理")
			switch_to("xpath",'//*[@id="subTabTwo-iframe"]')
			sleep(1)
			#刷新、勾选按钮
			click("xpath",'//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath",'//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("修改")
			switch_to("xpath",'//*[@id="singleModWin-iframe"]')
			click("xpath",'//*[@id="checkBalance"]')
			sleep(1)
			span_click("保存")
			
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("可操作组织单笔付款处理，修改成功")
			time.sleep(3)
			
			# 测试送审、撤销送审💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入可操作组织单笔付款处理窗体
			switch_to("xpath", '//*[@id="externalMassPayments-tab-iframe"]')
			span_click("可操作组织快捷单笔付款处理")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			
			span_click("送审")
			ok_click()
			
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！送审成功1笔，失败0笔。')]")
			print("可操作组织单笔付款处理，送审成功")
			time.sleep(3)
			
			# 测试撤销送审💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入可操作组织单笔付款处理窗体
			switch_to("xpath", '//*[@id="externalMassPayments-tab-iframe"]')
			span_click("可操作组织快捷单笔付款处理")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			
			triangle_cick_and_element("送审",'撤销送审')
			ok_click()
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'撤销送审成功！')]")
			print("可操作组织单笔付款处理，撤销送审成功")
			time.sleep(3)
			
			# 测试审核、撤销审核💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入可操作组织单笔付款处理窗体
			switch_to("xpath", '//*[@id="externalMassPayments-tab-iframe"]')
			span_click("可操作组织快捷单笔付款处理")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t1-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("审核")
			ok_click()
			
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！审核成功1笔，失败0笔。')]")
			print("可操作组织单笔付款处理，审核成功")
			time.sleep(3)
			
			# 撤销审核💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入可操作组织单笔付款处理窗体
			switch_to("xpath", '//*[@id="externalMassPayments-tab-iframe"]')
			span_click("可操作组织快捷单笔付款处理")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t1-fixed"]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("审核",'取消审核')
			ok_click()
			
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'取消审核成功！')]")
			print("可操作组织单笔付款处理，取消审核成功")
			time.sleep(3)
			
			# 测试余额检测💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入可操作组织单笔付款处理窗体
			switch_to("xpath", '//*[@id="externalMassPayments-tab-iframe"]')
			span_click("可操作组织快捷单笔付款处理")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("余额检测")
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'余额充足')]")
			print("可操作组织单笔付款处理，余额检测成功")
			time.sleep(3)
			
			# 测试作废💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入可操作组织单笔付款处理窗体
			switch_to("xpath", '//*[@id="externalMassPayments-tab-iframe"]')
			span_click("可操作组织快捷单笔付款处理")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t2-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("终止")
			ok_click()
			input("xpath", '//*[@id="terminateReason"]', '测试终止')
			sleep(1)
			span_click("确定")
			sleep(1)
			
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功')]")
			print("可操作组织单笔付款处理，终止成功")
			time.sleep(3)
			
			# 测试审批历史💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入可操作组织单笔付款处理窗体
			switch_to("xpath", '//*[@id="externalMassPayments-tab-iframe"]')
			span_click("可操作组织快捷单笔付款处理")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("送审")
			ok_click()
			sleep(3)
			
			double_click("xpath",'//*[@id="t1_t0"]/td[1]')
			sleep(2)
			switch_to("xpath",'//*[@id="wf_taskProcessing_win-iframe"]')
			span_click("同意")
			switch_parent()
			sleep(3)
			
			double_click("xpath", '//*[@id="t1_t0"]/td[1]')
			sleep(2)
			switch_to("xpath",'//*[@id="wf_taskProcessing_win-iframe"]')
			span_click("提交")
			switch_parent()
			sleep(3)
			
			double_click("xpath", '//*[@id="t1_t0"]/td[1]')
			sleep(2)
			switch_to("xpath", '//*[@id="wf_taskProcessing_win-iframe"]')
			span_click("同意")
			switch_parent()
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("审批历史")
			switch_to("xpath",'//*[@id="flowwin-iframe"]')
			sleep(2)
			span_click("流程流转")
			implici_wait("xpath", "//div[contains(text(),'开始')]")
			print("可操作组织单笔付款处理，审批历史查看成功")
			#点击×号
			switch_parent()
			click("xpath",'//*[@id="f-win-title-flowwin"]/div[1]/div')
			sleep(1)
			switch_default()
			
			# 测试支付💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入可操作组织单笔付款处理窗体
			switch_to("xpath", '//*[@id="externalMassPayments-tab-iframe"]')
			span_click("可操作组织快捷单笔付款处理")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("支付")
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！1笔进行了支付，0笔不允许支付。')]")
			print("可操作组织单笔付款处理，支付成功")
			time.sleep(3)
			
			# 测试查询支付状态💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入可操作组织单笔付款处理窗体
			switch_to("xpath", '//*[@id="externalMassPayments-tab-iframe"]')
			span_click("可操作组织快捷单笔付款处理")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("查询支付状态")
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'请查看相应结果')]")
			print("可操作组织单笔付款处理，查询支付状态成功")
			time.sleep(3)
			
			# 测试打印💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入可操作组织单笔付款处理窗体
			switch_to("xpath", '//*[@id="externalMassPayments-tab-iframe"]')
			span_click("可操作组织快捷单笔付款处理")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
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
				if self.driver.title == u"payandrecsingleprint":
					implici_wait("xpath", "//td[contains(text(),'浙江华语科技')]")
					print("可操作组织快捷付款申请，打印成功!！")
					time.sleep(3)
					self.driver.switch_to.window(now_handle)
					switch_default()
			
			# 测试打印记录💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入可操作组织单笔付款处理窗体
			switch_to("xpath", '//*[@id="externalMassPayments-tab-iframe"]')
			span_click("可操作组织快捷单笔付款处理")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("打印", '打印记录')
			switch_to("xpath", '//*[@id="printWin-iframe"]')
			
			# 用隐式等待方法等页面出现  操作人:mindy
			implici_wait("xpath", "//div[@title='操作人:mindy']")
			print("可操作组织快捷付款申请，打印记录查看成功！")
			switch_parent()
			click("xpath", '//*[@id="f-win-title-printWin"]/div[1]/div')
			sleep(1)
			switch_default()
			sleep(3)
			
			# 测试支付日志查看💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入可操作组织单笔付款处理窗体
			switch_to("xpath", '//*[@id="externalMassPayments-tab-iframe"]')
			span_click("可操作组织快捷单笔付款处理")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("支付日志查看")
			switch_to("xpath", '//*[@id="logsWin-iframe"]')
			implici_wait("xpath", "//div[contains(text(),'已收付')]")
			print("可操作组织快捷单笔付款处理，支付日志查看成功！")
			#点击×号
			switch_parent()
			click("xpath", '//*[@id="f-win-title-logsWin"]/div[1]/div')
			sleep(1)
			switch_default()
			sleep(3)
			
			# 测试不合规💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入可操作组织单笔付款处理窗体
			switch_to("xpath", '//*[@id="externalMassPayments-tab-iframe"]')
			span_click("可操作组织快捷单笔付款处理")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("不合规")
			input("xpath", '//*[@id="nocomplianceReason"]', '测试不合规')
			sleep(1)
			span_click("确定")
			sleep(1)
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("可操作组织快捷单笔付款处理，不合规成功")
			time.sleep(3)
			
			# 测试合规💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入可操作组织单笔付款处理窗体
			switch_to("xpath", '//*[@id="externalMassPayments-tab-iframe"]')
			span_click("可操作组织快捷单笔付款处理")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("合规")
			ok_click()
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("可操作组织快捷单笔付款处理，合规成功")
			time.sleep(3)
			
			# 测试确认已支付💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			
			sql2 = "update t_se_payments set paystate = '7' where purpose = '" + str("快捷集中可操作组织单笔付款处理数据导入1") + "'"
			ora_sql(ora_ip, ora_sid, ora_user, ora_pwd,
			        sql2)
			
			# 切入可操作组织单笔付款处理窗体
			switch_to("xpath", '//*[@id="externalMassPayments-tab-iframe"]')
			span_click("可操作组织快捷单笔付款处理")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("确认已支付")
			ok_click()
			
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'共1笔，处理成功1笔，失败0笔。')]")
			print("可操作组织快捷单笔付款处理，确认已支付成功")
			time.sleep(3)
			
			# 测试确认非直联已收付💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			sql2 = "update t_se_payments set paystate = '3' where purpose = '" + str("快捷集中可操作组织单笔付款处理数据导入1") + "'"
			ora_sql(ora_ip, ora_sid, ora_user, ora_pwd,
			        sql2)
			
			# 切入可操作组织单笔付款处理窗体
			switch_to("xpath", '//*[@id="externalMassPayments-tab-iframe"]')
			span_click("可操作组织快捷单笔付款处理")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("确认已支付", '确认非直联已支付')
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
			print("可操作组织快捷单笔付款处理， 确认非直联已支付成功！")
			time.sleep(3)
			
			# 测试冲正💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入可操作组织单笔付款处理窗体
			switch_to("xpath", '//*[@id="externalMassPayments-tab-iframe"]')
			span_click("可操作组织快捷单笔付款处理")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			
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
			we = str(today) + " " + "08:30:00"
			input("xpath", '//*[@id="reversedate-input"]', we)
			sleep(1)
			
			
			# 冲正原因
			click("xpath", '//*[@id="reversalreason"]')
			sleep(1)
			input("xpath", '//*[@id="reversalreason"]', '测试冲正')
			sleep(1)
			span_click("确认冲正")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("可操作组织快捷单笔付款处理，冲正成功！")
			time.sleep(3)
			
			# 测试支票领用💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 去支票支付那做数据
			span_click("业务系统对接")
			span_click("资金系统收付")
			span_click("付款处理")
			
			switch_to("xpath", "//iframe[@id='generalPayment-tab-iframe']")
			# 点击支票支付
			click("xpath", "//span[text()='支票支付']")
			sleep(1)
			# 切入支票支付窗体
			switch_to("xpath", "//iframe[@id='subTabFive-iframe']")
			
			# 点击新增
			click("xpath", "//span[text()='新增']")
			sleep(1)
			# 切入新增的iframe窗体
			switch_to("xpath", "//iframe[@id='addWin-iframe']")
			
			# 输入交易类型
			input("xpath", "//input[@id='combobox-input-paytypeid']", "103-对外付款")
			sleep(1)
			input_down("xpath", "//input[@id='combobox-input-paytypeid']")
			input_enter("xpath", "//input[@id='combobox-input-paytypeid']")
			time.sleep(1)
			
			# 选择结算方式
			clear("xpath", "//input[@id='combobox-input-settlementmodeid']")
			sleep(1)
			input("xpath", "//input[@id='combobox-input-settlementmodeid']", "403-现金/转账支票支付")
			sleep(1)
			input_down("xpath", "//input[@id='combobox-input-settlementmodeid']")
			input_enter("xpath", "//input[@id='combobox-input-settlementmodeid']")
			time.sleep(1)
			
			# 付方账户
			click("xpath", "//input[@id='combobox-input-ourbankaccountid']")
			sleep(1)
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
			input_down("xpath", "//input[@id='combobox-input-oppbanklocationid']")
			sleep(1)
			input_enter("xpath", "//input[@id='combobox-input-oppbanklocationid']")
			time.sleep(1)
			
			# 金额
			money = random.randint(100, 1000)
			input("xpath", "//input[@id='ouramount-input']", money)
			sleep(1)
			
			# 用途
			input("xpath", "//input[@id='combobox-input-purpose']", "可操作组织单笔付款处理支票领用数据导入")
			sleep(1)
			
			# 点击保存按钮
			click("xpath", "//span[text()='保存']")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			sql4 = "update t_se_payments set RECORDSOURCE = '4' where purpose = '可操作组织单笔付款处理支票领用数据导入'"
			ora_sql(ora_ip, ora_sid, ora_user, ora_pwd,
			        sql4)
			
			# 点击资金系统收付缩回窗口
			click("xpath", "//span[text()='资金系统收付']")
			sleep(1)
			js_click("xpath", "//span[contains(text(),'资金结算管理')]")
			sleep(1)
			js_gd("xpath", "//span[contains(text(),'票据管理')]")
			# 用JS的方法点击票据管理菜单按钮
			js_click("xpath", "//span[contains(text(),'票据管理')]")
			sleep(1)
			
			# 点击支票管理菜单
			click("xpath", "//span[@title='支票管理']")
			sleep(1)
			# 点击应付支票登记菜单
			click("xpath", "//span[@title='应付支票登记']")
			sleep(1)
			# 退出所有的iframe窗体
			switch_default()
			
			# 切入应付支票登记iframe窗体
			switch_to("xpath", "//iframe[@id='chequeStorage-tab-iframe']")
			# 用JS的方法点击新增按钮
			js_click("xpath", "//span[text()='新增']")
			sleep(1)
			# 切入新增的iframe窗体
			switch_to("xpath", "//iframe[@id='addWin-iframe']")
			sleep(1)
			
			#支票类型
			input("xpath", "//input[@id='combobox-input-booktype']", "现金/转账")
			sleep(1)
			click("xpath",'//*[@id="f-combo-booktype-list-0"]')
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
			
			# 切回可操作组织单笔付款处理
			# 将页面的滚动条滑动到‘资金结算管理’页面的地方
			js_gd("xpath", "//span[contains(text(),'资金结算管理')]")
			# 用JS的方法点击资金结算管理菜单按钮
			js_click("xpath", "//span[contains(text(),'资金结算管理')]")
			sleep(1)
			span_click("业务系统对接")
			sleep(1)
			span_click("快捷集中付款")
			sleep(1)
			
			# 切入可操作组织单笔付款处理窗体
			switch_to("xpath", '//*[@id="externalMassPayments-tab-iframe"]')
			span_click("可操作组织快捷单笔付款处理")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			sleep(3)
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
			
			span_click("支票领用")
			
			switch_to("xpath", '//*[@id="chequerecipientsWin-iframe"]')
			#勾选数据
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr/td[2]/div')
			sleep(1)
			span_click("下一步")
			sleep(1)
			# 切入下一步窗体
			switch_to("xpath", '//*[@id="applyWin-iframe"]')
			# 输入领用人
			input("xpath", '//*[@id="username"]', '张中国')
			sleep(2)
			# 领用用途
			click("xpath", '//*[@id="combobox-input-chequepurposeid"]')
			sleep(1)
			up_enter_click('//*[@id="combobox-input-chequepurposeid"]')
			
			# 点击领用
			click("xpath", "//span[text()='领用']")
			sleep(1)
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'领用成功！')]")
			print("可操作组织单笔付款处理，领用成功")
			span_click("快捷集中付款")
			
			
			
			
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
