# encoding=utf-8
# @Time : 2020/8/14 14:49
# @Author : Mindy
# 此文件是测试计划任务功能
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


class Test_Jhrw(unittest.TestCase):
	
	# 启动浏览器
	def setUp(self):
		# 启动浏览器的另外一个方法：通过封装启动浏览器的驱动，启动不同浏览器
		self.driver = get("chrome")
	
	# 登陆系统、对系统设置进行操作
	def test_trade(self):
		# 通过登陆封装函数，进行登陆
		# login( G_Ora_Url,TestUser,Password, "自动化测试租户")
		# login( G_Ora_Url,Tao, Password,"默认租户")
		login(G_Ora_Url, mindy, Password, "默认租户")
		# login( G_Mys_Url,TestUser,Password, "自动化测试租户")
		# login(G_Mys_Url, Tao, Password, "默认租户")
		# login(G_Mys_Url, mindy, Password, "默认租户")
		# login(G_Mys_Url, judy, Password, "默认租户")
		
		logging.info("开始测试计划任务功能")

		# 开始测试计划任务功能
		try:

			# 点击计划任务
			click("xpath", "//div[@class='taskset']")
			# 退出所有的iframe窗体
			switch_default()
			
			# 进入计划任务的iframe窗体
			switch_to("xpath", "//iframe[@id='scheduledtasks-tab-iframe']")
			sleep(1)
			# 切入计划任务--系统任务的iframe窗体
			switch_to("xpath", "//iframe[@id='systemtask']")
			logging.info("开始测试系统任务功能")
			
			# 用JS的方法点击新增按钮
			js_click("xpath", "//span[text()='新增']")
			
			# 切入新增的iframe窗体
			switch_to("xpath", "//iframe[@id='addWin-iframe']")
			sleep(1)
			
			# 选择查询账户余额
			click("xpath", "//input[@id='1000']")
			sleep(1)
			
			# 点击下一步
			click("xpath", "//span[text()='下一步']")
			sleep(1)
			
			# 退出所有窗体
			switch_default()
			
			# 进入计划任务窗体
			switch_to("xpath", "//iframe[@id='scheduledtasks-tab-iframe']")
			
			# 进入系统任务窗体
			switch_to("xpath", "//iframe[@id='systemtask']")
			
			# 进入计划任务详细页面nextWin-iframe
			switch_to("xpath", "//iframe[@id='nextWin-iframe']")
			sleep(1)
			
			# 填写任务名称
			input("xpath", "//input[@id='taskname']", "自动化测试账户余额查询计划任务")
			sleep(1)
			
			# 选择组织
			click("xpath", "//input[@id='combobox-input-orgids']")
			sleep(1)
			click("xpath", "//div[@title='代码-名称:001000-亚唐科技']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
			sleep(1)
			
			# 选择银行
			click("xpath", "//input[@id='combobox-input-bankids']")
			sleep(1)
			click("xpath", "//div[@title='代码-名称:BOC-中国银行']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
			sleep(1)
			
			# # 消息通知人
			# click("xpath", "//input[@id='combobox-input-userids']")
			# sleep(1)
			# click("xpath", "//div[@title='代码-名称:mindy-田遍地']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
			# sleep(1)
			
			# 勾选是否包含下级
			click("xpath", "//input[@id='isincsub']")
			sleep(1)
			
			# 日历
			click("xpath", "//input[@id='combobox-input-calendarid']")
			sleep(1)
			input_down("xpath", "//input[@id='combobox-input-calendarid']")
			input_enter("xpath", "//input[@id='combobox-input-calendarid']")
			sleep(1)
			
			# 选择开始日期--日期从
			# 点击日期从的日历按钮
			js_click("xpath", "//span[@id='dateStart-trigger']")
			time.sleep(1)
			
			# 退出所有的iframe窗体
			switch_default()
			
			# 切入日历框的iframe
			switch_to("xpath", "//iframe[@hidefocus='true']")
			# 点击日历框中今天的按钮
			click("xpath", "//input[@id='dpTodayInput']")
			time.sleep(1)
			# 退出当前日历框的iframe窗体
			switch_parent()
			
			# 日期到
			# 进入计划任务窗体
			switch_to("xpath", "//iframe[@id='scheduledtasks-tab-iframe']")
			
			# 进入系统任务窗体
			switch_to("xpath", "//iframe[@id='systemtask']")
			
			# 进入计划任务详细页面nextWin-iframe
			switch_to("xpath", "//iframe[@id='nextWin-iframe']")
			sleep(1)
			
			# 点击日期到的日历按钮
			js_click("xpath", "//span[@id='dateEnd-trigger']")
			time.sleep(1)
			
			# 退出所有的iframe窗体
			switch_default()
			
			# 切入日历框的iframe
			switch_to("xpath", "//iframe[@hidefocus='true']")
			# 点击日历框中确定的按钮
			click("xpath", "//input[@id='dpOkInput']")
			time.sleep(1)
			# 退出当前日历框的iframe窗体
			switch_parent()
			
			# 开始日期
			# 进入计划任务窗体
			switch_to("xpath", "//iframe[@id='scheduledtasks-tab-iframe']")
			
			# 进入系统任务窗体
			switch_to("xpath", "//iframe[@id='systemtask']")
			
			# 进入计划任务详细页面nextWin-iframe
			switch_to("xpath", "//iframe[@id='nextWin-iframe']")
			sleep(1)
			
			input("xpath", "//input[@id='startTime']", "10:00")
			sleep(1)
			
			# 结束日期
			input("xpath", "//input[@id='endTime']", "20:00")
			sleep(1)
		
			# 运行间隔
			input("xpath", "//input[@id='intervalTime-input']", "1")
			sleep(1)
		
			# 点击生成时间点按钮
			click("xpath", "//span[@class='f-new-btn-text clock_go_icon']")
			sleep(1)

			# 点击保存按钮
			click("xpath", "//span[text()='保存']")
			
			# 退出所有iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("查询账户余额，保存成功！")
			time.sleep(3)
			
			# 修改
			# 进入计划任务窗体
			switch_to("xpath", "//iframe[@id='scheduledtasks-tab-iframe']")
			
			# 进入系统任务窗体
			switch_to("xpath", "//iframe[@id='systemtask']")
			
			# 勾选
			click("xpath", "//div[@title='任务名称:自动化测试账户余额查询计划任务']/parent::*/preceding-sibling::*[2]/descendant::*[2]")
			
			# 点击修改按钮
			click("xpath", "//span[text()='修改']")
			sleep(1)

			# 进入修改窗体
			switch_to("xpath", "//iframe[@id='editWin-iframe']")
			sleep(1)
			
			# 描述框输入值
			input("xpath", "//textarea[@id='description']", "自动化测试查询账户余额描述框")
			sleep(1)
			
			# 点击保存按钮
			click("xpath", "//span[text()='保存']")
			
			# 退出所有iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功')]")
			print("查询账户余额计划任务，修改成功！")
			time.sleep(3)
			
			# 运行
			# 进入计划任务窗体
			switch_to("xpath", "//iframe[@id='scheduledtasks-tab-iframe']")
			
			# 进入系统任务窗体
			switch_to("xpath", "//iframe[@id='systemtask']")
			
			# 勾选
			click("xpath", "//div[@title='任务名称:自动化测试账户余额查询计划任务']/parent::*/preceding-sibling::*[2]/descendant::*[2]")
			
			# 点击运行按钮
			click("xpath", "//span[text()='运行']")
			
			# 点击弹出框的OK键
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
			
			# 退出所有iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'任务开始运行,具体结果请查看任务消息提示')]")
			print("查询账户余额计划任务，运行按钮点击成功！")
			time.sleep(3)
			
			# 启动
			# 进入计划任务窗体
			switch_to("xpath", "//iframe[@id='scheduledtasks-tab-iframe']")
			
			# 进入系统任务窗体
			switch_to("xpath", "//iframe[@id='systemtask']")
			
			# 勾选
			click("xpath", "//div[@title='任务名称:自动化测试账户余额查询计划任务']/parent::*/preceding-sibling::*[2]/descendant::*[2]")
			
			# 点击运行按钮
			click("xpath", "//span[text()='启动']")
			
			# 点击弹出框的OK键
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
			
			# 退出所有iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("查询账户余额计划任务，启动按钮点击成功！")
			time.sleep(3)
			
			# 当日运行计划
			# 进入计划任务的iframe窗体
			switch_to("xpath", "//iframe[@id='scheduledtasks-tab-iframe']")
			sleep(1)
			click("xpath", "//span[text()='当日运行计划']")
			# 切入计划任务--系统任务的iframe窗体
			switch_to("xpath", "//iframe[@id='runschedulers']")
			logging.info("开始测试当日运行计划功能")
			
			# 点击右下角刷新按钮
			click("xpath", "//span[@id='gridbar-page-refresh']")
			sleep(1)
			
			# 用隐式等待方法等页面出现预期数据：任务名称:自动化测试账户余额查询计划任务
			implici_wait("xpath", "//div[@title='任务名称:自动化测试账户余额查询计划任务']")
			print("当前运行计划查看成功！")
			time.sleep(3)
			
			switch_default()
			
			# 运行记录
			# 进入计划任务的iframe窗体
			switch_to("xpath", "//iframe[@id='scheduledtasks-tab-iframe']")
			sleep(1)
			click("xpath", "//span[text()='运行记录']")
			# 切入计划任务--运行记录的iframe窗体
			switch_to("xpath", "//iframe[@id='runhistories']")
			logging.info("开始测试当日运行计划功能")
			
			# 用隐式等待方法等页面出现预期数据：任务名称:自动化测试账户余额查询计划任务
			implici_wait("xpath", "//div[@title='任务名称:自动化测试账户余额查询计划任务']")
			print("运行记录查看成功！")
			time.sleep(3)
			
			switch_default()
			
			# 返回点击暂停按钮
			# 暂停
			# 进入计划任务窗体
			switch_to("xpath", "//iframe[@id='scheduledtasks-tab-iframe']")
			
			# 点击系统任务
			click("xpath", "//span[text()='系统任务']")
			
			# 进入系统任务窗体
			switch_to("xpath", "//iframe[@id='systemtask']")
			
			# 勾选
			click("xpath", "//div[@title='任务名称:自动化测试账户余额查询计划任务']/parent::*/preceding-sibling::*[2]/descendant::*[2]")
			
			# 点击运行按钮
			click("xpath", "//span[text()='暂停']")
			
			# 点击弹出框的OK键
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
			
			# 退出所有iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("查询账户余额计划任务，暂停按钮点击成功！")
			time.sleep(3)
			
			# 点击删除
			# 进入计划任务窗体
			switch_to("xpath", "//iframe[@id='scheduledtasks-tab-iframe']")
			
			# 进入系统任务窗体
			switch_to("xpath", "//iframe[@id='systemtask']")
			
			# 勾选
			click("xpath", "//div[@title='任务名称:自动化测试账户余额查询计划任务']/parent::*/preceding-sibling::*[2]/descendant::*[2]")
			
			# 点击删除按钮
			click("xpath", "//span[text()='删除']")
			
			# 点击弹出框的OK键
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
			
			# 退出所有iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功')]")
			print("查询账户余额计划任务，删除成功！")
			time.sleep(3)

			switch_default()

			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='计划任务']/child::*[1]")
			
			# 打印操作成功日志
			print("计划任务，操作成功!")
			logging.info("计划任务，操作成功!")
			time.sleep(2)

		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("计划任务,失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
			
	# # # def tearDown(self):
	# # #     self.driver.quit()
	# print("结束时间：", time.strftime("%Y-%m-%d %H:%M:%S"))
	
if __name__ == '__main__':
	#  启动单元测试
	unittest.main(verbosity=2)