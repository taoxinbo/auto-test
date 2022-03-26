# encoding=utf-8
# @Time : 2020/8/14 14:49
# @Author : Mindy
# 此文件是测试外联接口设置模块
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


class Test_Wljk(unittest.TestCase):
	
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
		# login(G_Mys_Url, mindy, Password, "亚唐科技")
		# login(G_Mys_Url, judy, Password, "默认租户")
		
		logging.info("开始测试外联接口设置的页面功能")
		# 将页面的滚动条滑动到‘外联接口设置’页面的地方
		js_gd("xpath", "//span[contains(text(),'外联接口设置')]")
		# 用JS的方法点击资金结算管理菜单按钮
		js_click("xpath", "//span[contains(text(),'外联接口设置')]")
		
		# 测试企业系统对接--业务管理
		try:
			# 点击理财投资菜单
			click("xpath", "//span[@title='企业系统对接']")
			# 点击理财合同登记菜单
			click("xpath", "//span[@title='业务管理']")
			# 退出所有的iframe窗体
			switch_default()

			logging.info("开始测试业务管理功能")

			for i in range(1, 2):
				# 切入支票用途的iframe窗体
				switch_to("xpath", "//iframe[@id='businessManage-tab-iframe']")
				logging.info("开始测试业务管理功能")

				# 用JS的方法点击新增按钮
				js_click("xpath", "//span[text()='新增']")

				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='addWin-iframe']")
				sleep(1)

				# 输入编码
				input("xpath", "//input[@name='code']", "TestBusMan")
				sleep(1)

				# 输入名称
				input("xpath", "//input[@id='name']", "自动化测试业务管理")
				sleep(1)

				# 业务类型
				click("xpath", "//input[@id='combobox-input-businesstypeid']")
				# 输入银行名称，模糊查询
				input("xpath", "//input[@id='combobox-input-businesstypeid']",  "保证金导入")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-businesstypeid']")
				input_enter("xpath", "//input[@id='combobox-input-businesstypeid']")
				time.sleep(1)

				# 流程插件
				click("xpath", "//input[@id='combobox-input-interfaceid']")
				# 输入银行名称，模糊查询
				input("xpath", "//input[@id='combobox-input-interfaceid']", "保证金导入")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-interfaceid']")
				input_enter("xpath", "//input[@id='combobox-input-interfaceid']")
				time.sleep(1)

				# 批处理模式combobox-input-rowmode
				click("xpath", "//input[@id='combobox-input-rowmode']")
				# 输入银行名称，模糊查询
				input("xpath", "//input[@id='combobox-input-rowmode']", "单处理")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-rowmode']")
				input_enter("xpath", "//input[@id='combobox-input-rowmode']")
				time.sleep(1)

				# 点击保存按钮
				click("xpath", "//span[text()='保存']")

				# 退出所有iframe窗体
				switch_default()

				# 用隐式等待方法等页面出现新增成功的提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				print("业务管理，保存成功！")
				time.sleep(3)

				if i == 1:
					# 修改功能
					# 切入业务管理的iframe窗体
					switch_to("xpath", "//iframe[@id='businessManage-tab-iframe']")

					# 点击查看
					# 用JS的方法点击放大镜
					js_click("xpath", "//span[@class='f-contrac-close']")
					sleep(1)

					# 输入名称
					input("xpath", "//input[@id='businessname']", "自动化测试业务管理")
					sleep(1)

					# 点击查询
					click("xpath", "//span[text()='查询']")

					# 勾选
					click("xpath", "//div[@title='名称:自动化测试业务管理']/parent::*/preceding-sibling::*[2]/descendant::*[2]")

					# 点击修改
					click("xpath", "//span[text()='修改']")
					sleep(1)

					switch_to("xpath", "//iframe[@id='modWin-iframe']")
					sleep(1)

					# 附加参数配置
					input("xpath", "//textarea[@id='attributes']", "自动化测试附加参数配置")
					sleep(1)

					# 点击保存按钮
					click("xpath", "//span[text()='保存']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现新增成功的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("业务管理，修改成功！")
					time.sleep(3)

					# 缺少设置解析规则

					# 禁用
					# 切入业务管理的iframe窗体
					switch_to("xpath", "//iframe[@id='businessManage-tab-iframe']")

					# 勾选
					click("xpath", "//div[@title='名称:自动化测试业务管理']/parent::*/preceding-sibling::*[2]/descendant::*[2]")

					# 点击修改
					click("xpath", "//span[text()='禁用']")
					sleep(1)

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现新增成功的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("业务管理，禁用成功！")
					time.sleep(3)

					# 激活
					# 切入业务管理的iframe窗体
					switch_to("xpath", "//iframe[@id='businessManage-tab-iframe']")

					# 勾选
					click("xpath", "//div[@title='名称:自动化测试业务管理']/parent::*/preceding-sibling::*[2]/descendant::*[2]")

					# 点击修改
					click("xpath", "//span[text()='激活']")
					sleep(1)

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现新增成功的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("业务管理，激活成功！")
					time.sleep(3)

					# 删除
					# 切入业务管理的iframe窗体
					switch_to("xpath", "//iframe[@id='businessManage-tab-iframe']")

					# 勾选
					click("xpath", "//div[@title='名称:自动化测试业务管理']/parent::*/preceding-sibling::*[2]/descendant::*[2]")

					# 点击修改
					click("xpath", "//span[text()='删除']")
					sleep(1)

					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现新增成功的提示框
					implici_wait("xpath", "//span[contains(text(),'共处理1个记录;删除成功1个;删除失败0个')]")
					print("业务管理，删除成功！")
					time.sleep(3)

			switch_default()

			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='业务管理']/child::*[1]")

			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//span[@title='企业系统对接']")

			# 打印操作成功日志
			print("业务管理，操作成功!")
			logging.info("业务管理，操作成功!")
			time.sleep(2)

		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("业务管理,失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)

		# 测试企业系统对接--业务转换对象管理
		try:
			# 点击企业系统对接菜单
			click("xpath", "//span[@title='企业系统对接']")
			# 点击理财合同登记菜单
			click("xpath", "//span[@title='业务转换对象管理']")
			# 退出所有的iframe窗体
			switch_default()

			logging.info("开始业务转换对象管理功能")

			for i in range(1, 2):

				# 切入业务转换对象管理的iframe窗体
				switch_to("xpath", "//iframe[@id='businessObjectManage-tab-iframe']")

				# 用JS的方法点击新增按钮
				js_click("xpath", "//span[text()='新增']")

				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='addWin-iframe']")
				sleep(1)

				# 业务类型
				click("xpath", "//input[@id='combobox-input-businesstypeid']")
				# 输入银行名称，模糊查询
				input("xpath", "//input[@id='combobox-input-businesstypeid']", "保证金导入")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-businesstypeid']")
				input_enter("xpath", "//input[@id='combobox-input-businesstypeid']")
				time.sleep(1)

				# 数据源类型
				click("xpath", "//input[@id='combobox-input-sourcetype']")
				# 输入银行名称，模糊查询
				input("xpath", "//input[@id='combobox-input-sourcetype']", "原始数据")
				sleep(1)
				input_down("xpath", "//input[@id='combobox-input-sourcetype']")
				input_enter("xpath", "//input[@id='combobox-input-sourcetype']")
				time.sleep(1)

				# 业务对象名称
				input("xpath", "//input[@id='name']", "自动化测试业务对象")
				sleep(1)

				# 业务对象编码
				input("xpath", "//input[@id='code']", "T_ZDH_SMS")
				sleep(1)

				# 表名称
				click("xpath", "//input[@id='atstablename']")
				# 输入银行名称，模糊查询
				input("xpath", "//input[@id='atstablename']", "自动化中间表")
				sleep(1)
				input_down("xpath", "//input[@id='atstablename']")
				input_enter("xpath", "//input[@id='atstablename']")
				time.sleep(1)

				# 表编码
				click("xpath", "//input[@id='tablecode']")
				# 输入银行名称，模糊查询
				input("xpath", "//input[@id='tablecode']", "T_ZDH_SMS_ZJB")
				sleep(1)
				input_down("xpath", "//input[@id='tablecode']")
				input_enter("xpath", "//input[@id='tablecode']")
				time.sleep(1)

				# 点击保存按钮
				click("xpath", "//span[text()='保存']")

				# 退出所有iframe窗体
				switch_default()

				# 用隐式等待方法等页面出现新增成功的提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				print("业务转换对象管理，保存成功！")
				time.sleep(3)

				if i == 1:
					# 修改功能
					# 切入业务管理的iframe窗体
					switch_to("xpath", "//iframe[@id='businessObjectManage-tab-iframe']")

					# 点击查看
					# 用JS的方法点击放大镜
					js_click("xpath", "//span[@class='f-contrac-close']")
					sleep(1)

					# 输入业务对象编码
					input("xpath", "//input[@id='code']", "T_ZDH_SMS")
					sleep(1)

					# 点击查询
					click("xpath", "//span[text()='查询']")

					# 勾选
					click("xpath", "//div[@title='业务对象编码:T_ZDH_SMS']/parent::*/preceding-sibling::*[2]/descendant::*[2]")

					# 点击修改
					click("xpath", "//span[text()='修改']")
					sleep(1)

					switch_to("xpath", "//iframe[@id='modWin-iframe']")
					sleep(1)

					# 描述
					input("xpath", "//textarea[@id='description']", "自动化测试业务转换对象管理")
					sleep(1)

					# 点击保存按钮
					click("xpath", "//span[text()='保存']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现新增成功的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("业务转换对象管理，修改成功！")
					time.sleep(3)

					# 字段维护
					# 切入业务转换对象管理的iframe窗体
					switch_to("xpath", "//iframe[@id='businessObjectManage-tab-iframe']")

					# 勾选
					click("xpath", "//div[@title='业务对象编码:T_ZDH_SMS']/parent::*/preceding-sibling::*[2]/descendant::*[2]")

					# 点击字段维护
					click("xpath", "//span[text()='字段维护']")
					sleep(1)

					switch_to("xpath", "//iframe[@id='businessobjectfields-iframe']")
					sleep(1)

					# 用JS的方法点击新增按钮
					js_click("xpath", "//span[text()='新增']")

					# 切入新增的iframe窗体
					switch_to("xpath", "//iframe[@id='addWin-iframe']")
					sleep(1)

					# 名称
					input("xpath", "//input[@id='fieldname']", "自动化测试字段维护")
					sleep(1)

					# 编码
					input("xpath", "//input[@id='fieldcode']", "Test_Code")
					sleep(1)

					# 长度
					input("xpath", "//input[@id='fieldlength-input']", "20")
					sleep(1)

					# 字段顺序
					input("xpath", "//input[@id='displayorder-input']", "2")
					sleep(1)

					# 点击保存按钮
					click("xpath", "//span[text()='保存']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现新增成功的提示框
					# implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("业务转换对象管理，字段维护新增保存成功！")
					time.sleep(3)

					# 切入业务转换对象管理的iframe窗体
					switch_to("xpath", "//iframe[@id='businessObjectManage-tab-iframe']")

					switch_to("xpath", "//iframe[@id='businessobjectfields-iframe']")
					sleep(1)

					# 勾选
					click("xpath", "//div[@title='编码:Test_Code']/parent::*/preceding-sibling::*[4]/descendant::*[2]")

					# 点击保存按钮
					click("xpath", "//span[text()='修改']")
					sleep(1)

					switch_to("xpath", "//iframe[@id='modWin-iframe']")
					sleep(1)

					# 点击保存按钮
					click("xpath", "//span[text()='保存']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现新增成功的提示框
					# implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("业务转换对象管理，字段维护修改成功！")
					time.sleep(3)

					# 删除
					# 切入业务转换对象管理的iframe窗体
					switch_to("xpath", "//iframe[@id='businessObjectManage-tab-iframe']")

					switch_to("xpath", "//iframe[@id='businessobjectfields-iframe']")
					sleep(1)

					# 勾选
					click("xpath", "//div[@title='编码:Test_Code']/parent::*/preceding-sibling::*[4]/descendant::*[2]")

					# 点击保存按钮
					click("xpath", "//span[text()='删除']")
					sleep(1)

					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现新增成功的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功!共删除1个字段!')]")
					print("业务转换对象管理，字段维护删除成功！")
					time.sleep(3)

					# 点击进入业务管理的窗体
					switch_to("xpath", "//iframe[@id='businessObjectManage-tab-iframe']")
					sleep(1)

					click("xpath", "//div[@class='f-win-tl' and @id='f-win-title-businessobjectfields']/descendant::*[2]")

					switch_default()

			# 数据删除
			# 切入业务管理的iframe窗体
			switch_to("xpath", "//iframe[@id='businessObjectManage-tab-iframe']")

			# 勾选
			# click("xpath", "//div[@title='业务对象编码:T_ZDH_SMS']/parent::*/preceding-sibling::*[2]/descendant::*[2]")

			# 点击保存按钮
			click("xpath", "//span[text()='删除']")
			sleep(1)

			# 点击弹出框的OK键
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功!共删除1个业务转换对象!')]")
			print("业务转换对象管理，删除成功！")
			time.sleep(3)

			switch_default()

			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='业务转换对象管理']/child::*[1]")

			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//span[@title='企业系统对接']")

			# 打印操作成功日志
			print("业务转换对象管理，操作成功!")
			logging.info("业务转换对象管理，操作成功!")
			time.sleep(2)

		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("业务转换对象管理,失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)

		# 业务类型查看
		try:
			# 点击企业系统对接菜单
			click("xpath", "//span[@title='企业系统对接']")
			# 点击理财合同登记菜单
			click("xpath", "//span[@title='业务类型查看']")

			logging.info("开始业务类型查看功能")

			# 退出所有的iframe窗体
			switch_default()

			# 切入‘业务类型查看’的iframe窗体
			switch_to("xpath", "//iframe[@id='businessTypeView-tab-iframe']")

			# 点击查看
			# 用JS的方法点击放大镜
			js_click("xpath", "//span[@class='f-contrac-close']")
			sleep(1)

			# 输入内容
			input("xpath", "//input[@id='uccode']", "UC_FL_MARGIN_IMPORT")
			sleep(1)

			# 点击查询
			click("xpath", "//span[text()='查询']")

			# 用隐式等待方法等页面出现预期数据：受益人:Mindy科技有限公司
			implici_wait("xpath", "//div[@title='名称:保证金导入']")
			print("业务类型查看成功！")
			time.sleep(3)

			# 退出所有iframe窗体
			switch_default()

			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='业务类型查看']/child::*[1]")

			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//span[@title='企业系统对接']")

			# 打印操作成功日志
			print("业务类型查看，操作成功!")
			logging.info("业务类型查看，操作成功!")
			time.sleep(2)
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("业务类型查看,失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)

		# 对接方式查看
		try:
			# 点击企业系统对接菜单
			click("xpath", "//span[@title='企业系统对接']")
			# 点击理财合同登记菜单
			click("xpath", "//span[@title='对接方式查看']")

			logging.info("开始对接方式查看功能")

			# 退出所有的iframe窗体
			switch_default()

			# 切入‘对接方式查看’的iframe窗体
			switch_to("xpath", "//iframe[@id='convertTypesView-tab-iframe']")

			# 点击查看
			# 用JS的方法点击放大镜
			js_click("xpath", "//span[@class='f-contrac-close']")
			sleep(1)

			# 对接方式编码输入内容
			input("xpath", "//input[@id='code']", "table")
			sleep(1)

			# 点击查询
			click("xpath", "//span[text()='查询']")

			# 用隐式等待方法等页面出现预期数据：对接方式名称:中间表导入
			implici_wait("xpath", "//div[@title='对接方式名称:中间表导入']")
			print("对接方式查看成功！")
			time.sleep(3)

			# 退出所有iframe窗体
			switch_default()

			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='对接方式查看']/child::*[1]")

			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//span[@title='企业系统对接']")

			# 打印操作成功日志
			print("对接方式查看，操作成功!")
			logging.info("对接方式查看，操作成功!")
			time.sleep(2)
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("对接方式查看,失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		
		# 数据映射管理
		# 测试企业系统对接--数据映射管理
		try:
			# 点击企业系统对接菜单
			click("xpath", "//span[@title='企业系统对接']")
			# 点击数据映射管理
			click("xpath", "//span[@title='数据映射管理']")
			# 退出所有的iframe窗体
			switch_default()

			logging.info("开始测试数据映射管理功能")

			for i in range(1, 2):

				# 切入数据映射管理的iframe窗体
				switch_to("xpath", "//iframe[@id='dataMapManage-tab-iframe']")

				# 用JS的方法点击新增按钮
				js_click("xpath", "//span[text()='新增']")

				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='addWin-iframe']")
				sleep(1)

				# 数据映射管理名称
				input("xpath", "//input[@id='name']", "自动化测试数据映射管理")
				sleep(1)

				# 数据映射管理编码
				input("xpath", "//input[@id='code']", "Test_DataMapManage")
				sleep(1)

				# 输入调用名称
				input("xpath", "//textarea[@id='description']", "自动化测试数据映射管理调用说明")
				sleep(1)

				# 点击保存按钮
				click("xpath", "//span[text()='保存']")

				# 退出所有iframe窗体
				switch_default()

				# 用隐式等待方法等页面出现新增成功的提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				print("数据映射管理，保存成功！")
				time.sleep(3)

				if i == 1:
					# 修改功能
					# 切入数据映射管理的iframe窗体
					switch_to("xpath", "//iframe[@id='dataMapManage-tab-iframe']")

					# 点击查看
					# 用JS的方法点击放大镜
					js_click("xpath", "//span[@class='f-contrac-close']")
					sleep(1)

					# 输入数据映射管理编码
					input("xpath", "//input[@id='code']", "Test_DataMapManage")
					sleep(1)

					# 点击查询
					click("xpath", "//span[text()='查询']")

					# 勾选
					click("xpath", "//div[@title='编码:Test_DataMapManage']/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 点击修改
					click("xpath", "//span[text()='修改']")
					sleep(1)

					switch_to("xpath", "//iframe[@id='modWin-iframe']")
					sleep(1)

					# 调用说明
					input("xpath", "//textarea[@id='description']", "自动化测试数据映射管理调用说明")
					sleep(1)

					# 点击保存按钮
					click("xpath", "//span[text()='保存']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现新增成功的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("数据映射管理，修改成功！")
					time.sleep(3)

					# 明细维护维护
					# 切入数据映射管理的iframe窗体
					switch_to("xpath", "//iframe[@id='dataMapManage-tab-iframe']")

					# 勾选
					click("xpath", "//div[@title='编码:Test_DataMapManage']/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 点击明细维护
					click("xpath", "//span[text()='明细维护']")
					sleep(1)

					switch_to("xpath", "//iframe[@id='detailMaintainWin-iframe']")
					sleep(1)

					# 用JS的方法点击新增按钮
					js_click("xpath", "//span[text()='新增']")

					# 切入新增的iframe窗体
					switch_to("xpath", "//iframe[@id='addWin-iframe']")
					sleep(1)

					# 原始值
					input("xpath", "//input[@id='sourcevalue']", "1")
					sleep(1)

					# 目标值
					input("xpath", "//input[@id='targetvalue']", "2")
					sleep(1)

					# 点击保存按钮
					click("xpath", "//span[text()='保存']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现新增成功的提示框
					# implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("数据映射管理，明细维护新增保存成功！")
					time.sleep(3)

					# 切入数据映射管理的iframe窗体
					switch_to("xpath", "//iframe[@id='dataMapManage-tab-iframe']")

					switch_to("xpath", "//iframe[@id='detailMaintainWin-iframe']")
					sleep(1)

					# 勾选
					click("xpath", "//div[@title='原始值:1']/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 点击修改按钮
					click("xpath", "//span[text()='修改']")
					sleep(1)

					switch_to("xpath", "//iframe[@id='modWin-iframe']")
					sleep(1)

					# 点击保存按钮
					click("xpath", "//span[text()='保存']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现新增成功的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("数据映射管理，明细维护修改成功！")
					time.sleep(3)

					# 删除
					# 切入数据映射管理的iframe窗体
					switch_to("xpath", "//iframe[@id='dataMapManage-tab-iframe']")

					switch_to("xpath", "//iframe[@id='detailMaintainWin-iframe']")
					sleep(1)

					# 勾选
					click("xpath", "//div[@title='原始值:1']/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 点击删除按钮
					click("xpath", "//span[text()='删除']")
					sleep(1)

					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现新增成功的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("数据映射管理，明细维护删除成功！")
					time.sleep(3)

					# 点击进入业务管理的窗体
					switch_to("xpath", "//iframe[@id='dataMapManage-tab-iframe']")

					click("xpath", "//div[@class='f-win-tl' and @id='f-win-title-detailMaintainWin']/descendant::*[2]")

					switch_default()

			# 数据删除
			# 切入数据映射管理的iframe窗体
			switch_to("xpath", "//iframe[@id='dataMapManage-tab-iframe']")

			# 勾选
			# click("xpath", "//div[@title='业务对象编码:T_ZDH_SMS']/parent::*/preceding-sibling::*[2]/descendant::*[2]")

			# 点击保存按钮
			click("xpath", "//span[text()='删除']")
			sleep(1)

			# 点击弹出框的OK键
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'共处理1个记录;删除成功1个;删除失败0个')]")
			print("数据映射管理，删除成功！")
			time.sleep(3)

			switch_default()

			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='数据映射管理']/child::*[1]")

			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//span[@title='企业系统对接']")

			# 打印操作成功日志
			print("数据映射管理，操作成功!")
			logging.info("数据映射管理，操作成功!")
			time.sleep(2)

		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("数据映射管理,失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		
		# 插件管理
		try:
			# 点击企业系统对接菜单
			click("xpath", "//span[@title='企业系统对接']")
			# 点击理财合同登记菜单
			click("xpath", "//span[@title='插件管理']")

			logging.info("开始测试插件管理--流程插件管理功能")

			# 退出所有的iframe窗体
			switch_default()

			# 切入‘插件管理’的iframe窗体
			switch_to("xpath", "//iframe[@id='interfaceManage-tab-iframe']")

			# 进入流程
			switch_to("xpath", "//iframe[@id='subTabTwo-iframe']")

			# 点击查看
			# 用JS的方法点击放大镜
			js_click("xpath", "//span[@class='f-contrac-close']")
			sleep(1)

			# 付款抽档插件输入内容
			input("xpath", "//input[@id='name']", "付款抽档插件")
			sleep(1)

			# 点击查询
			click("xpath", "//span[text()='查询']")

			# 用隐式等待方法等页面出现预期数据：对接方式名称:中间表导入
			implici_wait("xpath", "//div[@title='插件名称:net升级java付款抽档插件']")
			print("流程插件注册成功！")
			time.sleep(3)

			# 退出所有iframe窗体
			switch_default()

			# 开始测试转换器插件注册功能
			# 切入‘插件管理’的iframe窗体
			logging.info("开始测试插件管理--转换器插件注册功能")
			switch_to("xpath", "//iframe[@id='interfaceManage-tab-iframe']")

			click("xpath", "//span[text()='转换器插件注册']")
			sleep(1)

			# 进入转换器插件注册窗体
			switch_to("xpath", "//iframe[@id='subTabOne-iframe']")

			# 点击查看
			# 用JS的方法点击放大镜
			js_click("xpath", "//span[@class='f-contrac-close']")
			sleep(1)

			# 输入名称
			input("xpath", "//input[@id='name']", "根据短信来源信息匹配短信模板并生成短信内容")
			sleep(1)

			# 点击查询
			click("xpath", "//span[text()='查询']")

			# 用隐式等待方法等页面出现预期数据：对接方式名称:中间表导入
			implici_wait("xpath", "//div[contains(text(),'目标值：转换短信内容')]")
			print("转换器插件注册成功！")
			time.sleep(3)

			# 退出所有iframe窗体
			switch_default()

			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='插件管理']/child::*[1]")

			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//span[@title='企业系统对接']")

			# 打印操作成功日志
			print("插件管理，操作成功!")
			logging.info("插件管理，操作成功!")
			time.sleep(2)
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("插件管理,失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		"""
		# 中间表查询功能
		# 1. 企业系统对接--中间表查询--付款导入
		try:
			# 点击企业系统对接菜单
			click("xpath", "//span[@title='企业系统对接']")
			# 点击中间表查询菜单
			click("xpath", "//span[@title='中间表查询']")

			logging.info("开始测试企业系统对接--中间表查询功能")

			# 退出所有的iframe窗体
			switch_default()

			# 切入‘中间表查询’的iframe窗体
			switch_to("xpath", "//iframe[@id='midtableQuery-tab-iframe']")

			# 1. 付款导入
			switch_to("xpath", "//iframe[@id='subTabOne-iframe']")

			# 点击查看
			# 用JS的方法点击放大镜
			js_click("xpath", "//span[@class='f-contrac-close']")
			sleep(1)
			
			# 选择抽档状态
			click("xpath", "//input[@id='combobox-input-dealstate']")
			sleep(1)
			click("xpath", "//div[@title='已抽档']")
			
			# 选择支付状态
			click("xpath", "//input[@id='combobox-input-paystate']")
			sleep(1)
			click("xpath", "//div[@title='已收付']")
			
			# 选择返盘状态
			click("xpath", "//input[@id='combobox-input-returnstate']")
			sleep(1)
			click("xpath", "//div[@title='未返盘']")

			# 点击查询
			click("xpath", "//span[text()='查询']")

			# 用隐式等待方法等页面出现预期数据：创建人:OA
			implici_wait("xpath", "//div[@title='创建人:OA']")
			print("付款导入查看成功！")
			time.sleep(3)

			# 退出所有iframe窗体
			switch_default()
			
			# 切入‘中间表查询’的iframe窗体
			switch_to("xpath", "//iframe[@id='midtableQuery-tab-iframe']")
			
			# 2. 付款导出
			click("xpath", "//span[text()='付款导出']")
			
			switch_to("xpath", "//iframe[@id='subTabTwo-iframe']")
			
			# 点击查看
			# 用JS的方法点击放大镜
			js_click("xpath", "//span[@class='f-contrac-close']")
			sleep(1)
			
			# 选择抽档状态
			click("xpath", "//input[@id='combobox-input-dealstate']")
			sleep(1)
			click("xpath", "//div[@title='未抽档']")
			
			# 点击查询
			click("xpath", "//span[text()='查询']")
			
			# 用隐式等待方法等页面出现预期数据：收方户名:秦燕
			implici_wait("xpath", "//div[@title='收方户名:秦燕']")
			print("付款导出查看成功！")
			time.sleep(3)
			
			switch_default()
			
			# 切入‘中间表查询’的iframe窗体
			switch_to("xpath", "//iframe[@id='midtableQuery-tab-iframe']")
			
			# 3. 收款导出
			click("xpath", "//span[text()='收款导出']")
			
			switch_to("xpath", "//iframe[@id='subTabThree-iframe']")
			
			# 点击查看
			# 用JS的方法点击放大镜
			js_click("xpath", "//span[@class='f-contrac-close']")
			sleep(1)
			
			# 选择导出状态
			click("xpath", "//input[@id='combobox-input-dealstate']")
			sleep(1)
			click("xpath", "//div[@title='未抽档']")
			
			# 点击查询
			click("xpath", "//span[text()='查询']")
			
			# 用隐式等待方法等页面出现预期数据：收方户名:秦燕
			implici_wait("xpath", "//div[@title='付方户名:陈翔']")
			print("收款导出查看成功！")
			time.sleep(3)
			
			switch_default()
			
			# 切入‘中间表查询’的iframe窗体
			switch_to("xpath", "//iframe[@id='midtableQuery-tab-iframe']")
			
			# 4. 部门导入
			click("xpath", "//span[text()='部门导入']")
			
			switch_to("xpath", "//iframe[@id='subTabFour-iframe']")
			
			# 点击查看
			# 用JS的方法点击放大镜
			js_click("xpath", "//span[@class='f-contrac-close']")
			sleep(1)
			
			# 选择系统处理状态
			click("xpath", "//input[@id='combobox-input-dealstate']")
			sleep(1)
			click("xpath", "//div[@title='已抽档']")
			
			# 点击查询
			click("xpath", "//span[text()='查询']")
			
			# 用隐式等待方法等页面出现预期数据：收方户名:秦燕
			implici_wait("xpath", "//div[@title='修改人:OA']")
			print("收款导出查看成功！")
			time.sleep(3)
			
			switch_default()
			
			# 切入‘中间表查询’的iframe窗体
			switch_to("xpath", "//iframe[@id='midtableQuery-tab-iframe']")
			
			# 5. 银行账户交易明细导出
			click("xpath", "//span[text()='银行账户交易明细导出']")
			
			switch_to("xpath", "//iframe[@id='subTabFive-iframe']")
			
			# 点击查看
			# 用JS的方法点击放大镜
			js_click("xpath", "//span[@class='f-contrac-close']")
			sleep(1)
			
			# 选择系统处理状态
			click("xpath", "//input[@id='combobox-input-dealstate']")
			sleep(1)
			click("xpath", "//div[@title='未抽档']")
			
			# 点击查询
			click("xpath", "//span[text()='查询']")
			
			# 用隐式等待方法等页面出现预期数据：对方户名:秦燕
			implici_wait("xpath", "//div[@title='对方户名:秦燕']")
			print("银行账户交易明细导出查看成功！")
			time.sleep(3)
			
			switch_default()
			
			# 切入‘中间表查询’的iframe窗体
			switch_to("xpath", "//iframe[@id='midtableQuery-tab-iframe']")
			
			# 6. 交易对手账户导入
			click("xpath", "//span[text()='交易对手账户导入']")
			
			switch_to("xpath", "//iframe[@id='subTabSix-iframe']")
			
			# 点击查看
			# 用JS的方法点击放大镜
			js_click("xpath", "//span[@class='f-contrac-close']")
			sleep(1)
			
			# 选择系统处理状态
			click("xpath", "//input[@id='combobox-input-dealstate']")
			sleep(1)
			click("xpath", "//div[@title='已抽档']")
			
			# 点击查询
			click("xpath", "//span[text()='查询']")
			
			# 用隐式等待方法等页面出现预期数据：银行编码:ABC
			implici_wait("xpath", "//div[@title='银行编码:ABC']")
			print("交易对手账户导入成功！")
			time.sleep(3)
			
			# 退出所有iframe窗体
			switch_default()
			
			# 切入‘中间表查询’的iframe窗体
			switch_to("xpath", "//iframe[@id='midtableQuery-tab-iframe']")
			
			# 7. 交易对手导入
			click("xpath", "//span[text()='交易对手导入']")
			
			switch_to("xpath", "//iframe[@id='subTabSeven-iframe']")
			
			# 点击查看
			# 用JS的方法点击放大镜
			js_click("xpath", "//span[@class='f-contrac-close']")
			sleep(1)
			
			# 选择系统处理状态
			click("xpath", "//input[@id='combobox-input-dealstate']")
			sleep(1)
			click("xpath", "//div[@title='已抽档']")
			
			# 点击查询
			click("xpath", "//span[text()='查询']")
			
			# 用隐式等待方法等页面出现预期数据：创建人:OA
			implici_wait("xpath", "//div[@title='创建人:OA']")
			print("交易对手导入成功！")
			time.sleep(3)
			
			# 退出所有iframe窗体
			switch_default()
			
			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='中间表查询']/child::*[1]")

			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//span[@title='企业系统对接']")

			# 打印操作成功日志
			print("中间表查询，操作成功!")
			logging.info("中间表查询，操作成功!")
			time.sleep(2)
		
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("中间表查询,失败！" + str(traceback.format_exc()))
			# Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
			dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
			dir_path = make_current_hour_dir(dir_path + "\\")
			pic_path = os.path.join(dir_path, get_current_time() + ".png")
			capture(pic_path)
		"""
		# 外部系统注册
		# 测试企业系统对接--外部系统注册
		try:
			# 点击企业系统对接菜单
			click("xpath", "//span[@title='企业系统对接']")
			# 点击数据映射管理
			click("xpath", "//span[@title='外部系统注册']")
			# 退出所有的iframe窗体
			switch_default()

			logging.info("开始测试外部系统注册功能")

			for i in range(1, 2):

				# 切入外部系统注册的iframe窗体
				switch_to("xpath", "//iframe[@id='outSystemRegister-tab-iframe']")

				# 用JS的方法点击新增按钮
				js_click("xpath", "//span[text()='新增']")

				# 切入新增的iframe窗体
				switch_to("xpath", "//iframe[@id='addWin-iframe']")
				sleep(1)

				# 名称
				input("xpath", "//input[@id='name']", "自动化测试外部系统注册")
				sleep(1)

				# 编码
				input("xpath", "//input[@id='code']", "Test_outSystemRegister")
				sleep(1)

				# 服务地址
				input("xpath", "//input[@id='serverurl']", "/")
				sleep(1)

				# 点击保存按钮
				click("xpath", "//span[text()='保存']")

				# 退出所有iframe窗体
				switch_default()

				# 用隐式等待方法等页面出现新增成功的提示框
				implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
				print("外部系统注册，保存成功！")
				time.sleep(3)

				if i == 1:
					# 修改功能
					# 切入外部系统注册的iframe窗体
					switch_to("xpath", "//iframe[@id='outSystemRegister-tab-iframe']")

					# 点击查看
					# 用JS的方法点击放大镜
					js_click("xpath", "//span[@class='f-contrac-close']")
					sleep(1)

					# 输入数据映射管理编码
					input("xpath", "//input[@id='code']", "Test_outSystemRegister")
					sleep(1)

					# 点击查询
					click("xpath", "//span[text()='查询']")

					# 勾选
					click("xpath", "//div[@title='编码:Test_outSystemRegister']/parent::*/preceding-sibling::*[2]/descendant::*[2]")

					# 点击修改
					click("xpath", "//span[text()='修改']")
					sleep(1)

					switch_to("xpath", "//iframe[@id='modWin-iframe']")
					sleep(1)

					# 描述
					input("xpath", "//textarea[@id='description']", "自动化测试外部系统注册描述")
					sleep(1)

					# 点击保存按钮
					click("xpath", "//span[text()='保存']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现新增成功的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("外部系统注册，修改成功！")
					time.sleep(3)

					# 外部系统参数配置
					# 切入外部系统注册的iframe窗体
					switch_to("xpath", "//iframe[@id='outSystemRegister-tab-iframe']")

					# 勾选
					click("xpath", "//div[@title='编码:Test_outSystemRegister']/parent::*/preceding-sibling::*[2]/descendant::*[2]")

					# 点击外部系统参数配置
					click("xpath", "//span[text()='外部系统参数配置']")
					sleep(1)

					switch_to("xpath", "//iframe[@id='interfaceparamWin-iframe']")
					sleep(1)

					# 用JS的方法点击新增按钮
					js_click("xpath", "//span[text()='新增']")

					# 切入新增的iframe窗体
					switch_to("xpath", "//iframe[@id='addWin-iframe']")
					sleep(1)

					# 外部系统
					click("xpath", "//input[@id='combobox-input-outsystemid']")
					sleep(1)
					input("xpath", "//input[@id='combobox-input-outsystemid']", "自动化测试外部系统注册")
					sleep(1)
					# input_enter("xpath", "//input[@id='combobox-input-outsystemid']")
					# input_down("xpath", "//input[@id='combobox-input-outsystemid']")
					# time.sleep(1)
					click("xpath", "//div[@title='代码-名称:自动化测试外部系统注册']")
					sleep(1)

					# 业务类型
					click("xpath", "//input[@id='combobox-input-businesstypeid']")
					sleep(1)
					# input("xpath", "//input[@id='combobox-input-businesstypeid']", "net升级java付款抽档")
					# sleep(1)
					click("xpath", "//div[@title='名称:net升级java付款抽档']")
					sleep(1)

					# 请求方式
					click("xpath", "//input[@id='combobox-input-requestway']")
					sleep(1)
					input("xpath", "//input[@id='combobox-input-requestway']", "对外webservice接入")
					sleep(1)
					input_enter("xpath", "//input[@id='combobox-input-requestway']")
					input_down("xpath", "//input[@id='combobox-input-requestway']")
					time.sleep(1)

					# 插件参数
					input("xpath", "//input[@id='interfaceparam']", "1")
					sleep(1)

					# 点击保存按钮
					click("xpath", "//span[text()='保存']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现新增成功的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("外部系统注册，外部系统参数新增保存成功！")
					time.sleep(3)

					# 切入外部系统注册的iframe窗体
					switch_to("xpath", "//iframe[@id='outSystemRegister-tab-iframe']")

					switch_to("xpath", "//iframe[@id='interfaceparamWin-iframe']")
					sleep(1)

					# 勾选
					click("xpath", "//div[@title='外部系统:自动化测试外部系统注册']/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 点击修改按钮
					click("xpath", "//span[text()='修改']")
					sleep(1)

					switch_to("xpath", "//iframe[@id='modWin-iframe']")
					sleep(1)

					# 点击保存按钮
					click("xpath", "//span[text()='保存']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现新增成功的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("外部系统注册，外部系统参数修改成功！")
					time.sleep(3)

					# 删除
					# 切入外部系统注册的iframe窗体
					switch_to("xpath", "//iframe[@id='outSystemRegister-tab-iframe']")

					switch_to("xpath", "//iframe[@id='interfaceparamWin-iframe']")
					sleep(1)

					# 勾选
					click("xpath", "//div[@title='外部系统:自动化测试外部系统注册']/parent::*/preceding-sibling::*[1]/descendant::*[2]")

					# 点击删除按钮
					click("xpath", "//span[text()='删除']")
					sleep(1)

					# 点击弹出框的OK键
					click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

					# 退出所有iframe窗体
					switch_default()

					# 用隐式等待方法等页面出现新增成功的提示框
					implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
					print("外部系统注册，外部系统参数删除成功！")
					time.sleep(3)

					# 切入外部系统注册的iframe窗体
					switch_to("xpath", "//iframe[@id='outSystemRegister-tab-iframe']")

					click("xpath", "//div[@class='f-win-tl' and @id='f-win-title-interfaceparamWin']/descendant::*[2]")

					switch_default()

			# 数据删除
			# 切入外部系统注册的iframe窗体
			switch_to("xpath", "//iframe[@id='outSystemRegister-tab-iframe']")
			# 勾选
			# click("xpath", "//div[@title='业务对象编码:T_ZDH_SMS']/parent::*/preceding-sibling::*[2]/descendant::*[2]")

			# 点击保存按钮
			click("xpath", "//span[text()='删除']")
			sleep(1)

			# 点击弹出框的OK键
			click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

			# 退出所有iframe窗体
			switch_default()

			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			print("外部系统注册，删除成功！")
			time.sleep(3)

			switch_default()

			# 用JS的方法关闭当前页面
			js_click("xpath", "//a[@title='外部系统注册']/child::*[1]")

			# 再次点击基础设置菜单，使之关闭
			click("xpath", "//span[@title='企业系统对接']")

			# 打印操作成功日志
			print("外部系统注册，操作成功!")
			logging.info("外部系统注册，操作成功!")
			time.sleep(2)

		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("外部系统注册,失败！" + str(traceback.format_exc()))
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
