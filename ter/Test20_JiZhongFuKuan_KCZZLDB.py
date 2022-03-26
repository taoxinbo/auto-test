# encoding=utf-8
# @Time : 2020/10/21 14:49
# @Author : zzg
# 此文件是测试MySQL版本资金结算管理--资金系统收付--集中付款--可操作组织直联单笔付款
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


class Test20_JiZhongFuKuan_KCZZLDB(unittest.TestCase):
	
	# 启动浏览器
	def setUp(self):
		# 启动浏览器的另外一个方法：通过封装启动浏览器的驱动，启动不同浏览器
		self.driver = get("chrome")
	
	# 登陆系统、对系统设置进行操作
	def test_trade(self):
		# 通过登陆封装函数，进行登陆
		# login( G_Ora_Url,TestUser,Password, "自动化测试租户")
		# login( G_Ora_Url,Tao, Password,"默认租户")
		login(G_Mys_Url, mindy, Password, "亚唐科技")
		# login(G_Ora_Url, mindy, Password, "Mindy")
		# login(G_Ora_Url, mindy, Password, "Mindy")
		# login( G_Mys_Url,TestUser,Password, "自动化测试租户")
		# login(G_Mys_Url, Tao, Password, "默认租户")
		# login(G_Mys_Url, mindy, Password, "亚唐科技")
		# login(G_Mys_Url, judy, Password, "默认租户")
		
		logging.info("开始测试资金结算管理的页面功能")
		# 将页面的滚动条滑动到‘资金结算管理’页面的地方
		js_gd("xpath", "//span[contains(text(),'资金结算管理')]")
		# 用JS的方法点击资金结算管理菜单按钮
		js_click("xpath", "//span[contains(text(),'资金结算管理')]")
		sleep(1)
		# 点击'资金系统收付'菜单
		click("xpath", "//span[text()='资金系统收付']")
		sleep(1)
		# 点击集中付款菜单
		click("xpath", "//span[text()='集中付款']")
		sleep(1)
		# 退出所有iframe窗体
		switch_default()
		try:
			
			# 点击资金系统收付收回窗体===============================================
			click("xpath", "//span[text()='资金系统收付']")
			sleep(1)
			js_click("xpath", "//span[contains(text(),'资金结算管理')]")
			sleep(1)
			
			# 创建集中付款-可操作组织直联单笔付款账户
			# 将页面的滚动条滑动到‘账户资金监控’页面的地方
			js_gd("xpath", "//span[contains(text(),'账户资金监控')]")
			# 用JS的方法点击票据管理菜单按钮
			js_click("xpath", "//span[contains(text(),'账户资金监控')]")
			sleep(1)
			click("xpath", "//span[contains(text(),'账户生命周期')]")
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
			sleep(1)
			# 输入开户行大连泡崖街支行名称，模糊查询
			input("xpath", "//input[@id='combobox-input-accounttypeid']", "基本户")
			sleep(1)
			input_down("xpath", "//input[@id='combobox-input-accounttypeid']")
			input_enter("xpath", "//input[@id='combobox-input-accounttypeid']")
			time.sleep(1)
			
			# # 选择银企直联户isbankdirect
			click("xpath", "//input[@id='isbankdirect']")
			sleep(1)
			# 选择境内外
			click("xpath", "//input[@id='combobox-input-inorout']")
			sleep(1)
			# 输入开户行大连泡崖街支行名称，模糊查询
			input("xpath", "//input[@id='combobox-input-inorout']", "境内")
			sleep(1)
			input_down("xpath", "//input[@id='combobox-input-inorout']")
			input_enter("xpath", "//input[@id='combobox-input-inorout']")
			# 输入银行账号
			input("xpath", '//*[@id="accountnumber"]', '20211020')
			sleep(1)
			input("xpath", '//*[@id="accountname"]', '集中付款-可操作组织直联单笔付款账户')
			sleep(2)
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
			input("xpath", '//*[@id="accountnumber"]', '20211020')
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
			print("直联单笔付款测试账户创建成功")
			js_click("xpath", "//span[contains(text(),'账户资金监控')]")
			sleep(1)
			
			#回到主页面
			js_gd("xpath", "//span[contains(text(),'资金结算管理')]")
			# 用JS的方法点击资金结算管理菜单按钮
			js_click("xpath", "//span[contains(text(),'资金结算管理')]")
			sleep(1)
			# 点击'资金系统收付'菜单
			click("xpath", "//span[text()='资金系统收付']")
			sleep(1)
			# 点击集中付款菜单
			click("xpath", "//span[text()='集中付款']")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			
			
			
			##测试新增功能---------------------------------------------------------------------------------
			# 切入集中付款的iframe窗体
			switch_to("xpath", "//iframe[@id='massPayment-tab-iframe']")
			# 点击可操作组织直联单笔付款
			click("xpath", "//span[text()='可操作组织直联单笔付款']")
			sleep(1)
			switch_to("xpath", "//iframe[@id='subTabThree-iframe']")
			#点击新增
			click("xpath", "//span[text()='新增']")
			sleep(1)
			#切入新增的iframe窗体
			switch_to("xpath", "//iframe[@id='addWin-iframe']")
			
			#组织
			clear("xpath",'//*[@id="combobox-input-orgid"]')
			time.sleep(1)
			input("xpath",'//*[@id="combobox-input-orgid"]','001010-亚唐科技')
			sleep(2)
			click("xpath",'//*[@id="orgid-combogrid-body-table"]/tbody/tr/td[2]/div')
			sleep(1)
			
			#交易类型
			click("xpath", "//input[@id='combobox-input-paytypeid']")
			# 输入开户行大连泡崖街支行名称，模糊查询
			input("xpath", "//input[@id='combobox-input-paytypeid']", "103-对外付款")
			sleep(1)
			input_down("xpath", "//input[@id='combobox-input-paytypeid']")
			input_enter("xpath", "//input[@id='combobox-input-paytypeid']")
			time.sleep(1)
			
			# 选择结算方式
			click("xpath", "//input[@id='combobox-input-settlementmodeid']")
			sleep(1)
			clear("xpath", "//input[@id='combobox-input-settlementmodeid']")
			sleep(1)
			# 输入开户行大连泡崖街支行名称，模糊查询
			input("xpath", "//input[@id='combobox-input-settlementmodeid']", "101-直联单笔转账")
			sleep(1)
			input_down("xpath", "//input[@id='combobox-input-settlementmodeid']")
			input_enter("xpath", "//input[@id='combobox-input-settlementmodeid']")
			time.sleep(1)
			
			# 付方账户
			click("xpath", "//input[@id='combobox-input-ourbankaccountid']")
			# 输入账户
			input("xpath", "//input[@id='combobox-input-ourbankaccountid']", "20211020")
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
			input_enter("xpath", "//input[@id='combobox-input-oppbanklocationid']")
			sleep(1)
			input_down("xpath", "//input[@id='combobox-input-oppbanklocationid']")
			sleep(1)
			input_enter("xpath", "//input[@id='combobox-input-oppbanklocationid']")
			time.sleep(1)
			
			# 金额
			money = random.randint(100,200)
			input("xpath", "//input[@id='ouramount-input']", money)
			sleep(1)
			
			# 用途
			use = str(random.randint(1000, 10000))
			input("xpath", "//input[@id='combobox-input-purpose']", use)
			sleep(1)
			
			# 点击保存按钮
			click("xpath", "//span[text()='保存']")
			
			# 退出所有iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("集中付款-可操作组织直联单笔付款，新增成功！" )
			time.sleep(3)
			
			##测试复制功能---------------------------------------------------------------------------------
			# 切入集中付款的iframe窗体
			switch_to("xpath", "//iframe[@id='massPayment-tab-iframe']")
			# 点击可操作组织直联单笔付款
			click("xpath", "//span[text()='可操作组织直联单笔付款']")
			sleep(1)
			switch_to("xpath", "//iframe[@id='subTabThree-iframe']")
			
			#刷新，勾选数据
			click("xpath",'//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			#点击复制
			click("xpath", "//span[text()='复制']")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("集中付款-直联单笔支付，复制成功！")
			time.sleep(3)
			
			##测试修改功能---------------------------------------------------------------------------------
			# 切入集中付款的iframe窗体
			switch_to("xpath", "//iframe[@id='massPayment-tab-iframe']")
			# 点击可操作组织直联单笔付款
			click("xpath", "//span[text()='可操作组织直联单笔付款']")
			sleep(1)
			switch_to("xpath", "//iframe[@id='subTabThree-iframe']")
			
			# 刷新，勾选数据
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			# 点击修改按钮
			click("xpath", "//span[text()='修改']")
			sleep(1)
			# 切入修改的iframe窗体
			switch_to("xpath", "//iframe[@id='modWin-iframe']")
			clear("xpath",'//*[@id="combobox-input-purpose"]')
			sleep(1)
			input("xpath",'//*[@id="combobox-input-purpose"]','修改')
			sleep(2)
			# 点击保存按钮
			click("xpath", "//span[text()='保存']")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("集中付款-直联单笔支付，修改成功！")
			time.sleep(3)
			
			##测试余额检测---------------------------------------------------------------------------------
			# 切入集中付款的iframe窗体
			switch_to("xpath", "//iframe[@id='massPayment-tab-iframe']")
			# 点击可操作组织直联单笔付款
			click("xpath", "//span[text()='可操作组织直联单笔付款']")
			sleep(1)
			switch_to("xpath", "//iframe[@id='subTabThree-iframe']")
			
			# 刷新，勾选数据
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			# 用JS方便点击‘支付’按钮旁边的倒三角形
			js_click("xpath", "//span[text()='支付']/parent::*/following-sibling::*/child::*")
			sleep(1)
			
			# 点击查询状态按钮
			js_click("xpath", "//a[contains(text(),'余额检测')]")
			sleep(1)
			
			# 退出所有iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'余额充足')]")
			print("集中付款-可操作组织直联单笔支付，余额检测成功！")
			time.sleep(3)
			
			##测试删除功能---------------------------------------------------------------------------------
			# 切入集中付款的iframe窗体
			switch_to("xpath", "//iframe[@id='massPayment-tab-iframe']")
			# 点击可操作组织直联单笔付款
			click("xpath", "//span[text()='可操作组织直联单笔付款']")
			sleep(1)
			switch_to("xpath", "//iframe[@id='subTabThree-iframe']")
			
			# 刷新，勾选数据
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
			print("集中付款-直联单笔支付，删除成功！")
			time.sleep(3)
			
			##测试送审功能、撤销送审功能---------------------------------------------------------------------------------
			# 切入集中付款的iframe窗体
			switch_to("xpath", "//iframe[@id='massPayment-tab-iframe']")
			# 点击可操作组织直联单笔付款
			click("xpath", "//span[text()='可操作组织直联单笔付款']")
			sleep(1)
			switch_to("xpath", "//iframe[@id='subTabThree-iframe']")
			
			# 刷新，勾选数据
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
			print("集中付款-直联单笔支付，送审成功！")
			time.sleep(3)
			#测试撤销送审
			# 切入集中付款的iframe窗体
			switch_to("xpath", "//iframe[@id='massPayment-tab-iframe']")
			# 点击可操作组织直联单笔付款
			click("xpath", "//span[text()='可操作组织直联单笔付款']")
			sleep(1)
			switch_to("xpath", "//iframe[@id='subTabThree-iframe']")
			
			# 刷新，勾选数据
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			# 用JS方便点击"送审"按钮旁边的倒三角形
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
			print("集中付款-直联单笔支付，撤销送审成功！")
			time.sleep(3)
			
			##测试支付功能---------------------------------------------------------------------------------
			# 切入集中付款的iframe窗体
			switch_to("xpath", "//iframe[@id='massPayment-tab-iframe']")
			# 点击可操作组织直联单笔付款
			click("xpath", "//span[text()='可操作组织直联单笔付款']")
			sleep(1)
			switch_to("xpath", "//iframe[@id='subTabThree-iframe']")
			
			# 刷新，勾选数据
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			#点击审核按钮
			click("xpath", "//span[text()='送审']")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！送审成功1笔，失败0笔。')]")
			time.sleep(3)
			
			#二审
			# 切入集中付款的iframe窗体
			switch_to("xpath", "//iframe[@id='massPayment-tab-iframe']")
			# 点击可操作组织直联单笔付款
			click("xpath", "//span[text()='可操作组织直联单笔付款']")
			sleep(1)
			switch_to("xpath", "//iframe[@id='subTabThree-iframe']")
			
			double_click("xpath",'//*[@id="grid-body-table"]/tbody/tr[1]/td[3]/div')
			sleep(1)
			switch_to("xpath",'//*[@id="wf_taskProcessing_win-iframe"]')
			click("xpath", "//span[text()='同意']")
			sleep(1)
			switch_default()
			sleep(3)
			
			#点击支付按钮
			# 切入集中付款的iframe窗体
			switch_to("xpath", "//iframe[@id='massPayment-tab-iframe']")
			# 点击可操作组织直联单笔付款
			click("xpath", "//span[text()='可操作组织直联单笔付款']")
			sleep(1)
			switch_to("xpath", "//iframe[@id='subTabThree-iframe']")
			
			# 刷新，勾选数据
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			#点击支付按钮
			click("xpath", "//span[text()='支付']")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！1笔进行了支付，0笔不允许支付。')]")
			print("集中付款-可操作组织直联单笔支付成功！")
			time.sleep(3)
			
			##测试查询支付状态---------------------------------------------------------------------------------
			sql = "update t_se_payments set paystate = '4' where purpose = '" + use + "'"
			my_sql(my_host, my_port, my_user, my_passwd, my_db,
			       sql)
			# 切入集中付款的iframe窗体
			switch_to("xpath", "//iframe[@id='massPayment-tab-iframe']")
			# 点击可操作组织直联单笔付款
			click("xpath", "//span[text()='可操作组织直联单笔付款']")
			sleep(1)
			switch_to("xpath", "//iframe[@id='subTabThree-iframe']")
			
			# 刷新，勾选数据
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			# 用JS方便点击‘支付’按钮旁边的倒三角形
			js_click("xpath", "//span[text()='支付']/parent::*/following-sibling::*/child::*")
			sleep(1)
			
			# 点击查询状态按钮
			js_click("xpath", "//a[contains(text(),'查询状态')]")
			sleep(1)
			
			# 退出所有iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'单据已查询状态，请查看相应结果！')]")
			print("集中付款-可操作组织直联单笔支付，查询状态成功！")
			time.sleep(3)
			
			##测试确认已支付---------------------------------------------------------------------------------
			sql2 = "update t_se_payments set paystate = '7' where purpose = '" + use + "'"
			my_sql(my_host, my_port, my_user, my_passwd, my_db,
			       sql2)
			# 切入集中付款的iframe窗体
			switch_to("xpath", "//iframe[@id='massPayment-tab-iframe']")
			# 点击可操作组织直联单笔付款
			click("xpath", "//span[text()='可操作组织直联单笔付款']")
			sleep(1)
			switch_to("xpath", "//iframe[@id='subTabThree-iframe']")
			
			# 刷新，勾选数据
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			# 用JS方便点击‘支付’按钮旁边的倒三角形
			js_click("xpath", "//span[text()='支付']/parent::*/following-sibling::*/child::*")
			sleep(1)
			
			js_click("xpath", "//a[contains(text(),'确认已支付')]")
			sleep(1)
			# 点击OK按钮
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("集中付款-可操作组织直联单笔支付，确认已支付成功！")
			time.sleep(3)
			
			##测试确认支付失败不实现自动化---------------------------------------------------------------------------------
			
			##测试确认非直联已支付-------------------------------------------------------------------------
			sql3 = "update t_se_payments set paystate = '3' where purpose = '" + use + "'"
			my_sql(my_host, my_port, my_user, my_passwd, my_db,
			       sql3)
			# 切入集中付款的iframe窗体
			switch_to("xpath", "//iframe[@id='massPayment-tab-iframe']")
			# 点击可操作组织直联单笔付款
			click("xpath", "//span[text()='可操作组织直联单笔付款']")
			sleep(1)
			switch_to("xpath", "//iframe[@id='subTabThree-iframe']")
			
			# 刷新，勾选数据
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			# 用JS方便点击‘支付’按钮旁边的倒三角形
			js_click("xpath", "//span[text()='支付']/parent::*/following-sibling::*/child::*")
			sleep(1)
			
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
			print("集中付款-可操作组织直联单笔支付，非直联支付成功！")
			time.sleep(3)
			
			##测试日志查看-------------------------------------------------------------------------
			# 切入集中付款的iframe窗体
			switch_to("xpath", "//iframe[@id='massPayment-tab-iframe']")
			# 点击可操作组织直联单笔付款
			click("xpath", "//span[text()='可操作组织直联单笔付款']")
			sleep(1)
			switch_to("xpath", "//iframe[@id='subTabThree-iframe']")
			
			# 刷新，勾选数据
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			# 用JS方便点击‘支付’按钮旁边的倒三角形
			js_click("xpath", "//span[text()='支付']/parent::*/following-sibling::*/child::*")
			sleep(1)
			
			js_click("xpath", "//a[contains(text(),'日志查看')]")
			sleep(1)
			switch_to("xpath", "//iframe[@id='logsWin-iframe']")
			sleep(1)
			
			# 用隐式等待方法等页面出现
			implici_wait("xpath", "//div[@title='银行返回信息码:BOC01']")
			print("集中付款-可操作组织直联单笔支付，日志查看成功！")
			time.sleep(3)
			
			switch_parent()
			
			# 点击关闭页面
			click("xpath", "//span[text()='支付日志']/preceding-sibling::*[1]")
			sleep(1)
			switch_default()
			
			##测试冲正-------------------------------------------------------------------------
			# 切入集中付款的iframe窗体
			sql4 = "update t_se_payments set paystate = '2' where purpose = '" + use + "'"
			my_sql(my_host, my_port, my_user, my_passwd, my_db,
			       sql4)
			switch_to("xpath", "//iframe[@id='massPayment-tab-iframe']")
			# 点击可操作组织直联单笔付款
			click("xpath", "//span[text()='可操作组织直联单笔付款']")
			sleep(1)
			switch_to("xpath", "//iframe[@id='subTabThree-iframe']")
			
			# 刷新，勾选数据
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			# 用JS方便点击‘其他支付’按钮旁边的倒三角形
			js_click("xpath", "//span[text()='其他操作']/parent::*/following-sibling::*/child::*")
			sleep(1)
			
			# 点击冲正按钮
			js_click("xpath", "//a[contains(text(),'冲正')]")
			sleep(1)
			
			switch_to("xpath", "//iframe[@id='reverseWin-iframe']")
			sleep(1)
			
			# 点击选择冲正日期
			# 点击冲正日期的日历按钮
			js_click("xpath", "//span[@id='reversedate-trigger']")
			time.sleep(1)
			
			# 退出所有iframe窗体
			switch_default()
			# 切入日历框的iframe
			switch_to("xpath", "//iframe[@hidefocus='true']")
			# 点击日历框中今天的按钮
			click("xpath", "//input[@id='dpTodayInput']")
			time.sleep(1)
			# 退出当前日历框的iframe窗体
			switch_default()
			
			# 切入‘直联单笔付款’的iframe窗体
			switch_to("xpath", "//iframe[@id='massPayment-tab-iframe']")
			sleep(1)
			
			# 点击可操作组织直联单笔付款
			click("xpath", "//span[text()='可操作组织直联单笔付款']")
			sleep(1)
			switch_to("xpath", "//iframe[@id='subTabThree-iframe']")
			sleep(1)
			
			switch_to("xpath", "//iframe[@id='reverseWin-iframe']")
			sleep(1)
			
			# 点击选择冲正原因
			click("xpath", "//input[@id='reversalreason']")
			sleep(1)
			input("xpath", "//input[@id='reversalreason']", "测试冲正")
			sleep(1)
			#生成付款单
			click("xpath",'//*[@id="iscreatenewtrade"]')
			sleep(1)
			# 点击确定按钮
			click("xpath", "//span[text()='确认冲正']")
			sleep(1)
			
			switch_default()
			
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功')]")
			print("集中付款-可操作组织直联单笔支付，冲正成功！")
			time.sleep(3)
			
			##测试作废-------------------------------------------------------------------------
			# 切入集中付款的iframe窗体
			switch_to("xpath", "//iframe[@id='massPayment-tab-iframe']")
			# 点击可操作组织直联单笔付款
			click("xpath", "//span[text()='可操作组织直联单笔付款']")
			sleep(1)
			switch_to("xpath", "//iframe[@id='subTabThree-iframe']")
			
			# 刷新，勾选数据
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			# 用JS方便点击‘其他支付’按钮旁边的倒三角形
			js_click("xpath", "//span[text()='其他操作']/parent::*/following-sibling::*/child::*")
			sleep(1)
			
			# 点击作废按钮
			js_click("xpath", "//a[contains(text(),'作废')]")
			sleep(1)
			#点击ok
			click("xpath",'//*[@id="f-message-webgen-0-okBnt"]')
			sleep(1)
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("集中付款-可操作组织直联单笔支付，作废成功！")
			time.sleep(3)
			
			## 测试导入功能----------------------------------------------------------------------
			# 切入集中付款的iframe窗体
			switch_to("xpath", "//iframe[@id='massPayment-tab-iframe']")
			# 点击可操作组织直联单笔付款
			click("xpath", "//span[text()='可操作组织直联单笔付款']")
			sleep(1)
			switch_to("xpath", "//iframe[@id='subTabThree-iframe']")
			
			#点击导入按钮
			click("xpath",'//*[@id="gridtitle"]/div[3]/div[2]')
			sleep(1)
			#切入窗口
			switch_to("xpath",'//*[@id="importDataWin-iframe"]')
			input("xpath",'//*[@id="combobox-input-businessid"]','可操作组织直联单笔付款导入')
			sleep(2)
			click("xpath",'//*[@id="businessid-combogrid-body-table"]/tbody/tr[1]/td[2]/div')
			sleep(1)
			click("xpath","//span[text()='下一步']")
			sleep(1)
			
			switch_to("xpath",'//*[@id="loadNextWin-iframe"]')
			input("xpath", '//*[@id="combobox-input-paytypeid"]', '103-对外付款')
			sleep(2)
			click("xpath", '//*[@id="paytypeid-combogrid-body-table"]/tbody/tr/td[2]/div')
			sleep(1)
			
			# 附件上传
			upload_click("xpath", "//div[text()='上传文件']/parent::*[1]/descendant::*[4]",
			             'D:\FlieDownload', '"masspay2.xls"')
			sleep(3)
			# 点击保存按钮
			click("xpath", "//span[text()='上传']")
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功')]")
			print("集中付款-可操作组织直联单笔付款导入成功！")
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