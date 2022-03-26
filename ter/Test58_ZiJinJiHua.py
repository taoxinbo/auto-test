# encoding=utf-8
# @Time : 2020/11/19 13:30
# @Author : zzg
# 此文件是测试Mysql版本资金计划
import os
import sys
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
import random

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))
# print("开始时间：",time.strftime("%Y-%m-%d %H:%M:%S"))

driver = ""


class Test58_ZiJinJiHua(unittest.TestCase):
	
	# 启动浏览器
	def setUp(self):
		# 启动浏览器的另外一个方法：通过封装启动浏览器的驱动，启动不同浏览器
		self.driver = get("chrome")
	
	# 登陆系统、对系统设置进行操作
	def test_trade(self):
		
		# login(G_Ora_Url, mindy, Password, "亚唐科技")
		login(G_Mys_Url, mindy, Password, "亚唐科技")
		
		logging.info("开始测试资金计划功能")
		# 将页面的滚动条滑动到‘资金结算管理’页面的地方
		js_gd("xpath", "//span[contains(text(),'资金计划')]")
		# 用JS的方法点击资金结算管理菜单按钮
		js_click("xpath", "//span[contains(text(),'资金计划')]")
		sleep(1)
		# 退出所有iframe窗体
		switch_default()
		
		#测试基础设置--计划项目🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱
		try:
			logger.info("测试基础设置--计划项目")
			switch_default()
			
			#点击基础设置
			click("xpath",'/html/body/div[1]/div[1]/div/div[2]/div/div[2]/div/div/div/div[14]/div/div/ul/li[1]/a/span[2]')
			sleep(1)
			click("xpath", "//span[text()='计划项目']")
			sleep(1)
			switch_default()
			
			# 测试新增功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			for i in range (1,4):
				# 切入计划项目窗体
				switch_to("xpath", '//*[@id="budgetItem-tab-iframe"]')
				
				span_click("新增")
				switch_to("xpath",'//*[@id="addbudgetitemsWin-iframe"]')
				
				#代码
				coad = str(time.strftime("%Y%m%d%H%M%S"))
				input("xpath",'//*[@id="code"]',coad)
				sleep(1)
				
				#名称
				name ="测试计划" +str(time.strftime("%Y%M%S"))
				input("xpath",'//*[@id="name"]',name)
				sleep(1)
				
				#交易方向
				input_up_click('//*[@id="combobox-input-moneyWay"]','支出')
				
				#组织
				input_up_click('//*[@id="combobox-input-orgid"]','亚唐科技')
				
				#填报方式、明细类型
				if i ==1:
					input_up_click('//*[@id="combobox-input-fillreportmode"]', '明细填报')
					input_up_click('//*[@id="combobox-input-budgetdetailtype"]', '经营性支出')
				else :
					input_up_click('//*[@id="combobox-input-fillreportmode"]', '汇总填报')
				#设置单据对象
				click("xpath",'//*[@id="noteobjectsgrid-noteobjectvalues-h"]/div/div[1]/span')
				sleep(1)
				click("xpath",'//*[@id="roleassignformid"]/div/div[4]/div[3]/div[1]')
				sleep(1)
				
				#设置交易类型
				span_click("设置交易类型")
				click("xpath",'//*[@id="paytypegrid-paytypevalues-h"]/div/div[1]/span')
				sleep(1)
				click("xpath",'//*[@id="roleassignformid2"]/div/div[4]/div[3]/div[1]')
				sleep(1)
				
				span_click("保存")
				# 退出所有窗体
				switch_default()
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				if i ==3 :
					print("基础设置--计划项目，新增成功")
				time.sleep(3)
			
			# 测试修改功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入计划项目窗体
			switch_to("xpath", '//*[@id="budgetItem-tab-iframe"]')
			
			#刷新、勾选按钮
			click("xpath",'//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath",'//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("修改")
			switch_to("xpath",'//*[@id="modWin-iframe"]')
			sleep(1)
			
			input("xpath",'//*[@id="description"]','测试修改')
			sleep(1)
			
			span_click("保存")
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("基础设置--计划项目，修改成功")
			time.sleep(3)
			
			# 测试删除功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入计划项目窗体
			switch_to("xpath", '//*[@id="budgetItem-tab-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("删除")
			ok_click()
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("基础设置--计划项目，删除成功")
			time.sleep(3)
			
			# 测试失效功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入计划项目窗体
			switch_to("xpath", '//*[@id="budgetItem-tab-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("失效")
			
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'失效成功！')]")
			print("基础设置--计划项目，失效成功")
			time.sleep(3)
			
			# 测试生效功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入计划项目窗体
			switch_to("xpath", '//*[@id="budgetItem-tab-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("生效")
			
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'生效成功！')]")
			print("基础设置--计划项目，生效成功")
			time.sleep(3)
			
			# 测试设置适用范围功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入计划项目窗体
			switch_to("xpath", '//*[@id="budgetItem-tab-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("设置适用范围")
			switch_to("xpath",'//*[@id="setAppscopeWin-iframe"]')
			switch_to("xpath",'//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			click("xpath",'//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			span_click("分配")
		
			switch_to("xpath",'//*[@id="distributeWin-iframe"]')
			span_click("保存")
			
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("基础设置--计划项目，设置适用范围成功")
			click("xpath", "//span[text()='计划项目']")
			switch_default()
			time.sleep(3)
			
			# 测试查看/设置组织范围功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入计划项目窗体
			switch_to("xpath", '//*[@id="budgetItem-tab-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("查看/设置组织范围")
			switch_to("xpath", '//*[@id="setExcludeOrgWin-iframe"]')
			sleep(1)
			span_click("适用组织查看")
			
			switch_to("xpath",'//*[@id="subTabTwo-iframe"]')
			implici_wait("xpath", "//div[contains(text(),'亚唐科技')]")
			print("基础设置--计划项目，查看/设置组织范围查看成功")
			switch_default()
			click("xpath", "//span[text()='计划项目']")
			switch_default()
			time.sleep(3)
			
			# 测试添加同级项目功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入计划项目窗体
			switch_to("xpath", '//*[@id="budgetItem-tab-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("添加同级项目")
			switch_to("xpath",'//*[@id="addbudgetitemsWin-iframe"]')
			# 代码
			coad = str(time.strftime("%Y%m%d%H%M%S"))
			input("xpath", '//*[@id="code"]', coad)
			sleep(1)
			
			# 名称
			name = "测试计划" + str(time.strftime("%Y%M%S"))
			input("xpath", '//*[@id="name"]', name)
			sleep(1)
			
			# 交易方向
			input_up_click('//*[@id="combobox-input-moneyWay"]', '支出')
			
			# 组织
			input_up_click('//*[@id="combobox-input-orgid"]', '亚唐科技')
			
			# 填报方式、明细类型
			input_up_click('//*[@id="combobox-input-fillreportmode"]', '汇总填报')
			
			# 设置单据对象
			click("xpath", '//*[@id="noteobjectsgrid-noteobjectvalues-h"]/div/div[1]/span')
			sleep(1)
			click("xpath", '//*[@id="roleassignformid"]/div/div[4]/div[3]/div[1]')
			sleep(1)
			
			# 设置交易类型
			span_click("设置交易类型")
			click("xpath", '//*[@id="paytypegrid-paytypevalues-h"]/div/div[1]/span')
			sleep(1)
			click("xpath", '//*[@id="roleassignformid2"]/div/div[4]/div[3]/div[1]')
			sleep(1)
			
			span_click("保存")
			
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("基础设置--计划项目，添加同级项目成功")
			time.sleep(3)
			
			# 测试添加下级项目功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入计划项目窗体
			switch_to("xpath", '//*[@id="budgetItem-tab-iframe"]')
			
			#查询数据
			click("xpath",'//*[@id="north"]/div[2]/span')
			sleep(1)
			span_click("高级查询")
			input_up_click('//*[@id="combobox-input-value_7"]','汇总填报')
			click("xpath",'//*[@id="advQueryWin-btn-1"]/div[2]')
			sleep(1)
			click("xpath",'//*[@id="f-win-title-advQueryWin"]/div[1]/div')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("添加下级项目")
			switch_to("xpath", '//*[@id="addlowbudgetitemsWin-iframe"]')
			# 代码
			coad = str(time.strftime("%Y%m%d%H%M%S"))
			input("xpath", '//*[@id="code"]', coad)
			sleep(1)
			
			# 名称
			name = "测试计划" + str(time.strftime("%Y%M%S"))
			input("xpath", '//*[@id="name"]', name)
			sleep(1)
		
			
			# 组织
			input_up_click('//*[@id="combobox-input-orgid"]', '亚唐科技')
			
			# 填报方式、明细类型
			input_up_click('//*[@id="combobox-input-fillreportmode"]', '明细填报')
			input_up_click('//*[@id="combobox-input-budgetdetailtype"]', '经营性支出')
			# 设置单据对象
			click("xpath", '//*[@id="noteobjectsgrid-noteobjectvalues-h"]/div/div[1]/span')
			sleep(1)
			click("xpath", '//*[@id="roleassignformid"]/div/div[4]/div[3]/div[1]')
			sleep(1)
			
			# 设置交易类型
			span_click("设置交易类型")
			click("xpath", '//*[@id="paytypegrid-paytypevalues-h"]/div/div[1]/span')
			sleep(1)
			click("xpath", '//*[@id="roleassignformid2"]/div/div[4]/div[3]/div[1]')
			sleep(1)
			
			span_click("保存")
			
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("基础设置--计划项目，添加下级级项目成功")
			time.sleep(3)
			
			#点击基础设置，回到初始页面
			# 点击基础设置
			click("xpath",'/html/body/div[1]/div[1]/div/div[2]/div/div[2]/div/div/div/div[14]/div/div/ul/li[1]/a/span[2]')
			sleep(1)

		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("计划项目失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)

			# def tearDown(self):
			#     self.driver.quit()
			print("结束时间：", time.strftime("%Y-%m-%d %H:%M:%S"))
		
		
		# 测试基础设置--计划方案🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱
		try:
			logger.info("测试基础设置--计划方案")
			switch_default()
			
			# 点击基础设置
			click("xpath",
			      '/html/body/div[1]/div[1]/div/div[2]/div/div[2]/div/div/div/div[14]/div/div/ul/li[1]/a/span[2]')
			sleep(1)
			click("xpath", "//span[text()='计划方案']")
			sleep(1)
			switch_default()
			
			# 测试新增功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			for i in range(1, 4):
				# 切入计划项目窗体
				switch_to("xpath", '//*[@id="budgetScheme-tab-iframe"]')
				
				span_click("新增")
				switch_to("xpath", '//*[@id="addWin-iframe"]')
				
				# 名称
				name = "计划方案"+str(time.strftime("%Y%m%d%H%M%S"))
				input("xpath", '//*[@id="name"]', name)
				sleep(1)
				
				#计划期间跨度
				input_up_click('//*[@id="combobox-input-budgetperiodtype"]','月')
				
				#计划精度
				input_up_click('//*[@id="combobox-input-budgetaccuracygrade"]','月')
				
				#编制周期
				input("xpath",'//*[@id="editperiod-input"]',"1")
				sleep(1)
				
				#组织
				input_up_click('//*[@id="combobox-input-orgid"]','亚唐科技')
				
				#开始编制月
				input_up_click('//*[@id="combobox-input-editstartmonth"]','三月')
				span_click("保存")
				# 退出所有窗体
				switch_default()
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				if i == 2:
					print("基础设置--计划方案，新增成功")
				time.sleep(3)
			
			# 测试复制功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入计划项目窗体
			switch_to("xpath", '//*[@id="budgetScheme-tab-iframe"]')
			
			#刷新、勾选按钮
			click("xpath",'//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath",'//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("复制")
			switch_to("xpath",'//*[@id="copyWin-iframe"]')
			
			#计划方案名称
			name = "计划方案" + str(time.strftime("%Y%m%d%H%M%S"))
			input("xpath",'//*[@id="newname"]',name)
			sleep(1)
			
			#关联复制处理
			click("xpath",'//*[@id="combobox-input-copyparam"]')
			sleep(1)
			click("xpath",'//*[@id="copyparam-combogrid-body-table"]/tbody/tr[1]/td[2]/div')
			sleep(1)
			
			span_click("保存")
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("基础设置--计划项目，复制成功")
			time.sleep(3)
			
			# 测试删除功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入计划项目窗体
			switch_to("xpath", '//*[@id="budgetScheme-tab-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("删除")
			ok_click()
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("基础设置--计划项目，删除成功")
			time.sleep(3)
			
			# 测试修改功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入计划项目窗体
			switch_to("xpath", '//*[@id="budgetScheme-tab-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("修改")
			switch_to("xpath",'//*[@id="modWin-iframe"]')
			span_click("保存")
			
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("基础设置--计划项目，修改成功")
			time.sleep(3)
			
			#滚动、和执行，等下做完数据再来操作
			
			# 点击基础设置，回到初始页面
			# 点击基础设置
			click("xpath",
			      '/html/body/div[1]/div[1]/div/div[2]/div/div[2]/div/div/div/div[14]/div/div/ul/li[1]/a/span[2]')
			sleep(1)
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("计划方案失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
			
			# def tearDown(self):
			#     self.driver.quit()
			print("结束时间：", time.strftime("%Y-%m-%d %H:%M:%S"))
		
		
		# 测试基础设置--计划控制🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱
		try:
			logger.info("测试基础设置--计划控制")
			switch_default()
			
			# 点击基础设置
			click("xpath",
			      '/html/body/div[1]/div[1]/div/div[2]/div/div[2]/div/div/div/div[14]/div/div/ul/li[1]/a/span[2]')
			sleep(1)
			click("xpath", "//span[text()='计划控制']")
			sleep(1)
			switch_default()
			
			# 测试新增功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			for i in range(1, 3):
				# 切入计划项目窗体
				switch_to("xpath", '//*[@id="budgetControl-tab-iframe"]')
				
				span_click("新增")
				switch_to("xpath", '//*[@id="addWin-iframe"]')
				
				#组织
				input_up_click('//*[@id="combobox-input-orgid"]','亚唐科技')
				
				# 计划方案
				click_up_click('//*[@id="combobox-input-schemeid"]')
				
				# 单据对象
				input("xpath",'//*[@id="combobox-input-noteobjectid"]','ZJFK')
				click("xpath",'//*[@id="noteobjectid-combogrid-body-table"]/tbody/tr[2]/td[2]/div')
				sleep(1)
				
				#组织控制类型
				input_up_click('//*[@id="combobox-input-controlorgtype"]','本组织和下级组织')
				
				#控制方式
				input_up_click('//*[@id="combobox-input-budgetcontrolmode"]','提示')
				
				#控制类别
				input_up_click('//*[@id="combobox-input-budgetcontrolcategory"]','单向控制')
				
				#计划项目
				click("xpath",'//*[@id="combobox-input-budgetitemsrange"]')
				sleep(1)
				click("xpath",'//*[@id="budgetitemsrange-combogrid-body-table"]/tbody/tr[1]/td[2]/div/button')
				sleep(1)
				
				#计划项目控制类型
				input_up_click('//*[@id="combobox-input-controlbudgetitemtype"]', '计划金额分项控制')
				
				
				span_click("保存")
				# 退出所有窗体
				switch_default()
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				if i == 2:
					print("基础设置--计划方案，新增成功")
				time.sleep(3)
			
			# 测试修改功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入计划项目窗体
			switch_to("xpath", '//*[@id="budgetControl-tab-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("修改")
			switch_to("xpath",'//*[@id="modWin-iframe"]')
			sleep(1)
			input("xpath",'//*[@id="description"]','测试修改')
			sleep(1)
			span_click("保存")
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("基础设置--计划控制，修改成功")
			time.sleep(3)
			
			# 测试删除功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入计划项目窗体
			switch_to("xpath", '//*[@id="budgetControl-tab-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("删除")
			ok_click()
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("基础设置--计划控制，删除成功")
			time.sleep(3)
			
			# 点击基础设置，回到初始页面
			# 点击基础设置
			click("xpath",
			      '/html/body/div[1]/div[1]/div/div[2]/div/div[2]/div/div/div/div[14]/div/div/ul/li[1]/a/span[2]')
			sleep(1)
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("计划控制失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
			
			# def tearDown(self):
			#     self.driver.quit()
			print("结束时间：", time.strftime("%Y-%m-%d %H:%M:%S"))
		
		
		# 测试基础设置--计划数据源配置🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱
		try:
			logger.info("测试基础设置--计划数据源配置")
			switch_default()
			
			# 点击基础设置
			click("xpath",
			      '/html/body/div[1]/div[1]/div/div[2]/div/div[2]/div/div/div/div[14]/div/div/ul/li[1]/a/span[2]')
			sleep(1)
			click("xpath", "//span[text()='计划数据源配置']")
			sleep(1)
			switch_default()
			
			# 测试新增功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			for i in range(1, 3):
				# 切入计划项目窗体
				switch_to("xpath", '//*[@id="budgetItemDataSource-tab-iframe"]')
				
				span_click("新增")
				switch_to("xpath",'//*[@id="addWin-iframe"]')
				
				#目标计划方案
			
				click_up_click('//*[@id="combobox-input-targetschemeid"]')
				
				#目标计划项目
				if i ==1 :
					click_up_click('//*[@id="combobox-input-budgetitemid"]')
				if i ==2 :
					click("xpath",'//*[@id="combobox-input-budgetitemid"]')
					sleep(1)
					click("xpath",'//*[@id="budgetitemid-combogrid-body-table"]/tbody/tr[2]/td[2]/div')
					sleep(1)
					
				#目标数据源函数
				click("xpath",'//*[@id="combobox-input-sourcefuncs"]')
				sleep(1)
				click("xpath",'//*[@id="f-combo-sourcefuncs-list-4"]/div[1]')
				sleep(1)
				
				#数据引入方式
				input_up_click('//*[@id="combobox-input-importtype"]','参考引入')
				
				span_click("保存")
				# 退出所有窗体
				switch_default()
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				if i == 2:
					print("基础设置--计划数据源配置，新增成功")
				time.sleep(3)
			
			# 测试修改功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入计划项目窗体
			switch_to("xpath", '//*[@id="budgetItemDataSource-tab-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("修改")
			switch_to("xpath",'//*[@id="modWin-iframe"]')
			sleep(1)
			
			span_click("保存")
			
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("基础设置--计划数据源配置，修改成功")
			time.sleep(3)
			
			# 测试失效功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入计划项目窗体
			switch_to("xpath", '//*[@id="budgetItemDataSource-tab-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("失效")
			ok_click()
			
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'成功失效1条记录！')]")
			print("基础设置--计划数据源配置，失效成功")
			time.sleep(3)
			
			# 测试生效功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入计划项目窗体
			switch_to("xpath", '//*[@id="budgetItemDataSource-tab-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("生效")
			ok_click()
			
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'成功生效1条记录！')]")
			print("基础设置--计划数据源配置，生效成功")
			time.sleep(3)
			
			# 测试删除功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 切入计划项目窗体
			switch_to("xpath", '//*[@id="budgetItemDataSource-tab-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("删除")
			ok_click()
			
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("基础设置--计划数据源配置，删除成功")
			time.sleep(3)
			
			
			# 点击基础设置，回到初始页面
			# 点击基础设置
			click("xpath",
			      '/html/body/div[1]/div[1]/div/div[2]/div/div[2]/div/div/div/div[14]/div/div/ul/li[1]/a/span[2]')
			sleep(1)
			
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("计划控制失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
			
			# def tearDown(self):
			#     self.driver.quit()
			print("结束时间：", time.strftime("%Y-%m-%d %H:%M:%S"))
		
		# 测试基础设置--计划明细数据源配置🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱
		try:
			logger.info("测试基础设置--计划明细数据源配置")
			switch_default()
			
			# 点击基础设置
			click("xpath",
			      '/html/body/div[1]/div[1]/div/div[2]/div/div[2]/div/div/div/div[14]/div/div/ul/li[1]/a/span[2]')
			sleep(1)
			click("xpath", "//span[text()='计划明细数据源配置']")
			sleep(1)
			switch_default()
			
			# 测试新增功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath",'//*[@id="budgetDetailDataSource-tab-iframe"]')
			span_click("新增")
			
			switch_to("xpath",'//*[@id="addWin-iframe"]')
			
			#编码
			coad=str(time.strftime("%Y%m%d%H%M%S"))
			input("xpath",'//*[@id="code"]',coad)
			sleep(1)
			
			#名称
			name = "ZZG" +str(time.strftime("%Y%M%S"))
			input("xpath",'//*[@id="name"]',name)
			sleep(1)
			
			#目标计划项目
			click_up_click('//*[@id="combobox-input-budgetitemid"]')
			
			#数据来源分类
			click_up_click('//*[@id="combobox-input-datasource"]')
			
			#数据来源子分类
			click_up_click('//*[@id="combobox-input-subdatasource"]')
			
			#计划精度
			input_up_click('//*[@id="combobox-input-budgetaccuracygrade"]','月')
			
			#计划参数控制类型
			click_up_click('//*[@id="combobox-input-importtype"]')
			
			span_click("保存")
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("基础设置--计划明细数据源配置，新增成功")
			time.sleep(3)
			
			# 查询数据💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="budgetDetailDataSource-tab-iframe"]')
			click("xpath",'//*[@id="north"]/div[2]/span')
			sleep(1)
			input("xpath",'//*[@id="name"]','ZZG')
			sleep(1)
			span_click("查询")
			switch_default()
			
			
			# 测试修改功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="budgetDetailDataSource-tab-iframe"]')
			
			#刷新、勾选按钮
			click("xpath",'//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath",'//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
			sleep(1)
			
			span_click("修改")
			switch_to("xpath",'//*[@id="modWin-iframe"]')
			
			span_click("保存")
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("基础设置--计划明细数据源配置，修改成功")
			time.sleep(3)
			
			# 测试失效功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="budgetDetailDataSource-tab-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
			sleep(1)
			
			span_click("失效")
			ok_click()
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'成功失效1条记录！')]")
			print("基础设置--计划明细数据源配置，失效成功")
			time.sleep(3)
			
			# 测试生效功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="budgetDetailDataSource-tab-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
			sleep(1)
			
			span_click("生效")
			ok_click()
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'成功生效1条记录！')]")
			print("基础设置--计划明细数据源配置，失效成功")
			time.sleep(3)
			
			# 测试删除功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="budgetDetailDataSource-tab-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
			sleep(1)
			
			span_click("删除")
			ok_click()
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("基础设置--计划明细数据源配置，删除成功")
			time.sleep(3)
			
			# 点击基础设置，回到初始页面
			# 点击基础设置
			click("xpath",
			      '/html/body/div[1]/div[1]/div/div[2]/div/div[2]/div/div/div/div[14]/div/div/ul/li[1]/a/span[2]')
			sleep(1)
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("计划控制失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
			
			# def tearDown(self):
			#     self.driver.quit()
			print("结束时间：", time.strftime("%Y-%m-%d %H:%M:%S"))
		
		
		# 测试资金计划--计划编制处理🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱
		try:
			logger.info("测试资金计划--计划编制处理")
			switch_default()
			
			# 点击计划编制处理
			js_click("xpath", "//span[contains(text(),'计划编制处理')]")
			sleep(1)
			
			# 测试新增💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			for i in range (1,5):
				switch_to("xpath", '//*[@id="budgetMaking-tab-iframe"]')
				span_click("新增")
				switch_to("xpath", '//*[@id="addWin-iframe"]')
				
				# 计划方案
				click("xpath", '//*[@id="combobox-input-schemeid"]')
				sleep(1)
				if i ==1 or i ==4 :
					click("xpath", '//*[@id="schemeid-combogrid-body-table"]/tbody/tr[1]/td[2]/div')
				if i ==2 or i ==3 :
					click("xpath", '//*[@id="schemeid-combogrid-body-table"]/tbody/tr[2]/td[2]/div')
				sleep(1)
				
				# 计划项目
				if i ==1 or i ==4 :
					click("xpath",'//*[@id="t1_t0_t0-fixed"]/td[2]/div/button')
				if i ==2 or i ==3 :
					click("xpath",'//*[@id="t1_t1-fixed"]/td[2]/div/button')
				sleep(1)
				
				span_click("下一步")
				switch_parent()
				switch_to("xpath", '//*[@id="makingWin-iframe"]')
				
				double_click("xpath", '//*[@id="editgrid-data0-0-input"]')
				sleep(1)
				momey = str(random.randint(1, 300))
				input("xpath", '//*[@id="editgrid-data0-0-input"]', momey)
				sleep(1)
				
				span_click("保存")
				switch_default()
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				if i == 4:
					print("资金计划-计划编制处理，新增成功")
				time.sleep(3)
				if i == 1 :
					switch_to("xpath", '//*[@id="budgetMaking-tab-iframe"]')
					click("xpath",'//*[@id="t1_t0-fixed"]/td[2]/div/button')
					sleep(1)
					span_click("删除")
					ok_click()
					# 退出所有窗体
					switch_default()
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("资金计划-计划编制处理，删除成功")
					time.sleep(3)
				if i == 2 :
					switch_to("xpath", '//*[@id="budgetMaking-tab-iframe"]')
					click("xpath",'//*[@id="t1_t0-fixed"]/td[2]/div/button')
					sleep(1)
					span_click("作废")
					ok_click()
					# 退出所有窗体
					switch_default()
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("资金计划-计划编制处理，作废成功")
					time.sleep(3)
					
			# 测试刷新引入数据💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="budgetMaking-tab-iframe"]')
			
			#刷新、勾选数据
			click("xpath",'//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath",'//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("刷新引入数据")
			ok_click()
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("资金计划-计划编制处理，刷新引入数据成功")
			time.sleep(3)
			
			# 测试送审💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="budgetMaking-tab-iframe"]')
			
			# 刷新、勾选数据
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("送审")
			ok_click()
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'送审成功！')]")
			print("资金计划-计划编制处理，送审成功")
			time.sleep(3)
			
			# 测试撤销送审💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="budgetMaking-tab-iframe"]')
			
			# 刷新、勾选数据
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("送审",'撤销送审')
			ok_click()
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'撤销送审成功！')]")
			print("资金计划-计划编制处理，撤销送审成功")
			time.sleep(3)
			
			# 测试审核💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="budgetMaking-tab-iframe"]')
			
			# 刷新、勾选数据
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t1-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("审核")
			ok_click()
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("资金计划-计划编制处理，审核成功")
			time.sleep(3)
			
			# 测试取消审核💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="budgetMaking-tab-iframe"]')
			
			# 刷新、勾选数据
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t1-fixed"]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("审核",'取消审核')
			ok_click()
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'成功撤销送审1条记录！')]")
			print("资金计划-计划编制处理，取消审核成功")
			time.sleep(3)
			
			# 测试审核💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="budgetMaking-tab-iframe"]')
			
			# 刷新、勾选数据
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t1-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("审核")
			ok_click()
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
		
			time.sleep(3)
		
			# 测试附件信息💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="budgetMaking-tab-iframe"]')
			
			# 刷新、勾选数据
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t1-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("附件信息")
			switch_to("xpath",'//*[@id="makingWin-iframe"]')
			
			upload_click("xpath", "//div[text()='上传文件']/parent::*[1]/descendant::*[4]",
			             'D:\FlieDownload', '"directsinglediffbankpay.xls"')
			
			span_click("保存")
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'成功')]")
			print("资金计划-计划编制处理，附件信息上传成功")
			time.sleep(3)
			
			# 测试审批历史💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="budgetMaking-tab-iframe"]')
			
			# 刷新、勾选数据
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("送审")
			ok_click()
			sleep(3)
			
			double_click("xpath",'//*[@id="t1_t0"]/td[1]/div/span')
			sleep(1)
			switch_to("xpath",'//*[@id="wf_taskProcessing_win-iframe"]')
			sleep(1)
			span_click("同意")
			
			switch_parent()
			# 刷新、勾选数据
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("审批历史")
			switch_to("xpath",'//*[@id="flowwin-iframe"]')
			sleep(3)
			span_click("流程流转")
		
			switch_default()
			implici_wait("xpath", "//div[contains(text(),'开始')]")
			print("资金计划-计划编制处理，审批历史查看")
			time.sleep(3)
			
			# 点击计划编制处理
			js_click("xpath", "//span[contains(text(),'计划编制处理')]")
			sleep(1)
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("计划编制处理失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
			
			# def tearDown(self):
			#     self.driver.quit()
			print("结束时间：", time.strftime("%Y-%m-%d %H:%M:%S"))
		
		
		# 测试基础设置--计划数据查看🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱
		try:
			logger.info("测试基础设置--计划数据查看")
			switch_default()
			
			click("xpath", "//span[text()='计划数据查看']")
			sleep(1)
			switch_default()
			
			# 测试查看功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="budgetView-tab-iframe"]')
			
			click("xpath",'//*[@id="north"]/div[2]/span')
			sleep(1)
			click_up_click('//*[@id="combobox-input-schemeid"]')
			
			span_click("查询")
			
			implici_wait("xpath", "//div[contains(text(),'期初余额')]")
			print("资金计划--计划数据查看，查看成功")
			time.sleep(3)
			switch_default()
			click("xpath", "//span[text()='计划数据查看']")
			sleep(1)
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("计划数据查看失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
			
			# def tearDown(self):
			#     self.driver.quit()
			print("结束时间：", time.strftime("%Y-%m-%d %H:%M:%S"))
		
		
		# 测试基础设置--计划方案（执行、滚动功能）🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱
		try:
			logger.info("测试基础设置--计划数据查看")
			switch_default()
			
			# 点击基础设置
			click("xpath",'/html/body/div[1]/div[1]/div/div[2]/div/div[2]/div/div/div/div[14]/div/div/ul/li[1]/a/span[2]')
			sleep(1)
			click("xpath", "//span[text()='计划方案']")
			sleep(1)
			switch_default()
		
			
			# 测试执行功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			for i in range (1,3):
				switch_to("xpath", '//*[@id="budgetScheme-tab-iframe"]')
				
				# 刷新、勾选按钮
				click("xpath", '//*[@id="gridbar-page-refresh"]')
				sleep(1)
				if i ==1 :
					click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
				if i ==2 :
					click("xpath", '//*[@id="grid-body-table"]/tbody/tr[2]/td[2]/div/button')
				sleep(1)
				
				span_click("执行")
				ok_click()
				# 退出所有窗体
				switch_default()
				implici_wait("xpath", "//span[contains(text(),'操作成功')]")
				if i==2 :
					print("资金计划--计划方案，执行成功")
				time.sleep(3)
			
			# 测试滚动功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="budgetScheme-tab-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("滚动")
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功')]")
			print("资金计划--计划方案，滚动成功")
			time.sleep(3)
			
			#回到初始界面
			# 点击基础设置
			click("xpath",
			      '/html/body/div[1]/div[1]/div/div[2]/div/div[2]/div/div/div/div[14]/div/div/ul/li[1]/a/span[2]')
			sleep(1)
			switch_default()
			
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("计划数据查看失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
			
			# def tearDown(self):
			#     self.driver.quit()
			print("结束时间：", time.strftime("%Y-%m-%d %H:%M:%S"))
		
		
		# 测试资金计划--计划调整处理🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱
		try:
			logger.info("测试资金计划--计划调整处理")
			switch_default()
			
			click("xpath", "//span[text()='计划调整处理']")
			sleep(1)
			switch_default()
			
			# 测试新增功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			for i in range (1,5):
				switch_to("xpath",'//*[@id="budgetAdjust-tab-iframe"]')
				span_click("新增")
				switch_to("xpath",'//*[@id="addWin-iframe"]')
				if  i ==1 or i ==3:
					#计划方案
					click("xpath",'//*[@id="combobox-input-schemeid"]')
					sleep(1)
					click("xpath",'//*[@id="schemeid-combogrid-body-table"]/tbody/tr[1]/td[2]/div')
					sleep(1)
				if  i ==2 or i ==4:
					#计划方案
					click("xpath",'//*[@id="combobox-input-schemeid"]')
					sleep(1)
					click("xpath",'//*[@id="schemeid-combogrid-body-table"]/tbody/tr[2]/td[2]/div')
					sleep(1)
				#计划编制单
				click_up_click('//*[@id="combobox-input-budgetid"]')
				
				span_click("下一步")
				switch_parent()
				switch_to("xpath",'//*[@id="adjustWin-iframe"]')
				span_click("保存")
				
				# 退出所有窗体
				switch_default()
				implici_wait("xpath", "//span[contains(text(),'操作成功')]")
				if i == 4:
					print("资金计划--计划调整处理，新增成功")
				time.sleep(3)
				
				if i==1 :
					switch_to("xpath", '//*[@id="budgetAdjust-tab-iframe"]')
					#刷新、勾选按钮
					click("xpath",'//*[@id="t1_t0-fixed"]/td[2]/div/button')
					sleep(1)
					span_click("删除")
					ok_click()
					
					# 退出所有窗体
					switch_default()
					implici_wait("xpath", "//span[contains(text(),'操作成功')]")
					print("资金计划--计划调整处理，删除成功")
					time.sleep(3)
				if i == 2:
					switch_to("xpath", '//*[@id="budgetAdjust-tab-iframe"]')
					# 刷新、勾选按钮
					click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
					sleep(1)
					span_click("作废")
					ok_click()
					
					# 退出所有窗体
					switch_default()
					implici_wait("xpath", "//span[contains(text(),'操作成功')]")
					print("资金计划--计划调整处理，作废成功")
					time.sleep(3)
			
			# 测试修改功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="budgetAdjust-tab-iframe"]')
			#刷新、勾选按钮
			click("xpath",'//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath",'//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("修改")
			switch_to("xpath",'//*[@id="adjustWin-iframe"]')
			
			input("xpath",'//*[@id="editgrid-description0-0"]','测试修改')
			sleep(1)
			span_click("保存")
			
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功')]")
			print("资金计划--计划调整处理，修改成功")
			time.sleep(3)
			
			# 测试送审功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="budgetAdjust-tab-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("送审")
			ok_click()
			
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'送审成功！')]")
			print("资金计划--计划调整处理，送审成功")
			time.sleep(3)
			
			# 测试撤销送审功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="budgetAdjust-tab-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("送审",'撤销送审')
			ok_click()
			
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'撤销送审成功！')]")
			print("资金计划--计划调整处理，撤销送审成功")
			time.sleep(3)
			
			# 测试审核功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="budgetAdjust-tab-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t1-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("审核")
			ok_click()
			
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'成功')]")
			print("资金计划--计划调整处理，审核成功")
			time.sleep(3)
			
			# 测试审批历史功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="budgetAdjust-tab-iframe"]')
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("送审")
			ok_click()
			sleep(3)
			
			
			double_click("xpath",'//*[@id="t1_t0"]/td[1]/div/span')
			sleep(1)
			switch_to("xpath",'//*[@id="wf_taskProcessing_win-iframe"]')
			sleep(1)
			
			span_click("同意")
			switch_parent()
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("审批历史")
			switch_to("xpath",'//*[@id="flowwin-iframe"]')
			sleep(3)
			span_click("流程流转")
			implici_wait("xpath", "//span[contains(text(),'开始')]")
			print("资金计划--计划调整处理，审批历史查看成功")
			time.sleep(3)
			
			switch_default()
			click("xpath", "//span[text()='计划调整处理']")
			sleep(1)
			
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("计划调整处理失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
			
			# def tearDown(self):
			#     self.driver.quit()
			print("结束时间：", time.strftime("%Y-%m-%d %H:%M:%S"))
		
		
		# 测试资金计划--计划编制查看🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱
		try:
			logger.info("测试资金计划--计划编制查看")
			switch_default()
			
			click("xpath", "//span[text()='计划编制查看']")
			sleep(1)
			switch_default()
			
			# 测试查看功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath",'//*[@id="budgetMakingView-tab-iframe"]')
			double_click("xpath",'//*[@id="t1_t0"]/td[2]/div/span')
			
			switch_to("xpath",'//*[@id="flowwin-iframe"]')
			switch_to("xpath",'//*[@id="subTabOne-iframe"]')
			implici_wait("xpath", "//span[contains(text(),'组织')]")
			print("资金计划--计划编制查看，查看成功")
			time.sleep(3)
			switch_default()
			click("xpath", "//span[text()='计划编制查看']")
			sleep(1)
			
			# 测试附件信息查看💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath",'//*[@id="budgetMakingView-tab-iframe"]')
			
			#刷新、勾选按钮
			click("xpath",'//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath",'//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("附件信息")
			switch_to("xpath",'//*[@id="makingWin-iframe"]')
			
			implici_wait("xpath", "//span[contains(text(),'附件信息')]")
			print("资金计划--计划编制查看，附件信息查看成功")
			time.sleep(3)
			
			switch_default()
			click("xpath", "//span[text()='计划编制查看']")
			sleep(1)
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("计划调整处理失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
			
			# def tearDown(self):
			#     self.driver.quit()
			print("结束时间：", time.strftime("%Y-%m-%d %H:%M:%S"))
		
		
		# 测试资金计划--计划明细填报--经营性🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱
		try:
			logger.info("测试资金计划--计划明细填报--经营性")
			switch_default()
			
			click("xpath", "//span[text()='计划明细填报']")
			sleep(1)
			switch_default()
			
			# 做数据💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 点击基础设置
			click("xpath",
			      '/html/body/div[1]/div[1]/div/div[2]/div/div[2]/div/div/div/div[14]/div/div/ul/li[1]/a/span[2]')
			sleep(1)
			click("xpath", "//span[text()='计划项目']")
			sleep(1)
			switch_default()
			
			#三种计划
			for i in range(1, 4):
				# 切入计划项目窗体
				switch_to("xpath", '//*[@id="budgetItem-tab-iframe"]')
				
				span_click("新增")
				switch_to("xpath", '//*[@id="addbudgetitemsWin-iframe"]')
				
				# 代码
				coad = str(time.strftime("%Y%m%d%H%M%S"))
				input("xpath", '//*[@id="code"]', coad)
				sleep(1)
				
				# 名称
				name = "测试计划" + str(time.strftime("%Y%M%S"))
				input("xpath", '//*[@id="name"]', name)
				sleep(1)
				
				# 交易方向
				input_up_click('//*[@id="combobox-input-moneyWay"]', '支出')
				
				# 组织
				input_up_click('//*[@id="combobox-input-orgid"]', '亚唐科技')
				
				# 填报方式、明细类型
				input_up_click('//*[@id="combobox-input-fillreportmode"]', '明细填报')
				if i==1 :
					input_up_click('//*[@id="combobox-input-budgetdetailtype"]', '经营性支出')
				if i==2 :
					input_up_click('//*[@id="combobox-input-budgetdetailtype"]', '融资性支出')
				if i==3 :
					input_up_click('//*[@id="combobox-input-budgetdetailtype"]', '投资性支出')
			
				# 设置单据对象
				click("xpath", '//*[@id="noteobjectsgrid-noteobjectvalues-h"]/div/div[1]/span')
				sleep(1)
				click("xpath", '//*[@id="roleassignformid"]/div/div[4]/div[3]/div[1]')
				sleep(1)
				
				# 设置交易类型
				span_click("设置交易类型")
				click("xpath", '//*[@id="paytypegrid-paytypevalues-h"]/div/div[1]/span')
				sleep(1)
				click("xpath", '//*[@id="roleassignformid2"]/div/div[4]/div[3]/div[1]')
				sleep(1)
				
				span_click("保存")
				# 退出所有窗体
				switch_default()
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				time.sleep(3)
			#回到初始界面
			click("xpath",
			      '/html/body/div[1]/div[1]/div/div[2]/div/div[2]/div/div/div/div[14]/div/div/ul/li[1]/a/span[2]')
			sleep(1)
			click("xpath", "//span[text()='计划明细填报']")
			sleep(1)
			switch_default()
			
			# 测试新增功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			for i in range (1,4):
				switch_to("xpath",'//*[@id="budgetDetailEnter-tab-iframe"]')
				switch_to("xpath",'//*[@id="subTabOne-iframe"]')
				sleep(1)
				
				span_click("新增")
				switch_to("xpath",'//*[@id="addWin-iframe"]')
				
				#计划项目
				click_up_click('//*[@id="combobox-input-budgetitemid"]')
				
				#计划值
				money = random.randint(1,300)
				double_click("xpath",'//*[@id="budgetamount-input"]')
				sleep(1)
				input("xpath",'//*[@id="budgetamount-input"]',str(money))
				sleep(1)
				
				#票据结算值
				double_click("xpath",'//*[@id="billbudgetamount-input"]')
				sleep(1)
				input("xpath",'//*[@id="billbudgetamount-input"]',str(money))
				sleep(1)
				
				#合同结算金额
				double_click("xpath",'//*[@id="contractamount-input"]')
				sleep(1)
				input("xpath",'//*[@id="contractamount-input"]','50000')
				sleep(1)
				
				
				#计划精度
				input_up_click('//*[@id="combobox-input-budgetaccuracygrade"]','年')
				
				span_click("保存")
				#退出所有窗体
				switch_default()
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				if i == 3   :
					print("资金计划--计划明细填报--经营性，新增成功")
				time.sleep(3)
			
			#查询数据💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="budgetDetailEnter-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			click("xpath",'//*[@id="north"]/div[2]/span')
			sleep(1)
			input_up_click('//*[@id="combobox-input-cancelstate"]','未作废')
			span_click("查询")
			switch_default()
			
			# 测试修改功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="budgetDetailEnter-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			#刷新、勾选按钮
			click("xpath",'//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath",'//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("修改")
			switch_to("xpath",'//*[@id="addWin-iframe"]')
			
			input("xpath",'//*[@id="description"]','测试修改')
			sleep(1)
			
			span_click("保存")
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("资金计划--计划明细填报--经营性，保存成功")
			time.sleep(3)
			
			# 测试删除功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="budgetDetailEnter-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("删除")
			ok_click()
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("资金计划--计划明细填报--经营性，删除成功")
			time.sleep(3)
			
			# 测试审核功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="budgetDetailEnter-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("审核")
			ok_click()
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("资金计划--计划明细填报--经营性，审核成功")
			time.sleep(3)
			
			# 测试取消审核功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="budgetDetailEnter-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("审核",'取消审核')
			ok_click()
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("资金计划--计划明细填报--经营性，取消审核成功")
			time.sleep(3)
			
			# 测试作废功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="budgetDetailEnter-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
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
			span_click("作废")
			ok_click()
			
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("资金计划--计划明细填报--经营性，作废成功")
			time.sleep(3)
			
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("经营性填报失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
			
			# def tearDown(self):
			#     self.driver.quit()
			print("结束时间：", time.strftime("%Y-%m-%d %H:%M:%S"))
		
		
		# 测试资金计划--计划明细填报--经营性🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱
		try:
			logger.info("测试资金计划--计划明细填报--融资性")
			switch_default()
			
			click("xpath", "//span[text()='计划明细填报']")
			sleep(1)
			switch_default()
			
			
			# 测试新增功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			for i in range(1, 4):
				switch_to("xpath", '//*[@id="budgetDetailEnter-tab-iframe"]')
				span_click("融资性")
				switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
				sleep(1)
				
				span_click("新增")
				switch_to("xpath", '//*[@id="addWin-iframe"]')
				
				# 计划项目
				click_up_click('//*[@id="combobox-input-budgetitemid"]')
				
				# 计划值
				money = random.randint(1, 300)
				double_click("xpath", '//*[@id="budgetamount-input"]')
				sleep(1)
				input("xpath", '//*[@id="budgetamount-input"]', str(money))
				sleep(1)
				
				#计划精度
				input_up_click('//*[@id="combobox-input-budgetaccuracygrade"]','年')
				
				span_click("保存")
				# 退出所有窗体
				switch_default()
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				if i == 3:
					print("资金计划--计划明细填报--融资性，新增成功")
				time.sleep(3)
			
			# 查询数据💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="budgetDetailEnter-tab-iframe"]')
			span_click("融资性")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			sleep(1)
			
			click("xpath", '//*[@id="north"]/div[2]/span')
			sleep(1)
			input_up_click('//*[@id="combobox-input-cancelstate"]', '未作废')
			span_click("查询")
			switch_default()
			
			# 测试修改功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="budgetDetailEnter-tab-iframe"]')
			span_click("融资性")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
			sleep(1)
			
			span_click("修改")
			switch_to("xpath", '//*[@id="addWin-iframe"]')
			
			input("xpath", '//*[@id="description"]', '测试修改')
			sleep(1)
			
			span_click("保存")
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("资金计划--计划明细填报--融资性，修改成功")
			time.sleep(3)
			
			# 测试删除功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="budgetDetailEnter-tab-iframe"]')
			span_click("融资性")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
			sleep(1)
			
			span_click("删除")
			ok_click()
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("资金计划--计划明细填报--融资性，删除成功")
			time.sleep(3)
			
			# 测试审核功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="budgetDetailEnter-tab-iframe"]')
			span_click("融资性")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
			sleep(1)
			
			span_click("审核")
			ok_click()
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("资金计划--计划明细填报--融资性，审核成功")
			time.sleep(3)
			
			# 测试取消审核功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="budgetDetailEnter-tab-iframe"]')
			span_click("融资性")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("审核", '取消审核')
			ok_click()
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("资金计划--计划明细填报--融资性，取消审核成功")
			time.sleep(3)
			
			# 测试作废功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="budgetDetailEnter-tab-iframe"]')
			span_click("融资性")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
			sleep(1)
			span_click("审核")
			ok_click()
			sleep(3)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
			sleep(1)
			span_click("作废")
			ok_click()
			
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("资金计划--计划明细填报--融资性，作废成功")
			time.sleep(3)
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("经营性填报失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
			
			# def tearDown(self):
			#     self.driver.quit()
			print("结束时间：", time.strftime("%Y-%m-%d %H:%M:%S"))
		
		# 测试资金计划--计划明细填报--投资性🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱
		try:
			logger.info("测试资金计划--计划明细填报--融资性")
			switch_default()
			
			click("xpath", "//span[text()='计划明细填报']")
			sleep(1)
			switch_default()
			
			# 测试新增功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			for i in range(1, 4):
				switch_to("xpath", '//*[@id="budgetDetailEnter-tab-iframe"]')
				span_click("投资性")
				switch_to("xpath", '//*[@id="subTabThree-iframe"]')
				sleep(1)
				
				span_click("新增")
				switch_to("xpath", '//*[@id="addWin-iframe"]')
				
				# 计划项目
				click_up_click('//*[@id="combobox-input-budgetitemid"]')
				
				# 计划值
				money = random.randint(1, 300)
				double_click("xpath", '//*[@id="budgetamount-input"]')
				sleep(1)
				input("xpath", '//*[@id="budgetamount-input"]', str(money))
				sleep(1)
				
				# 计划精度
				input_up_click('//*[@id="combobox-input-budgetaccuracygrade"]', '年')
				
				#投资类型
				click_up_click('//*[@id="combobox-input-investmenttype"]')
				
				span_click("保存")
				# 退出所有窗体
				switch_default()
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				if i == 3:
					print("资金计划--计划明细填报--投资性，新增成功")
				time.sleep(3)
			
			# 查询数据💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="budgetDetailEnter-tab-iframe"]')
			span_click("投资性")
			switch_to("xpath", '//*[@id="subTabThree-iframe"]')
			sleep(1)
			
			click("xpath", '//*[@id="north"]/div[2]/span')
			sleep(1)
			input_up_click('//*[@id="combobox-input-cancelstate"]', '未作废')
			span_click("查询")
			switch_default()
			
			# 测试修改功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="budgetDetailEnter-tab-iframe"]')
			span_click("投资性")
			switch_to("xpath", '//*[@id="subTabThree-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("修改")
			switch_to("xpath", '//*[@id="addWin-iframe"]')
			
			input("xpath", '//*[@id="description"]', '测试修改')
			sleep(1)
			
			span_click("保存")
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("资金计划--计划明细填报--投资性，修改成功")
			time.sleep(3)
			
			# 测试删除功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="budgetDetailEnter-tab-iframe"]')
			span_click("投资性")
			switch_to("xpath", '//*[@id="subTabThree-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("删除")
			ok_click()
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("资金计划--计划明细填报--投资性，删除成功")
			time.sleep(3)
			
			# 测试审核功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="budgetDetailEnter-tab-iframe"]')
			span_click("投资性")
			switch_to("xpath", '//*[@id="subTabThree-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("审核")
			ok_click()
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("资金计划--计划明细填报--投资性，审核成功")
			time.sleep(3)
			
			# 测试取消审核功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="budgetDetailEnter-tab-iframe"]')
			span_click("投资性")
			switch_to("xpath", '//*[@id="subTabThree-iframe"]')
			sleep(1)
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="gridbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("审核", '取消审核')
			ok_click()
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("资金计划--计划明细填报--投资性，取消审核成功")
			time.sleep(3)
			
			# 测试作废功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="budgetDetailEnter-tab-iframe"]')
			span_click("投资性")
			switch_to("xpath", '//*[@id="subTabThree-iframe"]')
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
			span_click("作废")
			ok_click()
			
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("资金计划--计划明细填报--投资性，作废成功")
			time.sleep(3)
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("投资性失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
			
			# def tearDown(self):
			#     self.driver.quit()
			print("结束时间：", time.strftime("%Y-%m-%d %H:%M:%S"))
		
		
		# 测试资金计划--计划明细填报查看🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱
		try:
			logger.info("测试资金计划--计划明细填报查看")
			switch_default()
			
			click("xpath", "//span[text()='计划明细填报查看']")
			sleep(1)
			switch_default()
			
			# 测试经营性查看💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath",'//*[@id="budgetDetailEnterView-tab-iframe"]')
			span_click("经营性")
			switch_to("xpath",'//*[@id="subTabOne-iframe"]')
			
			double_click("xpath",'//*[@id="grid-body-table"]/tbody/tr[1]/td[3]/div')
			sleep(1)
			switch_to("xpath",'//*[@id="detailWin-iframe"]')
			
			implici_wait("xpath", "//span[contains(text(),'组织')]")
			print("计划明细填报查看--经营性，查看成功")
			time.sleep(3)
			switch_default()
			click("xpath", "//span[text()='计划明细填报查看']")
			sleep(1)
			
			# 测试融资性查看💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="budgetDetailEnterView-tab-iframe"]')
			span_click("融资性")
			switch_to("xpath", '//*[@id="subTabTwo-iframe"]')
			
			double_click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[3]/div')
			sleep(1)
			switch_to("xpath", '//*[@id="detailWin-iframe"]')
			
			implici_wait("xpath", "//span[contains(text(),'组织')]")
			print("计划明细填报查看--融资性，查看成功")
			time.sleep(3)
			switch_default()
			click("xpath", "//span[text()='计划明细填报查看']")
			sleep(1)
			
			# 测试投资性查看💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="budgetDetailEnterView-tab-iframe"]')
			span_click("投资性")
			switch_to("xpath", '//*[@id="subTabThree-iframe"]')
			
			double_click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[3]/div')
			sleep(1)
			switch_to("xpath", '//*[@id="detailWin-iframe"]')
			
			implici_wait("xpath", "//span[contains(text(),'组织')]")
			print("计划明细填报查看--投资性，查看成功")
			time.sleep(3)
			switch_default()
			click("xpath", "//span[text()='计划明细填报查看']")
			sleep(1)
			
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("投资性失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
			
			# def tearDown(self):
			#     self.driver.quit()
			print("结束时间：", time.strftime("%Y-%m-%d %H:%M:%S"))

		
		# 测试资金计划--计划拆分编制🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱
		try:
			logger.info("测试资金计划--计划拆分编制·    ")
			switch_default()
			
			click("xpath", "//span[text()='计划拆分编制']")
			sleep(1)
			switch_default()
			
			# 测试新增功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			for i in range (1,3):
				switch_to("xpath",'//*[@id="budgetSplitMaking-tab-iframe"]')
				span_click("新增")
				switch_to("xpath",'//*[@id="addWin-iframe"]')
				
				#计划方案
				click_up_click('//*[@id="combobox-input-schemeid"]')
				
				if i ==1 :
					click("xpath",'//*[@id="t1_t1-fixed"]/td[2]/div/button')
				if i ==2 :
					click("xpath", '//*[@id="t1_t2-fixed"]/td[2]/div/button')
				sleep(1)
				
				span_click("下一步")
				switch_parent()
				switch_to("xpath",'//*[@id="makingWin-iframe"]')
				
				span_click("保存")
				
				#退出所有窗体
				switch_default()
				implici_wait("xpath", "//span[contains(text(),'组织')]")
				if i==2 :
					print("计划拆分编制，新增成功")
				if i==1 :
					switch_to("xpath", '//*[@id="budgetSplitMaking-tab-iframe"]')
					click("xpath",'//*[@id="t1_t0-fixed"]/td[2]/div/button')
					sleep(1)
					
					span_click("删除")
					ok_click()
					# 退出所有窗体
					switch_default()
					implici_wait("xpath", "//span[contains(text(),'共处理1个记录，全部处理成功。')]")
					print("计划拆分编制，删除成功")
					
			# 测试修改功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="budgetSplitMaking-tab-iframe"]')
			span_click("新增")
			switch_to("xpath", '//*[@id="addWin-iframe"]')
			
			#刷新、勾选按钮
			click("xpath",'//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath",'//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("修改")
			switch_to("xpath",'//*[@id="makingWin-iframe"]')
			
			span_click("保存")
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("计划拆分编制，修改成功")
			
			# 测试送审功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="budgetSplitMaking-tab-iframe"]')
			span_click("新增")
			switch_to("xpath", '//*[@id="addWin-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			span_click("送审")
			ok_click()
			
			
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("计划拆分编制，送审成功")
			
			# 测试撤销送审功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="budgetSplitMaking-tab-iframe"]')
			span_click("新增")
			switch_to("xpath", '//*[@id="addWin-iframe"]')
			
			# 刷新、勾选按钮
			click("xpath", '//*[@id="treepagingbar-page-refresh"]')
			sleep(1)
			click("xpath", '//*[@id="t1_t0-fixed"]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("送审","撤销送审")
			ok_click()
			
			# 退出所有窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("计划拆分编制，撤销送审成功")
			
			
			
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("投资性失败！" + str(traceback.format_exc()))
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
