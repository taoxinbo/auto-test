# encoding=utf-8
# @Time : 2020/10/22 13:30
# @Author : zzg
# 此文件是测试MySQL版本资金结算管理--资金系统收付--集中付款--可操作组织直联批量付款
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


class Test_Jzfk_Kcz_Zlplfk_Mysql(unittest.TestCase):
	
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
		
		# 开始测试资金系统收付--集中付款--可操作组织直联批量付款
		# 测试集中付款--可操作组织直联批量付款
		try:
			# 点击'资金系统收付'菜单
			click("xpath", "//span[text()='资金系统收付']")
			# 点击集中付款菜单
			#click("xpath", "//span[text()='集中付款']")
			span_click("集中付款")
			print("测试成功")
			# 退出所有iframe窗体
			switch_default()
			
			for i in range(1, 3):
				
				# 第一笔，就先修改，再修改页面提交送审，再撤销送审，再删除
				if i == 1:
					# 切入‘可操作组织直联批量付款’的iframe窗体
					switch_to("xpath", "//iframe[@id='massPayment-tab-iframe']")
					sleep(1)
					
					# 点击可操作组织直联批量付款
					click("xpath", "//span[text()='可操作组织直联批量付款']")
					
					# 进入可操作组织直联批量付款的iframe窗体
					switch_to("xpath", "//iframe[@id='subTabFour-iframe']")
					sleep(1)
					
					# 点击查看
					# 用JS的方法点击放大镜
					js_click("xpath", "//span[@class='f-contrac-close']")
					sleep(1)
					
					# 支付状态
					click("xpath", "//input[@id='combobox-input-paystate']")
					sleep(1)
					input("xpath", "//input[@id='combobox-input-paystate']", "未收付")
					sleep(1)
					click("xpath", "//div[@title='未收付']")
					sleep(1)
					
					# 点击查询
					click("xpath", "//span[text()='查询']")
					
					# 修改勾选数据
					click("xpath", "//div[@title='未审批笔数:1']/parent::*/preceding-sibling::*[9]/descendant::*[2]")
					
					# 点击送审按钮
					click("xpath", "//span[text()='送审']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！送审成功1笔，失败0笔。')]")
					print("集中付款-直联批量支付，送审成功！")
					logging.info("集中付款-直联批量支付，送审成功！")
					time.sleep(3)
					
					switch_to("xpath", "//iframe[@id='massPayment-tab-iframe']")
					sleep(1)
					
					# 点击可操作组织直联批量付款
					click("xpath", "//span[text()='可操作组织直联批量付款']")
					
					# 进入可操作组织直联批量付款的iframe窗体
					switch_to("xpath", "//iframe[@id='subTabFour-iframe']")
					sleep(1)
					
					# 修改勾选数据
					click("xpath", "//div[@title='审批中笔数:1']/parent::*/preceding-sibling::*[10]/descendant::*[2]")
					
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
					print("集中付款-直联批量支付，撤销送审成功！")
					logging.info("集中付款-直联批量支付，撤销送审成功！")
					time.sleep(3)
					
					# 切入‘可操作组织直联批量付款’的iframe窗体
					switch_to("xpath", "//iframe[@id='massPayment-tab-iframe']")
					sleep(1)
					
					# 点击可操作组织直联批量付款
					click("xpath", "//span[text()='可操作组织直联批量付款']")
					
					# 进入可操作组织直联批量付款的iframe窗体
					switch_to("xpath", "//iframe[@id='subTabFour-iframe']")
					sleep(1)
					
					# 修改勾选数据
					click("xpath", "//div[@title='未审批笔数:1']/parent::*/preceding-sibling::*[9]/descendant::*[2]")
					
					# 点击送审按钮
					click("xpath", "//span[text()='送审']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！送审成功1笔，失败0笔。')]")
					print("集中付款-直联批量支付，送审成功！")
					logging.info("集中付款-直联批量支付，送审成功！")
					time.sleep(3)
					
					# 切入‘可操作组织直联批量付款’的iframe窗体
					switch_to("xpath", "//iframe[@id='massPayment-tab-iframe']")
					sleep(1)
					
					# 点击可操作组织直联批量付款
					click("xpath", "//span[text()='可操作组织直联批量付款']")
					
					# 进入可操作组织直联批量付款的iframe窗体
					switch_to("xpath", "//iframe[@id='subTabFour-iframe']")
					sleep(1)
					
					# 修改勾选数据
					double_click("xpath", "//div[@title='审批中笔数:1']/parent::*/preceding-sibling::*[10]/descendant::*[2]")
					sleep(1)
					
					switch_to("xpath", "//iframe[@id='wf_taskProcessing_win-iframe']")
					sleep(1)
					
					click("xpath", "//span[text()='同意']")
					sleep(1)
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("直联批量支付，直联一审审批成功！")
					logging.info("直联批量支付，直联一审审批成功！")
					time.sleep(3)
					
					# 切入‘可操作组织直联批量付款’的iframe窗体
					switch_to("xpath", "//iframe[@id='massPayment-tab-iframe']")
					sleep(1)
					
					# 点击可操作组织直联批量付款
					click("xpath", "//span[text()='可操作组织直联批量付款']")
					
					# 进入可操作组织直联批量付款的iframe窗体
					switch_to("xpath", "//iframe[@id='subTabFour-iframe']")
					sleep(1)
					
					# 修改勾选数据
					double_click("xpath",
					             "//div[@title='审批中笔数:1']/parent::*/preceding-sibling::*[10]/descendant::*[2]")
					sleep(1)
					
					switch_to("xpath", "//iframe[@id='wf_taskProcessing_win-iframe']")
					sleep(1)
					
					click("xpath", "//span[text()='同意']")
					sleep(1)
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("直联批量支付，审批成功！")
					logging.info("直联批量支付，审批成功！")
					time.sleep(3)
					
					# 点击支付
					# 支付
					# 切入‘可操作组织直联批量付款’的iframe窗体
					switch_to("xpath", "//iframe[@id='massPayment-tab-iframe']")
					sleep(1)
					
					# 点击可操作组织直联批量付款
					click("xpath", "//span[text()='可操作组织直联批量付款']")
					
					# 进入可操作组织直联批量付款的iframe窗体
					switch_to("xpath", "//iframe[@id='subTabFour-iframe']")
					sleep(1)
					
					# 点击重置
					# 用JS方便点击‘查询’按钮旁边的倒三角形
					js_click("xpath", "//span[text()='查询']/parent::*/following-sibling::*/child::*")
					sleep(1)
					
					# 点击重置按钮
					click("xpath", "//a[contains(text(),'重置')]")
					sleep(1)
					
					# 勾选数据
					click("xpath", "//div[@title='已审批笔数:1']/parent::*/preceding-sibling::*[11]/descendant::*[2]")
					sleep(1)
					
					# 点击支付按钮
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
					implici_wait("xpath", "//span[contains(text(),'操作成功！1批进行了支付，0批不允许支付')]")
					print("直联批量支付，支付成功！")
					logging.info("直联批量支付，支付成功！")
					time.sleep(3)
					
					# 查询状态
					# 切入‘可操作组织直联批量付款’的iframe窗体
					switch_to("xpath", "//iframe[@id='massPayment-tab-iframe']")
					sleep(1)
					
					# 点击可操作组织直联批量付款
					click("xpath", "//span[text()='可操作组织直联批量付款']")
					
					# 进入可操作组织直联批量付款的iframe窗体
					switch_to("xpath", "//iframe[@id='subTabFour-iframe']")
					sleep(1)
					
					# 点击重置
					# 用JS方便点击‘查询’按钮旁边的倒三角形
					js_click("xpath", "//span[text()='查询']/parent::*/following-sibling::*/child::*")
					sleep(1)
					
					# 点击重置按钮
					click("xpath", "//a[contains(text(),'重置')]")
					sleep(1)
					
					# 勾选数据
					click("xpath", "//div[@title='支付未知笔数:1']/parent::*/preceding-sibling::*[20]/descendant::*[2]")
					sleep(1)
					
					# 点击查询支付状态
					click("xpath", "//span[text()='查询支付状态']")
					sleep(1)
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'数据已处理,请查看相应结果!')]")
					print("直联批量支付，查询状态成功！")
					logging.info("直联批量支付，查询状态成功")
					time.sleep(3)
					
					# 打印
					switch_to("xpath", "//iframe[@id='massPayment-tab-iframe']")
					sleep(1)
					
					# 点击可操作组织直联批量付款
					click("xpath", "//span[text()='可操作组织直联批量付款']")
					
					# 进入可操作组织直联批量付款的iframe窗体
					switch_to("xpath", "//iframe[@id='subTabFour-iframe']")
					sleep(1)
					
					
					
					# 勾选数据
					click("xpath", "//div[@title='已审批笔数:1']/parent::*/preceding-sibling::*[11]/descendant::*[2]")
					sleep(1)
					
					# 点击打印按钮
					click("xpath", "//span[text()='打印']")
					sleep(1)
					
					# 获取所有窗口句柄
					all_handles = self.driver.window_handles
					# 循环遍历所有新打开的窗口句柄，也就是说不包括主窗口
					now_handle = self.driver.current_window_handle
					for handle in all_handles:
						self.driver.switch_to.window(handle)
						if self.driver.title == u"payandrecbatchprint":
							implici_wait("xpath", "//td[contains(text(),'Mindy科技有限公司')]")
							print("直联批量支付，打印成功!！")
							time.sleep(3)
							self.driver.switch_to.window(now_handle)
							switch_default()
					
					# 打印记录
					# 切入‘可操作组织直联批量付款’的iframe窗体
					switch_to("xpath", "//iframe[@id='massPayment-tab-iframe']")
					sleep(1)
					
					# 点击可操作组织直联批量付款
					click("xpath", "//span[text()='可操作组织直联批量付款']")
					
					# 进入可操作组织直联批量付款的iframe窗体
					switch_to("xpath", "//iframe[@id='subTabFour-iframe']")
					sleep(1)
					
					# # 勾选数据
					# click("xpath", "//div[@title='支付类型名称:直联']/parent::*/preceding-sibling::*[6]/descendant::*[2]")
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
					print("直联批量支付，打印记录查看成功！")
					logging.info("直联批量支付，打印记录查看成功！")
					time.sleep(3)
					
					switch_parent()
					
					# 点击关闭页面
					click("xpath", "//span[text()='打印记录']/preceding-sibling::*[1]")
					sleep(1)
					
					switch_default()
				
				if i == 2:
					# 删除
					switch_to("xpath", "//iframe[@id='massPayment-tab-iframe']")
					sleep(1)
					
					# 点击可操作组织直联批量付款
					click("xpath", "//span[text()='可操作组织直联批量付款']")
					
					# 进入可操作组织直联批量付款的iframe窗体
					switch_to("xpath", "//iframe[@id='subTabFour-iframe']")
					sleep(1)
					
					# 支付状态
					click("xpath", "//input[@id='combobox-input-paystate']")
					sleep(1)
					input("xpath", "//input[@id='combobox-input-paystate']", "未收付")
					sleep(1)
					click("xpath", "//div[@title='未收付']")
					sleep(1)
					
					# 点击查询
					click("xpath", "//span[text()='查询']")
					
					# 勾选数据
					click("xpath", "//div[@title='未审批笔数:1']/parent::*/preceding-sibling::*[9]/descendant::*[2]")
					sleep(1)
					
					# 点击删除按钮
					click("xpath", "//span[text()='删除']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现删除的提示框
					implici_wait("xpath", "//span[contains(text(),'成功删除1条记录！')]")
					print("集中付款-直联批量支付，删除成功！")
					logging.info("集中付款-直联批量支付，删除成功！")
					time.sleep(3)
			
			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='集中付款']/child::*[1]")
			
			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//span[text()='资金系统收付']")
			# 打印操作成功日志
			print("直联批量支付，操作成功!")
			logging.info("直联批量支付，操作成功!")
			time.sleep(2)
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("直联批量支付失败！" + str(traceback.format_exc()))
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