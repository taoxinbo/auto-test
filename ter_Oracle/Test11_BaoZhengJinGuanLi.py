# encoding=utf-8
# @Time : 2020/9/4 11:51
# @Author : Mindy
# 此文件是测试保证金管理页面功能
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

# print("开始时间：",time.strftime("%Y-%m-%d %H:%M:%S"))

driver = ""


@pytest.mark.flaky(reruns=pytest_flaky, reruns_delay=10)
class Test_Bzjgl(unittest.TestCase):
	
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
		# login( G_Mys_Url,TestUser,Password, "自动化测试租户")
		# login(G_Mys_Url, Tao, Password, "默认租户")
		login(G_Ora_Url, mindy, Password, "亚唐科技")
		# login(G_Mys_Url, judy, Password, "默认租户")
		
		logging.info("开始测试保证金管理的页面功能")
		# 将页面的滚动条滑动到‘保证金管理’页面的地方
		js_gd("xpath", "//span[contains(text(),'资金计划填报')]/ancestor::*[1]/preceding-sibling::*[2]/descendant::*[3]")
		# 用JS的方法点击保证金管理菜单按钮
		js_click("xpath", "//span[contains(text(),'资金计划填报')]/ancestor::*[1]/preceding-sibling::*[2]/descendant::*[3]")
		
		# 系统参数--利率方案
		try:
			# 点击系统设置
			click("xpath", "//div[@class='sysconfigset']")
			
			# 点击进入系统设置页面
			switch_to("xpath", "//iframe[@id='systemconfig-tab-iframe']")
			sleep(1)
			
			logging.info("开始测试基础资料--利率方案功能")
			# 将页面的滚动条滑动到‘利率方案’页面的地方
			js_gd("xpath", "//span[contains(text(),'利率方案')]")
			# 用JS的方法利率方案字段菜单按钮
			js_click("xpath", "//span[contains(text(),'利率方案')]")
			
			switch_default()
			
			switch_to("xpath", "//iframe[@id='interestRateSchemes-tab-iframe']")
			
			# 用JS的方法点击新增按钮
			js_click("xpath", "//span[text()='新增']")
			
			# 切入新增的iframe窗体
			switch_to("xpath", "//iframe[@id='addWin-iframe']")
			sleep(1)
			
			# 输入代码
			input("xpath", "//input[@name='code']", "L04")
			sleep(1)
			
			# 输入名称
			input("xpath", "//input[@id='name']", "保证金存入")
			sleep(1)
			# 单据对象
			click("xpath", "//input[@id='combobox-input-noteobjectid']")
			sleep(1)
			input("xpath", "//input[@id='combobox-input-noteobjectid']", "保证金存入")
			sleep(1)
			input_enter("xpath", "//input[@id='combobox-input-noteobjectid']")
			sleep(1)
			input_down("xpath", "//input[@id='combobox-input-noteobjectid']")
			sleep(1)
			input_enter("xpath", "//input[@id='combobox-input-noteobjectid']")
			sleep(1)
			# 利率类型
			click("xpath", "//input[@id='combobox-input-interestratetypeid']")
			sleep(1)
			input("xpath", "//input[@id='combobox-input-interestratetypeid']", "固定利率")
			sleep(1)
			input_enter("xpath", "//input[@id='combobox-input-interestratetypeid']")
			sleep(1)
			input_down("xpath", "//input[@id='combobox-input-interestratetypeid']")
			sleep(1)
			input_enter("xpath", "//input[@id='combobox-input-interestratetypeid']")
			sleep(1)
			
			# 共享模式combobox-input-includemode
			click("xpath", "//input[@id='combobox-input-includemode']")
			sleep(1)
			input("xpath", "//input[@id='combobox-input-includemode']", "下属组织共享")
			sleep(1)
			input_enter("xpath", "//input[@id='combobox-input-includemode']")
			sleep(1)
			input_down("xpath", "//input[@id='combobox-input-includemode']")
			sleep(1)
			input_enter("xpath", "//input[@id='combobox-input-includemode']")
			sleep(1)
			
			# 点击保存按钮
			click("xpath", "//span[text()='保存']")
			
			# 退出所有iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("利率方案，保存成功！")
			time.sleep(3)
			
			# 再次点击基础设置菜单，使之关闭
			# 用JS的方法关闭当前页面
			
			js_click("xpath", "//a[@title='利率方案']/child::*[1]")
			
			# 打印操作成功日志
			print("利率方案，操作成功!")
			logging.info("利率方案，操作成功!")
			time.sleep(2)
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("利率方案,失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		
		# 系统参数--利率
		try:
			# 点击系统设置
			click("xpath", "//div[@class='sysconfigset']")
			
			# 点击进入系统设置页面
			switch_to("xpath", "//iframe[@id='systemconfig-tab-iframe']")
			sleep(1)
			
			logging.info("开始测试基础资料--利率功能")
			# 将页面的滚动条滑动到‘利率’页面的地方
			js_gd("xpath", "//span[contains(text(),'利率')]")
			# 用JS的方法利率字段菜单按钮
			js_click("xpath", "//span[contains(text(),'利率')]")
			
			switch_default()
			
			switch_to("xpath", "//iframe[@id='interestRateValues-tab-iframe']")
			switch_to("xpath", "//iframe[@id='subTabOne-iframe']")
			
			# 勾选数据
			click("xpath", "//div[@title='利率类型:固定利率']/parent::*[1]/preceding-sibling::*[1]/descendant::*[2]")
			sleep(1)
			
			# 点击修改按钮
			click("xpath", "//span[text()='修改']")
			sleep(1)
			
			# 切入新增的iframe窗体
			switch_to("xpath", "//iframe[@id='modWin-iframe']")
			sleep(1)
			
			# 修改利率
			clear("xpath", "//input[@id='rate-input']")
			sleep(1)
			input("xpath", "//input[@id='rate-input']", "4")
			sleep(1)
			
			# 点击保存按钮
			click("xpath", "//span[text()='保存']")
			
			# 退出所有iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("利率，保存成功！")
			time.sleep(3)
			
			# 再次点击基础设置菜单，使之关闭
			# 用JS的方法关闭当前页面
			
			js_click("xpath", "//a[@title='利率']/child::*[1]")
			
			# 打印操作成功日志
			print("利率，操作成功!")
			logging.info("利率，操作成功!")
			time.sleep(2)
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("利率,失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		# 测试保证金管理
		try:
			# 点击保证金管理菜单
			click("xpath", "//span[@title='保证金管理']")
			# 退出所有的iframe窗体
			switch_default()
			logging.info("开始测试保证金管理功能")
			for i in range(1, 6):
				# 切入‘保证金管理’的iframe窗体
				switch_to("xpath", "//iframe[@id='margin-tab-iframe']")
				# 用JS的方法点击新增按钮
				js_click("xpath", "//span[text()='存入']")
				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='modWin-iframe']")
				sleep(1)
				
				# 选择金融机构
				# 点击‘金融机构’框
				click("xpath", "//input[@id='combobox-input-bankid']")
				# 输入自动化测试部，模糊查询
				input("xpath", "//input[@id='combobox-input-bankid']", "中国银行")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-bankid']")
				input_enter("xpath", "//input[@id='combobox-input-bankid']")
				time.sleep(1)
				
				# 选择金融机构网点
				# 点击‘金融机构网点’框
				click("xpath", "//input[@id='combobox-input-banklocationid']")
				# 输入自动化测试部，模糊查询
				input("xpath", "//input[@id='combobox-input-banklocationid']", "大连泡崖街支行")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-banklocationid']")
				input_enter("xpath", "//input[@id='combobox-input-banklocationid']")
				time.sleep(1)
				
				# 输入银行，通过模糊匹配搜索
				click("xpath", "//input[@id='combobox-input-accountid']")
				sleep(1)
				input("xpath", "//input[@id='combobox-input-accountid']", "CNY")
				sleep(1)
				# 模拟回车
				double_click("xpath", "//div[contains(text(),'CNY')]")
				sleep(1)
				
				# 保证金类型
				if i == 1:
					# 保证金类型
					click("xpath", "//input[@id='combobox-input-margintype']")
					# 输入信用证类型，模糊查询
					input("xpath", "//input[@id='combobox-input-margintype']", "活期")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-margintype']")
					input_enter("xpath", "//input[@id='combobox-input-margintype']")
					time.sleep(1)
				else:
					# 保证金类型
					click("xpath", "//input[@id='combobox-input-margintype']")
					# 输入信用证类型，模糊查询
					input("xpath", "//input[@id='combobox-input-margintype']", "定期")
					sleep(1)
					input_down("xpath", "//input[@id='combobox-input-margintype']")
					input_enter("xpath", "//input[@id='combobox-input-margintype']")
					time.sleep(1)
				
				# 输入金额
				click("xpath", "//input[@id='amount-input']")
				sleep(1)
				clear("xpath", "//input[@id='amount-input']")
				sleep(1)
				input("xpath", "//input[@id='amount-input']", "600000")
				sleep(1)
				
				if i == 1:
					# 开始日期
					today = date.today()
					begindate = today - timedelta(days=20)
					click("xpath", "//input[@id='begindate-input']")
					sleep(1)
					input("xpath", "//input[@id='begindate-input']", str(begindate))
					# 模拟回车键
					keyDown('enter')
					keyUp('enter')
					time.sleep(1)
					
					# 截止日期
					today = date.today()
					enddate = today + timedelta(days=60)
					click("xpath", "//input[@id='enddate-input']")
					sleep(1)
					input("xpath", "//input[@id='enddate-input']", str(enddate))
					# 模拟回车键
					keyDown('enter')
					keyUp('enter')
					time.sleep(1)
				
				if i == 2:
					# 开始日期
					today = date.today()
					begindate = today - timedelta(days=20)
					click("xpath", "//input[@id='begindate-input']")
					sleep(1)
					input("xpath", "//input[@id='begindate-input']", str(begindate))
					# 模拟回车键
					keyDown('enter')
					keyUp('enter')
					time.sleep(1)
					
					# 截止日期
					today = date.today()
					enddate = today + timedelta(days=60)
					click("xpath", "//input[@id='enddate-input']")
					sleep(1)
					input("xpath", "//input[@id='enddate-input']", str(enddate))
					# 模拟回车键
					keyDown('enter')
					keyUp('enter')
					time.sleep(1)
				
				if i == 3:
					# 开始日期
					today = date.today()
					begindate = today - timedelta(days=10)
					click("xpath", "//input[@id='begindate-input']")
					sleep(1)
					input("xpath", "//input[@id='begindate-input']", str(begindate))
					# 模拟回车键
					keyDown('enter')
					keyUp('enter')
					time.sleep(1)
					
					# 截止日期
					today = date.today()
					enddate = today + timedelta(days=30)
					click("xpath", "//input[@id='enddate-input']")
					sleep(1)
					input("xpath", "//input[@id='enddate-input']", str(enddate))
					# 模拟回车键
					keyDown('enter')
					keyUp('enter')
					time.sleep(1)
				
				if i == 4:
					# 开始日期
					today = date.today()
					begindate = today - timedelta(days=30)
					click("xpath", "//input[@id='begindate-input']")
					sleep(1)
					input("xpath", "//input[@id='begindate-input']", str(begindate))
					# 模拟回车键
					keyDown('enter')
					keyUp('enter')
					time.sleep(1)
					
					# 截止日期
					today = date.today()
					enddate = today - timedelta(days=10)
					click("xpath", "//input[@id='enddate-input']")
					sleep(1)
					input("xpath", "//input[@id='enddate-input']", str(enddate))
					# 模拟回车键
					keyDown('enter')
					keyUp('enter')
					time.sleep(1)
				
				if i == 5:
					# 开始日期
					today = date.today()
					begindate = today - timedelta(days=30)
					click("xpath", "//input[@id='begindate-input']")
					sleep(1)
					input("xpath", "//input[@id='begindate-input']", str(begindate))
					# 模拟回车键
					keyDown('enter')
					keyUp('enter')
					time.sleep(1)
					
					# 截止日期
					today = date.today()
					enddate = today - timedelta(days=10)
					click("xpath", "//input[@id='enddate-input']")
					sleep(1)
					input("xpath", "//input[@id='enddate-input']", str(enddate))
					# 模拟回车键
					keyDown('enter')
					keyUp('enter')
					time.sleep(1)
				
				# 存入用途
				input("xpath", "//input[@id='useage']", "自动化测试存入用途")
				sleep(1)
				
				# 计息方式中输入值
				# 点击计息方式插页
				# 1、选择还本方式
				click("xpath", "//input[@id='combobox-input-interestmode']")
				# 按键往下，选择‘按季还款’
				input_down("xpath", "//input[@id='combobox-input-interestmode']")
				input_enter("xpath", "//input[@id='combobox-input-interestmode']")
				time.sleep(1)
				
				# 2、选择利率方案
				click("xpath", "//input[@id='combobox-input-interestrateschemeid']")
				# 按键往下，选择利率方案
				sleep(2)
				input_down("xpath", "//input[@id='combobox-input-interestrateschemeid']")
				input_enter("xpath", "//input[@id='combobox-input-interestrateschemeid']")
				sleep(1)
				
				# 3、选择浮动方式
				click("xpath", "//input[@id='combobox-input-interestratefloattype']")
				# 按键往下，选择利率方案
				sleep(2)
				input_down("xpath", "//input[@id='combobox-input-interestratefloattype']")
				input_enter("xpath", "//input[@id='combobox-input-interestratefloattype']")
				sleep(1)
				
				# 点击保存按钮
				click("xpath", "//span[text()='保存']")
				
				# 退出所有iframe窗体
				switch_default()
				
				# 用隐式等待方法等页面出现提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				print("保证金管理第%s次，保存成功！" % i)
				logging.info("保证金管理第%s次，保存成功！" % i)
				time.sleep(3)
				
				# 第一笔，就先修改，再删除新建的‘保证金管理’
				if i == 1:
					# 切入‘委托方保函管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='margin-tab-iframe']")
					
					# 点击查看
					# 用JS的方法点击放大镜
					js_click("xpath", "//span[@class='f-contrac-close']")
					sleep(1)
					
					# 输入支票号：BZJ
					input("xpath", "//input[@id='notecode']", "BZJ")
					sleep(1)
					
					# 点击查询
					click("xpath", "//span[text()='查询']")
					
					# 修改 #勾选
					click("xpath", "//div[contains(text(),'BZJ')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")
					
					# 点击修改按钮
					js_click("xpath", "//span[text()='修改']")
					sleep(1)
					
					# 切入修改的iframe窗体
					switch_to("xpath", "//iframe[@id='modWin-iframe']")
					sleep(1)
					
					# 填写描述
					click("xpath", "//textarea[@id='description']")
					sleep(1)
					input("xpath", "//textarea[@id='description']", "自动化修改保证金描述框")
					sleep(1)
					
					# 点击保存按钮
					click("xpath", "//span[text()='保存']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("保证金管理，修改成功！")
					logging.info("保证金管理，修改成功！")
					time.sleep(3)
					
					# 切入‘委托方保函管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='margin-tab-iframe']")
					
					# 勾选
					click("xpath", "//div[contains(text(),'BZJ')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")
					
					# 点击删除按钮
					click("xpath", "//span[text()='支付']")
					
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现删除的提示框
					implici_wait("xpath", "//span[contains(text(),'成功支付保证金1笔！')]")
					print("保证金管理，支付成功！")
					logging.info("保证金管理，支付成功！")
					time.sleep(3)
					
					# 切入‘保证金管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='margin-tab-iframe']")
					
					# 勾选
					click("xpath", "//div[contains(text(),'BZJ')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")
					
					# 用JS方便点击‘审核’按钮旁边的倒三角形
					js_click("xpath", "//span[text()='支付']/parent::*/following-sibling::*/child::*")
					sleep(1)
					
					# 点击取消审核按钮
					js_click("xpath", "//a[contains(text(),'取消支付')]")
					sleep(1)
					
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现删除的提示框
					implici_wait("xpath", "//span[contains(text(),'成功取消支付保证金1笔！')]")
					print("保证金管理，取消支付成功！")
					logging.info("保证金管理，取消支付成功！")
					time.sleep(3)
					
					# 切入‘保证金管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='margin-tab-iframe']")
					
					# 勾选
					click("xpath", "//div[contains(text(),'BZJ')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")
					
					# 点击删除按钮
					click("xpath", "//span[text()='删除']")
					
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现删除的提示框
					implici_wait("xpath", "//span[contains(text(),'成功删除1条记录！')]")
					print("保证金管理，删除成功！")
					logging.info("保证金管理，删除成功！")
					time.sleep(3)
				
				# 第二笔，先审核、再取消审核、再托收、再托收到账
				if i == 2:
					# 切入‘委托方保函管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='margin-tab-iframe']")
					
					# 勾选
					click("xpath", "//div[contains(text(),'BZJ')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")
					
					# 点击审核按钮
					click("xpath", "//span[text()='支付']")
					
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现删除的提示框
					implici_wait("xpath", "//span[contains(text(),'成功支付保证金1笔！')]")
					print("保证金管理，支付成功！")
					logging.info("保证金管理，支付成功！")
					time.sleep(3)
					
					# 支付后支取
					# 切入‘保证金管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='margin-tab-iframe']")
					
					# 勾选
					click("xpath", "//div[contains(text(),'BZJ')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")
					
					# 点击审核按钮
					js_click("xpath", "//span[text()='支取']")
					
					switch_to("xpath", "//iframe[@id='drawWin-iframe']")
					sleep(1)
					
					# 支取日期
					today = date.today()
					due_date = today + timedelta(days=30)
					click("xpath", "//input[@id='operatedate-input']")
					sleep(1)
					clear("xpath", "//input[@id='operatedate-input']")
					sleep(1)
					input("xpath", "//input[@id='operatedate-input']", str(due_date))
					# 模拟回车键
					# keyDown('enter')
					# keyUp('enter')
					time.sleep(1)
					
					# 点击审核按钮
					click("xpath", "//span[text()='保存']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("保证金管理，支取成功！")
					logging.info("保证金管理，支取成功！")
					time.sleep(3)
				
				if i == 3:
					# 切入‘委托方保函管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='margin-tab-iframe']")
					
					# 勾选
					click("xpath", "//div[contains(text(),'BZJ')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")
					
					# 点击审核按钮
					click("xpath", "//span[text()='支付']")
					
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现删除的提示框
					implici_wait("xpath", "//span[contains(text(),'成功支付保证金1笔！')]")
					print("保证金管理，支付成功！")
					logging.info("保证金管理，支付成功！")
					time.sleep(3)
					
					# 结息
					# 切入‘保证金管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='margin-tab-iframe']")
					
					# 勾选
					click("xpath", "//div[contains(text(),'BZJ')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")
					
					# 点击审核按钮
					js_click("xpath", "//span[text()='结息']")
					sleep(1)
					
					switch_to("xpath", "//iframe[@id='interestsettleWin-iframe']")
					sleep(1)
					
					# 结息日期
					today = date.today()
					due_date = today + timedelta(days=30)
					click("xpath", "//input[@id='operatedate-input']")
					sleep(1)
					clear("xpath", "//input[@id='operatedate-input']")
					sleep(1)
					input("xpath", "//input[@id='operatedate-input']", str(due_date))
					# 模拟回车键
					# keyDown('enter')
					# keyUp('enter')
					time.sleep(1)
					
					# 金额
					click("xpath", "//input[@id='amount-input']")
					sleep(1)
					clear("xpath", "//input[@id='amount-input']")
					sleep(1)
					input("xpath", "//input[@id='amount-input']", "100")
					sleep(1)
					
					# 描述中填入值
					input("xpath", "//textarea[@id='description']", "自动化测试保证金结息描述框")
					sleep(1)
					
					# 点击审核按钮
					click("xpath", "//span[text()='保存']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("保证金管理，结息成功！")
					logging.info("保证金管理，结息成功！")
					time.sleep(3)
					
					# 取消结息
					# 切入‘保证金管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='margin-tab-iframe']")
					
					# 勾选
					click("xpath", "//div[contains(text(),'BZJ')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")
					
					# 用JS方便点击‘审核’按钮旁边的倒三角形
					js_click("xpath", "//span[text()='结息']/parent::*/following-sibling::*/child::*")
					sleep(1)
					
					# 点击取消审核按钮cancelinterestsettleWin-iframe
					js_click("xpath", "//a[contains(text(),'取消结息')]")
					sleep(1)
					
					switch_to("xpath", "//iframe[@id='cancelinterestsettleWin-iframe']")
					
					click("xpath", "//div[@title='金额:100.00']/parent::*/preceding-sibling::*[2]/descendant::*[2]")
					sleep(1)
					
					click("xpath", "//span[text()='取消结息']")
					sleep(1)
					
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					sleep(1)
					
					# # 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现删除的提示框
					implici_wait("xpath", "//span[contains(text(),'成功取消保证金结息1笔')]")
					print("保证金管理，取消结息成功！")
					logging.info("保证金管理，取消结息成功！")
					time.sleep(3)
					
					switch_to("xpath", "//iframe[@id='margin-tab-iframe']")
					sleep(1)
					
					click("xpath", "//span[text()='取消结息']/parent::*/descendant::*[1]")
					sleep(1)
					
					switch_default()
					
					# 利息试算trailWin-iframe
					
					# 结息
					# 切入‘保证金管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='margin-tab-iframe']")
					
					# # 勾选
					# click("xpath", "//div[contains(text(),'BZJ')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")
					# sleep(1)
					
					# 点击审核按钮
					js_click("xpath", "//span[text()='利息试算']")
					sleep(1)
					
					switch_to("xpath", "//iframe[@id='trailWin-iframe']")
					sleep(1)
					
					# 结息日期
					today = date.today()
					due_date = today
					click("xpath", "//input[@id='calculatedate-input']")
					sleep(1)
					clear("xpath", "//input[@id='calculatedate-input']")
					sleep(1)
					input("xpath", "//input[@id='calculatedate-input']", str(due_date))
					# 模拟回车键
					# keyDown('enter')
					# keyUp('enter')
					time.sleep(1)
					
					# 点击试算按钮
					click("xpath", "//span[text()='试算']")
					sleep(1)
					
					print("保证金管理，利息试算成功！")
					logging.info("保证金管理，利息试算成功！")
					
					# 点击取消按钮
					click("xpath", "//span[text()='取消']")
					sleep(1)
					
					# 退出所有iframe窗体
					switch_default()
				
				if i == 4:
					# 切入‘保证金管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='margin-tab-iframe']")
					
					# 勾选
					click("xpath", "//div[contains(text(),'BZJ')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")
					
					# 点击审核按钮
					click("xpath", "//span[text()='支付']")
					
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现删除的提示框
					implici_wait("xpath", "//span[contains(text(),'成功支付保证金1笔！')]")
					print("保证金管理，支付成功！")
					logging.info("保证金管理，支付成功！")
					time.sleep(3)
					
					# 结息
					# 切入‘保证金管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='margin-tab-iframe']")
					
					# 勾选
					click("xpath", "//div[contains(text(),'BZJ')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")
					
					# 用JS方便点击‘到期转存’按钮旁边的倒三角形
					js_click("xpath", "//span[text()='到期转存']/parent::*/following-sibling::*/child::*")
					sleep(1)
					
					# 点击取消审核按钮cancelinterestsettleWin-iframe
					js_click("xpath", "//a[contains(text(),'本金转存')]")
					sleep(1)
					
					switch_to("xpath", "//iframe[@id='modWin-iframe']")
					sleep(1)
					
					# 开始日期
					today = date.today()
					begin_date = today + timedelta(days=30)
					click("xpath", "//input[@id='begindate-input']")
					sleep(1)
					clear("xpath", "//input[@id='begindate-input']")
					sleep(1)
					input("xpath", "//input[@id='begindate-input']", str(begin_date))
					# 模拟回车键
					# keyDown('enter')
					# keyUp('enter')
					time.sleep(1)
					
					# 截止日期
					today = date.today()
					end_date = today + timedelta(days=30)
					click("xpath", "//input[@id='enddate-input']")
					sleep(1)
					clear("xpath", "//input[@id='enddate-input']")
					sleep(1)
					input("xpath", "//input[@id='enddate-input']", str(end_date))
					# 模拟回车键
					# keyDown('enter')
					# keyUp('enter')
					time.sleep(1)
					
					# 描述中填入值
					input("xpath", "//textarea[@id='description']", "自动化测试保证金本金转存描述框")
					sleep(1)
					
					# 点击审核按钮
					click("xpath", "//span[text()='保存']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("保证金管理，本金转存成功！")
					logging.info("保证金管理，本金转存成功！")
					time.sleep(3)
				
				if i == 5:
					# 切入‘保证金管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='margin-tab-iframe']")
					
					# 勾选
					click("xpath", "//div[contains(text(),'BZJ')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")
					
					# 点击审核按钮
					click("xpath", "//span[text()='支付']")
					
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现删除的提示框
					implici_wait("xpath", "//span[contains(text(),'成功支付保证金1笔！')]")
					print("保证金管理，支付成功！")
					logging.info("保证金管理，支付成功！")
					time.sleep(3)
					
					# 结息
					# 切入‘保证金管理’的iframe窗体
					switch_to("xpath", "//iframe[@id='margin-tab-iframe']")
					
					# 勾选
					click("xpath", "//div[contains(text(),'BZJ')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")
					
					# 用JS方便点击‘到期转存’按钮旁边的倒三角形
					js_click("xpath", "//span[text()='到期转存']/parent::*/following-sibling::*/child::*")
					sleep(1)
					
					# 点击取消审核按钮cancelinterestsettleWin-iframe
					js_click("xpath", "//a[contains(text(),'本息转存')]")
					sleep(1)
					
					switch_to("xpath", "//iframe[@id='modWin-iframe']")
					sleep(1)
					
					# 开始日期
					today = date.today()
					begin_date = today + timedelta(days=30)
					click("xpath", "//input[@id='begindate-input']")
					sleep(1)
					clear("xpath", "//input[@id='begindate-input']")
					sleep(1)
					input("xpath", "//input[@id='begindate-input']", str(begin_date))
					# 模拟回车键
					# keyDown('enter')
					# keyUp('enter')
					time.sleep(1)
					
					# 截止日期
					today = date.today()
					end_date = today + timedelta(days=30)
					click("xpath", "//input[@id='enddate-input']")
					sleep(1)
					clear("xpath", "//input[@id='enddate-input']")
					sleep(1)
					input("xpath", "//input[@id='enddate-input']", str(end_date))
					# 模拟回车键
					# keyDown('enter')
					# keyUp('enter')
					time.sleep(1)
					
					# 描述中填入值
					input("xpath", "//textarea[@id='description']", "自动化测试保证金本金转存描述框")
					sleep(1)
					
					# 点击审核按钮
					click("xpath", "//span[text()='保存']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("保证金管理，本金转存成功！")
					logging.info("保证金管理，本金转存成功！")
					time.sleep(3)
			
			# 退出所有iframe窗体
			switch_default()
			
			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='保证金管理']/child::*[1]")
			
			# 用JS的方法点击保证金管理菜单按钮
			click("xpath", "//span[contains(text(),'资金计划填报')]/ancestor::*[1]/preceding-sibling::*[2]/descendant::*[3]")
			
			# 打印操作成功日志
			print("保证金管理，操作成功!")
			logging.info("保证金管理，操作成功!")
			time.sleep(2)
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("保证金管理,失败！" + str(traceback.format_exc()))
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
