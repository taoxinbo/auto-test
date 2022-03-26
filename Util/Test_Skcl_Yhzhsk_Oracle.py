# encoding=utf-8
# @Time : 2020/8/17 9:32
# @Author : Mindy
# 此文件是测试Oracle版本资金结算管理--资金系统收付--收款处理--银行账户收款
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

# print("开始时间：",time.strftime("%Y-%m-%d %H:%M:%S"))

driver = ""


class Test_Skcl_Yhzhsk_Oracle(unittest.TestCase):
	
	# 启动浏览器
	def setUp(self):
		# 启动浏览器的另外一个方法：通过封装启动浏览器的驱动，启动不同浏览器
		self.driver = get("chrome")
	
	# 登陆系统、对系统设置进行操作
	def test_trade(self):
		# 通过登陆封装函数，进行登陆
		# login( G_Ora_Url,TestUser,Password, "自动化测试租户")
		# login( G_Ora_Url,Tao, Password,"默认租户")
		login(G_Ora_Url, mindy, Password, "亚唐科技")
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
		
		# 开始测试资金系统收付--收款处理--银行账户收款
		# 测试收款处理--银行账户收款
		try:
			# 点击'资金系统收付'菜单
			click("xpath", "//span[text()='资金系统收付']")
			# 点击收款处理菜单
			click("xpath", "//span[text()='收款处理']")
			# 退出所有iframe窗体
			switch_default()
			
			for i in range(1, 3):
				# 切入‘银行账户收款’的iframe窗体
				switch_to("xpath", "//iframe[@id='generalRecment-tab-iframe']")
				sleep(1)
				
				# 进入银行账户收款的iframe窗体
				switch_to("xpath", "//iframe[@id='subTabEight-iframe']")
				sleep(1)
				
				# 点击新增
				click("xpath", "//span[text()='新增']")
				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='addWin-iframe']")
				sleep(1)
				
				# 部门
				click("xpath", "//input[@id='combobox-input-deptid']")
				input("xpath", "//input[@id='combobox-input-deptid']", "自动化测试部")
				input_down("xpath", "//input[@id='combobox-input-deptid']")
				input_enter("xpath", "//input[@id='combobox-input-deptid']")
				time.sleep(1)
				
				# 交易类型
				click("xpath", "//input[@id='combobox-input-paytypeid']")
				# 输入开户行大连泡崖街支行名称，模糊查询
				input("xpath", "//input[@id='combobox-input-paytypeid']", "外部收款")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-paytypeid']")
				input_enter("xpath", "//input[@id='combobox-input-paytypeid']")
				time.sleep(1)
				
				# 选择结算方式
				click("xpath", "//input[@id='combobox-input-settlementmodeid']")
				clear("xpath", "//input[@id='combobox-input-settlementmodeid']")
				sleep(1)
				# 输入开户行大连泡崖街支行名称，模糊查询
				input("xpath", "//input[@id='combobox-input-settlementmodeid']", "单笔转账收款")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-settlementmodeid']")
				input_enter("xpath", "//input[@id='combobox-input-settlementmodeid']")
				time.sleep(1)
				
				# 收方账户
				click("xpath", "//input[@id='combobox-input-ourbankaccountid']")
				sleep(1)
				input("xpath", "//input[@id='combobox-input-ourbankaccountid']", "中国银行")
				sleep(1)
				input_enter("xpath", "//input[@id='combobox-input-ourbankaccountid']")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-ourbankaccountid']")
				sleep(1)
				input_enter("xpath", "//input[@id='combobox-input-ourbankaccountid']")
				sleep(1)
				
				# 付方名称
				input("xpath", "//input[@id='combobox-input-oppcounterpartyid']", "Mindy科技有限公司")
				sleep(1)
			
				# 双击清楚下拉框
				double_click("xpath", "//span[text()='卡折类型']")
				sleep(1)
				
				# 收方账户
				input("xpath", "//input[@id='combobox-input-oppcounterpartyaccountid']", "12341234")
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
				input("xpath", "//input[@id='ouramount-input']", "30000")
				sleep(1)
				
				# 用途
				input("xpath", "//input[@id='combobox-input-purpose']", "自动化测试")
				sleep(1)
				
				# 点击保存按钮
				click("xpath", "//span[text()='保存']")
				
				# 退出所有iframe窗体
				switch_default()
				
				# 用隐式等待方法等页面出现新增成功的提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				print("银行账户收款，第%s次保存成功！" % i)
				time.sleep(3)
				
				# 修改、删除
				if i == 1:
					# 切入‘银行账户收款’的iframe窗体
					switch_to("xpath", "//iframe[@id='generalRecment-tab-iframe']")
					sleep(1)
				
					# 进入银行账户收款的iframe窗体
					switch_to("xpath", "//iframe[@id='subTabEight-iframe']")
					sleep(1)
					
					# 点击查看
					# 用JS的方法点击放大镜
					js_click("xpath", "//span[@class='f-contrac-close']")
					sleep(1)
					
					# 输入收款户名：Mindy科技有限公司
					click("xpath", "//input[@id='oppbankaccountname']")
					sleep(1)
					input("xpath", "//input[@id='oppbankaccountname']", "Mindy科技有限公司")
					sleep(1)
					
					# 点击查询
					click("xpath", "//span[text()='查询']")
					
					# 修改勾选数据
					click("xpath",
					      "//div[@title='付款户名:Mindy科技有限公司']/parent::*/preceding-sibling::*[8]/descendant::*[2]")
					
					# 点击修改按钮
					click("xpath", "//span[text()='修改']")
					
					# 切入修改的iframe窗体
					switch_to("xpath", "//iframe[@id='modWin-iframe']")
					sleep(2)
					
					# 点击保存按钮
					click("xpath", "//span[text()='保存']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("收款处理-银行账户收款，修改成功！")
					logging.info("收款处理-银行账户收款，修改成功！")
					time.sleep(3)
					
					# 删除
					switch_to("xpath", "//iframe[@id='generalRecment-tab-iframe']")
					sleep(1)
					
					# 进入银行账户收款的iframe窗体
					switch_to("xpath", "//iframe[@id='subTabEight-iframe']")
					sleep(1)
					
					# 勾选数据
					click("xpath", "//div[@title='付款户名:Mindy科技有限公司']/parent::*/preceding-sibling::*[8]/descendant::*[2]")
					
					# 点击删除按钮
					click("xpath", "//span[text()='删除']")
					
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					sleep(1)
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现删除的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("收款处理-银行账户收款，删除成功！")
					logging.info("收款处理-银行账户收款，删除成功！")
					time.sleep(3)
				
				# 第二笔，收款、打印
				if i == 2:
					# 确认收款
					# 切入‘银行账户收款’的iframe窗体
					switch_to("xpath", "//iframe[@id='generalRecment-tab-iframe']")
					sleep(1)
					
					# 进入银行账户收款的iframe窗体
					switch_to("xpath", "//iframe[@id='subTabEight-iframe']")
					sleep(1)
					
					# 勾选数据
					click("xpath", "//div[@title='付款户名:Mindy科技有限公司']/parent::*/preceding-sibling::*[8]/descendant::*[2]")
					sleep(1)
					
					# 点击确认收款按钮
					click("xpath", "//span[text()='确认收款']")
					sleep(1)
					
					# 点击确定
					click("xpath", "//span[text()='确定']")
					sleep(1)
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("银行账户收款，收款成功！")
					logging.info("银行账户收款，收款成功！")
					time.sleep(3)
				
					# 打印
					switch_to("xpath", "//iframe[@id='generalRecment-tab-iframe']")
					sleep(1)
				
					# 进入银行账户收款的iframe窗体
					switch_to("xpath", "//iframe[@id='subTabEight-iframe']")
					sleep(1)
					
					# 勾选数据
					click("xpath", "//div[@title='付款户名:Mindy科技有限公司']/parent::*/preceding-sibling::*[8]/descendant::*[2]")
					sleep(1)
					
					# 点击打印按钮
					click("xpath", "//span[text()='打印']")
					sleep(1)
					
					# 获取所有窗口句柄
					all_handles = self.driver.window_handles
					# 循环遍历所有新打开的窗口句柄，也就是说不包括主窗口
					now_handle = self.driver.current_window_handle
					for handle in all_handles:
						self.driver.switch_to.window(handle)
						if self.driver.title == u"payandrecsingleprint":
							implici_wait("xpath", "//td[contains(text(),'Mindy科技有限公司')]")
							print("银行账户收款，打印成功!！")
							time.sleep(3)
							self.driver.switch_to.window(now_handle)
							switch_default()
					
					# 打印记录
					# 切入‘银行账户收款’的iframe窗体
					switch_to("xpath", "//iframe[@id='generalRecment-tab-iframe']")
					sleep(1)
					
					# 点击银行账户收款
					click("xpath", "//span[text()='银行账户收款']")
					
					# 进入银行账户收款的iframe窗体
					switch_to("xpath", "//iframe[@id='subTabEight-iframe']")
					sleep(1)
					
					# # 勾选数据
					# click("xpath", "//div[@title='付款户名:Mindy科技有限公司']/parent::*/preceding-sibling::*[8]/descendant::*[2]")
					# sleep(1)
					
					# 用JS方便点击‘收款’按钮旁边的倒三角形
					js_click("xpath", "//span[text()='打印']/parent::*/following-sibling::*/child::*")
					sleep(1)
					
					# 点击打印记录按钮
					js_click("xpath", "//a[contains(text(),'打印记录')]")
					sleep(1)
					
					switch_to("xpath", "//iframe[@id='printWin-iframe']")
					sleep(1)
					
					# 用隐式等待方法等页面出现  操作人:mindy
					implici_wait("xpath", "//div[@title='操作人:mindy']")
					print("银行账户收款，打印记录查看成功！")
					logging.info("银行账户收款，打印记录查看成功！")
					time.sleep(3)
					
					switch_parent()
					
					# 点击关闭页面
					click("xpath", "//span[text()='打印']/preceding-sibling::*[1]")
					sleep(1)
					
					switch_default()
					
					# 作废
					switch_to("xpath", "//iframe[@id='generalRecment-tab-iframe']")
					sleep(1)
					
					# 进入银行账户收款的iframe窗体
					switch_to("xpath", "//iframe[@id='subTabEight-iframe']")
					sleep(1)
					
					# # 勾选数据
					# click("xpath",
					#       "//div[@title='付款户名:Mindy科技有限公司']/parent::*/preceding-sibling::*[8]/descendant::*[2]")
					#
					# 点击作废按钮
					click("xpath", "//span[text()='作废']")
					
					# 点击OK提示框
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					sleep(1)
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现删除的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("收款处理-银行账户收款，作废成功！")
					logging.info("收款处理-银行账户收款，作废成功！")
					time.sleep(3)
				
			switch_default()
			
			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='收款处理']/child::*[1]")
			
			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//span[text()='资金系统收付']")
			# 打印操作成功日志
			print("银行账户收款，操作成功!")
			logging.info("银行账户收款，操作成功!")
			time.sleep(2)
	
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("银行账户收款失败！" + str(traceback.format_exc()))
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