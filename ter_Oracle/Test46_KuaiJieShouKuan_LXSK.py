# encoding=utf-8
# @Time : 2020/11/16 08:30
# @Author : zzg
# 此文件是测试Oracle版本资金结算管理--业务系统对接--快捷收款--离线收款
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
class Test46_KuaiJieShouKuan_LXSK(unittest.TestCase):
	
	# 启动浏览器
	def setUp(self):
		# 启动浏览器的另外一个方法：通过封装启动浏览器的驱动，启动不同浏览器
		self.driver = get("chrome")
	
	# 登陆系统、对系统设置进行操作
	def test_trade(self):
		
		# login(G_Ora_Url, mindy, Password, "亚唐科技")
		login(G_Ora_Url, mindy, Password, "亚唐科技")
		
		logging.info("开始测试资金结算管理--业务系统对接--快捷收款-离线收款")
		# 将页面的滚动条滑动到‘资金结算管理’页面的地方
		js_gd("xpath", "//span[contains(text(),'资金结算管理')]")
		# 用JS的方法点击资金结算管理菜单按钮
		js_click("xpath", "//span[contains(text(),'资金结算管理')]")
		sleep(1)
		# 点击'外币收付结算'菜单
		click("xpath", "//span[text()='业务系统对接']")
		sleep(1)
		# 点击收款处理菜单
		click("xpath", "//span[text()='快捷收款']")
		sleep(1)
		# 退出所有iframe窗体
		switch_default()
		try:
			'''
			# 收回窗体💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			click("xpath", "//span[text()='业务系统对接']")
			sleep(1)
			js_click("xpath", "//span[contains(text(),'资金结算管理')]")
			sleep(1)
			
			# 创建收款处理-银行账户收款账号
			js_gd("xpath", "//span[contains(text(),'账户资金监控')]")
			# 用JS的方法点击账户资金监控菜单按钮
			js_click("xpath", "//span[contains(text(),'账户资金监控')]")
			sleep(1)
			click("xpath", "//span[contains(text(),'账户生命周期')]")
			click("xpath", "//span[text()='账户维护']")
			sleep(1)
			switch_default()
			
			# 切入单币种账户窗体
			switch_to("xpath", '//*[@id="bankAccounts-tab-iframe"]')
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			sleep(1)
			click("xpath", "//span[text()='新增']")
			sleep(1)
			switch_to("xpath", '//*[@id="addWin-iframe"]')
			#银行
			click("xpath", "//input[@id='combobox-input-bankid']")
			sleep(1)
			click("xpath", "//div[@title='代码-名称:BOC-中国银行']")
			sleep(1)
			
			# 选择开户行
			input("xpath", "//input[@id='combobox-input-banklocationid']", "大连泡崖")
			sleep(1)
			click("xpath", "//div[@title='联行号-开户行名:104222000965-中国银行股份有限公司大连泡崖街支行']")
			sleep(1)
			
			# 选择币种
			input("xpath", "//input[@id='combobox-input-currencyid']", "CNY")
			sleep(1)
			input_down("xpath", "//input[@id='combobox-input-currencyid']")
			input_enter("xpath", "//input[@id='combobox-input-currencyid']")
			time.sleep(1)
			
			# 选择账户性质
			input("xpath", "//input[@id='combobox-input-accounttypeid']", "基本户")
			sleep(1)
			input_down("xpath", "//input[@id='combobox-input-accounttypeid']")
			input_enter("xpath", "//input[@id='combobox-input-accounttypeid']")
			time.sleep(1)
			
			# # 选择银企直联户isbankdirect
			click("xpath", "//input[@id='isbankdirect']")
			sleep(1)
			
			# 选择境内外
			input("xpath", "//input[@id='combobox-input-inorout']", "境内")
			sleep(1)
			input_down("xpath", "//input[@id='combobox-input-inorout']")
			input_enter("xpath", "//input[@id='combobox-input-inorout']")
			
			# 输入银行账号
			input("xpath", '//*[@id="accountnumber"]', '20211046')
			sleep(1)
			input("xpath", '//*[@id="accountname"]', '快捷收款-离线收款账户')
			sleep(1)
			# 点击保存按钮
			click("xpath", "//span[text()='保存']")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			sleep(1)
			# 切入窗体
			switch_to("xpath", '//*[@id="bankAccounts-tab-iframe"]')
			sleep(1)
			switch_to("xpath", '//*[@id="subTabOne-iframe"]')
			
			# 点击查看
			js_click("xpath", "//span[@class='f-contrac-close']")
			sleep(1)
			input("xpath", '//*[@id="accountnumber"]', '20211046')
			sleep(1)
			# 点击查询
			click("xpath", "//span[text()='查询']")
			sleep(1)
			
			# 勾选数据
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
			sleep(1)
			triangle_cick_and_element("维护", "开户")
			
			today = date.today()
			open_date = today - timedelta(days=20)
			click("xpath", "//input[@id='openeddatewin-input']")
			sleep(1)
			clear("xpath", "//input[@id='openeddatewin-input']")
			sleep(1)
			input("xpath", "//input[@id='openeddatewin-input']", str(open_date))
			time.sleep(1)
			click("xpath", '//*[@id="journalbalance-input"]')
			sleep(1)
			clear("xpath", '//*[@id="journalbalance-input"]')
			sleep(1)
			input("xpath", '//*[@id="journalbalance-input"]', "5000")
			sleep(1)
			click("xpath", "//span[text()='确定']")
			sleep(1)
			switch_default()
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			sleep(3)
			
			js_click("xpath", "//span[contains(text(),'账户资金监控')]")
			sleep(1)
			'''
			
			#做数据💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			# 回到收款处理页面
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
			
			sleep(1)
			# 切入‘银行账户收款’的iframe窗体
			switch_to("xpath", "//iframe[@id='generalRecment-tab-iframe']")
			# 进入银行账户收款的iframe窗体
			switch_to("xpath", "//iframe[@id='subTabEight-iframe']")
			# 点击新增
			click("xpath", "//span[text()='新增']")
			# 切入新增的iframe窗体
			switch_to("xpath", "//iframe[@id='addWin-iframe']")
			sleep(1)
			
			# 交易类型
			click("xpath", "//input[@id='combobox-input-paytypeid']")
			# 输入开户行大连泡崖街支行名称，模糊查询
			input("xpath", "//input[@id='combobox-input-paytypeid']", "201-外部收款")
			sleep(1)
			input_down("xpath", "//input[@id='combobox-input-paytypeid']")
			input_enter("xpath", "//input[@id='combobox-input-paytypeid']")
			time.sleep(1)
			
			# 选择结算方式
			click("xpath", "//input[@id='combobox-input-settlementmodeid']")
			sleep(1)
			clear("xpath", "//input[@id='combobox-input-settlementmodeid']")
			sleep(1)
			# 输入名称，模糊查询
			input("xpath", "//input[@id='combobox-input-settlementmodeid']", "602-单笔转账收款")
			sleep(1)
			input_down("xpath", "//input[@id='combobox-input-settlementmodeid']")
			input_enter("xpath", "//input[@id='combobox-input-settlementmodeid']")
			time.sleep(1)
			
			# 收方账户
			click("xpath", "//input[@id='combobox-input-ourbankaccountid']")
			sleep(1)
			input("xpath", "//input[@id='combobox-input-ourbankaccountid']", "20211046")
			sleep(1)
			input_enter("xpath", "//input[@id='combobox-input-ourbankaccountid']")
			sleep(1)
			input_down("xpath", "//input[@id='combobox-input-ourbankaccountid']")
			sleep(1)
			input_enter("xpath", "//input[@id='combobox-input-ourbankaccountid']")
			sleep(1)
			
			# 付方名称
			input("xpath", "//input[@id='combobox-input-oppcounterpartyid']", "浙江华语科技")
			sleep(1)
			
			# 双击清楚下拉框
			double_click("xpath", "//span[text()='卡折类型']")
			sleep(1)
			
			# 收方账户
			input("xpath", "//input[@id='combobox-input-oppcounterpartyaccountid']", "200848782767819")
			sleep(1)
			
			# 双击清楚下拉框
			double_click("xpath", "//span[text()='卡折类型']")
			sleep(1)
			
			# 收方开户银行
			click("xpath", "//input[@id='combobox-input-oppbanklocationid']")
			sleep(1)
			input_enter("xpath", "//input[@id='combobox-input-oppbanklocationid']")
			sleep(1)
			input_down("xpath", "//input[@id='combobox-input-oppbanklocationid']")
			sleep(1)
			input_enter("xpath", "//input[@id='combobox-input-oppbanklocationid']")
			time.sleep(1)
			
			# 金额
			money = random.randint(100, 300)
			input("xpath", "//input[@id='ouramount-input']", money)
			sleep(1)
			
			# 手续费
			clear("xpath", '//*[@id="costs-input"]')
			sleep(1)
			input("xpath", '//*[@id="costs-input"]', "10")
			sleep(2)
			
			# 用途
			input("xpath", "//input[@id='combobox-input-purpose']", "快捷收款离线收款数据导入")
			sleep(1)
			
			# 点击保存按钮
			click("xpath", "//span[text()='保存']")
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
			time.sleep(3)
			# 更改数据库单据来源
			sql = "update T_SE_RECMENTS set RECORDSOURCE = '4' where purpose like '%快捷收款离线收款数据导入%'"
			ora_sql(ora_ip, ora_sid, ora_user, ora_pwd,
			       sql)
			span_click("资金系统收付")
			span_click("业务系统对接")
			span_click("快捷收款")
			
			#修改功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			sql = "update T_SE_RECMENTS set paystate = '1' where purpose like '%快捷收款离线收款数据导入%'"
			ora_sql(ora_ip, ora_sid, ora_user, ora_pwd,
			       sql)
			switch_to("xpath",'//*[@id="externalRecments-tab-iframe"]')
			span_click("离线收款")
			sleep(1)
			switch_to("xpath",'//*[@id="subTabSix-iframe"]')
			
			#勾选按钮
			click("xpath",'//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("修改")
			switch_to("xpath",'//*[@id="singleModWin-iframe"]')
			span_click("保存")
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功')]")
			print("快捷收款-离线收款，修改成功！")
			time.sleep(3)
			
			# 收款失败💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			switch_to("xpath", '//*[@id="externalRecments-tab-iframe"]')
			span_click("离线收款")
			sleep(1)
			switch_to("xpath", '//*[@id="subTabSix-iframe"]')
			
			# 勾选按钮
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("收款失败")
			span_click("确定")
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功')]")
			print("快捷收款-离线收款，收款失败成功！")
			time.sleep(3)
			
			
			#确认收款功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			sql = "update T_SE_RECMENTS set APPROVESTATE = '2' where purpose like '%快捷收款离线收款数据导入%'"
			ora_sql(ora_ip, ora_sid, ora_user, ora_pwd,
			       sql)
			switch_to("xpath", '//*[@id="externalRecments-tab-iframe"]')
			span_click("离线收款")
			sleep(1)
			switch_to("xpath", '//*[@id="subTabSix-iframe"]')
			
			# 勾选按钮
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("核对并确认收款",'确认收款')
			ok_click()
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'收款单确认收款成功！')]")
			print("快捷收款-离线收款，确认收款成功！")
			time.sleep(3)
			
			# 勾对并确认收款功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			sql = "update T_SE_RECMENTS set paystate = '1' where purpose like '%快捷收款离线收款数据导入%'"
			ora_sql(ora_ip, ora_sid, ora_user, ora_pwd,
			       sql)
			switch_to("xpath", '//*[@id="externalRecments-tab-iframe"]')
			span_click("离线收款")
			sleep(1)
			switch_to("xpath", '//*[@id="subTabSix-iframe"]')
			
			# 勾选按钮
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			triangle_cick_and_element("核对并确认收款", '勾对并确认收款')
			
			#切入勾对确认付款窗体
			switch_to("xpath",'//*[@id="tickPayWin-iframe"]')
			sleep(1)
			#勾选按钮
			click("xpath",'//*[@id="gridfinance-body-table"]/tbody/tr/td[2]/div/button')
			sleep(1)
			click("xpath",'//*[@id="gridtransaction-head-table"]/thead/tr/th[2]/div/button')
			sleep(1)
			span_click("确认收款")
			ok_click()
			click("xpath",'//*[@id="f-message-webgen-0-okBnt"]')
			sleep(1)
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功')]")
			print("快捷收款-离线收款，勾对确认收款成功！")
			time.sleep(3)
			
			
			# 核对并确认收款功能💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨💨
			sql = "update T_SE_RECMENTS set paystate = '1' where purpose like '%快捷收款离线收款数据导入%'"
			ora_sql(ora_ip, ora_sid, ora_user, ora_pwd,
					sql)
			#去做银行流水
			span_click("业务系统对接")
			js_click("xpath", "//span[contains(text(),'资金结算管理')]")
			sleep(1)
			# 将页面的滚动条滑动到‘资金结算管理’页面的地方
			js_gd("xpath", "//span[contains(text(),'账户资金监控')]")
			# 用JS的方法点击资金结算管理菜单按钮
			js_click("xpath", "//span[contains(text(),'账户资金监控')]")
			sleep(1)
			span_click("直联账户查询")
			#切入直联账户查询窗体
			switch_to("xpath",'//*[@id="directBankAccountQuery-tab-iframe"]')
			switch_to("xpath",'//*[@id="subTabOne-iframe"]')
			sleep(1)
			#查询账户今日流水
			click('xpath','//*[@id="north"]/div[2]/span')
			sleep(1)
			#账户号码
			input("xpath",'//*[@id="accountnumber"]','20211046')
			sleep(1)
			span_click("查询")
			#勾选按钮
			click("xpath",'//*[@id="grid-body-table"]/tbody/tr/td[2]/div/button')
			sleep(1)
			span_click("今日明细查询")
			sleep(3)
			switch_default()
			js_click("xpath", "//span[contains(text(),'账户资金监控')]")
			sleep(1)
			js_click("xpath", "//span[contains(text(),'资金结算管理')]")
			sleep(1)
			span_click("业务系统对接")
			span_click("快捷收款")
			switch_default()
			
			switch_to("xpath", '//*[@id="externalRecments-tab-iframe"]')
			span_click("离线收款")
			sleep(1)
			switch_to("xpath", '//*[@id="subTabSix-iframe"]')
			
			# 勾选按钮
			click("xpath", '//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			
			span_click("核对并确认收款")
			switch_to("xpath",'//*[@id="confirmPayWin-iframe"]')
			#点击查询
			click("xpath",'//*[@id="north"]/div[2]/span')
			sleep(1)
			#清空金额
			double_click("xpath",'//*[@id="tsstartmoney-wrapper"]')
			sleep(1)
			clear("xpath",'//*[@id="tsstartmoney-input"]')
			sleep(1)
			double_click("xpath", '//*[@id="tsendmoney-wrapper"]')
			sleep(1)
			clear("xpath", '//*[@id="tsendmoney-input"]')
			sleep(1)
			
			span_click("查询")
			#勾选按钮
			click("xpath",'//*[@id="grid-body-table"]/tbody/tr[1]/td[2]/div/button')
			sleep(1)
			span_click("确认")
			ok_click()
			# 退出所有iframe窗体
			switch_default()
			# 用隐式等待方法等页面出现新增成功的提示框
			implici_wait("xpath", "//span[contains(text(),'操作成功')]")
			print("快捷收款-离线收款，核对并确认收款成功！")
			time.sleep(3)
			
			
			
			
		except Exception as err:
			# 发生其他异常时，打印异常堆栈信息
			print(traceback.print_exc())
			logging.debug("跨境外币汇款-其他支付失败！" + str(traceback.format_exc()))
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
