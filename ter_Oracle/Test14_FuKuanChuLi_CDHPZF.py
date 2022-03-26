# encoding=utf-8
# @Time : 2020/10/15 14:49
# @Author : zzg
# 此文件是测试oracle版本资金结算管理--资金系统收付--付款处理--承兑汇票支付
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
class Test14_FuKuanChuLi_CDHPZF(unittest.TestCase):
	
	# 启动浏览器
	def setUp(self):
		# 启动浏览器的另外一个方法：通过封装启动浏览器的驱动，启动不同浏览器
		self.driver = get("chrome")
	
	# 登陆系统、对系统设置进行操作
	def test_trade(self):
		#=================================================
		login(G_Ora_Url, mindy, Password, "亚唐科技")
		#=================================================

		logging.info("开始测试资金结算管理的页面功能")
		# 将页面的滚动条滑动到‘资金结算管理’页面的地方
		js_gd("xpath", "//span[contains(text(),'资金结算管理')]")
		# 用JS的方法点击资金结算管理菜单按钮
		js_click("xpath", "//span[contains(text(),'资金结算管理')]")
		sleep(1)
		# 点击'资金系统收付'菜单
		click("xpath", "//span[text()='资金系统收付']")
		# 点击付款处理菜单
		click("xpath", "//span[text()='付款处理']")
		# 退出所有iframe窗体
		switch_default()
		sleep(1)
		# 开始测试资金系统收付--付款处理--承兑汇票支付
		# 测试付款处理--承兑汇票支付

		try:

			# 测试新增功能=============================================================================
			for i in range(1,4):
				# 切入‘付款处理’的iframe窗体
				switch_to("xpath", "//iframe[@id='generalPayment-tab-iframe']")
				# 点击承兑汇票支付
				click("xpath", "//span[text()='承兑汇票支付']")
				# 切入‘承兑汇票支付’的iframe窗体
				switch_to("xpath", "//iframe[@id='subTabSix-iframe']")
				sleep(1)
				
				# 用JS的方法点击新增按钮
				js_click("xpath", "//span[text()='新增']")
				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='addWin-iframe']")
				sleep(1)
				# 选择交易类型
				click("xpath", "//input[@id='combobox-input-paytypeid']")
				input("xpath", "//input[@id='combobox-input-paytypeid']", "103-对外付款")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-paytypeid']")
				input_enter("xpath", "//input[@id='combobox-input-paytypeid']")
				time.sleep(1)
				
				# 选择结算方式
				click("xpath", "//input[@id='combobox-input-settlementmodeid']")
				clear("xpath", "//input[@id='combobox-input-settlementmodeid']")
				input("xpath", "//input[@id='combobox-input-settlementmodeid']", "应付承兑汇票出票")
				sleep(1)
				input_enter("xpath", "//input[@id='combobox-input-settlementmodeid']")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-settlementmodeid']")
				sleep(1)
				input_enter("xpath", "//input[@id='combobox-input-settlementmodeid']")
				time.sleep(1)
				
				# 收方名称
				click("xpath", "//input[@id='combobox-input-oppcounterpartyid']")
				sleep(1)
				input("xpath", "//input[@id='combobox-input-oppcounterpartyid']", "浙江华语科技")
				sleep(1)
				
				# 点击消除下拉框
				double_click("xpath", "//span[text()='用途']")
				
				# 输入金额
				input("xpath", "//input[@id='ouramount-input']", "100")
				sleep(1)
				
				# 点击保存
				click("xpath", "//span[text()='保存']")
				
				# 退出所有iframe窗体
				switch_default()
				
				# 用隐式等待方法等页面出现提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				if i == 3 :
					print("承兑汇票支付新增成功")
				sleep(3)
			
			
			#测试修改功能==================================================================================
			# 切入‘付款处理’的iframe窗体
			switch_to("xpath", "//iframe[@id='generalPayment-tab-iframe']")
			# 点击承兑汇票支付
			click("xpath", "//span[text()='承兑汇票支付']")
			sleep(1)
			# 切入‘承兑汇票支付’的iframe窗体
			switch_to("xpath", "//iframe[@id='subTabSix-iframe']")
			
			#勾选按钮
			click("xpath",'//*[@id="gridbar-page-refresh"]')
			click("xpath",'//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			# 点击修改按钮
			click("xpath", "//span[text()='修改']")
			sleep(1)
			# 切入修改的iframe窗体
			switch_to("xpath", "//iframe[@id='modWin-iframe']")
			# 更改用途
			input("xpath", "//input[@id='combobox-input-purpose']", "测试")
			sleep(1)
			
			# 双击消除下拉框
			double_click("xpath", "//span[text()='金额']")
			# 点击保存按钮
			click("xpath", "//span[text()='保存']")
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("付款处理-承兑汇票支付，修改成功！")
			time.sleep(3)
			
			# 测试删除功能======================================================================================
			# 切入‘付款处理’的iframe窗体
			switch_to("xpath", "//iframe[@id='generalPayment-tab-iframe']")
			# 点击承兑汇票支付
			click("xpath", "//span[text()='承兑汇票支付']")
			sleep(1)
			# 切入‘承兑汇票支付’的iframe窗体
			switch_to("xpath", "//iframe[@id='subTabSix-iframe']")
			
			# 勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			# 点击删除按钮
			click("xpath", "//span[text()='删除']")
			# 点击弹出框的OK键
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("付款处理-承兑汇票支付，删除成功！")
			time.sleep(3)
			
			# 测试作废功能====================================================================================
			# 切入‘付款处理’的iframe窗体
			switch_to("xpath", "//iframe[@id='generalPayment-tab-iframe']")
			# 点击承兑汇票支付
			click("xpath", "//span[text()='承兑汇票支付']")
			sleep(1)
			# 切入‘承兑汇票支付’的iframe窗体
			switch_to("xpath", "//iframe[@id='subTabSix-iframe']")
			
			# 勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			#点击作废按钮
			click("xpath","//span[text()='作废']")
			sleep(1)
			click("xpath",'//*[@id="f-message-webgen-0-okBnt"]')
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("付款处理-承兑汇票支付，作废成功！")
			time.sleep(3)
			
			
			#测试送审撤销送审功能============================================================================
			# 切入‘付款处理’的iframe窗体
			switch_to("xpath", "//iframe[@id='generalPayment-tab-iframe']")
			# 点击承兑汇票支付
			click("xpath", "//span[text()='承兑汇票支付']")
			sleep(1)
			# 切入‘承兑汇票支付’的iframe窗体
			switch_to("xpath", "//iframe[@id='subTabSix-iframe']")
			
			# 勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			#勾选送审按钮
			click("xpath", "//span[text()='送审']")
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！送审成功1笔，失败0笔。')]")
			print("付款处理-承兑汇票支付，送审成功！")
			time.sleep(3)
			
			#测试撤销送审功能
			switch_to("xpath", "//iframe[@id='generalPayment-tab-iframe']")
			# 点击承兑汇票支付
			click("xpath", "//span[text()='承兑汇票支付']")
			sleep(1)
			# 切入‘承兑汇票支付’的iframe窗体
			switch_to("xpath", "//iframe[@id='subTabSix-iframe']")
			# 勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
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
			print("付款处理-承兑汇票支付，撤销送审成功！")
			time.sleep(3)
			
			
			#测试审批历史功能============================================================================
			# 切入‘付款处理’的iframe窗体
			switch_to("xpath", "//iframe[@id='generalPayment-tab-iframe']")
			# 点击承兑汇票支付
			click("xpath", "//span[text()='承兑汇票支付']")
			sleep(1)
			# 切入‘承兑汇票支付’的iframe窗体
			switch_to("xpath", "//iframe[@id='subTabSix-iframe']")
			
			# 勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			# 勾选送审按钮
			click("xpath", "//span[text()='审批历史']")
			sleep(3)
			switch_to("xpath",'//*[@id="flowwin-iframe"]')
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
			switch_default()
			time.sleep(3)
			
			
			#测试领票功能===================================================================================
			
			js_click("xpath", "//span[contains(text(),'资金结算管理')]")
			sleep(1)
			js_gd("xpath", "//span[contains(text(),'票据管理')]")
			# 用JS的方法点击票据管理菜单按钮
			js_click("xpath", "//span[contains(text(),'票据管理')]")
			sleep(1)
			# 点击承兑票据管理菜单
			js_click("xpath", "//span[@title='承兑汇票管理']")
			# 点击应收支票登记菜单
			js_click("xpath", "//span[@title='应付票据管理']")
			# 退出所有的iframe窗体
			switch_default()
			
			# 切入‘应付票据管理’的iframe窗体
			switch_to("xpath", "//iframe[@id='payDraftManage-tab-iframe']")
			
			# 用JS的方法点击新增按钮
			js_click("xpath", "//span[text()='新增']")
			
			# 切入新增的iframe窗体
			switch_to("xpath", "//iframe[@id='addWin-iframe']")
			sleep(1)
			
			# 选择票据类型，点击‘票据类型’框
			click("xpath", "//input[@id='combobox-input-drafttype']")
			input("xpath", "//input[@id='combobox-input-drafttype']", "银行承兑汇票")
			sleep(1)
			input_down("xpath", "//input[@id='combobox-input-drafttype']")
			input_enter("xpath", "//input[@id='combobox-input-drafttype']")
			time.sleep(1)
			
			# 设置时间的变成存储，设置唯一性
			temp1 = time.strftime("%H%M%S")
			PJH="YFPJ"+str(temp1)
			# 输入票据号
			click("xpath", "//span[text()='票据号']/ancestor::*[2]/descendant::*[6]/descendant::*[1]")
			sleep(1)
			input("xpath", "//span[text()='票据号']/ancestor::*[2]/descendant::*[6]/descendant::*[1]", PJH)
			sleep(1)
			
			# 选择承兑银行
			input("xpath",'//*[@id="combobox-input-paybankid"]','中国银行')
			click("xpath",'//*[@id="paybankid-combogrid-body-table"]/tbody/tr[1]/td[2]/div')
			time.sleep(1)
			
			#
			# 选择外部收款单位
			input("xpath",'//*[@id="combobox-input-reccounterpartyid"]','浙江华语科技')
			sleep(1)
			#双击清楚下拉框
			double_click("xpath",'//*[@id="bailrate-input"]')
			
			# 输入付款期限
			click("xpath", "//span[@title='付款期限']/ancestor::*[2]/descendant::*[8]")
			sleep(1)
			clear("xpath", "//span[@title='付款期限']/ancestor::*[2]/descendant::*[8]")
			sleep(1)
			input("xpath", "//span[@title='付款期限']/ancestor::*[2]/descendant::*[8]", "60")
			sleep(1)
			
			# 输入票面金额
			click("xpath", "//input[@id='draftamount-input']")
			sleep(1)
			clear("xpath", "//input[@id='draftamount-input']")
			sleep(1)
			input("xpath", "//input[@id='draftamount-input']", "100")
			sleep(1)
			
			# 选择保证金担保方式
			click("xpath", "//input[@id='combobox-input-bailtype']")
			# 输入收票银行账户，模糊查询
			input("xpath", "//input[@id='combobox-input-bailtype']", "票据质押保证")
			sleep(1)
			input_down("xpath", "//input[@id='combobox-input-bailtype']")
			input_enter("xpath", "//input[@id='combobox-input-bailtype']")
			time.sleep(1)
			
			# 点击保存按钮
			click("xpath", "//span[text()='保存']")
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("应付票据管理，保存成功！")
			time.sleep(3)
			
			# 票据审核
			# 切入‘应付票据管理’的iframe窗体
			switch_to("xpath", "//iframe[@id='payDraftManage-tab-iframe']")
			# 勾选
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			click("xpath", "//div[contains(text(),'YFPJ')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")
			# 点击审核按钮
			click("xpath", "//span[text()='审核']")
			# 点击弹出框的OK键
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("应付票据管理，审核成功！")
			time.sleep(3)
			
			#回到承兑汇票页面
			# 将页面的滚动条滑动到‘资金结算管理’页面的地方
			js_gd("xpath", "//span[contains(text(),'资金结算管理')]")
			# 用JS的方法点击资金结算管理菜单按钮
			js_click("xpath", "//span[contains(text(),'资金结算管理')]")
			sleep(1)
			# 点击'资金系统收付'菜单
			js_click("xpath", "//span[text()='资金系统收付']")
			sleep(1)
			# 点击付款处理菜单
			js_click("xpath", "//span[text()='付款处理']")
			# 退出所有iframe窗体
			switch_default()
			
			# 切入‘承兑汇票支付’的iframe窗体
			switch_to("xpath", "//iframe[@id='generalPayment-tab-iframe']")
			# 点击承兑汇票支付
			click("xpath", "//span[text()='承兑汇票支付']")
			sleep(1)
			# 切入‘承兑汇票支付’的iframe窗体
			switch_to("xpath", "//iframe[@id='subTabSix-iframe']")
			
			
			# 勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			click("xpath", "//span[text()='修改']")
			sleep(1)
			# 切入修改的iframe窗体
			switch_to("xpath", "//iframe[@id='modWin-iframe']")
			#修改的地方
			input("xpath",'//*[@id="acceptancedraftcodes"]',PJH)
			# 点击保存按钮
			click("xpath", "//span[text()='保存']")
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			time.sleep(3)
			
			#对单据送审
			switch_to("xpath", "//iframe[@id='generalPayment-tab-iframe']")
			# 点击承兑汇票支付
			click("xpath", "//span[text()='承兑汇票支付']")
			sleep(1)
			# 切入‘承兑汇票支付’的iframe窗体
			switch_to("xpath", "//iframe[@id='subTabSix-iframe']")
			# 勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			# 勾选送审按钮
			click("xpath", "//span[text()='送审']")
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！送审成功1笔，失败0笔。')]")
			time.sleep(3)
			#二次审批
			switch_to("xpath", "//iframe[@id='generalPayment-tab-iframe']")
			# 点击承兑汇票支付
			click("xpath", "//span[text()='承兑汇票支付']")
			sleep(1)
			# 切入‘承兑汇票支付’的iframe窗体
			switch_to("xpath", "//iframe[@id='subTabSix-iframe']")
			double_click("xpath",'//*[@id="grid-body-table"]/tbody/tr[1]/td[3]/div')
			sleep(1)
			switch_to("xpath",'//*[@id="wf_taskProcessing_win-iframe"]')
			click("xpath","//span[text()='同意']")
			sleep(1)
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功')]")
			time.sleep(3)
			
			
			#点击领票/开票按钮
			# 切入‘付款处理’的iframe窗体
			switch_to("xpath", "//iframe[@id='generalPayment-tab-iframe']")
			# 点击承兑汇票支付
			click("xpath", "//span[text()='承兑汇票支付']")
			sleep(1)
			# 切入‘承兑汇票支付’的iframe窗体
			switch_to("xpath", "//iframe[@id='subTabSix-iframe']")
			
			# 勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			click("xpath","//span[text()='领票/开票']")
			sleep(1)
			#切入新增窗体
			switch_to("xpath",'//*[@id="payWin-iframe"]')
			#勾选数据
			click("xpath",'//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
			sleep(1)
			click("xpath","//span[text()='出票']")
			sleep(1)
			switch_to("xpath",'//*[@id="sendWin-iframe"]')
			click("xpath",'//*[@id="save"]/span/span')
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功')]")
			print("应付票据管理，出票成功！")
			time.sleep(3)
			
			
			#测试关联票据查看==================================================================================
			# 切入‘付款处理’的iframe窗体
			switch_to("xpath", "//iframe[@id='generalPayment-tab-iframe']")
			# 点击承兑汇票支付
			click("xpath", "//span[text()='承兑汇票支付']")
			sleep(1)
			# 切入‘承兑汇票支付’的iframe窗体
			switch_to("xpath", "//iframe[@id='subTabSix-iframe']")
			
			# 勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			#勾选关联票据查看
			click("xpath","//span[text()='关联票据查看']")
			sleep(1)
			switch_to("xpath",'//*[@id="draftViewWin-iframe"]')
			implici_wait("xpath", '//*[@id="griduniqueId-body-table"]/tbody/tr/td[3]/div')
			print("应付票据管理，关联票据查看成功！")
			switch_parent()
			click("xpath",'//*[@id="f-win-title-draftViewWin"]/div[1]/div')
			switch_default()
			sleep(3)
			
			
			#测试确认支付=====================================================================================
			# 切入‘付款处理’的iframe窗体
			switch_to("xpath", "//iframe[@id='generalPayment-tab-iframe']")
			# 点击承兑汇票支付
			click("xpath", "//span[text()='承兑汇票支付']")
			sleep(1)
			# 切入‘承兑汇票支付’的iframe窗体
			switch_to("xpath", "//iframe[@id='subTabSix-iframe']")
			
			# 勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			#勾选确认支付按钮
			click("xpath","//span[text()='确认支付']")
			sleep(1)
			click("xpath",'//*[@id="submit"]/span/span')
			
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！1笔进行了确认支付，0笔不允许确认支付。')]")
			print("应付票据管理，确认支付成功！")
			
			# 测试打印=======================================================================================
			# 切入‘付款处理’的iframe窗体
			switch_to("xpath", "//iframe[@id='generalPayment-tab-iframe']")
			# 点击承兑汇票支付
			click("xpath", "//span[text()='承兑汇票支付']")
			sleep(1)
			# 切入‘承兑汇票支付’的iframe窗体
			switch_to("xpath", "//iframe[@id='subTabSix-iframe']")
			
			# 勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			#勾选打印功能
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
					print("承兑汇票支付，打印成功!！")
					time.sleep(3)
					self.driver.switch_to.window(now_handle)
					switch_default()
			
			
			
			# 打印-打印记录====================================================================================
			# 切入‘承兑汇票支付’的iframe窗体
			switch_to("xpath", "//iframe[@id='generalPayment-tab-iframe']")
			# 点击承兑汇票支付
			click("xpath", "//span[text()='承兑汇票支付']")
			sleep(1)
			# 切入‘支票支付’的iframe窗体
			switch_to("xpath", "//iframe[@id='subTabSix-iframe']")
			# 勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			# 用JS方便点击‘支付’按钮旁边的倒三角形
			js_click("xpath", "//span[text()='打印']/parent::*/following-sibling::*/child::*")
			sleep(1)
			
			# 点击打印记录按钮
			js_click("xpath", "//a[contains(text(),'打印记录')]")
			sleep(1)
			
			switch_to("xpath", "//iframe[@id='printWin-iframe']")
			sleep(1)
			
			# 用隐式等待方法等页面出现  操作人:mindy
			implici_wait("xpath", "//div[@title='操作人:mindy']")
			print("承兑汇票支付，打印记录查看成功！")
			time.sleep(3)

			switch_parent()
			
			# 点击关闭页面
			click("xpath", "//span[text()='打印记录']/preceding-sibling::*[1]")
			sleep(1)
			switch_default()

			'''
			#测试确认电子电票支付成功=========================================================================
			#维护电票账户
			js_gd("xpath", "//span[contains(text(),'账户资金监控')]")
			js_click("xpath", "//span[contains(text(),'账户资金监控')]")
			sleep(1)
			# 用JS的方法点击账户资金监控菜单按钮
			#js_click("xpath", "click("xpath", "//span[contains(text(),'账户生命周期')]")")
			sleep(1)
			click("xpath", "//span[@title='账户生命周期']")
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
			
			# # 选择银企直联户isbankdirect
			click("xpath", "//input[@id='isbankdirect']")
			sleep(1)
			# 选择电票直联权限
			click("xpath",'//*[@id="combobox-input-directrightrange"]')
			sleep(1)
			click("xpath",'//*[@id="f-combo-directrightrange-list-0"]/div[1]')
			sleep(1)
			click("xpath",'//*[@id="combobox-input-directrightrange"]')
			sleep(1)
			click("xpath", "//input[@id='combobox-input-inorout']")
			# 输入开户行大连泡崖街支行名称，模糊查询
			input("xpath", "//input[@id='combobox-input-inorout']", "境内")
			sleep(1)
			input_down("xpath", "//input[@id='combobox-input-inorout']")
			input_enter("xpath", "//input[@id='combobox-input-inorout']")
			# 输入银行账号
			input("xpath", '//*[@id="accountnumber"]', '20211014')
			sleep(1)
			input("xpath", '//*[@id="accountname"]', '测试电子承兑汇票付款账户')
			
			# 点击保存按钮
			click("xpath", "//span[text()='保存']")
			# 退出所有iframe窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'成功')]")
			print("电子承兑汇票支付账户创建成功")
			# 对账户进行开户
			# 切入窗体
			switch_to("xpath", '//*[@id="bankAccounts-tab-iframe"]')
			sleep(1)
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')

			# 点击查询放大镜
			js_click("xpath", "//span[@class='f-contrac-close']")
			sleep(1)
			# 输入账户，进行查询
			input("xpath", '//*[@id="accountnumber"]', '20211014')
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
			click("xpath", "//span[@title='日记账余额']")
			sleep(1)
			click("xpath", '//*[@id="journalbalance-input"]')
			sleep(1)
			clear("xpath", '//*[@id="journalbalance-input"]')
			sleep(1)
			input("xpath", '//*[@id="journalbalance-input"]', "5000")
			sleep(1)

			# 到期日期
			today = date.today()
			open_date = today + timedelta(days=800)
			click("xpath", "//input[@id='accountdatedue-input']")
			sleep(1)
			clear("xpath", "//input[@id='accountdatedue-input']")
			sleep(1)
			input("xpath", "//input[@id='accountdatedue-input']", str(open_date))
			time.sleep(1)

			click("xpath", "//span[text()='确定']")
			sleep(1)

			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("电子承兑汇票支付账户开户成功")

			js_click("xpath", "//span[contains(text(),'账户资金监控')]")
			sleep(1)

			# 维护融资产品=============================
			#进入融资管理设置，点击融资管理实际上融资管理按钮会网上滚，变为不可见，
			# 尝试用click函数实施
			js_gd("xpath", "//span[contains(text(),'融资管理')]")
			sleep(1)
			# 用JS的方法点击融资管理菜单按钮
			js_click("xpath", "//span[contains(text(),'融资管理')]")
			sleep(1)
			js_gd("xpath", "//span[contains(text(),'资金往来调拨')]")
			sleep(1)
			#点击基础设置
			click("xpath", "//li[@f_value='loanSetting']/descendant-or-self::*[5]")
			sleep(1)
			js_click("xpath", "//span[contains(text(),'融资产品')]")
			switch_default()
			
			#切入窗体
			switch_to("xpath",'//*[@id="products-tab-iframe"]')
			#查询112的融资产品
			js_click("xpath",'//*[@id="north"]/div[2]/span')
			sleep(3)
			input("xpath",'//*[@id="code"]','112')
			sleep(1)
			click("xpath",'//*[@id="buttonlist_searchlist"]/div[1]/div/span')
			sleep(1)
			#勾选数据
			click("xpath",'//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
			#点击设置使用范围
			click("xpath", "//span[contains(text(),'设置适用范围')]")
			sleep(1)
			switch_to("xpath",'//*[@id="setscopeWin-iframe"]')
			switch_to("xpath",'//*[@id="subTab-iframe"]')
			#点击查询
			js_click("xpath",'//*[@id="north"]/div[2]/span')
			sleep(1)
			input("xpath",'//*[@id="name"]','电子票据')
			sleep(2)
			click("xpath", "//span[contains(text(),'查询')]")
			sleep(1)
			click("xpath",'//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
			sleep(1)
			click("xpath", "//span[contains(text(),'分配')]")
			switch_to("xpath",'//*[@id="distributeWin-iframe"]')
			#选择全部
			click('xpath','//*[@id="editgrid-distributefldvalue-h"]/div/div[1]/span')
			click("xpath",'//*[@id="roleassignformid"]/div[2]/div[4]/div[3]/div[1]')
			sleep(1)
			#保存
			click("xpath",'//*[@id="save"]/span/span')
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			
			#切入承兑汇票支付页面
			
			js_gd("xpath", "//span[contains(text(),'资金结算管理')]")
			# 用JS的方法点击资金结算管理菜单按钮
			js_click("xpath", "//span[contains(text(),'资金结算管理')]")
			sleep(1)
			# 点击'资金系统收付'菜单
			js_click("xpath", "//span[text()='资金系统收付']")
			sleep(1)
			# 点击付款处理菜单
			click("xpath", "//span[text()='付款处理']")
			# 退出所有iframe窗体
			switch_default()
			'''
			#做一笔数据用于测试==========================================================================
			# 切入‘付款处理’的iframe窗体
			switch_to("xpath", "//iframe[@id='generalPayment-tab-iframe']")
			# 点击承兑汇票支付
			click("xpath", "//span[text()='承兑汇票支付']")
			# 切入‘承兑汇票支付’的iframe窗体
			switch_to("xpath", "//iframe[@id='subTabSix-iframe']")
			sleep(1)
			
			# 用JS的方法点击新增按钮
			js_click("xpath", "//span[text()='新增']")
			# 切入新增的iframe窗体
			switch_to("xpath", "//iframe[@id='addWin-iframe']")
			sleep(1)
			# 选择交易类型
			click("xpath", "//input[@id='combobox-input-paytypeid']")
			input("xpath", "//input[@id='combobox-input-paytypeid']", "103-对外付款")
			sleep(1)
			input_down("xpath", "//input[@id='combobox-input-paytypeid']")
			input_enter("xpath", "//input[@id='combobox-input-paytypeid']")
			time.sleep(1)
			
			#选择结算方式
			input("xpath",'//*[@id="combobox-input-settlementmodeid"]','208-电子商业汇票出票')
			sleep(2)
			click("xpath",'//*[@id="settlementmodeid-combogrid-body-table"]/tbody/tr/td[2]/div')
			sleep(1)
			
			#选择付方账户
			input("xpath",'//*[@id="combobox-input-ourbankaccountid"]','20211014')
			sleep(2)
			click("xpath",'//*[@id="ourbankaccountid-combogrid-body-table"]/tbody/tr/td[2]/div')
			sleep(1)
			
			#填写收方名称
			input("xpath",'//*[@id="combobox-input-oppcounterpartyid"]','浙江华语科技')
			sleep(2)
			double_click("xpath",'//*[@id="combobox-input-oppcardtype"]')
			sleep(1)
			
			#填写收方账户
			input("xpath",'//*[@id="combobox-input-oppcounterpartyaccountid"]','200848782767819')
			sleep(2)
			double_click("xpath", '//*[@id="combobox-input-oppcardtype"]')
			sleep(1)
			
			#填写收方户名
			clear("xpath",'//*[@id="oppbankaccountname"]')
			input("xpath", '//*[@id="oppbankaccountname"]', '浙江华语科技')
			sleep(2)
			double_click("xpath", '//*[@id="combobox-input-oppcardtype"]')
			sleep(1)
			
			#填写收方开户银行
			click("xpath",'//*[@id="combobox-input-oppbanklocationid"]')
			sleep(1)
			click("xpath",'//*[@id="oppbanklocationid-combogrid-body-table"]/tbody/tr[1]/td[2]/div')
			sleep(1)
			
			#填写金额
			input("xpath",'//*[@id="ouramount-input"]','100')
			sleep(2)
			
			# 点击保存
			click("xpath", "//span[text()='保存']")
			
			# 退出所有iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			#对单据送审
			switch_to("xpath", "//iframe[@id='generalPayment-tab-iframe']")
			# 点击承兑汇票支付
			click("xpath", "//span[text()='承兑汇票支付']")
			sleep(1)
			# 切入‘承兑汇票支付’的iframe窗体
			switch_to("xpath", "//iframe[@id='subTabSix-iframe']")
			# 勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			# 勾选送审按钮
			click("xpath", "//span[text()='送审']")
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！送审成功1笔，失败0笔。')]")
			time.sleep(3)
			# 二次审批
			switch_to("xpath", "//iframe[@id='generalPayment-tab-iframe']")
			# 点击承兑汇票支付
			click("xpath", "//span[text()='承兑汇票支付']")
			sleep(1)
			# 切入‘承兑汇票支付’的iframe窗体
			switch_to("xpath", "//iframe[@id='subTabSix-iframe']")
			double_click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[3]/div')
			sleep(1)
			switch_to("xpath", '//*[@id="wf_taskProcessing_win-iframe"]')
			click("xpath", "//span[text()='同意']")
			sleep(1)
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功')]")
			time.sleep(3)
			
			#点击领票
			# 切入‘付款处理’的iframe窗体
			switch_to("xpath", "//iframe[@id='generalPayment-tab-iframe']")
			# 点击承兑汇票支付
			click("xpath", "//span[text()='承兑汇票支付']")
			sleep(1)
			# 切入‘承兑汇票支付’的iframe窗体
			switch_to("xpath", "//iframe[@id='subTabSix-iframe']")
			
			# 勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			click("xpath", "//span[text()='领票/开票']")
			sleep(1)
			# 切入新增窗体
			switch_to("xpath",'//*[@id="payWin-iframe"]')
			#选择交易类型
			input("xpath",'//*[@id="combobox-input-productid"]','112-电子银行承兑汇票')
			sleep(2)
			click("xpath",'//*[@id="productid-combogrid-body-table"]/tbody/tr/td[2]/div')
			sleep(1)
			
			#选择承兑人开户银行
			click('xpath','//*[@id="combobox-input-acceptorbanklocationid"]')
			sleep(1)
			input_down("xpath",'//*[@id="combobox-input-acceptorbanklocationid"]')
			input_enter("xpath", '//*[@id="combobox-input-acceptorbanklocationid"]')
			sleep(1)
			
			#勾选票据到期日
			click("xpath",'//*[@id="onemonth"]')
			sleep(1)
			
			#选择保证金担保方式
			input("xpath",'//*[@id="combobox-input-bailtype"]','票据质押保证')
			sleep(2)
			click("xpath",'//*[@id="f-combo-bailtype-list-0"]')
			sleep(1)
			
			#点击出票
			click("xpath",'//*[@id="save"]/span/span')
			sleep(1)
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功')]")
			
			#点击确认支付
			switch_to("xpath", "//iframe[@id='generalPayment-tab-iframe']")
			# 点击承兑汇票支付
			click("xpath", "//span[text()='承兑汇票支付']")
			sleep(1)
			# 切入‘承兑汇票支付’的iframe窗体
			switch_to("xpath", "//iframe[@id='subTabSix-iframe']")
			# 勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			# 勾选确认支付按钮
			click("xpath", "//span[text()='确认支付']")
			sleep(1)
			click("xpath", '//*[@id="submit"]/span/span')
			
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！1笔进行了确认支付，0笔不允许确认支付。')]")
			sleep(3)
			
			#点击确认电票支付
			switch_to("xpath", "//iframe[@id='generalPayment-tab-iframe']")
			# 点击承兑汇票支付
			click("xpath", "//span[text()='承兑汇票支付']")
			sleep(1)
			# 切入‘承兑汇票支付’的iframe窗体
			switch_to("xpath", "//iframe[@id='subTabSix-iframe']")
			# 勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			click("xpath","//span[text()='确认电票支付成功']")
			sleep(1)
			click("xpath",'//*[@id="f-message-webgen-0-okBnt"]')
			sleep(1)
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'共1笔，处理成功1笔，失败0笔。')]")
			print("承兑汇票支付，确认电票支付成功")
			
			#TODO 批量背书申请需要操纵电票系统，故不实现自动化============================================
			#TODO 拆分手工测试，因为拆分时每次生成的单据号不一样，但是如果数据库直接改单据号，还是有问题======================
			
			
			
			
			
			
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("承兑汇票支付失败！" + str(traceback.format_exc()))
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
