# encoding=utf-8
# @Time : 2020/8/14 14:49
# @Author : Mindy
# 此文件是测试内部借款管理--担保管理模--担保申请
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


class Test_Dbsq(unittest.TestCase):
	
	# 启动浏览器
	def setUp(self):
		# 启动浏览器的另外一个方法：通过封装启动浏览器的驱动，启动不同浏览器
		self.driver = get("chrome")
	
	# 登陆系统、对系统设置进行操作
	def test_trade(self):
		# 通过登陆封装函数，进行登陆
		# login( G_Ora_Url,TestUser,Password, "自动化测试租户")
		# login( G_Ora_Url,Tao, Password,"默认租户")
		login(G_Mys_Url, mindy, Password, "亚唐科技")
		# login( G_Mys_Url,TestUser,Password, "自动化测试租户")
		# login(G_Mys_Url, Tao, Password, "默认租户")
		# login(G_Mys_Url, mindy, Password, "亚唐科技")
		# login(G_Mys_Url, judy, Password, "默认租户")
		# self.driver.get(G_Ora_Url)
		
		click("xpath", "//input[@id='combobox-input-orgidswitch']")
		sleep(1)
		clear("xpath", "//input[@id='combobox-input-orgidswitch']")
		sleep(1)
		input("xpath", "//input[@id='combobox-input-orgidswitch']", "Mindy科技有限公司")
		sleep(1)
		input_down("xpath", "//input[@id='combobox-input-orgidswitch']")
		input_enter("xpath", "//input[@id='combobox-input-orgidswitch']")
		sleep(2)
		
		logging.info("开始测试内部借款管理的页面功能")
		# 将页面的滚动条滑动到‘资金结算管理’页面的地方
		js_gd("xpath", "//span[contains(text(),'内部借款管理')]")
		# 用JS的方法点击资金结算管理菜单按钮
		js_click("xpath", "//span[contains(text(),'内部借款管理')]")
		
		# 测试担保管理--担保申请
		try:
			# 点击担保管理菜单
			click("xpath", "//span[text()='担保管理']")
			# 点击担保申请菜单
			js_gd("xpath", "//span[contains(text(),'担保申请')]")
			# 用JS的方法点击资金结算管理菜单按钮
			js_click("xpath", "//span[contains(text(),'担保申请')]")
			# 退出所有iframe窗体
			switch_default()
			
			for i in range(1, 4):
				# 切入担保管理的iframe窗体
				switch_to("xpath", "//iframe[@id='externalguaranteeapply-tab-iframe']")
				logging.info("开始担保申请功能")
				
				# 用JS的方法点击新增按钮
				js_click("xpath", "//span[text()='新增']")
				
				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='addWin-iframe']")
				sleep(1)
				
				# 输入本次申请额度
				click("xpath", "//input[@id='applyamount-input']")
				sleep(1)
				clear("xpath", "//input[@id='applyamount-input']")
				sleep(1)
				input("xpath", "//input[@id='applyamount-input']", "5000")
				sleep(1)
				
				# 描述框中填入值
				input("xpath", "//textarea[@id='description']", "自动化测试担保申请描述框")
				sleep(1)
				
				# 资金用途
				input("xpath", "//input[@id='usages']", "5000")
				sleep(1)
				
				# 融资利率
				click("xpath", "//input[@id='guaranteerate-input']")
				sleep(1)
				clear("xpath", "//input[@id='guaranteerate-input']")
				sleep(1)
				input("xpath", "//input[@id='guaranteerate-input']", "1")
				sleep(1)
				
				# 担保方式
				input("xpath", "//input[@id='guaranteemode']", "自动化测试担保方式")
				sleep(1)
				
				# 选择开始日期
				today = date.today()
				begindate = today
				click("xpath", "//input[@id='begindate-input']")
				sleep(1)
				clear("xpath", "//input[@id='begindate-input']")
				sleep(1)
				input("xpath", "//input[@id='begindate-input']", str(begindate))
				# 模拟回车键
				keyDown('enter')
				keyUp('enter')
				time.sleep(2)
				
				# 选择截止日期
				today = date.today()
				enddate = today + timedelta(days=720)
				click("xpath", "//input[@id='enddate-input']")
				sleep(1)
				input("xpath", "//input[@id='enddate-input']", str(enddate))
				# 模拟回车键
				keyDown('enter')
				keyUp('enter')
				time.sleep(2)
				
				# 点击保存按钮
				click("xpath", "//span[text()='保存']")
				
				# 退出所有iframe窗体
				switch_default()
				
				# 用隐式等待方法等页面出现新增成功的提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				print("担保申请，保存成功！")
				time.sleep(3)
				
				if i == 1:
					# 切入担保申请的iframe窗体
					switch_to("xpath", "//iframe[@id='externalguaranteeapply-tab-iframe']")
					sleep(1)
					
					# 点击查看
					# 用JS的方法点击放大镜
					js_click("xpath", "//span[@class='f-contrac-close']")
					sleep(1)
					
					# 输入担保组织
					click("xpath", "//input[@id='combobox-input-guaranteeorgid']")
					sleep(1)
					
					input("xpath", "//input[@id='combobox-input-guaranteeorgid']", "亚唐科技")
					sleep(1)
					click("xpath", "//div[contains(text(),'亚唐科技')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")
					sleep(1)
					
					# 点击查询
					click("xpath", "//span[text()='查询']")
					sleep(1)
					
					# 勾选
					click("xpath", "//div[contains(text(),'亚唐科技')]/parent::*/preceding-sibling::*[3]/descendant::*[2]")
					
					click("xpath", "//span[text()='删除']")
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现删除的提示框
					implici_wait("xpath", "//span[contains(text(),'成功删除1条记录！')]")
					print("担保申请，删除成功！")
					time.sleep(3)
				
				if i == 2:
					# 修改功能
					# 切入‘担保申请’的iframe窗体
					switch_to("xpath", "//iframe[@id='externalguaranteeapply-tab-iframe']")
					sleep(1)
					
					# 勾选
					click("xpath", "//div[contains(text(),'亚唐科技')]/parent::*/preceding-sibling::*[3]/descendant::*[2]")
					# 点击修改按钮
					click("xpath", "//span[text()='修改']")
					sleep(1)
					
					# 切入新增的iframe窗体
					switch_to("xpath", "//iframe[@id='modWin-iframe']")
					sleep(1)
					
					# 描述框中填入值
					input("xpath", "//textarea[@id='description']", "自动化测试担保申请描述框修改")
					sleep(1)
					
					# 点击保存按钮
					click("xpath", "//span[text()='保存']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现删除的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功')]")
					print("担保申请，修改成功！")
					time.sleep(3)
					
					# 切入组织担保额度的iframe窗体
					switch_to("xpath", "//iframe[@id='externalguaranteeapply-tab-iframe']")
					
					# 勾选
					click("xpath", "//div[contains(text(),'亚唐科技')]/parent::*/preceding-sibling::*[3]/descendant::*[2]")
					
					# 点击审核按钮
					click("xpath", "//span[text()='送审']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'成功送审1条记录！')]")
					print("担保申请，第一次送审成功！")
					logging.info("担保申请，第一次送审成功！")
					time.sleep(3)
					
					# 取消送审
					# 切入‘担保申请’的iframe窗体
					switch_to("xpath", "//iframe[@id='externalguaranteeapply-tab-iframe']")
					sleep(1)
					
					# 勾选
					click("xpath", "//div[contains(text(),'亚唐科技')]/parent::*/preceding-sibling::*[3]/descendant::*[2]")
					
					# 用JS方便点击‘审核’按钮旁边的倒三角形
					js_click("xpath", "//span[text()='送审']/parent::*/following-sibling::*/child::*")
					sleep(1)
					
					# 点击取消送审按钮
					js_click("xpath", "//a[contains(text(),'撤销送审')]")
					sleep(1)
					
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'成功撤销送审1条记录！')]")
					print("担保申请，撤销送审成功！")
					logging.info("担保申请，撤销送审成功！")
					time.sleep(3)
					
					# 失效功能
					# 切入组织担保额度的iframe窗体
					switch_to("xpath", "//iframe[@id='externalguaranteeapply-tab-iframe']")
					
					click("xpath", "//div[contains(text(),'亚唐科技')]/parent::*/preceding-sibling::*[3]/descendant::*[2]")
					# 点击审核按钮
					click("xpath", "//span[text()='送审']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'成功送审1条记录！')]")
					print("担保申请，第一次送审成功！")
					logging.info("担保申请，第一次送审成功！")
					time.sleep(3)
					
					# 生效功能
					# 切入组织担保额度的iframe窗体
					switch_to("xpath", "//iframe[@id='externalguaranteeapply-tab-iframe']")
					
					# 勾选
					double_click("xpath",
					             "//div[contains(text(),'亚唐科技')]/parent::*/preceding-sibling::*[3]/descendant::*[2]")
					sleep(1)
					
					switch_to("xpath", "//iframe[@id='wf_taskProcessing_win-iframe']")
					
					# 点击生按钮
					click("xpath", "//span[text()='同意']")
					sleep(1)
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现删除的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("申请额度，第一次审核同意成功！")
					time.sleep(3)
					
					# 生效功能
					# 切入组织担保额度的iframe窗体
					switch_to("xpath", "//iframe[@id='externalguaranteeapply-tab-iframe']")
					
					# 勾选
					double_click("xpath",
					             "//div[contains(text(),'亚唐科技')]/parent::*/preceding-sibling::*[3]/descendant::*[2]")
					sleep(1)
					
					switch_to("xpath", "//iframe[@id='wf_taskProcessing_win-iframe']")
					
					# 点击生按钮
					click("xpath", "//span[text()='同意']")
					sleep(1)
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现删除的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("申请额度，第二次审核同意成功！")
					time.sleep(3)
					
					switch_to("xpath", "//iframe[@id='externalguaranteeapply-tab-iframe']")
					
					# 勾选
					click("xpath", "//div[contains(text(),'亚唐科技')]/parent::*/preceding-sibling::*[3]/descendant::*[2]")
					sleep(1)
					
					# 点击生按钮
					click("xpath", "//span[text()='作废']")
					sleep(1)
					
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现删除的提示框
					implici_wait("xpath", "//span[contains(text(),'成功作废1条!')]")
					print("担保申请，成功作废1条!！")
					time.sleep(3)
				if i == 3:
					# 切入组织担保额度的iframe窗体
					switch_to("xpath", "//iframe[@id='externalguaranteeapply-tab-iframe']")
					
					click("xpath", "//div[contains(text(),'亚唐科技')]/parent::*/preceding-sibling::*[3]/descendant::*[2]")
					# 点击审核按钮
					click("xpath", "//span[text()='送审']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'成功送审1条记录！')]")
					print("担保申请，第一次送审成功！")
					logging.info("担保申请，第一次送审成功！")
					time.sleep(3)
					
					# 生效功能
					# 切入组织担保额度的iframe窗体
					switch_to("xpath", "//iframe[@id='externalguaranteeapply-tab-iframe']")
					
					# 勾选
					double_click("xpath",
					             "//div[contains(text(),'亚唐科技')]/parent::*/preceding-sibling::*[3]/descendant::*[2]")
					sleep(1)
					
					switch_to("xpath", "//iframe[@id='wf_taskProcessing_win-iframe']")
					
					# 点击生按钮
					click("xpath", "//span[text()='同意']")
					sleep(1)
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现删除的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("申请额度，第一次审核同意成功！")
					time.sleep(3)
					
					# 生效功能
					# 切入组织担保额度的iframe窗体
					switch_to("xpath", "//iframe[@id='externalguaranteeapply-tab-iframe']")
					
					# 勾选
					double_click("xpath",
					             "//div[contains(text(),'亚唐科技')]/parent::*/preceding-sibling::*[3]/descendant::*[2]")
					sleep(1)
					
					switch_to("xpath", "//iframe[@id='wf_taskProcessing_win-iframe']")
					
					# 点击生按钮
					click("xpath", "//span[text()='同意']")
					sleep(1)
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现删除的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("担保申请，第二次审核同意成功！")
					time.sleep(3)
					
					# 打印
					switch_to("xpath", "//iframe[@id='externalguaranteeapply-tab-iframe']")
					sleep(1)
					
					# 勾选
					click("xpath", "//div[contains(text(),'亚唐科技')]/parent::*/preceding-sibling::*[3]/descendant::*[2]")
					# 点击修改按钮
					click("xpath", "//span[text()='打印']")
					time.sleep(3)
					
					# 获取所有窗口句柄
					all_handles = self.driver.window_handles
					# 循环遍历所有新打开的窗口句柄，也就是说不包括主窗口
					now_handle = self.driver.current_window_handle
					for handle in all_handles:
						self.driver.switch_to.window(handle)
						if self.driver.title == u"sctt_externalguaranteeapplyprint":
							implici_wait("xpath", "//td[contains(text(),'Mindy科技有限公司')]")
							print("担保申请，打印成功!！")
							time.sleep(3)
							self.driver.switch_to.window(now_handle)
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("担保申请操作失败！" + str(traceback.format_exc()))
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
