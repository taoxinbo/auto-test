# encoding=utf-8
# @Time : 2020/11/02 08:30
# @Author : zzg
# 此文件是测试Oracle版本资金结算管理--资金系统收付--收款处理--现金收款
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
class Test25_ShouKuanChuLi_XJSK(unittest.TestCase):
	
	# 启动浏览器
	def setUp(self):
		# 启动浏览器的另外一个方法：通过封装启动浏览器的驱动，启动不同浏览器
		self.driver = get("chrome")
	
	# 登陆系统、对系统设置进行操作
	def test_trade(self):
		
		#login(G_Ora_Url, mindy, Password, "亚唐科技")
		login(G_Ora_Url, mindy, Password, "亚唐科技")
		
		logging.info("开始测试资金结算管理-资金系统收付-收款处理-现金收款页面功能")
		# 将页面的滚动条滑动到‘资金结算管理’页面的地方
		js_gd("xpath", "//span[contains(text(),'资金结算管理')]")
		# 用JS的方法点击资金结算管理菜单按钮
		js_click("xpath", "//span[contains(text(),'资金结算管理')]")
		sleep(1)
		# 点击'资金系统收付'菜单
		click("xpath", "//span[text()='资金系统收付']")
		sleep(1)
		# 点击收款处理菜单
		click("xpath", "//span[text()='收款处理']")
		sleep(1)
		# 退出所有iframe窗体
		switch_default()
		try:
			'''
			#创建现金收款账户💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			##点击资金系统收付收回窗体
			click("xpath", "//span[text()='资金系统收付']")
			sleep(1)
			js_click("xpath", "//span[contains(text(),'资金结算管理')]")
			sleep(1)
			
			# 创建现金收款账户
			js_gd("xpath", "//span[contains(text(),'账户资金监控')]")
			# 用JS的方法点击票据管理菜单按钮
			js_click("xpath", "//span[contains(text(),'账户资金监控')]")
			sleep(1)
			click("xpath", "//span[text()='账户生命周期']")
			sleep(1)
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
			
			# # 选择现金虚拟户
			click("xpath", '//*[@id="iscashvirtual"]')
			
			# 选择境内外
			
			click("xpath", "//input[@id='combobox-input-inorout']")
			# 输入开户行大连泡崖街支行名称，模糊查询
			input("xpath", "//input[@id='combobox-input-inorout']", "境内")
			sleep(1)
			input_down("xpath", "//input[@id='combobox-input-inorout']")
			input_enter("xpath", "//input[@id='combobox-input-inorout']")
			# 输入银行账号
			input("xpath", '//*[@id="accountnumber"]', '20211025')
			sleep(1)
			input("xpath", '//*[@id="accountname"]', '现金收款账户')
			
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
			input("xpath", '//*[@id="accountnumber"]', '20211025')
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
			print("现金支付账户创建成功")
			#点击收回账户资金监控按钮
			js_click("xpath", "//span[contains(text(),'账户资金监控')]")
			sleep(1)
			
			#返回现金收款页面
			js_gd("xpath", "//span[contains(text(),'资金结算管理')]")
			# 用JS的方法点击资金结算管理菜单按钮
			js_click("xpath", "//span[contains(text(),'资金结算管理')]")
			sleep(1)
			# 点击'资金系统收付'菜单
			click("xpath", "//span[text()='资金系统收付']")
			sleep(1)
			# 点击收款处理菜单
			click("xpath", "//span[text()='收款处理']")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			'''
			#测试新增功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			for i in range(1,4):
				global use
				switch_to("xpath", "//iframe[@id='generalRecment-tab-iframe']")
				sleep(1)
				# 点击现金收款
				click("xpath", "//span[text()='现金收款']")
				sleep(1)
				# 切入‘现金收款’的iframe窗体
				switch_to("xpath", "//iframe[@id='subTabFour-iframe']")
				sleep(1)
				
				# 用JS的方法点击新增按钮
				js_click("xpath", "//span[text()='新增']")
				
				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='addWin-iframe']")
				sleep(1)
				
				
				# 交易类型
				click("xpath", "//input[@id='combobox-input-paytypeid']")
				sleep(1)
				# 输入开户行大连泡崖街支行名称，模糊查询
				input("xpath", "//input[@id='combobox-input-paytypeid']", "201-外部收款")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-paytypeid']")
				input_enter("xpath", "//input[@id='combobox-input-paytypeid']")
				time.sleep(1)
				
				# 选择结算方式
				click("xpath", "//input[@id='combobox-input-settlementmodeid']")
				clear("xpath", "//input[@id='combobox-input-settlementmodeid']")
				sleep(1)
				# 输入模糊查询
				input("xpath", "//input[@id='combobox-input-settlementmodeid']", "302-现金收款")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-settlementmodeid']")
				input_enter("xpath", "//input[@id='combobox-input-settlementmodeid']")
				time.sleep(1)
				
				# 收方账户  定位起来比较麻烦，普通定位方式不唯一
				input("xpath","//a[@id='checkBalance']/parent::li/parent::ul/parent::li/parent::ul/parent::li/preceding-sibling::li/following::input[2]",'20211025')
				sleep(1)
				input_down("xpath","//a[@id='checkBalance']/parent::li/parent::ul/parent::li/parent::ul/parent::li/preceding-sibling::li/following::input[2]")
				input_enter("xpath","//a[@id='checkBalance']/parent::li/parent::ul/parent::li/parent::ul/parent::li/preceding-sibling::li/following::input[2]")
				sleep(1)
				
				# 付方户名
				input("xpath", "//input[@id='combobox-input-oppcounterpartyid']", "浙江华语科技")
				sleep(1)
				# 双击清楚下拉框
				double_click("xpath", "//span[text()='卡折类型']")
				sleep(1)
				
				# 付方账户
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
				money=random.randint(100,300)
				input("xpath", "//input[@id='ouramount-input']", money)
				sleep(1)
				
				# 用途
				if i==1 :
					use = random.randint(1000,10000)
					input("xpath", "//input[@id='combobox-input-purpose']", use)
					sleep(1)
				if i==2 :
					use2 = random.randint(1000,10000)
					input("xpath", "//input[@id='combobox-input-purpose']", use2)
					sleep(1)
				if i==3 :
					use3=random.randint(1000,10000)
					input("xpath", "//input[@id='combobox-input-purpose']", use3)
					sleep(1)
				
				# 点击保存按钮
				click("xpath", "//span[text()='保存']")
				sleep(1)
				# 退出所有iframe窗体
				switch_default()
				
				# 用隐式等待方法等页面出现新增成功的提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				if i ==3:
					print("现金收款，新增成功")
				time.sleep(3)
		
			# 测试新增功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", "//iframe[@id='generalRecment-tab-iframe']")
			sleep(1)
			# 点击现金收款
			click("xpath", "//span[text()='现金收款']")
			sleep(1)
			# 切入‘现金收款’的iframe窗体
			switch_to("xpath", "//iframe[@id='subTabFour-iframe']")
			sleep(1)
			
			#刷新、勾选按钮
			click("xpath",'//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath",'//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			#点击修改按钮
			span_click("修改")
			sleep(1)
			# 切入修改的iframe窗体
			switch_to("xpath", "//iframe[@id='modWin-iframe']")
			sleep(2)
			
			# 更改备注
			input("xpath",'//*[@id="memo"]', "测试修改")
			sleep(1)
			
			# 点击保存按钮
			click("xpath", "//span[text()='保存']")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("现金收款，修改成功！")
			time.sleep(3)
			
			# 测试删除功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", "//iframe[@id='generalRecment-tab-iframe']")
			sleep(1)
			# 点击现金收款
			click("xpath", "//span[text()='现金收款']")
			sleep(1)
			# 切入‘现金收款’的iframe窗体
			switch_to("xpath", "//iframe[@id='subTabFour-iframe']")
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			#点击删除
			span_click("删除")
			sleep(1)
			# 点击弹出框的OK键
			ok_click()
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("现金收款，删除成功！")
			time.sleep(3)
			
			# 测试作废功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", "//iframe[@id='generalRecment-tab-iframe']")
			sleep(1)
			# 点击现金收款
			click("xpath", "//span[text()='现金收款']")
			sleep(1)
			# 切入‘现金收款’的iframe窗体
			switch_to("xpath", "//iframe[@id='subTabFour-iframe']")
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			# 点击作废
			span_click("作废")
			sleep(1)
			# 点击弹出框的OK键
			ok_click()
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("现金收款，作废成功！")
			time.sleep(3)
			
			# 测试送审功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", "//iframe[@id='generalRecment-tab-iframe']")
			sleep(1)
			# 点击现金收款
			click("xpath", "//span[text()='现金收款']")
			sleep(1)
			# 切入‘现金收款’的iframe窗体
			switch_to("xpath", "//iframe[@id='subTabFour-iframe']")
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			#点击送审
			span_click("送审")
			sleep(1)
			switch_default()
			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！送审成功1笔，失败0笔。')]")
			print("现金收款，送审成功！")
			time.sleep(3)
			
			#二审
			switch_to("xpath", "//iframe[@id='generalRecment-tab-iframe']")
			sleep(1)
			# 点击现金收款
			click("xpath", "//span[text()='现金收款']")
			sleep(1)
			# 切入‘现金收款’的iframe窗体
			switch_to("xpath", "//iframe[@id='subTabFour-iframe']")
			sleep(1)
			#双击数据
			double_click('xpath','//*[@id="grid-body-table"]/tbody/tr/td[3]/div')
			sleep(1)
			switch_to("xpath",'//*[@id="wf_taskProcessing_win-iframe"]')
			span_click("同意")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("现金收款，二审成功！")
			time.sleep(3)
			
			# 测试收款功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", "//iframe[@id='generalRecment-tab-iframe']")
			sleep(1)
			# 点击现金收款
			click("xpath", "//span[text()='现金收款']")
			sleep(1)
			# 切入‘现金收款’的iframe窗体
			switch_to("xpath", "//iframe[@id='subTabFour-iframe']")
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("收款")
			sleep(1)
			
			span_click("确定")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("现金收款，收款成功！")
			time.sleep(3)
			
			# 测试打印功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", "//iframe[@id='generalRecment-tab-iframe']")
			sleep(1)
			# 点击现金收款
			click("xpath", "//span[text()='现金收款']")
			sleep(1)
			# 切入‘现金收款’的iframe窗体
			switch_to("xpath", "//iframe[@id='subTabFour-iframe']")
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			#点击打印
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
					print("现金收款，打印成功!！")
					time.sleep(3)
					self.driver.switch_to.window(now_handle)
					switch_default()
			
			#测试收据打印💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			sql = "update T_SE_RECMENTS set FINACCOUNTSTATE ='2' where purpose = '" + str(use) + "'"
			ora_sql(ora_ip, ora_sid, ora_user, ora_pwd,
			       sql)
			
			switch_to("xpath", "//iframe[@id='generalRecment-tab-iframe']")
			sleep(1)
			# 点击现金收款
			click("xpath", "//span[text()='现金收款']")
			sleep(1)
			# 切入‘现金收款’的iframe窗体
			switch_to("xpath", "//iframe[@id='subTabFour-iframe']")
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			#点击倒三角
			triangle_cick_and_element("打印",'收据打印')
			
			switch_to("xpath", '//*[@id="printWin-iframe"]')
			implici_wait("xpath", "//td[contains(text(),'浙江华语科技')]")
			sleep(3)
			print("收款处理-承兑汇票收票，收据打印成功!！")
			switch_parent()
			click("xpath", '//*[@id="f-win-title-printWin"]/div[1]/div')
			sleep(1)
			switch_default()
			
			# 测试打印记录💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", "//iframe[@id='generalRecment-tab-iframe']")
			sleep(1)
			# 点击现金收款
			click("xpath", "//span[text()='现金收款']")
			sleep(1)
			# 切入‘现金收款’的iframe窗体
			switch_to("xpath", "//iframe[@id='subTabFour-iframe']")
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			# 点击倒三角
			triangle_cick("打印")
			sleep(1)
			# 点击打印记录按钮
			js_click("xpath", "//a[contains(text(),'打印记录')]")
			sleep(1)
			
			switch_to("xpath", "//iframe[@id='printWin-iframe']")
			sleep(1)
			
			# 用隐式等待方法等页面出现  操作人:mindy
			implici_wait("xpath", "//div[@title='操作人:mindy']")
			print("现金收款，打印记录查看成功！")
			time.sleep(3)
			switch_parent()
			# 点击关闭页面
			click("xpath", "//span[text()='打印']/preceding-sibling::*[1]")
			sleep(1)
			switch_default()
			
			# 测试上传功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", "//iframe[@id='generalRecment-tab-iframe']")
			sleep(1)
			# 点击现金收款
			click("xpath", "//span[text()='现金收款']")
			sleep(1)
			# 切入‘现金收款’的iframe窗体
			switch_to("xpath", "//iframe[@id='subTabFour-iframe']")
			sleep(1)
			
			#点击上传
			click("xpath",'//*[@id="gridtitle"]/div[3]/div[2]')
			sleep(1)
			switch_to("xpath",'//*[@id="importDataWin-iframe"]')
			click("xpath",'//*[@id="combobox-input-businessid"]')
			input_down("xpath",'//*[@id="combobox-input-businessid"]')
			input_enter("xpath",'//*[@id="combobox-input-businessid"]')
			sleep(1)
			sleep(1)
			span_click("下一步")
			sleep(1)
			switch_to("xpath",'//*[@id="loadNextWin-iframe"]')
			input("xpath",'//*[@id="combobox-input-paytypeid"]','201-外部收款')
			sleep(1)
			input_down("xpath",'//*[@id="combobox-input-paytypeid"]')
			input_enter("xpath",'//*[@id="combobox-input-paytypeid"]')
			sleep(1)
			input("xpath",'//*[@id="combobox-input-settlementmodeid"]',"302-现金收款")
			sleep(1)
			input_down("xpath",'//*[@id="combobox-input-settlementmodeid"]')
			input_enter("xpath",'//*[@id="combobox-input-settlementmodeid"]')
			sleep(1)
			# 附件上传
			upload_click("xpath", "//div[text()='上传文件']/parent::*[1]/descendant::*[4]",
			             'D:\FlieDownload', '"cashrec1.xls"')
			sleep(3)
			# 点击保存按钮
			click("xpath", "//span[text()='上传']")
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功,共导入1条数据，成功1条，失败0条，未处理0条。')]")
			print("现金收款，文件上传成功！")
			time.sleep(3)
			
			
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("现金收款失败！" + str(traceback.format_exc()))
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
