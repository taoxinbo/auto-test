# encoding=utf-8
# @Time : 2020/8/14 14:49
# @Author : Mindy
# 此文件是测试内部资金池模块功能
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


class Test_NbZjc(unittest.TestCase):
	
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
		# login( G_Mys_Url,TestUser,Password, "自动化测试租户")
		# login(G_Mys_Url, Tao, Password, "默认租户")
		# login(G_Mys_Url, mindy, Password, "亚唐科技")
		# login(G_Mys_Url, judy, Password, "默认租户")
		
		logging.info("开始测试内部资金池的页面功能")
		# 将页面的滚动条滑动到‘内部资金池’页面的地方
		js_gd("xpath", "//span[contains(text(),'内部资金池')]")
		# 用JS的方法点击内部资金池菜单按钮
		js_click("xpath", "//span[contains(text(),'内部资金池')]")

		try:
			# 点击项目资金管理菜单
			click("xpath", "//span[text()='项目资金管理']")
			# 用JS的方法点击项目期初设置菜单按钮
			js_click("xpath", "//span[contains(text(),'项目期初设置')]")
			# 退出所有iframe窗体
			switch_default()

			for i in range(1, 3):
				# 切入项目期初设置的iframe窗体
				switch_to("xpath", "//iframe[@id='projectInitializeSet-tab-iframe']")
				logging.info("开始测试项目期初设置功能")

				# 用JS的方法点击新增按钮
				js_click("xpath", "//span[text()='新增']")

				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='addWin-iframe']")
				sleep(1)
				
				# 工程项目
				click("xpath", "//input[@id='combobox-input-projectitemid']")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-projectitemid']")
				sleep(1)
				input_enter("xpath", "//input[@id='combobox-input-projectitemid']")
				sleep(1)
				
				# 初始余额
				clear("xpath", "//input[@id='banlance-input']")
				sleep(1)
				input("xpath", "//input[@id='banlance-input']", "30000")
				sleep(1)
				
				# 透支余额
				clear("xpath", "//input[@id='maxoverdraftamount-input']")
				sleep(1)
				input("xpath", "//input[@id='maxoverdraftamount-input']", "300")
				sleep(1)
				
				# 币种
				click("xpath", "//input[@id='combobox-input-currencyid']")
				sleep(1)
				input("xpath", "//input[@id='combobox-input-currencyid']", "人民币")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-currencyid']")
				sleep(1)
				input_enter("xpath", "//input[@id='combobox-input-currencyid']")
				sleep(1)
				
				# 控制方式
				click("xpath", "//input[@id='combobox-input-controlmode']")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-controlmode']")
				sleep(1)
				input_enter("xpath", "//input[@id='combobox-input-controlmode']")
				sleep(1)
				
				# 描述框中填入值
				input("xpath", "//textarea[@id='description']", "自动化测试往来决议备注框")
				sleep(1)

				# 缺少附件上传

				# 点击保存按钮
				click("xpath", "//span[text()='保存']")

				# 退出所有iframe窗体
				switch_default()

				# 用隐式等待方法等页面出现新增成功的提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				print("项目期初设置，保存成功！")
				time.sleep(3)

				if i == 1:
					# 切入项目期初设置的iframe窗体
					switch_to("xpath", "//iframe[@id='projectInitializeSet-tab-iframe']")
					sleep(1)

					# 点击查看
					# 用JS的方法点击放大镜
					js_click("xpath", "//span[@class='f-contrac-close']")
					sleep(1)

					# 选择工程项目
					click("xpath", "//input[@id='combobox-input-projectitemid']")
					sleep(1)
					click("xpath", "//div[@title='代码-名称:TestPro001-自动化测试工程项目']")
					sleep(1)
					
					# 点击查询
					click("xpath", "//span[text()='查询']")
					sleep(1)

					# 勾选
					click("xpath", "//span[contains(text(),'自动化测试工程项目')]/ancestor::*[7]/preceding-sibling::*[1]/descendant::*[19]")
					sleep(1)

					click("xpath", "//span[text()='删除']")
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现删除的提示框
					implici_wait("xpath", "//span[contains(text(),'成功删除1条记录！')]")
					print("项目期初设置，删除成功！")
					time.sleep(3)

			# 修改功能
			# 切入‘项目期初设置’的iframe窗体
			switch_to("xpath", "//iframe[@id='projectInitializeSet-tab-iframe']")
			sleep(1)
			
			# 勾选
			click("xpath", "//span[contains(text(),'自动化测试工程项目')]/ancestor::*[7]/preceding-sibling::*[1]/descendant::*[19]")
			sleep(1)

			# 点击修改按钮
			click("xpath", "//span[text()='修改']")
			sleep(1)

			# 切入新增的iframe窗体
			switch_to("xpath", "//iframe[@id='modWin-iframe']")
			sleep(1)

			# 描述框中填入值
			input("xpath", "//textarea[@id='description']", "自动化测试项目期初设置描述框修改")
			sleep(1)

			# 点击保存按钮
			click("xpath", "//span[text()='保存']")

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功')]")
			print("项目期初设置，修改成功！")
			time.sleep(3)
			
			# 切入‘项目期初设置’的iframe窗体
			switch_to("xpath", "//iframe[@id='projectInitializeSet-tab-iframe']")
			sleep(1)
			
			# 勾选
			click("xpath", "//span[contains(text(),'自动化测试工程项目')]/ancestor::*[7]/preceding-sibling::*[1]/descendant::*[19]")
			sleep(1)

			# 点击审核按钮
			click("xpath", "//span[text()='审核']")
			
			# 点击弹出框的OK键
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功')]")
			print("项目期初设置，第一次审核成功！")
			logging.info("项目期初设置，第一次审核成功！")
			time.sleep(3)

			# 取消审核
			# 切入‘项目期初设置’的iframe窗体
			switch_to("xpath", "//iframe[@id='projectInitializeSet-tab-iframe']")
			sleep(1)
			
			# 勾选
			click("xpath", "//span[contains(text(),'自动化测试工程项目')]/ancestor::*[7]/preceding-sibling::*[1]/descendant::*[19]")
			sleep(1)

			# 用JS方便点击‘审核’按钮旁边的倒三角形
			js_click("xpath", "//span[text()='审核']/parent::*/following-sibling::*/child::*")
			sleep(1)

			# 点击取消送审按钮
			js_click("xpath", "//a[contains(text(),'取消审核')]")
			sleep(1)

			# 点击弹出框的OK键
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'成功取消审批1条记录！')]")
			print("项目期初设置，取消审核成功！")
			logging.info("项目期初设置，取消审核成功！")
			time.sleep(3)
			
			# 切入‘项目期初设置’的iframe窗体
			switch_to("xpath", "//iframe[@id='projectInitializeSet-tab-iframe']")
			sleep(1)
			
			# 勾选
			click("xpath", "//span[contains(text(),'自动化测试工程项目')]/ancestor::*[7]/preceding-sibling::*[1]/descendant::*[19]")
			sleep(1)
			
			# 点击审核按钮
			click("xpath", "//span[text()='审核']")
			# 点击弹出框的OK键
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功')]")
			print("项目期初设置，第二次审核成功！")
			logging.info("项目期初设置，第二次审核成功！")
			time.sleep(3)
			
			# 切入‘项目期初设置’的iframe窗体
			switch_to("xpath", "//iframe[@id='projectInitializeSet-tab-iframe']")
			sleep(1)
			
			# 勾选
			click("xpath", "//span[contains(text(),'自动化测试工程项目')]/ancestor::*[7]/preceding-sibling::*[1]/descendant::*[19]")
			sleep(1)

			# 点击修改按钮
			click("xpath", "//span[text()='变更']")
			sleep(1)

			# 切入新增的iframe窗体
			switch_to("xpath", "//iframe[@id='modWin-iframe']")
			sleep(1)

			# 描述框中填入值
			input("xpath", "//textarea[@id='description']", "自动化测试项目期初设置描述框变更")
			sleep(1)

			# 点击保存按钮
			click("xpath", "//span[text()='保存']")

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功')]")
			print("项目期初设置，变更成功！")
			time.sleep(3)

			switch_default()

			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='项目期初设置']/child::*[1]")

			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//span[text()='项目资金管理']")

			# 打印操作成功日志
			print("项目期初设置，操作成功!")
			logging.info("项目期初设置，操作成功!")
			time.sleep(2)

		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("项目期初设置操作失败！" + str(traceback.format_exc()))
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