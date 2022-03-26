# encoding=utf-8
# @Time : 2020/8/28 10:42
# @Author : Mindy
# 此文件是测试MySQL版本资金结算管理--外币收付结算--全球汇款--其他支付
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


class Test_Qqhk_Qtzf_Mysql(unittest.TestCase):
	
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
		
		# 开始测试资金系统收付--集中付款--其他支付
		# 测试集中付款--其他支付
		try:
			# 点击'资金系统收付'菜单
			click("xpath", "//span[text()='资金系统收付']")
			# 点击集中付款菜单
			click("xpath", "//span[text()='集中付款']")
			# 退出所有iframe窗体
			switch_default()
			
			for i in range(1, 3):
				
				# 没有启动系统参数的情况下点击支付
				if i == 1:
					# 没有启动系统参数的情况下点击支付
					# 支付
					# 切入‘其他支付’的iframe窗体
					switch_to("xpath", "//iframe[@id='massPayment-tab-iframe']")
					sleep(1)
					
					# 点击其他支付
					click("xpath", "//span[text()='其他支付']")
					
					# 进入其他支付的iframe窗体
					switch_to("xpath", "//iframe[@id='subTabFive-iframe']")
					sleep(1)
					
					# 点击查看
					# 用JS的方法点击放大镜
					js_click("xpath", "//span[@class='f-contrac-close']")
					sleep(1)
					
					# 选未审批、未支付的数据直接确认支付
					click("xpath", "//input[@id='combobox-input-approvestate']")
					sleep(1)
					# 点击未审批
					click("xpath", "//div[@title='未审批']")
					sleep(1)
					click("xpath", "//div[@title='审批中']")
					sleep(1)
					click("xpath", "//div[@title='已审批']")
					sleep(1)
					
					# 输入支付状态：未支付
					click("xpath", "//input[@id='combobox-input-paystate']")
					sleep(1)
					# 点击未审批
					click("xpath", "//div[@title='未收付']")
					sleep(1)
					
					# 点击查询
					click("xpath", "//span[text()='查询']")
					sleep(1)
					
					# 勾选数据
					click("xpath",
					      "//div[@title='收款户名:Mindy科技有限公司']/parent::*/preceding-sibling::*[8]/descendant::*[2]")
					sleep(1)
					
					# 点击确认支付按钮
					click("xpath", "//span[text()='确认支付']")
					sleep(1)
					
					# 点击确定
					click("xpath", "//span[text()='确定']")
					sleep(1)
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("其他支付，支付成功！")
					logging.info("其他支付，支付成功！")
					time.sleep(3)
				
				# 第一笔，就先修改，再修改页面提交送审，再撤销送审，再删除
				if i == 2:
					# 修改系统参数--其它支付是否启用审批流
					
					# 点击系统参数
					click("xpath", "//div[@class='sysconfigset']")
					switch_to("xpath", "//iframe[@id='systemconfig-tab-iframe']")
					sleep(1)
					click("xpath", "//span[text()='系统参数']")
					switch_to("xpath", "//iframe[@id='tabs3-gen-2-iframe']")
					
					# 用JS的方法点击放大镜
					js_click("xpath", "//span[@class='f-contrac-close']")
					sleep(1)
					click("xpath", "//input[@id='combobox-input-paramurids']")
					sleep(1)
					input("xpath", "//input[@id='combobox-input-paramurids']", "其它支付是否启用工作流")
					sleep(1)
					click("xpath",
					      "//div[@title='代码-名称:其它支付是否启用工作流']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
					# 点击查询
					click("xpath", "//span[text()='查询']")
					sleep(1)
					
					click("xpath", "//span[text()='其它支付是否启用工作流']/ancestor::*[8]/descendant::*[28]")
					
					click("xpath", "//span[text()='修改']")
					
					# 切入修改的iframe窗体
					switch_to("xpath", "//iframe[@id='modWin-iframe']")
					sleep(1)
					
					# 点击单选值
					click("xpath", "//input[@id='value_check']")
					sleep(1)
					
					click("xpath", "//span[text()='保存']")
					
					switch_default()
					
					# 用隐式等待方法等页面出现删除的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功')]")
					print("系统参数，修改成功！")
					time.sleep(3)
					
					# 再次点击基础设置菜单，使之关闭
					# 用JS的方法关闭当前页面
					js_click("xpath", "//a[@title='系统设置']/child::*[1]")
					
					# 打印操作成功日志
					print("修改系统参数，操作成功!")
					logging.info("修改系统参数，操作成功!")
					time.sleep(2)
					
					# 切入‘其他支付’的iframe窗体
					switch_to("xpath", "//iframe[@id='massPayment-tab-iframe']")
					sleep(1)
					
					# 点击其他支付
					click("xpath", "//span[text()='其他支付']")
					
					# 进入其他支付的iframe窗体
					switch_to("xpath", "//iframe[@id='subTabFive-iframe']")
					sleep(1)
					
					# 勾选数据
					click("xpath",
					      "//div[@title='收款户名:Mindy科技有限公司']/parent::*/preceding-sibling::*[8]/descendant::*[2]")
					sleep(1)
					
					# 点击送审按钮
					click("xpath", "//span[text()='送审']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！送审成功1笔，失败0笔。')]")
					print("集中付款-其他支付，送审成功！")
					logging.info("集中付款-其他支付，送审成功！")
					time.sleep(3)
					
					switch_to("xpath", "//iframe[@id='massPayment-tab-iframe']")
					sleep(1)
					
					# 点击其他支付
					click("xpath", "//span[text()='其他支付']")
					
					# 进入其他支付的iframe窗体
					switch_to("xpath", "//iframe[@id='subTabFive-iframe']")
					sleep(1)
					
					# 选未审批、未支付的数据直接确认支付
					click("xpath", "//input[@id='combobox-input-approvestate']")
					sleep(1)
					
					# 点击未审批
					click("xpath", "//div[@title='未审批']")
					sleep(1)
					# 选择审批中的数据
					click("xpath", "//div[@title='审批中']")
					sleep(1)
					
					# 点击查询
					click("xpath", "//span[text()='查询']")
					sleep(1)
					
					# 修改勾选数据
					click("xpath",
					      "//div[@title='收款户名:Mindy科技有限公司']/parent::*/preceding-sibling::*[8]/descendant::*[2]")
					
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
					print("集中付款-其他支付，撤销送审成功！")
					logging.info("集中付款-其他支付，撤销送审成功！")
					time.sleep(3)
					
					# 切入‘其他支付’的iframe窗体
					switch_to("xpath", "//iframe[@id='massPayment-tab-iframe']")
					sleep(1)
					
					# 点击其他支付
					click("xpath", "//span[text()='其他支付']")
					
					# 进入其他支付的iframe窗体
					switch_to("xpath", "//iframe[@id='subTabFive-iframe']")
					sleep(1)
					
					# 选未审批、未支付的数据直接确认支付
					click("xpath", "//input[@id='combobox-input-approvestate']")
					sleep(1)
					# 选择审批中的数据
					click("xpath", "//div[@title='审批中']")
					sleep(1)
					# 点击未审批
					click("xpath", "//div[@title='未审批']")
					sleep(1)
					
					# 点击查询
					click("xpath", "//span[text()='查询']")
					sleep(1)
					
					# 修改勾选数据
					click("xpath",
					      "//div[@title='收款户名:Mindy科技有限公司']/parent::*/preceding-sibling::*[8]/descendant::*[2]")
					
					# 点击送审按钮
					click("xpath", "//span[text()='送审']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！送审成功1笔，失败0笔。')]")
					print("集中付款-其他支付，送审成功！")
					logging.info("集中付款-其他支付，送审成功！")
					time.sleep(3)
					
					# 切入‘其他支付’的iframe窗体
					switch_to("xpath", "//iframe[@id='massPayment-tab-iframe']")
					sleep(1)
					
					# 点击其他支付
					click("xpath", "//span[text()='其他支付']")
					
					# 进入其他支付的iframe窗体
					switch_to("xpath", "//iframe[@id='subTabFive-iframe']")
					sleep(1)
					
					# 选未审批、未支付的数据直接确认支付
					click("xpath", "//input[@id='combobox-input-approvestate']")
					sleep(1)
					
					# 点击未审批
					click("xpath", "//div[@title='未审批']")
					sleep(1)
					# 选择审批中的数据
					click("xpath", "//div[@title='审批中']")
					sleep(1)
					
					# 点击查询
					click("xpath", "//span[text()='查询']")
					sleep(1)
					
					# 修改勾选数据
					double_click("xpath",
					             "//div[@title='收款户名:Mindy科技有限公司']/parent::*/preceding-sibling::*[8]/descendant::*[2]")
					sleep(1)
					
					switch_to("xpath", "//iframe[@id='wf_taskProcessing_win-iframe']")
					sleep(1)
					
					click("xpath", "//span[text()='同意']")
					sleep(1)
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("其他支付，审批成功！")
					logging.info("其他支付，审批成功！")
					time.sleep(3)
					
					# 确认支付
					# 切入‘其他支付’的iframe窗体
					switch_to("xpath", "//iframe[@id='massPayment-tab-iframe']")
					sleep(1)
					
					# 点击其他支付
					click("xpath", "//span[text()='其他支付']")
					
					# 进入其他支付的iframe窗体
					switch_to("xpath", "//iframe[@id='subTabFive-iframe']")
					sleep(1)
					
					# 勾选数据
					click("xpath",
					      "//div[@title='收款户名:Mindy科技有限公司']/parent::*/preceding-sibling::*[8]/descendant::*[2]")
					sleep(1)
					
					# 点击确认支付按钮
					click("xpath", "//span[text()='确认支付']")
					sleep(1)
					
					# 点击确定
					click("xpath", "//span[text()='确定']")
					sleep(1)
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！1笔进行了支付，0笔不允许支付。')]")
					print("其他支付，支付成功！")
					logging.info("其他支付，支付成功！")
					time.sleep(3)
					
					# 修改系统参数--其它支付是否启用审批流
					
					# 点击系统参数
					click("xpath", "//div[@class='sysconfigset']")
					switch_to("xpath", "//iframe[@id='systemconfig-tab-iframe']")
					sleep(1)
					click("xpath", "//span[text()='系统参数']")
					switch_to("xpath", "//iframe[@id='tabs3-gen-2-iframe']")
					
					# 用JS的方法点击放大镜
					js_click("xpath", "//span[@class='f-contrac-close']")
					sleep(1)
					click("xpath", "//input[@id='combobox-input-paramurids']")
					sleep(1)
					input("xpath", "//input[@id='combobox-input-paramurids']", "其它支付是否启用工作流")
					sleep(1)
					click("xpath",
					      "//div[@title='代码-名称:其它支付是否启用工作流']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
					# 点击查询
					click("xpath", "//span[text()='查询']")
					sleep(1)
					
					click("xpath", "//span[text()='其它支付是否启用工作流']/ancestor::*[8]/descendant::*[28]")
					
					click("xpath", "//span[text()='修改']")
					
					# 切入修改的iframe窗体
					switch_to("xpath", "//iframe[@id='modWin-iframe']")
					sleep(1)
					
					# 点击单选值
					click("xpath", "//input[@id='value_check']")
					sleep(1)
					
					click("xpath", "//span[text()='保存']")
					
					switch_default()
					
					# 用隐式等待方法等页面出现删除的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功')]")
					print("系统参数，修改成功！")
					time.sleep(3)
			
			switch_default()
			
			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='集中付款']/child::*[1]")
			
			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//span[text()='资金系统收付']")
			# 打印操作成功日志
			print("其他支付，操作成功!")
			logging.info("其他支付，操作成功!")
			time.sleep(2)
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("其他支付失败！" + str(traceback.format_exc()))
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