# encoding=utf-8
# @Time : 2021/01/04 13:30
# @Author : zzg
# 此文件是测试Mysql版本资金结算管理--结算中心收付（委托付款申请、委托付款受理）
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


class Test54_ZiJinJieSuanGuanLi_JSZXSF(unittest.TestCase):
	
	# 启动浏览器
	def setUp(self):
		# 启动浏览器的另外一个方法：通过封装启动浏览器的驱动，启动不同浏览器
		self.driver = get("chrome")
	
	# 登陆系统、对系统设置进行操作
	def test_trade(self):
		
		# login(G_Ora_Url, mindy, Password, "亚唐科技")
		login(G_Mys_Url, mindy, Password, "亚唐科技")
		
		logging.info("开始测试资金结算管理--结算中心收付")
		#选择组织
		choose_organization("Mindy科技有限公司")
		
		# 将页面的滚动条滑动到‘资金结算管理’页面的地方
		js_gd("xpath", "//span[contains(text(),'资金结算管理')]")
		# 用JS的方法点击资金结算管理菜单按钮
		js_click("xpath", "//span[contains(text(),'资金结算管理')]")
		sleep(1)
		# 点击'外币收付结算'菜单
		click("xpath", "//span[text()='结算中心收付']")
		sleep(2)
		# 退出所有iframe窗体
		switch_default()
		
		'''
		#创建需要的数据🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱
		try:
			#创建所需数据💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			#选择组织
			choose_organization("亚唐科技")
			
			#创建内部账户利率方案
			# 点击系统设置
			click("xpath", "//div[@class='sysconfigset']")
			sleep(1)
			# 点击进入系统设置页面
			switch_to("xpath", "//iframe[@id='systemconfig-tab-iframe']")
			sleep(1)
			
			# 将页面的滚动条滑动到‘利率方案’页面的地方
			js_gd("xpath", "//span[contains(text(),'利率方案')]")
			# 用JS的方法利率方案字段菜单按钮
			js_click("xpath", "//span[contains(text(),'利率方案')]")
			sleep(1)
			
			switch_default()
			switch_to("xpath", "//iframe[@id='interestRateSchemes-tab-iframe']")
			sleep(1)
			# 用JS的方法点击新增按钮
			js_click("xpath", "//span[text()='新增']")
			sleep(1)
			# 切入新增的iframe窗体
			switch_to("xpath", "//iframe[@id='addWin-iframe']")
			sleep(1)
			
			# 输入代码
			code = "LV"+str(random.randint(0,1000))
			input("xpath", "//input[@name='code']",code )
			sleep(1)
			
			# 输入名称
			name="内部账户"+str(code)
			input("xpath", "//input[@id='name']", name)
			sleep(1)
			# 单据对象
			input_up_click("//input[@id='combobox-input-noteobjectid']",'内部账户')
			
			# 利率类型
			input_up_click("//input[@id='combobox-input-interestratetypeid']",'固定利率')
			
			# 共享模式combobox-input-includemode
			input_up_click("//input[@id='combobox-input-includemode']", "下属组织共享")
			
			# 点击保存按钮
			click("xpath", "//span[text()='保存']")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("内部账户利率方案，保存成功！")
			time.sleep(3)
			
			
			#创建内部账号💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 将页面的滚动条滑动到‘资金结算管理’页面的地方
			js_gd("xpath", "//span[contains(text(),'内部资金池')]")
			# 用JS的方法点击资金结算管理菜单按钮
			js_click("xpath", "//span[contains(text(),'内部资金池')]")
			sleep(1)
			# 点击'外币收付结算'菜单
			click("xpath", "//span[text()='资金池内部计价']")
			sleep(1)
			#点击内部账户管理
			click("xpath", "//span[text()='内部账户管理']")
			sleep(1)
			#退出所有窗体
			switch_default()
			for i in range(1,3):
				# 切入内部账户管理窗体
				switch_to("xpath", '//*[@id="accountManage-tab-iframe"]')
				sleep(3)
				span_click("新增内部账户池")
				
				switch_to("xpath", '//*[@id="addWin-iframe"]')
				# 代码  202106081346 202106081348
				code = str(time.strftime("%Y%m%d%H%M%S"))
				input("xpath", '//*[@id="code"]', code)
				sleep(1)
				
				# 名称
				name = "YT" + str(time.strftime("%Y%m%d%S"))
				input("xpath", '//*[@id="name"]', name)
				sleep(1)
				
				span_click("保存")
				switch_parent()
				sleep(3)
				
				# 新增内部账户
				span_click("新增内部账户")
				switch_to("xpath", '//*[@id="addWin-iframe"]')
				# 内部账户池
				input_up_click('//*[@id="combobox-input-accountpoolid"]', name)
				
				# 账户所属组织
				if i ==1:
					input_up_click('//*[@id="combobox-input-orgid"]', 'Mindy科技有限公司')
				if i ==2:
					input_up_click('//*[@id="combobox-input-orgid"]', '亚唐科技')
				
				# 账号
				number = str(time.strftime("%Y%m%d%H%M%S"))
				input("xpath", '//*[@id="code"]', number)
				sleep(1)
				
				# 名称
				name = "KJ" + str(time.strftime("%Y%m%d%S"))
				input("xpath", '//*[@id="name"]', name)
				sleep(1)
				
				# 币种
				input_up_click('//*[@id="combobox-input-currencyid"]', 'CNY-人民币')
				
				# 账户存款类型
				input_up_click('//*[@id="combobox-input-deposittype"]', '活期')
				
				# 存贷标志
				input_up_click('//*[@id="combobox-input-depositloansign"]', '1:存款')
				
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
				implici_wait("xpath", "//span[contains(text(),'操作成功')]")
				time.sleep(3)
				
				# 切入内部账户管理窗体
				switch_to("xpath", '//*[@id="accountManage-tab-iframe"]')
				# 查询
				if i ==1:
					click("xpath", '//*[@id="north"]/div[2]/span')
					sleep(1)
				if i ==2 :
					click("xpath",'//*[@id="combobox-input-urid"]')
					sleep(1)
					click("xpath",'//*[@id="urid-combogrid-head-table"]/thead/tr/th[2]/div/button')
					sleep(1)
					click("xpath", '//*[@id="urid-combogrid-head-table"]/thead/tr/th[2]/div/button')
					sleep(1)
				input("xpath", '//*[@id="combobox-input-urid"]', number)
				sleep(1)
				click("xpath", '//*[@id="urid-combogrid-body-table"]/tbody/tr/td[2]/div/button')
				sleep(1)
				span_click("查询")
				click("xpath", '//*[@id="t1_t0_t0-fixed"]/td[2]/div/button')
				sleep(1)
				# 开户
				triangle_cick_and_element("维护", '开户')
				# 初始余额
				double_click("xpath", '//*[@id="initbalance-input"]')
				sleep(1)
				input("xpath", '//*[@id="initbalance-input"]', '50000')
				sleep(1)
				click("xpath", '//div[text()="确定"]')
				
				# 退出所有窗体
				switch_default()
				implici_wait("xpath", "//span[contains(text(),'操作成功')]")
				sleep(3)
			print("内部账户管理，新增账户成功")
			time.sleep(3)
			
			
			
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("创建数据失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
			# def tearDown(self):
			#     self.driver.quit()
			print("结束时间：", time.strftime("%Y-%m-%d %H:%M:%S"))
		'''

		# 测试结算中心收付-委托付款申请-单笔转账处理,以及委托付款受理-单笔转账处理🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱
		try:
			logger.info("测试委托付款申请->单笔转账处理->单笔转账处理")
			# 选择组织
			choose_organization("Mindy科技有限公司")
			# 将页面的滚动条滑动到‘资金结算管理’页面的地方
			js_gd("xpath", "//span[contains(text(),'资金结算管理')]")
			# 用JS的方法点击资金结算管理菜单按钮
			js_click("xpath", "//span[contains(text(),'资金结算管理')]")
			sleep(1)
			# 点击'外币收付结算'菜单
			click("xpath", "//span[text()='结算中心收付']")
			sleep(2)
			# 退出所有iframe窗体
			switch_default()
			click("xpath", "//span[text()='委托付款申请']")
			sleep(1)
			switch_default()
			
			#测试新增💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			#切入单笔转账处理页面
			for i in range(1,4):
				#切入单笔转账处理窗体
				switch_to("xpath",'//*[@id="settleCenterApply-tab-iframe"]')
				switch_to("xpath",'//*[@id="subTabTwo-iframe"]')
				sleep(1)
				span_click("新增")
				#切入新增窗体
				switch_to("xpath",'//*[@id="addWin-iframe"]')
				#受托组织
				click_up_click('//*[@id="combobox-input-entrustorgid"]')
				
				#付方内部账户
				click_up_click('//*[@id="combobox-input-ourinternalaccountid"]')
				
				#交易类型
				input_up_click('//*[@id="combobox-input-paytypeid"]','103-对外付款')
				
				#结算方式
				input_up_click('//*[@id="combobox-input-settlementmodeid"]','101-直联单笔转账')
				
				#付方账户
				click_up_click('//*[@id="combobox-input-ourbankaccountid"]')
				
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
				click_up_click('//*[@id="combobox-input-oppbanklocationid"]')
				
				# 金额
				money = random.randint(0, 1000)
				input("xpath", '//*[@id="oppamount-input"]', money)
				sleep(1)
				
				#用途
				input("xpath",'//*[@id="combobox-input-purpose"]','单笔转账处理21')
				sleep(1)
				
				span_click("保存")
				switch_default()
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				if i == 3:
					print("委托付款申请-单笔转账处理，新增成功")
				time.sleep(3)
			
			# 测试修改💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入单笔转账处理窗体
			switch_to("xpath", '//*[@id="settleCenterApply-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			#刷新、勾选按钮
			click("xpath",'//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath",'//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("修改")
			switch_to("xpath",'//*[@id="modWin-iframe"]')
			input("xpath",'//*[@id="memo"]','修改')
			sleep(1)
			span_click("保存")
			#退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("委托付款申请-单笔转账处理，修改成功")
			time.sleep(3)
			
			# 测试删除功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入单笔转账处理窗体
			switch_to("xpath", '//*[@id="settleCenterApply-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
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
			print("委托付款申请-单笔转账处理，删除成功")
			time.sleep(3)
			
			# 测试送审功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入单笔转账处理窗体
			switch_to("xpath", '//*[@id="settleCenterApply-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("送审")
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！送审成功1笔，失败0笔。')]")
			print("委托付款申请-单笔转账处理，送审成功")
			time.sleep(3)
			
			# 测试撤销送审功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入单笔转账处理窗体
			switch_to("xpath", '//*[@id="settleCenterApply-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
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
			print("委托付款申请-单笔转账处理，撤销送审成功")
			time.sleep(3)
			
			# 测试复制功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入单笔转账处理窗体
			switch_to("xpath", '//*[@id="settleCenterApply-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("复制")
			ok_click()
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("委托付款申请-单笔转账处理，复制成功")
			time.sleep(3)
			
			# 测试作废功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入单笔转账处理窗体
			switch_to("xpath", '//*[@id="settleCenterApply-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
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
			print("委托付款申请-单笔转账处理，作废成功")
			time.sleep(3)
			
			# 测试提交功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入单笔转账处理窗体
			switch_to("xpath", '//*[@id="settleCenterApply-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
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
			switch_default()
			sleep(3)
			
			#对第二笔数据进行送审
			# 切入单笔转账处理窗体
			switch_to("xpath", '//*[@id="settleCenterApply-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			# 刷新、勾选按钮
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
			print("委托付款申请-单笔转账处理，提交成功")
			time.sleep(3)
			
			# 测试变更功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			sql = "update T_SE_PAYMENTAPPLYS set DEALSTATE = '4' where PURPOSE = '单笔转账处理21'"
			my_sql(my_host, my_port, my_user, my_passwd, my_db,
			       sql)
			# 切入单笔转账处理窗体
			switch_to("xpath", '//*[@id="settleCenterApply-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click('变更')
			switch_to("xpath",'//*[@id="modWin-iframe"]')
			span_click("保存")
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("委托付款申请-单笔转账处理，变更成功")
			time.sleep(3)
			
			#测试打印功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入单笔转账处理窗体
			switch_to("xpath", '//*[@id="settleCenterApply-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[2]/td[2]/div/button')
			sleep(1)
			
			span_click("提交")
			ok_click()
			switch_default()
			
			#去上级组织审批数据
			choose_organization("亚唐科技")
			
			# 将页面的滚动条滑动到‘资金结算管理’页面的地方
			js_gd("xpath", "//span[contains(text(),'资金结算管理')]")
			# 用JS的方法点击资金结算管理菜单按钮
			js_click("xpath", "//span[contains(text(),'资金结算管理')]")
			sleep(1)
			# 点击'外币收付结算'菜单
			click("xpath", "//span[text()='结算中心收付']")
			sleep(1)
			click("xpath", "//span[text()='委托付款受理']")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			
			#切入委托付款受理窗体
			switch_to("xpath",'//*[@id="settleCenterDeal-tab-iframe"]')
			switch_to("xpath",'//*[@id="subTabTwo-iframe"]')
			sleep(1)
			click("xpath",'//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
			sleep(1)
			span_click("受理")
			switch_to("xpath",'//*[@id="modWin-iframe"]')
			span_click("保存")
			
			#退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("委托付款处理-单笔转账处理，受理成功")
			time.sleep(3)
			
			#委托付款受理打回💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入委托付款受理窗体
			switch_to("xpath", '//*[@id="settleCenterDeal-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			sleep(1)
			#刷新、勾选按钮
			click("xpath",'//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
			sleep(1)
			span_click("打回")
			ok_click()
			input("xpath",'//*[@id="refuseReason"]','测试打回')
			sleep(1)
			span_click("确定")
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'打回操作成功:1笔!失败0笔！')]")
			print("委托付款处理-单笔转账处理，打回成功")
			time.sleep(3)
			
			
			# 选择组织
			choose_organization("Mindy科技有限公司")
			# 将页面的滚动条滑动到‘资金结算管理’页面的地方
			js_gd("xpath", "//span[contains(text(),'资金结算管理')]")
			# 用JS的方法点击资金结算管理菜单按钮
			js_click("xpath", "//span[contains(text(),'资金结算管理')]")
			sleep(1)
			# 点击'外币收付结算'菜单
			click("xpath", "//span[text()='结算中心收付']")
			sleep(1)
			click("xpath", "//span[text()='委托付款申请']")
			sleep(1)
			
			#测试上传功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入单笔转账处理窗体
			switch_to("xpath", '//*[@id="settleCenterApply-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			sleep(1)
			# 点击上传按钮
			click("xpath", '//*[@id="gridtitle"]/div[3]/div[2]')
			sleep(1)
			# 切入新出来的窗体
			switch_to("xpath", '//*[@id="importDataWin-iframe"]')
			sleep(1)
			span_click("下一步")
			
			# 切入新出来的窗体
			switch_to("xpath", '//*[@id="loadNextWin-iframe"]')
			sleep(1)
			# 选择交易类型
			input_up_click('//*[@id="combobox-input-paytypeid"]','103-对外付款')
			
			# 附件上传
			upload_click("xpath", "//div[text()='上传文件']/parent::*[1]/descendant::*[4]",
			             'D:\FlieDownload', '"DanBiZhuanZhangChuLi.xls"')
			sleep(3)
			# 点击保存按钮
			click("xpath", "//span[text()='上传']")
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功')]")
			print("委托付款申请-单笔转账处理，导入成功！")
			time.sleep(3)
			
			#返回委托付款处理页面
			click("xpath", "//span[text()='委托付款申请']")
			sleep(1)
			
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("单笔转账处理失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
			
			# def tearDown(self):
			#     self.driver.quit()
			print("结束时间：", time.strftime("%Y-%m-%d %H:%M:%S"))
	
	
		# 测试结算中心收付-委托付款申请-直联批量付款🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱
		try:
			logger.info("测试委托付款申请->直联批量付款，以及委托付款处理->直联批量付款")
			click("xpath", "//span[text()='委托付款申请']")
			sleep(1)
			switch_default()
			
			#测试上传功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			for i in range(1,5):
				#切入直联批量付款窗体
				switch_to("xpath",'//*[@id="settleCenterApply-tab-iframe"]')
				span_click("直联批量付款")
				switch_to("xpath",'//*[@id="subTabSeven-iframe"]')
				
				click("xpath",'//*[@id="gridtitle"]/div[3]/div[2]')
				sleep(1)
				switch_to("xpath",'//*[@id="importDataWin-iframe"]')
				sleep(1)
				
				input_up_click('//*[@id="combobox-input-businessid"]','委托付款申请直联批量付款导入')
				
				span_click("下一步")
				switch_to("xpath",'//*[@id="loadNextWin-iframe"]')
				sleep(1)
				#受托组织
				click_up_click('//*[@id="combobox-input-entrustorgid"]')
				
				#付方内部账户
				click_up_click('//*[@id="combobox-input-ourinternalaccountid"]')
				
				#交易类型
				input_up_click('//*[@id="combobox-input-paytypeid"]','3013-付款处理批量付款交易类型')
				
				#付方账户
				input_up_click('//*[@id="combobox-input-ourbankaccountid"]','20211013')
				
				upload_click("xpath", "//div[text()='上传文件']/parent::*[1]/descendant::*[4]",
				             'D:\FlieDownload', '"WeiTuoFuKuanShenQingPLFK.xls"')
				sleep(3)
				# 点击上传按钮
				click("xpath", "//span[text()='上传']")
				sleep(1)
				# 退出所有iframe窗体
				switch_default()
				# 用隐式等待方法等页面出现新增成功的提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功')]")
				if i ==3:
					print("委托付款申请-直联批量付款，导入成功！")
				time.sleep(3)
				click("xpath", "//span[text()='委托付款申请']")
				sleep(1)
			
			# 测试删除功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入直联批量付款窗体
			switch_to("xpath", '//*[@id="settleCenterApply-tab-iframe"]')
			span_click("直联批量付款")
			switch_to("xpath", '//*[@id="subTabSeven-iframe"]')
			
			#刷新、勾选按钮
			click("xpath",'//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath",'//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("删除")
			ok_click()
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("委托付款申请-直联批量付款，删除成功！")
			time.sleep(3)
			
			# 测试作废功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入直联批量付款窗体
			switch_to("xpath", '//*[@id="settleCenterApply-tab-iframe"]')
			span_click("直联批量付款")
			switch_to("xpath", '//*[@id="subTabSeven-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("作废")
			ok_click()
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'作废成功:1笔！失败:0笔！')]")
			print("委托付款申请-直联批量付款，作废成功！")
			time.sleep(3)
			
			#附件信息💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入直联批量付款窗体
			switch_to("xpath", '//*[@id="settleCenterApply-tab-iframe"]')
			span_click("直联批量付款")
			switch_to("xpath", '//*[@id="subTabSeven-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("附件信息")
			switch_to("xpath",'//*[@id="accessoryUploadWin-iframe"]')
			upload_click("xpath", "//div[text()='上传文件']/parent::*[1]/descendant::*[4]",
			             'D:\FlieDownload', '"WeiTuoFuKuanShenQingPLFK.xls"')
			sleep(1)
			span_click("保存")
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("委托付款申请-单笔转账处理，附件信息上传成功！")
			time.sleep(3)
			
			# 测试送审💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入直联批量付款窗体
			switch_to("xpath", '//*[@id="settleCenterApply-tab-iframe"]')
			span_click("直联批量付款")
			switch_to("xpath", '//*[@id="subTabSeven-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			span_click("送审")
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！送审成功1笔，失败0笔。')]")
			print("委托付款申请-直联批量付款，送审成功！")
			time.sleep(3)
			
			# 测试撤销送审💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入直联批量付款窗体
			switch_to("xpath", '//*[@id="settleCenterApply-tab-iframe"]')
			span_click("直联批量付款")
			switch_to("xpath", '//*[@id="subTabSeven-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			triangle_cick_and_element("送审","撤销送审")
			ok_click()
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'撤销送审成功:1笔!失败0笔！')]")
			print("委托付款申请-直联批量付款，撤销送审成功！")
			time.sleep(3)
			
			# 测试提交功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入直联批量付款窗体
			switch_to("xpath", '//*[@id="settleCenterApply-tab-iframe"]')
			span_click("直联批量付款")
			switch_to("xpath", '//*[@id="subTabSeven-iframe"]')
			
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
			
			#对第二笔数据进行送审
			# 刷新、勾选按钮
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
			time.sleep(3)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[2]/td[2]/div/button')
			sleep(1)
			
			span_click("提交")
			ok_click()
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("委托付款申请-直联批量付款，提交成功！")
			time.sleep(3)
			
			# 委托付款处理受理、打回、附件信息功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 去上级组织审批数据
			choose_organization("亚唐科技")
			
			# 将页面的滚动条滑动到‘资金结算管理’页面的地方
			js_gd("xpath", "//span[contains(text(),'资金结算管理')]")
			# 用JS的方法点击资金结算管理菜单按钮
			js_click("xpath", "//span[contains(text(),'资金结算管理')]")
			sleep(1)
			# 点击'外币收付结算'菜单
			click("xpath", "//span[text()='结算中心收付']")
			sleep(1)
			click("xpath", "//span[text()='委托付款受理']")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			
			#测试委托付款受理-直联批量付款-附件信息功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入委托付款受理窗体
			switch_to("xpath", '//*[@id="settleCenterDeal-tab-iframe"]')
			span_click("直联批量付款")
			switch_to("xpath", '//*[@id="subTabthree-iframe"]')
			sleep(1)
			
			#刷新、勾选按钮
			click("xpath",'//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath",'//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			span_click("附件信息")
			
			switch_to("xpath", '//*[@id="accessoryUploadWin-iframe"]')
			upload_click("xpath", "//div[text()='上传文件']/parent::*[1]/descendant::*[4]",
			             'D:\FlieDownload', '"WeiTuoFuKuanShenQingPLFK.xls"')
			sleep(1)
			span_click("保存")
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("委托付款申请-直联批量付款，附件信息上传成功！")
			time.sleep(3)
			
			# 测试委托付款受理-直联批量付款-受理功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入委托付款受理窗体
			switch_to("xpath", '//*[@id="settleCenterDeal-tab-iframe"]')
			span_click("直联批量付款")
			switch_to("xpath", '//*[@id="subTabthree-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("受理")
			switch_to("xpath",'//*[@id="modWin-iframe"]')
			span_click("保存")
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("委托付款申请-直联批量付款，受理成功！")
			time.sleep(3)
			
			# 测试委托付款受理-直联批量付款-打回功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入委托付款受理窗体
			switch_to("xpath", '//*[@id="settleCenterDeal-tab-iframe"]')
			span_click("直联批量付款")
			switch_to("xpath", '//*[@id="subTabthree-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("打回")
			ok_click()
			input("xpath",'//*[@id="refuseReason"]','测试打回')
			sleep(1)
			
			span_click("确定")

			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'打回操作成功:1笔!失败0笔！')]")
			print("委托付款申请-直联批量付款，打回成功！")
			time.sleep(3)
			
			#返回结算中心付款页面
			# 选择组织
			choose_organization("Mindy科技有限公司")
			
			# 将页面的滚动条滑动到‘资金结算管理’页面的地方
			js_gd("xpath", "//span[contains(text(),'资金结算管理')]")
			# 用JS的方法点击资金结算管理菜单按钮
			js_click("xpath", "//span[contains(text(),'资金结算管理')]")
			sleep(1)
			# 点击'外币收付结算'菜单
			click("xpath", "//span[text()='结算中心收付']")
			sleep(2)
			# 退出所有iframe窗体
			switch_default()
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("直联批量付款失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
			
			
			print("结束时间：", time.strftime("%Y-%m-%d %H:%M:%S"))
	
		
		# 测试结算中心收付-委托付款申请-承兑汇票支付🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱
		try:
			logger.info("测试委托付款申请->承兑汇票支付，以及委托付款处理->承兑汇票支付")
			click("xpath", "//span[text()='委托付款申请']")
			sleep(1)
			switch_default()
			
			# 测试新增功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			for i in range(1, 4):
				# 切入直联批量付款窗体
				switch_to("xpath", '//*[@id="settleCenterApply-tab-iframe"]')
				span_click("承兑汇票支付")
				switch_to("xpath", '//*[@id="subTabSix-iframe"]')
				
				span_click("新增")
				switch_to("xpath",'//*[@id="addWin-iframe"]')
				
				#受托组织
				click_up_click('//*[@id="combobox-input-entrustorgid"]')
				
				#交易类型
				input_up_click('//*[@id="combobox-input-paytypeid"]','103-对外付款')
				
				#结算方式
				click("xpath",'//*[@id="combobox-input-settlementmodeid"]')
				sleep(1)
				click("xpath",'//*[@id="settlementmodeid-combogrid-body-table"]/tbody/tr[3]/td[2]/div')
				sleep(1)
				
				#付方内部账户
				click_up_click('//*[@id="combobox-input-ourinternalaccountid"]')
				
				# 输入收方名称
				input("xpath", '//*[@id="combobox-input-oppcounterpartyid"]', "浙江华语科技")
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
				click_up_click('//*[@id="combobox-input-oppbanklocationid"]')
				
				# 金额
				money = random.randint(0, 1000)
				input("xpath", '//*[@id="oppamount-input"]', money)
				sleep(1)
				
				# 用途
				input("xpath", '//*[@id="combobox-input-purpose"]', '委托付款申请承兑汇票支付')
				sleep(1)
				
				span_click("保存")
				# 退出所有iframe窗体
				switch_default()
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				if i == 3:
					print("委托付款申请-承兑汇票支付，新增成功")
				time.sleep(3)
			
			
			# 测试修改功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入直联批量付款窗体
			switch_to("xpath", '//*[@id="settleCenterApply-tab-iframe"]')
			span_click("承兑汇票支付")
			switch_to("xpath", '//*[@id="subTabSix-iframe"]')
			
			#刷新、勾选按钮
			click("xpath",'//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath",'//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("修改")
			switch_to("xpath",'//*[@id="modWin-iframe"]')
			clear("xpath",'//*[@id="combobox-input-purpose"]')
			sleep(1)
			input("xpath",'//*[@id="combobox-input-purpose"]','修改')
			sleep(1)
			span_click("保存")
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("委托付款申请-承兑汇票支付，修改成功！")
			time.sleep(3)
			
			# 测试删除功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入直联批量付款窗体
			switch_to("xpath", '//*[@id="settleCenterApply-tab-iframe"]')
			span_click("承兑汇票支付")
			switch_to("xpath", '//*[@id="subTabSix-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("删除")
			ok_click()
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("委托付款申请-承兑汇票支付，删除成功！")
			time.sleep(3)
			
			# 测试复制功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入直联批量付款窗体
			switch_to("xpath", '//*[@id="settleCenterApply-tab-iframe"]')
			span_click("承兑汇票支付")
			switch_to("xpath", '//*[@id="subTabSix-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("复制")
			ok_click()
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("委托付款申请-承兑汇票支付，复制成功！")
			time.sleep(3)
			
			# 测试作废功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入直联批量付款窗体
			switch_to("xpath", '//*[@id="settleCenterApply-tab-iframe"]')
			span_click("承兑汇票支付")
			switch_to("xpath", '//*[@id="subTabSix-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("作废")
			ok_click()
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'作废成功:1笔！失败:0笔！')]")
			print("委托付款申请-承兑汇票支付，作废成功！")
			time.sleep(3)
			
			# 测试送审功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入直联批量付款窗体
			switch_to("xpath", '//*[@id="settleCenterApply-tab-iframe"]')
			span_click("承兑汇票支付")
			switch_to("xpath", '//*[@id="subTabSix-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("送审")
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("委托付款申请-承兑汇票支付，送审成功！")
			time.sleep(3)
			
			# 测试撤销送审功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入直联批量付款窗体
			switch_to("xpath", '//*[@id="settleCenterApply-tab-iframe"]')
			span_click("承兑汇票支付")
			switch_to("xpath", '//*[@id="subTabSix-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("送审",'撤销送审')
			ok_click()
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'撤销送审成功:1笔!失败0笔！')]")
			print("委托付款申请-承兑汇票支付，撤销送审成功！")
			time.sleep(3)
			
			# 测试变更功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			sql="update T_SE_PAYMENTAPPLYS set DEALSTATE = '4' where PURPOSE = '委托付款申请承兑汇票支付'"
			my_sql(my_host, my_port, my_user, my_passwd, my_db,
			        sql)
			# 切入直联批量付款窗体
			switch_to("xpath", '//*[@id="settleCenterApply-tab-iframe"]')
			span_click("承兑汇票支付")
			switch_to("xpath", '//*[@id="subTabSix-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("变更")
			switch_to("xpath",'//*[@id="modWin-iframe"]')
			clear("xpath",'//*[@id="combobox-input-oppcounterpartyaccountid"]')
			sleep(1)
			input("xpath",'//*[@id="combobox-input-oppcounterpartyaccountid"]','200848782767819')
			sleep(1)
			
			span_click("保存")
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("委托付款申请-承兑汇票支付，变更成功！")
			time.sleep(3)
			
			# 测试提交功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入直联批量付款窗体
			switch_to("xpath", '//*[@id="settleCenterApply-tab-iframe"]')
			span_click("承兑汇票支付")
			switch_to("xpath", '//*[@id="subTabSix-iframe"]')
			
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
			
			#对第二笔数据进行送审
			# 刷新、勾选按钮
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
			sleep(3)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[2]/td[2]/div/button')
			sleep(1)
			span_click("提交")
			ok_click()
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("委托付款申请-承兑汇票支付，提交成功！")
			time.sleep(3)
			
			# 委托付款处理-承兑汇票支付受理、打回功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 去上级组织审批数据
			choose_organization("亚唐科技")
			
			# 将页面的滚动条滑动到‘资金结算管理’页面的地方
			js_gd("xpath", "//span[contains(text(),'资金结算管理')]")
			# 用JS的方法点击资金结算管理菜单按钮
			js_click("xpath", "//span[contains(text(),'资金结算管理')]")
			sleep(1)
			# 点击'外币收付结算'菜单
			click("xpath", "//span[text()='结算中心收付']")
			sleep(1)
			click("xpath", "//span[text()='委托付款受理']")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			
			# 测试委托付款受理-直联批量付款-受理功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入委托付款受理窗体
			switch_to("xpath", '//*[@id="settleCenterDeal-tab-iframe"]')
			span_click("承兑汇票支付")
			switch_to("xpath", '//*[@id="subTabSix-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("受理")
			switch_to("xpath",'//*[@id="modWin-iframe"]')
			span_click("保存")
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("委托付款受理-承兑汇票支付，受理成功！")
			time.sleep(3)
			
			# 测试委托付款受理-直联批量付款-打回功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入委托付款受理窗体
			switch_to("xpath", '//*[@id="settleCenterDeal-tab-iframe"]')
			span_click("承兑汇票支付")
			switch_to("xpath", '//*[@id="subTabSix-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("打回")
			ok_click()
			input("xpath",'//*[@id="refuseReason"]','测试打回')
			sleep(1)
			span_click("确定")
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'打回操作成功:1笔!失败0笔！')]")
			print("委托付款受理-承兑汇票支付，打回成功！")
			time.sleep(3)
			
			# 返回结算中心付款页面
			# 选择组织
			choose_organization("Mindy科技有限公司")
			
			# 将页面的滚动条滑动到‘资金结算管理’页面的地方
			js_gd("xpath", "//span[contains(text(),'资金结算管理')]")
			# 用JS的方法点击资金结算管理菜单按钮
			js_click("xpath", "//span[contains(text(),'资金结算管理')]")
			sleep(1)
			# 点击'外币收付结算'菜单
			click("xpath", "//span[text()='结算中心收付']")
			sleep(2)
			# 退出所有iframe窗体
			switch_default()
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("承兑汇票支付失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
			
			print("结束时间：", time.strftime("%Y-%m-%d %H:%M:%S"))
		
		
		# 测试结算中心收付-委托付款申请-支票支付🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱
		try:
			logger.info("测试委托付款申请->支票支付，以及委托付款处理->支票支付")
			click("xpath", "//span[text()='委托付款申请']")
			sleep(1)
			switch_default()
			
			# 测试新增功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			for i in range(1, 4):
				# 切入直联批量付款窗体
				switch_to("xpath", '//*[@id="settleCenterApply-tab-iframe"]')
				span_click("支票支付")
				switch_to("xpath", '//*[@id="subTabFive-iframe"]')
				
				span_click("新增")
				switch_to("xpath", '//*[@id="addWin-iframe"]')
				
				# 受托组织
				click_up_click('//*[@id="combobox-input-entrustorgid"]')
				
				# 交易类型
				input_up_click('//*[@id="combobox-input-paytypeid"]', '103-对外付款')
				
				# 结算方式
				input_up_click('//*[@id="combobox-input-settlementmodeid"]','403-现金/转账支票支付')
				
				# 付方内部账户
				click_up_click('//*[@id="combobox-input-ourinternalaccountid"]')
				
				# 输入收方名称
				input("xpath", '//*[@id="combobox-input-oppcounterpartyid"]', "浙江华语科技")
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
				click_up_click('//*[@id="combobox-input-oppbanklocationid"]')
				
				# 金额
				money = random.randint(0, 1000)
				input("xpath", '//*[@id="oppamount-input"]', money)
				sleep(1)
				
				# 用途
				input("xpath", '//*[@id="combobox-input-purpose"]', '委托付款申请支票支付')
				sleep(1)
				
				span_click("保存")
				# 退出所有iframe窗体
				switch_default()
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				if i == 3:
					print("委托付款申请-支票支付，新增成功")
				time.sleep(3)
			
			# 测试修改功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入直联批量付款窗体
			switch_to("xpath", '//*[@id="settleCenterApply-tab-iframe"]')
			span_click("支票支付")
			switch_to("xpath", '//*[@id="subTabFive-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("修改")
			switch_to("xpath", '//*[@id="modWin-iframe"]')
			clear("xpath", '//*[@id="combobox-input-purpose"]')
			sleep(1)
			input("xpath", '//*[@id="combobox-input-purpose"]', '修改')
			sleep(1)
			span_click("保存")
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("委托付款申请-支票支付，修改成功！")
			time.sleep(3)
			
			# 测试删除功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入直联批量付款窗体
			switch_to("xpath", '//*[@id="settleCenterApply-tab-iframe"]')
			span_click("支票支付")
			switch_to("xpath", '//*[@id="subTabFive-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("删除")
			ok_click()
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("委托付款申请-支票支付，删除成功！")
			time.sleep(3)
			
			# 测试复制功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入直联批量付款窗体
			switch_to("xpath", '//*[@id="settleCenterApply-tab-iframe"]')
			span_click("支票支付")
			switch_to("xpath", '//*[@id="subTabFive-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("复制")
			ok_click()
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("委托付款申请-支票支付，复制成功！")
			time.sleep(3)
			
			# 测试作废功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入直联批量付款窗体
			switch_to("xpath", '//*[@id="settleCenterApply-tab-iframe"]')
			span_click("支票支付")
			switch_to("xpath", '//*[@id="subTabFive-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("作废")
			ok_click()
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'作废成功:1笔！失败:0笔！')]")
			print("委托付款申请-支票支付，作废成功！")
			time.sleep(3)
			
			# 测试送审功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入直联批量付款窗体
			switch_to("xpath", '//*[@id="settleCenterApply-tab-iframe"]')
			span_click("支票支付")
			switch_to("xpath", '//*[@id="subTabFive-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("送审")
			ok_click()
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("委托付款申请-支票支付，送审成功！")
			time.sleep(3)
			
			# 测试撤销送审功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入直联批量付款窗体
			switch_to("xpath", '//*[@id="settleCenterApply-tab-iframe"]')
			span_click("支票支付")
			switch_to("xpath", '//*[@id="subTabFive-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("送审", '撤销送审')
			ok_click()
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'撤销送审成功:1笔!失败0笔！')]")
			print("委托付款申请-支票支付，撤销送审成功！")
			time.sleep(3)
			
			# 测试变更功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			sql = "update T_SE_PAYMENTAPPLYS set DEALSTATE = '4' where PURPOSE = '委托付款申请支票支付'"
			my_sql(my_host, my_port, my_user, my_passwd, my_db,
			        sql)
			# 切入直联批量付款窗体
			switch_to("xpath", '//*[@id="settleCenterApply-tab-iframe"]')
			span_click("支票支付")
			switch_to("xpath", '//*[@id="subTabFive-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("变更")
			switch_to("xpath", '//*[@id="modWin-iframe"]')
			clear("xpath", '//*[@id="combobox-input-oppcounterpartyaccountid"]')
			sleep(1)
			input("xpath", '//*[@id="combobox-input-oppcounterpartyaccountid"]', '200848782767819')
			sleep(1)
			
			span_click("保存")
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("委托付款申请-支票支付，变更成功！")
			time.sleep(3)
			
			# 测试提交功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入直联批量付款窗体
			switch_to("xpath", '//*[@id="settleCenterApply-tab-iframe"]')
			span_click("支票支付")
			switch_to("xpath", '//*[@id="subTabFive-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("送审")
			ok_click()
			sleep(3)
			double_click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[3]/div')
			sleep(1)
			switch_to("xpath", '//*[@id="wf_taskProcessing_win-iframe"]')
			span_click("同意")
			switch_parent()
			sleep(3)
			
			# 对第二笔数据进行送审
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[2]/td[2]/div/button')
			sleep(1)
			
			span_click("送审")
			ok_click()
			sleep(3)
			double_click("xpath", '//*[@id="grid-body-table"]/tbody/tr[2]/td[3]/div')
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
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[2]/td[2]/div/button')
			sleep(1)
			span_click("提交")
			ok_click()
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("委托付款申请-支票支付，提交成功！")
			time.sleep(3)
			
			# 委托付款处理-承兑汇票支付受理、打回功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 去上级组织审批数据
			choose_organization("亚唐科技")
			
			# 将页面的滚动条滑动到‘资金结算管理’页面的地方
			js_gd("xpath", "//span[contains(text(),'资金结算管理')]")
			# 用JS的方法点击资金结算管理菜单按钮
			js_click("xpath", "//span[contains(text(),'资金结算管理')]")
			sleep(1)
			# 点击'外币收付结算'菜单
			click("xpath", "//span[text()='结算中心收付']")
			sleep(1)
			click("xpath", "//span[text()='委托付款受理']")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			
			# 测试委托付款受理-直联批量付款-受理功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入委托付款受理窗体
			switch_to("xpath", '//*[@id="settleCenterDeal-tab-iframe"]')
			span_click("支票支付")
			switch_to("xpath", '//*[@id="subTabFive-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("受理")
			switch_to("xpath", '//*[@id="modWin-iframe"]')
			click_up_click('//*[@id="combobox-input-ourbankaccountid"]')
			span_click("保存")
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("委托付款受理-支票支付，受理成功！")
			time.sleep(3)
			
			# 测试委托付款受理-直联批量付款-打回功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入委托付款受理窗体
			switch_to("xpath", '//*[@id="settleCenterDeal-tab-iframe"]')
			span_click("支票支付")
			switch_to("xpath", '//*[@id="subTabFive-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("打回")
			ok_click()
			input("xpath", '//*[@id="refuseReason"]', '测试打回')
			sleep(1)
			span_click("确定")
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'打回操作成功:1笔!失败0笔！')]")
			print("委托付款受理-支票支付，打回成功！")
			time.sleep(3)
			
			# 返回结算中心付款页面
			# 选择组织
			choose_organization("Mindy科技有限公司")
			
			# 将页面的滚动条滑动到‘资金结算管理’页面的地方
			js_gd("xpath", "//span[contains(text(),'资金结算管理')]")
			# 用JS的方法点击资金结算管理菜单按钮
			js_click("xpath", "//span[contains(text(),'资金结算管理')]")
			sleep(1)
			# 点击'外币收付结算'菜单
			click("xpath", "//span[text()='结算中心收付']")
			sleep(2)
			# 退出所有iframe窗体
			switch_default()
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("支票支付失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
			
			print("结束时间：", time.strftime("%Y-%m-%d %H:%M:%S"))
		
		
		# 测试结算中心收付-委托付款申请-现金支付🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱
		try:
			logger.info("测试委托付款申请->支票支付，以及委托付款处理->现金支付")
			click("xpath", "//span[text()='委托付款申请']")
			sleep(1)
			switch_default()
			
			# 测试新增功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			for i in range(1, 4):
				# 切入直联批量付款窗体
				switch_to("xpath", '//*[@id="settleCenterApply-tab-iframe"]')
				span_click("现金支付")
				switch_to("xpath", '//*[@id="subTabFour-iframe"]')
				
				span_click("新增")
				switch_to("xpath", '//*[@id="addWin-iframe"]')
				
				# 受托组织
				click_up_click('//*[@id="combobox-input-entrustorgid"]')
				
				# 交易类型
				input_up_click('//*[@id="combobox-input-paytypeid"]', '103-对外付款')
				
				# 结算方式
				input_up_click('//*[@id="combobox-input-settlementmodeid"]', '301-现金支付')
				
				# 付方内部账户
				click_up_click('//*[@id="combobox-input-ourinternalaccountid"]')
				
				# 输入收方名称
				input("xpath", '//*[@id="combobox-input-oppcounterpartyid"]', "浙江华语科技")
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
				click_up_click('//*[@id="combobox-input-oppbanklocationid"]')
				
				# 金额
				money = random.randint(0, 1000)
				input("xpath", '//*[@id="oppamount-input"]', money)
				sleep(1)
				
				# 用途
				input("xpath", '//*[@id="combobox-input-purpose"]', '委托付款申请现金支付')
				sleep(1)
				
				span_click("保存")
				# 退出所有iframe窗体
				switch_default()
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				if i == 3:
					print("委托付款申请-现金支付，新增成功")
				time.sleep(3)
			
			# 测试修改功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入直联批量付款窗体
			switch_to("xpath", '//*[@id="settleCenterApply-tab-iframe"]')
			span_click("现金支付")
			switch_to("xpath", '//*[@id="subTabFour-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("修改")
			switch_to("xpath", '//*[@id="modWin-iframe"]')
			clear("xpath", '//*[@id="combobox-input-purpose"]')
			sleep(1)
			input("xpath", '//*[@id="combobox-input-purpose"]', '修改')
			sleep(1)
			span_click("保存")
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("委托付款申请-现金支付，修改成功！")
			time.sleep(3)
			
			# 测试删除功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入直联批量付款窗体
			switch_to("xpath", '//*[@id="settleCenterApply-tab-iframe"]')
			span_click("现金支付")
			switch_to("xpath", '//*[@id="subTabFour-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("删除")
			ok_click()
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("委托付款申请-现金支付，删除成功！")
			time.sleep(3)
			
			# 测试复制功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入直联批量付款窗体
			switch_to("xpath", '//*[@id="settleCenterApply-tab-iframe"]')
			span_click("现金支付")
			switch_to("xpath", '//*[@id="subTabFour-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("复制")
			ok_click()
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("委托付款申请-现金支付，复制成功！")
			time.sleep(3)
			
			# 测试作废功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入直联批量付款窗体
			switch_to("xpath", '//*[@id="settleCenterApply-tab-iframe"]')
			span_click("现金支付")
			switch_to("xpath", '//*[@id="subTabFour-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("作废")
			ok_click()
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'作废成功:1笔！失败:0笔！')]")
			print("委托付款申请-现金支付，作废成功！")
			time.sleep(3)
			
			# 测试送审功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入直联批量付款窗体
			switch_to("xpath", '//*[@id="settleCenterApply-tab-iframe"]')
			span_click("现金支付")
			switch_to("xpath", '//*[@id="subTabFour-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("送审")
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("委托付款申请-现金支付，送审成功！")
			time.sleep(3)
			
			# 测试撤销送审功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入直联批量付款窗体
			switch_to("xpath", '//*[@id="settleCenterApply-tab-iframe"]')
			span_click("现金支付")
			switch_to("xpath", '//*[@id="subTabFour-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("送审", '撤销送审')
			ok_click()
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'撤销送审成功:1笔!失败0笔！')]")
			print("委托付款申请-现金支付，撤销送审成功！")
			time.sleep(3)
			
			# 测试变更功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			sql = "update T_SE_PAYMENTAPPLYS set DEALSTATE = '4' where PURPOSE = '委托付款申请现金支付'"
			my_sql(my_host, my_port, my_user, my_passwd, my_db,
			        sql)
			# 切入直联批量付款窗体
			switch_to("xpath", '//*[@id="settleCenterApply-tab-iframe"]')
			span_click("现金支付")
			switch_to("xpath", '//*[@id="subTabFour-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("变更")
			switch_to("xpath", '//*[@id="modWin-iframe"]')
			clear("xpath", '//*[@id="combobox-input-oppcounterpartyaccountid"]')
			sleep(1)
			input("xpath", '//*[@id="combobox-input-oppcounterpartyaccountid"]', '200848782767819')
			sleep(1)
			
			span_click("保存")
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("委托付款申请-现金支付，变更成功！")
			time.sleep(3)
			
			# 测试提交功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入直联批量付款窗体
			switch_to("xpath", '//*[@id="settleCenterApply-tab-iframe"]')
			span_click("现金支付")
			switch_to("xpath", '//*[@id="subTabFour-iframe"]')
			
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
			
			# 对第二笔数据进行送审
			# 刷新、勾选按钮
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
			sleep(3)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[2]/td[2]/div/button')
			sleep(1)
			span_click("提交")
			ok_click()
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("委托付款申请-现金支付，提交成功！")
			time.sleep(3)
			
			# 委托付款处理-承兑汇票支付受理、打回功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 去上级组织审批数据
			choose_organization("亚唐科技")
			
			# 将页面的滚动条滑动到‘资金结算管理’页面的地方
			js_gd("xpath", "//span[contains(text(),'资金结算管理')]")
			# 用JS的方法点击资金结算管理菜单按钮
			js_click("xpath", "//span[contains(text(),'资金结算管理')]")
			sleep(1)
			# 点击'外币收付结算'菜单
			click("xpath", "//span[text()='结算中心收付']")
			sleep(1)
			click("xpath", "//span[text()='委托付款受理']")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			
			# 测试委托付款受理-直联批量付款-受理功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入委托付款受理窗体
			switch_to("xpath", '//*[@id="settleCenterDeal-tab-iframe"]')
			span_click("现金支付")
			switch_to("xpath", '//*[@id="subTabFour-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("受理")
			switch_to("xpath", '//*[@id="modWin-iframe"]')
			click_up_click('//*[@id="combobox-input-ourbankaccountid"]')
			span_click("保存")
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("委托付款受理-现金支付，受理成功！")
			time.sleep(3)
			
			# 测试委托付款受理-现金支付-打回功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入委托付款受理窗体
			switch_to("xpath", '//*[@id="settleCenterDeal-tab-iframe"]')
			span_click("现金支付")
			switch_to("xpath", '//*[@id="subTabFour-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("打回")
			ok_click()
			input("xpath", '//*[@id="refuseReason"]', '测试打回')
			sleep(1)
			span_click("确定")
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'打回操作成功:1笔!失败0笔！')]")
			print("委托付款受理-现金支付，打回成功！")
			time.sleep(3)
			
			# 返回结算中心付款页面
			# 选择组织
			choose_organization("Mindy科技有限公司")
			
			# 将页面的滚动条滑动到‘资金结算管理’页面的地方
			js_gd("xpath", "//span[contains(text(),'资金结算管理')]")
			# 用JS的方法点击资金结算管理菜单按钮
			js_click("xpath", "//span[contains(text(),'资金结算管理')]")
			sleep(1)
			# 点击'外币收付结算'菜单
			click("xpath", "//span[text()='结算中心收付']")
			sleep(2)
			# 退出所有iframe窗体
			switch_default()
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("现金支付失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
			
			print("结束时间：", time.strftime("%Y-%m-%d %H:%M:%S"))
		
		
		# 测试结算中心收付-委托付款申请-其他支付🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱
		try:
			logger.info("测试委托付款申请->支票支付，以及委托付款处理->现金支付")
			click("xpath", "//span[text()='委托付款申请']")
			sleep(1)
			switch_default()
			
			# 测试新增功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			for i in range(1, 4):
				# 切入直联批量付款窗体
				switch_to("xpath", '//*[@id="settleCenterApply-tab-iframe"]')
				span_click("其他支付")
				switch_to("xpath", '//*[@id="subTabEight-iframe"]')
				
				span_click("新增")
				switch_to("xpath", '//*[@id="addWin-iframe"]')
				
				# 受托组织
				click_up_click('//*[@id="combobox-input-entrustorgid"]')
				
				# 交易类型
				input_up_click('//*[@id="combobox-input-paytypeid"]', '103-对外付款')
				
				# 结算方式
				input_up_click('//*[@id="combobox-input-settlementmodeid"]', '601-其他支付')
				
				# 付方内部账户
				click_up_click('//*[@id="combobox-input-ourinternalaccountid"]')
				
				# 输入收方名称
				input("xpath", '//*[@id="combobox-input-oppcounterpartyid"]', "浙江华语科技")
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
				click_up_click('//*[@id="combobox-input-oppbanklocationid"]')
				
				# 金额
				money = random.randint(0, 1000)
				input("xpath", '//*[@id="oppamount-input"]', money)
				sleep(1)
				
				# 用途
				input("xpath", '//*[@id="combobox-input-purpose"]', '委托付款申请其他支付')
				sleep(1)
				
				span_click("保存")
				# 退出所有iframe窗体
				switch_default()
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				if i == 3:
					print("委托付款申请-其他支付，新增成功")
				time.sleep(3)
			
			# 测试修改功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入直联批量付款窗体
			switch_to("xpath", '//*[@id="settleCenterApply-tab-iframe"]')
			span_click("其他支付")
			switch_to("xpath", '//*[@id="subTabEight-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("修改")
			switch_to("xpath", '//*[@id="modWin-iframe"]')
			clear("xpath", '//*[@id="combobox-input-purpose"]')
			sleep(1)
			input("xpath", '//*[@id="combobox-input-purpose"]', '修改')
			sleep(1)
			span_click("保存")
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("委托付款申请-其他支付，修改成功！")
			time.sleep(3)
			
			# 测试删除功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入直联批量付款窗体
			switch_to("xpath", '//*[@id="settleCenterApply-tab-iframe"]')
			span_click("其他支付")
			switch_to("xpath", '//*[@id="subTabEight-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("删除")
			ok_click()
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("委托付款申请-其他支付，删除成功！")
			time.sleep(3)
			
			# 测试复制功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入直联批量付款窗体
			switch_to("xpath", '//*[@id="settleCenterApply-tab-iframe"]')
			span_click("其他支付")
			switch_to("xpath", '//*[@id="subTabEight-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("复制")
			ok_click()
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("委托付款申请-其他支付，复制成功！")
			time.sleep(3)
			
			# 测试作废功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入直联批量付款窗体
			switch_to("xpath", '//*[@id="settleCenterApply-tab-iframe"]')
			span_click("其他支付")
			switch_to("xpath", '//*[@id="subTabEight-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("作废")
			ok_click()
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'作废成功:1笔！失败:0笔！')]")
			print("委托付款申请-其他支付，作废成功！")
			time.sleep(3)
			
			# 测试送审功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入直联批量付款窗体
			switch_to("xpath", '//*[@id="settleCenterApply-tab-iframe"]')
			span_click("其他支付")
			switch_to("xpath", '//*[@id="subTabEight-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("送审")
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("委托付款申请-其他支付，送审成功！")
			time.sleep(3)
			
			# 测试撤销送审功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入直联批量付款窗体
			switch_to("xpath", '//*[@id="settleCenterApply-tab-iframe"]')
			span_click("其他支付")
			switch_to("xpath", '//*[@id="subTabEight-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("送审", '撤销送审')
			ok_click()
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'撤销送审成功:1笔!失败0笔！')]")
			print("委托付款申请-其他支付，撤销送审成功！")
			time.sleep(3)
			
			# 测试变更功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			sql = "update T_SE_PAYMENTAPPLYS set DEALSTATE = '4' where PURPOSE = '委托付款申请其他支付'"
			my_sql(my_host, my_port, my_user, my_passwd, my_db,
			        sql)
			# 切入直联批量付款窗体
			switch_to("xpath", '//*[@id="settleCenterApply-tab-iframe"]')
			span_click("现金支付")
			switch_to("xpath", '//*[@id="subTabFour-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("变更")
			switch_to("xpath", '//*[@id="modWin-iframe"]')
			clear("xpath", '//*[@id="combobox-input-oppcounterpartyaccountid"]')
			sleep(1)
			input("xpath", '//*[@id="combobox-input-oppcounterpartyaccountid"]', '200848782767819')
			sleep(1)
			
			span_click("保存")
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("委托付款申请-其他支付，变更成功！")
			time.sleep(3)
			
			# 测试提交功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入直联批量付款窗体
			switch_to("xpath", '//*[@id="settleCenterApply-tab-iframe"]')
			span_click("其他支付")
			switch_to("xpath", '//*[@id="subTabEight-iframe"]')
			
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
			
			# 对第二笔数据进行送审
			# 刷新、勾选按钮
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
			sleep(3)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[2]/td[2]/div/button')
			sleep(1)
			span_click("提交")
			ok_click()
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("委托付款申请-其他支付，提交成功！")
			time.sleep(3)
			
			# 委托付款处理-承兑汇票支付受理、打回功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 去上级组织审批数据
			choose_organization("亚唐科技")
			
			# 将页面的滚动条滑动到‘资金结算管理’页面的地方
			js_gd("xpath", "//span[contains(text(),'资金结算管理')]")
			# 用JS的方法点击资金结算管理菜单按钮
			js_click("xpath", "//span[contains(text(),'资金结算管理')]")
			sleep(1)
			# 点击'外币收付结算'菜单
			click("xpath", "//span[text()='结算中心收付']")
			sleep(1)
			click("xpath", "//span[text()='委托付款受理']")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			
			# 测试委托付款受理-直联批量付款-受理功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入委托付款受理窗体
			switch_to("xpath", '//*[@id="settleCenterDeal-tab-iframe"]')
			span_click("其他支付")
			switch_to("xpath", '//*[@id="subTabSeven-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("受理")
			switch_to("xpath", '//*[@id="modWin-iframe"]')
			click_up_click('//*[@id="combobox-input-ourbankaccountid"]')
			span_click("保存")
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("委托付款受理-现金支付，受理成功！")
			time.sleep(3)
			
			# 测试委托付款受理-现金支付-打回功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入委托付款受理窗体
			switch_to("xpath", '//*[@id="settleCenterDeal-tab-iframe"]')
			span_click("其他支付")
			switch_to("xpath", '//*[@id="subTabSeven-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("打回")
			ok_click()
			input("xpath", '//*[@id="refuseReason"]', '测试打回')
			sleep(1)
			span_click("确定")
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'打回操作成功:1笔!失败0笔！')]")
			print("委托付款受理-现金支付，打回成功！")
			time.sleep(3)
			
			# 返回结算中心付款页面
			# 选择组织
			choose_organization("Mindy科技有限公司")
			
			# 将页面的滚动条滑动到‘资金结算管理’页面的地方
			js_gd("xpath", "//span[contains(text(),'资金结算管理')]")
			# 用JS的方法点击资金结算管理菜单按钮
			js_click("xpath", "//span[contains(text(),'资金结算管理')]")
			sleep(1)
			# 点击'外币收付结算'菜单
			click("xpath", "//span[text()='结算中心收付']")
			sleep(2)
			# 退出所有iframe窗体
			switch_default()
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("现金支付失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
			
			print("结束时间：", time.strftime("%Y-%m-%d %H:%M:%S"))
		
		# 测试结算中心收付-快捷付款申请🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱
		try:
			logger.info("测试委托付款申请->快捷付款申请")
			click("xpath", "//span[text()='快捷付款申请']")
			sleep(1)
			switch_default()
			
			# 去委托付款申请页面做数据💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			click("xpath", "//span[text()='委托付款申请']")
			sleep(1)
			switch_default()
			
			for i in range(1, 4):
				# 切入单笔转账处理窗体
				switch_to("xpath", '//*[@id="settleCenterApply-tab-iframe"]')
				switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
				sleep(1)
				span_click("新增")
				# 切入新增窗体
				switch_to("xpath", '//*[@id="addWin-iframe"]')
				# 受托组织
				click_up_click('//*[@id="combobox-input-entrustorgid"]')
				
				# 付方内部账户
				click_up_click('//*[@id="combobox-input-ourinternalaccountid"]')
				
				# 交易类型
				input_up_click('//*[@id="combobox-input-paytypeid"]', '103-对外付款')
				
				# 结算方式
				input_up_click('//*[@id="combobox-input-settlementmodeid"]', '101-直联单笔转账')
				
				# 付方账户
				click_up_click('//*[@id="combobox-input-ourbankaccountid"]')
				
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
				click_up_click('//*[@id="combobox-input-oppbanklocationid"]')
				
				# 金额
				money = random.randint(0, 1000)
				input("xpath", '//*[@id="oppamount-input"]', money)
				sleep(1)
				
				# 用途
				input("xpath", '//*[@id="combobox-input-purpose"]', '结算中心收付快捷付款申请')
				sleep(1)
				
				span_click("保存")
				switch_default()
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				if i == 2 :
					print("委托付款申请数据成功")
				time.sleep(3)
				
			#回到快捷付款申请界面
			click("xpath", "//span[text()='快捷付款申请']")
			sleep(1)
			switch_default()
			
			#测试修改功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			sql = "update T_SE_PAYMENTAPPLYS set RECORDSOURCE='4' where PURPOSE = '结算中心收付快捷付款申请'"
			my_sql(my_host, my_port, my_user, my_passwd, my_db,
			        sql)
			#切入快捷付款申请界面
			switch_to("xpath",'//*[@id="settleCenterQuickApply-tab-iframe"]')
			#刷新、勾选按钮
			click("xpath",'//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath",'//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("修改")
			switch_to("xpath",'//*[@id="modWin-iframe"]')
			span_click("保存")
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("结算中心收付-快捷付款申请，修改成功！")
			time.sleep(3)
			
			# 测试送审功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入快捷付款申请界面
			switch_to("xpath", '//*[@id="settleCenterQuickApply-tab-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("送审")
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！送审成功1笔，失败0笔。')]")
			print("结算中心收付-快捷付款申请，送审成功！")
			time.sleep(3)
			
			# 测试撤销送审功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入快捷付款申请界面
			switch_to("xpath", '//*[@id="settleCenterQuickApply-tab-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("送审","撤销送审")
			ok_click()
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'撤销送审成功:1笔!失败0笔！')]")
			print("结算中心收付-快捷付款申请，撤销送审成功！")
			time.sleep(3)
			
			# 测试作废功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入快捷付款申请界面
			switch_to("xpath", '//*[@id="settleCenterQuickApply-tab-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("作废")
			ok_click()
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'共1笔，作废成功1笔，失败0笔！')]")
			print("结算中心收付-快捷付款申请，作废成功！")
			time.sleep(3)
			
			# 测试审核功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入快捷付款申请界面
			switch_to("xpath", '//*[@id="settleCenterQuickApply-tab-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("审核")
			ok_click()
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'成功审核1条记录')]")
			print("结算中心收付-快捷付款申请，审核成功！")
			time.sleep(3)
			
			# 测试撤销审核功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入快捷付款申请界面
			switch_to("xpath", '//*[@id="settleCenterQuickApply-tab-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("审核","取消审核")
			ok_click()
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'取消审核成功！')]")
			print("结算中心收付-快捷付款申请，取消审核成功！")
			time.sleep(3)
			
			# 测试提交功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入快捷付款申请界面
			switch_to("xpath", '//*[@id="settleCenterQuickApply-tab-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[2]/td[2]/div/button')
			sleep(1)
			span_click("审核")
			ok_click()
			sleep(3)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[2]/td[2]/div/button')
			sleep(1)
			
			span_click("提交")
			ok_click()
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("结算中心收付-快捷付款申请，提交成功！")
			time.sleep(3)
			
			# 快捷付款申请受理、打回功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 去上级组织审批数据
			choose_organization("亚唐科技")
			
			# 将页面的滚动条滑动到‘资金结算管理’页面的地方
			js_gd("xpath", "//span[contains(text(),'资金结算管理')]")
			# 用JS的方法点击资金结算管理菜单按钮
			js_click("xpath", "//span[contains(text(),'资金结算管理')]")
			sleep(1)
			# 点击'外币收付结算'菜单
			click("xpath", "//span[text()='结算中心收付']")
			sleep(1)
			click("xpath", "//span[text()='快捷付款申请处理']")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			
			# 测试快捷付款申请处理-受理功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入快捷付款申请处理窗体
			switch_to("xpath", '//*[@id="settleCenterQuickApplyHandle-tab-iframe"]')
			#刷新、勾选按钮
			click("xpath",'//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath",'//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("受理")
			switch_to("xpath",'//*[@id="modWin-iframe"]')
			span_click("保存")
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("结算中心收付-快捷付款处理，受理成功！")
			time.sleep(3)
			
			# 测试快捷付款申请处理-打回功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入快捷付款申请处理窗体
			switch_to("xpath", '//*[@id="settleCenterQuickApplyHandle-tab-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("打回")
			ok_click()
			input("xpath",'//*[@id="refuseReason"]','测试打回')
			sleep(1)
			span_click("确定")
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'打回操作成功:1笔!失败0笔！')]")
			print("结算中心收付-快捷付款处理，打回成功！")
			time.sleep(3)
			
			
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("快捷付款处理失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
			
			print("结束时间：", time.strftime("%Y-%m-%d %H:%M:%S"))
		
		
		
		
		
if __name__ == '__main__':
	#  启动单元测试
	unittest.main(verbosity=2)
