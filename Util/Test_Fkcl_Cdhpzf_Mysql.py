# encoding=utf-8
# @Time : 2020/8/14 14:49
# @Author : Mindy
# 此文件是测试MySQL版本资金结算管理--资金系统收付--付款处理--承兑汇票支付
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


class Test_Fkcl_Cdhpzf_Mysql(unittest.TestCase):
	
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
		
		# 开始测试资金系统收付--付款处理--承兑汇票支付
		# 测试付款处理--承兑汇票支付
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
				
				# 点击承兑汇票支付
				click("xpath", "//span[text()='承兑汇票支付']")
				
				# 切入‘承兑汇票支付’的iframe窗体
				switch_to("xpath", "//iframe[@id='subTabSix-iframe']")
				sleep(1)
				
				# 用JS的方法点击新增按钮
				js_click("xpath", "//span[text()='新增']")
				
				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='addWin-iframe']")
				sleep(1)
				
				# 选择交易类型
				click("xpath", "//input[@id='combobox-input-paytypeid']")
				input("xpath", "//input[@id='combobox-input-paytypeid']", "103-对外付款")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-paytypeid']")
				input_enter("xpath", "//input[@id='combobox-input-paytypeid']")
				time.sleep(1)
				
				# 选择结算方式
				click("xpath", "//input[@id='combobox-input-settlementmodeid']")
				clear("xpath", "//input[@id='combobox-input-settlementmodeid']")
				input("xpath", "//input[@id='combobox-input-settlementmodeid']", "应付承兑汇票出票")
				sleep(1)
				input_enter("xpath", "//input[@id='combobox-input-settlementmodeid']")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-settlementmodeid']")
				sleep(1)
				input_enter("xpath", "//input[@id='combobox-input-settlementmodeid']")
				time.sleep(1)
				
				# 收方名称
				click("xpath", "//input[@id='combobox-input-oppcounterpartyid']")
				sleep(1)
				input("xpath", "//input[@id='combobox-input-oppcounterpartyid']", "Mindy科技有限公司")
				sleep(1)
				
				# 点击消除下拉框
				double_click("xpath", "//span[text()='用途']")
				
				# 输入金额
				input("xpath", "//input[@id='ouramount-input']", "666")
				sleep(1)
				
				# 点击保存
				click("xpath", "//span[text()='保存']")
				
				# 退出所有iframe窗体
				switch_default()
				
				# 用隐式等待方法等页面出现提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				print("付款处理，承兑汇票支付保存成功！")
				logging.info("付款处理，承兑汇票支付保存成功！")
				sleep(3)
				
				# 第一笔，就先修改，再修改页面提交送审，再撤销送审，再删除
				if i == 1:
					# 切入‘承兑汇票支付’的iframe窗体
					switch_to("xpath", "//iframe[@id='generalPayment-tab-iframe']")
					sleep(1)
					
					# 点击承兑汇票支付
					click("xpath", "//span[text()='承兑汇票支付']")
					
					# 切入‘承兑汇票支付’的iframe窗体
					switch_to("xpath", "//iframe[@id='subTabSix-iframe']")
					sleep(1)
					
					# 点击查看
					# 用JS的方法点击放大镜
					js_click("xpath", "//span[@class='f-contrac-close']")
					sleep(1)
					
					# 输入收方名称：Mindy科技有限公司
					click("xpath", "//input[@id='oppname']")
					sleep(1)
					input("xpath", "//input[@id='oppname']", "Mindy科技有限公司")
					sleep(1)
					
					# 点击查询
					click("xpath", "//span[text()='查询']")
					
					# 修改勾选数据
					click("xpath", "//div[@title='收方名称:Mindy科技有限公司']/parent::*/preceding-sibling::*[6]/descendant::*[2]")
					
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
					print("付款处理-承兑汇票支付，修改成功！")
					logging.info("付款处理-承兑汇票支付，修改成功！")
					time.sleep(3)
					
					# 数据删除
					switch_to("xpath", "//iframe[@id='generalPayment-tab-iframe']")
					sleep(1)
					
					# 点击承兑汇票支付
					click("xpath", "//span[text()='承兑汇票支付']")
					
					# 切入‘承兑汇票支付’的iframe窗体
					switch_to("xpath", "//iframe[@id='subTabSix-iframe']")
					sleep(1)
					
					# 修改勾选数据
					click("xpath", "//div[@title='收方名称:Mindy科技有限公司']/parent::*/preceding-sibling::*[6]/descendant::*[2]")
					
					# 点击删除按钮
					click("xpath", "//span[text()='删除']")
					
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现删除的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("付款处理-承兑汇票支付，删除成功！")
					logging.info("付款处理-承兑汇票支付，删除成功！")
					time.sleep(3)
				
				if i == 2:
					
					logging.info("开始测试票据管理的页面功能")
					# 将页面的滚动条滑动到‘票据管理’页面的地方
					js_gd("xpath", "//span[contains(text(),'票据管理')]")
					# 用JS的方法点击票据管理菜单按钮
					js_click("xpath", "//span[contains(text(),'票据管理')]")
					
					# 点击承兑票据管理菜单
					click("xpath", "//span[@title='承兑汇票管理']")
					# 点击应收支票登记菜单
					click("xpath", "//span[@title='应付票据管理']")
					# 退出所有的iframe窗体
					switch_default()
					
					logging.info("开始测试应付票据管理功能")
				
					# 切入‘应付票据管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='payDraftManage-tab-iframe']")
					
					# 用JS的方法点击新增按钮
					js_click("xpath", "//span[text()='新增']")
					
					# 切入新增的iframe窗体
					switch_to("xpath", "//iframe[@id='addWin-iframe']")
					sleep(1)
					
					# 选择工程项目
					# 点击‘工程项目’框
					click("xpath", "//input[@id='combobox-input-projectitemid']")
					# 输入自动化测试工程项目，模糊查询
					input("xpath", "//input[@id='combobox-input-projectitemid']", "自动化测试工程项目")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-projectitemid']")
					input_enter("xpath", "//input[@id='combobox-input-projectitemid']")
					time.sleep(1)
					
					# 选择部门
					# 点击‘部门’框
					click("xpath", "//input[@id='combobox-input-deptid']")
					# 输入自动化测试工程项目，模糊查询
					input("xpath", "//input[@id='combobox-input-deptid']", "自动化测试部")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-deptid']")
					input_enter("xpath", "//input[@id='combobox-input-deptid']")
					time.sleep(1)
					
					# 选择票据类型，点击‘票据类型’框
					click("xpath", "//input[@id='combobox-input-drafttype']")
					input("xpath", "//input[@id='combobox-input-drafttype']", "商业承兑汇票")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-drafttype']")
					input_enter("xpath", "//input[@id='combobox-input-drafttype']")
					time.sleep(1)
					
					# 设置时间的变成存储，设置唯一性
					temp1 = time.strftime("%H%M%S")
					# 输入票据号
					click("xpath", "//span[text()='票据号']/ancestor::*[2]/descendant::*[6]/descendant::*[1]")
					sleep(1)
					input("xpath", "//span[text()='票据号']/ancestor::*[2]/descendant::*[6]/descendant::*[1]", "YFPJ" + str(temp1))
					sleep(1)
					
					# 选择开票银行账户
					click("xpath", "//span[@title='开票银行账户']/parent::*/following-sibling::*[1]/descendant::*[3]")
					# 输入收票银行账户，模糊查询
					input("xpath", "//span[@title='开票银行账户']/parent::*/following-sibling::*[1]/descendant::*[3]", "中国银行")
					sleep(1)
					input_down("xpath", "//span[@title='开票银行账户']/parent::*/following-sibling::*[1]/descendant::*[3]")
					input_enter("xpath", "//span[@title='开票银行账户']/parent::*/following-sibling::*[1]/descendant::*[3]")
					time.sleep(1)
					
					# 选择承兑方
					click("xpath", "//input[@id='acceptor']")
					# 输入收票银行账户，模糊查询
					input("xpath", "//input[@id='acceptor']", "Mindy科技有限公司承兑方")
					sleep(1)
					input_down("xpath", "//input[@id='acceptor']")
					input_enter("xpath", "//input[@id='acceptor']")
					time.sleep(1)
					
					# 选择外部收款单位
					click("xpath", "//input[@id='combobox-input-reccounterpartyid' and @class='f-combo-input f-input-bg  f-combo-input-noforceselect']")
					# 输入银行名称，通过模糊匹配搜索
					input("xpath", "//input[@id='combobox-input-reccounterpartyid' and @class='f-combo-input f-input-bg  f-combo-input-noforceselect']", "Mindy科技有限公司")
					sleep(1)
					# 模拟回车
					double_click("xpath", "//div[contains(text(),'Mindy科技有限公司')]")
					sleep(1)
					
					# 输入付款期限
					click("xpath", "//span[@title='付款期限']/ancestor::*[2]/descendant::*[8]")
					sleep(1)
					clear("xpath", "//span[@title='付款期限']/ancestor::*[2]/descendant::*[8]")
					sleep(1)
					input("xpath", "//span[@title='付款期限']/ancestor::*[2]/descendant::*[8]", "60")
					sleep(1)
					
					# 输入票面金额
					click("xpath", "//input[@id='draftamount-input']")
					sleep(1)
					clear("xpath", "//input[@id='draftamount-input']")
					sleep(1)
					input("xpath", "//input[@id='draftamount-input']", "1000")
					sleep(1)
					
					# 选择保证金担保方式
					click("xpath", "//input[@id='combobox-input-bailtype']")
					# 输入收票银行账户，模糊查询
					input("xpath", "//input[@id='combobox-input-bailtype']", "票据质押保证")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-bailtype']")
					input_enter("xpath", "//input[@id='combobox-input-bailtype']")
					time.sleep(1)
					
					# 选择抵质押物
					click("xpath", "//input[@id='combobox-input-collateralsid']")
					# 输入收票银行账户，模糊查询
					input("xpath", "//input[@id='combobox-input-collateralsid']", "抵押01")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-collateralsid']")
					input_enter("xpath", "//input[@id='combobox-input-collateralsid']")
					time.sleep(1)
					
					# 描述框中填入值
					input("xpath", "//textarea[@id='description']", "自动化测试应付票据描述框")
					sleep(1)
					
					# 点击保存按钮
					click("xpath", "//span[text()='保存']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("应付票据管理，保存成功！")
					logging.info("应付票据管理，保存成功！")
					time.sleep(3)
				
					# 审核
					# 切入‘应付票据管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='payDraftManage-tab-iframe']")

					# 点击查看
					# 用JS的方法点击放大镜
					js_click("xpath", "//span[@class='f-contrac-close']")
					sleep(1)

					# 输入支票号：YFPJ
					input("xpath", "//input[@id='draftcode']", "YFPJ")
					sleep(1)

					# 点击查询
					click("xpath", "//span[text()='查询']")

					# 勾选
					click("xpath", "//div[contains(text(),'YFPJ')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 点击审核按钮
					click("xpath", "//span[text()='审核']")

					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("应付票据管理，审核成功！")
					logging.info("应付票据管理，审核成功！")
					time.sleep(3)
					
					# 用JS的方法关闭当前页面
					js_click("xpath", "//a[@title='应付票据管理']/child::*[1]")
					
					# 再次点击基础设置菜单，使之关闭
					click("xpath", "//span[@title='承兑汇票管理']")
					
					# 打印操作成功日志
					print("应付票据管理，操作成功!")
					logging.info("应付票据管理，操作成功!")
					time.sleep(2)
			
					logging.info("开始测试资金结算管理的页面功能")
					# 将页面的滚动条滑动到‘资金结算管理’页面的地方
					js_gd("xpath", "//span[contains(text(),'资金结算管理')]")
					# 用JS的方法点击资金结算管理菜单按钮
					js_click("xpath", "//span[contains(text(),'资金结算管理')]")
					
					# 点击'资金系统收付'菜单
					js_click("xpath", "//span[text()='资金系统收付']")
					sleep(1)
					# 点击付款处理菜单
					js_click("xpath", "//span[text()='付款处理']")
					# 退出所有iframe窗体
					switch_default()
					
					# 切入‘承兑汇票支付’的iframe窗体
					switch_to("xpath", "//iframe[@id='generalPayment-tab-iframe']")
					sleep(1)
					
					# 点击承兑汇票支付
					click("xpath", "//span[text()='承兑汇票支付']")
					
					# 切入‘承兑汇票支付’的iframe窗体
					switch_to("xpath", "//iframe[@id='subTabSix-iframe']")
					sleep(1)
					
					# 修改勾选数据
					click("xpath",  "//div[@title='收方名称:Mindy科技有限公司']/parent::*/preceding-sibling::*[6]/descendant::*[2]")
					
					# 点击审核按钮
					click("xpath", "//span[text()='送审']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！送审成功1笔，失败0笔。')]")
					print("付款处理-承兑汇票支付，送审成功！")
					logging.info("付款处理-承兑汇票支付，送审成功！")
					time.sleep(3)
					
					switch_to("xpath", "//iframe[@id='generalPayment-tab-iframe']")
					sleep(1)
					
					# 点击承兑汇票支付
					click("xpath", "//span[text()='承兑汇票支付']")
					
					# 切入‘支票支付’的iframe窗体
					switch_to("xpath", "//iframe[@id='subTabSix-iframe']")
					sleep(1)
					
					# 修改勾选数据
					click("xpath", "//div[@title='收方名称:Mindy科技有限公司']/parent::*/preceding-sibling::*[6]/descendant::*[2]")
					
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
					print("付款处理-承兑汇票支付，撤销送审成功！")
					logging.info("付款处理-承兑汇票支付，撤销送审成功！")
					time.sleep(3)

					# 切入‘承兑汇票支付’的iframe窗体
					switch_to("xpath", "//iframe[@id='generalPayment-tab-iframe']")
					sleep(1)
					
					# 点击承兑汇票支付
					click("xpath", "//span[text()='承兑汇票支付']")
					
					# 切入‘支票支付’的iframe窗体
					switch_to("xpath", "//iframe[@id='subTabSix-iframe']")
					sleep(1)
					
					# 修改勾选数据
					click("xpath", "//div[@title='收方名称:Mindy科技有限公司']/parent::*/preceding-sibling::*[6]/descendant::*[2]")
					
					# 点击审核按钮
					click("xpath", "//span[text()='送审']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！送审成功1笔，失败0笔。')]")
					print("付款处理-承兑汇票支付，送审成功！")
					logging.info("付款处理-承兑汇票支付，送审成功！")
					time.sleep(3)
					
					# 切入‘承兑汇票支付’的iframe窗体
					switch_to("xpath", "//iframe[@id='generalPayment-tab-iframe']")
					sleep(1)
					
					# 点击承兑汇票支付
					click("xpath", "//span[text()='承兑汇票支付']")
					
					# 切入‘支票支付’的iframe窗体
					switch_to("xpath", "//iframe[@id='subTabSix-iframe']")
					sleep(1)
					
					# 修改勾选数据
					double_click("xpath", "//div[@title='收方名称:Mindy科技有限公司']/parent::*/preceding-sibling::*[6]/descendant::*[2]")
					sleep(1)
					
					switch_to("xpath", "//iframe[@id='wf_taskProcessing_win-iframe']")
					sleep(1)
					
					click("xpath", "//span[text()='同意']")
					sleep(1)
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("承兑汇票支付，审批成功！")
					logging.info("承兑汇票支付，审批成功！")
					time.sleep(3)
					
					# 点击领票/开票
					# 切入‘承兑汇票支付’的iframe窗体
					switch_to("xpath", "//iframe[@id='generalPayment-tab-iframe']")
					sleep(1)
					
					# 点击承兑汇票支付
					click("xpath", "//span[text()='承兑汇票支付']")
					
					# 切入‘承兑汇票支付’的iframe窗体
					switch_to("xpath", "//iframe[@id='subTabSix-iframe']")
					sleep(1)
					
					# 勾选数据
					click("xpath", "//div[@title='收方名称:Mindy科技有限公司']/parent::*/preceding-sibling::*[6]/descendant::*[2]")
					sleep(1)
					
					click("xpath", "//span[text()='领票/开票']")
					sleep(1)
					
					switch_to("xpath", "//iframe[@id='payWin-iframe']")
					sleep(1)
					
					# 勾选数据
					click("xpath", "//div[@title='外部收款单位:Mindy科技有限公司']/parent::*/preceding-sibling::*[7]/descendant::*[2]")
					sleep(1)
					
					click("xpath", "//span[text()='出票']")
					sleep(1)
					
					# 点击进入出票详情页面
					switch_to("xpath", "//iframe[@id='sendWin-iframe']")
					
					# 点击出票
					click("xpath", "//span[text()='出票' and @class='f-new-btn-text save_icon']")
					sleep(1)
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("直联单笔支付，收付失败！")
					logging.info("直联单笔支付，收付失败！")
					time.sleep(3)
					
					# 切入‘承兑汇票支付’的iframe窗体
					switch_to("xpath", "//iframe[@id='generalPayment-tab-iframe']")
					sleep(1)
					
					# 点击承兑汇票支付
					click("xpath", "//span[text()='承兑汇票支付']")
					
					# 切入‘支票支付’的iframe窗体
					switch_to("xpath", "//iframe[@id='subTabSix-iframe']")
					sleep(1)
					
					# 确认支付
					# 勾选数据
					click("xpath", "//div[@title='收方名称:Mindy科技有限公司']/parent::*/preceding-sibling::*[6]/descendant::*[2]")
					sleep(1)
					
					# 点击‘支付’按钮
					click("xpath", "//span[text()='确认支付']")
					sleep(1)
					
					# 点击确定按钮
					click("xpath", "//span[text()='确定']")
					sleep(1)
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！1笔进行了确认支付，0笔不允许确认支付。')]")
					print("承兑汇票支付，确认支付成功！")
					logging.info("承兑汇票支付，确认支付成功！")
					time.sleep(3)
				
					# 打印
					# 切入‘承兑汇票支付’的iframe窗体
					switch_to("xpath", "//iframe[@id='generalPayment-tab-iframe']")
					sleep(1)
					
					# 点击承兑汇票支付
					click("xpath", "//span[text()='承兑汇票支付']")
					
					# 切入‘支票支付’的iframe窗体
					switch_to("xpath", "//iframe[@id='subTabSix-iframe']")
					sleep(1)
					
					# 勾选数据
					click("xpath", "//div[@title='收方名称:Mindy科技有限公司']/parent::*/preceding-sibling::*[6]/descendant::*[2]")
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
							print("承兑汇票支付，打印成功!！")
							time.sleep(3)
							self.driver.switch_to.window(now_handle)
							switch_default()
					
					# 打印-打印记录
					# 切入‘承兑汇票支付’的iframe窗体
					switch_to("xpath", "//iframe[@id='generalPayment-tab-iframe']")
					sleep(1)
					
					# 点击承兑汇票支付
					click("xpath", "//span[text()='承兑汇票支付']")
					
					# 切入‘支票支付’的iframe窗体
					switch_to("xpath", "//iframe[@id='subTabSix-iframe']")
					sleep(1)
					
					# # 勾选数据
					# click("xpath", "//div[@title='收方名称:Mindy科技有限公司']/parent::*/preceding-sibling::*[6]/descendant::*[2]")
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
					print("承兑汇票支付，打印记录查看成功！")
					logging.info("承兑汇票支付，打印记录查看成功！")
					time.sleep(3)
					
					switch_parent()
					
					# 点击关闭页面
					click("xpath", "//span[text()='打印记录']/preceding-sibling::*[1]")
					sleep(1)
					
					switch_default()
					
					# 关联票据查看
					# 切入‘承兑汇票支付’的iframe窗体
					switch_to("xpath", "//iframe[@id='generalPayment-tab-iframe']")
					sleep(1)
					
					# 点击承兑汇票支付
					click("xpath", "//span[text()='承兑汇票支付']")
					
					# 切入‘承兑汇票查看’的iframe窗体
					switch_to("xpath", "//iframe[@id='subTabSix-iframe']")
					sleep(1)
					
					# # 勾选数据
					# click("xpath", "//div[@title='收方名称:Mindy科技有限公司']/parent::*/preceding-sibling::*[6]/descendant::*[2]")
					# sleep(1)
					
					# 点击关联票据查看
					click("xpath", "//span[text()='关联票据查看']")
					sleep(1)
					
					# 进入关联票据查看的窗体
					switch_to("xpath", "//iframe[@id='draftViewWin-iframe']")
					sleep(1)
					
					# 用隐式等待方法等页面出现  承兑方:Mindy科技有限公司承兑方
					implici_wait("xpath", "//div[@title='承兑方:Mindy科技有限公司承兑方']")
					print("承兑汇票支付，打印记录查看成功！")
					logging.info("承兑汇票支付，打印记录查看成功！")
					time.sleep(3)
					
					switch_parent()
					
					# 点击关闭页面
					click("xpath", "//span[text()='关联票据查看']/preceding-sibling::*[1]")
					sleep(1)
					
					switch_default()
				
			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='付款处理']/child::*[1]")
			
			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//span[text()='资金系统收付']")
			# 打印操作成功日志
			print("承兑汇票支付，操作成功!")
			logging.info("承兑汇票支付，操作成功!")
			time.sleep(2)
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("承兑汇票支付失败！" + str(traceback.format_exc()))
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
