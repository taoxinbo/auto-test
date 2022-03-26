# encoding=utf-8
# @Time : 2020/9/7 14:44
# @Author : Mindy
# 此文件是测试Oracle版本资金结算管理-业务系统对接-快捷付款-付款申请
# 此页面的测试数据是付款处理模块，RECORDSOURCE单据来源改为4，接口导入

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


class Test_Kjfk_fksq_Oracle(unittest.TestCase):
	
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
		"""
		# 在资金系统收付--付款处理--直联单笔付款维护数据
		try:
			# 点击'资金系统收付'菜单
			click("xpath", "//span[text()='资金系统收付']")
			# 点击付款处理菜单
			click("xpath", "//span[text()='付款处理']")
			# 退出所有iframe窗体
			switch_default()
			
			for i in range(1, 7):
				# 切入付款处理的iframe窗体
				switch_to("xpath", "//iframe[@id='generalPayment-tab-iframe']")
				logging.info("开始测试直联单笔付款功能")
				sleep(1)
				switch_to("xpath", "//iframe[@id='subTabTwo-iframe']")
				# 点击新增
				click("xpath", "//span[text()='新增']")
				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='addWin-iframe']")
				sleep(1)
				
				# 部门
				click("xpath", "//input[@id='combobox-input-deptid']")
				input_enter("xpath", "//input[@id='combobox-input-deptid']")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-deptid']")
				input_enter("xpath", "//input[@id='combobox-input-deptid']")
				time.sleep(1)
				
				# 交易类型
				click("xpath", "//input[@id='combobox-input-paytypeid']")
				# 输入开户行大连泡崖街支行名称，模糊查询
				input("xpath", "//input[@id='combobox-input-paytypeid']", "对外付款")
				sleep(1)
				input_enter("xpath", "//input[@id='combobox-input-paytypeid']")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-paytypeid']")
				sleep(1)
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
				input_down("xpath", "//input[@id='combobox-input-ourbankaccountid']")
				input_enter("xpath", "//input[@id='combobox-input-ourbankaccountid']")
				time.sleep(1)
				
				# 收方名称
				input("xpath", "//input[@id='combobox-input-oppcounterpartyid']", "Mindy自动化测试快捷付款")
				sleep(1)
				
				# 双击清楚下拉框
				double_click("xpath", "//span[text()='卡折类型']")
				sleep(1)
				
				# 收方账户
				input("xpath", "//input[@id='combobox-input-oppcounterpartyaccountid']", "234554321")
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
				print("直联单笔付款，第%s次保存成功！" % i)
				time.sleep(3)
				
			switch_default()
			
			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='付款处理']/child::*[1]")
			
			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//span[text()='资金系统收付']")
			# 打印操作成功日志
			print("直联单笔支付，操作成功!")
			logging.info("直联单笔支付，操作成功!")
			time.sleep(2)
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("直联单笔支付失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
			
		# 修改数据库
		# 通过封装修改数据库函数把支付状态是'支付失败'改为'收付结果无法识别'
		ora_sql(ora_ip, ora_sid, ora_user, ora_pwd, "update t_se_payments a set a.recordsource='4' where a.oppbankaccountname='Mindy自动化测试快捷付款' and a.createdby='mindy'")
		time.sleep(2)
		
		#  系统设置-界面元素管理
		try:
			# 点击系统设置
			click("xpath", "//div[@class='sysconfigset']")
			
			# 点击进入系统设置页面
			switch_to("xpath", "//iframe[@id='systemconfig-tab-iframe']")
			sleep(1)
			
			logging.info("开始测试基础资料--界面元素管理的功能")
			# 将页面的滚动条滑动到‘界面元素管理’页面的地方
			js_gd("xpath", "//span[contains(text(),'界面元素管理')]")
			# 用JS的方法点击界面元素管理菜单按钮
			js_click("xpath", "//span[contains(text(),'界面元素管理')]")
			
			switch_default()
			# 进入界面元素管理窗体
			switch_to("xpath", "//iframe[@id='pagecontrolsmanager-tab-iframe']")
			# 进入界面元素控制的窗体
			switch_to("xpath", "//iframe[@id='subTabOne-iframe']")
			
			# 用JS点击新增
			js_click("xpath", "//span[text()='新增']")
			sleep(1)
			
			# 进入新增的窗体
			switch_to("xpath", "//iframe[@id='addWin-iframe']")
			
			# 控制类型
			click("xpath", "//input[@id='combobox-input-pagetype']")
			sleep(1)
			input("xpath", "//input[@id='combobox-input-pagetype']", "快捷付款单")
			sleep(1)
			input_enter("xpath", "//input[@id='combobox-input-pagetype']")
			sleep(1)
			
			# 字段信息
			click("xpath", "//input[@id='combobox-input-fieldid']")
			sleep(1)
			input("xpath", "//input[@id='combobox-input-fieldid']", "用途")
			sleep(1)
			input_down("xpath", "//input[@id='combobox-input-fieldid']")
			sleep(1)
			input_enter("xpath", "//input[@id='combobox-input-fieldid']")
			sleep(1)
			
			# 界面元素控制优先
			click("xpath", "//input[@id='isstrictcontrol']")
			sleep(1)
			
			# 点击保存
			click("xpath", "//span[text()='保存']")
			
			switch_default()
			
			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功')]")
			print("界面元素控制，保存成功！")
			time.sleep(3)
			
			# 再次点击基础设置菜单，使之关闭
			# 用JS的方法关闭当前页面
			
			js_click("xpath", "//a[@title='界面元素管理']/child::*[1]")
			sleep(1)
			js_click("xpath", "//a[@title='系统设置']/child::*[1]")
			# 打印操作成功日志
			print("界面元素控制，操作成功!")
			logging.info("界面元素控制，操作成功!")
			time.sleep(2)
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("界面元素控制,失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		"""
		# 在业务系统对接-快捷付款-付款申请
		try:
			# 点击'业务系统对接'菜单
			click("xpath", "//span[text()='业务系统对接']")
			# 点击快捷付款菜单
			click("xpath", "//span[text()='快捷付款']")
			# 退出所有iframe窗体
			switch_default()
			
			for i in range(1, 4):
				
				if i == 1:
					# 切入付款处理的iframe窗体
					switch_to("xpath", "//iframe[@id='externalPayments-tab-iframe']")
					logging.info("开始测试快捷付款功能")
					sleep(1)
					switch_to("xpath", "//iframe[@id='subTabOne-iframe']")
					
					# 选择第一笔数据
					click("xpath", "//span[contains(text(),'Mindy自动化测试快捷付款')]/ancestor::*[9]/descendant::*[1]/descendant::*[19]")
					sleep(1)
					
					# 选择第二笔数据
					click("xpath", "//span[contains(text(),'Mindy自动化测试快捷付款')]/ancestor::*[9]/descendant::*[1]/descendant::*[27]")
					sleep(1)
					
					# 点击合并
					click("xpath", "//span[text()='合并']")
					sleep(1)
					
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					
					# 进入新的iframe窗体mergeWin-iframe
					switch_to("xpath", "//iframe[@id='mergeWin-iframe']")
					sleep(1)
					
					# 选择付方账户
					click("xpath", "//input[@id='combobox-input-ourbankaccountid']")
					sleep(1)
					input_enter("xpath", "//input[@id='combobox-input-ourbankaccountid']")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-ourbankaccountid']")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-ourbankaccountid']")
					sleep(1)
					input_enter("xpath", "//input[@id='combobox-input-ourbankaccountid']")
					sleep(1)
					
					# 点击保存
					click("xpath", "//span[text()='保存']")
					sleep(1)
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("付款申请，合并成功！")
					logging.info("付款申请，合并成功！")
					time.sleep(3)
					
					# 合并后生成了三笔数据
					# 切入付款处理的iframe窗体
					switch_to("xpath", "//iframe[@id='externalPayments-tab-iframe']")
					sleep(1)
					switch_to("xpath", "//iframe[@id='subTabOne-iframe']")
					
					# 选择合并后的第一笔数据
					click("xpath", "//span[contains(text(),'Mindy自动化测试快捷付款')]/ancestor::*[9]/descendant::*[1]/descendant::*[19]")
					sleep(1)
					
					# 点击审核
					click("xpath", "//span[text()='审核']")
					sleep(1)
					
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！审核成功1笔，失败0笔。')]")
					print("付款申请，审核成功！")
					logging.info("付款申请，审核成功！")
					time.sleep(3)
					
					# 点击取消审核取消审核成功！
					# 操作成功！
					# 切入付款处理的iframe窗体
					switch_to("xpath", "//iframe[@id='externalPayments-tab-iframe']")
					sleep(1)
					switch_to("xpath", "//iframe[@id='subTabOne-iframe']")
					
					# 选择合并后的第一笔数据
					click("xpath",
					      "//span[contains(text(),'Mindy自动化测试快捷付款')]/ancestor::*[9]/descendant::*[1]/descendant::*[19]")
					sleep(1)
					
					# 用JS方便点击‘审核’按钮旁边的倒三角形
					js_click("xpath", "//span[text()='审核']/parent::*/following-sibling::*/child::*")
					sleep(1)
					
					# 点击取消审核按钮
					js_click("xpath", "//a[contains(text(),'取消审核')]")
					sleep(1)
					
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'取消审核成功！')]")
					print("付款申请，取消审核成功！")
					logging.info("付款申请，取消审核成功！")
					time.sleep(3)
					
					# 切入付款处理的iframe窗体
					switch_to("xpath", "//iframe[@id='externalPayments-tab-iframe']")
					sleep(1)
					switch_to("xpath", "//iframe[@id='subTabOne-iframe']")
					
					# 选择合并后的第一笔数据
					click("xpath",
					      "//span[contains(text(),'Mindy自动化测试快捷付款')]/ancestor::*[9]/descendant::*[1]/descendant::*[19]")
					sleep(1)
					
					# 点击审核
					click("xpath", "//span[text()='审核']")
					sleep(1)
					
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！审核成功1笔，失败0笔。')]")
					print("付款申请，审核成功！")
					logging.info("付款申请，审核成功！")
					time.sleep(3)
					
					# 切入付款处理的iframe窗体
					switch_to("xpath", "//iframe[@id='externalPayments-tab-iframe']")
					sleep(1)
					switch_to("xpath", "//iframe[@id='subTabOne-iframe']")
					
					# 选择合并后的第一笔数据
					click("xpath", "//span[contains(text(),'Mindy自动化测试快捷付款')]/ancestor::*[9]/descendant::*[1]/descendant::*[19]")
					sleep(1)
					
					# 点击作废
					click("xpath", "//span[text()='作废']")
					sleep(1)
					
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					
					# 点击确定
					click("xpath", "//span[text()='确定']")
					sleep(1)
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("付款申请，作废成功！")
					logging.info("付款申请，作废成功！")
					time.sleep(3)
				if i == 2:
					# 对第一笔数据拆分，每种结算方式拆分一次，共有7个
					# 依次是直联批量代付、应收承兑汇票背书、应付承兑汇票背书、现金支付、
					# 现金支票支付、转账支票支付、现金/转账支票支付
					# 切入付款处理的iframe窗体
					switch_to("xpath", "//iframe[@id='externalPayments-tab-iframe']")
					sleep(1)
					switch_to("xpath", "//iframe[@id='subTabOne-iframe']")
					
					# 选择合并后的第一笔数据
					click("xpath", "//span[contains(text(),'Mindy自动化测试快捷付款')]/ancestor::*[9]/descendant::*[1]/descendant::*[19]")
					sleep(1)
					
					# 点击拆分
					click("xpath", "//span[text()='拆分']")
					sleep(1)
					
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					sleep(1)
					
					switch_to("xpath", "//iframe[@id='splitWin-iframe']")
					
					# 选择付方账户
					click("xpath", "//input[@id='combobox-input-ourbankaccountid']")
					sleep(1)
					input("xpath", "//input[@id='combobox-input-ourbankaccountid']", "CNY")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-ourbankaccountid']")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-ourbankaccountid']")
					sleep(1)
					input_enter("xpath", "//input[@id='combobox-input-ourbankaccountid']")
					sleep(1)
					
					# 选择结算方式combobox-input-settlementmodeid
					click("xpath", "//input[@id='combobox-input-settlementmodeid']")
					sleep(1)
					input("xpath", "//input[@id='combobox-input-settlementmodeid']", "直联批量代付")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-settlementmodeid']")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-settlementmodeid']")
					sleep(1)
					input_enter("xpath", "//input[@id='combobox-input-settlementmodeid']")
					sleep(1)
					
					# 填入拆分金额
					clear("xpath", "//input[@id='splitingamount-input']")
					sleep(1)
					input("xpath", "//input[@id='splitingamount-input']", "200")
					sleep(1)
					
					# 点击保存
					click("xpath", "//span[text()='保存']")
					sleep(1)
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功!')]")
					print("付款申请,拆分成功！")
					logging.info("付款申请，拆分成功！")
					time.sleep(3)
					
					switch_to("xpath", "//iframe[@id='externalPayments-tab-iframe']")
					sleep(1)
					switch_to("xpath", "//iframe[@id='subTabOne-iframe']")
					
					# 选择合并后的第一笔数据
					click("xpath",
					      "//span[contains(text(),'Mindy自动化测试快捷付款')]/ancestor::*[9]/descendant::*[1]/descendant::*[19]")
					sleep(1)
					
					# 点击拆分
					click("xpath", "//span[text()='拆分']")
					sleep(1)
					
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					sleep(1)
					
					switch_to("xpath", "//iframe[@id='splitWin-iframe']")
					
					# 选择付方账户
					click("xpath", "//input[@id='combobox-input-ourbankaccountid']")
					sleep(1)
					input("xpath", "//input[@id='combobox-input-ourbankaccountid']", "CNY")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-ourbankaccountid']")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-ourbankaccountid']")
					sleep(1)
					input_enter("xpath", "//input[@id='combobox-input-ourbankaccountid']")
					sleep(1)
					
					# 选择结算方式combobox-input-settlementmodeid
					click("xpath", "//input[@id='combobox-input-settlementmodeid']")
					sleep(1)
					input("xpath", "//input[@id='combobox-input-settlementmodeid']", "直联批量代付")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-settlementmodeid']")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-settlementmodeid']")
					sleep(1)
					input_enter("xpath", "//input[@id='combobox-input-settlementmodeid']")
					sleep(1)
					
					# 填入拆分金额
					clear("xpath", "//input[@id='splitingamount-input']")
					sleep(1)
					input("xpath", "//input[@id='splitingamount-input']", "200")
					sleep(1)
					
					# 点击保存
					click("xpath", "//span[text()='保存']")
					sleep(1)
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功!')]")
					print("付款申请,拆分成功！")
					logging.info("付款申请，拆分成功！")
					time.sleep(3)
					
					switch_to("xpath", "//iframe[@id='externalPayments-tab-iframe']")
					sleep(1)
					switch_to("xpath", "//iframe[@id='subTabOne-iframe']")
					
					# 选择合并后的第一笔数据
					click("xpath",
					      "//span[contains(text(),'Mindy自动化测试快捷付款')]/ancestor::*[9]/descendant::*[1]/descendant::*[19]")
					sleep(1)
					
					# 点击拆分
					click("xpath", "//span[text()='拆分']")
					sleep(1)
					
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					sleep(1)
					
					switch_to("xpath", "//iframe[@id='splitWin-iframe']")
					
					# 选择付方账户
					click("xpath", "//input[@id='combobox-input-ourbankaccountid']")
					sleep(1)
					input("xpath", "//input[@id='combobox-input-ourbankaccountid']", "CNY")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-ourbankaccountid']")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-ourbankaccountid']")
					sleep(1)
					input_enter("xpath", "//input[@id='combobox-input-ourbankaccountid']")
					sleep(1)
					
					# 选择结算方式combobox-input-settlementmodeid
					click("xpath", "//input[@id='combobox-input-settlementmodeid']")
					sleep(1)
					input("xpath", "//input[@id='combobox-input-settlementmodeid']", "直联批量代付")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-settlementmodeid']")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-settlementmodeid']")
					sleep(1)
					input_enter("xpath", "//input[@id='combobox-input-settlementmodeid']")
					sleep(1)
					
					# 填入拆分金额
					clear("xpath", "//input[@id='splitingamount-input']")
					sleep(1)
					input("xpath", "//input[@id='splitingamount-input']", "200")
					sleep(1)
					
					# 点击保存
					click("xpath", "//span[text()='保存']")
					sleep(1)
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功!')]")
					print("付款申请,拆分成功！")
					logging.info("付款申请，拆分成功！")
					time.sleep(3)
				
				if i == 2:
					
					# 切入付款处理的iframe窗体
					switch_to("xpath", "//iframe[@id='externalPayments-tab-iframe']")
					logging.info("开始测试快捷付款功能")
					sleep(1)
					switch_to("xpath", "//iframe[@id='subTabOne-iframe']")
				
					# 选择第一笔数据
					click("xpath", "//span[contains(text(),'Mindy自动化测试快捷付款')]/ancestor::*[9]/descendant::*[1]/descendant::*[19]")
					sleep(1)
				
					# 选择第二笔数据
					click("xpath", "//span[contains(text(),'Mindy自动化测试快捷付款')]/ancestor::*[9]/descendant::*[1]/descendant::*[27]")
					sleep(1)
			
			switch_default()
			
			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='付款处理']/child::*[1]")
			
			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//span[text()='资金系统收付']")
			# 打印操作成功日志
			print("直联单笔支付，操作成功!")
			logging.info("直联单笔支付，操作成功!")
			time.sleep(2)
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("直联单笔支付失败！" + str(traceback.format_exc()))
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