# encoding=utf-8
# @Time : 2020/8/14 14:49
# @Author : Mindy
# 此文件是测试系统设置模块信息权限
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


class Test_XinxQx(unittest.TestCase):
	
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
		# login( G_Mys_Url,TestUser,Password, "自动化测试租户")
		# login(G_Mys_Url, Tao, Password, "默认租户")
		# login(G_Mys_Url, mindy, Password, "亚唐科技")
		# login(G_Mys_Url, judy, Password, "默认租户")
		
		logging.info("开始测试信息权限功能")
		
		# 信息权限功能
		try:

			# # 点击系统设置
			click("xpath", "//div[@class='sysconfigset']")
			switch_to("xpath", "//iframe[@id='systemconfig-tab-iframe']")
			sleep(1)
			click("xpath", "//span[text()='信息权限']")
			logging.info("开始测试信息权限--银行账户权限分配功能")

			# 点击银行账户权限分配
			click("xpath", "//span[text()='银行账户权限分配']")
			sleep(1)
			switch_default()

			# 进入银行账户权限分配的iframe窗体
			switch_to("xpath", "//iframe[@id='bankAccountRightConfig-tab-iframe']")
			# 进入银行账户权限角色分配窗体
			switch_to("xpath", "//iframe[@id='subTabOne-iframe']")

			# 点击勾选数据
			# 勾选
			click("xpath", "//div[@title='角色代码:fh']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
			sleep(1)

			# 点击银行账户权限分配
			click("xpath", "//span[text()='银行账户权限分配']")
			sleep(1)

			# 跳转进入银行账户权限分配的窗体
			switch_to("xpath", "//iframe[@id='distributeWin-iframe']")
			sleep(1)

			# 查询权限
			# 用JS方便点击‘查询权限’按钮旁边的倒三角形
			js_click("xpath", "//span[text()='查询权限']/parent::*//descendant::*[3]")
			sleep(1)

			click("xpath", "//div[contains(text(),'选择全部')]")
			sleep(1)

			# 结算权限
			# 用JS方便点击‘查询权限’按钮旁边的倒三角形
			js_click("xpath", "//span[text()='结算权限']/parent::*//descendant::*[3]")
			sleep(1)

			click("xpath", "//div[contains(text(),'选择全部')]")
			sleep(1)

			# 点击保存按钮
			click("xpath", "//span[text()='保存']")
			sleep(1)

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("银行账户权限，角色分配操作成功！")
			logging.info("银行账户权限，角色分配操作成功！")
			time.sleep(3)

			# 银行账户权限重置
			# 进入银行账户权限分配的iframe窗体
			switch_to("xpath", "//iframe[@id='bankAccountRightConfig-tab-iframe']")
			# 进入银行账户权限角色分配窗体
			switch_to("xpath", "//iframe[@id='subTabOne-iframe']")

			# 点击勾选数据
			# 勾选
			click("xpath", "//div[@title='角色代码:fh']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
			sleep(1)

			# 点击银行账户权限分配
			click("xpath", "//span[text()='银行账户权限重置']")
			sleep(1)

			# 跳转进入银行账户权限分配的窗体
			switch_to("xpath", "//iframe[@id='resetWin-iframe']")
			sleep(1)

			# 查询权限
			# 用JS方便点击‘查询权限’按钮旁边的倒三角形
			js_click("xpath", "//span[text()='查询权限']/parent::*//descendant::*[3]")
			sleep(1)

			click("xpath", "//div[contains(text(),'选择全部')]")
			sleep(1)

			# 结算权限
			# 用JS方便点击‘查询权限’按钮旁边的倒三角形
			js_click("xpath", "//span[text()='结算权限']/parent::*//descendant::*[3]")
			sleep(1)

			click("xpath", "//div[contains(text(),'选择全部')]")
			sleep(1)

			# 点击保存按钮
			click("xpath", "//span[text()='保存']")
			sleep(1)

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("银行账户权限，重置操作成功！")
			logging.info("银行账户权限，重置操作成功！")
			time.sleep(3)

			# 银行账户权限用户分配
			# 进入银行账户权限分配的iframe窗体
			switch_to("xpath", "//iframe[@id='bankAccountRightConfig-tab-iframe']")
			# 点击银行账户权限用户分配
			click("xpath", "//span[text()='银行账户权限用户分配']")
			sleep(1)
			# 进入银行账户权限用户分配窗体
			switch_to("xpath", "//iframe[@id='subTabTwo-iframe']")

			# 点击勾选数据
			# 勾选
			click("xpath", "//div[@title='用户名称:田遍地']/parent::*/preceding-sibling::*[2]/descendant::*[2]")
			sleep(1)

			# 点击银行账户权限分配
			click("xpath", "//span[text()='银行账户权限分配']")
			sleep(1)

			# 跳转进入银行账户权限分配的窗体
			switch_to("xpath", "//iframe[@id='distributeWin-iframe']")
			sleep(1)

			# 查询权限
			# 用JS方便点击‘查询权限’按钮旁边的倒三角形
			js_click("xpath", "//span[text()='查询权限']/parent::*//descendant::*[3]")
			sleep(1)

			click("xpath", "//div[contains(text(),'选择全部')]")
			sleep(1)

			# 结算权限
			# 用JS方便点击‘查询权限’按钮旁边的倒三角形
			js_click("xpath", "//span[text()='结算权限']/parent::*//descendant::*[3]")
			sleep(1)

			click("xpath", "//div[contains(text(),'选择全部')]")
			sleep(1)

			# 点击保存按钮
			click("xpath", "//span[text()='保存']")
			sleep(1)

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("银行账户权限，用户分配操作成功！")
			logging.info("银行账户权限，用户分配操作成功！")
			time.sleep(3)

			# 银行账户权限重置
			# 进入银行账户权限分配的iframe窗体
			switch_to("xpath", "//iframe[@id='bankAccountRightConfig-tab-iframe']")
			# 点击银行账户权限用户分配
			click("xpath", "//span[text()='银行账户权限用户分配']")
			sleep(1)
			# 进入银行账户权限用户分配窗体
			switch_to("xpath", "//iframe[@id='subTabTwo-iframe']")

			# 点击勾选数据
			# 勾选
			click("xpath", "//div[@title='用户名称:田遍地']/parent::*/preceding-sibling::*[2]/descendant::*[2]")
			sleep(1)

			# 点击银行账户权限分配
			click("xpath", "//span[text()='银行账户权限重置']")
			sleep(1)

			# 跳转进入银行账户权限分配的窗体
			switch_to("xpath", "//iframe[@id='resetWin-iframe']")
			sleep(1)

			# 查询权限
			# 用JS方便点击‘查询权限’按钮旁边的倒三角形
			js_click("xpath", "//span[text()='查询权限']/parent::*//descendant::*[3]")
			sleep(1)

			click("xpath", "//div[contains(text(),'选择全部')]")
			sleep(1)

			# 结算权限
			# 用JS方便点击‘查询权限’按钮旁边的倒三角形
			js_click("xpath", "//span[text()='结算权限']/parent::*//descendant::*[3]")
			sleep(1)

			click("xpath", "//div[contains(text(),'选择全部')]")
			sleep(1)

			# 点击保存按钮
			click("xpath", "//span[text()='保存']")
			sleep(1)

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("银行账户权限，用户重置操作成功！")
			logging.info("银行账户权限，用户重置操作成功！")
			time.sleep(3)

			switch_default()

			# 缺少本组织账户权限初始

			# 缺少可操作组织账户权限初始

			# 再次点击基础设置菜单，使之关闭
			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='银行账户权限分配']/child::*[1]")

			# 打印操作成功日志
			print("银行账户权限分配，操作成功!")
			logging.info("银行账户权限分配，操作成功!")
			time.sleep(2)

		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("银行账户权限分配,失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		
		# 系统参数权限分配
		try:
			# 点击系统设置
			click("xpath", "//div[@class='sysconfigset']")
			# 进入系统设置的iframe窗体
			switch_to("xpath", "//iframe[@id='systemconfig-tab-iframe']")
			logging.info("开始测试信息权限--系统参数权限分配功能")
			sleep(1)
			click("xpath", "//span[text()='信息权限']")

			# 点击系统参数权限分配
			click("xpath", "//span[text()='系统参数权限分配']")
			sleep(1)
			switch_default()

			# 进入系统参数权限分配的iframe窗体
			switch_to("xpath", "//iframe[@id='sysParamRightConfig-tab-iframe']")
			# 进入系统参数权限角色分配窗体
			switch_to("xpath", "//iframe[@id='subTabOne-iframe']")

			# 点击勾选数据
			# 勾选
			click("xpath", "//div[@title='角色代码:fh']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
			sleep(1)

			# 点击系统参数权限分配
			click("xpath", "//span[text()='系统参数权限分配']")
			sleep(1)

			# 跳转进入系统参数权限分配的窗体
			switch_to("xpath", "//iframe[@id='distributeWin-iframe']")
			sleep(1)

			# 查询权限
			# 用JS方便点击‘查询权限’按钮旁边的倒三角形
			js_click("xpath", "//span[text()='查询权限']/parent::*//descendant::*[3]")
			sleep(1)

			click("xpath", "//div[contains(text(),'选择全部')]")
			sleep(1)

			# 点击保存按钮
			click("xpath", "//span[text()='保存']")
			sleep(1)

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("系统参数权限，角色分配操作成功！")
			logging.info("系统参数权限，角色分配操作成功！")
			time.sleep(3)

			# 系统参数权限分配重置
			# 进入系统参数权限分配的iframe窗体
			switch_to("xpath", "//iframe[@id='sysParamRightConfig-tab-iframe']")
			# 进入系统参数权限角色分配窗体
			switch_to("xpath", "//iframe[@id='subTabOne-iframe']")

			# 点击勾选数据
			# 勾选
			click("xpath", "//div[@title='角色代码:fh']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
			sleep(1)

			# 点击系统参数权限分配
			click("xpath", "//span[text()='系统参数权限重置']")
			sleep(1)

			# 跳转进入系统参数权限分配的窗体
			switch_to("xpath", "//iframe[@id='resetWin-iframe']")
			sleep(1)

			# 查询权限
			# 用JS方便点击‘查询权限’按钮旁边的倒三角形
			js_click("xpath", "//span[text()='查询权限']/parent::*//descendant::*[3]")
			sleep(1)

			click("xpath", "//div[contains(text(),'选择全部')]")
			sleep(1)

			# 点击保存按钮
			click("xpath", "//span[text()='保存']")
			sleep(1)

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("系统参数权限，重置操作成功！")
			logging.info("系统参数权限，重置操作成功！")
			time.sleep(3)

			# 系统参数权限用户分配
			# 进入系统参数权限分配的iframe窗体
			switch_to("xpath", "//iframe[@id='sysParamRightConfig-tab-iframe']")
			# 点击银行账户权限用户分配
			click("xpath", "//span[text()='系统参数用户分配']")
			sleep(1)
			# 进入系统参数权限用户分配窗体
			switch_to("xpath", "//iframe[@id='subTabTwo-iframe']")

			# 点击勾选数据
			# 勾选
			click("xpath", "//div[@title='用户名称:田遍地']/parent::*/preceding-sibling::*[2]/descendant::*[2]")
			sleep(1)

			# 点击银行账户权限分配
			click("xpath", "//span[text()='系统参数权限分配']")
			sleep(1)

			# 跳转进入系统参数权限分配的窗体
			switch_to("xpath", "//iframe[@id='distributeWin-iframe']")
			sleep(1)

			# 查询权限
			# 用JS方便点击‘查询权限’按钮旁边的倒三角形
			js_click("xpath", "//span[text()='查询权限']/parent::*//descendant::*[3]")
			sleep(1)

			click("xpath", "//div[contains(text(),'选择全部')]")
			sleep(1)

			# # 结算权限
			# # 用JS方便点击‘查询权限’按钮旁边的倒三角形
			# js_click("xpath", "//span[text()='结算权限']/parent::*//descendant::*[3]")
			# sleep(1)
			#
			# click("xpath", "//div[contains(text(),'选择全部')]")
			# sleep(1)
			#
			# 点击保存按钮
			click("xpath", "//span[text()='保存']")
			sleep(1)

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("系统参数权限，用户分配操作成功！")
			logging.info("系统参数权限，用户分配操作成功！")
			time.sleep(3)

			# 系统参数权限重置
			# 进入系统参数权限的iframe窗体
			switch_to("xpath", "//iframe[@id='sysParamRightConfig-tab-iframe']")
			# 点击系统参数权限用户分配
			click("xpath", "//span[text()='系统参数用户分配']")
			sleep(1)
			# 进入系统参数权限分配窗体
			switch_to("xpath", "//iframe[@id='subTabTwo-iframe']")

			# 点击勾选数据
			# 勾选
			click("xpath", "//div[@title='用户名称:田遍地']/parent::*/preceding-sibling::*[2]/descendant::*[2]")
			sleep(1)

			# 点击系统参数权限重置
			click("xpath", "//span[text()='系统参数权限重置']")
			sleep(1)

			# 跳转进入系统参数权限重置的窗体
			switch_to("xpath", "//iframe[@id='resetWin-iframe']")
			sleep(1)

			# 查询权限
			# 用JS方便点击‘查询权限’按钮旁边的倒三角形
			js_click("xpath", "//span[text()='查询权限']/parent::*//descendant::*[3]")
			sleep(1)

			click("xpath", "//div[contains(text(),'选择全部')]")
			sleep(1)

			# 点击保存按钮
			click("xpath", "//span[text()='保存']")
			sleep(1)

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("系统参数权限，用户重置操作成功！")
			logging.info("系统参数权限，用户重置操作成功！")
			time.sleep(3)

			# 缺少本组织账户权限初始

			# 缺少可操作组织账户权限初始

			# 再次点击基础设置菜单，使之关闭
			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='系统参数权限分配']/child::*[1]")

			# 打印操作成功日志
			print("系统参数权限，操作成功!")
			logging.info("系统参数权限，操作成功!")
			time.sleep(2)

		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("系统参数权限,失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
	
		# 任务权限分配
		try:
			# 点击系统设置
			click("xpath", "//div[@class='sysconfigset']")
			# 进入系统设置的iframe窗体
			switch_to("xpath", "//iframe[@id='systemconfig-tab-iframe']")
			logging.info("开始测试信息权限--任务权限分配功能")
			sleep(1)
			click("xpath", "//span[text()='信息权限']")

			# 点击任务权限分配
			click("xpath", "//span[text()='任务权限分配']")
			sleep(1)
			switch_default()

			# 进入任务权限分配的iframe窗体
			switch_to("xpath", "//iframe[@id='taskRightConfig-tab-iframe']")
			# 进入任务权限分配窗体
			switch_to("xpath", "//iframe[@id='subTabOne-iframe']")

			# 点击勾选数据
			# 勾选
			click("xpath", "//div[@title='角色代码:fh']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
			sleep(1)

			# 点击任务命令权限分配
			click("xpath", "//span[text()='任务命令权限分配']")
			sleep(1)

			# 跳转进入任务命令权限分配的窗体
			switch_to("xpath", "//iframe[@id='distributeWin-iframe']")
			sleep(1)

			# 查询权限
			# 用JS方便点击‘查询权限’按钮旁边的倒三角形
			js_click("xpath", "//span[text()='查询权限']/parent::*//descendant::*[3]")
			sleep(1)

			click("xpath", "//div[contains(text(),'选择全部')]")
			sleep(1)

			# 点击保存按钮
			click("xpath", "//span[text()='保存']")
			sleep(1)

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("任务命令权限，角色分配操作成功！")
			logging.info("任务命令权限，角色分配操作成功！")
			time.sleep(3)

			# 任务命令权限重置
			# 进入任务权限分配的iframe窗体
			switch_to("xpath", "//iframe[@id='taskRightConfig-tab-iframe']")
			# 进入任务命令权限分配窗体
			switch_to("xpath", "//iframe[@id='subTabOne-iframe']")

			# 点击勾选数据
			# 勾选
			click("xpath", "//div[@title='角色代码:fh']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
			sleep(1)

			# 点击任务命令权限分配
			click("xpath", "//span[text()='任务命令权限重置']")
			sleep(1)

			# 跳转进入任务命令权限的窗体
			switch_to("xpath", "//iframe[@id='resetWin-iframe']")
			sleep(1)

			# 查询权限
			# 用JS方便点击‘查询权限’按钮旁边的倒三角形
			js_click("xpath", "//span[text()='查询权限']/parent::*//descendant::*[3]")
			sleep(1)

			click("xpath", "//div[contains(text(),'选择全部')]")
			sleep(1)

			# 点击保存按钮
			click("xpath", "//span[text()='保存']")
			sleep(1)

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("任务命令权限，重置操作成功！")
			logging.info("任务命令权限，重置操作成功！")
			time.sleep(3)

			# 任务命令权限用户分配
			# 进入任务命令权限分配的iframe窗体
			switch_to("xpath", "//iframe[@id='taskRightConfig-tab-iframe']")
			# 点击任务命令用户分配
			click("xpath", "//span[text()='任务命令用户分配']")
			sleep(1)
			# 进入任务命令用户分配窗体
			switch_to("xpath", "//iframe[@id='subTabTwo-iframe']")

			# 点击勾选数据
			# 勾选
			click("xpath", "//div[@title='用户名称:田遍地']/parent::*/preceding-sibling::*[2]/descendant::*[2]")
			sleep(1)

			# 点击银行账户权限分配
			click("xpath", "//span[text()='任务命令权限分配']")
			sleep(1)

			# 跳转进入系统参数权限分配的窗体
			switch_to("xpath", "//iframe[@id='distributeWin-iframe']")
			sleep(1)

			# 查询权限
			# 用JS方便点击‘查询权限’按钮旁边的倒三角形
			js_click("xpath", "//span[text()='查询权限']/parent::*//descendant::*[3]")
			sleep(1)

			click("xpath", "//div[contains(text(),'选择全部')]")
			sleep(1)

			# # 结算权限
			# # 用JS方便点击‘查询权限’按钮旁边的倒三角形
			# js_click("xpath", "//span[text()='结算权限']/parent::*//descendant::*[3]")
			# sleep(1)
			#
			# click("xpath", "//div[contains(text(),'选择全部')]")
			# sleep(1)
			#
			# 点击保存按钮
			click("xpath", "//span[text()='保存']")
			sleep(1)

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("任务命令权限，用户分配操作成功！")
			logging.info("任务命令权限，用户分配操作成功！")
			time.sleep(3)

			# 任务命令权限重置
			# 进入任务命令权限的iframe窗体
			switch_to("xpath", "//iframe[@id='taskRightConfig-tab-iframe']")
			# 点击系统参数权限用户分配
			click("xpath", "//span[text()='任务命令用户分配']")
			sleep(1)
			# 进入任务命令用户分配窗体
			switch_to("xpath", "//iframe[@id='subTabTwo-iframe']")

			# 点击勾选数据
			# 勾选
			click("xpath", "//div[@title='用户名称:田遍地']/parent::*/preceding-sibling::*[2]/descendant::*[2]")
			sleep(1)

			# 点击任务命令权限重置
			click("xpath", "//span[text()='任务命令权限重置']")
			sleep(1)

			# 跳转进入任务命令权限重置的窗体
			switch_to("xpath", "//iframe[@id='resetWin-iframe']")
			sleep(1)

			# 查询权限
			# 用JS方便点击‘查询权限’按钮旁边的倒三角形
			js_click("xpath", "//span[text()='查询权限']/parent::*//descendant::*[3]")
			sleep(1)

			click("xpath", "//div[contains(text(),'选择全部')]")
			sleep(1)

			# 点击保存按钮
			click("xpath", "//span[text()='保存']")
			sleep(1)

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("任务命令权限，用户重置操作成功！")
			logging.info("任务命令权限，用户重置操作成功！")
			time.sleep(3)

			# 缺少本组织账户权限初始

			# 缺少可操作组织账户权限初始

			# 再次点击基础设置菜单，使之关闭
			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='任务权限分配']/child::*[1]")

			# 打印操作成功日志
			print("任务权限分配，操作成功!")
			logging.info("任务权限分配，操作成功!")
			time.sleep(2)

		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("任务权限分配,失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)

		# 交易类型权限分配
		try:
			# 点击系统设置
			click("xpath", "//div[@class='sysconfigset']")
			# 进入系统设置的iframe窗体
			switch_to("xpath", "//iframe[@id='systemconfig-tab-iframe']")
			logging.info("开始测试信息权限--交易类型权限分配功能")
			sleep(1)
			click("xpath", "//span[text()='信息权限']")

			# 点击交易类型权限分配
			click("xpath", "//span[text()='交易类型权限分配']")
			sleep(1)
			switch_default()

			# 进入交易类型权限分配的iframe窗体
			switch_to("xpath", "//iframe[@id='payTypeRightConfig-tab-iframe']")
			# 进入交易类型权限分配窗体
			switch_to("xpath", "//iframe[@id='subTabOne-iframe']")

			# 点击勾选数据
			# 勾选
			click("xpath", "//div[@title='角色代码:fh']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
			sleep(1)

			# 点击交易类型权限分配
			click("xpath", "//span[text()='交易类型权限分配']")
			sleep(1)

			# 跳转进入交易类型权限分配的窗体
			switch_to("xpath", "//iframe[@id='distributeWin-iframe']")
			sleep(1)

			# 查询权限
			# 用JS方便点击‘查询权限’按钮旁边的倒三角形
			js_click("xpath", "//span[text()='查询权限']/parent::*//descendant::*[3]")
			sleep(1)

			click("xpath", "//div[contains(text(),'选择全部')]")
			sleep(1)

			# 点击保存按钮
			click("xpath", "//span[text()='保存']")
			sleep(1)

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("交易类型权限，角色分配操作成功！")
			logging.info("交易类型权限，角色分配操作成功！")
			time.sleep(3)

			# 交易类型权限重置
			# 进入交易类型权限分配的iframe窗体
			switch_to("xpath", "//iframe[@id='payTypeRightConfig-tab-iframe']")
			# 进入交易类型权限分配窗体
			switch_to("xpath", "//iframe[@id='subTabOne-iframe']")

			# 点击勾选数据
			# 勾选
			click("xpath", "//div[@title='角色代码:fh']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
			sleep(1)

			# 点击交易类型权限重置
			click("xpath", "//span[text()='交易类型权限重置']")
			sleep(1)

			# 跳转进入交易类型权限的窗体
			switch_to("xpath", "//iframe[@id='resetWin-iframe']")
			sleep(1)

			# 查询权限
			# 用JS方便点击‘查询权限’按钮旁边的倒三角形
			js_click("xpath", "//span[text()='查询权限']/parent::*//descendant::*[3]")
			sleep(1)

			click("xpath", "//div[contains(text(),'选择全部')]")
			sleep(1)

			# 点击保存按钮
			click("xpath", "//span[text()='保存']")
			sleep(1)

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("交易类型权限，重置操作成功！")
			logging.info("交易类型权限，重置操作成功！")
			time.sleep(3)

			# 交易类型权限用户分配
			# 进入交易类型权限分配的iframe窗体
			switch_to("xpath", "//iframe[@id='payTypeRightConfig-tab-iframe']")
			# 点击交易类型权限用户分配
			click("xpath", "//span[text()='交易类型权限用户分配']")
			sleep(1)
			# 进入交易类型权限用户分配窗体
			switch_to("xpath", "//iframe[@id='subTabTwo-iframe']")

			# 点击勾选数据
			# 勾选
			click("xpath", "//div[@title='用户名称:田遍地']/parent::*/preceding-sibling::*[2]/descendant::*[2]")
			sleep(1)

			# 点击交易类型权限分配
			click("xpath", "//span[text()='交易类型权限分配']")
			sleep(1)

			# 跳转进入系统参数权限分配的窗体
			switch_to("xpath", "//iframe[@id='distributeWin-iframe']")
			sleep(1)

			# 查询权限
			# 用JS方便点击‘查询权限’按钮旁边的倒三角形
			js_click("xpath", "//span[text()='查询权限']/parent::*//descendant::*[3]")
			sleep(1)

			click("xpath", "//div[contains(text(),'选择全部')]")
			sleep(1)

			# 点击保存按钮
			click("xpath", "//span[text()='保存']")
			sleep(1)

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("交易类型权限，用户分配操作成功！")
			logging.info("交易类型权限，用户分配操作成功！")
			time.sleep(3)

			# 任务命令权限重置
			# 进入任务命令权限的iframe窗体
			switch_to("xpath", "//iframe[@id='payTypeRightConfig-tab-iframe']")
			# 点击交易类型权限用户分配
			click("xpath", "//span[text()='交易类型权限用户分配']")
			sleep(1)
			# 进入交易类型权限用户分配窗体
			switch_to("xpath", "//iframe[@id='subTabTwo-iframe']")

			# 点击勾选数据
			# 勾选
			click("xpath", "//div[@title='用户名称:田遍地']/parent::*/preceding-sibling::*[2]/descendant::*[2]")
			sleep(1)

			# 点击交易类型权限重置
			click("xpath", "//span[text()='交易类型权限重置']")
			sleep(1)

			# 跳转进入交易类型权限重置的窗体
			switch_to("xpath", "//iframe[@id='resetWin-iframe']")
			sleep(1)

			# 查询权限
			# 用JS方便点击‘查询权限’按钮旁边的倒三角形
			js_click("xpath", "//span[text()='查询权限']/parent::*//descendant::*[3]")
			sleep(1)

			click("xpath", "//div[contains(text(),'选择全部')]")
			sleep(1)

			# 点击保存按钮
			click("xpath", "//span[text()='保存']")
			sleep(1)

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("交易类型权限，用户重置操作成功！")
			logging.info("交易类型权限，用户重置操作成功！")
			time.sleep(3)

			# 缺少本组织账户权限初始

			# 缺少可操作组织账户权限初始

			# 再次点击基础设置菜单，使之关闭
			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='交易类型权限分配']/child::*[1]")

			# 打印操作成功日志
			print("交易类型权限分配，操作成功!")
			logging.info("交易类型权限分配，操作成功!")
			time.sleep(2)

		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("交易类型权限分配,失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		
		# 部门权限分配
		try:
			# 点击系统设置
			click("xpath", "//div[@class='sysconfigset']")
			# 进入系统设置的iframe窗体
			switch_to("xpath", "//iframe[@id='systemconfig-tab-iframe']")
			logging.info("开始测试信息权限--部门权限分配功能")
			sleep(1)
			click("xpath", "//span[text()='信息权限']")

			# 点击部门权限分配
			click("xpath", "//span[text()='部门权限分配']")
			sleep(1)
			switch_default()

			# 进入部门权限分配的iframe窗体
			switch_to("xpath", "//iframe[@id='deptrightConfig-tab-iframe']")
			# 进入部门权限分配窗体
			switch_to("xpath", "//iframe[@id='subTabOne-iframe']")

			# 点击勾选数据
			# 勾选
			click("xpath", "//div[@title='角色代码:fh']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
			sleep(1)

			# 点击交易类型权限分配
			click("xpath", "//span[text()='部门权限分配']")
			sleep(1)

			# 跳转进入部门权限分配的窗体
			switch_to("xpath", "//iframe[@id='distributeWin-iframe']")
			sleep(1)

			# 查询权限
			# 用JS方便点击‘查询权限’按钮旁边的倒三角形
			js_click("xpath", "//span[text()='查询权限']/parent::*//descendant::*[3]")
			sleep(1)

			click("xpath", "//div[contains(text(),'选择全部')]")
			sleep(1)

			# 点击保存按钮
			click("xpath", "//span[text()='保存']")
			sleep(1)

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("部门权限，角色分配操作成功！")
			logging.info("部门权限，角色分配操作成功！")
			time.sleep(3)

			# 部门权限重置
			# 进入部门权限分配的iframe窗体
			switch_to("xpath", "//iframe[@id='deptrightConfig-tab-iframe']")
			# 进入部门权限分配窗体
			switch_to("xpath", "//iframe[@id='subTabOne-iframe']")

			# 点击勾选数据
			# 勾选
			click("xpath", "//div[@title='角色代码:fh']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
			sleep(1)

			# 点击部门权限重置
			click("xpath", "//span[text()='部门权限重置']")
			sleep(1)

			# 跳转进入部门权限的窗体
			switch_to("xpath", "//iframe[@id='resetWin-iframe']")
			sleep(1)

			# 查询权限
			# 用JS方便点击‘查询权限’按钮旁边的倒三角形
			js_click("xpath", "//span[text()='查询权限']/parent::*//descendant::*[3]")
			sleep(1)

			click("xpath", "//div[contains(text(),'选择全部')]")
			sleep(1)

			# 点击保存按钮
			click("xpath", "//span[text()='保存']")
			sleep(1)

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("部门权限，重置操作成功！")
			logging.info("部门权限，重置操作成功！")
			time.sleep(3)

			# 部门权限用户分配
			# 进入部门权限分配的iframe窗体
			switch_to("xpath", "//iframe[@id='deptrightConfig-tab-iframe']")
			# 点击部门用户分配
			click("xpath", "//span[text()='部门用户分配']")
			sleep(1)
			# 进入部门用户分配窗体
			switch_to("xpath", "//iframe[@id='subTabTwo-iframe']")

			# 点击勾选数据
			# 勾选
			click("xpath", "//div[@title='用户名称:田遍地']/parent::*/preceding-sibling::*[2]/descendant::*[2]")
			sleep(1)

			# 点击部门权限分配
			click("xpath", "//span[text()='部门权限分配']")
			sleep(1)

			# 跳转进入部门权限分配的窗体
			switch_to("xpath", "//iframe[@id='distributeWin-iframe']")
			sleep(1)

			# 查询权限
			# 用JS方便点击‘查询权限’按钮旁边的倒三角形
			js_click("xpath", "//span[text()='查询权限']/parent::*//descendant::*[3]")
			sleep(1)

			click("xpath", "//div[contains(text(),'选择全部')]")
			sleep(1)

			# 点击保存按钮
			click("xpath", "//span[text()='保存']")
			sleep(1)

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("部门权限，用户分配操作成功！")
			logging.info("部门权限，用户分配操作成功！")
			time.sleep(3)

			# 部门权限重置
			# 进入部门权限的iframe窗体
			switch_to("xpath", "//iframe[@id='deptrightConfig-tab-iframe']")
			# 点击部门用户分配
			click("xpath", "//span[text()='部门用户分配']")
			sleep(1)
			# 进入部门用户分配窗体
			switch_to("xpath", "//iframe[@id='subTabTwo-iframe']")

			# 点击勾选数据
			# 勾选
			click("xpath", "//div[@title='用户名称:田遍地']/parent::*/preceding-sibling::*[2]/descendant::*[2]")
			sleep(1)

			# 点击部门权限重置
			click("xpath", "//span[text()='部门权限重置']")
			sleep(1)

			# 跳转进入部门权限重置的窗体
			switch_to("xpath", "//iframe[@id='resetWin-iframe']")
			sleep(1)

			# 查询权限
			# 用JS方便点击‘查询权限’按钮旁边的倒三角形
			js_click("xpath", "//span[text()='查询权限']/parent::*//descendant::*[3]")
			sleep(1)

			click("xpath", "//div[contains(text(),'选择全部')]")
			sleep(1)

			# 点击保存按钮
			click("xpath", "//span[text()='保存']")
			sleep(1)

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("部门权限，用户重置操作成功！")
			logging.info("部门权限，用户重置操作成功！")
			time.sleep(3)

			# 缺少本组织账户权限初始

			# 缺少可操作组织账户权限初始

			# 再次点击基础设置菜单，使之关闭
			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='部门权限分配']/child::*[1]")

			# 打印操作成功日志
			print("部门权限分配，操作成功!")
			logging.info("部门权限分配，操作成功!")
			time.sleep(2)

		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("部门权限分配,失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
	
		# 工程项目分配
		try:
			# 点击系统设置
			click("xpath", "//div[@class='sysconfigset']")
			# 进入系统设置的iframe窗体
			switch_to("xpath", "//iframe[@id='systemconfig-tab-iframe']")
			logging.info("开始测试信息权限--工程项目权限分配功能")
			sleep(1)
			click("xpath", "//span[text()='信息权限']")
			
			# 点击工程项目权限分配
			click("xpath", "//span[text()='工程项目权限分配']")
			sleep(1)
			switch_default()
			
			# 进入工程项目权限分配的iframe窗体
			switch_to("xpath", "//iframe[@id='projectRightConfig-tab-iframe']")
			# 进入工程项目权限分配窗体
			switch_to("xpath", "//iframe[@id='subTabOne-iframe']")
			
			# 点击勾选数据
			# 勾选
			click("xpath", "//div[@title='角色代码:fh']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
			sleep(1)
			
			# 点击工程项目权限分配
			click("xpath", "//span[text()='工程项目权限分配']")
			sleep(1)
			
			# 跳转进入工程项目权限分配的窗体
			switch_to("xpath", "//iframe[@id='distributeWin-iframe']")
			sleep(1)
			
			# 查询权限
			# 用JS方便点击‘查询权限’按钮旁边的倒三角形
			js_click("xpath", "//span[text()='操作权限']/parent::*//descendant::*[3]")
			sleep(1)
			
			click("xpath", "//div[contains(text(),'选择全部')]")
			sleep(1)
			
			# 点击保存按钮
			click("xpath", "//span[text()='保存']")
			sleep(1)
			
			# 退出所有iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("工程项目权限，角色分配操作成功！")
			logging.info("工程项目权限，角色分配操作成功！")
			time.sleep(3)
			
			# 工程项目权限重置
			# 进入工程项目权限分配的iframe窗体
			switch_to("xpath", "//iframe[@id='projectRightConfig-tab-iframe']")
			# 进入工程项目权限分配窗体
			switch_to("xpath", "//iframe[@id='subTabOne-iframe']")
			
			# 点击勾选数据
			# 勾选
			click("xpath", "//div[@title='角色代码:fh']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
			sleep(1)
			
			# 点击部门权限重置
			click("xpath", "//span[text()='工程项目权限重置']")
			sleep(1)
			
			# 跳转进入工程项目权限的窗体
			switch_to("xpath", "//iframe[@id='resetWin-iframe']")
			sleep(1)
			
			# 查询权限
			# 用JS方便点击‘查询权限’按钮旁边的倒三角形
			js_click("xpath", "//span[text()='操作权限']/parent::*//descendant::*[3]")
			sleep(1)
			
			click("xpath", "//div[contains(text(),'选择全部')]")
			sleep(1)
			
			# 点击保存按钮
			click("xpath", "//span[text()='保存']")
			sleep(1)
			
			# 退出所有iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("工程项目权限，重置操作成功！")
			logging.info("工程项目权限，重置操作成功！")
			time.sleep(3)
			
			# 工程项目权限分配
			# 进入工程项目权限分配的iframe窗体
			switch_to("xpath", "//iframe[@id='projectRightConfig-tab-iframe']")
			# 点击工程项目权限分配
			click("xpath", "//span[text()='工程项目权限用户分配']")
			sleep(1)
			# 进入工程项目权限分配窗体
			switch_to("xpath", "//iframe[@id='subTabTwo-iframe']")
			
			# 点击勾选数据
			# 勾选
			click("xpath", "//div[@title='用户名称:田遍地']/parent::*/preceding-sibling::*[2]/descendant::*[2]")
			sleep(1)
			
			# 点击工程项目权限分配
			click("xpath", "//span[text()='工程项目权限分配']")
			sleep(1)
			
			# 跳转进入工程项目权限分配的窗体
			switch_to("xpath", "//iframe[@id='distributeWin-iframe']")
			sleep(1)
			
			# 查询权限
			# 用JS方便点击‘查询权限’按钮旁边的倒三角形
			js_click("xpath", "//span[text()='操作权限']/parent::*//descendant::*[3]")
			sleep(1)
			
			click("xpath", "//div[contains(text(),'选择全部')]")
			sleep(1)
			
			# 点击保存按钮
			click("xpath", "//span[text()='保存']")
			sleep(1)
			
			# 退出所有iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("工程项目权限，用户分配操作成功！")
			logging.info("工程项目权限，用户分配操作成功！")
			time.sleep(3)
			
			# 工程项目权限重置
			# 进入工程项目权限的iframe窗体
			switch_to("xpath", "//iframe[@id='projectRightConfig-tab-iframe']")
			# 点击工程项目权限用户分配
			click("xpath", "//span[text()='工程项目权限用户分配']")
			sleep(1)
			# 进入工程项目权限用户分配窗体
			switch_to("xpath", "//iframe[@id='subTabTwo-iframe']")
			
			# 点击勾选数据
			# 勾选
			click("xpath", "//div[@title='用户名称:田遍地']/parent::*/preceding-sibling::*[2]/descendant::*[2]")
			sleep(1)
			
			# 点击部门权限重置
			click("xpath", "//span[text()='工程项目权限重置']")
			sleep(1)
			
			# 跳转进入部门权限重置的窗体
			switch_to("xpath", "//iframe[@id='resetWin-iframe']")
			sleep(1)
			
			# 查询权限
			# 用JS方便点击‘查询权限’按钮旁边的倒三角形
			js_click("xpath", "//span[text()='操作权限']/parent::*//descendant::*[3]")
			sleep(1)
			
			click("xpath", "//div[contains(text(),'选择全部')]")
			sleep(1)
			
			# 点击保存按钮
			click("xpath", "//span[text()='保存']")
			sleep(1)
			
			# 退出所有iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("工程项目权限，用户重置操作成功！")
			logging.info("工程项目权限，用户重置操作成功！")
			time.sleep(3)
			
			# 再次点击基础设置菜单，使之关闭
			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='工程项目权限分配']/child::*[1]")
			
			# 点击关闭系统设置
			js_click("xpath", "//a[@title='系统设置']/child::*[1]")
			
			# 打印操作成功日志
			print("工程项目权限分配，操作成功!")
			logging.info("工程项目权限分配，操作成功!")
			time.sleep(2)
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("工程项目权限分配,失败！" + str(traceback.format_exc()))
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