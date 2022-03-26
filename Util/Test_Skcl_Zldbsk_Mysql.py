# encoding=utf-8
# @Time : 2020/8/14 14:49
# @Author : Mindy
# 此文件是测试MySQL版本资金结算管理--资金系统收付--收款处理--直联单笔收款
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

class Test_Skcl_Zldbsk_Mysql(unittest.TestCase):
	
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
		# login(G_Mys_Url, mindy, Password, "默认租户")
		# login(G_Mys_Url, mindy, Password, "亚唐科技")
		# login(G_Mys_Url, judy, Password, "默认租户")
		
		logging.info("开始测试资金结算管理的页面功能")
		# 将页面的滚动条滑动到‘资金结算管理’页面的地方
		js_gd("xpath", "//span[contains(text(),'资金结算管理')]")
		# 用JS的方法点击资金结算管理菜单按钮
		js_click("xpath", "//span[contains(text(),'资金结算管理')]")
		
		# 测试直联单笔收款-导入功能
		# 测试收款处理--直联单笔收款
		try:
			# 点击'资金系统收付'菜单
			click("xpath", "//span[text()='资金系统收付']")
			# 点击收款处理菜单
			click("xpath", "//span[text()='收款处理']")
			# 退出所有iframe窗体
			switch_default()

			for i in range(1, 2):
				# 切入直联单笔收款的iframe窗体
				switch_to("xpath", "//iframe[@id='generalRecment-tab-iframe']")
				logging.info("开始测试直联单笔收款直联单笔收款功能")
				sleep(1)
				
				# 点击直联单笔收款
				click("xpath", "//span[text()='直联单笔收款']")
				sleep(1)

				# 进入直联单笔收款的iframe 窗体
				switch_to("xpath", "//iframe[@id='subTabFive-iframe']")

				# 用JS的方法点击列表导入
				js_click("xpath", "//div[@title='列表导入']")

				# 进入导入详情页面窗体
				switch_to("xpath", "//iframe[@id='importDataWin-iframe']")
				sleep(1)
				
				# 选择导入类型
				click("xpath", "//input[@id='combobox-input-businessid']")
				sleep(1)
				input("xpath", "//input[@id='combobox-input-businessid']", "直联单笔收款单导入")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-businessid']")
				sleep(1)
				input_enter("xpath", "//input[@id='combobox-input-businessid']")
				sleep(1)
				
				# 点击下一步
				click("xpath", "//span[text()='下一步']")
				sleep(1)

				# 进入上传详情页窗体
				switch_to("xpath", "//iframe[@id='loadNextWin-iframe']")
				sleep(1)
				
				# 选择交易类型
				click("xpath", "//input[@id='combobox-input-paytypeid']")
				sleep(1)
				input("xpath", "//input[@id='combobox-input-paytypeid']", "外部收款")
				sleep(1)
				input_enter("xpath", "//input[@id='combobox-input-paytypeid']")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-paytypeid']")
				sleep(1)
				input_enter("xpath", "//input[@id='combobox-input-paytypeid']")
				sleep(1)
				
				# 选择结算方式
				click("xpath", "//input[@id='combobox-input-settlementmodeid']")
				sleep(1)
				input("xpath", "//input[@id='combobox-input-settlementmodeid']", "单笔实时收款")
				sleep(1)
				input_enter("xpath", "//input[@id='combobox-input-settlementmodeid']")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-settlementmodeid']")
				sleep(1)
				input_enter("xpath", "//input[@id='combobox-input-settlementmodeid']")
				sleep(1)
				
				# 选择附件上传
				upload_click("xpath", "//div[text()='选择文件']/parent::*[1]/descendant::*[4]", 'D:\Download\Collection_Handle', '"directsinglerec.xls"')
				sleep(2)

				# 点击保存按钮
				click("xpath", "//span[text()='上传']")

				# 退出所有iframe窗体
				switch_default()

				# 用隐式等待方法等页面出现新增成功的提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功,共导入3条数据，成功3条，失败0条，未处理0条。')]")
				print("直联单笔收款导入，保存成功！")
				time.sleep(3)
				
				# 切入直联单笔收款的iframe窗体
				switch_to("xpath", "//iframe[@id='generalRecment-tab-iframe']")
				sleep(1)
				
				# 点击直联单笔收款
				click("xpath", "//span[text()='直联单笔收款']")
				sleep(1)
				
				# 进入直联单笔收款的iframe 窗体
				switch_to("xpath", "//iframe[@id='subTabFive-iframe']")
				
				# 点击关闭页面
				click("xpath", "//span[text()='导入窗口']/preceding-sibling::*[2]")
				sleep(1)
				
				switch_default()
				
				if i == 1:
					# 切入直联单笔收款的iframe窗体
					switch_to("xpath", "//iframe[@id='generalRecment-tab-iframe']")
					sleep(1)
					
					# 点击直联单笔收款
					click("xpath", "//span[text()='直联单笔收款']")
					sleep(1)
					
					# 进入直联单笔收款的iframe 窗体
					switch_to("xpath", "//iframe[@id='subTabFive-iframe']")
					
					# 点击查看
					# 用JS的方法点击放大镜
					js_click("xpath", "//span[@class='f-contrac-close']")
					sleep(1)
					
					# 选择创建日期从
					today = date.today()
					due_date = today - timedelta(days=60)
					click("xpath", "//input[@id='createdonstart-input']")
					sleep(1)
					clear("xpath", "//input[@id='createdonstart-input']")
					sleep(1)
					input("xpath", "//input[@id='createdonstart-input']", str(due_date))
					time.sleep(1)
					
					# 选择应收日期从
					today = date.today()
					pay_date = today - timedelta(days=60)
					click("xpath", "//input[@id='paydatestart-input']")
					sleep(1)
					clear("xpath", "//input[@id='paydatestart-input']")
					sleep(1)
					input("xpath", "//input[@id='paydatestart-input']", str(pay_date))
					time.sleep(1)
					
					# 点击查询
					click("xpath", "//span[text()='查询']")
					
					# 修改勾选数据
					click("xpath", "//span[text()='Mindy科技有限公司']/ancestor::*[7]/preceding-sibling::*[1]/descendant::*[19]")
					sleep(1)
					
					# 点击审核按钮
					click("xpath", "//span[text()='审核']")
					
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现审核的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！审核成功1笔，失败0笔。')]")
					print("收款处理-现金收款，审核成功！")
					logging.info("收款处理-现金收款，审核成功！")
					time.sleep(3)
					
					# 切入直联单笔收款的iframe窗体
					switch_to("xpath", "//iframe[@id='generalRecment-tab-iframe']")
					sleep(1)
					
					# 点击直联单笔收款
					click("xpath", "//span[text()='直联单笔收款']")
					sleep(1)
					
					# 进入直联单笔收款的iframe 窗体
					switch_to("xpath", "//iframe[@id='subTabFive-iframe']")
					
					# 修改勾选数据
					click("xpath", "//span[text()='Mindy科技有限公司']/ancestor::*[7]/preceding-sibling::*[1]/descendant::*[19]")
					sleep(1)
					
					
					
					
		
		
		
		
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("直联单笔收款导入操作失败！" + str(traceback.format_exc()))
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

