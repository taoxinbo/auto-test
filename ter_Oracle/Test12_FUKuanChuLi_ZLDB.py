# encoding=utf-8
# @Time : 2020/10/12 14:49
# @Author : zzg
# 此文件是测试Mysql版本资金结算管理--资金系统收付--付款处理--直联单笔支付
#       拆分付款查看里面的功能和外面一致，故只需要测试一遍

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
class Test_Fkcl_Zldbzf_Mysql(unittest.TestCase):
	
	# 启动浏览器
	def setUp(self):
		# 启动浏览器的另外一个方法：通过封装启动浏览器的驱动，启动不同浏览器
		self.driver = get("chrome")
	
	# 登陆系统、对系统设置进行操作
	def test_trade(self):
		
		login(G_Ora_Url, mindy, Password, "亚唐科技")
		
		logging.info("开始测试资金结算管理--资金系统收付--付款处理--直联单笔支付")
		
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
		try:
			'''
			# 创建直联单笔支付账户💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
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
			click("xpath", "//span[@title='账户生命周期']")
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
			input("xpath", '//*[@id="accountnumber"]', '20211012')
			sleep(1)
			input("xpath", '//*[@id="accountname"]', '付款处理-直联单笔支付账户')
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
			input("xpath", '//*[@id="accountnumber"]', '20211012')
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
			input("xpath", '//*[@id="journalbalance-input"]', "50000")
			sleep(1)
			click("xpath", "//span[text()='确定']")
			sleep(1)
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			sleep(3)
			js_click("xpath", "//span[contains(text(),'账户资金监控')]")
			sleep(1)
			logging.info("账户开户成功")

			# 回到直联单笔付款界面
			js_gd("xpath", "//span[contains(text(),'资金结算管理')]")
			# 用JS的方法点击资金结算管理菜单按钮
			js_click("xpath", "//span[contains(text(),'资金结算管理')]")
			sleep(1)
			click("xpath", "//span[text()='资金系统收付']")
			sleep(1)
			click("xpath", "//span[text()='付款处理']")
			# 退出所有iframe窗体
			switch_default()
            '''
			# 开始测试直联单笔付款💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			for i in range(1, 8):
				# 切入窗体
				switch_to("xpath", '//*[@id="generalPayment-tab-iframe"]')
				switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
				sleep(1)
				# 切入新增窗体
				click("xpath", '//*[@id="button1"]/span/span')
				sleep(1)
				switch_to('xpath', '//*[@id="addWin-iframe"]')

				# 交易类型
				input("xpath", '//*[@id="combobox-input-paytypeid"]', "103-对外付款")
				sleep(1)
				click("xpath", '//*[@id="paytypeid-combogrid-body-table"]/tbody/tr/td[2]/div')
				sleep(1)

				# 点击付方账户
				input("xpath", '//*[@id="combobox-input-ourbankaccountid"]', "20211012")
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
					input("xpath", "//input[@id='combobox-input-purpose']", "验证复制功能")
				if i == 2:
					input("xpath", "//input[@id='combobox-input-purpose']", "验证删除功能")
				if i == 3:
					input("xpath", "//input[@id='combobox-input-purpose']", "验证作废功能")
				if i == 4:
					input("xpath", "//input[@id='combobox-input-purpose']", "验证终止功能")
				if i == 5:
					input("xpath", "//input[@id='combobox-input-purpose']", "验证拆分功能")
				if i == 6:
					input("xpath", "//input[@id='combobox-input-purpose']", "验证非直联已支付功能")
				if i == 7:
					input("xpath", "//input[@id='combobox-input-purpose']", "验证冲正功能")
				sleep(1)
				# 双击清楚下拉框
				double_click("xpath", "//span[text()='卡折类型']")
				sleep(1)

				# 保存
				click("xpath", '//*[@id="save"]/span/span')
				switch_default()

				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				if i == 2:
					print("付款处理-直联单笔付款，新增成功")
				time.sleep(3)

			# 测试复制功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入窗体
			switch_to("xpath", '//*[@id="generalPayment-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			sleep(1)
			# 勾选按钮
			click("xpath", "//div[@title='用途:验证复制功能']")
			sleep(1)
			click('xpath', '//*[@id="custButton2"]/span/span')
			sleep(1)
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("付款处理-直联单笔支付，复制成功！")
			sleep(3)

			# 测试修改功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="generalPayment-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			click("xpath", "//div[@title='用途:验证冲正功能']")
			sleep(1)
			click("xpath", '//*[@id="custButton1"]/span/span')
			switch_to('xpath', '//*[@id="modWin-iframe"]')
			sleep(1)
			input("xpath", '//*[@id="memo"]', '测试修改')
			sleep(1)
			click('xpath', '//*[@id="save"]/span/span')
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("付款处理-直联单笔支付，修改成功！")
			sleep(3)

			# 测试删除功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="generalPayment-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			click("xpath", "//div[@title='用途:验证删除功能']")
			sleep(1)
			click("xpath", '//*[@id="custButton3"]/span/span')
			sleep(1)
			click("xpath", '//*[@id="f-message-webgen-0-okBnt"]')
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("付款处理-直联单笔支付，删除成功！")
			sleep(3)

			# 测试送审，撤销送审功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="generalPayment-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			click("xpath", "//div[@title='用途:验证冲正功能']")
			sleep(1)
			click("xpath", "//span[text()='送审']")
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！送审成功1笔，失败0笔。')]")
			print("付款处理-直联单笔支付，送审成功！")
			time.sleep(3)

			# 撤销送审💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="generalPayment-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			click("xpath", "//div[@title='用途:验证冲正功能']")
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
			print("付款处理-直联单笔支付，撤销送审成功！")
			time.sleep(3)

			# 测试支付💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="generalPayment-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			click("xpath", "//div[@title='用途:验证冲正功能']")
			click("xpath", "//div[@title='用途:验证非直联已支付功能']")
			sleep(1)
			click("xpath", "//span[text()='送审']")
			# 退出所有iframe窗体
			switch_default()
			sleep(3)

			# 详情页审批💨💨💨💨💨💨💨💨
			for i in range(1, 3):
				switch_to("xpath", '//*[@id="generalPayment-tab-iframe"]')
				switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
				if i == 1:
					double_click("xpath", "//div[@title='用途:验证冲正功能']")
				if i == 2:
					double_click("xpath", "//div[@title='用途:验证非直联已支付功能']")
				sleep(1)
				switch_to('xpath', '//*[@id="wf_taskProcessing_win-iframe"]')
				sleep(1)
				click("xpath", "//span[text()='同意']")
				switch_default()
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				time.sleep(3)
			
			# 支付💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			for i in range(1, 2):
				switch_to("xpath", '//*[@id="generalPayment-tab-iframe"]')
				switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
				# if i == 1:
				# 	click("xpath", "//div[@title='用途:验证冲正功能']")
				if i == 1:
					click("xpath", "//div[@title='用途:验证非直联已支付功能']")
				sleep(1)
				click("xpath", "//span[text()='支付']")
				sleep(1)
				switch_default()
				implici_wait("xpath", "//span[contains(text(),'操作成功！1笔进行了支付，0笔不允许支付。')]")
				sleep(3)
				print('付款处理-直联单笔支付，支付成功')

			# 测试余额检测💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="generalPayment-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			click("xpath", "//div[@title='用途:验证冲正功能']")
			sleep(1)
			js_click("xpath", "//a[contains(text(),'余额检测')]")
			sleep(1)

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'余额充足')]")
			print("付款处理-直联单笔支付，余额检测成功！")
			time.sleep(3)

			# 测试确认已支付💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			sql = "update T_SE_PAYMENTS set PAYSTATE ='7' where purpose = '" + str("验证冲正功能") + "'"
			ora_sql(ora_ip, ora_sid, ora_user, ora_pwd,
			       sql)
			switch_to("xpath", '//*[@id="generalPayment-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			sleep(1)
			click('xpath', '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", "//div[@title='用途:验证冲正功能']")
			js_click("xpath", "//span[text()='支付']/parent::*/following-sibling::*/child::*")
			sleep(1)
			# 点击确认已支付按钮
			js_click("xpath", "//a[contains(text(),'确认已支付')]")
			sleep(1)
			# 点击OK按钮
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("付款处理-直联单笔支付，确认已支付成功！")
			time.sleep(3)

			# 测试查询状态💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			sql = "update T_SE_PAYMENTS set PAYSTATE ='7' where purpose = '" + str("验证非直联已支付功能") + "'"
			ora_sql(ora_ip, ora_sid, ora_user, ora_pwd,
			       sql)
			switch_to("xpath", '//*[@id="generalPayment-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			click("xpath", "//div[@title='用途:验证非直联已支付功能']")
			js_click("xpath", "//span[text()='支付']/parent::*/following-sibling::*/child::*")
			sleep(1)
			# 点击查询状态按钮
			js_click("xpath", "//a[contains(text(),'查询状态')]")
			sleep(1)

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'单据已查询状态，请查看相应结果！')]")
			print("付款处理-直联单笔支付，查询状态成功！")
			time.sleep(3)

			# 测试确认支付失败一个小时后手工确认（单据超过一个小时才能手工确认）💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨

			# 测试日志查看💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="generalPayment-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			click("xpath", "//div[@title='用途:验证冲正功能']")
			js_click("xpath", "//span[text()='支付']/parent::*/following-sibling::*/child::*")
			sleep(1)

			# 点击日志查看按钮
			js_click("xpath", "//a[contains(text(),'日志查看')]")
			sleep(1)

			switch_to("xpath", "//iframe[@id='logsWin-iframe']")
			sleep(1)

			# 用隐式等待方法等页面出现
			implici_wait("xpath", "//span[contains(text(),'交易单号')]")
			print("付款处理-直联单笔支付，日志查看成功！")
			time.sleep(3)

			switch_parent()

			# 点击关闭页面
			click("xpath", "//span[text()='支付日志']/preceding-sibling::*[1]")
			sleep(1)
			switch_default()
			
			# 测试非直联已支付💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			sql = "update T_SE_PAYMENTS set PAYSTATE ='3' where purpose = '" + str("验证非直联已支付功能") + "'"
			ora_sql(ora_ip, ora_sid, ora_user, ora_pwd,
			       sql)
			switch_to("xpath", '//*[@id="generalPayment-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", "//div[@title='用途:验证非直联已支付功能']")
			sleep(1)
			js_click("xpath", "//span[text()='支付']/parent::*/following-sibling::*/child::*")
			sleep(1)
			# 点击查询状态按钮
			js_click("xpath", "//a[contains(text(),'确认非直联已支付')]")
			sleep(1)
			click("xpath", '//*[@id="f-message-webgen-0-okBnt"]')
			sleep(1)
			# 切入
			switch_to("xpath", '//*[@id="confirmUndirectPayWin-iframe"]')
			input("xpath", '//*[@id="combobox-input-actualsettlementmodeid"]', '其他支付')
			sleep(1)
			click("xpath", '//*[@id="actualsettlementmodeid-combogrid-body-table"]/tbody/tr/td[2]/div')
			sleep(1)
			click("xpath", '//*[@id="determineConfirmUndirectPay"]/span/span')
			sleep(1)
			click("xpath", '//*[@id="f-message-webgen-0-okBnt"]')

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'共1笔，处理成功1笔，失败0笔。')]")
			print("付款处理-直联单笔支付，非直联支付成功！")
			time.sleep(3)

			# 测试打印💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="generalPayment-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", "//div[@title='用途:验证冲正功能']")
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
					implici_wait("xpath", "//td[contains(text(),'浙江华语科技')]")
					print("付款处理-直联单笔支付，打印成功!！")
					time.sleep(3)
					self.driver.switch_to.window(now_handle)
					switch_default()

			# 测试打印记录💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 其他操作-打印记录
			# 切入‘直联单笔付款’的iframe窗体
			switch_to("xpath", '//*[@id="generalPayment-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			sleep(2)
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			click("xpath", "//div[@title='用途:验证冲正功能']")
			sleep(2)

			# 用JS方便点击‘支付’按钮旁边的倒三角形
			js_click("xpath", "//span[text()='其他操作']/parent::*/following-sibling::*/child::*")
			sleep(1)

			# 点击打印记录按钮
			js_click("xpath", "//a[contains(text(),'打印记录')]")
			sleep(1)
			switch_to("xpath", "//iframe[@id='printWin-iframe']")
			sleep(1)
			# 用隐式等待方法等页面出现  操作人:mindy
			implici_wait("xpath", "//div[@title='操作人:mindy']")
			print("付款处理-直联单笔支付，打印记录查看成功！")
			time.sleep(3)

			switch_parent()

			# 点击关闭页面
			click("xpath", "//span[text()='打印记录']/preceding-sibling::*[1]")
			sleep(1)
			switch_default()

			# 测试结算中心打印💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="generalPayment-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			sleep(1)
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", "//div[@title='用途:验证冲正功能']")
			sleep(1)
			# 用JS方便点击‘支付’按钮旁边的倒三角形
			js_click("xpath", "//span[text()='其他操作']/parent::*/following-sibling::*/child::*")
			sleep(1)

			# 点击打印按钮
			js_click("xpath", "//a[contains(text(),'结算中心打印')]")
			time.sleep(3)

			# 获取所有窗口句柄
			all_handles = self.driver.window_handles
			# 循环遍历所有新打开的窗口句柄，也就是说不包括主窗口
			now_handle = self.driver.current_window_handle
			for handle in all_handles:
				self.driver.switch_to.window(handle)
				if self.driver.title == u"payandrecsinglecenterprint":
					implici_wait("xpath", "//td[contains(text(),'浙江华语科技')]")
					print("付款处理-直联单笔支付，结算中心打印成功!！")
					time.sleep(3)
					self.driver.switch_to.window(now_handle)
					switch_default()

			# 其他操作-结算中心打印记录💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入‘直联单笔付款’的iframe窗体
			switch_to("xpath", "//iframe[@id='generalPayment-tab-iframe']")
			sleep(1)

			switch_to("xpath", "//iframe[@id='subTabTwo-iframe']")
			sleep(1)

			js_click("xpath", "//span[text()='其他操作']/parent::*/following-sibling::*/child::*")
			sleep(1)

			# 点击打印记录按钮
			js_click("xpath", "//a[contains(text(),'结算中心打印记录')]")
			sleep(1)

			switch_to("xpath", "//iframe[@id='printWin-iframe']")
			sleep(1)

			# 用隐式等待方法等页面出现  操作人:mindy
			implici_wait("xpath", "//div[@title='操作人:mindy']")
			print("付款处理-直联单笔支付，结算中心打印记录查看成功！")
			time.sleep(3)
			switch_parent()
			# 点击关闭页面
			click("xpath", "//span[text()='打印记录']/preceding-sibling::*[1]")
			sleep(1)
			switch_default()
			sleep(2)

			# 测试审批历史按钮💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="generalPayment-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			sleep(1)
			# 勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", "//div[@title='用途:验证冲正功能']")
			sleep(1)
			span_click("审批历史")
			switch_to("xpath", '//*[@id="flowwin-iframe"]')
			sleep(1)
			# 部分单据提示：无审批流程信息！
			# 部分单据展示：流程图，流程流转tab页
			# 暂时使用它们共有的关键字进行匹配
			try:
				click("xpath", "//span[contains(text(),'流程图')]")
				sleep(2)
				logging.info("审批历史功能验证成功！")
			except:
				click("xpath", "//h1[contains(text(),'无审批流程信息')]")
				sleep(2)
				logging.info("该笔单据没有审批历史！")
			sleep(2)
			switch_parent()
			click('xpath', '//*[@id="f-win-title-flowwin"]/div[1]/div')
			switch_default()


			# 测试作废💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 复制一笔单据
			switch_to("xpath", '//*[@id="generalPayment-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			sleep(1)
			# 勾选用途为验证作废功能的单据
			click("xpath", "//div[@title='用途:验证作废功能']")
			sleep(1)
			# 展列其他操作列表
			js_click("xpath", "//span[text()='其他操作']/parent::*/following-sibling::*/child::*")
			sleep(1)
			# 点击作废按钮
			js_click("xpath", "//a[contains(text(),'作废')]")
			sleep(1)
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
			sleep(1)

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("付款处理-直联单笔支付, 作废成功！")
			time.sleep(3)
			
			# 测试终止💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="generalPayment-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			sleep(1)
			# 勾选按钮
			click("xpath", "//div[@title='用途:验证终止功能']")
			sleep(1)
			click("xpath", '//*[@id="custButton9"]/span/span')
			sleep(1)
			ok_click()
			input('xpath', '//*[@id="terminateReason"]', '测试终止')
			sleep(1)
			click('xpath', '//*[@id="determineTerminate"]/span/span')
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("付款处理-直联单笔支付，测试终止成功！")
			time.sleep(3)

			# 测试拆分功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨

			switch_to("xpath", '//*[@id="generalPayment-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			sleep(1)
			# use1
			# 通过sql直接将未审批单据置为已审批状态，便于验证拆分操作
			sql = "update T_SE_PAYMENTS set APPROVESTATE ='2' where purpose = '" + str("验证拆分功能") + "'"
			ora_sql(ora_ip, ora_sid, ora_user, ora_pwd,
			       sql)
			sleep(1)
			click('xpath', '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			# 勾选按钮
			click("xpath", "//div[@title='用途:验证拆分功能']")
			sleep(1)
			click("xpath", "//span[contains(text(),'拆分')]")
			switch_to("xpath", "//iframe[@id='splitWin-iframe']")
			sleep(1)
			# 填写拆分金额
			# 点击新增第一行
			click("xpath", "//span[text()='拆分金额']/ancestor::*[6]/following-sibling::*[2]/descendant::*[7]")
			sleep(1)
			# 拆分金额
			click("xpath", "//input[@id='splitDetailGrid-amount-0-input']")
			sleep(1)
			input("xpath", "//input[@id='splitDetailGrid-amount-0-input']", "10")
			sleep(1)
			# 点击保存
			click("xpath", "//span[text()='保存']")
			sleep(1)

			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("付款处理-直联单笔支付，拆分成功！")
			time.sleep(3)

			# 拆分付款查看
			# 切入‘直联单笔付款’的iframe窗体
			switch_to("xpath", "//iframe[@id='generalPayment-tab-iframe']")
			sleep(1)
			switch_to("xpath", "//iframe[@id='subTabTwo-iframe']")
			sleep(1)
			# 勾选数据
			click("xpath", "//div[@title='用途:验证拆分功能']")
			sleep(1)
			# 用JS方便点击‘支付’按钮旁边的倒三角形
			js_click("xpath", "//span[text()='拆分']/parent::*/following-sibling::*/child::*")
			sleep(1)
			# 点击查询状态按钮
			js_click("xpath", "//a[contains(text(),'拆分付款查看')]")
			sleep(1)
			switch_to("xpath", "//iframe[@id='splitPaymentsViewWin-iframe']")
			sleep(1)
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[text()='浙江华语科技']")
			print("付款处理-直联单笔支付，拆分付款查看成功！")
			time.sleep(3)
			# 退出当前页面
			switch_parent()
			# 点击关闭当前页面
			click("xpath", "//span[text()='拆分付款单查看']/preceding-sibling::*[1]")
			
			# 退出所有窗体
			switch_default()
			sleep(1)

			# 测试冲正💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入窗体
			switch_to("xpath", "//iframe[@id='generalPayment-tab-iframe']")
			switch_to("xpath", "//iframe[@id='subTabTwo-iframe']")
			sleep(1)
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", "//div[@title='用途:验证冲正功能']")
			sleep(1)
			# 用JS方便点击‘支付’按钮旁边的倒三角形
			js_click("xpath", "//span[text()='其他操作']/parent::*/following-sibling::*/child::*")
			sleep(1)
			# 点击冲正按钮
			js_click("xpath", "//a[contains(text(),'冲正')]")
			sleep(1)
			# reverseWin-iframe
			sleep(1)
			# switch_to("xpath", "//iframe[@id='reverseWin-iframe']")
			# 切入冲正窗体
			switch_to("xpath", '//*[@id="reverseWin-iframe"]')
			sleep(1)
			today = date.today()
			we = str(today) + " " + "08:30:00"
			input("xpath", '//*[@id="reversedate-input"]', we)
			sleep(1)
			keyDown('enter')
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
			print("付款处理-直联单笔支付，冲正成功！")
			time.sleep(3)

			# 测试导入功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入直联单笔支付窗体
			switch_to("xpath", '//*[@id="generalPayment-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			sleep(1)
			# 点击上传按钮
			click("xpath", '//*[@id="gridtitle"]/div[3]/div[2]')
			# 切入新出来的窗体
			switch_to("xpath", '//*[@id="importDataWin-iframe"]')
			# 选择业务点击下一笔
			input('xpath', '//*[@id="combobox-input-businessid"]', '直联单笔付款单导入')
			sleep(1)
			click('xpath', '//*[@id="businessid-combogrid-body-table"]/tbody/tr[1]/td[2]/div')
			sleep(1)
			click("xpath", '//*[@id="save"]/span/span')
			# 切入新出来的窗体
			switch_to("xpath", '//*[@id="loadNextWin-iframe"]')
			# 选择结算方式
			click("xpath", '//*[@id="combobox-input-paytypeid"]')
			click("xpath", '//*[@id="paytypeid-combogrid-body-table"]/tbody/tr[1]/td[2]/div')
			# 附件上传
			upload_click("xpath", "//div[text()='上传文件']/parent::*[1]/descendant::*[4]",
			             'D:\FlieDownload', '"directsinglediffbankpay.xls"')
			sleep(3)
			# 点击保存按钮
			click("xpath", "//span[text()='上传']")
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功')]")
			print("付款处理-直联单笔支付，导入成功！")
			time.sleep(3)

		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("直联单笔支付失败！" + str(traceback.format_exc()))
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