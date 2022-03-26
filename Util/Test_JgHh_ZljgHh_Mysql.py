# encoding=utf-8
# @Time : 2020/8/14 15:28
# @Author : Mindy
# 此文件是测试MySQL版本资金结算管理--资金系统收付--结购换汇--直联结购换汇
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

class Test_JgHh_ZljgHh_Mysql(unittest.TestCase):
	
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
		
		# 开始测试资金系统收付--结购换汇--直联结构换汇
		# 测试结购换汇--直联结构换汇
		try:
			# 点击'资金系统收付'菜单
			click("xpath", "//span[text()='资金系统收付']")
			# 点击结购换汇菜单
			click("xpath", "//span[text()='结购换汇']")
			# 退出所有iframe窗体
			switch_default()
			
			for i in range(1, 5):
				# 切入结购换汇的iframe窗体
				switch_to("xpath", "//iframe[@id='exchangePay-tab-iframe']")
				logging.info("开始测试直联结构换汇功能")
				sleep(1)
				
				switch_to("xpath", "//iframe[@id='subTabOne-iframe']")
				# 点击新增
				click("xpath", "//span[text()='新增']")
				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='addWin-iframe']")
				sleep(1)
				
				# 输入结构代码
				input("xpath", "//input[@id='ourregorgcode']", "TestRegorgCode")
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
				input("xpath", "//input[@id='combobox-input-paytypeid']", "结汇")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-paytypeid']")
				input_enter("xpath", "//input[@id='combobox-input-paytypeid']")
				time.sleep(1)
				
				# 选择结算方式
				click("xpath", "//input[@id='combobox-input-settlementmodeid']")
				clear("xpath", "//input[@id='combobox-input-settlementmodeid']")
				sleep(1)
				# 输入开户行大连泡崖街支行名称，模糊查询
				input("xpath", "//input[@id='combobox-input-settlementmodeid']", "直联单笔转账")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-settlementmodeid']")
				input_enter("xpath", "//input[@id='combobox-input-settlementmodeid']")
				time.sleep(1)
				
				# 付方账户
				click("xpath", "//input[@id='combobox-input-ourbankaccountid']")
				# 输入开户行大连泡崖街支行名称，模糊查询
				input("xpath", "//input[@id='combobox-input-ourbankaccountid']", "中国银行")
				sleep(1)
				input_enter("xpath", "//input[@id='combobox-input-ourbankaccountid']")
				sleep(1)
				# input_down("xpath", "//input[@id='combobox-input-ourbankaccountid']")
				# input_enter("xpath", "//input[@id='combobox-input-ourbankaccountid']")
				# time.sleep(1)
				click("xpath", "//div[contains(text(),'USD')]")
				sleep(1)
				
				# 收方账户
				click("xpath", "//input[@id='combobox-input-oppbankaccountid']")
				sleep(1)
				input("xpath", "//input[@id='combobox-input-oppbankaccountid']", "CNY")
				sleep(1)
				input_enter("xpath", "//input[@id='combobox-input-oppbankaccountid']")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-oppbankaccountid']")
				sleep(1)
				input_enter("xpath", "//input[@id='combobox-input-oppbankaccountid']")
				sleep(1)
			
				# 输入结汇金额
				click("xpath", "//input[@id='amount-input']")
				sleep(1)
				clear("xpath", "//input[@id='amount-input']")
				sleep(1)
				input("xpath", "//input[@id='amount-input']", "30000")
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
				print("直联结构换汇，第%s次保存成功！" % i)
				time.sleep(3)
				
				# 第一笔，就先修改，再修改页面提交送审，再撤销送审，再删除
				if i == 1:
					# 切入‘直联结构换汇’的iframe窗体
					switch_to("xpath", "//iframe[@id='exchangePay-tab-iframe']")
					sleep(1)
					
					switch_to("xpath", "//iframe[@id='subTabOne-iframe']")
					sleep(1)
					
					# # 点击查看
					# # 用JS的方法点击放大镜
					# js_click("xpath", "//span[@class='f-contrac-close']")
					# sleep(1)
					#
					# # 输入收款户名：亚唐科技
					# click("xpath", "//input[@id='oppbankaccountname']")
					# sleep(1)
					# input("xpath", "//input[@id='oppbankaccountname']", "亚唐科技")
					# sleep(1)
					#
					# # 点击查询
					# click("xpath", "//span[text()='查询']")
					
					# 修改勾选数据
					click("xpath",
					      "//div[@title='结购换汇币种:USD-美元']/parent::*/preceding-sibling::*[6]/descendant::*[2]")
					
					# 点击审核按钮
					click("xpath", "//span[text()='送审']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！送审成功1笔，失败0笔。')]")
					print("结购换汇-直联结构换汇，送审成功！")
					logging.info("结购换汇-直联结构换汇，送审成功！")
					time.sleep(3)
					
					switch_to("xpath", "//iframe[@id='exchangePay-tab-iframe']")
					sleep(1)
					
					switch_to("xpath", "//iframe[@id='subTabOne-iframe']")
					sleep(1)
					
					# 修改勾选数据
					click("xpath",
					      "//div[@title='结购换汇币种:USD-美元']/parent::*/preceding-sibling::*[6]/descendant::*[2]")
					
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
					print("结购换汇-直联结构换汇，撤销送审成功！")
					logging.info("结购换汇-直联结构换汇，撤销送审成功！")
					time.sleep(3)
					
					switch_to("xpath", "//iframe[@id='exchangePay-tab-iframe']")
					sleep(1)
					
					switch_to("xpath", "//iframe[@id='subTabOne-iframe']")
					sleep(1)
					
					# 修改勾选数据
					click("xpath",
					      "//div[@title='结购换汇币种:USD-美元']/parent::*/preceding-sibling::*[6]/descendant::*[2]")
					
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
					print("结购换汇-直联结构换汇，修改成功！")
					logging.info("结购换汇-直联结构换汇，修改成功！")
					time.sleep(3)
					
					# 切入‘直联结构换汇’的iframe窗体
					switch_to("xpath", "//iframe[@id='exchangePay-tab-iframe']")
					sleep(1)
					
					switch_to("xpath", "//iframe[@id='subTabOne-iframe']")
					sleep(1)
					
					# 修改勾选数据
					click("xpath",
					      "//div[@title='结购换汇币种:USD-美元']/parent::*/preceding-sibling::*[6]/descendant::*[2]")
					
					# 点击审核按钮
					click("xpath", "//span[text()='送审']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！送审成功1笔，失败0笔。')]")
					print("结购换汇-直联结构换汇，送审成功！")
					logging.info("结购换汇-直联结构换汇，送审成功！")
					time.sleep(3)
					
					# 切入‘直联结构换汇’的iframe窗体
					switch_to("xpath", "//iframe[@id='exchangePay-tab-iframe']")
					sleep(1)
					
					switch_to("xpath", "//iframe[@id='subTabOne-iframe']")
					sleep(1)
					
					# 修改勾选数据
					double_click("xpath",
					             "//div[@title='结购换汇币种:USD-美元']/parent::*/preceding-sibling::*[6]/descendant::*[2]")
					sleep(1)
					
					switch_to("xpath", "//iframe[@id='wf_taskProcessing_win-iframe']")
					sleep(1)
					
					click("xpath", "//span[text()='同意']")
					sleep(1)
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("直联结构换汇，审批成功！")
					logging.info("直联结构换汇，审批成功！")
					time.sleep(3)
					
					# 点击支付
					# 支付
					# 切入‘直联结构换汇’的iframe窗体
					switch_to("xpath", "//iframe[@id='exchangePay-tab-iframe']")
					sleep(1)
					
					switch_to("xpath", "//iframe[@id='subTabOne-iframe']")
					sleep(1)
					
					# 勾选数据
					click("xpath",
					      "//div[@title='结购换汇币种:USD-美元']/parent::*/preceding-sibling::*[6]/descendant::*[2]")
					sleep(1)
					
					click("xpath", "//span[text()='支付']")
					sleep(1)
					
					switch_to("xpath", "//iframe[@id='confirmPayWin-iframe']")
					sleep(1)
					
					# 启动大额支付的系统参数的情况下勾选数据
					click("xpath", "//button[@class='f-grid-radio']")
					sleep(1)
					
					click("xpath", "//span[text()='确认支付']")
					sleep(1)
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！1笔进行了支付，0笔不允许支付。')]")
					print("直联结构换汇，收付失败！")
					logging.info("直联结构换汇，收付失败！")
					time.sleep(3)
					
					# 修改数据库
					# 通过封装修改数据库函数把支付状态改为'收付结果无法识别'
					my_sql(my_host, my_port, my_user, my_passwd, my_db, "update T_SE_PAYMENTS a set a.paystate='7' where  a.oppbankaccountname='亚唐科技' and a.createdby='mindy'")
					time.sleep(2)
					
					# 切入‘直联结构换汇’的iframe窗体
					switch_to("xpath", "//iframe[@id='exchangePay-tab-iframe']")
					sleep(1)
					
					switch_to("xpath", "//iframe[@id='subTabOne-iframe']")
					sleep(1)
					
					# 点击右下角的刷新按钮
					click("xpath", "//span[@id='gridbar-page-refresh']")
					sleep(1)
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//div[@title='支付状态:收付结果无法识别']")
					print("直联结构换汇，状态更改成功！")
					logging.info("直联结构换汇，状态更改成功！")
					time.sleep(3)
					
					# 查询状态
					# 勾选数据
					click("xpath",
					      "//div[@title='结购换汇币种:USD-美元']/parent::*/preceding-sibling::*[6]/descendant::*[2]")
					sleep(1)
					
					# 用JS方便点击‘支付’按钮旁边的倒三角形
					js_click("xpath", "//span[text()='支付']/parent::*/following-sibling::*/child::*")
					sleep(1)
					
					# 点击查询状态按钮
					js_click("xpath", "//a[contains(text(),'查询状态')]")
					sleep(1)
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'单据已查询状态，请查看相应结果！')]")
					print("直联结构换汇，查询状态成功！")
					logging.info("直联结构换汇，查询状态成功")
					time.sleep(3)
					
					# 余额检测
					# 切入‘直联结构换汇’的iframe窗体
					switch_to("xpath", "//iframe[@id='exchangePay-tab-iframe']")
					sleep(1)
					
					switch_to("xpath", "//iframe[@id='subTabOne-iframe']")
					sleep(1)
					
					# 勾选数据
					click("xpath",
					      "//div[@title='结购换汇币种:USD-美元']/parent::*/preceding-sibling::*[6]/descendant::*[2]")
					sleep(1)
					
					# 用JS方便点击‘支付’按钮旁边的倒三角形
					js_click("xpath", "//span[text()='支付']/parent::*/following-sibling::*/child::*")
					sleep(1)
					
					# 点击余额检测按钮
					js_click("xpath", "//a[contains(text(),'余额检测')]")
					sleep(1)
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'当前余额')]")
					print("直联结构换汇，余额检测成功！")
					logging.info("直联结构换汇，余额检测成功")
					time.sleep(3)
					
					# 修改数据库
					# 通过封装修改数据库函数把支付状态是'支付失败'改为'收付结果无法识别'
					my_sql(my_host, my_port, my_user, my_passwd, my_db, "update T_SE_PAYMENTS a set a.paystate='7' where  a.oppbankaccountname='亚唐科技' and a.createdby='mindy'")
					time.sleep(2)
					
					# 切入‘直联结构换汇’的iframe窗体
					switch_to("xpath", "//iframe[@id='exchangePay-tab-iframe']")
					sleep(1)
					
					switch_to("xpath", "//iframe[@id='subTabOne-iframe']")
					sleep(1)
					
					# 点击右下角的刷新按钮
					click("xpath", "//span[@id='gridbar-page-refresh']")
					sleep(1)
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//div[@title='支付状态:收付结果无法识别']")
					print("直联结构换汇，状态更改成功！")
					logging.info("直联结构换汇，状态更改成功！")
					time.sleep(3)
					
					# 确认已支付
					# 勾选数据
					click("xpath", "//div[@title='结购换汇币种:USD-美元']/parent::*/preceding-sibling::*[6]/descendant::*[2]")
					sleep(1)
					
					# 用JS方便点击‘支付’按钮旁边的倒三角形
					js_click("xpath", "//span[text()='支付']/parent::*/following-sibling::*/child::*")
					sleep(1)
					
					# 点击余额检测按钮
					js_click("xpath", "//a[contains(text(),'确认已支付')]")
					sleep(1)
					
					# 点击OK按钮
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					sleep(1)
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("直联结构换汇，确认已支付成功！")
					logging.info("直联结构换汇，确认已支付成功！")
					time.sleep(3)
					
					# 日志查看
					# 切入‘直联结构换汇’的iframe窗体
					switch_to("xpath", "//iframe[@id='exchangePay-tab-iframe']")
					sleep(1)
					
					switch_to("xpath", "//iframe[@id='subTabOne-iframe']")
					sleep(1)
					
					# 勾选数据
					click("xpath",
					      "//div[@title='结购换汇币种:USD-美元']/parent::*/preceding-sibling::*[6]/descendant::*[2]")
					sleep(1)
					
					# 用JS方便点击‘支付’按钮旁边的倒三角形
					js_click("xpath", "//span[text()='支付']/parent::*/following-sibling::*/child::*")
					sleep(1)
					
					# 点击日志查看按钮
					js_click("xpath", "//a[contains(text(),'日志查看')]")
					sleep(1)
					
					switch_to("xpath", "//iframe[@id='logsWin-iframe']")
					sleep(1)
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//div[@title='日志类型:查询状态']")
					print("直联结构换汇，日志查看成功！")
					logging.info("直联结构换汇，日志查看成功！")
					time.sleep(3)
					
					switch_parent()
					
					# 点击关闭页面
					click("xpath", "//span[text()='支付日志']/preceding-sibling::*[1]")
					sleep(1)
					
					switch_default()
				
				if i == 2:
					# 切入‘直联结构换汇’的iframe窗体
					switch_to("xpath", "//iframe[@id='exchangePay-tab-iframe']")
					sleep(1)
					
					switch_to("xpath", "//iframe[@id='subTabOne-iframe']")
					sleep(1)
					
					# 修改勾选数据
					click("xpath",
					      "//div[@title='结购换汇币种:USD-美元']/parent::*/preceding-sibling::*[6]/descendant::*[2]")
					
					# 点击审核按钮
					click("xpath", "//span[text()='送审']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！送审成功1笔，失败0笔。')]")
					print("结购换汇-直联结构换汇，送审成功！")
					logging.info("结购换汇-直联结构换汇，送审成功！")
					time.sleep(3)
					
					# 切入‘直联结构换汇’的iframe窗体
					switch_to("xpath", "//iframe[@id='exchangePay-tab-iframe']")
					sleep(1)
					
					switch_to("xpath", "//iframe[@id='subTabOne-iframe']")
					sleep(1)
					
					# 修改勾选数据
					double_click("xpath",
					             "//div[@title='结购换汇币种:USD-美元']/parent::*/preceding-sibling::*[6]/descendant::*[2]")
					sleep(1)
					
					switch_to("xpath", "//iframe[@id='wf_taskProcessing_win-iframe']")
					sleep(1)
					
					click("xpath", "//span[text()='同意']")
					sleep(1)
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("直联结构换汇，审批成功！")
					logging.info("直联结构换汇，审批成功！")
					time.sleep(3)
			
					# 支付
					# 切入‘直联结构换汇’的iframe窗体
					switch_to("xpath", "//iframe[@id='exchangePay-tab-iframe']")
					sleep(1)
					
					switch_to("xpath", "//iframe[@id='subTabOne-iframe']")
					sleep(1)
					
					# 勾选数据
					click("xpath",
					      "//div[@title='结购换汇币种:USD-美元']/parent::*/preceding-sibling::*[6]/descendant::*[2]")
					sleep(1)
					
					click("xpath", "//span[text()='支付']")
					sleep(1)
					
					switch_to("xpath", "//iframe[@id='confirmPayWin-iframe']")
					sleep(1)
					
					# 启动大额支付的系统参数的情况下勾选数据
					click("xpath", "//button[@class='f-grid-radio']")
					sleep(1)
					
					click("xpath", "//span[text()='确认支付']")
					sleep(1)
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！1笔进行了支付，0笔不允许支付。')]")
					print("直联结构换汇，收付失败！")
					logging.info("直联结构换汇，收付失败！")
					time.sleep(3)
					
					# 确定支付
					# 通过封装修改数据库函数把支付状态是'支付失败'改为'收付结果无法识别'
					my_sql(my_host, my_port, my_user, my_passwd, my_db, "update T_SE_PAYMENTS a set a.paystate='7' where  a.oppbankaccountname='亚唐科技' and a.createdby='mindy'")
					time.sleep(2)
					
					# 切入‘直联结构换汇’的iframe窗体
					switch_to("xpath", "//iframe[@id='exchangePay-tab-iframe']")
					sleep(1)
					
					switch_to("xpath", "//iframe[@id='subTabOne-iframe']")
					sleep(1)
					
					# 点击右下角的刷新按钮
					click("xpath", "//span[@id='gridbar-page-refresh']")
					sleep(1)
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//div[@title='支付状态:收付结果无法识别']")
					print("直联结构换汇，状态更改成功！")
					logging.info("直联结构换汇，状态更改成功！")
					time.sleep(3)
					
					# 确认支付失败
					# 勾选数据
					click("xpath", "//div[@title='结购换汇币种:USD-美元']/parent::*/preceding-sibling::*[6]/descendant::*[2]")
					sleep(1)
					
					# 用JS方便点击‘支付’按钮旁边的倒三角形
					js_click("xpath", "//span[text()='支付']/parent::*/following-sibling::*/child::*")
					sleep(1)
					
					# 点击确认支付失败按钮
					js_click("xpath", "//a[contains(text(),'确认支付失败')]")
					sleep(1)
					
					# 点击OK按钮
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					sleep(1)
					
					# 切入新的窗口
					switch_to("xpath", "//iframe[@id='confirmFailureToPayWin-iframe']")
					sleep(1)
					
					# 点击勾选记录
					click("xpath", "//button[@class='f-grid-radio']")
					sleep(1)
					
					# 点击确认支付失败按钮
					click("xpath", "//span[text()='确认支付失败']")
					sleep(1)
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'确认支付失败申请流程发起成功！')]")
					print("直联结构换汇，确认支付失败申请流程发起成功！")
					logging.info("直联结构换汇，确认支付失败申请流程发起成功！")
					time.sleep(3)
					
					# 确定支付
					# 通过封装修改数据库函数把支付状态是'支付失败'改为'收付结果无法识别'
					my_sql(my_host, my_port, my_user, my_passwd, my_db, "update T_SE_PAYMENTS a set a.paystate='1' where  a.oppbankaccountname='亚唐科技' and a.createdby='mindy'")
					time.sleep(2)
					
					# 切入‘直联结构换汇’的iframe窗体
					switch_to("xpath", "//iframe[@id='exchangePay-tab-iframe']")
					sleep(1)
					
					switch_to("xpath", "//iframe[@id='subTabOne-iframe']")
					sleep(1)
					
					# 点击右下角的刷新按钮
					click("xpath", "//span[@id='gridbar-page-refresh']")
					sleep(1)
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//div[@title='支付状态:未收付']")
					print("直联结构换汇，状态更改成功！")
					logging.info("直联结构换汇，状态更改成功！")
					time.sleep(3)
				
					# 作废
					# 勾选数据
					click("xpath",
					      "//div[@title='结购换汇币种:USD-美元']/parent::*/preceding-sibling::*[6]/descendant::*[2]")
					sleep(1)
					
					# 点击作废按钮
					js_click("xpath", "//span[text()='作废']")
					sleep(1)
					
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					sleep(1)
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("直联结构换汇, 作废成功！")
					logging.info("直联结构换汇, 作废成功！")
					time.sleep(3)
					
				if i == 3:
					
					#  因为具有审批历史的单据不允许删除，因此第二笔删除
					switch_to("xpath", "//iframe[@id='exchangePay-tab-iframe']")
					sleep(1)
					
					switch_to("xpath", "//iframe[@id='subTabOne-iframe']")
					sleep(1)
					
					# 修改勾选数据
					click("xpath", "//div[@title='结购换汇币种:USD-美元']/parent::*/preceding-sibling::*[6]/descendant::*[2]")
					
					# 点击删除按钮
					click("xpath", "//span[text()='删除']")
					
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现删除的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("结购换汇-直联结构换汇，删除成功！")
					logging.info("结购换汇-直联结构换汇，删除成功！")
					time.sleep(3)
		
				if i == 4:
					# 切入‘直联结构换汇’的iframe窗体
					switch_to("xpath", "//iframe[@id='exchangePay-tab-iframe']")
					sleep(1)
					
					switch_to("xpath", "//iframe[@id='subTabOne-iframe']")
					sleep(1)
					
					# 修改勾选数据
					click("xpath",
					      "//div[@title='结购换汇币种:USD-美元']/parent::*/preceding-sibling::*[6]/descendant::*[2]")
					
					# 点击审核按钮
					click("xpath", "//span[text()='送审']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！送审成功1笔，失败0笔。')]")
					print("结购换汇-直联结构换汇，送审成功！")
					logging.info("结购换汇-直联结构换汇，送审成功！")
					time.sleep(3)
					
					# 切入‘直联结构换汇’的iframe窗体
					switch_to("xpath", "//iframe[@id='exchangePay-tab-iframe']")
					sleep(1)
					
					switch_to("xpath", "//iframe[@id='subTabOne-iframe']")
					sleep(1)
					
					# 修改勾选数据
					double_click("xpath",
					             "//div[@title='结购换汇币种:USD-美元']/parent::*/preceding-sibling::*[6]/descendant::*[2]")
					sleep(1)
					
					switch_to("xpath", "//iframe[@id='wf_taskProcessing_win-iframe']")
					sleep(1)
					
					click("xpath", "//span[text()='同意']")
					sleep(1)
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("直联结构换汇，审批成功！")
					logging.info("直联结构换汇，审批成功！")
					time.sleep(3)
					
					# 确认非直联已支付
					# 切入‘直联结构换汇’的iframe窗体
					switch_to("xpath", "//iframe[@id='exchangePay-tab-iframe']")
					sleep(1)
					
					switch_to("xpath", "//iframe[@id='subTabOne-iframe']")
					sleep(1)
					
					# 勾选数据
					click("xpath", "//div[@title='结购换汇币种:USD-美元']/parent::*/preceding-sibling::*[6]/descendant::*[2]")
					sleep(1)
					
					# 用JS方便点击‘支付’按钮旁边的倒三角形
					js_click("xpath", "//span[text()='支付']/parent::*/following-sibling::*/child::*")
					sleep(1)
					
					# 点击非直联已支付按钮
					js_click("xpath", "//a[contains(text(),'确认非直联已支付')]")
					sleep(1)
					
					# 点击OK按钮
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					sleep(1)
					
					# 切入新的窗口
					switch_to("xpath", "//iframe[@id='confirmUndirectPayWin-iframe']")
					sleep(1)
					
					# 点击勾选记录
					click("xpath", "//input[@id='combobox-input-actualsettlementmodeid']")
					sleep(1)
					input("xpath", "//input[@id='combobox-input-actualsettlementmodeid']", "其他支付")
					sleep(1)
					input_enter("xpath", "//input[@id='combobox-input-actualsettlementmodeid']")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-actualsettlementmodeid']")
					sleep(1)
					input_enter("xpath", "//input[@id='combobox-input-actualsettlementmodeid']")
					time.sleep(1)
					
					# 点击确认支付失败按钮
					click("xpath", "//span[text()='确定']")
					sleep(1)
					
					# 点击OK按钮
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					sleep(1)
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'共1笔，处理成功1笔，失败0笔。')]")
					print("直联结构换汇，确认非直联已支付成功！")
					logging.info("直联结构换汇，确认非直联已支付成功！")
					time.sleep(3)
			
			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='结购换汇']/child::*[1]")
			
			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//span[text()='资金系统收付']")
			# 打印操作成功日志
			print("直联结构换汇，操作成功!")
			logging.info("直联结构换汇，操作成功!")
			time.sleep(2)
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("直联结构换汇失败！" + str(traceback.format_exc()))
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