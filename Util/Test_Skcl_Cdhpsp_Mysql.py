# encoding=utf-8
# @Time : 2020/8/14 14:49
# @Author : Mindy
# 此文件是测试MySQL版本资金结算管理--资金系统收付--收款处理--承兑汇票收票

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


class Test_Skcl_Cdhpsp_Mysql(unittest.TestCase):
	
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
		
		# 开始测试资金系统收付--收款处理--承兑汇票收票
		# 测试收款处理--承兑汇票收票
		try:
			# 点击'资金系统收付'菜单
			click("xpath", "//span[text()='资金系统收付']")
			# 点击收款处理菜单
			click("xpath", "//span[text()='收款处理']")
			# 退出所有iframe窗体
			switch_default()
			
			for i in range(1, 2):
				# 切入‘收款处理’的iframe窗体
				switch_to("xpath", "//iframe[@id='generalRecment-tab-iframe']")
				
				# 点击承兑汇票收票
				click("xpath", "//span[text()='承兑汇票收票']")
				
				# 切入‘承兑汇票收票’的iframe窗体
				switch_to("xpath", "//iframe[@id='subTabSix-iframe']")
				sleep(1)
				
				# 用JS方便点击‘确认收票’按钮旁边的倒三角形
				js_click("xpath", "//span[text()='确认收票']/parent::*/following-sibling::*/child::*")
				sleep(1)
				
				# 点击纸票确认收票
				js_click("xpath", "//a[contains(text(),'纸票确认收票')]")
				sleep(1)
				
				# 切入确认收票的的iframe窗体
				switch_to("xpath", "//iframe[@id='recWin-iframe']")
				sleep(1)
				
				# 修改勾选数据
				click("xpath", "//div[@title='外部给票单位:Mindy自动化测试']/parent::*/preceding-sibling::*[5]/descendant::*[2]")
				sleep(1)
				
				# 点击下一步
				click("xpath", "//span[text()='下一步']")
				sleep(1)
				
				# 进入收票详情页
				switch_to("xpath", "//iframe[@id='recmentsWin-iframe']")
				sleep(1)
				
				# 点击保存按钮
				click("xpath", "//span[text()='保存']")
				sleep(1)
				
				# 退出所有iframe窗体
				switch_default()
				
				# 用隐式等待方法等页面出现提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				print("收款处理，承兑汇票收票保存成功！")
				logging.info("收款处理，承兑汇票收票保存成功！")
				sleep(3)
			
				# 第一笔，就先修改，再修改页面提交送审，再撤销送审，再删除
				if i == 1:
					
					# 切入‘收款处理’的iframe窗体
					switch_to("xpath", "//iframe[@id='generalRecment-tab-iframe']")
					
					# 点击承兑汇票收票
					click("xpath", "//span[text()='承兑汇票收票']")
					
					# 切入‘承兑汇票收票’的iframe窗体
					switch_to("xpath", "//iframe[@id='subTabSix-iframe']")
					sleep(1)
					
					# 点击关闭页面
					click("xpath", "//span[text()='承兑汇票选择']/preceding-sibling::*[1]")
					sleep(1)
					
					switch_default()
					
					# 切入‘承兑汇票收票’的iframe窗体
					switch_to("xpath", "//iframe[@id='generalRecment-tab-iframe']")
					sleep(1)
					
					# 点击承兑汇票收票
					click("xpath", "//span[text()='承兑汇票收票']")
					
					# 切入‘承兑汇票收票’的iframe窗体
					switch_to("xpath", "//iframe[@id='subTabSix-iframe']")
					sleep(1)
					
					# 点击查看
					# 用JS的方法点击放大镜
					js_click("xpath", "//span[@class='f-contrac-close']")
					sleep(1)
					
					# 选择应收日期从
					today = date.today()
					due_date = today - timedelta(days=30)
					click("xpath", "//input[@id='paydatestart-input']")
					sleep(1)
					clear("xpath", "//input[@id='paydatestart-input']")
					sleep(1)
					input("xpath", "//input[@id='paydatestart-input']", str(due_date))
					time.sleep(1)
					
					# 点击查询
					click("xpath", "//span[text()='查询']")
					
					# 打印
					# 勾选数据
					click("xpath", "//div[@title='付方名称:Mindy自动化测试']/parent::*/preceding-sibling::*[6]/descendant::*[2]")
					sleep(1)
					
					# 点击‘打印’按钮
					click("xpath", "//span[text()='打印']")
					sleep(1)
					
					# 获取所有窗口句柄
					all_handles = self.driver.window_handles
					# 循环遍历所有新打开的窗口句柄，也就是说不包括主窗口
					now_handle = self.driver.current_window_handle
					for handle in all_handles:
						self.driver.switch_to.window(handle)
						if self.driver.title == u"payandrecsingleprint":
							implici_wait("xpath", "//td[contains(text(),'Mindy自动化测试')]")
							print("承兑汇票收票，打印成功!！")
							time.sleep(3)
							self.driver.switch_to.window(now_handle)
							switch_default()
					
					# 打印-打印记录
					# 切入‘承兑汇票收票’的iframe窗体
					switch_to("xpath", "//iframe[@id='generalRecment-tab-iframe']")
					sleep(1)
					
					# 点击承兑汇票收票
					click("xpath", "//span[text()='承兑汇票收票']")
					
					# 切入‘支票支付’的iframe窗体
					switch_to("xpath", "//iframe[@id='subTabSix-iframe']")
					sleep(1)
					
					# # 勾选数据
					# click("xpath", "//div[@title='付方名称:Mindy自动化测试']/parent::*/preceding-sibling::*[6]/descendant::*[2]")
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
					print("承兑汇票收票，打印记录查看成功！")
					logging.info("承兑汇票收票，打印记录查看成功！")
					time.sleep(3)
					
					switch_parent()
					
					# 点击关闭页面
					click("xpath", "//span[text()='打印']/preceding-sibling::*[1]")
					sleep(1)
					
					switch_default()
					
					# 关联票据查看
					# 切入‘承兑汇票收票’的iframe窗体
					switch_to("xpath", "//iframe[@id='generalRecment-tab-iframe']")
					sleep(1)
					
					# 点击承兑汇票收票
					click("xpath", "//span[text()='承兑汇票收票']")
					
					# 切入‘承兑汇票查看’的iframe窗体
					switch_to("xpath", "//iframe[@id='subTabSix-iframe']")
					sleep(1)
					
					# # 勾选数据
					# click("xpath", "//div[@title='付方名称:Mindy自动化测试']/parent::*/preceding-sibling::*[6]/descendant::*[2]")
					# sleep(1)
					
					# 点击关联票据查看
					click("xpath", "//span[text()='关联票据查看']")
					sleep(1)
					
					# 进入关联票据查看的窗体
					switch_to("xpath", "//iframe[@id='draftViewWin-iframe']")
					sleep(1)
					
					# 用隐式等待方法等页面出现  承兑方:Mindy自动化测试承兑方
					implici_wait("xpath", "//div[contains(text(),'亚唐科技')]")
					print("承兑汇票收票，打印记录查看成功！")
					logging.info("承兑汇票收票，打印记录查看成功！")
					time.sleep(3)
					
					switch_parent()
					
					# 点击关闭页面
					click("xpath", "//span[text()='关联票据查看']/preceding-sibling::*[1]")
					sleep(1)
					
					switch_default()
					
					# 作废按钮
					# 切入‘承兑汇票收票’的iframe窗体
					switch_to("xpath", "//iframe[@id='generalRecment-tab-iframe']")
					sleep(1)
					
					# 点击承兑汇票收票
					click("xpath", "//span[text()='承兑汇票收票']")
					
					# 切入‘承兑汇票查看’的iframe窗体
					switch_to("xpath", "//iframe[@id='subTabSix-iframe']")
					sleep(1)
					
					# # 勾选数据
					# click("xpath", "//div[@title='付方名称:Mindy自动化测试']/parent::*/preceding-sibling::*[6]/descendant::*[2]")
					# sleep(1)
					
					# 点击作废
					click("xpath", "//span[text()='作废']")
					sleep(1)
					
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					sleep(1)
				
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("承兑汇票支付, 作废成功！")
					logging.info("承兑汇票支付, 作废成功！")
					time.sleep(3)
					
			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='收款处理']/child::*[1]")
			
			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//span[text()='资金系统收付']")
			# 打印操作成功日志
			print("承兑汇票收票，操作成功!")
			logging.info("承兑汇票收票，操作成功!")
			time.sleep(2)
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("承兑汇票收票失败！" + str(traceback.format_exc()))
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
