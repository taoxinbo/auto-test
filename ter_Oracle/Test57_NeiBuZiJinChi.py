# encoding=utf-8
# @Time : 2020/03/16 13:30
# @Author : zzg
# 此文件是测试Mysql版本内部资金池
import os
import sys
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
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))
# print("开始时间：",time.strftime("%Y-%m-%d %H:%M:%S"))

driver = ""


@pytest.mark.flaky(reruns=pytest_flaky, reruns_delay=10)
class Test57_NeiBuZiJinChi(unittest.TestCase):
	
	# 启动浏览器
	def setUp(self):
		# 启动浏览器的另外一个方法：通过封装启动浏览器的驱动，启动不同浏览器
		self.driver = get("chrome")
	
	# 登陆系统、对系统设置进行操作
	def test_trade(self):
		
		# login(G_Ora_Url, mindy, Password, "亚唐科技")
		login(G_Mys_Url, mindy, Password, "亚唐科技")
		
		logging.info("开始测试内部资金池功能")
		# 将页面的滚动条滑动到‘资金结算管理’页面的地方
		js_gd("xpath", "//span[contains(text(),'内部资金池')]")
		# 用JS的方法点击资金结算管理菜单按钮
		js_click("xpath", "//span[contains(text(),'内部资金池')]")
		sleep(1)
		# 退出所有iframe窗体
		switch_default()
		'''
		#测试资金池上划管理--资金上划设置🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱
		try:
			logger.info("测试资金池上划管理--资金上划设置")
			switch_default()

			click("xpath", "//span[text()='资金池上划管理']")
			sleep(1)
			click("xpath", "//span[text()='资金上划设置']")
			sleep(1)
			switch_default()
			sleep(3)
			
			#去下级组织页面做账户数据💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			choose_organization("Mindy科技有限公司")
			
			# 点击'外币收付结算'菜单
			js_gd("xpath", "//span[contains(text(),'账户资金监控')]")
			# 用JS的方法点击账户资金监控菜单
			js_click("xpath", "//span[contains(text(),'账户资金监控')]")
			sleep(1)
			# 点击账户生命周期
			click("xpath",'/html/body/div[1]/div[1]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div/ul/li[2]/a/span[2]')
			sleep(1)
			click("xpath", "//span[text()='账户维护']")
			sleep(1)
			switch_default()
			
			for i in range(1, 6):
				# 切入单币种账户窗体，新增账户
				switch_to("xpath", '//*[@id="bankAccounts-tab-iframe"]')
				switch_to("xpath", '//*[@id="subTabOne-iframe"]')
				sleep(1)
				
				span_click("新增")
				# 切入新增窗体
				switch_to("xpath", '//*[@id="addWin-iframe"]')
				sleep(2)
				
				# 银行
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
				input("xpath", "//input[@id='combobox-input-inorout']", "境内")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-inorout']")
				input_enter("xpath", "//input[@id='combobox-input-inorout']")
				
				# 输入银行账号
				number=str(time.strftime("%Y%m%d%H%M%S"))
				input("xpath", '//*[@id="accountnumber"]', number)
				sleep(1)
				
				name = "下级账户"+number
				input("xpath", '//*[@id="accountname"]',name)
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
				if i ==1 :
					# 点击查询放大镜
					js_click("xpath", "//span[@class='f-contrac-close']")
					sleep(1)
				# 输入账户，进行查询
				clear("xpath",'//*[@id="accountnumber"]')
				sleep(1)
				input("xpath", '//*[@id="accountnumber"]', number)
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
				
			print("下级账户数据构造完成")
			
			# 回到快捷付款申请页面，完成组织留底余额设置
			choose_organization("亚唐科技")
			js_click("xpath", "//span[contains(text(),'内部资金池')]")
			sleep(1)
			sleep(1)
			click("xpath", "//span[text()='资金池上划管理']")
			sleep(1)
			click("xpath", "//span[text()='组织留底余额设置']")
			sleep(1)
			switch_default()
			
			switch_to("xpath",'//*[@id="orgReservedBalance-tab-iframe"]')
			span_click("新增")
			switch_to("xpath",'//*[@id="balanceaddWin-iframe"]')
			
			#组织
			input_up_click('//*[@id="combobox-input-orgid"]','00200101-Mindy科技金华分站')
			
			#留底余额
			double_click("xpath",'//*[@id="reservedbalance-input"]')
			sleep(1)
			input("xpath",'//*[@id="reservedbalance-input"]','1500')
			sleep(1)
			
			span_click("保存")
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			time.sleep(3)
			
			#银行账户分配
			switch_to("xpath", '//*[@id="orgReservedBalance-tab-iframe"]')
			click("xpath",'//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("银行账户分配")
			switch_to("xpath",'//*[@id="distributeWin-iframe"]')
			js_click("xpath",'//*[@id="editgrid-queryauthvalue-h"]/div/div[1]/span')
			sleep(1)
			click("xpath",'//*[@id="roleassignformid"]/div[2]/div[4]/div[3]/div[1]')
			sleep(1)
			
			span_click("保存")
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			time.sleep(3)
			
			click("xpath", "//span[text()='资金上划设置']")
			sleep(1)
			switch_default()
			
			
			
			
			
			#测试新增功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			for i in range(1,7):
				#切入资金上划窗体
				switch_to("xpath",'//*[@id="collectionRule-tab-iframe"]')
				
				span_click("新增")
				switch_to("xpath",'//*[@id="addWin-iframe"]')
				
				if i == 1 :
					#名称
					name ="按组织留底上划"+str(time.strftime("%M%S"))
					input("xpath",'//*[@id="name"]',name)
					sleep(1)
					
					#上划模式
					input_up_click('//*[@id="combobox-input-collectionmode"]','按组织留底上划')
					
					#组织
					input_up_click('//*[@id="combobox-input-uperorgid"]','001010-亚唐科技')
					
					#账户
					click("xpath",'//*[@id="combobox-input-uperaccountid"]')
					sleep(1)
					click("xpath", '//*[@id="uperaccountid-combogrid-body-table"]/tbody/tr[1]/td[2]/div')
					sleep(1)
					
					#新增行
					click("xpath",'//*[@id="gridbar"]/div/div[1]/table/tbody/tr/td[1]/span')
					sleep(1)
					
					#组织
					input_up_click('//*[@id="combobox-input-editgrid-orgid-0"]','002001-Mindy科技有限公司')
					
					#账户
					click("xpath",'//*[@id="combobox-input-editgrid-accountid-0"]')
					sleep(1)
					click("xpath",'//*[@id="editgrid-accountid-0-combogrid-body-table"]/tbody/tr[1]/td[2]/div')
					sleep(1)
					
					#满额上划金额
					double_click("xpath",'//*[@id="editgrid-miniuptransferamount-0-input"]')
					sleep(1)
					input("xpath",'//*[@id="editgrid-miniuptransferamount-0-input"]','50000')
					sleep(1)
					
					#最小划拨金额
					double_click("xpath",'//*[@id="editgrid-minitransferamount-0-input"]')
					sleep(1)
					input("xpath",'//*[@id="editgrid-minitransferamount-0-input"]','100')
					
					span_click("保存")
					# 退出所有窗体
					switch_default()
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					time.sleep(3)
					
					# 切入资金上划窗体
					switch_to("xpath", '//*[@id="collectionRule-tab-iframe"]')
					
					#刷新勾选按钮
					click("xpath",'//*[@id="treepagingbar-page-refresh"]')
					sleep(1)
					click("xpath",'//*[@id="t1_t0-fixed"]/td[2]/div/button')
					sleep(1)
					
					span_click("删除")
					ok_click()
					
					#退出所有窗体
					switch_default()
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("资金上划设置--满额上划,删除成功")
					time.sleep(3)
				if i == 2:
					# 名称
					name = "按组织留底上划" + str(time.strftime("%M%S"))
					input("xpath", '//*[@id="name"]', name)
					sleep(1)
					
					# 上划模式
					input_up_click('//*[@id="combobox-input-collectionmode"]', '按组织留底上划')
					
					# 组织
					input_up_click('//*[@id="combobox-input-uperorgid"]', '001010-亚唐科技')
					
					# 指定交易类型
					click_up_click('//*[@id="combobox-input-paytypeid"]')
					
					# 账户
					click("xpath", '//*[@id="combobox-input-uperaccountid"]')
					sleep(1)
					click("xpath", '//*[@id="uperaccountid-combogrid-body-table"]/tbody/tr[1]/td[2]/div')
					sleep(1)
					
					
					
					# 新增行
					click("xpath", '//*[@id="gridbar"]/div/div[1]/table/tbody/tr/td[1]/span')
					sleep(1)
					
					# 组织
					input_up_click('//*[@id="combobox-input-editgrid-orgid-0"]', '002001-Mindy科技有限公司')
					
					# 账户
					click("xpath", '//*[@id="combobox-input-editgrid-accountid-0"]')
					sleep(1)
					click("xpath", '//*[@id="editgrid-accountid-0-combogrid-body-table"]/tbody/tr[1]/td[2]/div')
					sleep(1)
					
					# 满额上划金额
					double_click("xpath", '//*[@id="editgrid-miniuptransferamount-0-input"]')
					sleep(1)
					input("xpath", '//*[@id="editgrid-miniuptransferamount-0-input"]', '50000')
					sleep(1)
					
					# 最小划拨金额
					double_click("xpath", '//*[@id="editgrid-minitransferamount-0-input"]')
					sleep(1)
					input("xpath", '//*[@id="editgrid-minitransferamount-0-input"]', '100')
					
					span_click("保存")
					# 退出所有窗体
					switch_default()
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					time.sleep(3)
				
				if i == 3:
					# 名称
					name = "异常资金上划" + str(time.strftime("%M%S"))
					input("xpath", '//*[@id="name"]', name)
					sleep(1)
					
					# 上划模式
					input_up_click('//*[@id="combobox-input-collectionmode"]', '异常资金上划')
					
					# 组织
					input_up_click('//*[@id="combobox-input-uperorgid"]', '001010-亚唐科技')
					
					# 指定交易类型
					click_up_click('//*[@id="combobox-input-paytypeid"]')
					
					# 账户
					click("xpath", '//*[@id="combobox-input-uperaccountid"]')
					sleep(1)
					click("xpath", '//*[@id="uperaccountid-combogrid-body-table"]/tbody/tr[2]/td[2]/div')
					sleep(1)
					
					# 新增行
					js_gd("xpath", '//*[@id="gridbar"]/div/div[1]/table/tbody/tr/td[1]/span')
					sleep(1)
					js_click("xpath", '//*[@id="gridbar"]/div/div[1]/table/tbody/tr/td[1]/span')
					sleep(1)
					# 组织
					input_up_click('//*[@id="combobox-input-editgrid-orgid-0"]', '002001-Mindy科技有限公司')
					
					# 账户
					click("xpath", '//*[@id="combobox-input-editgrid-accountid-0"]')
					sleep(1)
					click("xpath", '//*[@id="editgrid-accountid-0-combogrid-body-table"]/tbody/tr[2]/td[2]/div')
					sleep(1)
				
					
					js_gd("xpath",'//*[@id="save"]/span/span')
					sleep(1)
					span_click("保存")
					# 退出所有窗体
					switch_default()
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					time.sleep(3)
				if i == 4:
					# 名称
					name = "按比例上划" + str(time.strftime("%M%S"))
					input("xpath", '//*[@id="name"]', name)
					sleep(1)
					
					# 上划模式
					input_up_click('//*[@id="combobox-input-collectionmode"]', '按比例上划')
					
					# 组织
					input_up_click('//*[@id="combobox-input-uperorgid"]', '001010-亚唐科技')
					
					# 指定交易类型
					click_up_click('//*[@id="combobox-input-paytypeid"]')
					
					# 账户
					click("xpath", '//*[@id="combobox-input-uperaccountid"]')
					sleep(1)
					click("xpath", '//*[@id="uperaccountid-combogrid-body-table"]/tbody/tr[3]/td[2]/div')
					sleep(1)
					
					
					# 新增行
					click("xpath", '//*[@id="gridbar"]/div/div[1]/table/tbody/tr/td[1]/span')
					sleep(1)
					
					# 组织
					input_up_click('//*[@id="combobox-input-editgrid-orgid-0"]', '002001-Mindy科技有限公司')
					
					# 账户
					click("xpath", '//*[@id="combobox-input-editgrid-accountid-0"]')
					sleep(1)
					click("xpath", '//*[@id="editgrid-accountid-0-combogrid-body-table"]/tbody/tr[3]/td[2]/div')
					sleep(1)
					
					#上划比例
					double_click("xpath",'//*[@id="editgrid-collectionvalue-0-input"]')
					sleep(1)
					input("xpath",'//*[@id="editgrid-collectionvalue-0-input"]','5')
					sleep(1)
					
					span_click("保存")
					# 退出所有窗体
					switch_default()
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					time.sleep(3)
				if i == 5:
					# 名称
					name = "定额上划" + str(time.strftime("%M%S"))
					input("xpath", '//*[@id="name"]', name)
					sleep(1)
					
					# 上划模式
					input_up_click('//*[@id="combobox-input-collectionmode"]', '定额上划')
					
					# 组织
					input_up_click('//*[@id="combobox-input-uperorgid"]', '001010-亚唐科技')
					
					# 指定交易类型
					click_up_click('//*[@id="combobox-input-paytypeid"]')
					
					# 账户
					click("xpath", '//*[@id="combobox-input-uperaccountid"]')
					sleep(1)
					click("xpath", '//*[@id="uperaccountid-combogrid-body-table"]/tbody/tr[4]/td[2]/div')
					sleep(1)
					
					
					# 新增行
					click("xpath", '//*[@id="gridbar"]/div/div[1]/table/tbody/tr/td[1]/span')
					sleep(1)
					
					# 组织
					input_up_click('//*[@id="combobox-input-editgrid-orgid-0"]', '002001-Mindy科技有限公司')
					
					# 账户
					click("xpath", '//*[@id="combobox-input-editgrid-accountid-0"]')
					sleep(1)
					click("xpath", '//*[@id="editgrid-accountid-0-combogrid-body-table"]/tbody/tr[4]/td[2]/div')
					sleep(1)
					
					# 上划金额
					double_click("xpath", '//*[@id="editgrid-collectionvalue-0-input"]')
					sleep(1)
					input("xpath", '//*[@id="editgrid-collectionvalue-0-input"]', '100')
					sleep(1)
					
					span_click("保存")
					# 退出所有窗体
					switch_default()
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					time.sleep(3)
				if i == 6:
					# 名称
					name = "满额上划" + str(time.strftime("%M%S"))
					input("xpath", '//*[@id="name"]', name)
					sleep(1)
					
					# 上划模式
					input_up_click('//*[@id="combobox-input-collectionmode"]', '满额上划')
					
					# 组织
					input_up_click('//*[@id="combobox-input-uperorgid"]', '001010-亚唐科技')
					
					# 指定交易类型
					click_up_click('//*[@id="combobox-input-paytypeid"]')
					
					# 账户
					click("xpath", '//*[@id="combobox-input-uperaccountid"]')
					sleep(1)
					click("xpath", '//*[@id="uperaccountid-combogrid-body-table"]/tbody/tr[5]/td[2]/div')
					sleep(1)
					
					
					# 新增行
					click("xpath", '//*[@id="gridbar"]/div/div[1]/table/tbody/tr/td[1]/span')
					sleep(1)
					
					# 组织
					input_up_click('//*[@id="combobox-input-editgrid-orgid-0"]', '002001-Mindy科技有限公司')
					
					# 账户
					click("xpath", '//*[@id="combobox-input-editgrid-accountid-0"]')
					sleep(1)
					click("xpath", '//*[@id="editgrid-accountid-0-combogrid-body-table"]/tbody/tr[5]/td[2]/div')
					sleep(1)
					
					# 上划金额
					double_click("xpath", '//*[@id="editgrid-miniuptransferamount-0-input"]')
					sleep(1)
					input("xpath", '//*[@id="editgrid-miniuptransferamount-0-input"]', '50000')
					sleep(1)
					
					span_click("保存")
					# 退出所有窗体
					switch_default()
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("资金上划管理--资金上划设置，新增成功")
					time.sleep(3)
			
			# 测试修改功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入资金上划窗体
			switch_to("xpath", '//*[@id="collectionRule-tab-iframe"]')
			
			#刷新、勾选按钮
			click("xpath",'//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath",'//*[@id="t1_t1-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("修改")
			switch_to("xpath",'//*[@id="modWin-iframe"]')
			sleep(2)
			span_click("保存")
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("资金上划管理--资金上划设置，修改成功")
			time.sleep(3)
			
			# 测试失效功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入资金上划窗体
			switch_to("xpath", '//*[@id="collectionRule-tab-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t1-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("失效")
			ok_click()
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'失效成功！')]")
			print("资金上划管理--资金上划设置，失效成功")
			time.sleep(3)
			
			# 测试生效功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入资金上划窗体
			switch_to("xpath", '//*[@id="collectionRule-tab-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t1-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("生效")
			
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'生效成功！')]")
			print("资金上划管理--资金上划设置，生效成功")
			time.sleep(3)
			
			# 测试设置留底金额功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入资金上划窗体
			switch_to("xpath", '//*[@id="collectionRule-tab-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("设置上划条件","设置留底金额")
			switch_to("xpath",'//*[@id="reservedbalanceWin-iframe"]')
			sleep(2)
			
			double_click("xpath",'//*[@id="reservedbalance-input"]')
			sleep(1)
			input("xpath",'//*[@id="reservedbalance-input"]','50000')
			sleep(1)
			span_click("保存")
			
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("资金上划管理--资金上划设置，设置留底金额成功")
			time.sleep(3)
			
			# 测试设置满额上划金额功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入资金上划窗体
			switch_to("xpath", '//*[@id="collectionRule-tab-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("设置上划条件", "设置满额上划金额")
			switch_to("xpath", '//*[@id="miniuptransferamountWin-iframe"]')
			sleep(2)
			
			double_click("xpath", '//*[@id="miniuptransferamount-input"]')
			sleep(1)
			input("xpath", '//*[@id="miniuptransferamount-input"]', '50000')
			sleep(1)
			span_click("保存")
			
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("资金上划管理--资金上划设置，设置满额上划金额成功")
			time.sleep(3)
			
			# 测试设置最小划拨金额功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入资金上划窗体
			switch_to("xpath", '//*[@id="collectionRule-tab-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("设置上划条件", "设置最小划拨金额")
			switch_to("xpath", '//*[@id="minitransferamountWin-iframe"]')
			sleep(2)
			
			double_click("xpath", '//*[@id="minitransferamount-input"]')
			sleep(1)
			input("xpath", '//*[@id="minitransferamount-input"]', '100')
			sleep(1)
			span_click("保存")
			
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("资金上划管理--资金上划设置，设置最小划拨金额成功")
			time.sleep(3)
			
			# 测试取整划拨等级功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入资金上划窗体
			switch_to("xpath", '//*[@id="collectionRule-tab-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("设置上划条件", "设置取整划拨等级")
			switch_to("xpath", '//*[@id="integerrateWin-iframe"]')
			sleep(2)
			
			click_up_click('//*[@id="combobox-input-integerrate"]')
			span_click("保存")
			
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("资金上划管理--资金上划设置，设置取整划拨等级成功")
			time.sleep(3)
			
			# 测试设置上划金额功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入资金上划窗体
			switch_to("xpath", '//*[@id="collectionRule-tab-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t3-fixed"]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("设置上划条件", "设置上划金额")
			switch_to("xpath", '//*[@id="collectionvalueamountWin-iframe"]')
			sleep(2)
			
			double_click("xpath", '//*[@id="collectionvalue-input"]')
			sleep(1)
			input("xpath", '//*[@id="collectionvalue-input"]', '100')
			sleep(1)
			span_click("保存")
			
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("资金上划管理--资金上划设置，设置上划金额成功")
			time.sleep(3)
			
			# 测试设置上划比例功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入资金上划窗体
			switch_to("xpath", '//*[@id="collectionRule-tab-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t1-fixed"]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("设置上划条件", "设置上划比例")
			switch_to("xpath", '//*[@id="collectionvaluepropWin-iframe"]')
			sleep(2)
			
			input("xpath", '//*[@id="collectionvalue"]', '5')
			sleep(1)
			span_click("保存")
			
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("资金上划管理--资金上划设置，设置上划比例成功")
			time.sleep(3)
			
			#回到初始页面
			click("xpath", "//span[text()='资金池上划管理']")
			sleep(1)
			
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("资金上划设置失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)

			# def tearDown(self):
			#     self.driver.quit()
			print("结束时间：", time.strftime("%Y-%m-%d %H:%M:%S"))
		
		
		# 测试资金池上划处理--满额上划🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱
		try:
			logger.info("测试资金池上划管理--资金上划设置")
			switch_default()
			click("xpath", "//span[text()='资金池上划管理']")
			sleep(1)
			click("xpath", "//span[text()='资金上划处理']")
			sleep(1)
			switch_default()
			sleep(3)
			
			#余额查询💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath",'//*[@id="collectionHandle-tab-iframe"]')
			switch_to("xpath",'//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			#上划模板
			clear("xpath",'//*[@id="combobox-input-collectionruleid"]')
			sleep(1)
			click("xpath",'//*[@id="combobox-input-collectionruleid"]')
			sleep(1)
			click("xpath",'//*[@id="collectionruleid-combogrid-body-table"]/tbody/tr/td[2]/div')
			sleep(1)
			
			#勾选按钮
			click("xpath",'//*[@id="editgrid-syscheck-0"]')
			sleep(1)
			
			span_click("余额查询")
			
			#退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'当前银行可用余额')]")
			print("资金上划设置--满额上划，余额查询成功！")
			click("xpath", "//span[text()='资金上划处理']")
			sleep(3)
			
			# 测试立即上划功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="collectionHandle-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			# 上划模板
			clear("xpath", '//*[@id="combobox-input-collectionruleid"]')
			sleep(1)
			click("xpath", '//*[@id="combobox-input-collectionruleid"]')
			sleep(1)
			click("xpath", '//*[@id="collectionruleid-combogrid-body-table"]/tbody/tr/td[2]/div')
			sleep(1)
			
			# 勾选按钮
			click("xpath", '//*[@id="editgrid-syscheck-0"]')
			sleep(1)
			
			span_click("立即上划")
			ok_click()
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'生成上划单成功！')]")
			print("资金上划设置--满额上划，立即上划成功！")
			click("xpath", "//span[text()='资金上划处理']")
			sleep(3)
			
			# 测试生成上划单功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			for i in range(1,4):
				switch_to("xpath", '//*[@id="collectionHandle-tab-iframe"]')
				switch_to("xpath", '//*[@id="subTabOne-iframe"]')
				sleep(1)
				
				# 上划模板
				clear("xpath", '//*[@id="combobox-input-collectionruleid"]')
				sleep(1)
				click("xpath", '//*[@id="combobox-input-collectionruleid"]')
				sleep(1)
				click("xpath", '//*[@id="collectionruleid-combogrid-body-table"]/tbody/tr/td[2]/div')
				sleep(1)
				
				# 勾选按钮
				click("xpath", '//*[@id="editgrid-syscheck-0"]')
				sleep(1)
				
				span_click("生成上划单")
				ok_click()
				# 退出所有窗体
				switch_default()
				implici_wait("xpath", "//span[contains(text(),'生成上划单成功！')]")
				if i ==3 :
					print("资金池上划管理--资金上划设置，立即上划成功！")
				click("xpath", "//span[text()='资金上划处理']")
				sleep(3)
			
			# 测试删除功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="collectionHandle-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			
			# 勾选按钮
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("删除")
			ok_click()
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'删除操作成功！')]")
			print("资金上划设置--满额上划，删除成功！")
			click("xpath", "//span[text()='资金上划处理']")
			sleep(3)
			
			# 测试作废功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="collectionHandle-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			# 勾选按钮
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("作废")
			ok_click()
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("资金上划设置--满额上划，作废成功！")
			click("xpath", "//span[text()='资金上划处理']")
			sleep(3)
			
			# 测试上划状态查询功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="collectionHandle-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			# 勾选按钮
			click("xpath", '//*[@id="t1_t2-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("上划状态查询")
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'单据已查询状态，请查看相应结果')]")
			print("资金上划设置--满额上划，上划状态查询成功！")
			click("xpath", "//span[text()='资金上划处理']")
			sleep(3)
			
			# 测试送审功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="collectionHandle-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			# 勾选按钮
			click("xpath", '//*[@id="t1_t1-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("送审")
			
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'成功送审1笔，失败0笔。')]")
			print("资金上划设置--满额上划，送审成功！")
			click("xpath", "//span[text()='资金上划处理']")
			sleep(3)
			
			# 测试审批历史💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="collectionHandle-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			#一审
			# 勾选按钮
			double_click("xpath",'//*[@id="t1_t1"]/td[1]/div')
			sleep(1)
			
			switch_to("xpath",'//*[@id="wf_taskProcessing_win-iframe"]')
			sleep(1)
			
			span_click("同意")
			switch_parent()
			sleep(3)
			
			#二审
			# 勾选按钮
			double_click("xpath", '//*[@id="t1_t1"]/td[1]/div')
			sleep(1)
			
			switch_to("xpath", '//*[@id="wf_taskProcessing_win-iframe"]')
			sleep(1)
			
			span_click("同意")
			switch_parent()
			sleep(3)
			
			#勾选按钮
			click("xpath",'//*[@id="t1_t1-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("审批历史")
			switch_to("xpath",'//*[@id="flowwin-iframe"]')
			sleep(1)
			implici_wait("xpath", "//span[contains(text(),'流程图')]")
			print("资金上划设置--满额上划，审批历史查看成功！")
			# 退出所有窗体
			switch_default()
			click("xpath", "//span[text()='资金上划处理']")
			sleep(3)
			
			# 测试上划功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="collectionHandle-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			# 勾选按钮
			click("xpath", '//*[@id="t1_t1-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("上划")
			
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'上划操作成功！')]")
			print("资金上划设置--满额上划，上划成功！")
			click("xpath", "//span[text()='资金上划处理']")
			sleep(3)
			
			# 测试上划日志查看功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="collectionHandle-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			# 勾选按钮
			click("xpath", '//*[@id="t1_t1-fixed"]/td[1]/div/span')
			sleep(1)
			click("xpath", '//*[@id="t1_t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("上划日志查看")
			switch_to("xpath",'//*[@id="logsWin-iframe"]')
			implici_wait("xpath", "//div[contains(text(),'支付')]")
			print("资金上划设置--满额上划，上划日志查看成功！")
			# 退出所有窗体
			switch_default()
			click("xpath", "//span[text()='资金上划处理']")
			sleep(3)
			
			
			# 测试确认已上划💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			sql = "update t_se_payments set paystate = '7' where ourbankaccountname like '%账户2021%'"
			ora_sql(ora_ip, ora_sid, ora_user, ora_pwd,
			       sql)
			sleep(1
			)
			switch_to("xpath", '//*[@id="collectionHandle-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			# 勾选按钮
			
			click("xpath", '//*[@id="t1_t1-fixed"]/td[2]/div')
			sleep(1)
			
			span_click("确认已上划")
			ok_click()
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("资金上划设置--满额上划，确认已上划成功！")
			# 退出所有窗体
			switch_default()
			click("xpath", "//span[text()='资金上划处理']")
			sleep(3)
			
			#回到初始界面
			click("xpath", "//span[text()='资金池上划管理']")
			sleep(1)
			
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("满额上划失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
			
			# def tearDown(self):
			#     self.driver.quit()
			print("结束时间：", time.strftime("%Y-%m-%d %H:%M:%S"))
		
		
		# 测试资金池上划处理--定额上划🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱
		try:
			logger.info("测试资金池上划管理--资金上划设置")
			switch_default()
			click("xpath", "//span[text()='资金池上划管理']")
			sleep(1)
			click("xpath", "//span[text()='资金上划处理']")
			sleep(1)
			switch_default()
			sleep(3)
			
			# 余额查询💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="collectionHandle-tab-iframe"]')
			span_click("定额上划")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			sleep(1)
			
			# 上划模板
			clear("xpath", '//*[@id="combobox-input-collectionruleid"]')
			sleep(1)
			click("xpath", '//*[@id="combobox-input-collectionruleid"]')
			sleep(1)
			click("xpath", '//*[@id="collectionruleid-combogrid-body-table"]/tbody/tr/td[2]/div')
			sleep(1)
			
			# 勾选按钮
			click("xpath", '//*[@id="editgrid-syscheck-0"]')
			sleep(1)
			
			span_click("余额查询")
			
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'当前银行可用余额')]")
			print("资金上划设置--定额上划，余额查询成功！")
			click("xpath", "//span[text()='资金上划处理']")
			sleep(3)
			
			# 测试立即上划功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="collectionHandle-tab-iframe"]')
			span_click("定额上划")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			sleep(1)
			
			# 上划模板
			clear("xpath", '//*[@id="combobox-input-collectionruleid"]')
			sleep(1)
			click("xpath", '//*[@id="combobox-input-collectionruleid"]')
			sleep(1)
			click("xpath", '//*[@id="collectionruleid-combogrid-body-table"]/tbody/tr/td[2]/div')
			sleep(1)
			
			# 勾选按钮
			click("xpath", '//*[@id="editgrid-syscheck-0"]')
			sleep(1)
			
			span_click("立即上划")
			ok_click()
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'生成上划单成功！')]")
			print("金上划设置--定额上划，余额查询成功！")
			click("xpath", "//span[text()='资金上划处理']")
			sleep(3)
			
			# 测试生成上划单功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			for i in range(1, 4):
				switch_to("xpath", '//*[@id="collectionHandle-tab-iframe"]')
				span_click("定额上划")
				switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
				sleep(1)
				
				# 上划模板
				clear("xpath", '//*[@id="combobox-input-collectionruleid"]')
				sleep(1)
				click("xpath", '//*[@id="combobox-input-collectionruleid"]')
				sleep(1)
				click("xpath", '//*[@id="collectionruleid-combogrid-body-table"]/tbody/tr/td[2]/div')
				sleep(1)
				
				# 勾选按钮
				click("xpath", '//*[@id="editgrid-syscheck-0"]')
				sleep(1)
				
				span_click("生成上划单")
				ok_click()
				# 退出所有窗体
				switch_default()
				implici_wait("xpath", "//span[contains(text(),'生成上划单成功！')]")
				if i == 3:
					print("金上划设置--定额上划，生成上划单成功！")
				click("xpath", "//span[text()='资金上划处理']")
				sleep(3)
			
			# 测试删除功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="collectionHandle-tab-iframe"]')
			span_click("定额上划")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			sleep(1)
			
			# 勾选按钮
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("删除")
			ok_click()
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'删除操作成功！')]")
			print("资金上划设置--定额上划，删除成功！")
			click("xpath", "//span[text()='资金上划处理']")
			sleep(3)
			
			# 测试作废功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="collectionHandle-tab-iframe"]')
			span_click("定额上划")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			sleep(1)
			
			# 勾选按钮
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("作废")
			ok_click()
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("资金上划设置--定额上划，作废成功！")
			click("xpath", "//span[text()='资金上划处理']")
			sleep(3)
			
			# 测试上划状态查询功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="collectionHandle-tab-iframe"]')
			span_click("定额上划")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			sleep(1)
			
			# 勾选按钮
			click("xpath", '//*[@id="t1_t2-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("上划状态查询")
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'单据已查询状态，请查看相应结果')]")
			print("资金上划设置--定额上划，上划状态查询成功！")
			click("xpath", "//span[text()='资金上划处理']")
			sleep(3)
			
			# 测试送审功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="collectionHandle-tab-iframe"]')
			span_click("定额上划")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			sleep(1)
			
			# 勾选按钮
			click("xpath", '//*[@id="t1_t1-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("送审")
			
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'成功送审1笔，失败0笔。')]")
			print("资金上划设置--定额上划，送审成功！")
			click("xpath", "//span[text()='资金上划处理']")
			sleep(3)
			
			# 测试审批历史💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="collectionHandle-tab-iframe"]')
			span_click("定额上划")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			sleep(1)
			
			# 一审
			# 勾选按钮
			double_click("xpath", '//*[@id="t1_t1"]/td[1]/div')
			sleep(1)
			
			switch_to("xpath", '//*[@id="wf_taskProcessing_win-iframe"]')
			sleep(1)
			
			span_click("同意")
			switch_parent()
			sleep(3)
			
			# 二审
			# 勾选按钮
			double_click("xpath", '//*[@id="t1_t1"]/td[1]/div')
			sleep(1)
			
			switch_to("xpath", '//*[@id="wf_taskProcessing_win-iframe"]')
			sleep(1)
			
			span_click("同意")
			switch_parent()
			sleep(3)
			
			# 勾选按钮
			click("xpath", '//*[@id="t1_t1-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("审批历史")
			switch_to("xpath", '//*[@id="flowwin-iframe"]')
			sleep(1)
			implici_wait("xpath", "//span[contains(text(),'流程图')]")
			print("资金上划设置--定额上划，审批历史查看成功！")
			# 退出所有窗体
			switch_default()
			click("xpath", "//span[text()='资金上划处理']")
			sleep(3)
			
			# 测试上划功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="collectionHandle-tab-iframe"]')
			span_click("定额上划")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			sleep(1)
			
			# 勾选按钮
			click("xpath", '//*[@id="t1_t1-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("上划")
			
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'上划操作成功！')]")
			print("资金上划设置--定额上划，上划成功！")
			click("xpath", "//span[text()='资金上划处理']")
			sleep(3)
			
			# 测试上划日志查看功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="collectionHandle-tab-iframe"]')
			span_click("定额上划")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			sleep(1)
			
			# 勾选按钮
			click("xpath", '//*[@id="t1_t1-fixed"]/td[1]/div/span')
			sleep(1)
			click("xpath", '//*[@id="t1_t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("上划日志查看")
			switch_to("xpath", '//*[@id="logsWin-iframe"]')
			implici_wait("xpath", "//div[contains(text(),'支付')]")
			print("资金上划设置--定额上划，上划日志查看成功！")
			# 退出所有窗体
			switch_default()
			click("xpath", "//span[text()='资金上划处理']")
			sleep(3)
			
			# 测试确认已上划💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			sql = "update t_se_payments set paystate = '7' where ourbankaccountname like '%账户2021%'"
			ora_sql(ora_ip, ora_sid, ora_user, ora_pwd,
			       sql)
			sleep(1
			      )
			switch_to("xpath", '//*[@id="collectionHandle-tab-iframe"]')
			span_click("定额上划")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			sleep(1)
			
			# 勾选按钮
			
			click("xpath", '//*[@id="t1_t1-fixed"]/td[2]/div')
			sleep(1)
			
			span_click("确认已上划")
			ok_click()
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("资金上划设置--定额上划，确认已上划成功！")
			# 退出所有窗体
			switch_default()
			click("xpath", "//span[text()='资金上划处理']")
			sleep(3)
			
			# 回到初始界面
			click("xpath", "//span[text()='资金池上划管理']")
			sleep(1)
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("定额上划失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
			
			# def tearDown(self):
			#     self.driver.quit()
			print("结束时间：", time.strftime("%Y-%m-%d %H:%M:%S"))
		
		
		# 测试资金池上划处理--按比例上划🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱
		try:
			logger.info("测试资金池上划管理--资金上划设置")
			switch_default()
			click("xpath", "//span[text()='资金池上划管理']")
			sleep(1)
			click("xpath", "//span[text()='资金上划处理']")
			sleep(1)
			switch_default()
			sleep(3)
			
			# 余额查询💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="collectionHandle-tab-iframe"]')
			span_click("按比例上划")
			switch_to("xpath", '//*[@id="subTabThree-iframe"]')
			sleep(1)
			
			# 上划模板
			clear("xpath", '//*[@id="combobox-input-collectionruleid"]')
			sleep(1)
			click("xpath", '//*[@id="combobox-input-collectionruleid"]')
			sleep(1)
			click("xpath", '//*[@id="collectionruleid-combogrid-body-table"]/tbody/tr/td[2]/div')
			sleep(1)
			
			# 勾选按钮
			click("xpath", '//*[@id="editgrid-syscheck-0"]')
			sleep(1)
			
			span_click("余额查询")
			
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'当前银行可用余额')]")
			print("资金上划设置--按比例上划，余额查询成功！")
			click("xpath", "//span[text()='资金上划处理']")
			sleep(3)
			
			# 测试立即上划功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="collectionHandle-tab-iframe"]')
			span_click("按比例上划")
			switch_to("xpath", '//*[@id="subTabThree-iframe"]')
			sleep(1)
			
			# 上划模板
			clear("xpath", '//*[@id="combobox-input-collectionruleid"]')
			sleep(1)
			click("xpath", '//*[@id="combobox-input-collectionruleid"]')
			sleep(1)
			click("xpath", '//*[@id="collectionruleid-combogrid-body-table"]/tbody/tr/td[2]/div')
			sleep(1)
			
			# 勾选按钮
			click("xpath", '//*[@id="editgrid-syscheck-0"]')
			sleep(1)
			
			span_click("立即上划")
			ok_click()
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'生成上划单成功！')]")
			print("资金上划设置--按比例上划，余额查询成功！")
			click("xpath", "//span[text()='资金上划处理']")
			sleep(3)
			
			# 测试生成上划单功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			for i in range(1, 4):
				switch_to("xpath", '//*[@id="collectionHandle-tab-iframe"]')
				span_click("按比例上划")
				switch_to("xpath", '//*[@id="subTabThree-iframe"]')
				sleep(1)
				
				# 上划模板
				clear("xpath", '//*[@id="combobox-input-collectionruleid"]')
				sleep(1)
				click("xpath", '//*[@id="combobox-input-collectionruleid"]')
				sleep(1)
				click("xpath", '//*[@id="collectionruleid-combogrid-body-table"]/tbody/tr/td[2]/div')
				sleep(1)
				
				# 勾选按钮
				click("xpath", '//*[@id="editgrid-syscheck-0"]')
				sleep(1)
				
				span_click("生成上划单")
				ok_click()
				# 退出所有窗体
				switch_default()
				implici_wait("xpath", "//span[contains(text(),'生成上划单成功！')]")
				if i == 3:
					print("资金上划设置--按比例上划，生成上划单成功！")
				click("xpath", "//span[text()='资金上划处理']")
				sleep(3)
			
			# 测试删除功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="collectionHandle-tab-iframe"]')
			span_click("按比例上划")
			switch_to("xpath", '//*[@id="subTabThree-iframe"]')
			sleep(1)
			
			# 勾选按钮
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("删除")
			ok_click()
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'删除操作成功！')]")
			print("资金上划设置--按比例上划，删除成功！")
			click("xpath", "//span[text()='资金上划处理']")
			sleep(3)
			
			# 测试作废功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="collectionHandle-tab-iframe"]')
			span_click("按比例上划")
			switch_to("xpath", '//*[@id="subTabThree-iframe"]')
			sleep(1)
			
			# 勾选按钮
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("作废")
			ok_click()
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("资金上划设置--按比例上划，作废成功！")
			click("xpath", "//span[text()='资金上划处理']")
			sleep(3)
			
			# 测试上划状态查询功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="collectionHandle-tab-iframe"]')
			span_click("按比例上划")
			switch_to("xpath", '//*[@id="subTabThree-iframe"]')
			sleep(1)
			
			# 勾选按钮
			click("xpath", '//*[@id="t1_t2-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("上划状态查询")
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'单据已查询状态，请查看相应结果')]")
			print("资金上划设置--按比例上划，上划状态查询成功！")
			click("xpath", "//span[text()='资金上划处理']")
			sleep(3)
			
			# 测试送审功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="collectionHandle-tab-iframe"]')
			span_click("按比例上划")
			switch_to("xpath", '//*[@id="subTabThree-iframe"]')
			sleep(1)
			
			# 勾选按钮
			click("xpath", '//*[@id="t1_t1-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("送审")
			
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'成功送审1笔，失败0笔。')]")
			print("资金上划设置--按比例上划，送审成功！")
			click("xpath", "//span[text()='资金上划处理']")
			sleep(3)
			
			# 测试审批历史💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="collectionHandle-tab-iframe"]')
			span_click("按比例上划")
			switch_to("xpath", '//*[@id="subTabThree-iframe"]')
			sleep(1)
			
			# 一审
			# 勾选按钮
			double_click("xpath", '//*[@id="t1_t1"]/td[1]/div')
			sleep(1)
			
			switch_to("xpath", '//*[@id="wf_taskProcessing_win-iframe"]')
			sleep(1)
			
			span_click("同意")
			switch_parent()
			sleep(3)
			
			# 二审
			# 勾选按钮
			double_click("xpath", '//*[@id="t1_t1"]/td[1]/div')
			sleep(1)
			
			switch_to("xpath", '//*[@id="wf_taskProcessing_win-iframe"]')
			sleep(1)
			
			span_click("同意")
			switch_parent()
			sleep(3)
			
			# 勾选按钮
			click("xpath", '//*[@id="t1_t1-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("审批历史")
			switch_to("xpath", '//*[@id="flowwin-iframe"]')
			sleep(1)
			implici_wait("xpath", "//span[contains(text(),'流程图')]")
			print("资金上划设置--按比例上划，审批历史查看成功！")
			# 退出所有窗体
			switch_default()
			click("xpath", "//span[text()='资金上划处理']")
			sleep(3)
			
			# 测试上划功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="collectionHandle-tab-iframe"]')
			span_click("按比例上划")
			switch_to("xpath", '//*[@id="subTabThree-iframe"]')
			sleep(1)
			
			# 勾选按钮
			click("xpath", '//*[@id="t1_t1-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("上划")
			
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'上划操作成功！')]")
			print("资金上划设置--按比例上划，上划成功！")
			click("xpath", "//span[text()='资金上划处理']")
			sleep(3)
			
			# 测试上划日志查看功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="collectionHandle-tab-iframe"]')
			span_click("按比例上划")
			switch_to("xpath", '//*[@id="subTabThree-iframe"]')
			sleep(1)
			
			# 勾选按钮
			click("xpath", '//*[@id="t1_t1-fixed"]/td[1]/div/span')
			sleep(1)
			click("xpath", '//*[@id="t1_t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("上划日志查看")
			switch_to("xpath", '//*[@id="logsWin-iframe"]')
			implici_wait("xpath", "//div[contains(text(),'支付')]")
			print("资金上划设置--按比例上划，上划日志查看成功！")
			# 退出所有窗体
			switch_default()
			click("xpath", "//span[text()='资金上划处理']")
			sleep(3)
			
			# 测试确认已上划💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			sql = "update t_se_payments set paystate = '7' where ourbankaccountname like '%账户2021%'"
			ora_sql(ora_ip, ora_sid, ora_user, ora_pwd,
			       sql)
			sleep(1
			      )
			switch_to("xpath", '//*[@id="collectionHandle-tab-iframe"]')
			span_click("按比例上划")
			switch_to("xpath", '//*[@id="subTabThree-iframe"]')
			sleep(1)
			
			# 勾选按钮
			
			click("xpath", '//*[@id="t1_t1-fixed"]/td[2]/div')
			sleep(1)
			
			span_click("确认已上划")
			ok_click()
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("资金上划设置--按比例上划，确认已上划成功！")
			# 退出所有窗体
			switch_default()
			click("xpath", "//span[text()='资金上划处理']")
			sleep(3)
			
			# 回到初始界面
			click("xpath", "//span[text()='资金池上划管理']")
			sleep(1)
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("按比例上划失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
			
			# def tearDown(self):
			#     self.driver.quit()
			print("结束时间：", time.strftime("%Y-%m-%d %H:%M:%S"))
		
		# 测试资金池上划处理--异常资金上划🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱
		try:
			logger.info("测试资金池上划管理--资金上划设置")
			switch_default()
			click("xpath", "//span[text()='资金池上划管理']")
			sleep(1)
			click("xpath", "//span[text()='资金上划处理']")
			sleep(1)
			switch_default()
			sleep(3)
			
			# 查询今日明细💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			click("xpath", "//span[text()='资金池上划管理']")
			sleep(1)
			js_click("xpath", "//span[contains(text(),'内部资金池')]")
			sleep(1)
		
			refresh()
			js_gd("xpath", "//span[contains(text(),'账户资金监控')]")
			# 用JS的方法点击账户资金监控菜单
			js_click("xpath", "//span[contains(text(),'账户资金监控')]")
			sleep(1)
			click("xpath", "//span[text()='直联账户查询']")
			sleep(1)
			
			#切入所有可操作组织窗体
			switch_to("xpath",'//*[@id="directBankAccountQuery-tab-iframe"]')
			span_click("所有可操作组织查询")
			switch_to("xpath",'//*[@id="subTabTwo-iframe"]')
			#查询
			click("xpath",'//*[@id="north"]/div[2]/span')
			sleep(1)
			click("xpath",'//*[@id="combobox-input-orgid"]')
			sleep(1)
			click("xpath", '//*[@id="orgid-combogrid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			click("xpath", '//*[@id="orgid-combogrid-body-table"]/tbody/tr[2]/td[2]/div/button')
			sleep(1)
			
			span_click("查询")
			click("xpath",'//*[@id="grid-head-table"]/thead/tr/th[2]/div')
			sleep(1)
			span_click("今日明细查询")
			implici_wait("xpath", "//span[contains(text(),'今日明细查询-查询成功')]")
			switch_default()
			
			js_gd("xpath", "//span[contains(text(),'账户资金监控')]")
			# 用JS的方法点击账户资金监控菜单
			js_click("xpath", "//span[contains(text(),'账户资金监控')]")
			sleep(1)
			js_click("xpath", "//span[contains(text(),'内部资金池')]")
			sleep(1)
			click("xpath", "//span[text()='资金池上划管理']")
			sleep(1)
			click("xpath", "//span[text()='资金上划处理']")
			sleep(1)
			
			# 余额查询💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="collectionHandle-tab-iframe"]')
			span_click("异常资金上划")
			switch_to("xpath", '//*[@id="subTabFour-iframe"]')
			sleep(1)
			
			# 上划模板
			clear("xpath", '//*[@id="combobox-input-collectionruleid"]')
			sleep(1)
			click("xpath", '//*[@id="combobox-input-collectionruleid"]')
			sleep(1)
			click("xpath", '//*[@id="collectionruleid-combogrid-body-table"]/tbody/tr/td[2]/div')
			sleep(1)
			
			# 勾选按钮
			click("xpath", '//*[@id="editgrid-syscheck-0"]')
			sleep(1)
			
			span_click("余额查询")
			
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'当前银行可用余额')]")
			print("资金上划设置--异常资金上划，余额查询成功！")
			click("xpath", "//span[text()='资金上划处理']")
			sleep(3)
			
			# 测试立即上划功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="collectionHandle-tab-iframe"]')
			span_click("异常资金上划")
			switch_to("xpath", '//*[@id="subTabFour-iframe"]')
			sleep(1)
			
			# 上划模板
			clear("xpath", '//*[@id="combobox-input-collectionruleid"]')
			sleep(1)
			click("xpath", '//*[@id="combobox-input-collectionruleid"]')
			sleep(1)
			click("xpath", '//*[@id="collectionruleid-combogrid-body-table"]/tbody/tr/td[2]/div')
			sleep(1)
			
			# 开始日期
			click("xpath", '//*[@id="startdate-trigger"]')
			sleep(1)
			switch_default()
			switch_to("xpath", '/html/body/div[6]/iframe')
			click("xpath", '//*[@id="dpTodayInput"]')
			sleep(1)
			switch_default()
			switch_to("xpath", '//*[@id="collectionHandle-tab-iframe"]')
			span_click("异常资金上划")
			switch_to("xpath", '//*[@id="subTabFour-iframe"]')
			sleep(1)
			
			# 结束日期
			click("xpath", '//*[@id="enddate-trigger"]')
			sleep(1)
			switch_default()
			switch_to("xpath", '/html/body/div[6]/iframe')
			click("xpath", '//*[@id="dpTodayInput"]')
			sleep(1)
			switch_default()
			switch_to("xpath", '//*[@id="collectionHandle-tab-iframe"]')
			span_click("异常资金上划")
			switch_to("xpath", '//*[@id="subTabFour-iframe"]')
			sleep(1)
			
			
			# 勾选按钮
			click("xpath", '//*[@id="editgrid-syscheck-0"]')
			sleep(1)
			
			span_click("立即上划")
			ok_click()
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'生成上划单成功！')]")
			print("资金上划设置--异常资金上划，立即上划成功！")
			click("xpath", "//span[text()='资金上划处理']")
			sleep(3)
			
			# 测试生成上划单功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			for i in range(1, 4):
				switch_to("xpath", '//*[@id="collectionHandle-tab-iframe"]')
				span_click("异常资金上划")
				switch_to("xpath", '//*[@id="subTabFour-iframe"]')
				sleep(1)
				
				# 上划模板
				clear("xpath", '//*[@id="combobox-input-collectionruleid"]')
				sleep(1)
				click("xpath", '//*[@id="combobox-input-collectionruleid"]')
				sleep(1)
				click("xpath", '//*[@id="collectionruleid-combogrid-body-table"]/tbody/tr/td[2]/div')
				sleep(1)
				
				#开始日期
				click("xpath",'//*[@id="startdate-trigger"]')
				sleep(1)
				switch_default()
				switch_to("xpath",'/html/body/div[6]/iframe')
				click("xpath",'//*[@id="dpTodayInput"]')
				sleep(1)
				switch_default()
				switch_to("xpath", '//*[@id="collectionHandle-tab-iframe"]')
				span_click("异常资金上划")
				switch_to("xpath", '//*[@id="subTabFour-iframe"]')
				sleep(1)
				
				#结束日期
				click("xpath", '//*[@id="enddate-trigger"]')
				sleep(1)
				switch_default()
				switch_to("xpath", '/html/body/div[6]/iframe')
				click("xpath", '//*[@id="dpTodayInput"]')
				sleep(1)
				switch_default()
				switch_to("xpath", '//*[@id="collectionHandle-tab-iframe"]')
				span_click("异常资金上划")
				switch_to("xpath", '//*[@id="subTabFour-iframe"]')
				sleep(1)
				
				
				
				if i ==1 :
					clear("xpath",'//*[@id="combobox-input-editgrid-accountid-0"]')
					sleep(1)
					click("xpath",'//*[@id="combobox-input-editgrid-accountid-0"]')
					sleep(1)
					click("xpath",'//*[@id="editgrid-accountid-0-combogrid-body-table"]/tbody/tr[3]/td[2]/div')
					sleep(1)
				if i == 2:
					clear("xpath", '//*[@id="combobox-input-editgrid-accountid-0"]')
					sleep(1)
					click("xpath", '//*[@id="combobox-input-editgrid-accountid-0"]')
					sleep(1)
					click("xpath", '//*[@id="editgrid-accountid-0-combogrid-body-table"]/tbody/tr[4]/td[2]/div')
					sleep(1)
				if i == 3:
					clear("xpath", '//*[@id="combobox-input-editgrid-accountid-0"]')
					sleep(1)
					click("xpath", '//*[@id="combobox-input-editgrid-accountid-0"]')
					sleep(1)
					click("xpath", '//*[@id="editgrid-accountid-0-combogrid-body-table"]/tbody/tr[5]/td[2]/div')
					sleep(1)
					
				
				
				
				# 勾选按钮
				click("xpath", '//*[@id="editgrid-syscheck-0"]')
				sleep(1)
				
				span_click("生成上划单")
				ok_click()
				# 退出所有窗体
				switch_default()
				implici_wait("xpath", "//span[contains(text(),'生成上划单成功！')]")
				if i == 3:
					print("资金上划设置--异常资金上划，生成上划单成功！")
				click("xpath", "//span[text()='资金上划处理']")
				sleep(3)
			
			# 测试删除功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="collectionHandle-tab-iframe"]')
			span_click("异常资金上划")
			switch_to("xpath", '//*[@id="subTabFour-iframe"]')
			sleep(1)
			
			# 勾选按钮
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("删除")
			ok_click()
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'删除操作成功！')]")
			print("资金上划设置--异常资金上划，删除成功！")
			click("xpath", "//span[text()='资金上划处理']")
			sleep(3)
			
			# 测试作废功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="collectionHandle-tab-iframe"]')
			span_click("异常资金上划")
			switch_to("xpath", '//*[@id="subTabFour-iframe"]')
			sleep(1)
			
			# 勾选按钮
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("作废")
			ok_click()
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("资金上划设置--异常资金上划，作废成功！")
			click("xpath", "//span[text()='资金上划处理']")
			sleep(3)
			
			# 测试上划状态查询功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="collectionHandle-tab-iframe"]')
			span_click("异常资金上划")
			switch_to("xpath", '//*[@id="subTabFour-iframe"]')
			sleep(1)
			
			# 勾选按钮
			click("xpath", '//*[@id="t1_t2-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("上划状态查询")
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'单据已查询状态，请查看相应结果')]")
			print("资金上划设置--异常资金上划，上划状态查询成功！")
			click("xpath", "//span[text()='资金上划处理']")
			sleep(3)
			
			# 测试送审功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="collectionHandle-tab-iframe"]')
			span_click("异常资金上划")
			switch_to("xpath", '//*[@id="subTabFour-iframe"]')
			sleep(1)
			
			# 勾选按钮
			click("xpath", '//*[@id="t1_t1-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("送审")
			
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'成功送审1笔，失败0笔。')]")
			print("资金上划设置--异常资金上划，送审成功！")
			click("xpath", "//span[text()='资金上划处理']")
			sleep(3)
			
			# 测试审批历史💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="collectionHandle-tab-iframe"]')
			span_click("异常资金上划")
			switch_to("xpath", '//*[@id="subTabFour-iframe"]')
			sleep(1)
			
			# 一审
			# 勾选按钮
			double_click("xpath", '//*[@id="t1_t1"]/td[2]/div/span')
			sleep(1)
			
			switch_to("xpath", '//*[@id="wf_taskProcessing_win-iframe"]')
			sleep(1)
			
			span_click("同意")
			switch_parent()
			sleep(3)
			
			# 二审
			# 勾选按钮
			double_click("xpath", '//*[@id="t1_t1"]/td[2]/div/span')
			sleep(1)
			
			switch_to("xpath", '//*[@id="wf_taskProcessing_win-iframe"]')
			sleep(1)
			
			span_click("同意")
			switch_parent()
			sleep(3)
			
			# 勾选按钮
			click("xpath", '//*[@id="t1_t1-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("审批历史")
			switch_to("xpath", '//*[@id="flowwin-iframe"]')
			sleep(1)
			implici_wait("xpath", "//span[contains(text(),'流程图')]")
			print("资金上划设置--异常资金上划，审批历史查看成功！")
			# 退出所有窗体
			switch_default()
			click("xpath", "//span[text()='资金上划处理']")
			sleep(3)
			
			# 测试上划功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="collectionHandle-tab-iframe"]')
			span_click("异常资金上划")
			switch_to("xpath", '//*[@id="subTabFour-iframe"]')
			sleep(1)
			
			# 勾选按钮
			click("xpath", '//*[@id="t1_t1-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("上划")
			
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'上划操作成功！')]")
			print("资金上划设置--异常资金上划，上划成功！")
			click("xpath", "//span[text()='资金上划处理']")
			sleep(3)
			
			# 测试上划日志查看功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="collectionHandle-tab-iframe"]')
			span_click("异常资金上划")
			switch_to("xpath", '//*[@id="subTabFour-iframe"]')
			sleep(1)
			
			# 勾选按钮
			click("xpath", '//*[@id="t1_t1-fixed"]/td[1]/div/span')
			sleep(1)
			click("xpath", '//*[@id="t1_t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("上划日志查看")
			switch_to("xpath", '//*[@id="logsWin-iframe"]')
			implici_wait("xpath", "//div[contains(text(),'支付')]")
			print("资金上划设置--异常资金上划，上划日志查看成功！")
			# 退出所有窗体
			switch_default()
			click("xpath", "//span[text()='资金上划处理']")
			sleep(3)
			
			# 测试确认已上划💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			sql = "update t_se_payments set paystate = '7' where ourbankaccountname like '%账户2021%'"
			ora_sql(ora_ip, ora_sid, ora_user, ora_pwd,
			       sql)
			sleep(1
			      )
			switch_to("xpath", '//*[@id="collectionHandle-tab-iframe"]')
			span_click("异常资金上划")
			switch_to("xpath", '//*[@id="subTabFour-iframe"]')
			sleep(1)
			
			# 勾选按钮
			
			click("xpath", '//*[@id="t1_t1-fixed"]/td[2]/div')
			sleep(1)
			
			span_click("确认已上划")
			ok_click()
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("资金上划设置--异常资金上划，确认已上划成功！")
			# 退出所有窗体
			switch_default()
			click("xpath", "//span[text()='资金上划处理']")
			sleep(3)
			
			# 回到初始界面
			click("xpath", "//span[text()='资金池上划管理']")
			sleep(1)
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("异常资金上划失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
			
			# def tearDown(self):
			#     self.driver.quit()
			print("结束时间：", time.strftime("%Y-%m-%d %H:%M:%S"))
		
		
		
		# 测试资金池上划处理--组织留底上划🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱
		try:
			logger.info("测试资金池上划管理--资金上划设置")
			switch_default()
			click("xpath", "//span[text()='资金池上划管理']")
			sleep(1)
			click("xpath", "//span[text()='资金上划处理']")
			sleep(1)
			switch_default()
			sleep(3)
			
			
			
			# 测试立即上划功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="collectionHandle-tab-iframe"]')
			span_click("组织留底上划")
			switch_to("xpath", '//*[@id="subTabFive-iframe"]')
			sleep(1)
			
			# 上划模板
			clear("xpath", '//*[@id="combobox-input-collectionruleid"]')
			sleep(1)
			click("xpath", '//*[@id="combobox-input-collectionruleid"]')
			sleep(1)
			click("xpath", '//*[@id="collectionruleid-combogrid-body-table"]/tbody/tr/td[2]/div')
			sleep(1)
			
			# 勾选按钮
			click("xpath", '//*[@id="editgrid-syscheck-0"]')
			sleep(1)
			
			span_click("立即上划")
			ok_click()
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'生成上划单成功！')]")
			print("资金上划设置--组织留底上划，余额查询成功！")
			click("xpath", "//span[text()='资金上划处理']")
			sleep(3)
			
			# 测试生成上划单功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			for i in range(1, 4):
				switch_to("xpath", '//*[@id="collectionHandle-tab-iframe"]')
				span_click("组织留底上划")
				switch_to("xpath", '//*[@id="subTabFive-iframe"]')
				sleep(1)
				
				# 上划模板
				clear("xpath", '//*[@id="combobox-input-collectionruleid"]')
				sleep(1)
				click("xpath", '//*[@id="combobox-input-collectionruleid"]')
				sleep(1)
				click("xpath", '//*[@id="collectionruleid-combogrid-body-table"]/tbody/tr/td[2]/div')
				sleep(1)
				
				# 勾选按钮
				click("xpath", '//*[@id="editgrid-syscheck-0"]')
				sleep(1)
				
				span_click("生成上划单")
				ok_click()
				# 退出所有窗体
				switch_default()
				implici_wait("xpath", "//span[contains(text(),'生成上划单成功！')]")
				if i == 3:
					print("资金上划设置--组织留底上划，生成上划单成功！")
				click("xpath", "//span[text()='资金上划处理']")
				sleep(3)
			
			# 测试删除功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="collectionHandle-tab-iframe"]')
			span_click("组织留底上划")
			switch_to("xpath", '//*[@id="subTabFive-iframe"]')
			sleep(1)
			
			# 勾选按钮
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("删除")
			ok_click()
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'删除操作成功！')]")
			print("资金上划设置--组织留底上划，删除成功！")
			click("xpath", "//span[text()='资金上划处理']")
			sleep(3)
			
			# 测试作废功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="collectionHandle-tab-iframe"]')
			span_click("组织留底上划")
			switch_to("xpath", '//*[@id="subTabFive-iframe"]')
			sleep(1)
			
			# 勾选按钮
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("作废")
			ok_click()
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("资金上划设置--组织留底上划，作废成功！")
			click("xpath", "//span[text()='资金上划处理']")
			sleep(3)
			
			# 测试上划状态查询功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="collectionHandle-tab-iframe"]')
			span_click("组织留底上划")
			switch_to("xpath", '//*[@id="subTabFive-iframe"]')
			sleep(1)
			
			# 勾选按钮
			click("xpath", '//*[@id="t1_t2-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("上划状态查询")
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'单据已查询状态，请查看相应结果')]")
			print("资金上划设置--组织留底上划，上划状态查询成功！")
			click("xpath", "//span[text()='资金上划处理']")
			sleep(3)
			
			# 测试送审功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="collectionHandle-tab-iframe"]')
			span_click("组织留底上划")
			switch_to("xpath", '//*[@id="subTabFive-iframe"]')
			sleep(1)
			
			# 勾选按钮
			click("xpath", '//*[@id="t1_t1-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("送审")
			
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'成功送审1笔，失败0笔。')]")
			print("资金上划设置--组织留底上划，送审成功！")
			click("xpath", "//span[text()='资金上划处理']")
			sleep(3)
			
			# 测试审批历史💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="collectionHandle-tab-iframe"]')
			span_click("组织留底上划")
			switch_to("xpath", '//*[@id="subTabFive-iframe"]')
			sleep(1)
			
			# 一审
			# 勾选按钮
			double_click("xpath", '//*[@id="t1_t1"]/td[1]/div')
			sleep(1)
			
			switch_to("xpath", '//*[@id="wf_taskProcessing_win-iframe"]')
			sleep(1)
			
			span_click("同意")
			switch_parent()
			sleep(3)
			
			# 二审
			# 勾选按钮
			double_click("xpath", '//*[@id="t1_t1"]/td[1]/div')
			sleep(1)
			
			switch_to("xpath", '//*[@id="wf_taskProcessing_win-iframe"]')
			sleep(1)
			
			span_click("同意")
			switch_parent()
			sleep(3)
			
			# 勾选按钮
			click("xpath", '//*[@id="t1_t1-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("审批历史")
			switch_to("xpath", '//*[@id="flowwin-iframe"]')
			sleep(1)
			implici_wait("xpath", "//span[contains(text(),'流程图')]")
			print("资金上划设置--组织留底上划，审批历史查看成功！")
			# 退出所有窗体
			switch_default()
			click("xpath", "//span[text()='资金上划处理']")
			sleep(3)
			
			# 测试上划功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="collectionHandle-tab-iframe"]')
			span_click("组织留底上划")
			switch_to("xpath", '//*[@id="subTabFive-iframe"]')
			sleep(1)
			
			# 勾选按钮
			click("xpath", '//*[@id="t1_t1-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("上划")
			
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'上划操作成功！')]")
			print("资金上划设置--组织留底上划，上划成功！")
			click("xpath", "//span[text()='资金上划处理']")
			sleep(3)
			
			# 测试上划日志查看功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="collectionHandle-tab-iframe"]')
			span_click("组织留底上划")
			switch_to("xpath", '//*[@id="subTabFive-iframe"]')
			sleep(1)
			
			# 勾选按钮
			click("xpath", '//*[@id="t1_t1-fixed"]/td[1]/div/span')
			sleep(1)
			click("xpath", '//*[@id="t1_t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("上划日志查看")
			switch_to("xpath", '//*[@id="logsWin-iframe"]')
			implici_wait("xpath", "//div[contains(text(),'支付')]")
			print("资金上划设置--组织留底上划，上划日志查看成功！")
			# 退出所有窗体
			switch_default()
			click("xpath", "//span[text()='资金上划处理']")
			sleep(3)
			
			# 测试确认已上划💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			sql = "update t_se_payments set paystate = '7' where ourbankaccountname like '%账户2021%'"
			ora_sql(ora_ip, ora_sid, ora_user, ora_pwd,
			       sql)
			sleep(1)
			switch_to("xpath", '//*[@id="collectionHandle-tab-iframe"]')
			span_click("组织留底上划")
			switch_to("xpath", '//*[@id="subTabFive-iframe"]')
			sleep(1)
			
			# 勾选按钮
			
			click("xpath", '//*[@id="t1_t1-fixed"]/td[2]/div')
			sleep(1)
			
			span_click("确认已上划")
			ok_click()
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("资金上划设置--组织留底上划，确认已上划成功！")
			# 退出所有窗体
			switch_default()
			click("xpath", "//span[text()='资金上划处理']")
			sleep(3)
			
			# 回到初始界面
			click("xpath", "//span[text()='资金池上划管理']")
			sleep(1)
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("组织留底上划失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
			
			# def tearDown(self):
			#     self.driver.quit()
			print("结束时间：", time.strftime("%Y-%m-%d %H:%M:%S"))
		
		
		# 测试资金下拨设置--资金申请类型🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱
		try:
			logger.info("测试资金下拨设置--资金申请类型")
			switch_default()
			click("xpath", "//span[text()='资金池下拨管理']")
			sleep(1)
			click("xpath", "//span[text()='资金下拨设置']")
			sleep(1)
			switch_default()
			sleep(3)
			
			#测试新增功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			for i in range (1,3):
				switch_to("xpath", '//*[@id="allocationSetting-tab-iframe"]')
				switch_to("xpath", '//*[@id="subTabOne-iframe"]')
				sleep(1)
				
				span_click("新增")
				switch_to("xpath",'//*[@id="addWin-iframe"]')
				
				#代码
				coad = str(time.strftime("%Y%m%d%H%M%S"))
				input("xpath",'//*[@id="code"]',coad)
				sleep(1)
				
				#名称
				name = "ZJSQLX" + str(time.strftime("%Y%S"))
				input("xpath", '//*[@id="name"]', name)
				sleep(1)
				
				span_click("保存")
				switch_default()
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				if i == 2:
					print("资金下拨设置--资金申请类型，新增成功！")
				click("xpath", "//span[text()='资金下拨设置']")
				sleep(3)
				
			# 测试修改功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="allocationSetting-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			#刷新、勾选按钮
			click("xpath",'//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath",'//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("修改")
			switch_to("xpath",'//*[@id="modWin-iframe"]')
			
			#备注
			input("xpath",'//*[@id="description"]','测试修改')
			sleep(1)
			
			span_click("保存")
			
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("资金下拨设置--资金申请类型，修改成功！")
			click("xpath", "//span[text()='资金下拨设置']")
			sleep(3)
			
			# 测试删除功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="allocationSetting-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("删除")
			ok_click()
		
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("资金下拨设置--资金申请类型，删除成功！")
			click("xpath", "//span[text()='资金下拨设置']")
			sleep(3)
			
			# 测试失效功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="allocationSetting-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("失效")
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'失效成功！')]")
			print("资金下拨设置--资金申请类型，失效成功！")
			click("xpath", "//span[text()='资金下拨设置']")
			sleep(3)
			
			# 测试生效功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="allocationSetting-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("生效")
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'生效成功！')]")
			print("资金下拨设置--资金申请类型，生效成功！")
			click("xpath", "//span[text()='资金下拨设置']")
			sleep(3)
			
			# 回到初始界面
			click("xpath", "//span[text()='资金池下拨管理']")
			sleep(1)
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("资金申请类型失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
			
			# def tearDown(self):
			#     self.driver.quit()
			print("结束时间：", time.strftime("%Y-%m-%d %H:%M:%S"))
		
		
		# 测试资金下拨设置--下拨顺序🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱
		try:
			logger.info("测试资金下拨设置--下拨顺序")
			switch_default()
			click("xpath", "//span[text()='资金池下拨管理']")
			sleep(1)
			click("xpath", "//span[text()='资金下拨设置']")
			sleep(1)
			switch_default()
			sleep(3)
			
			# 测试配置功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="allocationSetting-tab-iframe"]')
			span_click("下拨顺序")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("配置")
			switch_to("xpath", '//*[@id="orderDetail-iframe"]')
	
			span_click("保存")
			
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("资金下拨设置--下拨顺序，配置成功！")
			click("xpath", "//span[text()='资金下拨设置']")
			sleep(3)
			
			# 测试下移功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="allocationSetting-tab-iframe"]')
			span_click("下拨顺序")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("下移")
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("资金下拨设置--下拨顺序，下移成功！")
			click("xpath", "//span[text()='资金下拨设置']")
			sleep(3)
			
			# 测试上移功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="allocationSetting-tab-iframe"]')
			span_click("下拨顺序")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[2]/td[2]/div/button')
			sleep(1)
			
			span_click("上移")
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("资金下拨设置--下拨顺序，上移成功！")
			click("xpath", "//span[text()='资金下拨设置']")
			sleep(3)
			
			# 测试失效功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="allocationSetting-tab-iframe"]')
			span_click("下拨顺序")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[2]/td[2]/div/button')
			sleep(1)
			
			span_click("失效")
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'失效成功！')]")
			print("资金下拨设置--下拨顺序，失效成功！")
			click("xpath", "//span[text()='资金下拨设置']")
			sleep(3)
			
			# 测试生效功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="allocationSetting-tab-iframe"]')
			span_click("下拨顺序")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[2]/td[2]/div/button')
			sleep(1)
			
			span_click("生效")
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'生效成功！')]")
			print("资金下拨设置--下拨顺序，生效成功！")
			click("xpath", "//span[text()='资金下拨设置']")
			sleep(3)
			
			# 回到初始界面
			click("xpath", "//span[text()='资金池下拨管理']")
			sleep(1)
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("组织留底上划失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
			
			# def tearDown(self):
			#     self.driver.quit()
			print("结束时间：", time.strftime("%Y-%m-%d %H:%M:%S"))
		
		
		# 测试资金下拨设置--下拨方案🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱
		try:
			logger.info("测试资金下拨设置--下拨方案")
			switch_default()
			click("xpath", "//span[text()='资金池下拨管理']")
			sleep(1)
			click("xpath", "//span[text()='资金下拨设置']")
			sleep(1)
			switch_default()
			sleep(3)
			
			# 测试新增功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			for i in range (1,3):
				switch_to("xpath", '//*[@id="allocationSetting-tab-iframe"]')
				span_click("下拨方案")
				switch_to("xpath", '//*[@id="subTabThree-iframe"]')
				sleep(1)
				
				span_click("新增")
				switch_to("xpath",'//*[@id="addWin-iframe"]')
				
				#代码
				code = str(time.strftime("%Y%m%d%H%M%S"))
				input("xpath",'//*[@id="code"]',code)
				sleep(1)
				
				# 名称
				name ="下拨方案"+ str(time.strftime("%Y%S"))
				input("xpath", '//*[@id="name"]', name)
				sleep(1)
				
				#播出户设置
				click("xpath",'//*[@id="gridbar"]/div/div[1]/table/tbody/tr/td[1]/span')
				sleep(1)
				
				#顺序号
				input("xpath",'//*[@id="allocateSchemePayDef-serialno-0"]','01')
				sleep(1)
				
				#拨出组织
				input_up_click('//*[@id="combobox-input-allocateSchemePayDef-orgid-0"]','001010-亚唐科技')
				
				#拨出账号
				click_up_click('//*[@id="combobox-input-allocateSchemePayDef-accountid-0"]')
				
				#余额不足处理
				input_up_click('//*[@id="combobox-input-allocateSchemePayDef-lackdeal-0"]','不下拨')
				
				# 结算方式
				input_up_click('//*[@id="combobox-input-allocateSchemePayDef-settlementmodeid-0"]', '101-直联单笔转账')
				
				#拨入户设置
				span_click('拨入户设置')
				click("xpath",'/html/body/form/div[2]/div[2]/ul/li[2]/div/div/div/div/ul/div[1]/div[3]/div/div[1]/table/tbody/tr/td[1]/span')
				sleep(1)
				
				#拨入组织
				input_up_click('//*[@id="combobox-input-allocateSchemeRecDef-orgid-0"]','Mindy科技有限公司')
				
				#拨入账户
				click("xpath",'//*[@id="combobox-input-allocateSchemeRecDef-accountid-0"]')
				sleep(1)
				if i ==1 :
					click("xpath",'//*[@id="allocateSchemeRecDef-accountid-0-combogrid-body-table"]/tbody/tr[4]/td[2]/div')
					sleep(1)
				if i ==2 :
					click("xpath",'//*[@id="allocateSchemeRecDef-accountid-0-combogrid-body-table"]/tbody/tr[3]/td[2]/div')
					sleep(1)
				
				
				span_click("保存")
				# 退出所有窗体
				switch_default()
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				if i == 2 :
					print("资金下拨设置--下拨方案，新增成功！")
				sleep(3)
				
			# 测试修改功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="allocationSetting-tab-iframe"]')
			span_click("下拨方案")
			switch_to("xpath", '//*[@id="subTabThree-iframe"]')
			sleep(1)
			
			#刷新、勾选按钮
			click("xpath",'//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath",'//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("修改")
			switch_to("xpath",'//*[@id="modWin-iframe"]')
			sleep(1)
			span_click("保存")
			
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("资金下拨设置--下拨顺序，修改成功！")
			sleep(3)
			
			# 测试删除功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="allocationSetting-tab-iframe"]')
			span_click("下拨方案")
			switch_to("xpath", '//*[@id="subTabThree-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("删除")
			ok_click()
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("资金下拨设置--下拨顺序，删除成功！")
			sleep(3)
			
			# 测试失效功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="allocationSetting-tab-iframe"]')
			span_click("下拨方案")
			switch_to("xpath", '//*[@id="subTabThree-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("失效")
			
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'失效成功！')]")
			print("资金下拨设置--下拨顺序，失效成功！")
			sleep(3)
			
			# 测试生效功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="allocationSetting-tab-iframe"]')
			span_click("下拨方案")
			switch_to("xpath", '//*[@id="subTabThree-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("生效")
			
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'生效成功！')]")
			print("资金下拨设置--下拨顺序，生效成功！")
			sleep(3)
			
			
			# 回到初始界面
			click("xpath", "//span[text()='资金池下拨管理']")
			sleep(1)
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("下拨方案失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
			
			# def tearDown(self):
			#     self.driver.quit()
			print("结束时间：", time.strftime("%Y-%m-%d %H:%M:%S"))
		
		
		# 测试资金下拨设置--下拨规则🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱
		try:
			logger.info("测试资金下拨设置--下拨规则")
			switch_default()
			click("xpath", "//span[text()='资金池下拨管理']")
			sleep(1)
			click("xpath", "//span[text()='资金下拨设置']")
			sleep(1)
			switch_default()
			sleep(3)
			
			# 测试新增功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			for i in range(1, 4):
				switch_to("xpath", '//*[@id="allocationSetting-tab-iframe"]')
				span_click("下拨规则")
				switch_to("xpath", '//*[@id="subTabFour-iframe"]')
				sleep(1)
				
				span_click("新增")
				switch_to("xpath",'//*[@id="addWin-iframe"]')
				
				#名称
				name = "下拨规则"+time.strftime("%Y%M%S")
				input("xpath",'//*[@id="name"]',str(name))
				sleep(1)
				
				if i ==1 :
					#下拨模式
					input_up_click('//*[@id="combobox-input-allocatemode"]','定额下拨')
					
					#新增行
					click("xpath",'//*[@id="gridbar"]/div/div[1]/table/tbody/tr/td[1]/span')
					sleep(1)
					
					#拨入组织
					input_up_click('//*[@id="combobox-input-ruleegrid-orgid-0"]','Mindy科技有限公司')
					
					#拨入账户
					click("xpath",'//*[@id="combobox-input-ruleegrid-accountid-0"]')
					sleep(1)
					click("xpath", '//*[@id="ruleegrid-accountid-0-combogrid-body-table"]/tbody/tr[1]/td[2]/div')
					sleep(1)
					
					#拨入金额
					double_click("xpath",'//*[@id="ruleegrid-allocatevalue-0-input"]')
					sleep(1)
					input("xpath",'//*[@id="ruleegrid-allocatevalue-0-input"]','100')
					sleep(1)
					
					span_click("保存")
					# 退出所有窗体
					switch_default()
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					sleep(3)
					
					switch_to("xpath", '//*[@id="allocationSetting-tab-iframe"]')
					span_click("下拨规则")
					switch_to("xpath", '//*[@id="subTabFour-iframe"]')
					sleep(1)
					
					#勾选按钮
					click("xpath",'//*[@id="t1_t0-fixed"]/td[2]/div/button')
					sleep(1)
					span_click("删除")
					ok_click()
					
					# 退出所有窗体
					switch_default()
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("资金下拨设置--下拨顺序，删除成功！")
					sleep(3)
				if i ==2 :
					# 下拨模式
					input_up_click('//*[@id="combobox-input-allocatemode"]', '定额下拨')
					
					# 新增行
					click("xpath", '//*[@id="gridbar"]/div/div[1]/table/tbody/tr/td[1]/span')
					sleep(1)
					
					# 拨入组织
					input_up_click('//*[@id="combobox-input-ruleegrid-orgid-0"]', 'Mindy科技有限公司')
					
					# 拨入账户
					click("xpath", '//*[@id="combobox-input-ruleegrid-accountid-0"]')
					sleep(1)
					click("xpath", '//*[@id="ruleegrid-accountid-0-combogrid-body-table"]/tbody/tr[1]/td[2]/div')
					sleep(1)
					
					# 拨入金额
					double_click("xpath", '//*[@id="ruleegrid-allocatevalue-0-input"]')
					sleep(1)
					input("xpath", '//*[@id="ruleegrid-allocatevalue-0-input"]', '100')
					sleep(1)
					
					span_click("保存")
					# 退出所有窗体
					switch_default()
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					sleep(3)
					
				if i == 3:
					# 下拨模式
					input_up_click('//*[@id="combobox-input-allocatemode"]', '留底下拨')
					
					# 新增行
					click("xpath", '//*[@id="gridbar"]/div/div[1]/table/tbody/tr/td[1]/span')
					sleep(1)
					
					# 拨入组织
					input_up_click('//*[@id="combobox-input-ruleegrid-orgid-0"]', 'Mindy科技有限公司')
					
					# 拨入账户
					click("xpath", '//*[@id="combobox-input-ruleegrid-accountid-0"]')
					sleep(1)
					click("xpath", '//*[@id="ruleegrid-accountid-0-combogrid-body-table"]/tbody/tr[2]/td[2]/div')
					sleep(1)
					
					span_click("保存")
					# 退出所有窗体
					switch_default()
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("资金下拨设置--下拨顺序，新增成功！")
					sleep(3)
				
			# 测试修改功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="allocationSetting-tab-iframe"]')
			span_click("下拨规则")
			switch_to("xpath", '//*[@id="subTabFour-iframe"]')
			sleep(1)
			
			#刷新勾选按钮
			click("xpath",'//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath",'//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("修改")
			switch_to("xpath", '//*[@id="detailWin-iframe"]')
			sleep(1)
			span_click("保存")
			
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("资金下拨设置--下拨规则，修改成功！")
			sleep(3)
			
			# 测试失效功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="allocationSetting-tab-iframe"]')
			span_click("下拨规则")
			switch_to("xpath", '//*[@id="subTabFour-iframe"]')
			sleep(1)
			
			# 刷新勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			span_click("失效")
			ok_click()
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'失效成功！')]")
			print("资金下拨设置--下拨规则，失效成功！")
			sleep(3)
			
			# 测试生效功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="allocationSetting-tab-iframe"]')
			span_click("下拨规则")
			switch_to("xpath", '//*[@id="subTabFour-iframe"]')
			sleep(1)
			
			# 刷新勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			span_click("生效")
			
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'生效成功！')]")
			print("资金下拨设置--下拨规则，生效成功！")
			sleep(3)

			# 回到初始界面
			click("xpath", "//span[text()='资金池下拨管理']")
			sleep(1)
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("下拨方案失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
			
			# def tearDown(self):
			#     self.driver.quit()
			print("结束时间：", time.strftime("%Y-%m-%d %H:%M:%S"))
		
		
		# 测试资金下拨申请--申请🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱
		try:
			logger.info("测试资金下拨申请--申请")
			switch_default()
			choose_organization("Mindy科技有限公司")
			
			# 将页面的滚动条滑动到‘资金结算管理’页面的地方
			js_gd("xpath", "//span[contains(text(),'内部资金池')]")
			# 用JS的方法点击资金结算管理菜单按钮
			js_click("xpath", "//span[contains(text(),'内部资金池')]")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			click("xpath", "//span[text()='资金池下拨管理']")
			sleep(1)
			click("xpath", "//span[text()='资金下拨申请']")
			sleep(1)
			switch_default()
			sleep(3)
			
			# 测试新增功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			for i in range(1, 6):
				switch_to("xpath",'//*[@id="allocationApply-tab-iframe"]')
				switch_to("xpath", '//*[@id="subTabOne-iframe"]')
				sleep(1)
				span_click("新增")
				switch_to("xpath",'//*[@id="addWin-iframe"]')
				
				#新增行
				click("xpath",'//*[@id="gridbar"]/div/div[1]/table/tbody/tr/td[1]/span')
				sleep(1)
				
				#申请类型
				click_up_click('//*[@id="combobox-input-applydetail-allocateapplytypeid-0"]')
				
				#拨入账户
				click_up_click('//*[@id="combobox-input-applydetail-accountid-0"]')
				
				#申请金额
				money=str(random.randint(1,300))
				input("xpath",'//*[@id="applydetail-applyallocateamount-0-input"]',money)
				sleep(1)
				
				#申请拨入日期
				today=date.today()
				input("xpath",'//*[@id="applydetail-applyallocatedate-0-input"]',str(today))
				sleep(1)
				span_click("保存")
				
				# 退出所有窗体
				switch_default()
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				if i ==4 :
					print("资金下拨设置--下拨规则，修改成功！")
				sleep(3)
				
			
			# 测试修改功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="allocationApply-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			# 刷新勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("修改")
			switch_to("xpath", '//*[@id="modWin-iframe"]')
			
			input("xpath",'//*[@id="memo"]','测试修改')
			sleep(1)
			span_click("保存")
			
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("资金下拨申请--申请，修改成功！")
			sleep(3)
			
			# 测试删除功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="allocationApply-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			# 刷新勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("删除")
			ok_click()
			
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("资金下拨申请--申请，删除成功！")
			sleep(3)
			
			# 测试送审功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="allocationApply-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			# 刷新勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("送审")
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'送审成功！')]")
			print("资金下拨申请--申请，送审成功！")
			sleep(3)
			
			# 测试撤销送审功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="allocationApply-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			# 刷新勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("撤销送审")
			ok_click()
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'撤销送审成功！')]")
			print("资金下拨申请--申请，撤销送审成功！")
			sleep(3)
			
			# 测试作废功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="allocationApply-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			# 刷新勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("送审")
			sleep(3)
			double_click("xpath",'//*[@id="grid-body-table"]/tbody/tr[1]/td[3]/div')
			sleep(1)
			switch_to("xpath",'//*[@id="wf_taskProcessing_win-iframe"]')
			span_click("同意")
			switch_parent()
			double_click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[3]/div')
			sleep(1)
			switch_to("xpath", '//*[@id="wf_taskProcessing_win-iframe"]')
			span_click("同意")
			switch_parent()
			
			click("xpath",'//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("作废")
			ok_click()
		
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'成功作废1条记录！')]")
			print("资金下拨申请--申请，作废成功！")
			sleep(3)
			
			# 做数据💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="allocationApply-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			# 刷新勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("送审")
			sleep(3)
			double_click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[3]/div')
			sleep(1)
			switch_to("xpath", '//*[@id="wf_taskProcessing_win-iframe"]')
			span_click("同意")
			switch_parent()
			double_click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[3]/div')
			sleep(1)
			switch_to("xpath", '//*[@id="wf_taskProcessing_win-iframe"]')
			span_click("同意")
			
			# 退出所有窗体
			switch_default()
			sleep(3)
			
			#数据2
			switch_to("xpath", '//*[@id="allocationApply-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			# 刷新勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[2]/td[2]/div/button')
			sleep(1)
			
			span_click("送审")
			sleep(3)
			double_click("xpath", '//*[@id="grid-body-table"]/tbody/tr[2]/td[3]/div')
			sleep(1)
			switch_to("xpath", '//*[@id="wf_taskProcessing_win-iframe"]')
			span_click("同意")
			switch_parent()
			double_click("xpath", '//*[@id="grid-body-table"]/tbody/tr[2]/td[3]/div')
			sleep(1)
			switch_to("xpath", '//*[@id="wf_taskProcessing_win-iframe"]')
			span_click("同意")
			
			# 退出所有窗体
			switch_default()
			sleep(3)
			
			#数据3
			switch_to("xpath", '//*[@id="allocationApply-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			# 刷新勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[3]/td[2]/div/button')
			sleep(1)
			
			span_click("送审")
			sleep(3)
			double_click("xpath", '//*[@id="grid-body-table"]/tbody/tr[3]/td[3]/div')
			sleep(1)
			switch_to("xpath", '//*[@id="wf_taskProcessing_win-iframe"]')
			span_click("同意")
			switch_parent()
			double_click("xpath", '//*[@id="grid-body-table"]/tbody/tr[3]/td[3]/div')
			sleep(1)
			switch_to("xpath", '//*[@id="wf_taskProcessing_win-iframe"]')
			span_click("同意")
			
			# 退出所有窗体
			switch_default()
			sleep(3)
			
			# 回到初始界面
			choose_organization("亚唐科技")
			# 将页面的滚动条滑动到‘资金结算管理’页面的地方
			js_gd("xpath", "//span[contains(text(),'内部资金池')]")
			# 用JS的方法点击资金结算管理菜单按钮
			js_click("xpath", "//span[contains(text(),'内部资金池')]")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("下拨方案失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
			
			# def tearDown(self):
			#     self.driver.quit()
			print("结束时间：", time.strftime("%Y-%m-%d %H:%M:%S"))
		
		
		# 测试资金下拨申请--申请处理🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱
		try:
			logger.info("测试资金下拨申请--申请处理")
			switch_default()
			click("xpath", "//span[text()='资金池下拨管理']")
			sleep(1)
			click("xpath", "//span[text()='资金下拨申请']")
			sleep(1)
			switch_default()
			sleep(3)
			
			# 测试作废功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath",'//*[@id="allocationApply-tab-iframe"]')
			span_click("申请处理")
			switch_to("xpath",'//*[@id="subTabtwo-iframe"]')
			
			#查询
			click("xpath",'//*[@id="north"]/div[2]/span')
			sleep(1)
			
			span_click("高级查询")
			
			#审批状态
			click("xpath",'//*[@id="combobox-input-value_4"]')
			sleep(1)
			click("xpath",'//*[@id="f-combo-value_4-list-1"]/div[1]')
			sleep(1)
			click("xpath", '//*[@id="combobox-input-value_4"]')
			sleep(1)
			
			#作废状态
			click("xpath", '//*[@id="combobox-input-value_5"]')
			sleep(1)
			click("xpath", '//*[@id="f-combo-value_5-list-0"]/div[1]')
			sleep(1)
			
			click("xpath",'//*[@id="advQueryWin-btn-1"]/div[2]')
			sleep(1)
			
			click("xpath",'//*[@id="f-win-title-advQueryWin"]/div[1]/div')
			sleep(1)
			
			#勾选按钮
			click("xpath",'//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("作废")
			ok_click()
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'成功作废1条记录！')]")
			print("资金下拨申请--申请处理，作废成功！")
			sleep(3)
			
			# 回到初始界面
			click("xpath", "//span[text()='资金池下拨管理']")
			sleep(1)
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("申请处理失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
			
			# def tearDown(self):
			#     self.driver.quit()
			print("结束时间：", time.strftime("%Y-%m-%d %H:%M:%S"))
		
		
		# 测试资金下拨处理--申请下拨🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱
		try:
			logger.info("测试资金下拨处理--申请下拨")
			switch_default()
			click("xpath", "//span[text()='资金池下拨管理']")
			sleep(1)
			click("xpath", "//span[text()='资金下拨处理']")
			sleep(1)
			switch_default()
			sleep(3)
			
			# 测试调整保留天数💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath",'//*[@id="allocationHandle-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			#刷新、勾选按钮
			click("xpath",'//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath",'//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			
			span_click("调整保留天数")
			ok_click()
			switch_to("xpath",'//*[@id="adjustWin-iframe"]')
			
			#保留天数
			double_click("xpath",'//*[@id="applydetail-reservekeepdays-0-input"]')
			sleep(1)
			input("xpath",'//*[@id="applydetail-reservekeepdays-0-input"]','5')
			sleep(1)
			
			span_click("保存")
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("资金下拨处理--申请下拨，调整保留天数成功！")
			sleep(3)
			
			# 测试手工下拨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="allocationHandle-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			
			triangle_cick_and_element("下拨","手工下拨")
			
			switch_to("xpath",'//*[@id="allocateWin-iframe"]')
			
			#拨出账户
			click("xpath",'//*[@id="combobox-input-ourbankaccountid"]')
			sleep(1)
			click("xpath",'//*[@id="ourbankaccountid-combogrid-body-table"]/tbody/tr[2]/td[2]/div')
			sleep(1)
			
			span_click("下拨")
			
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'下拨成功,生成一笔下拨单')]")
			print("资金下拨处理--申请下拨，下拨成功！")
			sleep(3)
			
			# 测试手工生成下拨单💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="allocationHandle-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[2]/td[2]/div/button')
			
			triangle_cick_and_element("下拨", "手工生成下拨单")
			
			switch_to("xpath", '//*[@id="allocateWin-iframe"]')
			
			# 拨出账户
			click("xpath", '//*[@id="combobox-input-ourbankaccountid"]')
			sleep(1)
			click("xpath", '//*[@id="ourbankaccountid-combogrid-body-table"]/tbody/tr[3]/td[2]/div')
			sleep(1)
			
			span_click("生成下拨单")
			
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'下拨成功,生成一笔下拨单')]")
			print("资金下拨处理--申请下拨，手工生成下拨单成功！")
			sleep(3)
			
			# 测试下拨状态查询💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="allocationHandle-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			
			span_click("下拨状态查询")
			ok_click()
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'请查看相应结果！')]")
			print("资金下拨处理--申请下拨，下拨状态查询成功！")
			sleep(3)
			
			# 回到初始界面
			click("xpath", "//span[text()='资金池下拨管理']")
			sleep(1)
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("申请下拨失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
			
			# def tearDown(self):
			#     self.driver.quit()
			print("结束时间：", time.strftime("%Y-%m-%d %H:%M:%S"))
		
		
		# 测试资金下拨处理--定额下拨🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱
		try:
			logger.info("测试资金下拨处理--定额下拨")
			switch_default()
			click("xpath", "//span[text()='资金池下拨管理']")
			sleep(1)
			click("xpath", "//span[text()='资金下拨处理']")
			sleep(1)
			switch_default()
			sleep(3)
			
			# 测试余额查询💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="allocationHandle-tab-iframe"]')
			span_click("定额下拨")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			sleep(1)
			
			#下拨模板
			input_up_click('//*[@id="combobox-input-allocateruleid"]','下拨规则')
			
			#拨出账户
			click("xpath",'//*[@id="combobox-input-ourbankaccountid"]')
			sleep(1)
			click("xpath", '//*[@id="ourbankaccountid-combogrid-body-table"]/tbody/tr[1]/td[2]/div')
			sleep(1)
			
			#刷新、勾选按钮
			click("xpath",'//*[@id="editgrid-syscheck-0"]')
			sleep(1)
			
			span_click("余额查询")
			
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'拨出账户的余额为')]")
			print("资金下拨处理--定额下拨，余额查询成功！")
			sleep(3)
			click("xpath", "//span[text()='资金下拨处理']")
			sleep(1)
			
			# 测试立即下拨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="allocationHandle-tab-iframe"]')
			span_click("定额下拨")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			sleep(1)
			
			# 下拨模板
			input_up_click('//*[@id="combobox-input-allocateruleid"]', '下拨规则')
			
			#拨出组织
			input_up_click('//*[@id="combobox-input-ourorgid"]','亚唐科技')
			
			# 拨出账户
			click("xpath", '//*[@id="combobox-input-ourbankaccountid"]')
			sleep(1)
			click("xpath", '//*[@id="ourbankaccountid-combogrid-body-table"]/tbody/tr[1]/td[2]/div')
			sleep(1)

			span_click("立即下拨")
			
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'生成下拨单成功')]")
			print("资金下拨处理--定额下拨，立即下拨成功！")
			sleep(3)
			click("xpath", "//span[text()='资金下拨处理']")
			sleep(1)
			
			# 测试生成下拨单💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			for i in range (1,4):
				switch_to("xpath", '//*[@id="allocationHandle-tab-iframe"]')
				span_click("定额下拨")
				switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
				sleep(1)
				
				# 下拨模板
				input_up_click('//*[@id="combobox-input-allocateruleid"]', '下拨规则')
				
				# 拨出组织
				input_up_click('//*[@id="combobox-input-ourorgid"]', '亚唐科技')
				
				# 拨出账户
				click("xpath", '//*[@id="combobox-input-ourbankaccountid"]')
				sleep(1)
				click("xpath", '//*[@id="ourbankaccountid-combogrid-body-table"]/tbody/tr[1]/td[2]/div')
				sleep(1)
				
				span_click("生成下拨单")
				
				# 退出所有窗体
				switch_default()
				implici_wait("xpath", "//span[contains(text(),'生成下拨单成功')]")
				if i == 3:
					print("资金下拨处理--定额下拨，生成下拨单成功！")
				sleep(3)
				click("xpath", "//span[text()='资金下拨处理']")
				sleep(1)
			
			# 测试删除功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="allocationHandle-tab-iframe"]')
			span_click("定额下拨")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			sleep(1)
			
			#刷新、勾选按钮
			click("xpath",'//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath",'//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("删除")
			ok_click()
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'删除操作成功！')]")
			print("资金下拨处理--定额下拨，删除成功！")
			sleep(3)
			click("xpath", "//span[text()='资金下拨处理']")
			sleep(1)
			
			# 测试作废功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="allocationHandle-tab-iframe"]')
			span_click("定额下拨")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t1-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("作废")
			ok_click()
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("资金下拨处理--定额下拨，作废成功！")
			sleep(3)
			click("xpath", "//span[text()='资金下拨处理']")
			sleep(1)
			
			# 测试送审功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="allocationHandle-tab-iframe"]')
			span_click("定额下拨")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("送审")
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'送审成功！')]")
			print("资金下拨处理--定额下拨，送审成功！")
			sleep(3)
			click("xpath", "//span[text()='资金下拨处理']")
			sleep(1)
			
			# 测试审批历史功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="allocationHandle-tab-iframe"]')
			span_click("定额下拨")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			sleep(1)
			
			double_click("xpath",'//*[@id="t1_t0"]/td[1]/div/span')
			sleep(1)
			switch_to("xpath",'//*[@id="wf_taskProcessing_win-iframe"]')
			span_click("同意")
			switch_parent()
			#二审
			double_click("xpath", '//*[@id="t1_t0"]/td[1]/div/span')
			sleep(1)
			switch_to("xpath", '//*[@id="wf_taskProcessing_win-iframe"]')
			span_click("同意")
			switch_parent()
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("审批历史")
			switch_to("xpath",'//*[@id="flowwin-iframe"]')
			sleep(2)
			span_click("流程流转")
			
			implici_wait("xpath", "//div[contains(text(),'开始')]")
			print("资金下拨处理--定额下拨，审批历史查看成功！")
			sleep(3)
			# 退出所有窗体
			switch_default()
			click("xpath", "//span[text()='资金下拨处理']")
			sleep(1)
			
			# 测试下拨功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="allocationHandle-tab-iframe"]')
			span_click("定额下拨")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("下拨")
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'下拨操作成功！')]")
			print("资金下拨处理--定额下拨，下拨成功！")
			sleep(3)
			click("xpath", "//span[text()='资金下拨处理']")
			sleep(1)
			
			# 测试查询下拨状态功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="allocationHandle-tab-iframe"]')
			span_click("定额下拨")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("下拨状态查询")
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'单据已查询状态，请查看相应结果！')]")
			print("资金下拨处理--定额下拨，下拨状态查询成功！")
			sleep(3)
			click("xpath", "//span[text()='资金下拨处理']")
			sleep(1)
			
			# 测试下拨日志查看💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="allocationHandle-tab-iframe"]')
			span_click("定额下拨")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t0_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("下拨日志查看")
			switch_to("xpath",'//*[@id="logsWin-iframe"]')
			implici_wait("xpath", "//div[contains(text(),'支付')]")
			print("资金下拨处理--定额下拨，下拨日志查看成功！")
			switch_default()
			sleep(3)
			click("xpath", "//span[text()='资金下拨处理']")
			sleep(1)
			
			# 测试确认已下拨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			sql = "update t_se_payments set paystate = '7' where OPPNAME like '%账户2021%'"
			ora_sql(ora_ip, ora_sid, ora_user, ora_pwd,
			       sql)
			sleep(1)
			switch_to("xpath", '//*[@id="allocationHandle-tab-iframe"]')
			span_click("定额下拨")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("确认已下拨")
			ok_click()
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("资金下拨处理--定额下拨，确认已下拨成功！")
			sleep(3)
			click("xpath", "//span[text()='资金下拨处理']")
			sleep(1)
			
			# 回到初始界面
			click("xpath", "//span[text()='资金池下拨管理']")
			sleep(1)
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("申请下拨失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
			
			# def tearDown(self):
			#     self.driver.quit()
			print("结束时间：", time.strftime("%Y-%m-%d %H:%M:%S"))
		
		
		# 测试资金下拨处理--补足留底下拨🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱
		try:
			logger.info("测试资金下拨处理--补足留底下拨")
			switch_default()
			click("xpath", "//span[text()='资金池下拨管理']")
			sleep(1)
			click("xpath", "//span[text()='资金下拨处理']")
			sleep(1)
			switch_default()
			sleep(3)
			# 测试余额查询💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="allocationHandle-tab-iframe"]')
			span_click("补足留底下拨")
			switch_to("xpath", '//*[@id="subTabThree-iframe"]')
			sleep(1)
			
			# 下拨模板
			input_up_click('//*[@id="combobox-input-allocateruleid"]', '下拨规则')
			
			# 拨出账户
			click("xpath", '//*[@id="combobox-input-ourbankaccountid"]')
			sleep(1)
			click("xpath", '//*[@id="ourbankaccountid-combogrid-body-table"]/tbody/tr[1]/td[2]/div')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="editgrid-syscheck-0"]')
			sleep(1)
			
			span_click("余额查询")
			
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'拨出账户的余额为')]")
			print("资金下拨处理--补足留底下拨，余额查询成功！")
			sleep(3)
			click("xpath", "//span[text()='资金下拨处理']")
			sleep(1)
			
			# 测试立即下拨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="allocationHandle-tab-iframe"]')
			span_click("补足留底下拨")
			switch_to("xpath", '//*[@id="subTabThree-iframe"]')
			sleep(1)
			
			# 下拨模板
			input_up_click('//*[@id="combobox-input-allocateruleid"]', '下拨规则')
			
			# 拨出组织
			input_up_click('//*[@id="combobox-input-ourorgid"]', '亚唐科技')
			
			# 拨出账户
			click("xpath", '//*[@id="combobox-input-ourbankaccountid"]')
			sleep(1)
			click("xpath", '//*[@id="ourbankaccountid-combogrid-body-table"]/tbody/tr[2]/td[2]/div')
			sleep(1)
			
			#拨入金额
			double_click("xpath",'//*[@id="editgrid-ouramount-0-input"]')
			sleep(1)
			input("xpath",'//*[@id="editgrid-ouramount-0-input"]',str(random.randint(1,300)))
			sleep(1)
			
			
			span_click("立即下拨")
			
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'生成下拨单成功')]")
			print("资金下拨处理--补足留底下拨，立即下拨成功！")
			sleep(3)
			click("xpath", "//span[text()='资金下拨处理']")
			sleep(1)
			
			# 测试生成下拨单💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			for i in range(1, 4):
				switch_to("xpath", '//*[@id="allocationHandle-tab-iframe"]')
				span_click("补足留底下拨")
				switch_to("xpath", '//*[@id="subTabThree-iframe"]')
				sleep(1)
				
				# 下拨模板
				input_up_click('//*[@id="combobox-input-allocateruleid"]', '下拨规则')
				
				# 拨出组织
				input_up_click('//*[@id="combobox-input-ourorgid"]', '亚唐科技')
				
				# 拨出账户
				click("xpath", '//*[@id="combobox-input-ourbankaccountid"]')
				sleep(1)
				click("xpath", '//*[@id="ourbankaccountid-combogrid-body-table"]/tbody/tr[2]/td[2]/div')
				sleep(1)
				
				double_click("xpath", '//*[@id="editgrid-ouramount-0-input"]')
				sleep(1)
				input("xpath", '//*[@id="editgrid-ouramount-0-input"]', str(random.randint(1, 300)))
				sleep(1)
				
				span_click("生成下拨单")
				
				# 退出所有窗体
				switch_default()
				implici_wait("xpath", "//span[contains(text(),'生成下拨单成功')]")
				if i == 3:
					print("资金下拨处理--补足留底下拨，生成下拨单成功！")
				sleep(3)
				click("xpath", "//span[text()='资金下拨处理']")
				sleep(1)
			
			# 测试删除功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="allocationHandle-tab-iframe"]')
			span_click("补足留底下拨")
			switch_to("xpath", '//*[@id="subTabThree-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("删除")
			ok_click()
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'删除操作成功！')]")
			print("资金下拨处理--补足留底下拨，删除成功！")
			sleep(3)
			click("xpath", "//span[text()='资金下拨处理']")
			sleep(1)
			
			# 测试作废功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="allocationHandle-tab-iframe"]')
			span_click("补足留底下拨")
			switch_to("xpath", '//*[@id="subTabThree-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t1-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("作废")
			ok_click()
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("资金下拨处理--补足留底下拨，作废成功！")
			sleep(3)
			click("xpath", "//span[text()='资金下拨处理']")
			sleep(1)
			
			# 测试送审功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="allocationHandle-tab-iframe"]')
			span_click("补足留底下拨")
			switch_to("xpath", '//*[@id="subTabThree-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("送审")
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'送审成功！')]")
			print("资金下拨处理--补足留底下拨，送审成功！")
			sleep(3)
			click("xpath", "//span[text()='资金下拨处理']")
			sleep(1)
			
			# 测试审批历史功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="allocationHandle-tab-iframe"]')
			span_click("补足留底下拨")
			switch_to("xpath", '//*[@id="subTabThree-iframe"]')
			sleep(1)
			
			double_click("xpath", '//*[@id="t1_t0"]/td[1]/div/span')
			sleep(1)
			switch_to("xpath", '//*[@id="wf_taskProcessing_win-iframe"]')
			span_click("同意")
			switch_parent()
			# 二审
			double_click("xpath", '//*[@id="t1_t0"]/td[1]/div/span')
			sleep(1)
			switch_to("xpath", '//*[@id="wf_taskProcessing_win-iframe"]')
			span_click("同意")
			switch_parent()
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("审批历史")
			switch_to("xpath", '//*[@id="flowwin-iframe"]')
			sleep(2)
			span_click("流程流转")
			
			implici_wait("xpath", "//div[contains(text(),'开始')]")
			print("资金下拨处理--补足留底下拨，审批历史查看成功！")
			sleep(3)
			# 退出所有窗体
			switch_default()
			click("xpath", "//span[text()='资金下拨处理']")
			sleep(1)
			
			# 测试下拨功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="allocationHandle-tab-iframe"]')
			span_click("补足留底下拨")
			switch_to("xpath", '//*[@id="subTabThree-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("下拨")
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'下拨操作成功！')]")
			print("资金下拨处理--补足留底下拨，下拨成功！")
			sleep(3)
			click("xpath", "//span[text()='资金下拨处理']")
			sleep(1)
			
			# 测试查询下拨状态功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="allocationHandle-tab-iframe"]')
			span_click("补足留底下拨")
			switch_to("xpath", '//*[@id="subTabThree-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("下拨状态查询")
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'单据已查询状态，请查看相应结果！')]")
			print("资金下拨处理--补足留底下拨，下拨状态查询成功！")
			sleep(3)
			click("xpath", "//span[text()='资金下拨处理']")
			sleep(1)
			
			# 测试下拨日志查看💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="allocationHandle-tab-iframe"]')
			span_click("补足留底下拨")
			switch_to("xpath", '//*[@id="subTabThree-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t0_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("下拨日志查看")
			switch_to("xpath", '//*[@id="logsWin-iframe"]')
			implici_wait("xpath", "//div[contains(text(),'支付')]")
			print("资金下拨处理--补足留底下拨，下拨日志查看成功！")
			switch_default()
			sleep(3)
			click("xpath", "//span[text()='资金下拨处理']")
			sleep(1)
			
			# 测试确认已下拨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			sql = "update t_se_payments set paystate = '7' where OPPNAME like '%账户2021%'"
			ora_sql(ora_ip, ora_sid, ora_user, ora_pwd,
			       sql)
			sleep(1)
			switch_to("xpath", '//*[@id="allocationHandle-tab-iframe"]')
			span_click("补足留底下拨")
			switch_to("xpath", '//*[@id="subTabThree-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("确认已下拨")
			ok_click()
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("资金下拨处理--补足留底下拨，确认已下拨成功！")
			sleep(3)
			click("xpath", "//span[text()='资金下拨处理']")
			sleep(1)
			
			# 回到初始界面
			click("xpath", "//span[text()='资金池下拨管理']")
			sleep(1)
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("申请下拨失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
			
			# def tearDown(self):
			#     self.driver.quit()
			print("结束时间：", time.strftime("%Y-%m-%d %H:%M:%S"))
		
		
		# 测试资金下拨处理--下拨单批量下拨🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱
		try:
			logger.info("测试资金下拨处理--下拨单批量下拨")
			switch_default()
			click("xpath", "//span[text()='资金池下拨管理']")
			sleep(1)
			click("xpath", "//span[text()='资金下拨处理']")
			sleep(1)
			switch_default()
			sleep(3)
			
			sql = "update t_se_payments set paystate = '1' where OPPNAME like '%下级账户2021%'"
			ora_sql(ora_ip, ora_sid, ora_user, ora_pwd,
			       sql)
			sleep(1)
			sql = "update t_se_payments set approvestate = '1' where OPPNAME like '%下级账户2021%'"
			ora_sql(ora_ip, ora_sid, ora_user, ora_pwd,
			       sql)
			sleep(1)
			
			# 测试送审💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="allocationHandle-tab-iframe"]')
			span_click("下拨单批量下拨")
			switch_to("xpath", '//*[@id="subTabSix-iframe"]')
			sleep(1)
			
			#刷新、勾选按钮
			click("xpath",'//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("送审")
			
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'送审成功！')]")
			print("资金下拨处理--下拨单批量下拨，送审成功！")
			sleep(3)
			click("xpath", "//span[text()='资金下拨处理']")
			sleep(1)
			
			# 测试审核功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="allocationHandle-tab-iframe"]')
			span_click("下拨单批量下拨")
			switch_to("xpath", '//*[@id="subTabSix-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t1-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("审核")
			ok_click()
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("资金下拨处理--下拨单批量下拨，审核成功！")
			sleep(3)
			click("xpath", "//span[text()='资金下拨处理']")
			sleep(1)
			
			# 测试审批历史功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="allocationHandle-tab-iframe"]')
			span_click("下拨单批量下拨")
			switch_to("xpath", '//*[@id="subTabSix-iframe"]')
			sleep(1)
			#一审
			double_click("xpath",'//*[@id="t1_t0_t0"]/td[1]/div/span')
			sleep(1)
			switch_to("xpath",'//*[@id="wf_taskProcessing_win-iframe"]')
			
			span_click("同意")
			sleep(3)
			switch_parent()
			
			# 二审
			double_click("xpath", '//*[@id="t1_t0_t0"]/td[1]/div/span')
			sleep(1)
			switch_to("xpath", '//*[@id="wf_taskProcessing_win-iframe"]')
			
			span_click("同意")
			sleep(3)
			switch_parent()
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("审批历史")
			switch_to("xpath",'//*[@id="flowwin-iframe"]')
			sleep(2)
			span_click("流程流转")
			
			# 退出所有窗体
			implici_wait("xpath", "//div[contains(text(),'开始')]")
			print("资金下拨处理--下拨单批量下拨，审批历史查看成功！")
			sleep(3)
			switch_default()
			click("xpath", "//span[text()='资金下拨处理']")
			sleep(1)
			
			# 测试下拨功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="allocationHandle-tab-iframe"]')
			span_click("下拨单批量下拨")
			switch_to("xpath", '//*[@id="subTabSix-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("下拨")
			
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'下拨操作成功！')]")
			print("资金下拨处理--下拨单批量下拨，下拨成功！")
			sleep(3)
			click("xpath", "//span[text()='资金下拨处理']")
			sleep(1)
			
			# 测试下拨状态查询功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="allocationHandle-tab-iframe"]')
			span_click("下拨单批量下拨")
			switch_to("xpath", '//*[@id="subTabSix-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("下拨状态查询")
			ok_click()
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'单据已查询状态，请查看相应结果！')]")
			print("资金下拨处理--下拨单批量下拨，下拨状态查询成功！")
			sleep(3)
			click("xpath", "//span[text()='资金下拨处理']")
			sleep(1)
			
			# 测试确认已下拨功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			sql = "update t_se_payments set paystate = '7' where OPPNAME like '%下级账户2021%'"
			ora_sql(ora_ip, ora_sid, ora_user, ora_pwd,
			       sql)
			sleep(1)
			
			switch_to("xpath", '//*[@id="allocationHandle-tab-iframe"]')
			span_click("下拨单批量下拨")
			switch_to("xpath", '//*[@id="subTabSix-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("确认已下拨")
			ok_click()
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("资金下拨处理--下拨单批量下拨，确认已下拨成功！")
			sleep(3)
			click("xpath", "//span[text()='资金下拨处理']")
			sleep(1)
			
			# 测试支付日志查看功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="allocationHandle-tab-iframe"]')
			span_click("下拨单批量下拨")
			switch_to("xpath", '//*[@id="subTabSix-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("支付日志查看")
			switch_to("xpath",'//*[@id="logsWin-iframe"]')
			implici_wait("xpath", "//div[contains(text(),'支付')]")
			print("资金下拨处理--下拨单批量下拨，支付日志查看成功！")
			sleep(3)
			switch_default()
			click("xpath", "//span[text()='资金下拨处理']")
			sleep(1)
			
			# 测试作废功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			sql = "update t_se_payments set paystate = '1' where ourbankaccountname like '%下级账户2021%'"
			ora_sql(ora_ip, ora_sid, ora_user, ora_pwd,
			       sql)
			switch_to("xpath", '//*[@id="allocationHandle-tab-iframe"]')
			span_click("下拨单批量下拨")
			switch_to("xpath", '//*[@id="subTabSix-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("作废")
			ok_click()
			
			#退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'作废')]")
			print("资金下拨处理--下拨单批量下拨，作废成功！")
			sleep(3)
			click("xpath", "//span[text()='资金下拨处理']")
			sleep(1)
			
			
			# 回到初始界面
			click("xpath", "//span[text()='资金池下拨管理']")
			sleep(1)
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("申请下拨失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
			
			# def tearDown(self):
			#     self.driver.quit()
			print("结束时间：", time.strftime("%Y-%m-%d %H:%M:%S"))
		
		
		# 测试资金池下拨管理--下拨交易查看🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱
		try:
			logger.info("测试资金池下拨管理--下拨交易查看")
			switch_default()
			click("xpath", "//span[text()='资金池下拨管理']")
			sleep(1)
			click("xpath", "//span[text()='下拨交易查看']")
			sleep(1)
			switch_default()
			sleep(3)
			sql = "update t_se_payments set APPROVESTATE = '2' where OPPNAME like '%账户2021%'"
			ora_sql(ora_ip, ora_sid, ora_user, ora_pwd,
			       sql)
			sleep(1)
			sql = "update t_se_payments set paystate = '2' where OPPNAME like '%账户2021%'"
			ora_sql(ora_ip, ora_sid, ora_user, ora_pwd,
			       sql)
			sleep(1)
			
			# 测试打印💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath",'//*[@id="allocationView-tab-iframe"]')
			
			#刷新、勾选按钮
			click("xpath",'//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t0_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("打印")
			
			# 获取所有窗口句柄
			all_handles = self.driver.window_handles
			# 循环遍历所有新打开的窗口句柄，也就是说不包括主窗口
			now_handle = self.driver.current_window_handle
			for handle in all_handles:
				self.driver.switch_to.window(handle)
				if self.driver.title == u"allocationviewprint":
					implici_wait("xpath", "//td[contains(text(),'单据号')]")
					print("资金池下拨管理--下拨交易查看，打印成功!！")
					time.sleep(3)
					self.driver.switch_to.window(now_handle)
					switch_default()
			
			# 测试打印💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="allocationView-tab-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t0_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("带审批记录打印")
			
			# 获取所有窗口句柄
			all_handles = self.driver.window_handles
			# 循环遍历所有新打开的窗口句柄，也就是说不包括主窗口
			now_handle = self.driver.current_window_handle
			for handle in all_handles:
				self.driver.switch_to.window(handle)
				if self.driver.title == u"allocationviewprint":
					implici_wait("xpath", "//td[contains(text(),'单据号')]")
					print("资金池下拨管理--下拨交易查看，打审批记录打印成功!！")
					time.sleep(3)
					self.driver.switch_to.window(now_handle)
					switch_default()
			
			# 回到初始界面
			click("xpath", "//span[text()='资金池下拨管理']")
			sleep(1)
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("下拨交易查看失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
			
			# def tearDown(self):
			#     self.driver.quit()
			print("结束时间：", time.strftime("%Y-%m-%d %H:%M:%S"))
		
		
		# 测试资金池内部计价--内部账户申请🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱
		try:
			logger.info("测试资金池内部计价--内部账户申请")
			switch_default()
			click("xpath", "//span[text()='资金池内部计价']")
			sleep(1)
			click("xpath", "//span[text()='内部账户申请']")
			sleep(1)
			switch_default()
			sleep(3)
			
			# 测试申请开户💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			for i in range (1,4):
				switch_to("xpath", '//*[@id="accountApplyManage-tab-iframe"]')
				switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
				sleep(1)
				
				triangle_cick_and_element("申请",'申请开户')
				switch_to('xpath','//*[@id="custButton1Win1-iframe"]')
				
				#池所属组织
				click_up_click('//*[@id="combobox-input-poolorgid"]')
				
				#币种
				input_up_click('//*[@id="combobox-input-currencyid"]','CNY-人民币')
				
				#账户存款类型
				input_up_click('//*[@id="combobox-input-deposittype"]','活期')
				
				#存款标识
				input_up_click('//*[@id="combobox-input-depositloansign"]','1:存款')
				
				#透支额度
				double_click("xpath",'//*[@id="maxoverdraftamount-input"]')
				sleep(1)
				input("xpath",'//*[@id="maxoverdraftamount-input"]','5000')
				sleep(1)
				
				#申请原因
				input("xpath",'//*[@id="applyreason"]','测试开户')
				sleep(1)
				
				span_click("保存")
				
				# 退出所有窗体
				switch_default()
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				if i == 3:
					print("资金池内部计价--内部账户申请，申请开户成功！")
				sleep(3)
				
			# 测试修改💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="accountApplyManage-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			sleep(1)
			
			#刷新、勾选按钮
			click("xpath",'//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath",'//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("修改")
			switch_to("xpath",'//*[@id="editWin-iframe"]')
			
			input("xpath",'//*[@id="description"]','测试修改')
			sleep(1)
			
			span_click("保存")
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("资金池内部计价--内部账户申请，修改成功！")
			sleep(3)
			
			# 测试删除💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="accountApplyManage-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("删除")
			ok_click()
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'成功删除1条记录！')]")
			print("资金池内部计价--内部账户申请，删除成功！")
			sleep(3)
			
			# 测试作废💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="accountApplyManage-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("作废")
			ok_click()
			switch_to("xpath",'//*[@id="canceldesrpWin-iframe"]')
			input("xpath",'//*[@id="cancelreason"]','测试作废')
			sleep(1)
			click("xpath",'//*[@id="save"]/span/span')
			sleep(1)
			
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("资金池内部计价--内部账户申请，作废成功！")
			sleep(3)
			
			# 测试送审💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="accountApplyManage-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("送审")
			ok_click()
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'成功送审1条记录！')]")
			print("资金池内部计价--内部账户申请，送审成功！")
			sleep(3)
			
			# 测试受理💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="accountApplyManage-tab-iframe"]')
			span_click("受理")
			switch_to("xpath", '//*[@id="subTabSix-iframe"]')
			sleep(1)
			
			#一审
			double_click("xpath",'//*[@id="grid-body-table"]/tbody/tr/td[3]/div')
			sleep(1)
			switch_to("xpath",'//*[@id="wf_taskProcessing_win-iframe"]')
			sleep(1)
			span_click("同意")
			switch_parent()
			sleep(3)
			
			#二审
			double_click("xpath", '//*[@id="grid-body-table"]/tbody/tr/td[3]/div')
			sleep(1)
			switch_to("xpath",'//*[@id="wf_taskProcessing_win-iframe"]')
			switch_to("xpath", '//*[@id="wf_busi_form"]')
			sleep(1)
			#内部账户池
			click("xpath",'//*[@id="combobox-input-accountpoolid"]')
			sleep(1)
			print(2)
			
			click("xpath", '//*[@id="accountpoolid-combogrid-body-table"]/tbody/tr[1]/td[2]/div')
			sleep(1)
			
			#账户
			number=str(time.strftime("%Y%m%d%H%M%S"))
			input("xpath",'//*[@id="code"]',number)
			sleep(1)
			
			#名称
			name = "内部账户" +str(time.strftime("%Y%M%S"))
			input("xpath",'//*[@id="name"]',name)
			
			#利率方案
			click_up_click('//*[@id="combobox-input-interestrateschemeid"]')
			
			#计息周期
			click_up_click('//*[@id="combobox-input-interestperiodtype"]')
			
			#结息日
			input("xpath",'//*[@id="interestsettlementdate"]','21')
			sleep(1)
			switch_parent()
			span_click("同意")
			
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("资金池内部计价--内部账户申请，受理成功！")
			sleep(3)
			
			# 测试申请销户💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="accountApplyManage-tab-iframe"]')
			span_click("申请")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("申请",'申请销户')
			switch_to("xpath",'//*[@id="custButton1Win2-iframe"]')
			
			#内部账户
			click_up_click('//*[@id="combobox-input-internalaccountsid"]')
			
			#申请原因
			input("xpath",'//*[@id="applyreason"]','测试销户')
			sleep(1)
			
			span_click("保存")
			
			
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("资金池内部计价--内部账户申请，申请销户成功！")
			sleep(3)

			# 回到初始界面
			click("xpath", "//span[text()='资金池内部计价']")
			sleep(1)
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("内部账户申请失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
			
			# def tearDown(self):
			#     self.driver.quit()
			print("结束时间：", time.strftime("%Y-%m-%d %H:%M:%S"))
		
		
		# 测试资金池内部计价--内部账户管理🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱
		try:
			logger.info("测试资金池内部计价--内部账户申请")
			switch_default()
			click("xpath", "//span[text()='资金池内部计价']")
			sleep(1)
			click("xpath", "//span[text()='内部账户管理']")
			sleep(1)
			switch_default()
			sleep(3)
			
			# 测试新增内部账户池💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath",'//*[@id="accountManage-tab-iframe"]')
			span_click("新增内部账户池")
			switch_to("xpath",'//*[@id="addWin-iframe"]')
			
			#代码
			coad = str(time.strftime("%Y%m%d%H%M%S"))
			input("xpath",'//*[@id="code"]',coad)
			sleep(1)
			
			#名称
			name = "SY" +str(time.strftime("%Y%M%S"))
			input("xpath",'//*[@id="name"]',name)
			sleep(1)
			
			span_click("保存")
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("资金池内部计价--内部账户管理，新增账户池成功！")
			sleep(3)
			
			# 测试新增内部账户💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			for i in range (1,3):
				switch_to("xpath", '//*[@id="accountManage-tab-iframe"]')
				span_click("新增内部账户")
				switch_to("xpath", '//*[@id="addWin-iframe"]')
				
				# 代码
				coad1 = str(time.strftime("%Y%m%d%H%M%S"))
				input("xpath", '//*[@id="code"]', coad1)
				sleep(1)
				
				#内部账户池
				input_up_click('//*[@id="combobox-input-accountpoolid"]',coad)
				
				#账户所属组织
				input_up_click('//*[@id="combobox-input-orgid"]', '亚唐科技')
				
				#名称
				name2 ="内部账户"+str(time.strftime("%Y%M%S"))
				input("xpath",'//*[@id="name"]',name2)
				sleep(1)
				
				#币种
				input_up_click('//*[@id="combobox-input-currencyid"]','CNY-人民币')
				
				#账户存款类型
				input_up_click('//*[@id="combobox-input-deposittype"]','活期')
				
				#存贷标识
				click_up_click('//*[@id="combobox-input-depositloansign"]')
				
				# 利率方案
				click_up_click('//*[@id="combobox-input-interestrateschemeid"]')
				
				# 计息周期
				click_up_click('//*[@id="combobox-input-interestperiodtype"]')
				
				# 结息日
				input("xpath", '//*[@id="interestsettlementdate"]', '21')
				sleep(1)
				
				span_click("保存")
				# 退出所有窗体
				switch_default()
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				if i ==2 :
					print("资金池内部计价--内部账户管理，新增内部账户成功！")
				sleep(3)
			
			# 查询出数据💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="accountManage-tab-iframe"]')
		
			#查询数据
			click("xpath",'//*[@id="north"]/div[2]/span')
			sleep(1)
			
			#内部账户池
			input("xpath",'//*[@id="combobox-input-accountpoolid"]',name)
			sleep(1)
			click("xpath",'//*[@id="accountpoolid-combogrid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			span_click("查询")
			switch_default()
			
			# 测试修改功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="accountManage-tab-iframe"]')
			
			#刷新、勾选按钮
			click("xpath",'//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath",'//*[@id="t1_t0_t0-fixed"]/td[2]/div')
			sleep(1)
			
			span_click("修改")
			switch_to("xpath",'//*[@id="modWin-iframe"]')
			sleep(1)
			span_click("保存")
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("资金池内部计价--内部账户管理，修改成功！")
			sleep(3)
			
			# 测试删除功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="accountManage-tab-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t0_t0-fixed"]/td[2]/div')
			sleep(1)
			
			span_click("删除")
			ok_click()
			
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("资金池内部计价--内部账户管理，删除成功！")
			sleep(3)
			
			# 测试开户功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="accountManage-tab-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t0_t0-fixed"]/td[2]/div')
			sleep(1)
			
			triangle_cick_and_element("维护",'开户')
			
			double_click("xpath",'//*[@id="initbalance-input"]')
			sleep(1)
			input("xpath",'//*[@id="initbalance-input"]','5000')
			sleep(1)
			
			click("xpath",'//*[@id="dateWin-btn-0"]/div[2]')
			sleep(1)
			
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("资金池内部计价--内部账户管理，开户成功！")
			sleep(3)
			
			# 测试变更功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="accountManage-tab-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t0_t0-fixed"]/td[2]/div')
			sleep(1)
			
			triangle_cick_and_element("维护", '变更')
			switch_to("xpath",'//*[@id="modWin-iframe"]')
			sleep(1)
			span_click("保存")
			
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("资金池内部计价--内部账户管理，变更成功！")
			sleep(3)
			
			# 测试冻结功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="accountManage-tab-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t0_t0-fixed"]/td[2]/div')
			sleep(1)
			
			triangle_cick_and_element("维护", '冻结')
			
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("资金池内部计价--内部账户管理，冻结成功！")
			sleep(3)
			
			# 测试解冻功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="accountManage-tab-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t0_t0-fixed"]/td[2]/div')
			sleep(1)
			
			triangle_cick_and_element("维护", '解冻')
			
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("资金池内部计价--内部账户管理，解冻成功！")
			sleep(3)
			
			# 测试销户功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="accountManage-tab-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t0_t0-fixed"]/td[2]/div')
			sleep(1)
			
			triangle_cick_and_element("维护", '销户')
			ok_click()
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("资金池内部计价--内部账户管理，销户成功！")
			sleep(3)
			
			# 回到初始界面
			click("xpath", "//span[text()='资金池内部计价']")
			sleep(1)
			
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("内部账户管理失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
			
			# def tearDown(self):
			#     self.driver.quit()
			print("结束时间：", time.strftime("%Y-%m-%d %H:%M:%S"))
		
		
		# 测试资金池内部计价--内部核算规则🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱
		try:
			logger.info("测试资金池内部计价--内部核算规则")
			switch_default()
			click("xpath", "//span[text()='资金池内部计价']")
			sleep(1)
			click("xpath", "//span[text()='内部核算规则']")
			sleep(1)
			switch_default()
			sleep(3)
			
			# 测试新增池核算规则💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			for i in range (1,3):
				switch_to("xpath",'//*[@id="accountingRules-tab-iframe"]')
				span_click("新增池核算规则")
				switch_to("xpath",'//*[@id="addWin-iframe"]')
				
				#名称
				name = "账户池核算规则" + str(time.strftime("%Y%M%S"))
				input("xpath",'//*[@id="name"]',name)
				sleep(1)
				
				#内部账户池
				click_up_click('//*[@id="combobox-input-accountpoolid"]')
				
				#核算对象
				input_up_click('//*[@id="combobox-input-accountobject"]','内部账户')
				
				# 单据对象
				input_up_click('//*[@id="combobox-input-noteobjectid"]', 'ZJFK-付款单')
				
				span_click("保存")
				# 退出所有窗体
				switch_default()
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				print("资金池内部计价--内部核算规则，新增池核算规则成功！")
				sleep(3)
			
			# 测试修改功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="accountingRules-tab-iframe"]')
			#刷新、勾选按钮
			click("xpath",'//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath",'//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("修改")
			switch_to("xpath",'//*[@id="modWin-iframe"]')
			
			input("xpath",'//*[@id="description"]','测试修改')
			sleep(1)
			
			span_click("保存")
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("资金池内部计价--内部账户管理，修改成功！")
			sleep(3)
			
			# 测试删除功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="accountingRules-tab-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("删除")
			ok_click()
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'删除操作成功！')]")
			print("资金池内部计价--内部账户管理，删除成功！")
			sleep(3)
			
			# 测试失效功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="accountingRules-tab-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("失效")
			ok_click()
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("资金池内部计价--内部账户管理，失效成功！")
			sleep(3)
			
			# 测试生效功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="accountingRules-tab-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("生效")
			ok_click()
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("资金池内部计价--内部账户管理，生效成功！")
			sleep(3)
			
			# 测试新增账户核算规则💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="accountingRules-tab-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("新增账户核算规则")
			switch_to("xpath",'//*[@id="addWin-iframe"]')
			
			#内部账户
			click_up_click('//*[@id="combobox-input-internalaccountid"]')
			
			#交易方向
			input_up_click('//*[@id="combobox-input-moneyway"]','支出')
			
			span_click("保存")
			
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("资金池内部计价--内部账户管理，新增账户核算规则成功！")
			sleep(3)
			
			
			# 回到初始界面
			click("xpath", "//span[text()='资金池内部计价']")
			sleep(1)
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("内部账户管理失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
			
			# def tearDown(self):
			#     self.driver.quit()
			print("结束时间：", time.strftime("%Y-%m-%d %H:%M:%S"))
		
		
		# 测试资金池内部计价--内部转账申请🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱
		try:
			logger.info("测试资金池内部计价--内部核算规则")
			switch_default()
			choose_organization("Mindy科技有限公司")
			
			# 将页面的滚动条滑动到‘资金结算管理’页面的地方
			js_gd("xpath", "//span[contains(text(),'内部资金池')]")
			# 用JS的方法点击资金结算管理菜单按钮
			js_click("xpath", "//span[contains(text(),'内部资金池')]")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			
			click("xpath", "//span[text()='资金池内部计价']")
			sleep(1)
			click("xpath", "//span[text()='内部转账申请']")
			sleep(1)
			switch_default()
			
			# 做数据💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			choose_organization("亚唐科技")
			# 将页面的滚动条滑动到‘资金结算管理’页面的地方
			js_gd("xpath", "//span[contains(text(),'内部资金池')]")
			# 用JS的方法点击资金结算管理菜单按钮
			js_click("xpath", "//span[contains(text(),'内部资金池')]")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			
			click("xpath", "//span[text()='资金池内部计价']")
			sleep(1)
			click("xpath", "//span[text()='内部账户管理']")
			sleep(1)
			switch_default()
			
			# 新增内部账户池
			switch_to("xpath", '//*[@id="accountManage-tab-iframe"]')
			span_click("新增内部账户池")
			switch_to("xpath", '//*[@id="addWin-iframe"]')
			
			# 代码
			coad3 = str(time.strftime("%Y%m%d%H%M%S"))
			input("xpath", '//*[@id="code"]', coad3)
			sleep(1)
			
			# 名称
			
			input("xpath", '//*[@id="name"]', "内部账户转账")
			sleep(1)
			
			span_click("保存")
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			sleep(3)
			
			# 测试新增内部账户
			for i in range(1, 4):
				switch_to("xpath", '//*[@id="accountManage-tab-iframe"]')
				span_click("新增内部账户")
				switch_to("xpath", '//*[@id="addWin-iframe"]')
				
				# 代码
				if i ==1 :
					input("xpath", '//*[@id="code"]', "20211057")
				if i ==2 :
					input("xpath", '//*[@id="code"]', "2021105701")
				if i ==3 :
					input("xpath", '//*[@id="code"]', "2021105702")
				sleep(1)
				
				
				# 内部账户池
				input_up_click('//*[@id="combobox-input-accountpoolid"]', coad3)
				
				# 账户所属组织
				if i == 1 :
					input_up_click('//*[@id="combobox-input-orgid"]', 'Mindy科技有限公司')
				if i == 2 :
					input_up_click('//*[@id="combobox-input-orgid"]', 'Mindy科技有限公司')
				if i == 3 :
					input_up_click('//*[@id="combobox-input-orgid"]', 'Mindy科技有限公司')
				
				# 名称
				if i !=3 :
					name2 = "内部账户" + str(time.strftime("%Y%M%S"))
					input("xpath", '//*[@id="name"]', name2)
					sleep(1)
				else :
					name2 = "结汇账户" + str(time.strftime("%Y%M%S"))
					input("xpath", '//*[@id="name"]', name2)
					sleep(1)
				
				# 币种
				if i !=3 :
					input_up_click('//*[@id="combobox-input-currencyid"]', 'CNY-人民币')
				else :
					input_up_click('//*[@id="combobox-input-currencyid"]', 'USD')
				# 账户存款类型
				input_up_click('//*[@id="combobox-input-deposittype"]', '活期')
				
				# 存贷标识
				click_up_click('//*[@id="combobox-input-depositloansign"]')
				
				# 利率方案
				click_up_click('//*[@id="combobox-input-interestrateschemeid"]')
				
				# 计息周期
				click_up_click('//*[@id="combobox-input-interestperiodtype"]')
				
				# 结息日
				input("xpath", '//*[@id="interestsettlementdate"]', '21')
				sleep(1)
				
				span_click("保存")
				# 退出所有窗体
				switch_default()
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				sleep(3)
			
			#对数据进行开户
			switch_to("xpath", '//*[@id="accountManage-tab-iframe"]')
			
			# 查询数据
			click("xpath", '//*[@id="north"]/div[2]/span')
			sleep(1)
			
			# 内部账户池
			input("xpath", '//*[@id="combobox-input-accountpoolid"]', "内部账户转账")
			sleep(1)
			click("xpath", '//*[@id="accountpoolid-combogrid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			span_click("查询")
			switch_default()
			
			#开户
			for i in range (1,4):
				switch_to("xpath", '//*[@id="accountManage-tab-iframe"]')
				# 刷新、勾选按钮
				click("xpath", '//*[@id="treepagingbar-page-refresh"]')
				sleep(1)
				if i ==1 :
					click("xpath", '//*[@id="t1_t0_t0-fixed"]/td[2]/div')
					sleep(1)
				if i ==2 :
					click("xpath", '//*[@id="t1_t0_t1-fixed"]/td[2]/div/button')
					sleep(1)
				if i ==3 :
					click("xpath", '//*[@id="t1_t0_t2-fixed"]/td[2]/div/button')
					sleep(1)
				
				triangle_cick_and_element("维护", '开户')
				
				double_click("xpath", '//*[@id="initbalance-input"]')
				sleep(1)
				input("xpath", '//*[@id="initbalance-input"]', '5000')
				sleep(1)
				
				click("xpath", '//*[@id="dateWin-btn-0"]/div[2]')
				sleep(1)
				
				# 退出所有窗体
				switch_default()
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				sleep(3)
				
			#回到下级页面
			choose_organization("Mindy科技有限公司")
			# 将页面的滚动条滑动到‘资金结算管理’页面的地方
			js_gd("xpath", "//span[contains(text(),'内部资金池')]")
			# 用JS的方法点击资金结算管理菜单按钮
			js_click("xpath", "//span[contains(text(),'内部资金池')]")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			
			click("xpath", "//span[text()='资金池内部计价']")
			sleep(1)
			click("xpath", "//span[text()='内部转账申请']")
			sleep(1)
			switch_default()
			
			# 测试新增功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			for i in range (1,3):
				switch_to("xpath", '//*[@id="transferapplys-tab-iframe"]')
				switch_to("xpath", '//*[@id="subTabOne-iframe"]')
				sleep(1)
				
				span_click("新增")
				switch_to("xpath", '//*[@id="addWin-iframe"]')
				
				# 受托组织
				input_up_click('//*[@id="combobox-input-entrustorgid"]', '001010-亚唐科技')
				
				# 收方组织
				input_up_click('//*[@id="combobox-input-opporgid"]', '002001-Mindy科技有限公司')
				
				# 交易类型
				click_up_click('//*[@id="combobox-input-paytypeid"]')
				
				# 内部账户池
				input_up_click('//*[@id="combobox-input-accountpoolid"]', '内部账户转账')
				
				# 付方内部账户
				input_up_click('//*[@id="combobox-input-ourinternalaccountid"]', '20211057')
				
				# 收方内部账户
				input_up_click('//*[@id="combobox-input-oppinternalaccountid"]', '2021105701')
				
				# 金额
				double_click("xpath", '//*[@id="oppamount-input"]')
				sleep(1)
				input("xpath", '//*[@id="oppamount-input"]', str(random.randint(1, 300)))
				sleep(1)
				
				span_click("保存")
				# 退出所有窗体
				switch_default()
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				if i == 2 :
					print("资金池内部计价--内部转账申请，新增成功！")
				sleep(3)
				
			# 测试复制功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="transferapplys-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			#刷新、勾选按钮
			click("xpath",'//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath",'//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("复制")
			ok_click()
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("资金池内部计价--内部转账申请，复制成功！")
			sleep(3)
			
			# 测试修改功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="transferapplys-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("修改")
			
			switch_to("xpath",'//*[@id="modWin-iframe"]')
			sleep(1)
			input("xpath",'//*[@id="memo"]','测试修改')
			sleep(1)
			
			span_click("保存")
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("资金池内部计价--内部转账申请，修改成功！")
			sleep(3)
			
			# 测试删除功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="transferapplys-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("删除")
			ok_click()
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("资金池内部计价--内部转账申请，删除成功！")
			sleep(3)
			
			# 测试作废功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="transferapplys-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("作废")
			ok_click()
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'作废成功:1笔！失败:0笔！')]")
			print("资金池内部计价--内部转账申请，作废成功！")
			sleep(3)
			
			# 测试送审功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="transferapplys-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("送审")
			
			
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("资金池内部计价--内部转账申请，送审成功！")
			sleep(3)
			
			# 测试撤销送审功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="transferapplys-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			
			triangle_cick_and_element("送审",'撤销送审')
			ok_click()
			
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'撤销送审成功:1笔!失败0笔！')]")
			print("资金池内部计价--内部转账申请，撤销送审成功！")
			sleep(3)
			
			# 测试提交功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="transferapplys-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("送审")
			sleep(3)
			double_click("xpath",'//*[@id="grid-body-table"]/tbody/tr[1]/td[3]/div')
			sleep(1)
			switch_to("xpath",'//*[@id="wf_taskProcessing_win-iframe"]')
			span_click("同意")
			switch_parent()
			sleep(3)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("提交")
			ok_click()
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("资金池内部计价--内部转账申请，提交成功！")
			sleep(3)
			
			#回到初始页面
			choose_organization("亚唐科技")
			# 将页面的滚动条滑动到‘资金结算管理’页面的地方
			js_gd("xpath", "//span[contains(text(),'内部资金池')]")
			# 用JS的方法点击资金结算管理菜单按钮
			js_click("xpath", "//span[contains(text(),'内部资金池')]")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("内部账户管理失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
			
			# def tearDown(self):
			#     self.driver.quit()
			print("结束时间：", time.strftime("%Y-%m-%d %H:%M:%S"))
		
		
		# 测试资金池内部计价--内部转账申请🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱
		try:
			logger.info("测试资金池内部计价--内部核算规则")
			switch_default()
			choose_organization("Mindy科技有限公司")
			
			# 将页面的滚动条滑动到‘资金结算管理’页面的地方
			js_gd("xpath", "//span[contains(text(),'内部资金池')]")
			# 用JS的方法点击资金结算管理菜单按钮
			js_click("xpath", "//span[contains(text(),'内部资金池')]")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			
			click("xpath", "//span[text()='资金池内部计价']")
			sleep(1)
			click("xpath", "//span[text()='内部转账申请']")
			sleep(1)
			switch_default()
			
			# 测试导入功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			for i in range (1,4) :
				switch_to("xpath", '//*[@id="transferapplys-tab-iframe"]')
				span_click("批量转账申请")
				switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
				#点击上传按钮
				click("xpath",'//*[@id="gridtitle"]/div[3]/div[2]')
				sleep(1)
				
				switch_to("xpath",'//*[@id="importDataWin-iframe"]')
				sleep(1)
				
				#业务
				click_up_click('//*[@id="combobox-input-businessid"]')
				span_click("下一步")
				
				switch_to("xpath",'//*[@id="loadNextWin-iframe"]')
				
				#交易类型
				click_up_click('//*[@id="combobox-input-paytypeid"]')
				
				#结算方式
				clear("xpath",'//*[@id="combobox-input-settlementmodeid"]')
				sleep(1)
				click_up_click('//*[@id="combobox-input-settlementmodeid"]')
				
				#受托组织
				input_up_click('//*[@id="combobox-input-entrustorgid"]','亚唐科技')
				
				#附件上传
				upload_click("xpath", "//div[text()='上传文件']/parent::*[1]/descendant::*[4]",
				             'D:\FlieDownload', '"NeiBuZhuanZhangShenQing.xls"')
				sleep(3)
				# 点击保存按钮
				click("xpath", "//span[text()='上传']")
				# 退出所有iframe窗体
				switch_default()
				# 用隐式等待方法等页面出现新增成功的提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功')]")
				if i==3 :
					print("资金池内部计价--内部账户管理，批量转账申请，导入成功！")
				time.sleep(3)
				click("xpath", "//span[text()='内部转账申请']")
				sleep(1)
				switch_default()
				
			
			# 查询数据💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="transferapplys-tab-iframe"]')
			span_click("批量转账申请")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			sleep(1)
			
			#点击查询按钮
			click("xpath",'//*[@id="north"]/div[2]/span')
			sleep(1)
			
			clear("xpath",'//*[@id="paydateto-input"]')
			sleep(1)
			
			span_click("查询")
			switch_default()
			
			# 测试删除功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="transferapplys-tab-iframe"]')
			span_click("批量转账申请")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			sleep(1)
			
			#刷新、勾选按钮
			click("xpath",'//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath",'//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("删除")
			ok_click()
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功')]")
			print("资金池内部计价--内部账户管理，批量转账申请，删除成功！")
			time.sleep(3)
			
			# 测试作废功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="transferapplys-tab-iframe"]')
			span_click("批量转账申请")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("作废")
			ok_click()
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'作废成功')]")
			print("资金池内部计价--内部账户管理，批量转账申请，作废成功！")
			time.sleep(3)
			
			# 测试送审功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="transferapplys-tab-iframe"]')
			span_click("批量转账申请")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("送审")
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功')]")
			print("资金池内部计价--内部账户管理，批量转账申请，送审成功！")
			time.sleep(3)
			
			# 测试撤销送审功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="transferapplys-tab-iframe"]')
			span_click("批量转账申请")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("送审","撤销送审")
			ok_click()
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'撤销送审成功')]")
			print("资金池内部计价--内部账户管理，批量转账申请，撤销送审成功！")
			time.sleep(3)
			
			# 测试提交功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="transferapplys-tab-iframe"]')
			span_click("批量转账申请")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("送审")
			sleep(3)
			
			double_click("xpath",'//*[@id="grid-body-table"]/tbody/tr[1]/td[3]/div')
			sleep(1)
			switch_to("xpath",'//*[@id="wf_taskProcessing_win-iframe"]')
			span_click("同意")
			switch_parent()
			sleep(3)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("提交")
			ok_click()
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("资金池内部计价--内部账户管理，批量转账申请，提交成功！")
			time.sleep(3)
			
			# 回到初始页面
			choose_organization("亚唐科技")
			# 将页面的滚动条滑动到‘资金结算管理’页面的地方
			js_gd("xpath", "//span[contains(text(),'内部资金池')]")
			# 用JS的方法点击资金结算管理菜单按钮
			js_click("xpath", "//span[contains(text(),'内部资金池')]")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("内部账户管理失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
			
			# def tearDown(self):
			#     self.driver.quit()
			print("结束时间：", time.strftime("%Y-%m-%d %H:%M:%S"))
		
		
		# 测试资金池内部计价--内部转账受理--单笔转账受理🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱
		try:
			logger.info("测试资金池内部计价--内部转账受理--单笔转账受理")
			
			click("xpath", "//span[text()='资金池内部计价']")
			sleep(1)
			click("xpath", "//span[text()='内部转账受理']")
			sleep(1)
			switch_default()
			
			# 做数据💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			choose_organization("Mindy科技有限公司")
			# 将页面的滚动条滑动到‘资金结算管理’页面的地方
			js_gd("xpath", "//span[contains(text(),'内部资金池')]")
			# 用JS的方法点击资金结算管理菜单按钮
			js_click("xpath", "//span[contains(text(),'内部资金池')]")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			
			click("xpath", "//span[text()='资金池内部计价']")
			sleep(1)
			click("xpath", "//span[text()='内部转账申请']")
			sleep(1)
			switch_default()
			
			#新增数据
			for i in range(1, 3):
				switch_to("xpath", '//*[@id="transferapplys-tab-iframe"]')
				switch_to("xpath", '//*[@id="subTabOne-iframe"]')
				sleep(1)
				
				span_click("新增")
				switch_to("xpath", '//*[@id="addWin-iframe"]')
				
				# 受托组织
				input_up_click('//*[@id="combobox-input-entrustorgid"]', '001010-亚唐科技')
				sleep(1)
				
				# 收方组织
				input_up_click('//*[@id="combobox-input-opporgid"]', '002001-Mindy科技有限公司')
				
				# 交易类型
				click_up_click('//*[@id="combobox-input-paytypeid"]')
				
				# 内部账户池
				input_up_click('//*[@id="combobox-input-accountpoolid"]', '内部账户转账')
				
				# 付方内部账户
				input_up_click('//*[@id="combobox-input-ourinternalaccountid"]', '20211057')
				
				# 收方内部账户
				input_up_click('//*[@id="combobox-input-oppinternalaccountid"]', '2021105701')
				
				# 金额
				double_click("xpath", '//*[@id="oppamount-input"]')
				sleep(1)
				input("xpath", '//*[@id="oppamount-input"]', str(random.randint(1, 300)))
				sleep(1)
				
				span_click("保存")
				# 退出所有窗体
				switch_default()
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				sleep(3)
				
				#送审、提交
				switch_to("xpath", '//*[@id="transferapplys-tab-iframe"]')
				switch_to("xpath", '//*[@id="subTabOne-iframe"]')
				sleep(1)
				
				#刷新、勾选按钮
				click("xpath",'//*[@id="gridbar-page-refresh"]')
				sleep(1)
				click("xpath",'//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
				
				span_click("送审")
				sleep(3)
				double_click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[3]/div')
				sleep(1)
				switch_to("xpath", '//*[@id="wf_taskProcessing_win-iframe"]')
				span_click("同意")
				switch_parent()
				sleep(3)
				
				# 刷新、勾选按钮
				click("xpath", '//*[@id="gridbar-page-refresh"]')
				sleep(1)
				click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
				sleep(1)
				
				span_click("提交")
				ok_click()
				# 退出所有窗体
				switch_default()
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				sleep(3)
				
		
			choose_organization("亚唐科技")
			# 将页面的滚动条滑动到‘资金结算管理’页面的地方
			js_gd("xpath", "//span[contains(text(),'内部资金池')]")
			# 用JS的方法点击资金结算管理菜单按钮
			js_click("xpath", "//span[contains(text(),'内部资金池')]")
			sleep(1)
			click("xpath", "//span[text()='资金池内部计价']")
			sleep(1)
			click("xpath", "//span[text()='内部转账受理']")
			sleep(1)
			switch_default()
			
			# 测试打回功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath",'//*[@id="transferdeals-tab-iframe"]')
			switch_to("xpath",'//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			#刷新、勾选按钮
			click("xpath",'//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath",'//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("打回")
			ok_click()
			input("xpath",'//*[@id="refuseReason"]','测试打回')
			sleep(1)
			click("xpath",'//*[@id="determineCancel"]/span/span')
			sleep(1)
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'打回操作成功')]")
			print("资金池内部计价--内部账户管理，内部转账受理，打回操作成功！")
			time.sleep(3)
			
			# 测试受理功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="transferdeals-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("受理")
			switch_to("xpath",'//*[@id="modWin-iframe"]')
			sleep(1)
			span_click("受理")
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("资金池内部计价--内部账户管理，内部转账受理，受理成功！")
			time.sleep(3)
			
			#回到初始界面
			click("xpath", "//span[text()='资金池内部计价']")
			sleep(1)
			
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("内部账户管理失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
			
			# def tearDown(self):
			#     self.driver.quit()
			print("结束时间：", time.strftime("%Y-%m-%d %H:%M:%S"))
		
		
		# 测试资金池内部计价--内部转账受理-批量转账受理🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱
		try:
			logger.info("测试资金池内部计价--内部转账受理--单笔转账受理")
			
			click("xpath", "//span[text()='资金池内部计价']")
			sleep(1)
			click("xpath", "//span[text()='内部转账受理']")
			sleep(1)
			switch_default()
			
			# 做数据💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			choose_organization("Mindy科技有限公司")
			# 将页面的滚动条滑动到‘资金结算管理’页面的地方
			js_gd("xpath", "//span[contains(text(),'内部资金池')]")
			# 用JS的方法点击资金结算管理菜单按钮
			js_click("xpath", "//span[contains(text(),'内部资金池')]")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			
			click("xpath", "//span[text()='资金池内部计价']")
			sleep(1)
			click("xpath", "//span[text()='内部转账申请']")
			sleep(1)
			switch_default()
			# 导入数据
			for i in range(1, 3):
				switch_to("xpath", '//*[@id="transferapplys-tab-iframe"]')
				span_click("批量转账申请")
				switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
				# 点击上传按钮
				click("xpath", '//*[@id="gridtitle"]/div[3]/div[2]')
				sleep(1)
			
				switch_to("xpath", '//*[@id="importDataWin-iframe"]')
				sleep(1)
				
				#业务
				click_up_click('//*[@id="combobox-input-businessid"]')
				span_click("下一步")
				
				switch_to("xpath", '//*[@id="loadNextWin-iframe"]')
				
				# 交易类型
				click_up_click('//*[@id="combobox-input-paytypeid"]')
				
				# 结算方式
				clear("xpath", '//*[@id="combobox-input-settlementmodeid"]')
				sleep(1)
				click_up_click('//*[@id="combobox-input-settlementmodeid"]')
				
				# 受托组织
				click_up_click('//*[@id="combobox-input-entrustorgid"]')
				
				# 附件上传
				upload_click("xpath", "//div[text()='上传文件']/parent::*[1]/descendant::*[4]",
				             'D:\FlieDownload', '"NeiBuZhuanZhangShenQing.xls"')
				sleep(3)
				# 点击保存按钮
				click("xpath", "//span[text()='上传']")
				sleep(1)
				# 退出所有iframe窗体
				switch_default()
				# 用隐式等待方法等页面出现新增成功的提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功')]")
				time.sleep(3)
				click("xpath", "//span[text()='内部转账申请']")
				sleep(1)
				switch_default()
				
				# 查询数据
				switch_to("xpath", '//*[@id="transferapplys-tab-iframe"]')
				span_click("批量转账申请")
				switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
				sleep(1)
				
				# 点击查询按钮
				click("xpath", '//*[@id="north"]/div[2]/span')
				sleep(1)
				
				clear("xpath", '//*[@id="paydateto-input"]')
				sleep(1)
				
				span_click("查询")
				switch_default()
				
				# 提交
				switch_to("xpath", '//*[@id="transferapplys-tab-iframe"]')
				span_click("批量转账申请")
				switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
				sleep(1)
				
				# 刷新、勾选按钮
				click("xpath", '//*[@id="gridbar-page-refresh"]')
				sleep(1)
				click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
				sleep(1)
				
				span_click("送审")
				sleep(3)
				
				double_click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[3]/div')
				sleep(1)
				switch_to("xpath", '//*[@id="wf_taskProcessing_win-iframe"]')
				span_click("同意")
				switch_parent()
				sleep(3)
				
				# 刷新、勾选按钮
				click("xpath", '//*[@id="gridbar-page-refresh"]')
				sleep(1)
				click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
				sleep(1)
				
				span_click("提交")
				ok_click()
				# 退出所有iframe窗体
				switch_default()
				# 用隐式等待方法等页面出现新增成功的提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				time.sleep(3)
				
			choose_organization("亚唐科技")
			# 将页面的滚动条滑动到‘资金结算管理’页面的地方
			js_gd("xpath", "//span[contains(text(),'内部资金池')]")
			# 用JS的方法点击资金结算管理菜单按钮
			js_click("xpath", "//span[contains(text(),'内部资金池')]")
			sleep(1)
			click("xpath", "//span[text()='资金池内部计价']")
			sleep(1)
			click("xpath", "//span[text()='内部转账受理']")
			sleep(1)
			switch_default()
			
			# 测试受理功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath",'//*[@id="transferdeals-tab-iframe"]')
			span_click("批量转账受理")
			switch_to("xpath",'//*[@id="subTabTwo-iframe"]')
			
			#查询数据
			click("xpath",'//*[@id="north"]/div[2]/span')
			sleep(1)
			clear("xpath",'//*[@id="paydateto-input"]')
			sleep(1)
			
			span_click("查询")
			
			#刷新、勾选数据
			click("xpath",'//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath",'//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("受理")
			switch_to("xpath",'//*[@id="modWin-iframe"]')
			sleep(1)
			span_click("保存")
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("资金池内部计价--内部账户管理，批量转账受理，受理成功！")
			time.sleep(3)
			click("xpath", "//span[text()='内部转账受理']")
			sleep(1)
			switch_default()
			
			# 测试打回功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="transferdeals-tab-iframe"]')
			span_click("批量转账受理")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			
			# 查询数据
			click("xpath", '//*[@id="north"]/div[2]/span')
			sleep(1)
			clear("xpath", '//*[@id="paydateto-input"]')
			sleep(1)
			
			span_click("查询")
			
			# 刷新、勾选数据
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("打回")
			ok_click()
			input("xpath",'//*[@id="refuseReason"]','测试打回')
			sleep(1)
			
			click("xpath",'//*[@id="determineCancel"]/span/span')
			sleep(1)
			
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'打回操作成功')]")
			print("资金池内部计价--内部账户管理，批量转账受理，打回成功！")
			time.sleep(3)
			
			# 回到初始界面
			click("xpath", "//span[text()='资金池内部计价']")
			sleep(1)
			
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("批量转账受理失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
			
			# def tearDown(self):
			#     self.driver.quit()
			print("结束时间：", time.strftime("%Y-%m-%d %H:%M:%S"))
		
		
		# 测试资金池内部计价--内部转账转账-单笔转账🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱
		try:
			logger.info("测试资金池内部计价--内部转账转账-单笔转账")
			
			click("xpath", "//span[text()='资金池内部计价']")
			sleep(1)
			click("xpath", "//span[text()='内部账户转账']")
			sleep(1)
			switch_default()
			
			
			# 测试新增功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			for i in range (1,4):
				switch_to("xpath", '//*[@id="transfers-tab-iframe"]')
				switch_to("xpath", '//*[@id="subTabOne-iframe"]')
				sleep(1)
				
				span_click("新增")
				switch_to("xpath",'//*[@id="addWin-iframe"]')
				
				#交易类型
				click_up_click('//*[@id="combobox-input-paytypeid"]')
				
				#内部账户池
				input_up_click('//*[@id="combobox-input-accountpoolid"]',"内部账户转账")
				
				#付方内部账户
				input_up_click('//*[@id="combobox-input-ourinternalaccountid"]','20211057')
				
				#收方内部账户
				input_up_click('//*[@id="combobox-input-oppinternalaccountid"]','2021105701')
				
				#金额
				money = str(random.randint(1,300))
				double_click("xpath",'//*[@id="ouramount-input"]')
				sleep(1)
				input("xpath",'//*[@id="ouramount-input"]',money)
				sleep(1)
				
				span_click("保存")
				# 退出所有iframe窗体
				switch_default()
				# 用隐式等待方法等页面出现新增成功的提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				if i==3 :
					print("资金池内部计价--内部转账转账，单笔转账，新增成功！")
				time.sleep(3)
				
			# 测试修改功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="transfers-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			#刷新、勾选按钮
			click("xpath",'//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("修改")
			switch_to("xpath",'//*[@id="modWin-iframe"]')
			
			input("xpath",'//*[@id="memo"]','测试修改')
			sleep(1)
			
			span_click("保存")
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("资金池内部计价--内部转账转账，单笔转账，保存成功！")
			time.sleep(3)
			
			# 测试删除功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="transfers-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("删除")
			ok_click()
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("资金池内部计价--内部转账转账，单笔转账，删除成功！")
			time.sleep(3)
			
			
			
			# 测试送审功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="transfers-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("送审")
			click("xpath",'//*[@id="f-message-webgen-0-yesBnt"]')
			sleep(1)
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("资金池内部计价--内部转账转账，单笔转账，送审成功！")
			time.sleep(3)
			
			# 测试撤销送审功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="transfers-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("送审",'撤销送审')
			ok_click()
			
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'撤销送审成功！')]")
			print("资金池内部计价--内部转账转账，单笔转账，撤销送审成功！")
			time.sleep(3)
			
			# 测试作废功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="transfers-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("作废")
			ok_click()
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("资金池内部计价--内部转账转账，单笔转账，作废成功！")
			time.sleep(3)
			
			# 测试审核功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="transfers-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("审核")
			ok_click()
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("资金池内部计价--内部转账转账，单笔转账，审核成功！")
			time.sleep(3)
			
			# 测试撤销审核功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="transfers-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("审核",'取消审核')
			ok_click()
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("资金池内部计价--内部转账转账，单笔转账，取消审核成功！")
			time.sleep(3)
			
			# 测试支付功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="transfers-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("审核")
			ok_click()
			sleep(3)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("支付")
			ok_click()
			click("xpath",'//*[@id="submit"]/span')
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("资金池内部计价--内部转账转账，单笔转账，支付成功！")
			time.sleep(3)
			
			# 测试打印功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="transfers-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("打印")
			# 获取所有窗口句柄
			all_handles = self.driver.window_handles
			# 循环遍历所有新打开的窗口句柄，也就是说不包括主窗口
			now_handle = self.driver.current_window_handle
			for handle in all_handles:
				self.driver.switch_to.window(handle)
				if self.driver.title == u"transfersrecprint":
					implici_wait("xpath", "//td[contains(text(),'Mindy科技有限公司')]")
					print("资金池内部计价--内部转账转账，单笔转账，打印成功！")
					time.sleep(3)
					self.driver.switch_to.window(now_handle)
					switch_default()
			
			
			

			# 回到初始界面
			click("xpath", "//span[text()='资金池内部计价']")
			sleep(1)
			
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("批量转账受理失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
			
			# def tearDown(self):
			#     self.driver.quit()
			print("结束时间：", time.strftime("%Y-%m-%d %H:%M:%S"))
		
		
		# 测试资金池内部计价--内部转账转账-批量转账🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱
		try:
			logger.info("测试资金池内部计价--内部转账转账-批量转账")
			
			click("xpath", "//span[text()='资金池内部计价']")
			sleep(1)
			click("xpath", "//span[text()='内部账户转账']")
			sleep(1)
			switch_default()
			
			# 测试上传功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			for i in range (1,4):
				switch_to("xpath",'//*[@id="transfers-tab-iframe"]')
				span_click("批量转账")
				switch_to("xpath",'//*[@id="subTabTwo-iframe"]')
				
				click("xpath",'//*[@id="gridtitle"]/div[3]/div[2]')
				sleep(1)
				switch_to("xpath",'//*[@id="importDataWin-iframe"]')
				sleep(1)
				span_click("下一步")
				switch_to("xpath",'//*[@id="loadNextWin-iframe"]')
				sleep(1)
				#交易类型
				click_up_click('//*[@id="combobox-input-paytypeid"]')
				
				# 附件上传
				upload_click("xpath", "//div[text()='上传文件']/parent::*[1]/descendant::*[4]",
				             'D:\FlieDownload', '"NeiBuZhangHuZhuanZhangPLZZ.xls"')
				sleep(3)
				# 点击保存按钮
				click("xpath", "//span[text()='上传']")
				# 退出所有iframe窗体
				switch_default()
				# 用隐式等待方法等页面出现新增成功的提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功')]")
				if i==3 :
					print("资金池内部计价--内部转账转账，批量转账，上传成功！")
				time.sleep(3)
				click("xpath", "//span[text()='内部账户转账']")
				sleep(1)
				switch_default()
			
			# 测试删除功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="transfers-tab-iframe"]')
			span_click("批量转账")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			
			#刷新、勾选按钮
			click("xpath",'//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath",'//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("删除")
			ok_click()
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("资金池内部计价--内部转账转账，批量转账，删除成功！")
			time.sleep(3)
			
			# 测试送审功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="transfers-tab-iframe"]')
			span_click("批量转账")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[2]/td[2]/div/button')
			sleep(1)
			
			span_click("送审")
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("资金池内部计价--内部转账转账，批量转账，送审成功！")
			time.sleep(3)
			
			# 测试撤销送审功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="transfers-tab-iframe"]')
			span_click("批量转账")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[2]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("送审",'撤销送审')
			ok_click()
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'撤销送审成功！')]")
			print("资金池内部计价--内部转账转账，批量转账，撤销送审成功！")
			time.sleep(3)
			
			# 测试审核功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="transfers-tab-iframe"]')
			span_click("批量转账")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("审核")
			ok_click()
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("资金池内部计价--内部转账转账，批量转账，审核成功！")
			time.sleep(3)
			
			# 测试取消审核功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="transfers-tab-iframe"]')
			span_click("批量转账")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element('审核','取消审核')
			ok_click()
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("资金池内部计价--内部转账转账，批量转账，取消审核成功！")
			time.sleep(3)
			
			# 测试支付功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="transfers-tab-iframe"]')
			span_click("批量转账")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("审核")
			ok_click()
			sleep(3)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("支付")
			ok_click()
			span_click("确定")
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("资金池内部计价--内部转账转账，批量转账，支付成功！")
			time.sleep(3)
		
			# 回到初始界面
			click("xpath", "//span[text()='资金池内部计价']")
			sleep(1)
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("批量转账受理失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
			
			# def tearDown(self):
			#     self.driver.quit()
			print("结束时间：", time.strftime("%Y-%m-%d %H:%M:%S"))
		
		# 测试资金池内部计价--内部转账转账-批量转账🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱
		try:
			logger.info("测试资金池内部计价--内部转账转账-批量转账")
			
			click("xpath", "//span[text()='资金池内部计价']")
			sleep(1)
			click("xpath", "//span[text()='内部账户转账']")
			sleep(1)
			switch_default()
			
			# 创建交易类型及结算方式💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			click("xpath", "//span[text()='资金池内部计价']")
			sleep(1)
			js_click("xpath", "//span[contains(text(),'内部资金池')]")
			sleep(1)
			js_gd("xpath", "//span[contains(text(),'资金结算管理')]")
			sleep(1)
			js_click("xpath", "//span[contains(text(),'资金结算管理')]")
			sleep(1)
			
			# 点击基础设置
			click("xpath",
			      '/html/body/div[1]/div[1]/div/div[2]/div/div[2]/div/div/div/div[4]/div/div/ul/li[1]/a/span[2]')
			sleep(1)
			
			#结算方式
			click("xpath", "//span[text()='结算方式']")
			sleep(1)
			switch_to("xpath",'//*[@id="settlementMode-tab-iframe"]')
			
			span_click("新增")
			switch_to("xpath",'//*[@id="addWin-iframe"]')
			
			#代码
			input("xpath",'//*[@id="code"]','2057')
			sleep(1)
			
			#名称
			input("xpath",'//*[@id="name"]','结购汇内部转账')
			sleep(1)
			
			#交易方向
			input_up_click('//*[@id="combobox-input-moneyway"]','支出')
			
			#支付类型
			input_up_click('//*[@id="combobox-input-dealtype"]','结算中心转账')
			
			span_click("保存")
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			sleep(3)
			
			# 交易类型
			click("xpath", "//span[text()='交易类型']")
			sleep(1)
			switch_to("xpath", '//*[@id="payType-tab-iframe"]')
			
			span_click("新增")
			switch_to("xpath",'//*[@id="addWin-iframe"]')
			
			#代码
			input("xpath",'//*[@id="code"]','3057')
			sleep(1)
			
			#名称
			input("xpath",'//*[@id="name"]','结购汇内部转账')
			sleep(1)
			
			#交易方向
			input_up_click('//*[@id="combobox-input-moneyway"]','支出')
			
			#交易类型类型
			input_up_click('//*[@id="combobox-input-paytypecategory"]','结汇')
			
			#可选结算方式
			input("xpath",'//*[@id="combobox-input-settlementmoderange"]','2057')
			sleep(1)
			click("xpath",'//*[@id="settlementmoderange-combogrid-body-table"]/tbody/tr/td[2]/div/button')
			sleep(1)
			
			#默认结算方式
			click_up_click('//*[@id="combobox-input-defaultsettlementmodeid"]')
			
			#计划项目
			input_up_click('//*[@id="combobox-input-budgetitemrequiredtype"]','非必填')
			
			span_click("保存")
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			sleep(3)
			
			#回到初始界面
			# 点击基础设置
			click("xpath",
			      '/html/body/div[1]/div[1]/div/div[2]/div/div[2]/div/div/div/div[4]/div/div/ul/li[1]/a/span[2]')
			sleep(1)
			js_click("xpath", "//span[contains(text(),'资金结算管理')]")
			sleep(1)
			js_click("xpath", "//span[contains(text(),'内部资金池')]")
			sleep(1)
			click("xpath", "//span[text()='资金池内部计价']")
			sleep(1)
			click("xpath", "//span[text()='内部账户转账']")
			sleep(1)
			switch_default()
			
			
			# 测试新增功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			for i  in range (1,4):
				switch_to("xpath", '//*[@id="transfers-tab-iframe"]')
				span_click("结购汇")
				switch_to("xpath", '//*[@id="subTabThree-iframe"]')
				
				span_click("新增")
				switch_to("xpath",'//*[@id="addWin-iframe"]')
				
				#交易类型
				click_up_click('//*[@id="combobox-input-paytypeid"]')
				
				#结汇账户池
				input_up_click('//*[@id="combobox-input-accountpoolid"]','内部账户转账')
				
				#结汇账户
				click_up_click('//*[@id="combobox-input-ourinternalaccountid"]')
				
				#结汇金额
				money = random.randint(1,300)
				money2=money*6.0
				double_click("xpath",'//*[@id="ouramount-input"]')
				sleep(1)
				input("xpath",'//*[@id="ouramount-input"]',str(money))
				
				#收方账户池
				input_up_click('//*[@id="combobox-input-oppaccountpoolid"]','内部账户转账')
				
				#收方内部账户
				click_up_click('//*[@id="combobox-input-oppinternalaccountid"]')
				
				#收方金额
				double_click("xpath",'//*[@id="oppamount-input"]')
				sleep(1)
				input("xpath",'//*[@id="oppamount-input"]',str(money2))
				sleep(1)
				
				span_click("保存")
				
				#退出所有窗体
				switch_default()
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				if i == 3 :
					print("资金池内部计价--内部转账转账，结购汇转账，新增成功！")
				time.sleep(3)
			
			# 测试修改功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="transfers-tab-iframe"]')
			span_click("结购汇")
			switch_to("xpath", '//*[@id="subTabThree-iframe"]')
			
			#刷新、勾选按钮
			click("xpath",'//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath",'//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("修改")
			switch_to("xpath",'//*[@id="modWin-iframe"]')
			sleep(1)
			
			input("xpath",'//*[@id="combobox-input-purpose"]','测试修改')
			
			span_click("保存")
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("资金池内部计价--内部转账转账，结购汇转账，修改成功！")
			time.sleep(3)
			
			# 测试删除功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="transfers-tab-iframe"]')
			span_click("结购汇")
			switch_to("xpath", '//*[@id="subTabThree-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("删除")
			ok_click()
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("资金池内部计价--内部转账转账，结购汇转账，删除成功！")
			time.sleep(3)
			
			# 测试作废功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="transfers-tab-iframe"]')
			span_click("结购汇")
			switch_to("xpath", '//*[@id="subTabThree-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[2]/td[2]/div/button')
			sleep(1)
			
			span_click("作废")
			ok_click()
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("资金池内部计价--内部转账转账，结购汇转账，作废成功！")
			time.sleep(3)
			
			# 测试审核功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="transfers-tab-iframe"]')
			span_click("结购汇")
			switch_to("xpath", '//*[@id="subTabThree-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("审核")
			ok_click()
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("资金池内部计价--内部转账转账，结购汇转账，审核成功！")
			time.sleep(3)
			
			# 测试取消审核功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="transfers-tab-iframe"]')
			span_click("结购汇")
			switch_to("xpath", '//*[@id="subTabThree-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("审核",'取消审核')
			ok_click()
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("资金池内部计价--内部转账转账，结购汇转账，取消审核成功！")
			time.sleep(3)
			
			# 测试支付功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="transfers-tab-iframe"]')
			span_click("结购汇")
			switch_to("xpath", '//*[@id="subTabThree-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("审核")
			ok_click()
			sleep(3)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("支付")
			ok_click()
			click("xpath",'//*[@id="submit"]/span/span')
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("资金池内部计价--内部转账转账，结购汇转账，支付成功！")
			time.sleep(3)
			
			# 测试打印功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="transfers-tab-iframe"]')
			span_click("结购汇")
			switch_to("xpath", '//*[@id="subTabThree-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("打印")
			# 获取所有窗口句柄
			all_handles = self.driver.window_handles
			# 循环遍历所有新打开的窗口句柄，也就是说不包括主窗口
			now_handle = self.driver.current_window_handle
			for handle in all_handles:
				self.driver.switch_to.window(handle)
				if self.driver.title == u"internalsettlementprint":
					implici_wait("xpath", "//td[contains(text(),'Mindy科技有限公司')]")
					print("资金池内部计价--内部转账转账，结购汇转账，打印成功！")
					time.sleep(3)
					self.driver.switch_to.window(now_handle)
					switch_default()
			
			# 回到初始界面
			click("xpath", "//span[text()='资金池内部计价']")
			sleep(1)
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("批量转账受理失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
			
			# def tearDown(self):
			#     self.driver.quit()
			print("结束时间：", time.strftime("%Y-%m-%d %H:%M:%S"))
		
		
		# 测试资金池内部计价-内部账户明细🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱
		try:
			logger.info("测试资金池内部计价--内部账户明细")
			
			click("xpath", "//span[text()='资金池内部计价']")
			sleep(1)
			click("xpath", "//span[text()='内部账户明细']")
			sleep(1)
			switch_default()
			
			# 测试新增功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath",'//*[@id="internalTransactions-tab-iframe"]')
			
			span_click("新增")
			switch_to("xpath",'//*[@id="addWin-iframe"]')
			
			#内部账户
			click_up_click('//*[@id="combobox-input-internalaccountid"]')
			
			#交易日期
			today = date.today()
			input("xpath",'//*[@id="tradedate-input"]',str(today))
			sleep(1)
			
			#交易时间
			click("xpath",'//*[@id="tradedatetime-trigger"]')
			sleep(1)
			switch_default()
			switch_to("xpath",'/html/body/div[6]/iframe')
			click("xpath",'//*[@id="dpTodayInput"]')
			sleep(1)
			switch_default()
			switch_to("xpath",'//*[@id="internalTransactions-tab-iframe"]')
			switch_to("xpath", '//*[@id="addWin-iframe"]')
			
			#交易方向
			input_up_click('//*[@id="combobox-input-moneyway"]','支出')
			
			#交易金额
			money =str(random.randint(1,300))
			input("xpath",'//*[@id="amount-input"]',money)
			sleep(1)
			
			span_click("保存")
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("资金池内部计价--内部账户明细，新增成功！")
			time.sleep(3)
			
			# 测试修改功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath",'//*[@id="internalTransactions-tab-iframe"]')
			
			#刷新、勾选按钮
			click("xpath",'//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath",'//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("修改")
			switch_to("xpath",'//*[@id="modWin-iframe"]')
			input("xpath",'//*[@id="comments"]','测试修改')
			sleep(1)
			
			span_click("保存")
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("资金池内部计价--内部账户明细，修改成功！")
			time.sleep(3)
			
			# 测试删除功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath",'//*[@id="internalTransactions-tab-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("删除")
			ok_click()
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'成功删除1笔内部账户明细！')]")
			print("资金池内部计价--内部账户明细，删除成功！")
			time.sleep(3)
			
			
			# 回到初始界面
			click("xpath", "//span[text()='资金池内部计价']")
			sleep(1)
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("内部账户明细失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
			
			# def tearDown(self):
			#     self.driver.quit()
			print("结束时间：", time.strftime("%Y-%m-%d %H:%M:%S"))
		
		
		# 测试资金池内部计价-内部账户余额🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱
		try:
			logger.info("测试资金池内部计价--内部账户明细")
			
			click("xpath", "//span[text()='资金池内部计价']")
			sleep(1)
			click("xpath", "//span[text()='内部账户余额']")
			sleep(1)
			switch_default()
			
			# 测试内部账户余额查看💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="balances-tab-iframe"]')
			span_click("内部账户余额")
			switch_to("xpath",'//*[@id="subTabTwo-iframe"]')
			
			double_click("xpath",'//*[@id="grid-body-table"]/tbody/tr[1]/td[3]/div')
			sleep(1)
			switch_to("xpath",'//*[@id="detailWin-iframe"]')
			sleep(1)
		
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'内部账户')]")
			print("资金池内部计价--内部账户明细，查看成功！")
			switch_default()
			click("xpath", "//span[text()='内部账户余额']")
			time.sleep(3)
			
			# 测试下属单位内部余额查看💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="balances-tab-iframe"]')
			span_click("下属单位内部账户余额查看")
			switch_to("xpath", '//*[@id="subTabThree-iframe"]')
			
			double_click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[3]/div')
			sleep(1)
			switch_to("xpath", '//*[@id="detailWin-iframe"]')
			sleep(1)
			
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'内部账户')]")
			print("资金池内部计价--下属单位内部账户余额查看，查看成功！")
			switch_default()
			click("xpath", "//span[text()='内部账户余额']")
			time.sleep(3)
			
		
			# 回到初始界面
			click("xpath", "//span[text()='资金池内部计价']")
			sleep(1)
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("内部账户明细失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
			
			# def tearDown(self):
			#     self.driver.quit()
			print("结束时间：", time.strftime("%Y-%m-%d %H:%M:%S"))
		
		
		# 测试资金池内部计价-内部账户计息🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱
		try:
			logger.info("测试资金池内部计价--内部账户计息")
			
			click("xpath", "//span[text()='资金池内部计价']")
			sleep(1)
			click("xpath", "//span[text()='内部账户计息']")
			sleep(1)
			switch_default()
			
			#测试新增功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="interests-tab-iframe"]')
			
			span_click("新增")
			switch_to("xpath", '//*[@id="addWin-iframe"]')
			
			# 内部账户
			input_up_click('//*[@id="combobox-input-internalaccountid"]', '结汇')
			
			# 计息开始时间
			begenday = date.today() - timedelta(days=15)
			
			input("xpath", '//*[@id="begindate-input"]', str(begenday))
			sleep(1)
			
			# 计息结束日期
			click("xpath", '//*[@id="enddate-trigger"]')
			sleep(1)
			switch_default()
			switch_to("xpath", '/html/body/div[6]/iframe')
			click("xpath", '//*[@id="dpTodayInput"]')
			sleep(1)
			
			switch_default()
			switch_to("xpath", '//*[@id="interests-tab-iframe"]')
			switch_to("xpath", '//*[@id="addWin-iframe"]')
			span_click("保存")
			
			# 退出所有窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'成功生成一笔')]")
			print("资金池内部计价--内部账户计息，新增成功！")
			time.sleep(3)
				
			# 测试修改功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="interests-tab-iframe"]')
			
			#刷新、勾选按钮
			click("xpath",'//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath",'//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("修改")
			switch_to("xpath",'//*[@id="modWin-iframe"]')
			sleep(1)
			
			input("xpath",'//*[@id="description"]','测试修改')
			sleep(1)
			
			span_click("保存")
			# 退出所有窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("资金池内部计价--内部账户计息，修改成功！")
			time.sleep(3)
			
			
			# 测试结息功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="interests-tab-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("结息")
			click("xpath",'//*[@id="settleWin-btn-0"]/div[2]')
			sleep(1)
			# 退出所有窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'结息成功1笔计息单！')]")
			print("资金池内部计价--内部账户计息，结息成功！")
			time.sleep(3)
			
			# 测试反结息功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="interests-tab-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("反结息")
			
			
			# 退出所有窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'反结息成功1笔计息单！')]")
			print("资金池内部计价--内部账户计息，反结息成功！")
			time.sleep(3)
			
			# 测试打印功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="interests-tab-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("打印")
			# 获取所有窗口句柄
			all_handles = self.driver.window_handles
			# 循环遍历所有新打开的窗口句柄，也就是说不包括主窗口
			now_handle = self.driver.current_window_handle
			for handle in all_handles:
				self.driver.switch_to.window(handle)
				if self.driver.title == u"interestsprint":
					implici_wait("xpath", "//td[contains(text(),'结息日期')]")
					print("资金池内部计价--内部账户计息，打印成功！")
					time.sleep(3)
					self.driver.switch_to.window(now_handle)
					switch_default()
		
			
			# 测试删除功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="interests-tab-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("删除")
			ok_click()
			# 退出所有窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'成功删除1笔计息单！')]")
			print("资金池内部计价--内部账户计息，删除成功！")
			time.sleep(3)
			
			# 回到初始界面
			click("xpath", "//span[text()='资金池内部计价']")
			sleep(1)
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("内部账户计息失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
			
			# def tearDown(self):
			#     self.driver.quit()
			print("结束时间：", time.strftime("%Y-%m-%d %H:%M:%S"))
		
		
		# 测试资金池内部计价-账户余额确认🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱
		try:
			logger.info("测试资金池内部计价--账户余额确认")
			
			click("xpath", "//span[text()='资金池内部计价']")
			sleep(1)
			click("xpath", "//span[text()='账户余额确认']")
			sleep(1)
			switch_default()
			
			# 测试余额确认功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath",'//*[@id="balanceConfirm-tab-iframe"]')
			span_click("余额确认")
			switch_to("xpath",'//*[@id="subTabOne-iframe"]')
			
			span_click("余额确认")
			switch_to("xpath",'//*[@id="confirmWin-iframe"]')
			
			#内部账户
			input("xpath",'//*[@id="combobox-input-internalaccountid"]','结汇')
			sleep(1)
			click("xpath",'//*[@id="internalaccountid-combogrid-body-table"]/tbody/tr/td[2]/div/button')
			sleep(1)
			
			
			#余额日期
			today= date.today()
			input("xpath",'//*[@id="reportdate-input"]',str(today))
			sleep(1)
			
			span_click("查询")
			
			#勾选按钮
			click("xpath",'//*[@id="editgrid-syscheck-0"]')
			sleep(1)
			
			input_up_click('//*[@id="combobox-input-editgrid-confirmresult-0"]','相符')
			
			span_click("确认")
			
			# 退出所有窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("资金池内部计价--账户余额确认，确认成功！")
			time.sleep(3)
			click("xpath", "//span[text()='账户余额确认']")
			sleep(1)
			
			# 测试确认结果查看功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="balanceConfirm-tab-iframe"]')
			span_click("确认结果查看")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			double_click("xpath",'//*[@id="grid-body-table"]/tbody/tr/td[3]/div')
			sleep(1)
			switch_to("xpath",'//*[@id="detailWin-iframe"]')
			
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'内部账户池')]")
			print("资金池内部计价--账户余额确认，确认结果查看成功！")
			#退出所有窗体
			switch_default()
			click("xpath", "//span[text()='账户余额确认']")
			time.sleep(3)
			
			# 测试取消确认功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="balanceConfirm-tab-iframe"]')
			span_click("余额确认")
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			
			#刷新、勾选按钮
			click("xpath",'//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath",'//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
			sleep(1)
			
			span_click("取消确认")
			# 退出所有窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("资金池内部计价--账户余额确认，取消确认成功！")
			time.sleep(3)
			
			# 回到初始界面
			click("xpath", "//span[text()='资金池内部计价']")
			sleep(1)
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("内部账户计息失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
			
			# def tearDown(self):
			#     self.driver.quit()
			print("结束时间：", time.strftime("%Y-%m-%d %H:%M:%S"))
		'''
		
		# 测试内部资金池--项目资金管理--项目初期设置🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱
		try:
			logger.info("测试内部资金池--项目资金管理--项目初期设置")
			
			click("xpath", "//span[text()='项目资金管理']")
			sleep(1)
			click("xpath", "//span[text()='项目期初设置']")
			sleep(1)
			switch_default()
			
			# 作数据💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			click("xpath", "//span[text()='项目资金管理']")
			sleep(1)
			
			# 退出所有窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("资金池内部计价--账户余额确认，确认成功！")
			time.sleep(3)
			click("xpath", "//span[text()='账户余额确认']")
			sleep(1)
			
			
			
			# 回到初始界面
			click("xpath", "//span[text()='资金池内部计价']")
			sleep(1)
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("内部账户计息失败！" + str(traceback.format_exc()))
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
