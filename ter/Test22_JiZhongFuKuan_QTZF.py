# encoding=utf-8
# @Time : 2020/11/14 14:49
# @Author : zzg
# 此文件是测试MySQL版本资金结算管理--资金系统收付--集中付款--其他支付
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


class Test22_JiZhongFuKuan_QTZF(unittest.TestCase):
	
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
		span_click("资金系统收付")
		# 点击集中付款菜单
		click("xpath", "//span[text()='集中付款']")
		# 退出所有iframe窗体
		switch_default()
		try:
			'''
			# 点击资金系统收付收回窗体============================================================================
			click("xpath", "//span[text()='资金系统收付']")
			sleep(1)
			js_click("xpath", "//span[contains(text(),'资金结算管理')]")
			sleep(1)
			
			#创建集中付款-其他支付账户
			js_gd("xpath", "//span[contains(text(),'账户资金监控')]")
			# 用JS的方法点击账户资金监控菜单按钮
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
			# 输入开户行大连泡崖街支行名称，模糊查询
			input("xpath", "//input[@id='combobox-input-accounttypeid']", "基本户")
			sleep(1)
			input_down("xpath", "//input[@id='combobox-input-accounttypeid']")
			input_enter("xpath", "//input[@id='combobox-input-accounttypeid']")
			time.sleep(1)
			
			# # 选择现金虚拟户
			
			# 选择境内外
			
			click("xpath", "//input[@id='combobox-input-inorout']")
			# 输入开户行大连泡崖街支行名称，模糊查询
			input("xpath", "//input[@id='combobox-input-inorout']", "境内")
			sleep(1)
			input_down("xpath", "//input[@id='combobox-input-inorout']")
			input_enter("xpath", "//input[@id='combobox-input-inorout']")
			# 输入银行账号
			input("xpath", '//*[@id="accountnumber"]', '20211022')
			sleep(1)
			input("xpath", '//*[@id="accountname"]', '集中付款-其他支付账户')
			
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
			input("xpath", '//*[@id="accountnumber"]', '20211022')
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
			print("集中付款-现金支付账户创建成功")
			'''
			#到付款处理-其他支付页面做数据
			js_click("xpath", "//span[contains(text(),'账户资金监控')]")
			sleep(1)
			# 回到其他支付页面
			js_gd("xpath", "//span[contains(text(),'资金结算管理')]")
			# 用JS的方法点击资金结算管理菜单按钮
			js_click("xpath", "//span[contains(text(),'资金结算管理')]")
			# 点击'资金系统收付'菜单
			click("xpath", "//span[text()='资金系统收付']")
			# 点击付款处理菜单
			click("xpath", "//span[text()='付款处理']")
			# 退出所有iframe窗体
			switch_default()
			
			
			for i in range(1, 4):
				global use
				# 切入其他支付窗体
				switch_to("xpath", "//iframe[@id='generalPayment-tab-iframe']")
				# 点击其他支付
				click("xpath", "//span[text()='其他支付']")
				sleep(1)
				# 进入其他支付的iframe窗体
				switch_to("xpath", "//iframe[@id='subTabEight-iframe']")
				
				# 点击新增
				click("xpath", "//span[text()='新增']")
				sleep(1)
				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='addWin-iframe']")
				sleep(1)
				
				# 交易类型
				click("xpath", "//input[@id='combobox-input-paytypeid']")
				# 输入交易类型，模糊查询
				input("xpath", "//input[@id='combobox-input-paytypeid']", "103-对外付款")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-paytypeid']")
				input_enter("xpath", "//input[@id='combobox-input-paytypeid']")
				time.sleep(1)
				
				# 选择结算方式
				click("xpath", "//input[@id='combobox-input-settlementmodeid']")
				clear("xpath", "//input[@id='combobox-input-settlementmodeid']")
				sleep(1)
				# 输入支付方式
				input("xpath", "//input[@id='combobox-input-settlementmodeid']", "601-其他支付")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-settlementmodeid']")
				input_enter("xpath", "//input[@id='combobox-input-settlementmodeid']")
				time.sleep(1)
				
				# 付方账户
				click("xpath", "//input[@id='combobox-input-ourbankaccountid']")
				# 输入账号
				input("xpath", "//input[@id='combobox-input-ourbankaccountid']", "20211022")
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
				money = random.randint(100, 300)
				input("xpath", "//input[@id='ouramount-input']", money)
				sleep(1)
				
				# 用途
				if i ==1:
					use = random.randint(1000,10000)
					input("xpath", "//input[@id='combobox-input-purpose']", use)
					sleep(1)
				if i ==2:
					use2 = random.randint(1000,10000)
					input("xpath", "//input[@id='combobox-input-purpose']", use2)
					sleep(1)
				if i ==3:
					use3 = random.randint(1000,10000)
					input("xpath", "//input[@id='combobox-input-purpose']", use3)
					sleep(1)
				
				# 手续费
				clear("xpath", '//*[@id="costs-input"]')
				sleep(1)
				input("xpath", '//*[@id="costs-input"]', '10')
				sleep(2)
				
				# 点击保存按钮
				click("xpath", "//span[text()='保存']")
				sleep(1)
				# 退出所有iframe窗体
				switch_default()
				
				# 用隐式等待方法等页面出现新增成功的提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				time.sleep(3)
			
			#回到集中付款-其他支付页面
			span_click("集中付款")
			sleep(1)
			switch_default()
			
			
			#测试修改功能----------------------------------------------------------------------------------
			#切入集中付款窗体
			switch_to("xpath",'//*[@id="massPayment-tab-iframe"]')
			span_click("其他支付")
			sleep(1)
			switch_to("xpath",'//*[@id="subTabFive-iframe"]')
			#点击刷新，勾选按钮
			click("xpath",'//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath",'//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
			
			#点击修改按钮
			span_click("修改")
			sleep(1)
			switch_to("xpath", "//iframe[@id='modWin-iframe']")
			#修改手续费
			clear("xpath",'//*[@id="costs-input"]')
			sleep(1)
			input("xpath",'//*[@id="costs-input"]',"15")
			sleep(1)
			span_click("保存")
			sleep(1)
			switch_default()
			# 用隐式等待方法等页面出现成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("集中付款-其他支付，修改成功！")
			time.sleep(3)
			
			# 测试删除功能----------------------------------------------------------------------------------
			# 切入集中付款窗体
			switch_to("xpath", '//*[@id="massPayment-tab-iframe"]')
			span_click("其他支付")
			sleep(1)
			switch_to("xpath", '//*[@id="subTabFive-iframe"]')
			# 点击刷新，勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
			
			#点击删除
			span_click("删除")
			sleep(1)
			#点击ok
			click("xpath",'//*[@id="f-message-webgen-0-okBnt"]')
			sleep(1)
			switch_default()
			# 用隐式等待方法等页面出现成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("集中付款-其他支付，删除成功！")
			time.sleep(3)
			
			# 测试作废功能----------------------------------------------------------------------------------
			# 切入集中付款窗体
			switch_to("xpath", '//*[@id="massPayment-tab-iframe"]')
			span_click("其他支付")
			sleep(1)
			switch_to("xpath", '//*[@id="subTabFive-iframe"]')
			# 点击刷新，勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
			
			# 点击删除
			span_click("作废")
			sleep(1)
			# 点击ok
			click("xpath", '//*[@id="f-message-webgen-0-okBnt"]')
			sleep(1)
			switch_default()
			# 用隐式等待方法等页面出现成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("集中付款-其他支付，作废成功！")
			time.sleep(3)
			
			
			# 测试送审、撤销送审功能----------------------------------------------------------------------------------
			# 切入集中付款窗体
			switch_to("xpath", '//*[@id="massPayment-tab-iframe"]')
			span_click("其他支付")
			sleep(1)
			switch_to("xpath", '//*[@id="subTabFive-iframe"]')
			# 点击刷新，勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
			sleep(1)
			
			span_click("送审")
			sleep(1)
			switch_default()
			
			# 用隐式等待方法等页面出现成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！送审成功1笔，失败0笔。')]")
			print("集中付款-其他支付，送审成功！")
			time.sleep(3)
			
			#测试撤销送审
			# 切入集中付款窗体
			switch_to("xpath", '//*[@id="massPayment-tab-iframe"]')
			span_click("其他支付")
			sleep(1)
			switch_to("xpath", '//*[@id="subTabFive-iframe"]')
			# 点击刷新，勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
			sleep(1)
			
			#点击送审旁边的倒三角
			click("xpath",'/html/body/div[1]/div[3]/div/div[1]/a')
			sleep(1)
			#点击撤销送审
			click("xpath","//a[contains(text(),'撤销送审')]")
			sleep(1)
			# 点击弹出框的OK键
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'撤销送审成功！')]")
			print("集中付款-其他支付，撤销送审成功！")
			time.sleep(3)
			
			# 测试余额检测功能----------------------------------------------------------------------------------
			# 切入集中付款窗体
			switch_to("xpath", '//*[@id="massPayment-tab-iframe"]')
			span_click("其他支付")
			sleep(1)
			switch_to("xpath", '//*[@id="subTabFive-iframe"]')
			# 点击刷新，勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
			
			#点击余额检测
			span_click("余额检测")
			sleep(1)
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'余额充足')]")
			print("集中付款-其他支付，余额检测成功！")
			time.sleep(3)
			
			# 测试确认支付功能----------------------------------------------------------------------------------
			# 切入集中付款窗体
			switch_to("xpath", '//*[@id="massPayment-tab-iframe"]')
			span_click("其他支付")
			sleep(1)
			switch_to("xpath", '//*[@id="subTabFive-iframe"]')
			# 点击刷新，勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
			
			span_click("送审")
			sleep(3)
			double_click("xpath",'//*[@id="grid-body-table"]/tbody/tr[1]/td[3]/div')
			sleep(1)
			switch_to("xpath",'//*[@id="wf_taskProcessing_win-iframe"]')
			span_click("同意")
			sleep(3)
			switch_parent()
			# 点击刷新，勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
			sleep(1)
			span_click("确认支付")
			sleep(1)
			click("xpath",'//*[@id="submit"]/span/span')
			sleep(1)
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！1笔进行了支付，0笔不允许支付。')]")
			print("集中付款-其他支付，确认支付成功！")
			time.sleep(3)
			
			
			# 测试冲正功能----------------------------------------------------------------------------------
			# 切入集中付款窗体
			switch_to("xpath", '//*[@id="massPayment-tab-iframe"]')
			span_click("其他支付")
			sleep(1)
			switch_to("xpath", '//*[@id="subTabFive-iframe"]')
			# 点击刷新，勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
			sleep(1)
			span_click("冲正")
			sleep(1)
			switch_to("xpath",'//*[@id="reverseWin-iframe"]')
			#点击日历旁边的小按钮
			click("xpath",'//*[@id="reversedate-trigger"]')
			sleep(1)
			switch_default()
			#切入日历窗体
			switch_to("xpath", "//iframe[@hidefocus='true']")
			#点击今天
			click("xpath",'//*[@id="dpTodayInput"]')
			switch_default()
			switch_to("xpath", '//*[@id="massPayment-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabFive-iframe"]')
			switch_to("xpath", '//*[@id="reverseWin-iframe"]')
			sleep(1)
			input("xpath",'//*[@id="reversalreason"]','测试冲正')
			sleep(2)
			click("xpath",'//*[@id="iscreatenewtrade"]')
			sleep(1)
			span_click("提交")
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("集中付款-其他支付，冲正成功！")
			time.sleep(3)
			
			
			# 测试上传功能----------------------------------------------------------------------------------
			# 切入集中付款窗体
			switch_to("xpath", '//*[@id="massPayment-tab-iframe"]')
			span_click("其他支付")
			sleep(1)
			switch_to("xpath", '//*[@id="subTabFive-iframe"]')
			
			click("xpath", '//*[@id="gridtitle"]/div[3]/div[2]')
			sleep(1)
			switch_to("xpath", '//*[@id="importDataWin-iframe"]')
			clear("xpath",'//*[@id="combobox-input-businessid"]')
			sleep(1)
			input("xpath", '//*[@id="combobox-input-businessid"]', '集中其它付款导入')
			sleep(2)
			click("xpath", '//*[@id="businessid-combogrid-body-table"]/tbody/tr[1]/td[2]/div')
			sleep(1)
			# 点击下一步
			click("xpath", "//span[text()='下一步']")
			sleep(1)
			switch_to("xpath", '//*[@id="loadNextWin-iframe"]')
			input("xpath", '//*[@id="combobox-input-paytypeid"]', '103-对外付款')
			sleep(2)
			click("xpath", '//*[@id="paytypeid-combogrid-body-table"]/tbody/tr/td[2]/div')
			sleep(1)
			input("xpath", '//*[@id="combobox-input-settlementmodeid"]', '601-其他支付')
			sleep(2)
			click("xpath", '//*[@id="settlementmodeid-combogrid-body-table"]/tbody/tr/td[2]/div')
			sleep(1)
			
			# 附件上传
			upload_click("xpath", "//div[text()='上传文件']/parent::*[1]/descendant::*[4]",
			             'D:\FlieDownload', '"massotherpay1.xls"')
			sleep(3)
			# 点击保存按钮
			click("xpath", "//span[text()='上传']")
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功')]")
			print("付款处理-其他支付，文件上传成功！")
			time.sleep(3)
			
			
			
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("其他支付失败！" + str(traceback.format_exc()))
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