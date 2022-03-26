# encoding=utf-8
# @Time : 2020/12/20 14:49
# @Author : zzg
# 此文件是测试内部借款管理
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
class Test_Dbsq(unittest.TestCase):
	
	# 启动浏览器
	def setUp(self):
		# 启动浏览器的另外一个方法：通过封装启动浏览器的驱动，启动不同浏览器
		self.driver = get("chrome")
	
	# 登陆系统、对系统设置进行操作
	def test_trade(self):
		
		login(G_Ora_Url, mindy, Password, "亚唐科技")
	
		js_gd("xpath", "//span[contains(text(),'内部借款管理')]")
		# 用JS的方法点击资金结算管理菜单按钮
		js_click("xpath", "//span[contains(text(),'内部借款管理')]")
		sleep(1)
		
		# 测试基础设置->往来决议🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱
		try:
			logger.info("开始测试->内部借款管理->基础设置->往来决议")
			# 点击基础设置菜单
			click("xpath", "//li[@f_value='ifloansetting']/descendant-or-self::*[5]")
			sleep(1)
			# 点击往来决议
			click("xpath", "//span[contains(text(),'往来决议')]")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			
			# 测试新增💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			for i in range(1,4):
				# 切入往来决议的iframe窗体
				switch_to("xpath", "//iframe[@id='contactDecision-tab-iframe']")
				span_click("新增")
				
				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='addWin-iframe']")
				sleep(1)
				
				# 授信对象
				click("xpath", "//input[@id='combobox-input-opporgid']")
				sleep(1)
				up_enter_click("//input[@id='combobox-input-opporgid']")
				
				
				# 决议编号
				name = "JYBH"+str(time.strftime("%H%M%S"))
				input("xpath", "//input[@id='contractcode']", name)
				sleep(1)
				
				# 授信额度
				input("xpath", "//input[@id='amount-input']", "5000")
				sleep(1)
				
				# 授信开始日期
				today = date.today()
				due_date = today - timedelta(days=20)
				click("xpath", "//input[@id='begindate-input']")
				sleep(1)
				clear("xpath", "//input[@id='begindate-input']")
				sleep(1)
				input("xpath", "//input[@id='begindate-input']", str(due_date))
				time.sleep(1)
				
				# 授信截止日期
				today = date.today()
				due_date = today + timedelta(days=60)
				click("xpath", "//input[@id='enddate-input']")
				sleep(1)
				clear("xpath", "//input[@id='enddate-input']")
				sleep(1)
				input("xpath", "//input[@id='enddate-input']", str(due_date))
				time.sleep(1)
				
				# 描述框中填入值
				click("xpath","//textarea[@id='description']")
				sleep(1)
				input("xpath", "//textarea[@id='description']", "备注")
				sleep(1)
				
				# 点击保存按钮
				click("xpath", "//span[text()='保存']")
				sleep(1)
				
				# 退出所有iframe窗体
				switch_default()
				# 用隐式等待方法等页面出现新增成功的提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				if i ==3 :
					print("基础设置-往来决议，新增成功！")
				time.sleep(3)
			
			
			# 测试修改💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入往来决议的iframe窗体
			switch_to("xpath", "//iframe[@id='contactDecision-tab-iframe']")
			#刷新、勾选按钮
			click("xpath",'//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath",'//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("修改")
			# 切入新增的iframe窗体
			switch_to("xpath", "//iframe[@id='modWin-iframe']")
			sleep(1)
			
			# 描述框中填入值
			clear("xpath", "//textarea[@id='description']")
			sleep(1)
			input("xpath", "//textarea[@id='description']", "修改")
			sleep(1)
			
			# 点击保存按钮
			click("xpath", "//span[text()='保存']")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功')]")
			print("基础设置-往来决议，修改成功！")
			time.sleep(3)
			
			# 测试删除💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入往来决议的iframe窗体
			switch_to("xpath", "//iframe[@id='contactDecision-tab-iframe']")
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("删除")
			ok_click()
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功')]")
			print("基础设置-往来决议，删除成功！")
			time.sleep(3)
			
			# 测试审核、撤销审核💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入往来决议的iframe窗体
			switch_to("xpath", "//iframe[@id='contactDecision-tab-iframe']")
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("审核")
			ok_click()
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'成功条数:1')]")
			print("基础设置-往来决议，审核成功！")
			time.sleep(3)
			
			#撤销审核💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入往来决议的iframe窗体
			switch_to("xpath", "//iframe[@id='contactDecision-tab-iframe']")
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("审核",'取消审核')
			ok_click()
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'取消审核成功1笔')]")
			print("基础设置-往来决议，取消审核成功！")
			time.sleep(3)
			
			# 测试作废💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入往来决议的iframe窗体
			switch_to("xpath", "//iframe[@id='contactDecision-tab-iframe']")
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[2]/td[2]/div/button')
			sleep(1)
			
			span_click("审核")
			ok_click()
			sleep(3)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[2]/td[2]/div/button')
			sleep(1)
			
			span_click("作废")
			ok_click()
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'作废成功:1条')]")
			print("基础设置-往来决议，作废成功！")
			time.sleep(3)
			
			# 测试变更💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入往来决议的iframe窗体
			switch_to("xpath", "//iframe[@id='contactDecision-tab-iframe']")
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("审核")
			ok_click()
			sleep(3)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("变更")
			# 切入新增的iframe窗体
			switch_to("xpath", "//iframe[@id='modWin-iframe']")
			sleep(1)
			
			# 描述框中填入值
			clear("xpath", "//textarea[@id='description']")
			sleep(1)
			input("xpath", "//textarea[@id='description']", "变更")
			sleep(1)
			
			# 点击保存按钮
			click("xpath", "//span[text()='保存']")
			sleep(1)
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现删除的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功')]")
			print("基础设置-往来决议，变更成功！")
			time.sleep(3)
			
			#点击基础设置、收回窗体
			click("xpath", "//li[@f_value='ifloansetting']/descendant-or-self::*[5]")
			sleep(1)
			
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("往来决议失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		
		
		# 添加所需要的数据🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱
		try:
			logger.info("开始添加需要的数据")
			#收回窗体
			js_click("xpath", "//span[contains(text(),'内部借款管理')]")
			sleep(1)
		
			# 点击系统设置
			click("xpath", "//div[@class='sysconfigset']")
			sleep(1)
			# 点击进入系统设置页面
			switch_to("xpath", "//iframe[@id='systemconfig-tab-iframe']")
			sleep(1)
			
			
			# 将页面的滚动条滑动到‘利率方案’页面的地方
			js_gd("xpath", "//span[contains(text(),'利率方案')]")
			# 用JS的方法利率方案字段菜单按钮
			js_click("xpath", "//span[contains(text(),'利率方案')]")
			sleep(1)
			switch_default()
			
			#借出往来合同💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			#切入利率方案窗体
			switch_to("xpath", "//iframe[@id='interestRateSchemes-tab-iframe']")
			
			# 用JS的方法点击新增按钮
			js_click("xpath", "//span[text()='新增']")
			sleep(1)
			# 切入新增的iframe窗体
			switch_to("xpath", "//iframe[@id='addWin-iframe']")
			
			# 输入代码
			code = "LV"+str(random.randint(1,100))
			input("xpath", "//input[@name='code']", code)
			sleep(1)
			
			# 输入名称
			input("xpath", "//input[@id='name']", "借出往来合同")
			sleep(1)
			
			# 单据对象
			click("xpath", "//input[@id='combobox-input-noteobjectid']")
			sleep(1)
			input("xpath", "//input[@id='combobox-input-noteobjectid']", "借出往来合同")
			sleep(1)
			input_enter("xpath", "//input[@id='combobox-input-noteobjectid']")
			sleep(1)
			input_down("xpath", "//input[@id='combobox-input-noteobjectid']")
			sleep(1)
			input_enter("xpath", "//input[@id='combobox-input-noteobjectid']")
			sleep(1)
			
			# 利率类型
			click("xpath", "//input[@id='combobox-input-interestratetypeid']")
			sleep(1)
			input("xpath", "//input[@id='combobox-input-interestratetypeid']", "固定利率")
			sleep(1)
			input_enter("xpath", "//input[@id='combobox-input-interestratetypeid']")
			sleep(1)
			input_down("xpath", "//input[@id='combobox-input-interestratetypeid']")
			sleep(1)
			input_enter("xpath", "//input[@id='combobox-input-interestratetypeid']")
			sleep(1)
			
			# 共享模式
			click("xpath", "//input[@id='combobox-input-includemode']")
			sleep(1)
			input("xpath", "//input[@id='combobox-input-includemode']", "下属组织共享")
			sleep(1)
			input_enter("xpath", "//input[@id='combobox-input-includemode']")
			sleep(1)
			input_down("xpath", "//input[@id='combobox-input-includemode']")
			sleep(1)
			input_enter("xpath", "//input[@id='combobox-input-includemode']")
			sleep(1)
			
			# 点击保存按钮
			click("xpath", "//span[text()='保存']")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("利率方案-借出往来合同，新增成功！")
			time.sleep(3)
			
			#借入往来合同💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", "//iframe[@id='interestRateSchemes-tab-iframe']")
			# 用JS的方法点击新增按钮
			js_click("xpath", "//span[text()='新增']")
			sleep(1)
			
			# 切入新增的iframe窗体
			switch_to("xpath", "//iframe[@id='addWin-iframe']")
			
			# 输入代码
			code = "LV"+str(random.randint(1,100))
			input("xpath", "//input[@name='code']", code)
			sleep(1)
			
			# 输入名称
			input("xpath", "//input[@id='name']", "借入往来合同")
			sleep(1)
			# 单据对象
			click("xpath", "//input[@id='combobox-input-noteobjectid']")
			sleep(1)
			input("xpath", "//input[@id='combobox-input-noteobjectid']", "借入往来合同")
			sleep(1)
			input_enter("xpath", "//input[@id='combobox-input-noteobjectid']")
			sleep(1)
			input_down("xpath", "//input[@id='combobox-input-noteobjectid']")
			sleep(1)
			input_enter("xpath", "//input[@id='combobox-input-noteobjectid']")
			sleep(1)
			
			# 利率类型
			click("xpath", "//input[@id='combobox-input-interestratetypeid']")
			sleep(1)
			input("xpath", "//input[@id='combobox-input-interestratetypeid']", "固定利率")
			sleep(1)
			input_enter("xpath", "//input[@id='combobox-input-interestratetypeid']")
			sleep(1)
			input_down("xpath", "//input[@id='combobox-input-interestratetypeid']")
			sleep(1)
			input_enter("xpath", "//input[@id='combobox-input-interestratetypeid']")
			sleep(1)
			
			# 共享模式
			click("xpath", "//input[@id='combobox-input-includemode']")
			sleep(1)
			input("xpath", "//input[@id='combobox-input-includemode']", "下属组织共享")
			sleep(1)
			input_enter("xpath", "//input[@id='combobox-input-includemode']")
			sleep(1)
			input_down("xpath", "//input[@id='combobox-input-includemode']")
			sleep(1)
			input_enter("xpath", "//input[@id='combobox-input-includemode']")
			sleep(1)
			
			# 点击保存按钮
			click("xpath", "//span[text()='保存']")
			sleep(1)
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("利率方案-借入往来合同，新增成功！")
			time.sleep(3)
			
			#计提方案-借出往来合同💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 点击系统设置
			click("xpath", "//div[@class='sysconfigset']")
			sleep(1)
			# 点击进入系统设置页面
			switch_to("xpath", "//iframe[@id='systemconfig-tab-iframe']")
			sleep(1)
			
			# 将页面的滚动条滑动到‘计提方案’页面的地方
			js_gd("xpath", "//span[contains(text(),'计提方案')]")
			# 用JS的方法利率方案字段菜单按钮
			js_click("xpath", "//span[contains(text(),'计提方案')]")
			sleep(1)
			switch_default()
			
			#切入计提窗体
			switch_to("xpath",'//*[@id="accrualschemes-tab-iframe"]')
			span_click("新增")
			switch_to("xpath",'//*[@id="addWin-iframe"]')
			
			#方案代码
			code=str(time.strftime("%Y%m%d%H%M%S"))
			input("xpath",'//*[@id="code"]',code)
			sleep(1)
			
			#方案名称
			name = "FAMC"+str(time.strftime("%H%M%S"))
			input("xpath",'//*[@id="name"]',name)
			sleep(1)
			
			# 计提业务
			input("xpath", '//*[@id="combobox-input-businessid"]', 'JCWLHT-借出往来合同')
			sleep(1)
			up_enter_click('//*[@id="combobox-input-businessid"]')
			
			#计提频率
			input("xpath",'//*[@id="combobox-input-accrualfrequencymode"]','按季计提')
			sleep(1)
			up_enter_click('//*[@id="combobox-input-accrualfrequencymode"]')
			
			#融资产品
			click("xpath",'//*[@id="combobox-input-financeproductid"]')
			sleep(1)
			click("xpath",'//*[@id="financeproductid-combogrid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			
			span_click("保存")
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("利率方案-计提方案，借出往来合同成功！")
			time.sleep(3)
			
			# 计提方案-借入往来合同💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入计提窗体
			switch_to("xpath", '//*[@id="accrualschemes-tab-iframe"]')
			span_click("新增")
			switch_to("xpath", '//*[@id="addWin-iframe"]')
			
			# 方案代码
			code = str(time.strftime("%Y%m%d%H%M%S"))
			input("xpath", '//*[@id="code"]', code)
			sleep(1)
			
			# 方案名称
			name = "FAMC" + str(time.strftime("%H%M%S"))
			input("xpath", '//*[@id="name"]', name)
			sleep(1)
			
			# 计提业务
			input("xpath", '//*[@id="combobox-input-businessid"]', 'JRWLHT-借入往来合同')
			sleep(1)
			up_enter_click('//*[@id="combobox-input-businessid"]')
			
			# 计提频率
			input("xpath", '//*[@id="combobox-input-accrualfrequencymode"]', '按季计提')
			sleep(1)
			up_enter_click('//*[@id="combobox-input-accrualfrequencymode"]')
			
			# 融资产品
			click("xpath", '//*[@id="combobox-input-financeproductid"]')
			sleep(1)
			click("xpath", '//*[@id="financeproductid-combogrid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("保存")
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("利率方案-计提方案，借入往来合同成功！")
			time.sleep(3)
			
			#回到内部借款页面
			js_gd("xpath", "//span[contains(text(),'内部借款管理')]")
			# 用JS的方法点击资金结算管理菜单按钮
			js_click("xpath", "//span[contains(text(),'内部借款管理')]")
			sleep(1)
			
			#借款类型💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 点击基础设置菜单
			click("xpath", "//li[@f_value='ifloansetting']/descendant-or-self::*[5]")
			sleep(1)
			# 点击往来决议
			click("xpath", "//span[contains(text(),'借款类型')]")
			sleep(1)
			switch_default()
			
			#切入借款类型窗体
			switch_to("xpath",'//*[@id="loantype-tab-iframe"]')
			span_click("新增")
			switch_to("xpath",'//*[@id="addWin-iframe"]')
			
			#代码
			code = str(time.strftime("%Y%m%d%H%M%S"))
			input("xpath",'//*[@id="code"]',code)
			sleep(1)
			
			#名称
			name="JKLX"+str(time.strftime("%H%M%S"))
			input("xpath",'//*[@id="name"]',name)
			sleep(1)
			
			span_click("保存")
			
			#退出所有窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("基础设置-借款类型，新增成功！")
			time.sleep(3)
			
			#点击基础设置，收回窗体
			click("xpath", "//li[@f_value='ifloansetting']/descendant-or-self::*[5]")
			sleep(1)
			
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("利率方案失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		
		
		
		# 测试借出方管理->借出合同登记🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱
		try:
			logging.info("开始测试借出方管理->借出合同登记")
			# 点击借出方管理菜单
			click("xpath", "//span[@title='借出方管理']")
			sleep(1)
			# 点击理财合同登记菜单
			click("xpath", "//span[@title='借出合同登记']")
			sleep(1)
			# 退出所有的iframe窗体
			switch_default()
			
			#测试新增功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			for i in range(1, 4):
				# 切入iframe窗体
				switch_to("xpath", "//iframe[@id='lendingcontract-tab-iframe']")
				
				span_click("新增")
				sleep(1)
				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='addWin-iframe']")
				sleep(1)
				
				# 借入组织
				click("xpath", "//input[@id='combobox-input-opporgid']")
				sleep(1)
				up_enter_click("//input[@id='combobox-input-opporgid']")
				
				# 借款类型
				click("xpath", "//input[@id='combobox-input-loantype']")
				sleep(1)
				up_enter_click("//input[@id='combobox-input-loantype']")
				
				
				# 合同编号
				temp1 = "HTBH"+str(time.strftime("%H%M%S"))
				# 合同编号
				input("xpath", "//input[@id='contractcode']", temp1)
				sleep(1)
				
				# 合同签订日
				today = date.today()
				sign_date = today - timedelta(days=20)
				click("xpath", "//input[@id='signeddate-input']")
				sleep(1)
				clear("xpath", "//input[@id='signeddate-input']")
				sleep(1)
				input("xpath", "//input[@id='signeddate-input']", str(sign_date))
				time.sleep(1)
				
				# 合同起始日
				today = date.today()
				sign_date = today - timedelta(days=20)
				click("xpath", "//input[@id='begindate-input']")
				sleep(1)
				clear("xpath", "//input[@id='begindate-input']")
				sleep(1)
				input("xpath", "//input[@id='begindate-input']", str(sign_date))
				time.sleep(1)
				
				# 合同到期日
				today = date.today()
				end_date = today + timedelta(days=20)
				click("xpath", "//input[@id='enddate-input']")
				sleep(1)
				clear("xpath", "//input[@id='enddate-input']")
				sleep(1)
				input("xpath", "//input[@id='enddate-input']", str(end_date))
				time.sleep(1)
				
				# 合同期限日
				input("xpath", "//input[@id='loantermday-input']", "40")
				sleep(1)
				
				# 币种
				input("xpath", "//input[@id='combobox-input-currencyid']", "人民币")
				sleep(1)
				up_enter_click("//input[@id='combobox-input-currencyid']")
				
				# 金额
				money=random.randint(100,1000)
				double_click("xpath", "//input[@id='amount-input']")
				sleep(1)
				input("xpath", "//input[@id='amount-input']", money)
				sleep(1)
				
				# 借款经办人
				input("xpath", "//input[@id='loanoperator']", "zzg")
				sleep(1)
				
				# 计息开始日期
				today = date.today()
				start_date = today + timedelta(days=20)
				click("xpath", "//input[@id='intereststartdate-input']")
				sleep(1)
				clear("xpath", "//input[@id='intereststartdate-input']")
				sleep(1)
				input("xpath", "//input[@id='intereststartdate-input']", str(start_date))
				time.sleep(1)
				
				# 费率
				clear("xpath", "//input[@id='feerate-input']")
				sleep(1)
				input("xpath", "//input[@id='feerate-input']", "5")
				sleep(1)
				
				
				
				# 计息方式
				click("xpath", "//input[@id='combobox-input-interestmode']")
				sleep(1)
				up_enter_click("//input[@id='combobox-input-interestmode']")
				
				# 利率方案
				input("xpath", "//input[@id='combobox-input-interestrateschemeid']","借出往来合同")
				sleep(1)
				up_enter_click("//input[@id='combobox-input-interestrateschemeid']")
				
				#利率
				double_click("xpath",'//*[@id="factinterestrate-input"]')
				sleep(1)
				input("xpath",'//*[@id="factinterestrate-input"]','5')
				sleep(1)
				
				# 点击保存按钮
				click("xpath", "//span[text()='保存']")
				sleep(1)
				
				# 退出所有iframe窗体
				switch_default()
				# 用隐式等待方法等页面出现提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				if i == 4:
					print("借出方管理->借出合同登记，新增成功")
				time.sleep(3)
			
			# 测试修改功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入iframe窗体
			switch_to("xpath", "//iframe[@id='lendingcontract-tab-iframe']")
			#刷新、勾选按钮
			click("xpath",'//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("修改")
			# 切入修改的iframe窗体
			switch_to("xpath", "//iframe[@id='modWin-iframe']")
			
			# 备注框中输入新内容
			input("xpath", "//textarea[@id='description']", "修改")
			sleep(1)
			
			# 点击保存按钮
			click("xpath", "//span[text()='保存']")
			sleep(1)
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("借出方管理->借出合同登记，修改成功！")
			time.sleep(3)
			
			# 测试删除功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入iframe窗体
			switch_to("xpath", "//iframe[@id='lendingcontract-tab-iframe']")
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("删除")
			ok_click()
			
			switch_default()
			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'成功删除1条记录！')]")
			print("借出方管理->借出合同登记，删除成功！")
			time.sleep(3)
			
			# 测试审核、撤销审核功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入iframe窗体
			switch_to("xpath", "//iframe[@id='lendingcontract-tab-iframe']")
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("审核")
			ok_click()
			
			#退出所有窗体
			switch_default()
			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'成功审核1条记录')]")
			print("借出方管理->借出合同登记，审核成功！")
			time.sleep(3)
			
			# 测试撤销审核功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入iframe窗体
			switch_to("xpath", "//iframe[@id='lendingcontract-tab-iframe']")
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("审核",'取消审核')
			ok_click()
			
			#退出所有窗体
			switch_default()
			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'成功取消审核:1条')]")
			print("借出方管理->借出合同登记，取消审核成功！")
			time.sleep(3)
			
			# 测试变更功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入iframe窗体
			switch_to("xpath", "//iframe[@id='lendingcontract-tab-iframe']")
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("审核")
			ok_click()
			sleep(3)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			span_click("变更")
			
			switch_to("xpath",'//*[@id="modWin-iframe"]')
			#描述
			clear("xpath",'//*[@id="description"]')
			sleep(1)
			input("xpath",'//*[@id="description"]','变更')
			sleep(1)
			
			span_click("保存")
			
			# 退出所有窗体
			switch_default()
			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("借出方管理->借出合同登记，变更成功！")
			time.sleep(3)
			
			# 测试继承功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入iframe窗体
			switch_to("xpath", "//iframe[@id='lendingcontract-tab-iframe']")
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("继承")
			switch_to("xpath",'//*[@id="modWin-iframe"]')
			
			# 合同编号
			temp1 = "HTBH" + str(time.strftime("%H%M%S"))
			# 合同编号
			input("xpath", "//input[@id='contractcode']", temp1)
			sleep(1)
			
			# 合同签订日
			today = date.today()
			sign_date = today - timedelta(days=20)
			click("xpath", "//input[@id='signeddate-input']")
			sleep(1)
			clear("xpath", "//input[@id='signeddate-input']")
			sleep(1)
			input("xpath", "//input[@id='signeddate-input']", str(sign_date))
			time.sleep(1)
			
			# 合同起始日
			today = date.today()
			sign_date = today - timedelta(days=20)
			click("xpath", "//input[@id='begindate-input']")
			sleep(1)
			clear("xpath", "//input[@id='begindate-input']")
			sleep(1)
			input("xpath", "//input[@id='begindate-input']", str(sign_date))
			time.sleep(1)
			
			# 合同到期日
			today = date.today()
			end_date = today + timedelta(days=20)
			click("xpath", "//input[@id='enddate-input']")
			sleep(1)
			clear("xpath", "//input[@id='enddate-input']")
			sleep(1)
			input("xpath", "//input[@id='enddate-input']", str(end_date))
			time.sleep(1)
			
			# 合同期限日
			input("xpath", "//input[@id='loantermday-input']", "40")
			sleep(1)
			
			# 币种
			clear("xpath", "//input[@id='combobox-input-currencyid']")
			sleep(1)
			input("xpath", "//input[@id='combobox-input-currencyid']", "人民币")
			sleep(1)
			up_enter_click("//input[@id='combobox-input-currencyid']")
			
			# 金额
			money = random.randint(100, 1000)
			double_click("xpath", "//input[@id='amount-input']")
			sleep(1)
			input("xpath", "//input[@id='amount-input']", money)
			sleep(1)
			
			# 借款经办人
			input("xpath", "//input[@id='loanoperator']", "zzg")
			sleep(1)
			
			# 计息开始日期
			today = date.today()
			start_date = today + timedelta(days=20)
			click("xpath", "//input[@id='intereststartdate-input']")
			sleep(1)
			clear("xpath", "//input[@id='intereststartdate-input']")
			sleep(1)
			input("xpath", "//input[@id='intereststartdate-input']", str(start_date))
			time.sleep(1)
			
			# 费率
			clear("xpath", "//input[@id='feerate-input']")
			sleep(1)
			input("xpath", "//input[@id='feerate-input']", "5")
			sleep(1)
			
			# 计息方式
			click("xpath", "//input[@id='combobox-input-interestmode']")
			sleep(1)
			up_enter_click("//input[@id='combobox-input-interestmode']")
			
			# 利率方案
			input("xpath", "//input[@id='combobox-input-interestrateschemeid']", "借出往来合同")
			sleep(1)
			up_enter_click("//input[@id='combobox-input-interestrateschemeid']")
			
			# 利率
			double_click("xpath", '//*[@id="factinterestrate-input"]')
			sleep(1)
			input("xpath", '//*[@id="factinterestrate-input"]', '5')
			sleep(1)
			
			# 点击保存按钮
			click("xpath", "//span[text()='保存']")
			sleep(1)
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("借出方管理->借出合同登记，继承成功")
			time.sleep(3)
			
			# 测试放款功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入iframe窗体
			switch_to("xpath", "//iframe[@id='lendingcontract-tab-iframe']")
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("审核")
			ok_click()
			sleep(3)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			span_click("放款")
			
			switch_to("xpath",'//*[@id="lendPayWin-iframe"]')
			
			#放款日期
			today =str( date.today())
			input("xpath",'//*[@id="lenddate-input"]',today)
			sleep(1)
			
			#放款金额
			click("xpath",'//*[@id="amount-input"]')
			sleep(1)
			input("xpath", '//*[@id="amount-input"]','50')
			sleep(1)
			
			span_click("保存")
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("借出方管理->借出合同登记，放款成功")
			time.sleep(3)
			
			# 测试回款功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			#去主动放款页面对放款单进行审核
			span_click("放款处理")
			switch_to("xpath",'//*[@id="lendingloan-tab-iframe"]')
			span_click("主动放款")
			switch_to("xpath",'//*[@id="subTabTwo-iframe"]')
			
			#勾选数据
			click("xpath",'//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			span_click("审核")
			ok_click()
			sleep(3)
			switch_default()
			
			#回到借出合同登记页面
			span_click("借出合同登记")
			# 切入iframe窗体
			switch_to("xpath", "//iframe[@id='lendingcontract-tab-iframe']")
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("回款")
			switch_to("xpath",'//*[@id="lendPayWin-iframe"]')
			
			#回款日期
			today = str(date.today())
			input("xpath",'//*[@id="repaydate-input"]',today)
			sleep(1)
			
			#回款金额
			double_click("xpath",'//*[@id="principal-input"]')
			input("xpath",'//*[@id="principal-input"]','10')
			sleep(1)
			
			#结息方式
			clear("xpath",'//*[@id="combobox-input-settlementinterestmode"]')
			sleep(1)
			input("xpath",'//*[@id="combobox-input-settlementinterestmode"]','结算归还本金的利息')
			sleep(1)
			up_enter_click('//*[@id="combobox-input-settlementinterestmode"]')
			
			#应计利息
			double_click("xpath",'//*[@id="possibleinterest-input"]')
			sleep(1)
			input("xpath",'//*[@id="possibleinterest-input"]','1')
			sleep(1)
			
			# 实收利息
			double_click("xpath", '//*[@id="interest-input"]')
			sleep(1)
			input("xpath", '//*[@id="interest-input"]', '1')
			sleep(1)
			
			span_click("保存")
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("借出方管理->借出合同登记，回款成功")
			time.sleep(3)
			
			# 测试利息登记💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入iframe窗体
			switch_to("xpath", "//iframe[@id='lendingcontract-tab-iframe']")
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("利息登记")
			switch_to("xpath",'//*[@id="lendPayWin-iframe"]')
			
			# 回款日期
			today = str(date.today())
			input("xpath", '//*[@id="repaydate-input"]', today)
			sleep(1)
			
			# 结息方式
			clear("xpath", '//*[@id="combobox-input-settlementinterestmode"]')
			sleep(1)
			input("xpath", '//*[@id="combobox-input-settlementinterestmode"]', '结算归还本金的利息')
			sleep(1)
			up_enter_click('//*[@id="combobox-input-settlementinterestmode"]')
			
			# 应计利息
			double_click("xpath", '//*[@id="possibleinterest-input"]')
			sleep(1)
			input("xpath", '//*[@id="possibleinterest-input"]', '1')
			sleep(1)
			
			# 实收利息
			double_click("xpath", '//*[@id="interest-input"]')
			sleep(1)
			input("xpath", '//*[@id="interest-input"]', '1')
			sleep(1)
			
			span_click("保存")
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("借出方管理->借出合同登记，利息登记成功")
			time.sleep(3)
			
			# 测试应收利息💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入iframe窗体
			switch_to("xpath", "//iframe[@id='lendingcontract-tab-iframe']")
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("应收利息")
			switch_to("xpath",'//*[@id="lendPayWin-iframe"]')
			
			span_click("试算")
			sleep(1)
			span_click("取消")
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现提示框
			#implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("借出方管理->借出合同登记，应收利息成功")
			time.sleep(3)
			
			# 测试重新生成还款计息计划💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入iframe窗体
			switch_to("xpath", "//iframe[@id='lendingcontract-tab-iframe']")
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("调整还款计划","重新生成还款计息计划")
			ok_click()
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'成功重新计息:1条！')]")
			print("借出方管理->借出合同登记，重新生成还款计息计划成功")
			time.sleep(3)
			
			# 测试重新生成计提还款计息计划💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入iframe窗体
			switch_to("xpath", "//iframe[@id='lendingcontract-tab-iframe']")
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("调整还款计划", "重新生成计提还款计息计划")
			
			#计提方案
			click("xpath",'//*[@id="combobox-input-schemesid"]')
			sleep(1)
			up_enter_click('//*[@id="combobox-input-schemesid"]')
			
			
			
			click("xpath","//div[text()='确定']")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'成功重新计息:1条')]")
			print("借出方管理->借出合同登记，重新生成计提还款计息计划")
			time.sleep(3)
			
			# 测试作废💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入iframe窗体
			switch_to("xpath", "//iframe[@id='lendingcontract-tab-iframe']")
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[3]/td[2]/div/button')
			sleep(1)
			
			span_click("审核")
			ok_click()
			sleep(3)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[3]/td[2]/div/button')
			sleep(1)
			span_click("作废")
			ok_click()
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'成功作废1条记录！')]")
			print("借出方管理->借出合同登记，作废成功")
			time.sleep(3)
			
			#收回窗体
			click("xpath", "//span[@title='借出方管理']")
			sleep(1)
			
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("借出合同登记失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)

		
		
		# 测试借出方管理->放款处理->申请放款处理🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱
		try:
			logging.info("开始测试借出方管理->放款处理->申请放款处理")
			# 点击借出方管理菜单
			click("xpath", "//span[@title='借出方管理']")
			sleep(1)
			# 点击理财合同登记菜单
			click("xpath", "//span[@title='放款处理']")
			sleep(1)
			# 退出所有的iframe窗体
			switch_default()
			
			#切换组织去下级组织做数据💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			#切换组织
			refresh()
			sleep(1)
			js_click("xpath", "//input[@id='combobox-input-orgidswitch']")
			sleep(1)
			clear("xpath", "//input[@id='combobox-input-orgidswitch']")
			sleep(1)
			input("xpath", "//input[@id='combobox-input-orgidswitch']", "Mindy科技有限公司")
			sleep(1)
			input_down("xpath", "//in"
			                    "put[@id='combobox-input-orgidswitch']")
			input_enter("xpath", "//input[@id='combobox-input-orgidswitch']")
			sleep(1)
			
			#去借入方管理
			js_gd("xpath", "//span[contains(text(),'内部借款管理')]")
			# 用JS的方法点击资金结算管理菜单按钮
			js_click("xpath", "//span[contains(text(),'内部借款管理')]")
			sleep(1)
	
			click("xpath", "//span[@title='借入方管理']")
			sleep(1)
			# 点击理财合同登记菜单
			click("xpath", "//span[@title='放款申请']")
			sleep(1)
			# 退出所有的iframe窗体
			switch_default()
			
			#切入放款申请窗体
			for i in range(1,3):
				switch_to("xpath", '//*[@id="lendinglendapply-tab-iframe"]')
				span_click("新增")
				switch_to("xpath",'//*[@id="modWin-iframe"]')
				#勾选按钮
				click("xpath",'//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
				sleep(1)
				span_click("放款申请")
				switch_parent()
				switch_to("xpath",'//*[@id="modWin-iframe"]')
				sleep(1)
				
				#放款日期
				today=date.today()
				input("xpath",'//*[@id="lenddate-input"]',str(today))
				sleep(1)
				
				#放款金额
				click("xpath",'//*[@id="amount-input"]')
				sleep(1)
				input("xpath",'//*[@id="amount-input"]','15')
				sleep(1)
				span_click("保存")
				
				# 退出所有iframe窗体
				switch_default()
				# 用隐式等待方法等页面出现提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				time.sleep(3)
				
				# 对数据进行送审
				switch_to("xpath", '//*[@id="lendinglendapply-tab-iframe"]')
				# 勾选数据
				click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
				sleep(1)
				span_click("送审")
				ok_click()
				sleep(3)
				
				double_click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[3]/div')
				sleep(1)
				switch_to("xpath", '//*[@id="wf_taskProcessing_win-iframe"]')
				span_click("同意")
				switch_parent()
				sleep(3)
				
				double_click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[3]/div')
				sleep(1)
				switch_to("xpath", '//*[@id="wf_taskProcessing_win-iframe"]')
				span_click("同意")
				switch_parent()
				sleep(3)
				
				# 勾选数据、提交
				click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
				sleep(1)
				span_click("提交")
				sleep(3)
				switch_default()
			
			
			#回到上级组织
			refresh()
			sleep(1)
			js_click("xpath", "//input[@id='combobox-input-orgidswitch']")
			sleep(1)
			clear("xpath", "//input[@id='combobox-input-orgidswitch']")
			sleep(1)
			input("xpath", "//input[@id='combobox-input-orgidswitch']", "亚唐科技")
			sleep(1)
			input_down("xpath", "//in"
			                    "put[@id='combobox-input-orgidswitch']")
			input_enter("xpath", "//input[@id='combobox-input-orgidswitch']")
			sleep(1)
			
			# 去借入方管理
			js_gd("xpath", "//span[contains(text(),'内部借款管理')]")
			# 用JS的方法点击资金结算管理菜单按钮
			js_click("xpath", "//span[contains(text(),'内部借款管理')]")
			sleep(1)
			
			click("xpath", "//span[@title='借出方管理']")
			sleep(1)
			# 点击理财合同登记菜单
			click("xpath", "//span[@title='放款处理']")
			sleep(1)
			# 退出所有的iframe窗体
			switch_default()
			
			# 测试生成交易单💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			#切入申请放款窗体
			switch_to("xpath",'//*[@id="lendingloan-tab-iframe"]')
			switch_to("xpath",'//*[@id="subTabOne-iframe"]')
			
			#勾选按钮
			click("xpath",'//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("生成交易单")
			switch_to("xpath",'//*[@id="lendGenRecWin-iframe"]')
			
			#支付类型
			input("xpath",'//*[@id="combobox-input-dealtype"]','其他')
			sleep(1)
			up_enter_click('//*[@id="combobox-input-dealtype"]')
			
			span_click("下一步")
			switch_parent()
			
			switch_to("xpath",'//*[@id="addRecWin-iframe"]')
			#交易类型
			input("xpath",'//*[@id="combobox-input-paytypeid"]','103-对外付款')
			sleep(1)
			up_enter_click('//*[@id="combobox-input-paytypeid"]')
			
			#结算方式
			clear("xpath",'//*[@id="combobox-input-settlementmodeid"]')
			sleep(1)
			input("xpath",'//*[@id="combobox-input-settlementmodeid"]','601-其他支付')
			sleep(1)
			up_enter_click('//*[@id="combobox-input-settlementmodeid"]')
			
			#付方账户
			click("xpath",'//*[@id="combobox-input-ourbankaccountid"]')
			sleep(1)
			up_enter_click('//*[@id="combobox-input-ourbankaccountid"]')
			
			#收方名称
			input("xpath",'//*[@id="combobox-input-oppcounterpartyid"]','浙江华语科技')
			sleep(1)
			
			span_click("保存")
			
			#退出所有窗体
			switch_default()
			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("借出方管理->放款处理->申请放款，生成交易单成功！")
			time.sleep(3)
			
			# 测试作废💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入申请放款窗体
			switch_to("xpath", '//*[@id="lendingloan-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			
			# 勾选按钮
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[2]/td[2]/div/button')
			sleep(1)
			
			span_click("作废")
			ok_click()
			# 退出所有窗体
			switch_default()
			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'作废成功:1笔！失败:0笔！')]")
			print("借出方管理->放款处理->申请放款，作废成功！")
			time.sleep(3)
			
			# 收回窗体
			click("xpath", "//span[@title='借出方管理']")
			sleep(1)
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("申请放款失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
			
		
		# 测试借出方管理->放款处理->主动放款🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱
		try:
			logging.info("开始测试借出方管理->放款处理->主动放款")
			# 点击借出方管理菜单
			click("xpath", "//span[@title='借出方管理']")
			sleep(1)
			# 点击理财合同登记菜单
			click("xpath", "//span[@title='放款处理']")
			sleep(1)
			# 退出所有的iframe窗体
			switch_default()
			
			#去借出合同登记页面做数据💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨 💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 点击借出方管理菜单
			click("xpath", "//span[@title='借出合同登记']")
			sleep(1)
			for i in range (1,5):
				switch_to("xpath", "//iframe[@id='lendingcontract-tab-iframe']")
				sleep(1)
				# 刷新、勾选按钮
				click("xpath", '//*[@id="gridbar-page-refresh"]')
				sleep(1)
				click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
				sleep(1)

				span_click("放款")
				switch_to("xpath", '//*[@id="lendPayWin-iframe"]')
				
				# 放款日期
				today = str(date.today())
				input("xpath", '//*[@id="lenddate-input"]', today)
				sleep(1)
				
				# 放款金额
				click("xpath", '//*[@id="amount-input"]')
				sleep(1)
				input("xpath", '//*[@id="amount-input"]', '15')
				sleep(1)
				
				span_click("保存")
				
				# 退出所有iframe窗体
				switch_default()
				# 用隐式等待方法等页面出现提示框
				time.sleep(3)
			
			#回到放款处理页面
			click("xpath", "//span[@title='放款处理']")
			sleep(1)
			switch_default()
			
			# 测试修改功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath",'//*[@id="lendingloan-tab-iframe"]')
			span_click("主动放款")
			switch_to("xpath",'//*[@id="subTabTwo-iframe"]')
			sleep(1)
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("修改")
			switch_to("xpath",'//*[@id="modWin-iframe"]')
			input("xpath",'//*[@id="description"]','修改')
			sleep(1)
			span_click("保存")
			

			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功')]")
			print("借出方管理->放款处理->主动放款，修改成功")
			time.sleep(3)
			
			# 测试送审功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="lendingloan-tab-iframe"]')
			span_click("主动放款")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			sleep(1)
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("送审")
			ok_click()
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'送审成功')]")
			print("借出方管理->放款处理->主动放款，送审成功")
			time.sleep(3)
			
			# 测试撤销送审功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="lendingloan-tab-iframe"]')
			span_click("主动放款")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			sleep(1)
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("送审",'撤销送审')
			ok_click()
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功')]")
			print("借出方管理->放款处理->主动放款，撤销送审成功")
			time.sleep(3)
			
			# 测试删除功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="lendingloan-tab-iframe"]')
			span_click("主动放款")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			sleep(1)
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("删除")
			ok_click()
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'删除成功')]")
			print("借出方管理->放款处理->主动放款，删除成功")
			time.sleep(3)
			
			# 测试审核、撤销审核功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="lendingloan-tab-iframe"]')
			span_click("主动放款")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			sleep(1)
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("审核")
			ok_click()
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功')]")
			print("借出方管理->放款处理->主动放款，审核成功")
			time.sleep(3)
			
			# 测试撤销审核功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="lendingloan-tab-iframe"]')
			span_click("主动放款")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			sleep(1)
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("审核",'取消审核')
			ok_click()
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功')]")
			print("借出方管理->放款处理->主动放款，取消审核成功")
			time.sleep(3)
			
			# 测试变更功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="lendingloan-tab-iframe"]')
			span_click("主动放款")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			sleep(1)
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("审核")
			ok_click()
			sleep(3)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click('变更')
			switch_to("xpath",'//*[@id="modWin-iframe"]')
			input("xpath",'//*[@id="description"]','变更')
			sleep(1)
			span_click("保存")
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功')]")
			print("借出方管理->放款处理->主动放款，变更成功")
			time.sleep(3)
			
			# 测试作废功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="lendingloan-tab-iframe"]')
			span_click("主动放款")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			sleep(1)
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("审核")
			ok_click()
			sleep(3)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click('作废')
			ok_click()
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'作废成功')]")
			print("借出方管理->放款处理->主动放款，作废成功")
			time.sleep(3)
			
			# 测试放款功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="lendingloan-tab-iframe"]')
			span_click("主动放款")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			sleep(1)
			
			span_click('放款')
			#切入放款窗体
			switch_to("xpath",'//*[@id="modWin-iframe"]')
			#勾选按钮
			click("xpath",'//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div')
			sleep(1)
			span_click("确认放款")
			
			switch_parent()
			switch_to("xpath",'//*[@id="modWin-iframe"]')
			sleep(1)
			
			#放款日期
			today=date.today()
			input("xpath",'//*[@id="lenddate-input"]',str(today))
			sleep(1)
			
			#放款金额
			click("xpath",'//*[@id="amount-input"]')
			sleep(1)
			input("xpath",'//*[@id="amount-input"]','20')
			sleep(1)
			
			span_click("保存")
			
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功')]")
			print("借出方管理->放款处理->主动放款，放款成功")
			time.sleep(3)
			
			
			# 测试生成交易单功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="lendingloan-tab-iframe"]')
			span_click("主动放款")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			sleep(1)
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("审核")
			ok_click()
			sleep(3)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("生成交易单")
			switch_to("xpath",'//*[@id="lendGenRecWin-iframe"]')
			
			# 支付类型
			input("xpath", '//*[@id="combobox-input-dealtype"]', '其他')
			sleep(1)
			up_enter_click('//*[@id="combobox-input-dealtype"]')
			
			span_click("下一步")
			switch_parent()
			
			switch_to("xpath", '//*[@id="addRecWin-iframe"]')
			
			# 交易类型
			input("xpath", '//*[@id="combobox-input-paytypeid"]', '103-对外付款')
			sleep(1)
			up_enter_click('//*[@id="combobox-input-paytypeid"]')
			
			# 结算方式
			clear("xpath", '//*[@id="combobox-input-settlementmodeid"]')
			sleep(1)
			input("xpath", '//*[@id="combobox-input-settlementmodeid"]', '601-其他支付')
			sleep(1)
			up_enter_click('//*[@id="combobox-input-settlementmodeid"]')
			
			# 付方账户
			click("xpath",'//*[@id="combobox-input-ourbankaccountid"]')
			sleep(1)
			up_enter_click('//*[@id="combobox-input-ourbankaccountid"]')
		
			# 收方名称
			input("xpath", '//*[@id="combobox-input-oppcounterpartyid"]', '浙江华语科技')
			sleep(1)
			
			span_click("保存")
			
			# 退出所有窗体
			switch_default()
			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("借出方管理->放款处理->主动放款，生成交易单成功！")
			time.sleep(3)
			
			# 点击借出方管理菜单，收回窗体
			click("xpath", "//span[@title='借出方管理']")
			sleep(1)
			
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("主动放款失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
	
	
		# 测试借出方管理->放款处理->回款登记🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱
		try:
			logging.info("开始测试借出方管理->放款处理->主动放款")
			# 点击借出方管理菜单
			click("xpath", "//span[@title='借出方管理']")
			sleep(1)
			# 点击理财合同登记菜单
			click("xpath", "//span[@title='回款登记']")
			sleep(1)
			# 退出所有的iframe窗体
			switch_default()
			
			# 回款💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨 💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			for i in range(1,4):
				#切入回款登记窗体
				switch_to("xpath",'//*[@id="lendingsrepayment-tab-iframe"]')
				sleep(1)
				span_click("回款")
				#切入回款窗体
				switch_to("xpath",'//*[@id="modWin-iframe"]')
				#勾选按钮
				click("xpath",'//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
				sleep(1)
				span_click("确认回款")
				
				switch_parent()
				switch_to("xpath",'//*[@id="modWin-iframe"]')
				sleep(1)
				#回款日期
				today=date.today()
				input("xpath",'//*[@id="repaydate-input"]',str(today))
				sleep(1)
				
				#回款金额
				double_click("xpath",'//*[@id="principal-input"]')
				sleep(1)
				input("xpath",'//*[@id="principal-input"]','5')
				sleep(1)
				
				span_click("保存")
				
				# 退出所有窗体
				switch_default()
				# 用隐式等待方法等页面出现提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				if i ==3 :
					print("借出方管理->回款登记，回款成功！")
				time.sleep(3)
			
			# 测试修改功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨 💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入回款登记窗体
			switch_to("xpath", '//*[@id="lendingsrepayment-tab-iframe"]')
			#刷新、勾选按钮
			click("xpath",'//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("修改")
			switch_to("xpath",'//*[@id="modWin-iframe"]')
			#修改描述
			input("xpath",'//*[@id="description"]','修改')
			sleep(1)
			span_click("保存")
			
			#退出所有的窗体
			switch_default()
			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("借出方管理->回款登记，修改成功！")
			time.sleep(3)
			
			# 测试删除功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨 💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入回款登记窗体
			switch_to("xpath", '//*[@id="lendingsrepayment-tab-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("删除")
			ok_click()
			
			# 退出所有的窗体
			switch_default()
			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'删除成功')]")
			print("借出方管理->回款登记，删除成功！")
			time.sleep(3)
			
			# 测试送审、撤销送审功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨 💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入回款登记窗体
			switch_to("xpath", '//*[@id="lendingsrepayment-tab-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("送审")
			ok_click()
			
			# 退出所有的窗体
			switch_default()
			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'送审成功1笔')]")
			print("借出方管理->回款登记，送审成功！")
			time.sleep(3)
			
			# 测试撤销送审功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入回款登记窗体
			switch_to("xpath", '//*[@id="lendingsrepayment-tab-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("送审",'撤销送审')
			ok_click()
			
			# 退出所有的窗体
			switch_default()
			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功')]")
			print("借出方管理->回款登记，撤销送审成功！")
			time.sleep(3)
			
			# 测试审核、取消审核功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入回款登记窗体
			switch_to("xpath", '//*[@id="lendingsrepayment-tab-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[2]/td[2]/div/button')
			sleep(1)
			
			span_click("审核")
			ok_click()
			
			# 退出所有的窗体
			switch_default()
			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功')]")
			print("借出方管理->回款登记，审核成功！")
			time.sleep(3)
			
			# 测试取消审核功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入回款登记窗体
			switch_to("xpath", '//*[@id="lendingsrepayment-tab-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[2]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("审核",'取消审核')
			ok_click()
			
			# 退出所有的窗体
			switch_default()
			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("借出方管理->回款登记，取消审核成功！")
			time.sleep(3)
			
			# 测试变更功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入回款登记窗体
			switch_to("xpath", '//*[@id="lendingsrepayment-tab-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[2]/td[2]/div/button')
			sleep(1)
			
			span_click("审核")
			ok_click()
			sleep(3)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[2]/td[2]/div/button')
			sleep(1)
			
			span_click("变更")
			#切入变更窗体
			switch_to("xpath",'//*[@id="modWin-iframe"]')
			input("xpath",'//*[@id="description"]','变更')
			sleep(1)
			span_click("保存")
			
			# 退出所有的窗体
			switch_default()
			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("借出方管理->回款登记，变更成功！")
			time.sleep(3)
			
			# 测试作废功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨 💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入回款登记窗体
			switch_to("xpath", '//*[@id="lendingsrepayment-tab-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[2]/td[2]/div/button')
			sleep(1)
			
			span_click("审核")
			ok_click()
			sleep(3)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[2]/td[2]/div/button')
			sleep(1)
			span_click("作废")
			ok_click()
			
			# 退出所有的窗体
			switch_default()
			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'成功条数:1')]")
			print("借出方管理->回款登记，作废成功！")
			time.sleep(3)
			
			# 测试生成交易单功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨 💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入回款登记窗体
			switch_to("xpath", '//*[@id="lendingsrepayment-tab-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("送审")
			ok_click()
			time.sleep(3)
			
			#二审
			double_click("xpath",'//*[@id="grid-body-table"]/tbody/tr[1]/td[3]/div')
			sleep(1)
			switch_to("xpath",'//*[@id="wf_taskProcessing_win-iframe"]')
			span_click("同意")
			switch_parent()
			sleep(3)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			span_click("生成交易单")
			
			switch_to("xpath",'//*[@id="lendGenRecWin-iframe"]')
			
			#支付类型
			clear("xpath",'//*[@id="combobox-input-dealtype"]')
			sleep(1)
			input("xpath",'//*[@id="combobox-input-dealtype"]','其他')
			sleep(1)
			up_enter_click('//*[@id="combobox-input-dealtype"]')
			span_click("下一步")
			switch_parent()
			switch_to("xpath",'//*[@id="addPayWin-iframe"]')
			sleep(1)
			
			#交易类型
			click_up_click('//*[@id="combobox-input-paytypeid"]')
			
			#结算方式
			clear("xpath",'//*[@id="combobox-input-settlementmodeid"]')
			sleep(1)
			input_up_click('//*[@id="combobox-input-settlementmodeid"]','单笔转账收款')
			
			#收方账户
			click_up_click('//*[@id="combobox-input-ourbankaccountid"]')
			
			#付方名称
			input("xpath",'//*[@id="combobox-input-oppcounterpartyid"]','浙江华语科技')
			sleep(1)
			
			span_click("保存")
			
			# 退出所有的窗体
			switch_default()
			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("借出方管理->回款登记，生成交易单成功！")
			time.sleep(3)
			
			# 点击借出方管理菜单，收回窗体
			click("xpath", "//span[@title='借出方管理']")
			sleep(1)
			
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("回款登记失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		
		
		# 测试借入方管理->借入合同登记🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱
		try:
			logging.info("开始测试借入方管理->借入合同统计")
			# 点击借出方管理菜单
			click("xpath", "//span[@title='借入方管理']")
			sleep(1)
			# 点击理财合同登记菜单
			click("xpath", "//span[@title='借入合同登记']")
			sleep(1)
			# 退出所有的iframe窗体
			switch_default()
			
			#测试新增功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			for i in range(1,4):
				#切入借出合同登记窗体
				switch_to("xpath",'//*[@id="loancontract-tab-iframe"]')
				span_click("新增")
				#切入新增窗体
				switch_to("xpath",'//*[@id="addWin-iframe"]')
				
				#借出组织
				click_up_click('//*[@id="combobox-input-opporgid"]')
				
				#借款类型
				click_up_click('//*[@id="combobox-input-loantype"]')
				
				#合同编号
				HTBH="HTBH"+str(time.strftime("%H%M%S"))
				input("xpath",'//*[@id="contractcode"]',HTBH)
				sleep(1)
				
				#合同签订日
				today=str(date.today())
				input("xpath",'//*[@id="signeddate-input"]',today)
				sleep(1)
				
				# 合同起始日
				click("xpath", '//*[@id="begindate-input"]')
				sleep(1)
				clear("xpath", '//*[@id="begindate-input"]')
				sleep(1)
				input("xpath", '//*[@id="begindate-input"]', today)
				sleep(1)
				
				#合同到期日
				expireddate = date.today() + timedelta(days=60)
				click("xpath", '//*[@id="enddate-input"]')
				sleep(1)
				clear("xpath", '//*[@id="enddate-input"]')
				sleep(1)
				input("xpath",'//*[@id="enddate-input"]',str(expireddate))
				sleep(1)
				
				#合同期限日
				click("xpath",'//*[@id="loantermday-input"]')
				sleep(1)
				input("xpath",'//*[@id="loantermday-input"]','60')
				sleep(1)
				
				#币种
				input_up_click('//*[@id="combobox-input-currencyid"]','CNY-人民币')
				
				#金额
				double_click("xpath",'//*[@id="amount-input"]')
				sleep(1)
				input("xpath",'//*[@id="amount-input"]','5000')
				sleep(1)
				
				#借款经办人
				input("xpath",'//*[@id="loanoperator"]','zzg')
				sleep(1)
				
				#费率
				double_click("xpath",'//*[@id="feerate-input"]')
				sleep(1)
				input("xpath",'//*[@id="feerate-input"]','5')
				sleep(1)
				
				#计息方式
				click_up_click('//*[@id="combobox-input-interestmode"]')
				
				#利率方案
				input_up_click('//*[@id="combobox-input-interestrateschemeid"]','借入往来合同')
				
				#利率
				double_click("xpath",'//*[@id="factinterestrate-input"]')
				sleep(1)
				input("xpath",'//*[@id="factinterestrate-input"]','5')
				sleep(1)
				
				span_click("保存")
				# 退出所有窗体
				switch_default()
				# 用隐式等待方法等页面出现提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				if i ==3:
					print("借入方管理->借入合同登记，新增成功！")
				time.sleep(3)
			
			# 测试修改功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			#切入借出合同登记窗体
			switch_to("xpath",'//*[@id="loancontract-tab-iframe"]')
			#刷新、勾选按钮
			click("xpath",'//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("修改")
			switch_to("xpath",'//*[@id="modWin-iframe"]')
			#描述
			input("xpath",'//*[@id="description"]','修改')
			sleep(1)
			span_click("保存")
			
			# 退出所有窗体
			switch_default()
			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("借入方管理->借入合同登记，修改成功！")
			time.sleep(3)
			
			# 测试删除功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入借出合同登记窗体
			switch_to("xpath", '//*[@id="loancontract-tab-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("删除")
			ok_click()
			
			# 退出所有窗体
			switch_default()
			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'成功删除1条记录！')]")
			print("借入方管理->借入合同登记，删除成功！")
			time.sleep(3)
			
			# 测试审核、取消审核功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入借出合同登记窗体
			switch_to("xpath", '//*[@id="loancontract-tab-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("审核")
			ok_click()
			
			# 退出所有窗体
			switch_default()
			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'成功审核1条记录')]")
			print("借入方管理->借入合同登记，审核成功！")
			time.sleep(3)
			
			# 测试取消审核功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入借出合同登记窗体
			switch_to("xpath", '//*[@id="loancontract-tab-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("审核",'取消审核')
			ok_click()
			
			# 退出所有窗体
			switch_default()
			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'成功取消审核:1条')]")
			print("借入方管理->借入合同登记，取消审核成功！")
			time.sleep(3)
			
			# 测试变更功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入借出合同登记窗体
			switch_to("xpath", '//*[@id="loancontract-tab-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("审核")
			ok_click()
			sleep(3)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("变更")
			switch_to("xpath",'//*[@id="modWin-iframe"]')
			#描述
			input("xpath",'//*[@id="description"]','变更')
			sleep(1)
			span_click("保存")
			
			# 退出所有窗体
			switch_default()
			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("借入方管理->借入合同登记，变更成功！")
			time.sleep(3)
			
			# 测试继承功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入借出合同登记窗体
			switch_to("xpath", '//*[@id="loancontract-tab-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("继承")
			switch_to("xpath",'//*[@id="modWin-iframe"]')
			# 借款类型
			click_up_click('//*[@id="combobox-input-loantype"]')
			
			# 合同编号
			HTBH = "HTBH" + str(time.strftime("%H%M%S"))
			input("xpath", '//*[@id="contractcode"]', HTBH)
			sleep(1)
			
			# 合同签订日
			today = str(date.today())
			input("xpath", '//*[@id="signeddate-input"]', today)
			sleep(1)
			
			# 合同起始日
			click("xpath", '//*[@id="begindate-input"]')
			sleep(1)
			clear("xpath", '//*[@id="begindate-input"]')
			sleep(1)
			input("xpath", '//*[@id="begindate-input"]', today)
			sleep(1)
			
			# 合同到期日
			expireddate = date.today() + timedelta(days=60)
			click("xpath", '//*[@id="enddate-input"]')
			sleep(1)
			clear("xpath", '//*[@id="enddate-input"]')
			sleep(1)
			input("xpath", '//*[@id="enddate-input"]', str(expireddate))
			sleep(1)
			
			# 合同期限日
			click("xpath", '//*[@id="loantermday-input"]')
			sleep(1)
			input("xpath", '//*[@id="loantermday-input"]', '60')
			sleep(1)
			
			# 币种
			input_up_click('//*[@id="combobox-input-currencyid"]', 'CNY-人民币')
			
			# 金额
			double_click("xpath", '//*[@id="amount-input"]')
			sleep(1)
			input("xpath", '//*[@id="amount-input"]', '5000')
			sleep(1)
			
			# 借款经办人
			input("xpath", '//*[@id="loanoperator"]', 'zzg')
			sleep(1)
			
			# 费率
			double_click("xpath", '//*[@id="feerate-input"]')
			sleep(1)
			input("xpath", '//*[@id="feerate-input"]', '5')
			sleep(1)
			
			# 计息方式
			click_up_click('//*[@id="combobox-input-interestmode"]')
			
			# 利率方案
			input_up_click('//*[@id="combobox-input-interestrateschemeid"]', '借入往来合同')
			
			# 利率
			double_click("xpath", '//*[@id="factinterestrate-input"]')
			sleep(1)
			input("xpath", '//*[@id="factinterestrate-input"]', '5')
			sleep(1)
			
			span_click("保存")
			# 退出所有窗体
			switch_default()
			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("借入方管理->借入合同登记，继承成功！")
			time.sleep(3)
			
			# 测试提款功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入借出合同登记窗体
			switch_to("xpath", '//*[@id="loancontract-tab-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("审核")
			ok_click()
			sleep(3)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			span_click("提款")
			
			switch_to("xpath",'//*[@id="lendPayWin-iframe"]')
			#提款日期
			today=date.today()
			input("xpath",'//*[@id="lenddate-input"]',str(today))
			sleep(1)
			
			#金额
			click("xpath",'//*[@id="amount-input"]')
			sleep(1)
			input("xpath",'//*[@id="amount-input"]','15')
			sleep(1)
			span_click("保存")
			
			# 退出所有窗体
			switch_default()
			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("借入方管理->借入合同登记，提款成功！")
			time.sleep(3)
			
			# 测试还款功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			#去提款登记页面审核
			span_click("提款登记")
			switch_to("xpath",'//*[@id="loanlends-tab-iframe"]')
			click("xpath",'//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			span_click("审核")
			ok_click()
			sleep(3)
			switch_default()
			
			#回到借入合同登记页面
			span_click("借入合同登记")
			# 切入借出合同登记窗体
			switch_to("xpath", '//*[@id="loancontract-tab-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("还款")
			switch_to("xpath",'//*[@id="lendPayWin-iframe"]')
			#还款日期
			input("xpath",'//*[@id="repaydate-input"]',str(today))
			sleep(1)
			
			#还款金额
			double_click("xpath",'//*[@id="principal-input"]')
			sleep(1)
			input("xpath",'//*[@id="principal-input"]','5')
			sleep(1)
			
			span_click("保存")
			
			# 退出所有窗体
			switch_default()
			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("借入方管理->借入合同登记，还款成功！")
			time.sleep(3)
			
			# 测试利息登记功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入借出合同登记窗体
			switch_to("xpath", '//*[@id="loancontract-tab-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("利息登记")
			switch_to("xpath",'//*[@id="lendPayWin-iframe"]')
			sleep(1)
			#还款日期
			today=date.today()
			input("xpath",'//*[@id="repaydate-input"]',str(today))
			sleep(1)
			
			#结息方式
			click("xpath",'//*[@id="combobox-input-settlementinterestmode"]')
			sleep(1)
			clear("xpath",'//*[@id="combobox-input-settlementinterestmode"]')
			sleep(1)
			input_up_click('//*[@id="combobox-input-settlementinterestmode"]','结算归还本金的利息')
			
			#还息金额
			double_click("xpath",'//*[@id="interest-input"]')
			sleep(1)
			input("xpath",'//*[@id="interest-input"]','1')
			sleep(1)
			
			span_click("保存")
			# 退出所有窗体
			switch_default()
			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("借入方管理->借入合同登记，利息登记成功！")
			time.sleep(3)
			
			# 测试应还利息功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入借出合同登记窗体
			switch_to("xpath", '//*[@id="loancontract-tab-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("应还利息")
			switch_to("xpath",'//*[@id="lendPayWin-iframe"]')
			span_click("试算")
			sleep(2)
			span_click("取消")
			
			# 退出所有窗体
			switch_default()
			# 用隐式等待方法等页面出现提示框
			print("借入方管理->借入合同登记，利息试算成功！")
			time.sleep(3)
			
			# 测试重新生成还款计息计划功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入借出合同登记窗体
			switch_to("xpath", '//*[@id="loancontract-tab-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("调整还款计划",'重新生成还款计息计划')
			ok_click()
			
			# 退出所有窗体
			switch_default()
			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'成功重新计息:1条！')]")
			print("借入方管理->借入合同登记，重新生成还款计息计划成功！")
			time.sleep(3)
			
			# 测试重新生成计提还款计息计划功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入借出合同登记窗体
			switch_to("xpath", '//*[@id="loancontract-tab-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("调整还款计划", '重新生成计提还款计息计划')
			
			#计提方案
			click_up_click('//*[@id="combobox-input-schemesid"]')
			click("xpath",'//*[@id="schemeWin-btn-0"]/div[2]')
			sleep(1)
			
			# 退出所有窗体
			switch_default()
			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'成功重新计息:1条！')]")
			print("借入方管理->借入合同登记，重新生成计提还款计息计划成功！")
			time.sleep(3)
			
			# 测试作废功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入借出合同登记窗体
			switch_to("xpath", '//*[@id="loancontract-tab-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[3]/td[2]/div/button')
			sleep(1)
			
			span_click("审核")
			ok_click()
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[3]/td[2]/div/button')
			sleep(1)
			
			span_click("作废")
			ok_click()
			
			# 退出所有窗体
			switch_default()
			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'成功作废1条记录！')]")
			print("借入方管理->借入合同登记，作废成功！")
			time.sleep(3)
			
			# 点击借入方管理菜单，收回窗体
			click("xpath", "//span[@title='借入方管理']")
			sleep(1)
			
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("借入合同登记失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		
		
		# 测试借入方管理->提款登记🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱
		try:
			logging.info("开始测试借入方管理->提款登记")
			# 点击借出方管理菜单
			click("xpath", "//span[@title='借入方管理']")
			sleep(1)
			# 点击理财合同登记菜单
			click("xpath", "//span[@title='提款登记']")
			sleep(1)
			# 退出所有的iframe窗体
			switch_default()
			
			# 测试提款功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			for i in range(1,4):
				#切入提款登记窗体
				switch_to("xpath",'//*[@id="loanlends-tab-iframe"]')
				span_click("提款")
				
				switch_to("xpath",'//*[@id="modWin-iframe"]')
				click("xpath",'//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
				sleep(1)
				span_click("确认提款")
				switch_parent()
				switch_to("xpath",'//*[@id="modWin-iframe"]')
				sleep(1)
				
				#提款日期
				today=date.today()
				input("xpath",'//*[@id="lenddate-input"]',str(today))
				sleep(1)
				
				#提款金额
				money =random.randint(5,30)
				click("xpath",'//*[@id="amount-input"]')
				sleep(1)
				input("xpath",'//*[@id="amount-input"]',money)
				sleep(1)
				span_click("保存")
				# 退出所有窗体
				switch_default()
				# 用隐式等待方法等页面出现提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				if i == 3:
					print("借入方管理->提款登记，提款成功！")
				time.sleep(3)
		
			# 测试修改功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入提款登记窗体
			switch_to("xpath", '//*[@id="loanlends-tab-iframe"]')
			#刷新、勾选按钮
			click("xpath",'//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("修改")
			switch_to("xpath",'//*[@id="modWin-iframe"]')
			input("xpath",'//*[@id="description"]','修改')
			sleep(1)
			span_click("保存")
			
			# 退出所有窗体
			switch_default()
			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("借入方管理->提款登记，修改成功！")
			time.sleep(3)
			
			# 测试删除功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入提款登记窗体
			switch_to("xpath", '//*[@id="loanlends-tab-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("删除")
			ok_click()
			
			# 退出所有窗体
			switch_default()
			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'成功删除1条记录！')]")
			print("借入方管理->提款登记，删除成功！")
			time.sleep(3)
			
			# 测试送审功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入提款登记窗体
			switch_to("xpath", '//*[@id="loanlends-tab-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("送审")
			ok_click()
			
			# 退出所有窗体
			switch_default()
			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'成功送审1条记录！')]")
			print("借入方管理->提款登记，送审成功！")
			time.sleep(3)
			
			# 测试撤销送审功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入提款登记窗体
			switch_to("xpath", '//*[@id="loanlends-tab-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("送审",'撤销送审')
			ok_click()
			
			# 退出所有窗体
			switch_default()
			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'成功撤销送审1条记录！')]")
			print("借入方管理->提款登记，撤销送审成功！")
			time.sleep(3)
			
			# 测试变更功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入提款登记窗体
			switch_to("xpath", '//*[@id="loanlends-tab-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("送审")
			ok_click()
			sleep(3)
			double_click("xpath",'//*[@id="grid-body-table"]/tbody/tr[1]/td[3]/div')
			sleep(1)
			switch_to("xpath",'//*[@id="wf_taskProcessing_win-iframe"]')
			span_click("同意")
			switch_parent()
			sleep(3)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			span_click("变更")
			switch_to("xpath",'//*[@id="modWin-iframe"]')
			input("xpath",'//*[@id="description"]','变更')
			sleep(1)
			span_click("保存")
			
			# 退出所有窗体
			switch_default()
			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("借入方管理->提款登记，变更成功！")
			time.sleep(3)
			
			# 测试作废功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入提款登记窗体
			switch_to("xpath", '//*[@id="loanlends-tab-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("送审")
			ok_click()
			sleep(3)
			double_click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[3]/div')
			sleep(1)
			switch_to("xpath", '//*[@id="wf_taskProcessing_win-iframe"]')
			span_click("同意")
			switch_parent()
			sleep(3)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			span_click("作废")
			ok_click()
			# 退出所有窗体
			switch_default()
			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'成功作废1条记录！')]")
			print("借入方管理->提款登记，作废成功！")
			time.sleep(3)
			
			# 测试审核功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入提款登记窗体
			switch_to("xpath", '//*[@id="loanlends-tab-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("审核")
			ok_click()
			
			# 退出所有窗体
			switch_default()
			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功')]")
			print("借入方管理->提款登记，审核成功！")
			time.sleep(3)
			
			# 测试撤销审核功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入提款登记窗体
			switch_to("xpath", '//*[@id="loanlends-tab-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("审核",'取消审核')
			ok_click()
			
			# 退出所有窗体
			switch_default()
			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功')]")
			print("借入方管理->提款登记，取消审核成功！")
			time.sleep(3)
			
			# 测试生成交易单💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入提款登记窗体
			switch_to("xpath", '//*[@id="loanlends-tab-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("审核")
			ok_click()
			sleep(3)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("生成交易单")
			switch_to("xpath", '//*[@id="lendGenRecWin-iframe"]')
			
			# 支付类型
			clear("xpath", '//*[@id="combobox-input-dealtype"]')
			sleep(1)
			input("xpath", '//*[@id="combobox-input-dealtype"]', '其他')
			sleep(1)
			up_enter_click('//*[@id="combobox-input-dealtype"]')
			
			span_click("下一步")
			switch_parent()
			
			switch_to("xpath", '//*[@id="addRecWin-iframe"]')
			# 交易类型
			input("xpath", '//*[@id="combobox-input-paytypeid"]', '201-外部收款')
			sleep(1)
			up_enter_click('//*[@id="combobox-input-paytypeid"]')
			
			# 结算方式
			clear("xpath", '//*[@id="combobox-input-settlementmodeid"]')
			sleep(1)
			input("xpath", '//*[@id="combobox-input-settlementmodeid"]', '单笔转账收款')
			sleep(1)
			up_enter_click('//*[@id="combobox-input-settlementmodeid"]')
			
			# 付方账户
			click("xpath", '//*[@id="combobox-input-ourbankaccountid"]')
			sleep(1)
			up_enter_click('//*[@id="combobox-input-ourbankaccountid"]')
			
			# 收方名称
			input("xpath", '//*[@id="combobox-input-oppcounterpartyid"]', '浙江华语科技')
			sleep(1)
			
			span_click("保存")
			
			# 退出所有窗体
			switch_default()
			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("借入方管理->提款登记，生成交易单成功！")
			time.sleep(3)
			# 点击借入方管理菜单，收回窗体
			click("xpath", "//span[@title='借入方管理']")
			sleep(1)
			
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("提款登记失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		
		
		# 测试借入方管理->还款处理🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱
		try:
			logging.info("开始测试借入方管理->还款处理")
			# 点击借出方管理菜单
			click("xpath", "//span[@title='借入方管理']")
			sleep(1)
			# 点击理财合同登记菜单
			click("xpath", "//span[@title='还款处理']")
			sleep(1)
			# 退出所有的iframe窗体
			switch_default()
			
			# 测试还款功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			for i in range(1,4):
				# 切入还款处理窗体
				switch_to("xpath", '//*[@id="loanrepays-tab-iframe"]')
				span_click("还款")
				
				switch_to("xpath", '//*[@id="modWin-iframe"]')
				click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
				sleep(1)
				span_click("确认还款")
				switch_parent()
				switch_to("xpath", '//*[@id="modWin-iframe"]')
				sleep(1)
				
				# 还款日期
				today = date.today()
				input("xpath", '//*[@id="repaydate-input"]', str(today))
				sleep(1)
				
				# 还款金额
				double_click("xpath", '//*[@id="principal-input"]')
				sleep(1)
				input("xpath", '//*[@id="principal-input"]', '5')
				sleep(1)
				
				span_click("保存")
				# 退出所有有窗体
				switch_default()
				# 用隐式等待方法等页面出现提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				if i ==3:
					print("借入方管理->还款处理，还款成功！")
				time.sleep(3)
			
			
			# 测试修改功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入还款处理窗体
			switch_to("xpath", '//*[@id="loanrepays-tab-iframe"]')
			#刷新、勾选按钮
			click("xpath",'//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("修改")
			switch_to("xpath",'//*[@id="modWin-iframe"]')
			input("xpath",'//*[@id="description"]','修改')
			sleep(1)
			span_click("保存")
			
			# 退出所有有窗体
			switch_default()
			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("借入方管理->还款处理，修改成功！")
			time.sleep(3)
			
			# 测试删除功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入还款处理窗体
			switch_to("xpath", '//*[@id="loanrepays-tab-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("删除")
			ok_click()
			
			# 退出所有有窗体
			switch_default()
			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'成功删除1条记录！')]")
			print("借入方管理->还款处理，删除成功！")
			time.sleep(3)
			
			# 测试送审功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入还款处理窗体
			switch_to("xpath", '//*[@id="loanrepays-tab-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("送审")
			ok_click()
			
			# 退出所有有窗体
			switch_default()
			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'成功送审1条记录！')]")
			print("借入方管理->还款处理，送审成功！")
			time.sleep(3)
			
			# 测试撤销送审功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入还款处理窗体
			switch_to("xpath", '//*[@id="loanrepays-tab-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("送审",'撤销送审')
			ok_click()
			
			# 退出所有有窗体
			switch_default()
			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'成功撤销送审1条记录！')]")
			print("借入方管理->还款处理，撤销送审成功！")
			time.sleep(3)
			
			# 测试审核功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入还款处理窗体
			switch_to("xpath", '//*[@id="loanrepays-tab-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[2]/td[2]/div/button')
			sleep(1)
			
			span_click("审核")
			ok_click()
			
			# 退出所有有窗体
			switch_default()
			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功!')]")
			print("借入方管理->还款处理，审核成功！")
			time.sleep(3)
			
			# 测试取消审核功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入还款处理窗体
			switch_to("xpath", '//*[@id="loanrepays-tab-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[2]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("审核",'取消审核')
			ok_click()
			
			# 退出所有有窗体
			switch_default()
			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("借入方管理->还款处理，取消审核成功！")
			time.sleep(3)
			
			# 测试变更功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入还款处理窗体
			switch_to("xpath", '//*[@id="loanrepays-tab-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[2]/td[2]/div/button')
			sleep(1)
			
			span_click("审核")
			ok_click()
			sleep(3)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[2]/td[2]/div/button')
			sleep(1)
			span_click("变更")
			
			switch_to("xpath",'//*[@id="modWin-iframe"]')
			input("xpath",'//*[@id="description"]','变更')
			sleep(1)
			span_click("保存")
			
			# 退出所有有窗体
			switch_default()
			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("借入方管理->还款处理，变更成功！")
			time.sleep(3)
			
			# 测试作废功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入还款处理窗体
			switch_to("xpath", '//*[@id="loanrepays-tab-iframe"]')
			sleep(1)
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[2]/td[2]/div/button')
			sleep(1)
			
			span_click("审核")
			ok_click()
			sleep(3)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[2]/td[2]/div/button')
			sleep(1)
			span_click("作废")
			ok_click()
			
			# 退出所有有窗体
			switch_default()
			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'成功作废1条记录！')]")
			print("借入方管理->还款处理，作废成功！")
			time.sleep(3)
			
			# 测试生成交易单功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入还款处理窗体
			switch_to("xpath", '//*[@id="loanrepays-tab-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("送审")
			ok_click()
			sleep(3)
			
			double_click("xpath",'//*[@id="grid-body-table"]/tbody/tr[1]/td[3]/div')
			sleep(1)
			switch_to("xpath",'//*[@id="wf_taskProcessing_win-iframe"]')
			span_click("同意")
			switch_parent()
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("生成交易单")
			switch_to("xpath",'//*[@id="lendGenRecWin-iframe"]')
			clear("xpath",'//*[@id="combobox-input-dealtype"]')
			sleep(1)
			input_up_click('//*[@id="combobox-input-dealtype"]','其他')
			span_click("下一步")
			switch_parent()
			switch_to("xpath",'//*[@id="addRecWin-iframe"]')
			
			#交易类型
			input_up_click('//*[@id="combobox-input-paytypeid"]','103-对外付款')
			sleep(1)
			#结算方式
			clear("xpath",'//*[@id="combobox-input-settlementmodeid"]')
			sleep(1)
			input_up_click('//*[@id="combobox-input-settlementmodeid"]','601-其他支付')
			
			#付方账户
			click_up_click('//*[@id="combobox-input-ourbankaccountid"]')
			
			#收方名称
			input("xpath",'//*[@id="combobox-input-oppcounterpartyid"]','浙江华语科技')
			sleep(1)
			span_click("保存")
			
			# 退出所有有窗体
			switch_default()
			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("借入方管理->还款处理，生成交易单成功！")
			time.sleep(3)
			
			# 点击借入方管理菜单，收回窗体
			click("xpath", "//span[@title='借入方管理']")
			sleep(1)
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("提款登记失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		
		
		# 测试借入方管理->还款处理🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱
		try:
			logging.info("开始测试借入方管理->还款处理")
			# 点击借出方管理菜单
			click("xpath", "//span[@title='借入方管理']")
			sleep(1)
			# 点击理财合同登记菜单
			click("xpath", "//span[@title='还款处理']")
			sleep(1)
			# 退出所有的iframe窗体
			switch_default()
			
			# 测试还款功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			for i in range(1, 4):
				# 切入还款处理窗体
				switch_to("xpath", '//*[@id="loanrepays-tab-iframe"]')
				span_click("还款")
				
				switch_to("xpath", '//*[@id="modWin-iframe"]')
				click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
				sleep(1)
				span_click("确认还款")
				switch_parent()
				switch_to("xpath", '//*[@id="modWin-iframe"]')
				sleep(1)
				
				# 还款日期
				today = date.today()
				input("xpath", '//*[@id="repaydate-input"]', str(today))
				sleep(1)
				
				# 还款金额
				double_click("xpath", '//*[@id="principal-input"]')
				sleep(1)
				input("xpath", '//*[@id="principal-input"]', '5')
				sleep(1)
				
				span_click("保存")
				# 退出所有有窗体
				switch_default()
				# 用隐式等待方法等页面出现提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				if i == 3:
					print("借入方管理->还款处理，还款成功！")
				time.sleep(3)
			
			# 测试修改功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入还款处理窗体
			switch_to("xpath", '//*[@id="loanrepays-tab-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("修改")
			switch_to("xpath", '//*[@id="modWin-iframe"]')
			input("xpath", '//*[@id="description"]', '修改')
			sleep(1)
			span_click("保存")
			
			# 退出所有有窗体
			switch_default()
			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("借入方管理->还款处理，修改成功！")
			time.sleep(3)
			
			# 测试删除功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入还款处理窗体
			switch_to("xpath", '//*[@id="loanrepays-tab-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("删除")
			ok_click()
			
			# 退出所有有窗体
			switch_default()
			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'成功删除1条记录！')]")
			print("借入方管理->还款处理，删除成功！")
			time.sleep(3)
			
			# 测试送审功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入还款处理窗体
			switch_to("xpath", '//*[@id="loanrepays-tab-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("送审")
			ok_click()
			
			# 退出所有有窗体
			switch_default()
			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'成功送审1条记录！')]")
			print("借入方管理->还款处理，送审成功！")
			time.sleep(3)
			
			# 测试撤销送审功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入还款处理窗体
			switch_to("xpath", '//*[@id="loanrepays-tab-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("送审", '撤销送审')
			ok_click()
			
			# 退出所有有窗体
			switch_default()
			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'成功撤销送审1条记录！')]")
			print("借入方管理->还款处理，撤销送审成功！")
			time.sleep(3)
			
			# 测试审核功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入还款处理窗体
			switch_to("xpath", '//*[@id="loanrepays-tab-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[2]/td[2]/div/button')
			sleep(1)
			
			span_click("审核")
			ok_click()
			
			# 退出所有有窗体
			switch_default()
			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功!')]")
			print("借入方管理->还款处理，审核成功！")
			time.sleep(3)
			
			# 测试取消审核功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入还款处理窗体
			switch_to("xpath", '//*[@id="loanrepays-tab-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[2]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("审核", '取消审核')
			ok_click()
			
			# 退出所有有窗体
			switch_default()
			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("借入方管理->还款处理，取消审核成功！")
			time.sleep(3)
			
			# 测试变更功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入还款处理窗体
			switch_to("xpath", '//*[@id="loanrepays-tab-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[2]/td[2]/div/button')
			sleep(1)
			
			span_click("审核")
			ok_click()
			sleep(3)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[2]/td[2]/div/button')
			sleep(1)
			span_click("变更")
			
			switch_to("xpath", '//*[@id="modWin-iframe"]')
			input("xpath", '//*[@id="description"]', '变更')
			sleep(1)
			span_click("保存")
			
			# 退出所有有窗体
			switch_default()
			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("借入方管理->还款处理，变更成功！")
			time.sleep(3)
			
			# 测试作废功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入还款处理窗体
			switch_to("xpath", '//*[@id="loanrepays-tab-iframe"]')
			sleep(1)
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[2]/td[2]/div/button')
			sleep(1)
			
			span_click("审核")
			ok_click()
			sleep(3)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[2]/td[2]/div/button')
			sleep(1)
			span_click("作废")
			ok_click()
			
			# 退出所有有窗体
			switch_default()
			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'成功作废1条记录！')]")
			print("借入方管理->还款处理，作废成功！")
			time.sleep(3)
			
			# 测试生成交易单功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入还款处理窗体
			switch_to("xpath", '//*[@id="loanrepays-tab-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("送审")
			ok_click()
			sleep(3)
			
			double_click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[3]/div')
			sleep(1)
			switch_to("xpath", '//*[@id="wf_taskProcessing_win-iframe"]')
			span_click("同意")
			switch_parent()
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("生成交易单")
			switch_to("xpath", '//*[@id="lendGenRecWin-iframe"]')
			clear("xpath", '//*[@id="combobox-input-dealtype"]')
			sleep(1)
			input_up_click('//*[@id="combobox-input-dealtype"]', '其他')
			span_click("下一步")
			switch_parent()
			switch_to("xpath", '//*[@id="addRecWin-iframe"]')
			
			# 交易类型
			input_up_click('//*[@id="combobox-input-paytypeid"]', '103-对外付款')
			
			# 结算方式
			clear("xpath", '//*[@id="combobox-input-settlementmodeid"]')
			sleep(1)
			input_up_click('//*[@id="combobox-input-settlementmodeid"]', '601-其他支付')
			
			# 付方账户
			click_up_click('//*[@id="combobox-input-ourbankaccountid"]')
			
			# 收方名称
			input("xpath", '//*[@id="combobox-input-oppcounterpartyid"]', '浙江华语科技')
			sleep(1)
			span_click("保存")
			
			# 退出所有有窗体
			switch_default()
			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("借入方管理->还款处理，生成交易单成功！")
			time.sleep(3)
			
			# 点击借入方管理菜单，收回窗体
			click("xpath", "//span[@title='借入方管理']")
			sleep(1)
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("提款登记失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		
		
		# 测试借出方管理->放款处理->放款处理🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱
		try:
			logging.info("开始测试借出方管理->放款处理->放款申请")

			# 切换组织
			refresh()
			sleep(1)
			js_click("xpath", "//input[@id='combobox-input-orgidswitch']")
			sleep(1)
			clear("xpath", "//input[@id='combobox-input-orgidswitch']")
			sleep(1)
			input("xpath", "//input[@id='combobox-input-orgidswitch']", "Mindy科技有限公司")
			sleep(1)
			input_down("xpath", "//in"
			                    "put[@id='combobox-input-orgidswitch']")
			input_enter("xpath", "//input[@id='combobox-input-orgidswitch']")
			sleep(1)
			
			# 去借入方管理
			js_gd("xpath", "//span[contains(text(),'内部借款管理')]")
			# 用JS的方法点击资金结算管理菜单按钮
			js_click("xpath", "//span[contains(text(),'内部借款管理')]")
			sleep(1)
			
			click("xpath", "//span[@title='借入方管理']")
			sleep(1)
			# 点击理财合同登记菜单
			click("xpath", "//span[@title='放款申请']")
			sleep(1)
			# 退出所有的iframe窗体
			switch_default()
			
			#测试新增功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入放款申请窗体
			for i in range(1, 3):
				switch_to("xpath", '//*[@id="lendinglendapply-tab-iframe"]')
				span_click("新增")
				switch_to("xpath", '//*[@id="modWin-iframe"]')
				# 勾选按钮
				click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
				sleep(1)
				span_click("放款申请")
				switch_parent()
				switch_to("xpath", '//*[@id="modWin-iframe"]')
				sleep(1)
				
				# 放款日期
				today = date.today()
				input("xpath", '//*[@id="lenddate-input"]', str(today))
				sleep(1)
				
				# 放款金额
				click("xpath", '//*[@id="amount-input"]')
				sleep(1)
				input("xpath", '//*[@id="amount-input"]', '15')
				sleep(1)
				span_click("保存")
				
				# 退出所有iframe窗体
				switch_default()
				# 用隐式等待方法等页面出现提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				if i ==2 :
					print("借出方管理->放款申请,新增成功")
				time.sleep(3)
			
			# 测试修改功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入放款申请窗体
			switch_to("xpath", '//*[@id="lendinglendapply-tab-iframe"]')
			#刷新、勾选按钮
			click("xpath",'//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath",'//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("修改")
			switch_to("xpath",'//*[@id="modWin-iframe"]')
			input("xpath",'//*[@id="description"]','修改')
			sleep(1)
			span_click("保存")
			
			# 退出所有窗体
			switch_default()
			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("借出方管理->放款申请,修改成功")
			time.sleep(3)
			
			# 测试删除功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入放款申请窗体
			switch_to("xpath", '//*[@id="lendinglendapply-tab-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("删除")
			ok_click()
			
			# 退出所有窗体
			switch_default()
			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'删除成功')]")
			print("借出方管理->放款申请,删除成功")
			time.sleep(3)
			
			# 测试送审功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入放款申请窗体
			switch_to("xpath", '//*[@id="lendinglendapply-tab-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("送审")
			ok_click()
			
			# 退出所有窗体
			switch_default()
			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'送审成功')]")
			print("借出方管理->放款申请,送审成功")
			time.sleep(3)
			
			# 测试撤销送审功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入放款申请窗体
			switch_to("xpath", '//*[@id="lendinglendapply-tab-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("送审",'撤销送审')
			ok_click()
			
			# 退出所有窗体
			switch_default()
			# 用隐式等待方法等页面出现提示框
			print("借出方管理->放款申请,撤销送审成功")
			time.sleep(3)
			
			# 测试提交功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入放款申请窗体
			switch_to("xpath", '//*[@id="lendinglendapply-tab-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("送审")
			ok_click()
			sleep(3)
			double_click("xpath",'//*[@id="grid-body-table"]/tbody/tr[1]/td[3]/div')
			sleep(1)
			switch_to("xpath",'//*[@id="wf_taskProcessing_win-iframe"]')
			span_click("同意")
			sleep(3)
			switch_parent()
			
			double_click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[3]/div')
			sleep(1)
			switch_to("xpath", '//*[@id="wf_taskProcessing_win-iframe"]')
			span_click("同意")
			sleep(3)
			switch_parent()
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("提交")
			
			# 退出所有窗体
			switch_default()
			# 用隐式等待方法等页面出现提示框
			implici_wait("xpath", "//span[contains(text(),'提交成功')]")
			print("借出方管理->放款申请,提交成功")
			time.sleep(3)
			
			# 点击借入方管理菜单，收回窗体
			click("xpath", "//span[@title='借入方管理']")
			sleep(1)
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("申请放款失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		
		
		
		# 测试借入方管理->内部借款合同查看🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱
		try:
			logging.info("开始测试借入方管理->放款处理->放款申请")
			# 点击借出方管理菜单
			click("xpath", "//span[@title='借入方管理']")
			sleep(1)
			# 点击理财合同登记菜单
			click("xpath", "//span[@title='内部借款合同查看']")
			sleep(1)
			# 退出所有的iframe窗体
			switch_default()
			
			switch_to("xpath",'//*[@id="lendingsview-tab-iframe"]')
			double_click("xpath",'//*[@id="grid-body-table"]/tbody/tr[1]/td[3]/div')
			sleep(1)
			switch_to("xpath",'//*[@id="detailWin-iframe"]')
			implici_wait("xpath", '//*[@id="opporgidshow"]')
			sleep(3)
			print("借入方管理->内部借款合同查看，查看成功")
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("申请放款失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		
		
		
		
		
		
		
		
		
		
		print("结束时间：", time.strftime("%Y-%m-%d %H:%M:%S"))


if __name__ == '__main__':
	#  启动单元测试
	unittest.main(verbosity=2)
