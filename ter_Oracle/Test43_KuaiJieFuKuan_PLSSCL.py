# encoding=utf-8
# @Time : 2020/11/12 08:30
# @Author : zzg
# 此文件是测试MySQL版本资金结算管理--业务系统对接--快捷付款--付款申请
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
class Test43_KuaiJieFuKuan_PLSSCL(unittest.TestCase):
	
	# 启动浏览器
	def setUp(self):
		# 启动浏览器的另外一个方法：通过封装启动浏览器的驱动，启动不同浏览器
		self.driver = get("chrome")
	
	# 登陆系统、对系统设置进行操作
	def test_trade(self):
		
		# login(G_Ora_Url, mindy, Password, "亚唐科技")
		login(G_Ora_Url, mindy, Password, "亚唐科技")
		
		logging.info("开始测试资金结算管理--业务系统对接--快捷付款--付款申请")
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
			
			#去直联单笔页面做数据💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			click("xpath", "//span[text()='业务系统对接']")
			sleep(1)
			click("xpath", "//span[text()='资金系统收付']")
			sleep(1)
			click("xpath", "//span[text()='付款处理']")
			sleep(1)
			for i in range(1, 2):
				# 切入窗体
				switch_to("xpath", '//*[@id="generalPayment-tab-iframe"]')
				switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
				sleep(1)
				# 切入新增窗体
				click("xpath", '//*[@id="button1"]/span/span')
				sleep(1)
				switch_to('xpath', '//*[@id="addWin-iframe"]')
				
				# 交易类型
				input("xpath", '//*[@id="combobox-input-paytypeid"]', "103-对外付款")
				sleep(1)
				click("xpath", '//*[@id="paytypeid-combogrid-body-table"]/tbody/tr/td[2]/div')
				sleep(1)
				
				# 点击付方账户
				input("xpath", '//*[@id="combobox-input-ourbankaccountid"]', "20211012")
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
				input("xpath", "//input[@id='combobox-input-purpose']", "快捷付款批量送审处理")
				sleep(1)
				# 双击清楚下拉框
				double_click("xpath", "//span[text()='卡折类型']")
				sleep(1)
				
				# 保存
				click("xpath", '//*[@id="save"]/span/span')
				sleep(1)
				switch_default()
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				time.sleep(3)
				
			sql = "update t_se_payments set FINVOUCHERCODE = '2020' where purpose = '快捷付款批量送审处理'"
			my_sql(my_host, my_port, my_user, my_passwd, my_db,
				    sql)
			sql = "update t_se_payments set RECORDSOURCE = '4' where purpose = '快捷付款批量送审处理'"
			my_sql(my_host, my_port, my_user, my_passwd, my_db,
				    sql)
				
			#回到快捷付款批量送审处理页面
			click("xpath", "//span[text()='资金系统收付']")
			sleep(1)
			click("xpath", "//span[text()='业务系统对接']")
			sleep(1)
			click("xpath", "//span[text()='快捷付款']")
			sleep(1)
			switch_default()
			
			# 测试余额检测功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath",'//*[@id="subTabTen-iframe"]')
			switch_to("xpath",'//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			#刷新、勾选按钮
			click("xpath",'//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath",'//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("余额检测")
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'余额充足')]")
			print("快捷付款--批量送审处理，余额检测成功！")
			time.sleep(3)
			
			# 测试组批送审功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="subTabTen-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			#查询数据
			click("xpath",'//*[@id="north"]/div[2]/span')
			sleep(1)
			input("xpath",'//*[@id="combobox-input-ourbankaccountid"]','20211012')
			sleep(1)
			click("xpath", '//*[@id="ourbankaccountid-combogrid-body-table"]/tbody/tr/td[2]/div/button')
			sleep(1)
			span_click("查询")
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			
			span_click("组批送审")
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'余额充足')]")
			print("快捷付款--批量送审处理，余额检测成功！")
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
