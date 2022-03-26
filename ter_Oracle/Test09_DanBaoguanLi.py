# encoding=utf-8
# @Time : 2020/8/14 14:49
# @Author : Mindy
# 此文件是测试内部借款管理--担保管理模块，包含组织担保额度和担保方台账登记
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
class Test_Dbgl(unittest.TestCase):
	
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
		
		logging.info("开始测试内部借款管理的页面功能")
		# 将页面的滚动条滑动到‘资金结算管理’页面的地方
		js_gd("xpath", "//span[contains(text(),'内部借款管理')]")
		# 用JS的方法点击资金结算管理菜单按钮
		js_click("xpath", "//span[contains(text(),'内部借款管理')]")
		
		# 测试担保管理--组织担保额度
		try:
			# 点击担保管理菜单
			click("xpath", "//span[text()='担保管理']")
			# 点击组织担保额度菜单
			click("xpath", "//span[text()='组织担保额度']")
			# 退出所有iframe窗体
			switch_default()

			for i in range(1, 3):
				# 切入担保管理的iframe窗体
				switch_to("xpath", "//iframe[@id='externalguaranteeamount-tab-iframe']")
				logging.info("开始担保申请功能")

				# 用JS的方法点击新增按钮
				js_click("xpath", "//span[text()='新增']")

				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='addWin-iframe']")
				sleep(1)

				# 被担保单位
				click("xpath", "//input[@id='combobox-input-guaranteedorgid']")
				sleep(1)
				input("xpath", "//input[@id='combobox-input-guaranteedorgid']", "Mindy科技有限公司")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-guaranteedorgid']")
				input_enter("xpath", "//input[@id='combobox-input-guaranteedorgid']")
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
				clear("xpath", "//input[@id='enddate-input']")
				sleep(1)
				input("xpath", "//input[@id='enddate-input']", str(enddate))
				# 模拟回车键
				keyDown('enter')
				keyUp('enter')
				time.sleep(2)

				# 选择币种
				click("xpath", "//input[@id='combobox-input-currencyid']")
				sleep(1)
				input("xpath", "//input[@id='combobox-input-currencyid']", "CNY")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-currencyid']")
				input_enter("xpath", "//input[@id='combobox-input-currencyid']")
				sleep(1)

				# 输入担保额度
				clear("xpath", "//input[@id='guaranteeamount-input']")
				sleep(1)
				input("xpath", "//input[@id='guaranteeamount-input']", "10000")
				sleep(1)

				# 选择控制方式
				click("xpath", "//input[@id='combobox-input-controlmode']")
				sleep(1)
				input("xpath", "//input[@id='combobox-input-controlmode']", "不控制")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-controlmode']")
				input_enter("xpath", "//input[@id='combobox-input-controlmode']")
				sleep(1)

				# 描述框中填入值
				input("xpath", "//textarea[@id='description']", "自动化测试组织担保额度描述框")
				sleep(1)

				# 点击保存按钮
				click("xpath", "//span[text()='保存']")

				# 退出所有iframe窗体
				switch_default()

				# 用隐式等待方法等页面出现新增成功的提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				print("组织担保额度，保存成功！")
				time.sleep(3)

				if i == 1:

					# 切入组织担保额度的iframe窗体
					switch_to("xpath", "//iframe[@id='externalguaranteeamount-tab-iframe']")
					sleep(1)

					# 点击查看
					# 用JS的方法点击放大镜
					js_click("xpath", "//span[@class='f-contrac-close']")
					sleep(1)

					# 输入被担保单位
					click("xpath", "//input[@id='combobox-input-guaranteedorgid']")
					sleep(1)
					input("xpath", "//input[@id='combobox-input-guaranteedorgid']", "Mindy科技有限公司")
					sleep(1)
					click("xpath", "//div[contains(text(),'Mindy科技有限公司')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")
					sleep(1)

					# 点击查询
					click("xpath", "//span[text()='查询']")
					sleep(1)

					# 勾选
					click("xpath", "//div[contains(text(),'Mindy科技有限公司')]/parent::*/preceding-sibling::*[2]/descendant::*[2]")
					# 点击保存按钮

					click("xpath", "//span[text()='删除']")
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现删除的提示框
					implici_wait("xpath", "//span[contains(text(),'成功删除1条记录！')]")
					print("组织担保额度，删除成功！")
					time.sleep(3)

			# 修改功能
			# 切入组织担保额度的iframe窗体
			switch_to("xpath", "//iframe[@id='externalguaranteeamount-tab-iframe']")

			# 勾选
			click("xpath", "//div[contains(text(),'Mindy科技有限公司')]/parent::*/preceding-sibling::*[2]/descendant::*[2]")

			# 点击修改按钮
			click("xpath", "//span[text()='修改']")
			sleep(1)

			# 切入新增的iframe窗体
			switch_to("xpath", "//iframe[@id='modWin-iframe']")
			sleep(1)

			# 描述框中填入值
			input("xpath", "//textarea[@id='description']", "自动化测试组织担保额度描述框修改")
			sleep(1)

			# 点击保存按钮
			click("xpath", "//span[text()='保存']")

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功')]")
			print("组织担保额度，修改成功！")
			time.sleep(3)

			# 失效功能
			# 切入组织担保额度的iframe窗体
			switch_to("xpath", "//iframe[@id='externalguaranteeamount-tab-iframe']")

			# 勾选
			click("xpath", "//div[contains(text(),'Mindy科技有限公司')]/parent::*/preceding-sibling::*[2]/descendant::*[2]")

			# 点击修改按钮
			click("xpath", "//span[text()='失效']")
			sleep(1)

			# 点击弹出框的OK键
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'成功失效1条记录！')]")
			print("组织担保额度，失效成功！")
			time.sleep(3)

			# 生效功能
			# 切入组织担保额度的iframe窗体
			switch_to("xpath", "//iframe[@id='externalguaranteeamount-tab-iframe']")

			# 勾选
			click("xpath", "//div[contains(text(),'Mindy科技有限公司')]/parent::*/preceding-sibling::*[2]/descendant::*[2]")

			# 点击生按钮
			click("xpath", "//span[text()='生效']")
			sleep(1)

			# 点击弹出框的OK键
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'成功生效1条记录！')]")
			print("组织担保额度，生效成功！")
			time.sleep(3)

			switch_default()

			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='组织担保额度']/child::*[1]")

			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//span[text()='担保管理']")

			# 打印操作成功日志
			print("组织担保额度，操作成功!")
			logging.info("组织担保额度，操作成功!")
			time.sleep(2)
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("组织担保额度操作失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		
		# 测试担保管理--担保方台账登记
		try:
			
			# 点击担保管理菜单
			click("xpath", "//span[text()='担保管理']")
			# 点击担保申请菜单
			js_gd("xpath", "//span[contains(text(),'担保方台账登记')]")
			# 用JS的方法点击资金结算管理菜单按钮
			js_click("xpath", "//span[contains(text(),'担保方台账登记')]")
			# 退出所有iframe窗体
			switch_default()
			
			for i in range(1, 3):
				# 切入担保管理的iframe窗体
				switch_to("xpath", "//iframe[@id='externalguarantee-tab-iframe']")
				logging.info("开始担保方台账登记功能")
				
				# 用JS的方法点击新增按钮
				js_click("xpath", "//span[text()='新增']")
				
				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='addWin-iframe']")
				sleep(1)
				
				# 输入合同号
				temp = time.strftime("%Y%m%d%H%M%S")
				input("xpath", "//input[@id='contractcode']", "TestConNo" + str(temp))
				sleep(1)
				
				# 担保额度单据号
				click("xpath", "//input[@id='combobox-input-guaranteeamountid']")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-guaranteeamountid']")
				input_enter("xpath", "//input[@id='combobox-input-guaranteeamountid']")
				sleep(1)
				
				# 选择开始日期
				today = date.today()
				begindate = today - timedelta(days=20)
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
				enddate = today + timedelta(days=40)
				click("xpath", "//input[@id='enddate-input']")
				sleep(1)
				clear("xpath", "//input[@id='enddate-input']")
				sleep(1)
				input("xpath", "//input[@id='enddate-input']", str(enddate))
				# 模拟回车键
				keyDown('enter')
				keyUp('enter')
				time.sleep(2)
				
				# 金额
				clear("xpath", "//input[@id='amount-input']")
				sleep(1)
				input("xpath", "//input[@id='amount-input']", "2000")
				sleep(1)
				
				# 金融机构类型选择
				click("xpath", "//input[@id='combobox-input-financialinstitutiontype']")
				sleep(1)
				input("xpath", "//input[@id='combobox-input-financialinstitutiontype']", "银行")
				input_down("xpath", "//input[@id='combobox-input-financialinstitutiontype']")
				sleep(1)
				input_enter("xpath", "//input[@id='combobox-input-financialinstitutiontype']")
				sleep(1)
				
				# 金融机构
				click("xpath", "//input[@id='combobox-input-bankid']")
				sleep(1)
				input("xpath", "//input[@id='combobox-input-bankid']", "中国银行")
				input_down("xpath", "//input[@id='combobox-input-bankid']")
				input_enter("xpath", "//input[@id='combobox-input-bankid']")
				sleep(1)
				
				# 描述框中填入值
				input("xpath", "//textarea[@id='description']", "自动化测试担保申请描述框")
				sleep(1)
				
				# 点击保存按钮
				click("xpath", "//span[text()='保存']")
				
				# 退出所有iframe窗体
				switch_default()
				
				# 用隐式等待方法等页面出现新增成功的提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				print("担保方台账登记，保存成功！")
				time.sleep(3)
				
				if i == 1:
					# 切入担保方台账登记的iframe窗体
					switch_to("xpath", "//iframe[@id='externalguarantee-tab-iframe']")
					sleep(1)
					
					# 点击查看
					# 用JS的方法点击放大镜
					js_click("xpath", "//span[@class='f-contrac-close']")
					sleep(1)
					
					# 输入合同号
					input("xpath", "//input[@id='contractcode']", "TestConNo")
					sleep(1)
					
					# 点击查询
					click("xpath", "//span[text()='查询']")
					sleep(1)
					
					# 勾选
					click("xpath",
					      "//div[contains(text(),'Mindy科技有限公司')]/parent::*/preceding-sibling::*[5]/descendant::*[2]")
					
					click("xpath", "//span[text()='删除']")
					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
					
					# 退出所有iframe窗体
					switch_default()
					
					# 用隐式等待方法等页面出现删除的提示框
					implici_wait("xpath", "//span[contains(text(),'成功删除1条记录！')]")
					print("担保方台账登记，删除成功！")
					time.sleep(3)
			
			# 修改功能
			# 切入‘担保方台账登记’的iframe窗体
			switch_to("xpath", "//iframe[@id='externalguarantee-tab-iframe']")
			sleep(1)
			
			# 勾选
			click("xpath", "//div[contains(text(),'Mindy科技有限公司')]/parent::*/preceding-sibling::*[5]/descendant::*[2]")
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
			switch_to("xpath", "//iframe[@id='externalguarantee-tab-iframe']")
			
			click("xpath", "//div[contains(text(),'Mindy科技有限公司')]/parent::*/preceding-sibling::*[5]/descendant::*[2]")
			# 点击审核按钮
			click("xpath", "//span[text()='审核']")
			# 点击弹出框的OK键
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
			
			# 退出所有iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'成功审核1条记录')]")
			print("担保方台账登记，第一次送审成功！")
			logging.info("担保方台账登记，第一次送审成功！")
			time.sleep(3)
			
			# 取消送审
			# 切入‘担保方台账登记’的iframe窗体
			switch_to("xpath", "//iframe[@id='externalguarantee-tab-iframe']")
			sleep(1)
			
			click("xpath", "//div[contains(text(),'Mindy科技有限公司')]/parent::*/preceding-sibling::*[5]/descendant::*[2]")
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
			implici_wait("xpath", "//span[contains(text(),'成功取消审核1条！')]")
			print("担保方台账登记，取消审核成功！")
			logging.info("担保方台账登记，取消审核成功！")
			time.sleep(3)
			
			# 失效功能
			# 切入组织担保额度的iframe窗体
			switch_to("xpath", "//iframe[@id='externalguarantee-tab-iframe']")
			
			click("xpath", "//div[contains(text(),'Mindy科技有限公司')]/parent::*/preceding-sibling::*[5]/descendant::*[2]")
			# 点击审核按钮
			click("xpath", "//span[text()='审核']")
			# 点击弹出框的OK键
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
			
			# 退出所有iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现审核的提示框
			implici_wait("xpath", "//span[contains(text(),'成功审核1条记录')]")
			print("担保方台账登记，第二次审核成功！")
			logging.info("担保方台账登记，第二次审核成功！")
			time.sleep(3)
			
			switch_to("xpath", "//iframe[@id='externalguarantee-tab-iframe']")
			
			# 勾选
			click("xpath", "//div[contains(text(),'Mindy科技有限公司')]/parent::*/preceding-sibling::*[5]/descendant::*[2]")
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
			print("担保方台账登记，成功作废1条!！")
			time.sleep(3)
			
			switch_default()
			
			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='担保方台账登记']/child::*[1]")
			
			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//span[text()='担保管理']")
			
			# 打印操作成功日志
			print("担保方台账登记，操作成功!")
			logging.info("担保方台账登记，操作成功!")
			time.sleep(2)
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("担保方台账登记操作失败！" + str(traceback.format_exc()))
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
