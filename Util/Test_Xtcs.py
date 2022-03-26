# encoding=utf-8
# @Time : 2020/8/14 14:49
# @Author : Mindy
# 此文件是测试系统设置系统参数
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


class Test_Xtcs(unittest.TestCase):
	
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
		
		logging.info("开始测试系统参数功能")

		# 系统参数
		try:
			
			# # 点击系统设置
			click("xpath", "//div[@class='sysconfigset']")
			switch_to("xpath", "//iframe[@id='systemconfig-tab-iframe']")
			sleep(1)
			click("xpath", "//span[text()='系统参数']")
			switch_to("xpath", "//iframe[@id='tabs3-gen-2-iframe']")
			
			# 点击新增按钮
			js_click("xpath", "//span[text()='新增']")

			# 切入新增的iframe窗体
			switch_to("xpath", "//iframe[@id='addWin-iframe']")
			sleep(1)

			# 下拉选择
			click("xpath", "//input[@id='combobox-input-paramdefid']")
			sleep(1)
			input_down("xpath", "//input[@id='combobox-input-paramdefid']")
			input_enter("xpath", "//input[@id='combobox-input-paramdefid']")
			sleep(1)

			# 点击保存
			click("xpath", "//span[text()='保存']")

			# 退出所有的iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("系统参数，新增保存成功！")
			logging.info("系统参数，新增保存成功！")
			time.sleep(3)
			
			# 进入系统设置窗体
			switch_to("xpath", "//iframe[@id='systemconfig-tab-iframe']")
			sleep(1)
			click("xpath", "//span[text()='系统参数']")
			switch_to("xpath", "//iframe[@id='tabs3-gen-2-iframe']")
			
			# 用JS的方法点击放大镜
			js_click("xpath", "//span[@class='f-contrac-close']")
			sleep(1)
			
			# 选择修改的系统参数
			click("xpath", "//input[@id='combobox-input-paramurids']")
			sleep(1)
			input("xpath", "//input[@id='combobox-input-paramurids']", "是否启用附件上传")
			sleep(1)
			click("xpath", "//div[@title='代码-名称:是否启用附件上传']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
			
			# 点击查询
			click("xpath", "//span[text()='查询']")
			sleep(1)

			click("xpath", "//span[text()='是否启用附件上传']/ancestor::*[8]/descendant::*[28]")

			click("xpath", "//span[text()='修改']")

			# 切入修改的iframe窗体
			switch_to("xpath", "//iframe[@id='modWin-iframe']")
			sleep(1)
			
			# 修改参数值
			click("xpath", "//input[@id='value_check']")
			sleep(1)

			# 点击保存按钮
			click("xpath", "//span[text()='保存']")

			switch_default()

			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功')]")
			print("系统参数，修改成功！")
			time.sleep(3)
			
			# 删除功能暂不做
			
			# 再次点击基础设置菜单，使之关闭
			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='系统设置']/child::*[1]")
			
			# 打印操作成功日志
			print("修改系统参数，操作成功!")
			logging.info("修改系统参数，操作成功!")
			time.sleep(2)
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("系统参数功能,失败！" + str(traceback.format_exc()))
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