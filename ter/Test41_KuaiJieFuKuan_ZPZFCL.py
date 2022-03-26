# encoding=utf-8
# @Time : 2020/11/12 08:30
# @Author : zzg
# 此文件是测试MySQL版本资金结算管理--业务系统对接--快捷付款--支票付款处理
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


class Test41_KuaiJieFuKuan_ZPZFCL(unittest.TestCase):
	
	# 启动浏览器
	def setUp(self):
		# 启动浏览器的另外一个方法：通过封装启动浏览器的驱动，启动不同浏览器
		self.driver = get("chrome")
	
	# 登陆系统、对系统设置进行操作
	def test_trade(self):
		
		# login(G_Ora_Url, mindy, Password, "亚唐科技")
		login(G_Mys_Url, mindy, Password, "亚唐科技")
		
		logging.info("开始测试资金结算管理--业务系统对接--快捷付款--支票付款处理")
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
			
			# 去支票支付页面做数据💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 收回窗体
			click("xpath", "//span[text()='业务系统对接']")
			sleep(1)
			span_click("资金系统收付")
			sleep(1)
			span_click("付款处理")
			#进入支票支付页面
			switch_to("xpath", "//iframe[@id='generalPayment-tab-iframe']")
			# 点击支票支付
			click("xpath", "//span[text()='支票支付']")
			sleep(1)
			# 切入支票支付窗体
			switch_to("xpath", "//iframe[@id='subTabFive-iframe']")
			
			# 点击新增
			click("xpath", "//span[text()='新增']")
			# 切入新增的iframe窗体
			switch_to("xpath", "//iframe[@id='addWin-iframe']")
			
			# 输入交易类型
			input("xpath", "//input[@id='combobox-input-paytypeid']", "103-对外付款")
			sleep(2)
			input_down("xpath", "//input[@id='combobox-input-paytypeid']")
			sleep(1)
			input_enter("xpath", "//input[@id='combobox-input-paytypeid']")
			time.sleep(1)
			
			# 选择结算方式
			click("xpath", "//input[@id='combobox-input-settlementmodeid']")
			clear("xpath", "//input[@id='combobox-input-settlementmodeid']")
			sleep(1)
			# 输入开户行大连泡崖街支行名称，模糊查询
			input("xpath", "//input[@id='combobox-input-settlementmodeid']", "403-现金/转账支票支付")
			sleep(1)
			input_down("xpath", "//input[@id='combobox-input-settlementmodeid']")
			input_enter("xpath", "//input[@id='combobox-input-settlementmodeid']")
			time.sleep(1)
			
			# 付方账户
			click("xpath", "//input[@id='combobox-input-ourbankaccountid']")
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
			input("xpath", "//input[@id='combobox-input-purpose']", "快捷付款支票支付处理数据导入")
			sleep(1)
			
			# 点击保存按钮
			click("xpath", "//span[text()='保存']")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			time.sleep(3)

			#票据管理页面做数据
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
			
			# 切入新增的iframe窗体
			switch_to("xpath", "//iframe[@id='addWin-iframe']")
			sleep(1)
			
			click("xpath", "//input[@id='combobox-input-booktype']")
			# 模糊匹配搜索
			input("xpath", "//input[@id='combobox-input-booktype']", "现金/转账")
			sleep(1)
			up_enter_click("//input[@id='combobox-input-booktype']")
			
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
			up_enter_click("//input[@id='combobox-input-accountid']")
			
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
			# 更改数据
			sql = "update t_se_payments set RECORDSOURCE = '4' where purpose like '%快捷付款支票支付处理数据导入%'"
			my_sql(my_host, my_port, my_user, my_passwd, my_db,
			       sql)
			sql2 = "update t_se_payments set APPROVESTATE = '2' where purpose like '%快捷付款支票支付处理数据导入%'"
			my_sql(my_host, my_port, my_user, my_passwd, my_db,
			       sql2)
			#返回快捷付款-支票支付处理页面
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
			
			# 测试领用功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			#进入支票支付处理页面
			switch_to("xpath",'//*[@id="externalPayments-tab-iframe"]')
			span_click("支票付款处理")
			sleep(1)
			switch_to("xpath",'//*[@id="subTabSix-iframe"]')
			#勾选
			click("xpath",'//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			span_click("领用")
			switch_to("xpath",'//*[@id="chequerecipientsWin-iframe"]')
			#勾选数据
			click("xpath",'//*[@id="grid-body-table"]/tbody/tr[1]/td[2]')
			sleep(1)
			span_click("下一步")
			switch_to("xpath",'//*[@id="applyWin-iframe"]')
			#领用人
			input("xpath",'//*[@id="username"]','张中国')
			sleep(1)
			#领用用途
			click("xpath",'//*[@id="combobox-input-chequepurposeid"]')
			sleep(1)
			up_enter_click('//*[@id="combobox-input-chequepurposeid"]')
			
			span_click("领用")
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'领用成功！')]")
			print("快捷付款-支票支付处理，领用成功")
			
			
			
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
