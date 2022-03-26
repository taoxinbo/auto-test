
# encoding=utf-8
# @Time : 2020/10/26 13:30
# @Author : zzg
# 此文件是测试Oracle版本资金结算管理--资金系统收付--收款处理--承兑汇票收票
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
import random
# print("开始时间：",time.strftime("%Y-%m-%d %H:%M:%S"))

driver = ""


@pytest.mark.flaky(reruns=pytest_flaky, reruns_delay=10)
class Test24_ShouKuanChuLi_CDHPSP(unittest.TestCase):
	
	# 启动浏览器
	def setUp(self):
		
		# 启动浏览器的另外一个方法：通过封装启动浏览器的驱动，启动不同浏览器
		self.driver = get("chrome")
	
	# 登陆系统、对系统设置进行操作
	def test_trade(self):
		
		# 通过登陆封装函数，进行登陆
		# login( G_Ora_Url,Tao, Password,"亚唐科技")
		login(G_Ora_Url, mindy, Password, "亚唐科技")
		
		####点票确认收票、电票合并收票，需要电票工具，故不实现自动化
		
		logging.info("开始测试资金结算管理-资金系统收付-收款处理-承兑汇票收票")
		# 将页面的滚动条滑动到‘资金结算管理’页面的地方
		js_gd("xpath", "//span[contains(text(),'资金结算管理')]")
		# 用JS的方法点击资金结算管理菜单按钮
		js_click("xpath", "//span[contains(text(),'资金结算管理')]")
		sleep(1)
		# 点击'资金系统收付'菜单
		click("xpath", "//span[text()='资金系统收付']")
		sleep(1)
		# 点击收款处理菜单
		click("xpath", "//span[text()='收款处理']")
		sleep(1)
		# 退出所有iframe窗体
		switch_default()
		
		try:
			
			#去票据管理-承兑汇票管理-应收票据管理，做数据==========================
			##点击资金系统收付收回窗体
			click("xpath", "//span[text()='资金系统收付']")
			sleep(1)
			js_click("xpath", "//span[contains(text(),'资金结算管理')]")
			sleep(1)
			
			#滚动到票据管理
			js_gd("xpath", "//span[contains(text(),'票据管理')]")
			# 用JS的方法点击票据管理菜单按钮
			js_click("xpath", "//span[contains(text(),'票据管理')]")
			sleep(1)
			# 点击承兑票据管理菜单
			js_click("xpath", "//span[@title='承兑汇票管理']")
			# 点击应收票据管理
			js_click("xpath", "//span[@title='应收票据管理']")
			# 退出所有的iframe窗体
			switch_default()
			
			for i in range (1,4):
				# 切入应收票据管理窗体
				switch_to("xpath", "//iframe[@id='recDraftManage-tab-iframe']")
				# 用JS的方法点击新增按钮
				js_click("xpath", "//span[text()='新增']")
				sleep(1)
				switch_to("xpath", '//*[@id="addWin-iframe"]')
				
				# 票据类型
				input("xpath", '//*[@id="combobox-input-drafttype"]', '109-银行承兑汇票')
				sleep(1)
				click("xpath", '//*[@id="drafttype-combogrid-body-table"]/tbody/tr/td[2]/div')
				sleep(1)
				
				# 票据号
				PJH = time.strftime("%Y%m%d%H%M%S")
				input("xpath",'//*[@id="draftcode"]',PJH)
				sleep(2)
				
				#到期期限
				clear("xpath",'//*[@id="terms-input"]')
				sleep(1)
				input("xpath",'//*[@id="terms-input"]',"60")
				sleep(1)
				
				#票面金额
				clear("xpath", '//*[@id="draftamount-input"]')
				sleep(1)
				input("xpath", '//*[@id="draftamount-input"]', "100")
				sleep(1)
				
				#外部给票单位
				input("xpath",'//*[@id="combobox-input-endorsecounterpartyid"]','浙江华语科技')
				sleep(2)
				#双击清楚下拉框
				double_click("xpath",'//*[@id="recaccountinfo"]')
				sleep(1)
				
				#承兑银行
				input("xpath",'//*[@id="combobox-input-paybankid"]',"BOC-中国银行")
				sleep(2)
				click("xpath",'//*[@id="paybankid-combogrid-body-table"]/tbody/tr[1]/td[2]/div')
				sleep(1)
				
				#保存
				span_click("保存")
				switch_default()
				sleep(3)
				
				#回到上层窗口
				switch_default()
				switch_to("xpath", "//iframe[@id='recDraftManage-tab-iframe']")
				
				#点击刷新勾选数据
				js_click("xpath",'//*[@id="gridbar-page-refresh"]')
				sleep(1)
				js_click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
				sleep(1)
				
				#审核
				span_click("审核")
				sleep(1)
				#点击ok
				click("xpath",'//*[@id="f-message-webgen-0-okBnt"]')
				sleep(1)
				switch_default()
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				sleep(3)
			
			#收缩按钮
			js_click("xpath", "//span[@title='承兑汇票管理']")
			sleep(1)
			js_click("xpath", "//span[contains(text(),'票据管理')]")
			sleep(1)
			
			#回到承兑汇票支付页面
			
			js_gd("xpath", "//span[contains(text(),'资金结算管理')]")
			# 用JS的方法点击资金结算管理菜单按钮
			js_click("xpath", "//span[contains(text(),'资金结算管理')]")
			sleep(1)
			# 点击'资金系统收付'菜单
			click("xpath", "//span[text()='资金系统收付']")
			sleep(1)
			# 点击收款处理菜单
			click("xpath", "//span[text()='收款处理']")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			
			
			#测试纸质确认收票----------------------------------------------------------------------------
			#切入窗体
			switch_to("xpath",'//*[@id="generalRecment-tab-iframe"]')
			#点击承兑汇票支付
			span_click("承兑汇票收票")
			sleep(1)
			#切入承兑汇票支付窗体
			switch_to("xpath",'//*[@id="subTabSix-iframe"]')
			
			#点击确认收票旁边的三角
			click("xpath","//span[text()='确认收票']/parent::*/following-sibling::*/child::*")
			sleep(1)
			js_click("xpath", "//a[contains(text(),'纸票确认收票')]")
			sleep(1)
			
			#切入窗体
			switch_to("xpath",'//*[@id="recWin-iframe"]')
			#查询数据
			span_click("票据号")
			sleep(1)
			span_click("票据号")
			sleep(1)
			#勾选数据
			click("xpath",'//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			#点击下一步
			span_click("下一步")
			sleep(1)
			
			switch_to("xpath",'//*[@id="recmentsWin-iframe"]')
			use = random.randint(1000,10000)
			sleep(1)
			input("xpath",'//*[@id="combobox-input-purpose"]',use)
			sleep(3)
			span_click("保存")
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("收款处理-承兑汇票收票，纸质确认收票成功！")
			span_click("收款处理")
			sleep(3)
			
			
			# 测试关联票据查看----------------------------------------------------------------------------
			# 切入窗体
			switch_to("xpath", '//*[@id="generalRecment-tab-iframe"]')
			# 点击承兑汇票支付
			span_click("承兑汇票收票")
			sleep(1)
			
			# 切入承兑汇票支付窗体
			switch_to("xpath", '//*[@id="subTabSix-iframe"]')
			
			#点击刷新按钮,勾选数据
			click("xpath",'//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath",'//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("关联票据查看")
			sleep(1)
			switch_to("xpath",'//*[@id="draftViewWin-iframe"]')
			implici_wait("xpath",'//*[@id="griduniqueId-body-table"]/tbody/tr/td[3]/div')
			sleep(1)
			print("收款处理-承兑汇票收票，关联票据查看成功！")
			switch_parent()
			click("xpath",'//*[@id="f-win-title-draftViewWin"]/div[1]/div')
			sleep(1)
			switch_default()
			sleep(3)
			
			
			# 测试打印----------------------------------------------------------------------------
			sql = "update T_SE_RECMENTS set FINACCOUNTSTATE ='2' where purpose = '" + str(use) + "'"
			ora_sql(ora_ip, ora_sid, ora_user, ora_pwd,
			       sql)
			# 切入窗体
			switch_to("xpath", '//*[@id="generalRecment-tab-iframe"]')
			# 点击承兑汇票支付
			span_click("承兑汇票收票")
			sleep(1)
			# 切入承兑汇票支付窗体
			switch_to("xpath", '//*[@id="subTabSix-iframe"]')
			
			# 点击刷新按钮,勾选数据
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
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
					implici_wait("xpath", "//td[contains(text(),'外部收款')]")
					print("收款出路-承兑汇票收票，打印成功!！")
					time.sleep(3)
					self.driver.switch_to.window(now_handle)
					switch_default()
			
			#测试收据打印
			# 切入窗体
			switch_to("xpath", '//*[@id="generalRecment-tab-iframe"]')
			# 点击承兑汇票支付
			span_click("承兑汇票收票")
			sleep(1)
			# 切入承兑汇票支付窗体
			switch_to("xpath", '//*[@id="subTabSix-iframe"]')
			
			# 点击刷新按钮,勾选数据
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			# 用JS方便点击‘打印’按钮旁边的倒三角形
			js_click("xpath", "//span[text()='打印']/parent::*/following-sibling::*/child::*")
			sleep(1)
			
			# 点击收据打印按钮
			js_click("xpath", "//a[contains(text(),'收据打印')]")
			sleep(1)
			switch_to("xpath", '//*[@id="printWin-iframe"]')
			implici_wait("xpath", "//td[contains(text(),'浙江华语科技')]")
			sleep(3)
			print("收款处理-承兑汇票收票，收据打印成功!！")
			switch_parent()
			click("xpath", '//*[@id="f-win-title-printWin"]/div[1]/div')
			sleep(1)
			switch_default()
			
			# 打印记录
			# 切入窗体
			switch_to("xpath", '//*[@id="generalRecment-tab-iframe"]')
			# 点击承兑汇票支付
			span_click("承兑汇票收票")
			sleep(1)
			# 切入承兑汇票支付窗体
			switch_to("xpath", '//*[@id="subTabSix-iframe"]')
			
			# 点击刷新按钮,勾选数据
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			# 用JS方便点击‘收款’按钮旁边的倒三角形
			js_click("xpath", "//span[text()='打印']/parent::*/following-sibling::*/child::*")
			sleep(1)
			
			# 点击打印记录按钮
			js_click("xpath", "//a[contains(text(),'打印记录')]")
			sleep(1)
			
			switch_to("xpath", "//iframe[@id='printWin-iframe']")
			sleep(1)
			
			# 用隐式等待方法等页面出现  操作人:mindy
			implici_wait("xpath", "//div[@title='操作人:mindy']")
			print("收款处理-承兑汇票收票，打印记录查看成功！")
			time.sleep(3)
			switch_parent()
			# 点击关闭页面
			click("xpath", "//span[text()='打印']/preceding-sibling::*[1]")
			sleep(1)
			switch_default()
			
			# 测试作废----------------------------------------------------------------------------
			
			sql2 = "update T_SE_RECMENTS set FINACCOUNTSTATE ='1' where purpose = '" + str(use) + "'"
			ora_sql(ora_ip, ora_sid, ora_user, ora_pwd,
			       sql2)
			
			# 切入窗体
			switch_to("xpath", '//*[@id="generalRecment-tab-iframe"]')
			# 点击承兑汇票支付
			span_click("承兑汇票收票")
			sleep(1)
			# 切入承兑汇票支付窗体
			switch_to("xpath", '//*[@id="subTabSix-iframe"]')
			
			# 点击刷新按钮,勾选数据
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("作废")
			sleep(1)
			click("xpath",'//*[@id="f-message-webgen-0-okBnt"]')
			sleep(1)
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("收款处理-承兑汇票收票，作废成功！")
			
			# 测试纸票合并收票----------------------------------------------------------------------------
			# 切入窗体
			switch_to("xpath", '//*[@id="generalRecment-tab-iframe"]')
			# 点击承兑汇票支付
			span_click("承兑汇票收票")
			sleep(1)
			# 切入承兑汇票支付窗体
			switch_to("xpath", '//*[@id="subTabSix-iframe"]')
			
			# 点击确认收票旁边的三角
			click("xpath", "//span[text()='确认收票']/parent::*/following-sibling::*/child::*")
			sleep(1)
			
			js_click("xpath", "//a[contains(text(),'纸票合并收票')]")
			sleep(1)
			
			# 切入窗体
			switch_to("xpath", '//*[@id="recWin-iframe"]')
			#排序
			span_click("票据号")
			sleep(1)
			span_click("票据号")
			sleep(1)
			# 勾选数据
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[2]/td[2]/div/button')
			sleep(1)
			# 点击下一步
			click("xpath",'//*[@id="grid-body-table"]/tbody/tr[3]/td[2]/div/button')
			sleep(1)
			span_click("下一步")
			sleep(1)
			switch_to("xpath",'//*[@id="receiveGenRecmentWin-iframe"]')
			sleep(1)
			span_click("确认")
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("收款处理-承兑汇票收票，纸质合并收票成功！")
			span_click("收款处理")
			sleep(3)
			
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("收款处理-承兑汇票收票，操作失败！" + str(traceback.format_exc()))
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

