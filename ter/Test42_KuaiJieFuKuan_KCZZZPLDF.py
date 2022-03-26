# encoding=utf-8
# @Time : 2020/11/12 08:30
# @Author : zzg
# 此文件是测试Oracle版本资金结算管理--业务系统对接--快捷付款--可操作组织批量代付处理
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


class Test42_KuaiJieFuKuan_KCZZZPLDF(unittest.TestCase):
	
	# 启动浏览器
	def setUp(self):
		# 启动浏览器的另外一个方法：通过封装启动浏览器的驱动，启动不同浏览器
		self.driver = get("chrome")
	
	# 登陆系统、对系统设置进行操作
	def test_trade(self):
		
		# login(G_Ora_Url, mindy, Password, "亚唐科技")
		login(G_Mys_Url, mindy, Password, "亚唐科技")
		
		logging.info("开始测试资金结算管理--业务系统对接--快捷付款--可操作组织批量代付处理")
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
			'''
			# 创建可操作组织直联批量付款账户
			# 点击资金系统收付收回窗体💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			click("xpath", "//span[text()='业务系统对接']")
			sleep(1)
			js_click("xpath", "//span[contains(text(),'资金结算管理')]")
			sleep(1)


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
			sleep(1)
			switch_to("xpath", '//*[@id="addWin-iframe"]')
			click("xpath", "//input[@id='combobox-input-bankid']")
			sleep(1)
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

			click("xpath", "//input[@id='combobox-input-inorout']")
			# 输入开户行大连泡崖街支行名称，模糊查询
			input("xpath", "//input[@id='combobox-input-inorout']", "境内")
			sleep(1)
			input_down("xpath", "//input[@id='combobox-input-inorout']")
			input_enter("xpath", "//input[@id='combobox-input-inorout']")
			sleep(1)
			# 输入银行账号
			input("xpath", '//*[@id="accountnumber"]', '20211042')
			sleep(1)
			input("xpath", '//*[@id="accountname"]', '快捷付款-可操作组织批量代付处理')
			sleep(1)
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
			input("xpath", '//*[@id="accountnumber"]', '20211042')
			sleep(1)
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
			# 点击账户资金监控缩回页面
			js_click("xpath", "//span[contains(text(),'账户资金监控')]")
			sleep(1)

			# 开始创建直联批量付款的交易类型以及结算方式💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
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
			input("xpath", "//input[@name='code']", "2042")
			sleep(1)

			# 输入结算方式
			input("xpath", "//input[@id='name']", "快捷付款可操作组织批量处理")
			sleep(1)

			# 输入交易方向
			click("xpath", "//input[@id='combobox-input-moneyway']")
			sleep(1)
			input("xpath", "//input[@id='combobox-input-moneyway']", "支出")
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
			input("xpath", '//*[@id="combobox-input-editgrid-bankid-0"]', 'BOC-中国银行')
			click('xpath', '//*[@id="editgrid-bankid-0-combogrid-body-table"]/tbody/tr/td[2]/div')
			sleep(1)
			input('xpath', '//*[@id="combobox-input-editgrid-settlementscenarios-0"]', '代发代扣默认')
			click('xpath', '//*[@id="f-combo-editgrid-settlementscenarios-0-list-0"]')
			sleep(1)
			click('xpath', '//*[@id="combobox-input-editgrid-directchannelid-0"]')
			click('xpath', '//*[@id="editgrid-directchannelid-0-combogrid-body-table"]/tbody/tr[1]/td[2]/div')
			sleep(1)
			input('xpath', '//*[@id="combobox-input-editgrid-directchannelcmdid-0"]', '批量代付')
			click('xpath', '//*[@id="editgrid-directchannelcmdid-0-combogrid-body-table"]/tbody/tr[1]/td[2]/div')
			sleep(1)
			click('xpath', '//*[@id="combobox-input-editgrid-directinterbanksystemid-0"]')
			click('xpath', '//*[@id="editgrid-directinterbanksystemid-0-combogrid-body-table"]/tbody/tr[1]/td[2]/div')
			sleep(1)
			# 点击保存按钮
			click("xpath", "//span[text()='保存']")
			# 退出所有iframe窗体
			switch_default()

			# 创建直联批量付款的交易类型
			click("xpath", "//span[text()='交易类型']")
			switch_to('xpath', '//*[@id="payType-tab-iframe"]')
			js_click("xpath", "//span[text()='新增']")
			# 切入新增的iframe窗体
			switch_to("xpath", "//iframe[@id='addWin-iframe']")
			sleep(1)

			# 输入代码
			input("xpath", "//input[@id='code']", "3042")
			sleep(1)

			# 输入名称
			input("xpath", "//input[@id='name']", "快捷付款可操作组织付款交易类型")
			sleep(1)

			# 交易方向
			click("xpath", "//input[@id='combobox-input-moneyway']")
			sleep(1)
			input("xpath", "//input[@id='combobox-input-moneyway']", "支出")
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
			input("xpath", "//input[@id='combobox-input-settlementmoderange']", '2042-快捷付款可操作组织批量处理')
			sleep(1)
			click("xpath", '//*[@id="settlementmoderange-combogrid-body-table"]/tbody/tr/td[2]/div/button')
			sleep(1)
			input("xpath", "//input[@id='combobox-input-settlementmoderange']", '601')
			sleep(1)
			click("xpath", '//*[@id="settlementmoderange-combogrid-body-table"]/tbody/tr/td[2]/div/button')
			sleep(1)

			# 默认结算方式
			click("xpath", "//input[@id='combobox-input-defaultsettlementmodeid']")
			sleep(1)
			input("xpath", "//input[@id='combobox-input-defaultsettlementmodeid']",'2042-快捷付款可操作组织批量处理')
			sleep(1)
			input_down("xpath", "//input[@id='combobox-input-defaultsettlementmodeid']")
			input_enter("xpath", "//input[@id='combobox-input-defaultsettlementmodeid']")
			sleep(1)

			# 勾选代发代扣
			click('xpath', '//*[@id="isagentpayoff"]')
			sleep(1)

			# 对方对象类型
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
			
			# 返回付款处理-直联批量付款页面做数据💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 点击基础设置，收回窗体
			click("xpath",
			      '/html/body/div[1]/div[1]/div/div[2]/div/div[2]/div/div/div/div[4]/div/div/ul/li[1]/a/span[2]')
			sleep(1)
			click("xpath", "//span[text()='资金系统收付']")
			sleep(1)
			# 点击付款处理菜单
			click("xpath", "//span[text()='集中付款']")
			sleep(1)

			for i in range(1,3):
				# 切入‘可操作组织直联批量付款’的iframe窗体
				switch_to("xpath", "//iframe[@id='massPayment-tab-iframe']")
				# 点击可操作组织直联批量付款
				click("xpath", "//span[text()='可操作组织直联批量付款']")
				sleep(1)
				# 进入可操作组织直联批量付款的iframe窗体
				switch_to("xpath", "//iframe[@id='subTabFour-iframe']")

				click("xpath", '//*[@id="gridtitle"]/div[3]/div[2]')
				sleep(1)
				switch_to("xpath", '//*[@id="importDataWin-iframe"]')
				input("xpath", '//*[@id="combobox-input-businessid"]', '可操作组织集中支付导入')
				sleep(2)
				click("xpath", '//*[@id="businessid-combogrid-body-table"]/tbody/tr[1]/td[2]/div')
				sleep(1)
				click("xpath", "//span[text()='下一步']")
				sleep(1)
				switch_to("xpath", '//*[@id="loadNextWin-iframe"]')
				input("xpath", '//*[@id="combobox-input-paytypeid"]', '3042-快捷付款可操作组织付款交易类型')
				sleep(2)
				click("xpath", '//*[@id="paytypeid-combogrid-body-table"]/tbody/tr/td[2]/div')
				sleep(1)
				# 选择组批条件
				click("xpath", '//*[@id="combobox-input-groupcondition"]')
				sleep(1)
				input_down("xpath", '//*[@id="combobox-input-groupcondition"]')
				input_enter("xpath", '//*[@id="combobox-input-groupcondition"]')
				sleep(1)
				# 附件上传
				upload_click("xpath", "//div[text()='上传文件']/parent::*[1]/descendant::*[4]",
				             'D:\FlieDownload', '"KuaiJieFuKuanKCZZZPLFK.xls"')
				sleep(3)
				# 点击保存按钮
				click("xpath", "//span[text()='上传']")
				# 退出所有iframe窗体
				switch_default()
				# 用隐式等待方法等页面出现新增成功的提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功')]")
				time.sleep(3)
				if i ==1 :
					click("xpath", "//span[text()='集中付款']")
					sleep(1)

			sql = "update t_se_payments set RECORDSOURCE = '4' where purpose like '%付款处理可操作组织批量数据导入%'"
			my_sql(my_host, my_port, my_user, my_passwd, my_db,
			       sql)
			#回到快捷付款-可操作组织批量处理页面
			click("xpath", "//span[text()='资金系统收付']")
			sleep(1)
			click("xpath", "//span[text()='业务系统对接']")
			sleep(1)
			click("xpath", "//span[text()='快捷付款']")
			sleep(1)

			#测试送审、撤销送审功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			#切入可组织批量代付处理页面
			switch_to("xpath",'//*[@id="externalPayments-tab-iframe"]')
			span_click("可操作组织批量代付处理")
			sleep(1)
			switch_to("xpath",'//*[@id="subTabNine-iframe"]')
			span_click("批次号")

			#双击数据，进入详情页
			double_click("xpath",'//*[@id="grid-body-table"]/tbody/tr[1]/td[3]/div')
			sleep(1)
			switch_to("xpath",'//*[@id="detailWin-iframe"]')
			#勾选数据
			click("xpath",'//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			span_click("送审")
			ok_click()
			#推出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功')]")
			print("快捷付款-直联批量付款处理，审核成功")
			span_click("快捷付款")
			sleep(1)

			# 撤销送审功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入可组织批量代付处理页面
			switch_to("xpath", '//*[@id="externalPayments-tab-iframe"]')
			span_click("可操作组织批量代付处理")
			sleep(1)
			switch_to("xpath", '//*[@id="subTabNine-iframe"]')
			span_click("批次号")
			# 双击数据，进入详情页
			double_click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[3]/div')
			sleep(1)
			switch_to("xpath", '//*[@id="detailWin-iframe"]')
			# 勾选数据
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)

			triangle_cick_and_element("送审","撤销送审")
			ok_click()
			# 推出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'撤销送审成功！')]")
			print("快捷付款-直联批量付款处理，撤销送审成功")
			span_click("快捷付款")
			sleep(1)
			
			# 测试拒绝功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入可组织批量代付处理页面
			switch_to("xpath", '//*[@id="externalPayments-tab-iframe"]')
			span_click("可操作组织批量代付处理")
			sleep(1)
			switch_to("xpath", '//*[@id="subTabNine-iframe"]')
			span_click("批次号")
			# 双击数据，进入详情页
			double_click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[3]/div')
			sleep(1)
			switch_to("xpath", '//*[@id="detailWin-iframe"]')
			# 勾选数据
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)

			span_click("送审")
			ok_click()
			switch_default()
			span_click("快捷付款")
			sleep(3)
			#再次回到页面
			switch_to("xpath", '//*[@id="externalPayments-tab-iframe"]')
			span_click("可操作组织批量代付处理")
			sleep(1)
			switch_to("xpath", '//*[@id="subTabNine-iframe"]')
			span_click("批次号")
			# 双击数据，进入详情页
			double_click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[3]/div')
			sleep(1)
			switch_to("xpath", '//*[@id="detailWin-iframe"]')
			# 勾选数据
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)

			triangle_cick_and_element("同意","拒绝")
			ok_click()
			input("xpath",'//*[@id="remark"]','测试拒绝')
			sleep(1)
			span_click("确定")
			# 推出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'全部成功')]")
			print("快捷付款-直联批量付款处理,拒绝成功")
			span_click("快捷付款")
			sleep(1)

			# 测试同意功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入可组织批量代付处理页面
			switch_to("xpath", '//*[@id="externalPayments-tab-iframe"]')
			span_click("可操作组织批量代付处理")
			sleep(1)
			switch_to("xpath", '//*[@id="subTabNine-iframe"]')
			span_click("批次号")
			# 双击数据，进入详情页
			double_click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[3]/div')
			sleep(1)
			switch_to("xpath", '//*[@id="detailWin-iframe"]')
			# 勾选数据
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)

			span_click("送审")
			ok_click()
			switch_default()
			span_click("快捷付款")
			sleep(3)
			# 再次回到页面
			switch_to("xpath", '//*[@id="externalPayments-tab-iframe"]')
			span_click("可操作组织批量代付处理")
			sleep(1)
			switch_to("xpath", '//*[@id="subTabNine-iframe"]')
			span_click("批次号")
			# 双击数据，进入详情页
			double_click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[3]/div')
			sleep(1)
			switch_to("xpath", '//*[@id="detailWin-iframe"]')
			# 勾选数据
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)

			span_click("同意")
			ok_click()
			# 推出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'全部成功')]")
			print("快捷付款-直联批量付款处理,同意成功")
			span_click("快捷付款")
			sleep(3)

			# 测试支付功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入可组织批量代付处理页面
			switch_to("xpath", '//*[@id="externalPayments-tab-iframe"]')
			span_click("可操作组织批量代付处理")
			sleep(1)
			switch_to("xpath", '//*[@id="subTabNine-iframe"]')
			span_click("批次号")
			# 双击数据，进入详情页
			double_click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[3]/div')
			sleep(1)
			switch_to("xpath", '//*[@id="detailWin-iframe"]')
			# 勾选数据
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)

			span_click("支付")
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！1笔进行了支付，0笔不允许支付。')]")
			print("快捷付款-直联批量付款处理,支付成功")
			span_click("快捷付款")
			sleep(3)

			# 测试查询支付状态💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 修改数据
			sql = "update t_se_payments set  paystate = '7' where purpose like '%付款处理可操作组织批量数据导入%'"
			my_sql(my_host, my_port, my_user, my_passwd, my_db,
			        sql)

			# 切入可组织批量代付处理页面
			switch_to("xpath", '//*[@id="externalPayments-tab-iframe"]')
			span_click("可操作组织批量代付处理")
			sleep(1)
			switch_to("xpath", '//*[@id="subTabNine-iframe"]')
			span_click("批次号")
			# 双击数据，进入详情页
			double_click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[3]/div')
			sleep(1)
			switch_to("xpath", '//*[@id="detailWin-iframe"]')
			# 勾选数据
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)

			triangle_cick_and_element("支付","查询支付状态")
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'请查看相应结果!')]")
			print("快捷付款-直联批量付款处理,查询支付状态成功")
			span_click("快捷付款")
			sleep(3)
			
			# 测试确认已支付💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 修改数据
			sql = "update t_se_payments set  paystate = '7' where purpose like '%付款处理可操作组织批量数据导入%'"
			my_sql(my_host, my_port, my_user, my_passwd, my_db,
			        sql)
			
			# 切入可组织批量代付处理页面
			switch_to("xpath", '//*[@id="externalPayments-tab-iframe"]')
			span_click("可操作组织批量代付处理")
			sleep(1)
			switch_to("xpath", '//*[@id="subTabNine-iframe"]')
			span_click("批次号")
			# 双击数据，进入详情页
			double_click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[3]/div')
			sleep(1)
			switch_to("xpath", '//*[@id="detailWin-iframe"]')
			# 勾选数据
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("支付", "确认已支付")
			ok_click()
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'共1笔，处理成功1笔，失败0笔。')]")
			print("快捷付款-直联批量付款处理,确认已支付成功")
			span_click("快捷付款")
			sleep(3)
			
			# 测试转网银💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 修改数据
			sql = "update t_se_payments set  paystate = '1' where purpose like '%付款处理可操作组织批量数据导入%'"
			my_sql(my_host, my_port, my_user, my_passwd, my_db,
			        sql)
			
			# 切入可组织批量代付处理页面
			switch_to("xpath", '//*[@id="externalPayments-tab-iframe"]')
			span_click("可操作组织批量代付处理")
			sleep(1)
			switch_to("xpath", '//*[@id="subTabNine-iframe"]')
			span_click("批次号")
			# 双击数据，进入详情页
			double_click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[3]/div')
			sleep(1)
			switch_to("xpath", '//*[@id="detailWin-iframe"]')
			# 勾选数据
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("支付", "转网银")
			# 结算方式
			click("xpath", '//*[@id="combobox-input-settlementmodeid"]')
			sleep(1)
			up_enter_click('//*[@id="combobox-input-settlementmodeid"]')
			span_click("确定")
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'转网银成功1笔，请通过网银支付成功确认支付。')]")
			print("快捷付款-直联批量付款处理,转网银成功")
			span_click("快捷付款")
			sleep(3)
			
			# 测试网银支付成功💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入可组织批量代付处理页面
			switch_to("xpath", '//*[@id="externalPayments-tab-iframe"]')
			span_click("可操作组织批量代付处理")
			sleep(1)
			switch_to("xpath", '//*[@id="subTabNine-iframe"]')
			span_click("批次号")
			# 双击数据，进入详情页
			double_click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[3]/div')
			sleep(1)
			switch_to("xpath", '//*[@id="detailWin-iframe"]')
			# 勾选数据
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("支付", "网银支付成功")
			span_click("确定")
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！1笔进行了支付，0笔不允许支付。')]")
			print("快捷付款-直联批量付款处理,网银支付成功")
			span_click("快捷付款")
			sleep(3)
			
			# 测试冲正功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入可组织批量代付处理页面
			switch_to("xpath", '//*[@id="externalPayments-tab-iframe"]')
			span_click("可操作组织批量代付处理")
			sleep(1)
			switch_to("xpath", '//*[@id="subTabNine-iframe"]')
			span_click("批次号")
			# 双击数据，进入详情页
			double_click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[3]/div')
			sleep(1)
			switch_to("xpath", '//*[@id="detailWin-iframe"]')
			# 勾选数据
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("其他操作", '冲正')
			switch_to("xpath", '//*[@id="reverseWin-iframe"]')
			# 冲正日期
			today = date.today()
			we = str(today) + " " + "08:30:00"
			input("xpath", '//*[@id="reversedate-input"]', we)
			sleep(1)
			keyDown('enter')
			sleep(1)
			
			# 冲正原因
			input("xpath", '//*[@id="reversalreason"]', '测试冲正')
			sleep(1)
			
			# 生成付款单
			span_click("冲正原因")
			click("xpath", '//*[@id="iscreatenewtrade"]')
			sleep(1)
			span_click("确认冲正")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("快捷付款-直联批量付款处理,冲正成功")
			span_click("快捷付款")
			sleep(3)
			
			# 测试作废功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入可组织批量代付处理页面
			switch_to("xpath", '//*[@id="externalPayments-tab-iframe"]')
			span_click("可操作组织批量代付处理")
			sleep(1)
			switch_to("xpath", '//*[@id="subTabNine-iframe"]')
			span_click("批次号")
			# 双击数据，进入详情页
			double_click("xpath", '//*[@id="grid-body-table"]/tbody/tr[2]/td[3]/div')
			sleep(1)
			switch_to("xpath", '//*[@id="detailWin-iframe"]')
			# 勾选数据
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("其他操作", '作废')
			ok_click()
			
			input("xpath", '//*[@id="combobox-input-cancelReason"]', '测试作废')
			sleep(1)
			js_click("xpath", '//*[@id="determineCancel"]/span/span')
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功')]")
			print("快捷付款-直联批量付款处理,作废成功")
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
