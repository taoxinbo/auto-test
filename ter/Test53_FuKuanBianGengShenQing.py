# encoding=utf-8
# @Time : 2020/11/19 13:30
# @Author : zzg
# 此文件是测试Mysql版本资金结算管理--业务系统对接--付款变更申请
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


class Test53_FuKuanBianGengShenQing(unittest.TestCase):
	
	# 启动浏览器
	def setUp(self):
		# 启动浏览器的另外一个方法：通过封装启动浏览器的驱动，启动不同浏览器
		self.driver = get("chrome")
	
	# 登陆系统、对系统设置进行操作
	def test_trade(self):
		
		# login(G_Ora_Url, mindy, Password, "亚唐科技")
		login(G_Mys_Url, mindy, Password, "亚唐科技")
		
		logging.info("开始测试资金结算管理--业务系统对接--付款变更申请")
		# 将页面的滚动条滑动到‘资金结算管理’页面的地方
		js_gd("xpath", "//span[contains(text(),'资金结算管理')]")
		# 用JS的方法点击资金结算管理菜单按钮
		js_click("xpath", "//span[contains(text(),'资金结算管理')]")
		sleep(1)
		# 点击'外币收付结算'菜单
		click("xpath", "//span[text()='业务系统对接']")
		sleep(1)
		# 点击收款处理菜单
		click("xpath", "//span[text()='付款变更申请']")
		sleep(1)
		# 退出所有iframe窗体
		switch_default()
		try:
			'''
			# 创建快捷集中付款--可操作组织快捷批量付款处理账户💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 收回窗体
			click("xpath", "//span[text()='业务系统对接']")
			sleep(1)
			js_click("xpath", "//span[contains(text(),'资金结算管理')]")
			sleep(1)

			# 将页面的滚动条滑动到‘票据管理’页面的地方
			js_gd("xpath", "//span[contains(text(),'账户资金监控')]")
			# 用JS的方法点击账户资金监控菜单按钮
			js_click("xpath", "//span[contains(text(),'账户资金监控')]")
			sleep(1)
			#点击基础设置
			click("xpath", "//span[contains(text(),'账户生命周期')]")
			sleep(1)
			click("xpath", "//span[text()='账户维护']")
			sleep(1)
			switch_default()

			# 切入单币种账户窗体
			switch_to("xpath", '//*[@id="bankAccounts-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')

			click("xpath", "//span[text()='新增']")
			sleep(1)
			switch_to("xpath", '//*[@id="addWin-iframe"]')

			#账户
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
			click("xpath", "//input[@id='combobox-input-inorout']")
			sleep(1)

			# 输入开户行大连泡崖街支行名称，模糊查询
			input("xpath", "//input[@id='combobox-input-inorout']", "境内")
			sleep(1)
			input_down("xpath", "//input[@id='combobox-input-inorout']")
			input_enter("xpath", "//input[@id='combobox-input-inorout']")

			# 输入银行账号
			input("xpath", '//*[@id="accountnumber"]', '20211053')
			sleep(1)
			input("xpath", '//*[@id="accountname"]', '付款变更申请账户')
			sleep(1)

			# 点击保存按钮
			click("xpath", "//span[text()='保存']")
			sleep(1)

			# 退出所有iframe窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")

			#对账户进行开户
			# 切入窗体
			switch_to("xpath", '//*[@id="bankAccounts-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)

			# 点击查看
			js_click("xpath", "//span[@class='f-contrac-close']")
			sleep(1)
			input("xpath", '//*[@id="accountnumber"]', '20211053')
			sleep(1)
			# 点击查询
			click("xpath", "//span[text()='查询']")
			sleep(1)

			# 勾选数据
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
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

			#日记账金额
			click("xpath", '//*[@id="journalbalance-input"]')
			sleep(1)
			clear("xpath", '//*[@id="journalbalance-input"]')
			sleep(1)
			input("xpath", '//*[@id="journalbalance-input"]', "50000")
			sleep(1)

			click("xpath", "//span[text()='确定']")
			sleep(1)
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			
			#点击账户资金监控，收回窗体
			js_click("xpath", "//span[contains(text(),'账户资金监控')]")
			sleep(1)
			'''
			
			js_gd("xpath", "//span[contains(text(),'资金结算管理')]")
			# 用JS的方法点击资金结算管理菜单按钮
			js_click("xpath", "//span[contains(text(),'资金结算管理')]")
			sleep(1)
			click("xpath", "//span[text()='资金系统收付']")
			sleep(1)
			click("xpath", "//span[text()='付款处理']")
			# 退出所有iframe窗体
			switch_default()
			
			switch_to("xpath", '//*[@id="generalPayment-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			sleep(1)
			# 切入新增窗体
			span_click("新增")
			sleep(1)
			switch_to('xpath', '//*[@id="addWin-iframe"]')
			# 点击对外付款
			input("xpath", '//*[@id="combobox-input-paytypeid"]', "对外付款")
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
			input("xpath", '//*[@id="combobox-input-ourbankaccountid"]', "20211053")
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
			input("xpath", "//input[@id='combobox-input-purpose']", "快捷变更申请数据导入")
			sleep(1)
			# 双击清楚下拉框
			double_click("xpath", "//span[text()='卡折类型']")
			sleep(1)
			
			click("xpath", '//*[@id="save"]/span/span')
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			
			time.sleep(3)
			# 更改数据库单据来源
			sql = "update t_se_payments set RECORDSOURCE = '4' where purpose = '快捷变更申请数据导入'"
			my_sql(my_host, my_port, my_user, my_passwd, my_db,
			        sql)
			
			# 返回快捷付款-付款申请页面
			click("xpath", "//span[text()='资金系统收付']")
			sleep(1)
			click("xpath", "//span[text()='业务系统对接']")
			sleep(1)
			click("xpath", "//span[text()='快捷付款']")
			sleep(1)
			# 点击申请变更功能💨💨💨💨💨💨💨💨💨💨💨💨
			
			# 切入快捷付款-付款申请窗体
			switch_to("xpath", '//*[@id="externalPayments-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			# 刷新、勾选数据
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("审核")
			ok_click()
			sleep(3)
			
			# 刷新、勾选数据
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			span_click("申请变更")
			sleep(1)
			switch_to("xpath", '//*[@id="singleModWin-iframe"]')
			sleep(2)
			input("xpath", '//*[@id="applyreason"]', '测试申请变更')
			sleep(1)
			span_click("下一步")
			sleep(1)
			switch_to("xpath", '//*[@id="updateWin-iframe"]')
			span_click("保存")
			sleep(1)
			# 退出所有窗体
			switch_default()
			span_click("付款变更申请")
		
			# 送审、撤销功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			#切入付款变更申请窗体
			switch_to("xpath",'//*[@id="externalPaymentsUpdate-tab-iframe"]')
			
			#刷新、勾选按钮
			click("xpath",'//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr/td[2]/div')
			sleep(1)
			
			span_click("送审")
			ok_click()
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'成功送审1条记录！')]")
			print("付款变更申请，送审成功")
			time.sleep(3)
			
			# 撤销功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入付款变更申请窗体
			switch_to("xpath", '//*[@id="externalPaymentsUpdate-tab-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr/td[2]/div')
			sleep(1)
			
			triangle_cick_and_element("送审",'撤销送审')
			ok_click()
			
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'成功撤销送审1条记录！')]")
			print("付款变更申请，撤销送审成功")
			time.sleep(3)
			
			# 撤销功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入付款变更申请窗体
			switch_to("xpath", '//*[@id="externalPaymentsUpdate-tab-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr/td[2]/div')
			sleep(1)
			
			span_click("作废")
			ok_click()
			input("xpath",'//*[@id="combobox-input-cancelreason"]','测试作废')
			sleep(1)
			js_click("xpath",'//*[@id="determineCancel"]/span/span')
			sleep(1)
			
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'共1笔，作废成功1笔，失败0笔！')]")
			print("付款变更申请，作废成功")
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
