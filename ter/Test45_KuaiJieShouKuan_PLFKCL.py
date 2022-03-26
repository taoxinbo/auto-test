# encoding=utf-8
# @Time : 2020/11/12 08:30
# @Author : zzg
# 此文件是测试MySQL版本资金结算管理--业务系统对接--快捷收款-批量付款处理
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


class Test45_KuaiJieShouKuan_PLFKCL(unittest.TestCase):
	
	# 启动浏览器
	def setUp(self):
		# 启动浏览器的另外一个方法：通过封装启动浏览器的驱动，启动不同浏览器
		self.driver = get("chrome")
	
	# 登陆系统、对系统设置进行操作
	def test_trade(self):
		
		# login(G_Ora_Url, mindy, Password, "亚唐科技")
		login(G_Mys_Url, mindy, Password, "亚唐科技")
		
		logging.info("开始测试资金结算管理--业务系统对接--快捷收款-批量付款处理")
		# 将页面的滚动条滑动到‘资金结算管理’页面的地方
		js_gd("xpath", "//span[contains(text(),'资金结算管理')]")
		# 用JS的方法点击资金结算管理菜单按钮
		js_click("xpath", "//span[contains(text(),'资金结算管理')]")
		sleep(1)
		# 点击'外币收付结算'菜单
		click("xpath", "//span[text()='业务系统对接']")
		sleep(1)
		# 点击收款处理菜单
		click("xpath", "//span[text()='快捷收款']")
		sleep(1)
		# 退出所有iframe窗体
		switch_default()
		try:
			'''
			# 创建批量收款处理账户💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 收回窗体
			click("xpath", "//span[text()='业务系统对接']")
			sleep(1)
			js_click("xpath", "//span[contains(text(),'资金结算管理')]")
			sleep(1)
			
			# 创建直联单笔收款账户
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
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			#点击新增
			click("xpath", "//span[text()='新增']")
			sleep(1)
			switch_to("xpath", '//*[@id="addWin-iframe"]')
			
			#银行
			click("xpath", "//input[@id='combobox-input-bankid']")
			sleep(1)
			click("xpath", "//div[@title='代码-名称:ABC-农业银行']")
			sleep(1)
			
			# 选择开户行
			input("xpath", "//input[@id='combobox-input-banklocationid']", "103611001617-中国农业银行股份有限公司南宁科园支行")
			sleep(1)
			click("xpath", '//*[@id="banklocationid-combogrid-body-table"]/tbody/tr[1]/td[2]/div')
			sleep(1)
			
			# 选择币种
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
			
			
			# 境内外
			input("xpath", "//input[@id='combobox-input-inorout']", "境内")
			sleep(1)
			input_down("xpath", "//input[@id='combobox-input-inorout']")
			input_enter("xpath", "//input[@id='combobox-input-inorout']")
			# 输入银行账号
			input("xpath", '//*[@id="accountnumber"]', '20211045')
			sleep(1)
			input("xpath", '//*[@id="accountname"]', '付款处理-批量付款处理账户')
			sleep(1)
			# 点击保存按钮
			click("xpath", "//span[text()='保存']")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			sleep(1)
			#对新增账户进行开户
			# 切入窗体
			switch_to("xpath", '//*[@id="bankAccounts-tab-iframe"]')
			sleep(1)
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			
			# 点击查看
			js_click("xpath", "//span[@class='f-contrac-close']")
			sleep(1)
			input("xpath", '//*[@id="accountnumber"]', '20211045')
			# 点击查询
			click("xpath", "//span[text()='查询']")
			sleep(1)
			
			# 勾选数据
			click("xpath",'//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
			sleep(1)
			triangle_cick_and_element("维护","开户")
			#开户日期
			today = date.today()
			open_date = today - timedelta(days=20)
			click("xpath", "//input[@id='openeddatewin-input']")
			sleep(1)
			clear("xpath", "//input[@id='openeddatewin-input']")
			sleep(1)
			input("xpath", "//input[@id='openeddatewin-input']", str(open_date))
			time.sleep(1)
			#金额
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
			input("xpath", "//input[@name='code']", "2045")
			sleep(1)
			
			# 输入结算方式
			input("xpath", "//input[@id='name']", "快捷收款批量收款处理")
			sleep(1)
			
			# 输入交易方向
			input("xpath", "//input[@id='combobox-input-moneyway']", "收入")
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
			input("xpath", '//*[@id="combobox-input-editgrid-bankid-0"]', 'ABC-农业银行')
			click('xpath', '//*[@id="editgrid-bankid-0-combogrid-body-table"]/tbody/tr/td[2]/div')
			sleep(1)
			input('xpath', '//*[@id="combobox-input-editgrid-settlementscenarios-0"]', '默认')
			click('xpath', '//*[@id="f-combo-editgrid-settlementscenarios-0-list-0"]')
			sleep(1)
			click('xpath', '//*[@id="combobox-input-editgrid-directchannelid-0"]')
			sleep(1)
			click('xpath', '//*[@id="editgrid-directchannelid-0-combogrid-body-table"]/tbody/tr[2]/td[2]/div')
			sleep(1)
			input('xpath', '//*[@id="combobox-input-editgrid-directchannelcmdid-0"]', '批量代收')
			click('xpath', '//*[@id="editgrid-directchannelcmdid-0-combogrid-body-table"]/tbody/tr[1]/td[2]/div')
			sleep(1)
			click('xpath', '//*[@id="combobox-input-editgrid-directinterbanksystemid-0"]')
			click('xpath', '//*[@id="editgrid-directinterbanksystemid-0-combogrid-body-table"]/tbody/tr[1]/td[2]/div')
			sleep(1)
			# 点击保存按钮
			click("xpath", "//span[text()='保存']")
			sleep(3)
			# 退出所有iframe窗体
			switch_default()
			
			# 创建直联单笔收款的交易类型
			click("xpath", "//span[text()='交易类型']")
			sleep(1)
			switch_to('xpath', '//*[@id="payType-tab-iframe"]')
			js_click("xpath", "//span[text()='新增']")
			sleep(1)
			# 切入新增的iframe窗体
			switch_to("xpath", "//iframe[@id='addWin-iframe']")
			# 输入代码
			input("xpath", "//input[@id='code']", "3045")
			sleep(1)
			
			# 输入名称
			input("xpath", "//input[@id='name']", "快捷收款-批量收款处理")
			sleep(1)
			
			# 交易方向
			click("xpath", "//input[@id='combobox-input-moneyway']")
			sleep(1)
			input("xpath", "//input[@id='combobox-input-moneyway']", "收入")
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
			input("xpath", "//input[@id='combobox-input-settlementmoderange']", '2045')
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
			'''


			# 返回直联单笔收款页面💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			#点击基础设置收回窗体
			click("xpath",
			      '/html/body/div[1]/div[1]/div/div[2]/div/div[2]/div/div/div/div[4]/div/div/ul/li[1]/a/span[2]')
			sleep(1)
			js_click("xpath", "//span[text()='资金系统收付']")
			sleep(1)
			# 点击收款处理菜单
			click("xpath", "//span[text()='收款处理']")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			
			# 切入直联单笔收款的iframe窗体
			switch_to("xpath", "//iframe[@id='generalRecment-tab-iframe']")
			# 点击直联单笔收款
			click("xpath", "//span[text()='直联批量收款']")
			sleep(1)
			# 进入直联批量收款的iframe 窗体
			switch_to("xpath", '//*[@id="subTabNine-iframe"]')
			# 用JS的方法点击列表导入
			js_click("xpath", "//div[@title='列表导入']")
			# 进入导入详情页面窗体
			switch_to("xpath", "//iframe[@id='importDataWin-iframe']")
			# 选择导入类型
			click("xpath", "//input[@id='combobox-input-businessid']")
			sleep(1)
			input("xpath", "//input[@id='combobox-input-businessid']", "直联批量收款单导入")
			sleep(1)
			input_down("xpath", "//input[@id='combobox-input-businessid']")
			sleep(1)
			input_enter("xpath", "//input[@id='combobox-input-businessid']")
			sleep(1)
			
			# 点击下一步
			click("xpath", "//span[text()='下一步']")
			sleep(1)
			
			# 进入上传详情页窗体
			switch_to("xpath", "//iframe[@id='loadNextWin-iframe']")
			sleep(1)
			
			# 选择交易类型
			click("xpath", "//input[@id='combobox-input-paytypeid']")
			sleep(1)
			input("xpath", "//input[@id='combobox-input-paytypeid']", "3045-快捷收款-批量收款处理")
			sleep(1)
			input_enter("xpath", "//input[@id='combobox-input-paytypeid']")
			sleep(1)
			input_down("xpath", "//input[@id='combobox-input-paytypeid']")
			sleep(2)
			input_enter("xpath", "//input[@id='combobox-input-paytypeid']")
			sleep(2)
			# 选择附件上传
			upload_click("xpath", "//div[text()='上传文件']/parent::*[1]/descendant::*[4]",
			             'D:\FlieDownload', '"KuaiJieFuKuanPLFKCL.xls"')
			sleep(2)
			"directbatchrec (1).xls"
			
			# 点击保存按钮
			click("xpath", "//span[text()='上传']")

			# 退出所有iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功')]")
			time.sleep(3)
			# 更改数据库单据来源
			sql = "update T_SE_RECMENTS set RECORDSOURCE = '4' where purpose like '%快捷付款批量付款处理数据导入%'"
			my_sql(my_host, my_port, my_user, my_passwd, my_db,
			       sql)
			
			# 返回快捷收款-单笔收款查看页面
			click("xpath", "//span[text()='资金系统收付']")
			sleep(1)
			# 点击'外币收付结算'菜单
			click("xpath", "//span[text()='业务系统对接']")
			sleep(1)
			# 点击收款处理菜单
			click("xpath", "//span[text()='快捷收款']")
			sleep(1)
			# 退出所有iframe窗体sleep(1)
			switch_default()
			
			#测试送审功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			#切入批量收款处理页面
			switch_to("xpath",'//*[@id="externalRecments-tab-iframe"]')
			span_click("批量收款处理")
			sleep(1)
			switch_to("xpath",'//*[@id="subTabFour-iframe"]')
			
			#点击放大镜查询数据
			click("xpath",'//*[@id="north"]/div[2]/span')
			sleep(1)
			clear("xpath",'//*[@id="paydatestart-input"]')
			sleep(1)
			span_click("查询")
			
			#勾选数据
			click("xpath",'//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
			sleep(1)
			
			span_click("送审")
			ok_click()
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功')]")
			print("快捷收款-批量收款处理，送审成功！")
			time.sleep(3)
			
			# 二审💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入批量收款处理页面
			switch_to("xpath", '//*[@id="externalRecments-tab-iframe"]')
			span_click("批量收款处理")
			sleep(1)
			switch_to("xpath", '//*[@id="subTabFour-iframe"]')
			
			double_click("xpath",'//*[@id="grid-body-table"]/tbody/tr/td[3]/div')
			sleep(1)
			switch_to("xpath",'//*[@id="wf_taskProcessing_win-iframe"]')
			span_click("同意")
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功')]")
			time.sleep(3)
			
			# 三审💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入批量收款处理页面
			switch_to("xpath", '//*[@id="externalRecments-tab-iframe"]')
			span_click("批量收款处理")
			sleep(1)
			switch_to("xpath", '//*[@id="subTabFour-iframe"]')
			
			double_click("xpath", '//*[@id="grid-body-table"]/tbody/tr/td[3]/div')
			sleep(1)
			switch_to("xpath", '//*[@id="wf_taskProcessing_win-iframe"]')
			span_click("同意")
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功')]")
			time.sleep(3)
			
			# 收款功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入批量收款处理页面
			switch_to("xpath", '//*[@id="externalRecments-tab-iframe"]')
			span_click("批量收款处理")
			sleep(1)
			switch_to("xpath", '//*[@id="subTabFour-iframe"]')
			
			# 勾选数据
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
			sleep(1)
			span_click("收款")
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功')]")
			print("快捷收款-批量收款处理，收款成功！")
			time.sleep(3)
			
			#查询支付状态💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			sql = "update T_SE_RECMENTS set paystate = '7' where purpose like '%快捷付款批量付款处理数据导入%'"
			my_sql(my_host, my_port, my_user, my_passwd, my_db,
			       sql)
			# 切入批量收款处理页面
			switch_to("xpath", '//*[@id="externalRecments-tab-iframe"]')
			span_click("批量收款处理")
			sleep(1)
			switch_to("xpath", '//*[@id="subTabFour-iframe"]')
			
			# 勾选数据
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
			sleep(1)
			
			span_click("收款状态查询")
			ok_click()
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'请查看相应结果!')]")
			print("快捷收款-批量收款处理，查询支付状态成功！")
			time.sleep(3)
			
			#确认已支付💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入批量收款处理页面
			switch_to("xpath", '//*[@id="externalRecments-tab-iframe"]')
			span_click("批量收款处理")
			sleep(1)
			switch_to("xpath", '//*[@id="subTabFour-iframe"]')
			
			# 勾选数据
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
			sleep(1)
			
			span_click("确认已支付")
			ok_click()
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功')]")
			print("快捷收款-批量收款处理，确认已支付成功！")
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
