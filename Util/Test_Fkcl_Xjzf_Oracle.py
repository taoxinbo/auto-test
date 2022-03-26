# encoding=utf-8
# @Time : 2020/8/14 14:49
# @Author : Mindy
# 此文件是测试Oracle版本资金结算管理--资金系统收付--付款处理--现金支付
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


class Test_Fkcl_Xjzf_Oracle(unittest.TestCase):
	
	# 启动浏览器
	def setUp(self):
		# 启动浏览器的另外一个方法：通过封装启动浏览器的驱动，启动不同浏览器
		self.driver = get("chrome")
	
	# 登陆系统、对系统设置进行操作
	def test_trade(self):
		# 通过登陆封装函数，进行登陆
		# login( G_Ora_Url,TestUser,Password, "自动化测试租户")
		# login( G_Ora_Url,Tao, Password,"默认租户")
		# login(G_Ora_Url, mindy, Password, "亚唐科技")
		login(G_Ora_Url, mindy, Password, "默认租户")
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
		
		# 开始测试资金系统收付--付款处理--现金支付
		# 测试付款处理--现金支付
		try:
			# 点击'资金系统收付'菜单
			click("xpath", "//span[text()='资金系统收付']")
			# 点击付款处理菜单
			click("xpath", "//span[text()='付款处理']")
			# 退出所有iframe窗体
			switch_default()
			
			for i in range(1, 3):
				# 切入‘付款处理’的iframe窗体
				switch_to("xpath", "//iframe[@id='generalPayment-tab-iframe']")
				
				# 点击现金支付
				click("xpath", "//span[text()='现金支付']")
				
				# 切入‘现金支付’的iframe窗体
				switch_to("xpath", "//iframe[@id='subTabFour-iframe']")
				sleep(1)
				
				# 用JS的方法点击新增按钮
				js_click("xpath", "//span[text()='新增']")
				
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
				input("xpath", "//input[@id='combobox-input-paytypeid']", "对外付款")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-paytypeid']")
				input_enter("xpath", "//input[@id='combobox-input-paytypeid']")
				time.sleep(1)
				
				# 选择结算方式
				click("xpath", "//input[@id='combobox-input-settlementmodeid']")
				clear("xpath", "//input[@id='combobox-input-settlementmodeid']")
				sleep(1)
				# 输入开户行大连泡崖街支行名称，模糊查询
				input("xpath", "//input[@id='combobox-input-settlementmodeid']", "现金支付")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-settlementmodeid']")
				input_enter("xpath", "//input[@id='combobox-input-settlementmodeid']")
				time.sleep(1)
				
				# 付方账户
				click("xpath", "//input[@id='combobox-input-ourbankaccountid']")
				# 输入开户行大连泡崖街支行名称，模糊查询
				input_enter("xpath", "//input[@id='combobox-input-ourbankaccountid']")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-ourbankaccountid']")
				input_enter("xpath", "//input[@id='combobox-input-ourbankaccountid']")
				time.sleep(1)
				
				# 收款户名
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
				print("现金支付，第%s次保存成功！" % i)
				time.sleep(3)
				
				# 第一笔，就先修改，再修改页面提交送审，再撤销送审，再删除
				if i == 1:
					# 切入‘现金支付’的iframe窗体
					switch_to("xpath", "//iframe[@id='generalPayment-tab-iframe']")
					sleep(1)
					
					# 点击现金支付
					click("xpath", "//span[text()='现金支付']")
					
					# 切入‘现金支付’的iframe窗体
					switch_to("xpath", "//iframe[@id='subTabFour-iframe']")
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
					click("xpath", "//div[@title='收款户名:Mindy科技有限公司']/parent::*/preceding-sibling::*[6]/descendant::*[2]")
					
					# 点击修改按钮
					click("xpath", "//span[text()='修改']")
					
					# 切入修改的iframe窗体
					switch_to("xpath", "//iframe[@id='modWin-iframe']")
					sleep(2)
					
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
					print("付款处理-现金支付，修改成功！")
					logging.info("付款处理-现金支付，修改成功！")
					time.sleep(3)
					
					# 数据删除
					switch_to("xpath", "//iframe[@id='generalPayment-tab-iframe']")
					sleep(1)
					
					# 点击现金支付
					click("xpath", "//span[text()='现金支付']")
					
					# 切入‘现金支付’的iframe窗体
					switch_to("xpath", "//iframe[@id='subTabFour-iframe']")
					sleep(1)
					
					# 修改勾选数据
					click("xpath", "//div[@title='收款户名:Mindy科技有限公司']/parent::*/preceding-sibling::*[6]/descendant::*[2]")
					
					# 点击删除按钮
					click("xpath", "//span[text()='删除']")
					
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现删除的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("付款处理-现金支付，删除成功！")
					logging.info("付款处理-现金支付，删除成功！")
					time.sleep(3)
				
				if i == 2:
					
					# 切入‘现金支付’的iframe窗体
					switch_to("xpath", "//iframe[@id='generalPayment-tab-iframe']")
					sleep(1)
					
					# 点击现金支付
					click("xpath", "//span[text()='现金支付']")
					
					# 切入‘现金支付’的iframe窗体
					switch_to("xpath", "//iframe[@id='subTabFour-iframe']")
					sleep(1)
					
					# 修改勾选数据
					click("xpath", "//div[@title='收款户名:Mindy科技有限公司']/parent::*/preceding-sibling::*[6]/descendant::*[2]")
					
					# 点击审核按钮
					click("xpath", "//span[text()='送审']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！送审成功1笔，失败0笔。')]")
					print("付款处理-现金支付，送审成功！")
					logging.info("付款处理-现金支付，送审成功！")
					time.sleep(3)
					
					switch_to("xpath", "//iframe[@id='generalPayment-tab-iframe']")
					sleep(1)
					
					# 点击现金支付
					click("xpath", "//span[text()='现金支付']")
					
					# 切入‘现金支付’的iframe窗体
					switch_to("xpath", "//iframe[@id='subTabFour-iframe']")
					sleep(1)
					
					# 修改勾选数据
					click("xpath", "//div[@title='收款户名:Mindy科技有限公司']/parent::*/preceding-sibling::*[6]/descendant::*[2]")
					
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
					print("付款处理-现金支付，撤销送审成功！")
					logging.info("付款处理-现金支付，撤销送审成功！")
					time.sleep(3)
					
					# 切入‘现金支付’的iframe窗体
					switch_to("xpath", "//iframe[@id='generalPayment-tab-iframe']")
					sleep(1)
					
					# 点击现金支付
					click("xpath", "//span[text()='现金支付']")
					
					# 切入‘现金支付’的iframe窗体
					switch_to("xpath", "//iframe[@id='subTabFour-iframe']")
					sleep(1)
					
					# 修改勾选数据
					click("xpath", "//div[@title='收款户名:Mindy科技有限公司']/parent::*/preceding-sibling::*[6]/descendant::*[2]")
					
					# 点击审核按钮
					click("xpath", "//span[text()='送审']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！送审成功1笔，失败0笔。')]")
					print("付款处理-现金支付，送审成功！")
					logging.info("付款处理-现金支付，送审成功！")
					time.sleep(3)
					
					# 切入‘现金支付’的iframe窗体
					switch_to("xpath", "//iframe[@id='generalPayment-tab-iframe']")
					sleep(1)
					
					# 点击现金支付
					click("xpath", "//span[text()='现金支付']")
					
					# 切入‘现金支付’的iframe窗体
					switch_to("xpath", "//iframe[@id='subTabFour-iframe']")
					sleep(1)
					
					# 修改勾选数据
					double_click("xpath", "//div[@title='收款户名:Mindy科技有限公司']/parent::*/preceding-sibling::*[6]/descendant::*[2]")
					sleep(1)
					
					switch_to("xpath", "//iframe[@id='wf_taskProcessing_win-iframe']")
					sleep(1)
					
					click("xpath", "//span[text()='同意']")
					sleep(1)
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("现金支付，审批成功！")
					logging.info("现金支付，审批成功！")
					time.sleep(3)
					
					# 切入‘现金支付’的iframe窗体
					switch_to("xpath", "//iframe[@id='generalPayment-tab-iframe']")
					sleep(1)
					
					# 点击现金支付
					click("xpath", "//span[text()='现金支付']")
					
					# 切入‘现金支付’的iframe窗体
					switch_to("xpath", "//iframe[@id='subTabFour-iframe']")
					sleep(1)
					
					# 支付
					# 勾选数据
					click("xpath", "//div[@title='收款户名:Mindy科技有限公司']/parent::*/preceding-sibling::*[6]/descendant::*[2]")
					sleep(1)

					# 点击‘支付’按钮
					click("xpath", "//span[text()='支付']")
					sleep(1)
					
					# 点击确定按钮
					click("xpath", "//span[text()='确定']")
					sleep(1)
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！1笔进行了支付，0笔不允许支付。')]")
					print("现金支付，确认支付成功！")
					logging.info("现金支付，确认支付成功！")
					time.sleep(3)
					
					# 打印
					# 切入‘现金支付’的iframe窗体
					switch_to("xpath", "//iframe[@id='generalPayment-tab-iframe']")
					sleep(1)
					
					# 点击现金支付
					click("xpath", "//span[text()='现金支付']")
					
					# 切入‘现金支付’的iframe窗体
					switch_to("xpath", "//iframe[@id='subTabFour-iframe']")
					sleep(1)
					
					# 勾选数据
					click("xpath", "//div[@title='收款户名:Mindy科技有限公司']/parent::*/preceding-sibling::*[6]/descendant::*[2]")
					sleep(1)
					
					# 用JS方便点击‘打印’按钮旁边的倒三角形
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
							print("现金支付，打印成功!！")
							time.sleep(3)
							self.driver.switch_to.window(now_handle)
							switch_default()
					
					# 打印-打印记录
					# 切入‘现金支付’的iframe窗体
					switch_to("xpath", "//iframe[@id='generalPayment-tab-iframe']")
					sleep(1)
					
					# 点击现金支付
					click("xpath", "//span[text()='现金支付']")
					
					# 切入‘现金支付’的iframe窗体
					switch_to("xpath", "//iframe[@id='subTabFour-iframe']")
					sleep(1)
					
					# # 勾选数据
					# click("xpath", "//div[@title='收款户名:Mindy科技有限公司']/parent::*/preceding-sibling::*[6]/descendant::*[2]")
					# sleep(1)
					
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
					print("现金支付，打印记录查看成功！")
					logging.info("现金支付，打印记录查看成功！")
					time.sleep(3)
					
					switch_parent()
					
					# 点击关闭页面
					click("xpath", "//span[text()='打印记录']/preceding-sibling::*[1]")
					sleep(1)
					
					switch_default()
					
					# 切入‘现金支付’的iframe窗体
					switch_to("xpath", "//iframe[@id='generalPayment-tab-iframe']")
					sleep(1)
					
					# 点击现金支付
					click("xpath", "//span[text()='现金支付']")
					
					# 切入‘现金支付’的iframe窗体
					switch_to("xpath", "//iframe[@id='subTabFour-iframe']")
					sleep(1)
					
					# # 支付
					# # 勾选数据
					# click("xpath",
					#       "//div[@title='收款户名:Mindy科技有限公司']/parent::*/preceding-sibling::*[6]/descendant::*[2]")
					# sleep(1)
					
					# 点击‘支付’按钮
					click("xpath", "//span[text()='作废']")
					sleep(1)
					
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("现金支付，作废成功！")
					logging.info("现金支付，作废成功！")
					time.sleep(3)
				
			switch_default()
			
			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='付款处理']/child::*[1]")
			
			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//span[text()='资金系统收付']")
			# 打印操作成功日志
			print("现金支付，操作成功!")
			logging.info("现金支付，操作成功!")
			time.sleep(2)
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("现金支付失败！" + str(traceback.format_exc()))
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
