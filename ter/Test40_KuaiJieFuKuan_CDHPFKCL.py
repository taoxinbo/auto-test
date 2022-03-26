# encoding=utf-8
# @Time : 2020/11/11 08:30
# @Author : zzg
# 此文件是测试MySQL版本资金结算管理--业务系统对接--快捷付款--承兑汇票付款
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


class Test40_KuaiJieFuKuan_CDHPFKCL(unittest.TestCase):
	
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
			
			# 去承兑汇票支付页面做数据💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 收回窗体
			click("xpath", "//span[text()='业务系统对接']")
			sleep(1)
			span_click("资金系统收付")
			sleep(1)
			span_click("付款处理")
			
			for i in range(1, 3):
				# 切入‘付款处理’的iframe窗体
				switch_to("xpath", "//iframe[@id='generalPayment-tab-iframe']")
				click("xpath", "//span[text()='承兑汇票支付']")
				switch_to("xpath", "//iframe[@id='subTabSix-iframe']")
				sleep(1)
				# 用JS的方法点击新增按钮
				js_click("xpath", "//span[text()='新增']")
				sleep(1)
				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='addWin-iframe']")
				if i==1 :
					global PJH1
					# 选择交易类型
					input("xpath", "//input[@id='combobox-input-paytypeid']", "103-对外付款")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-paytypeid']")
					input_enter("xpath", "//input[@id='combobox-input-paytypeid']")
					time.sleep(1)
					
					# 选择结算方式
					input("xpath", "//input[@id='combobox-input-settlementmodeid']", "应付承兑汇票出票")
					sleep(1)
					up_enter_click("//input[@id='combobox-input-settlementmodeid']")
					
					#票据号
					PJH1 = time.strftime("%Y%m%d%H%M%S")
					input("xpath",'//*[@id="acceptancedraftcodes"]',PJH1)
					sleep(1)
					
					# 收方组织
					click("xpath", "//input[@id='combobox-input-oppcounterpartyid']")
					sleep(1)
					input("xpath", "//input[@id='combobox-input-oppcounterpartyid']", "浙江华语科技")
					sleep(1)
					
					# 点击消除下拉框
					double_click("xpath", "//span[text()='用途']")
					sleep(1)
					# 输入金额
					input("xpath", "//input[@id='ouramount-input']", "100")
					sleep(1)
					#输入用途
					input("xpath",'//*[@id="combobox-input-purpose"]','快捷付款承兑汇票付款数据导入')
					sleep(1)
					# 点击保存
					click("xpath", "//span[text()='保存']")
					sleep(1)
					# 退出所有iframe窗体
					switch_default()
					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					sleep(3)
				if i ==2 :
					# 选择交易类型
					click("xpath", "//input[@id='combobox-input-paytypeid']")
					input("xpath", "//input[@id='combobox-input-paytypeid']", "103-对外付款")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-paytypeid']")
					input_enter("xpath", "//input[@id='combobox-input-paytypeid']")
					time.sleep(1)
					
					# 选择结算方式
					input("xpath", '//*[@id="combobox-input-settlementmodeid"]', '208-电子商业汇票出票')
					sleep(2)
					click("xpath", '//*[@id="settlementmodeid-combogrid-body-table"]/tbody/tr/td[2]/div')
					sleep(1)
					
					# 选择付方账户
					input("xpath", '//*[@id="combobox-input-ourbankaccountid"]', '20211014')
					sleep(2)
					click("xpath", '//*[@id="ourbankaccountid-combogrid-body-table"]/tbody/tr/td[2]/div')
					sleep(1)
					
					# 填写收方名称
					input("xpath", '//*[@id="combobox-input-oppcounterpartyid"]', '浙江华语科技')
					sleep(2)
					double_click("xpath", '//*[@id="combobox-input-oppcardtype"]')
					sleep(1)
					
					# 填写收方账户
					input("xpath", '//*[@id="combobox-input-oppcounterpartyaccountid"]', '200848782767819')
					sleep(2)
					double_click("xpath", '//*[@id="combobox-input-oppcardtype"]')
					sleep(1)
					
					# 填写收方户名
					clear("xpath", '//*[@id="oppbankaccountname"]')
					input("xpath", '//*[@id="oppbankaccountname"]', '浙江华语科技')
					sleep(2)
					double_click("xpath", '//*[@id="combobox-input-oppcardtype"]')
					sleep(1)
					
					# 填写收方开户银行
					click("xpath", '//*[@id="combobox-input-oppbanklocationid"]')
					sleep(1)
					click("xpath", '//*[@id="oppbanklocationid-combogrid-body-table"]/tbody/tr[1]/td[2]/div')
					sleep(1)
					
					# 填写金额
					input("xpath", '//*[@id="ouramount-input"]', '100')
					sleep(2)
					
					# 输入用途
					input("xpath", '//*[@id="combobox-input-purpose"]', '快捷付款承兑汇票付款数据导入')
					sleep(1)
					
					# 点击保存
					click("xpath", "//span[text()='保存']")
					sleep(1)
					# 退出所有iframe窗体
					switch_default()
					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			#更改数据
			sql = "update t_se_payments set RECORDSOURCE = '4' where purpose like '%快捷付款承兑汇票付款数据导入%'"
			my_sql(my_host, my_port, my_user, my_passwd, my_db,
			       sql)
			sql2 = "update t_se_payments set APPROVESTATE = '2' where purpose like '%快捷付款承兑汇票付款数据导入%'"
			my_sql(my_host, my_port, my_user, my_passwd, my_db,
			       sql2)
			#去承兑汇票页面做数据
			#拉回窗体
			js_click("xpath", "//span[contains(text(),'资金系统收付')]")
			sleep(1)
			js_click("xpath", "//span[contains(text(),'资金结算管理')]")
			sleep(1)
			
			js_gd("xpath", "//span[contains(text(),'票据管理')]")
			# 用JS的方法点击票据管理菜单按钮
			js_click("xpath", "//span[contains(text(),'票据管理')]")
			sleep(1)
			# 点击承兑票据管理菜单
			js_click("xpath", "//span[@title='承兑汇票管理']")
			# 点击应付支票登记菜单
			js_click("xpath", "//span[@title='应付票据管理']")
			# 退出所有的iframe窗体
			switch_default()
			
			# 切入‘应付票据管理’的iframe窗体
			switch_to("xpath", "//iframe[@id='payDraftManage-tab-iframe']")
			
			# 用JS的方法点击新增按钮
			js_click("xpath", "//span[text()='新增']")
			sleep(1)
			# 切入新增的iframe窗体
			switch_to("xpath", "//iframe[@id='addWin-iframe']")
			# 选择票据类型，点击‘票据类型’框
			click("xpath", "//input[@id='combobox-input-drafttype']")
			input("xpath", "//input[@id='combobox-input-drafttype']", "银行承兑汇票")
			sleep(1)
			input_down("xpath", "//input[@id='combobox-input-drafttype']")
			input_enter("xpath", "//input[@id='combobox-input-drafttype']")
			time.sleep(1)
			
			
			# 输入票据号
			input("xpath", "//span[text()='票据号']/ancestor::*[2]/descendant::*[6]/descendant::*[1]", PJH1)
			sleep(1)
			
			# 选择承兑银行
			input("xpath", '//*[@id="combobox-input-paybankid"]', '中国银行')
			click("xpath", '//*[@id="paybankid-combogrid-body-table"]/tbody/tr[1]/td[2]/div')
			time.sleep(1)
			
			#
			# 选择外部收款单位
			input("xpath", '//*[@id="combobox-input-reccounterpartyid"]', '浙江华语科技')
			sleep(1)
			# 双击清楚下拉框
			double_click("xpath", '//*[@id="bailrate-input"]')
			
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
			time.sleep(3)
			
			# 票据审核
			# 切入‘应付票据管理’的iframe窗体
			switch_to("xpath", "//iframe[@id='payDraftManage-tab-iframe']")
			# 勾选
			click("xpath",'//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			# 点击审核按钮
			click("xpath", "//span[text()='审核']")
			sleep(1)
			# 点击弹出框的OK键
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			time.sleep(3)
			
			#回到快捷付款-承兑汇票处理页面
			js_click("xpath", "//span[contains(text(),'票据管理')]")
			sleep(1)
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
			
			# 领票/开票功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			#切入承兑汇票付款处理页面
			switch_to("xpath",'//*[@id="externalPayments-tab-iframe"]')
			span_click("承兑汇票付款处理")
			sleep(1)
			switch_to("xpath",'//*[@id="subTabFive-iframe"]')
			
			#刷新、勾选按钮
			click("xpath",'//*[@id="gridbar-page-refresh"]')
			sleep(2)
			click("xpath",'//*[@id="grid-body-table"]/tbody/tr[2]/td[2]/div/button')
			sleep(1)
			
			span_click("领票/开票")
			switch_to("xpath",'//*[@id="payWin-iframe"]')
			click("xpath",'//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
			sleep(1)
			click("xpath", "//span[text()='出票']")
			sleep(1)
			# 切入新增窗体
			switch_to("xpath", '//*[@id="sendWin-iframe"]')
			click("xpath", '//*[@id="save"]/span/span')
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功')]")
			print("应付票据管理，出票成功！")
			time.sleep(3)
			
			# 支付功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入承兑汇票付款处理页面
			switch_to("xpath", '//*[@id="externalPayments-tab-iframe"]')
			span_click("承兑汇票付款处理")
			sleep(1)
			switch_to("xpath", '//*[@id="subTabFive-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(2)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[2]/td[2]/div/button')
			sleep(1)
			
			span_click("支付")
			span_click("确定")
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！1笔进行了支付，0笔不允许支付。')]")
			print("承兑汇票付款处理，支付成功")
			time.sleep(3)
			
			# 电票支付成功功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入承兑汇票付款处理页面
			switch_to("xpath", '//*[@id="externalPayments-tab-iframe"]')
			span_click("承兑汇票付款处理")
			sleep(1)
			switch_to("xpath", '//*[@id="subTabFive-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(2)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]')
			sleep(1)
			
			span_click("领票/开票")
			switch_to("xpath",'//*[@id="payWin-iframe"]')
			#票据类型
			input("xpath",'//*[@id="combobox-input-productid"]','109-银行承兑汇票')
			sleep(1)
			up_enter_click('//*[@id="combobox-input-productid"]')
			
			#承兑人开户银行
			input("xpath", '//*[@id="combobox-input-acceptorbanklocationid"]', '104222000965-中国银行股份有限公司大连泡崖街支行')
			sleep(1)
			up_enter_click('//*[@id="combobox-input-acceptorbanklocationid"]')
			
			# 票据质押保证金
			input("xpath", '//*[@id="combobox-input-bailtype"]', '票据质押保证')
			sleep(1)
			up_enter_click('//*[@id="combobox-input-bailtype"]')
			
			# 承兑人全称
			input("xpath", '//*[@id="acceptor"]', '华语科技')
			sleep(1)
			
			# 勾选票据到期日
			click("xpath", '//*[@id="onemonth"]')
			sleep(1)
			
			span_click("出票")
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			time.sleep(3)
			
			# 切入承兑汇票付款处理页面
			switch_to("xpath", '//*[@id="externalPayments-tab-iframe"]')
			span_click("承兑汇票付款处理")
			sleep(1)
			switch_to("xpath", '//*[@id="subTabFive-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(2)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]')
			sleep(1)
			
			span_click("支付")
			span_click("确定")
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(2)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]')
			sleep(1)
			
			span_click("确认电票支付成功")
			ok_click()
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'共1笔，处理成功1笔，失败0笔。')]")
			print("承兑汇票付款处理，确认电票支付成功")
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
