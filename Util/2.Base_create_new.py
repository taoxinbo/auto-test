#encoding=utf-8
# 2020-09-04
# TaoXB
# 此文件是自动化测试全新的一个租户：测试新建租户（租户、套餐、权限分配等功能）、测试系统管理、测试新增用户、测试权限、 新用户（登陆/退出）、新用户（修改登陆密码/修改支付密码/重置支付密码）

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

#print("开始时间：",time.strftime("%Y-%m-%d %H:%M:%S"))

driver = ""
class Base_create_new(unittest.TestCase):

    #启动浏览器
    def setUp(self):

        #启动浏览器的另外一个方法：通过封装启动浏览器的驱动，启动不同浏览器
        self.driver = get("chrome")

    # 登陆系统、对系统设置进行操作
    def test_trade(self):

        logging.info("测试‘租户、套餐、协议、组织、用户、权限’的功能")

        for url in Url_L:
            logging.info("测试‘租户、套餐、协议’的功能")

            #通过登陆封装函数，登陆‘SupAdmin’，创建‘租户、套餐、协议’
            login( url, SupAdmin, privatecloud,"假的")
            #login(url, 'Felix', Password, "默认租户")

            #点击系统菜单
            self.driver.find_element_by_xpath("//span[contains(text(),'系统菜单')]").click()
            time.sleep(1)
            #点击租户管理菜单
            self.driver.find_element_by_xpath("//span[contains(text(),'租户管理')]").click()
            time.sleep(1)


            # 测试租户
            logging.info("测试‘租户’")
            # 点击租户设置菜单
            self.driver.find_element_by_xpath("//span[contains(text(),'租户设置')]").click()
            time.sleep(1)

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 切入租户设置的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id ='bizSetTenant-tab-iframe']"))

            # 用JS的方法点击新增按钮
            button = self.driver.find_element_by_xpath("//span[text()='新增']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 切入新增租户的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id ='tenantaddWin-iframe']"))

            #输入租户编码
            self.driver.find_element_by_xpath("//input[@id='tenantCode']").send_keys("TestTenant")
            time.sleep(2)

            #输入租户名称
            self.driver.find_element_by_xpath("//input[@id='tenantName']").send_keys('自动化测试租户')
            time.sleep(2)

            #输入地址
            self.driver.find_element_by_xpath("//input[@id='address']").send_keys('浙江杭州')
            time.sleep(2)

            #输入联系人
            self.driver.find_element_by_xpath("//input[@id='contact']").send_keys('testman')
            time.sleep(2)

            # 输入联系人手机号
            self.driver.find_element_by_xpath("//input[@id='mobile']").send_keys('13888888888')
            time.sleep(2)

            # 输入固定电话
            self.driver.find_element_by_xpath("//input[@id='telno']").send_keys('057188888888')
            time.sleep(2)

            # 输入联系人邮箱
            self.driver.find_element_by_xpath("//input[@id='email']").send_keys('testman@test.com')
            time.sleep(2)

            # 输入排序
            self.driver.find_element_by_xpath("//input[@id='tenantOrder']").send_keys('12')
            time.sleep(2)

            # 输入租户中文简称
            self.driver.find_element_by_xpath("//input[@id='tenantCnshortName']").send_keys('测试租户')
            time.sleep(2)

            # 输入租户英文简称
            self.driver.find_element_by_xpath("//input[@id='tenantShortName']").send_keys('TT')
            time.sleep(2)

            # 输入租户类型
            self.temp = self.driver.find_element_by_xpath("//input[@id='combobox-input-tenantType']")
            self.temp.click()
            self.temp.send_keys("集团")
            time.sleep(1)
            self.temp.send_keys(Keys.ENTER)

            # 输入备注
            self.driver.find_element_by_xpath("//input[@id='remark']").send_keys('自动化测试租户')
            time.sleep(2)

            # 点击保存按钮
            self.driver.find_element_by_xpath("//span[text()='保存']").click()

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 用隐式等待方法等页面出现提示框
            self.driver.implicitly_wait(1800)
            self.driver.find_element_by_xpath("//span[contains(text(),'操作成功！')]")
            print("新建保存‘租户’,成功！")
            logging.info("新建保存‘租户’,成功！")
            time.sleep(3)

            # 切入租户设置的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id ='bizSetTenant-tab-iframe']"))

            # 点击查看
            # 用JS的方法点击放大镜
            button = self.driver.find_element_by_xpath("//span[@class='f-contrac-close']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 输入英文简称
            self.temp = self.driver.find_element_by_xpath("//input[@id='tenantShortName']")
            self.temp.click()
            time.sleep(1)
            self.temp.send_keys("TT")
            time.sleep(1)

            # 点击查询
            self.driver.find_element_by_xpath("//span[text()='查询']").click()
            time.sleep(3)

            # 测试‘修改租户设置’功能
            try:

                # 勾选
                self.driver.find_element_by_xpath("//div[@title='租户编码:TestTenant']/parent::*/preceding-sibling::*[1]/descendant::*[2]").click()
                time.sleep(1)

                # 点击修改按钮
                self.driver.find_element_by_xpath("//span[text()='修改']").click()
                time.sleep(1)

                # 切入修改的iframe窗体
                self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='tenanteditWin-iframe']"))

                # 修改排序的内容
                self.temp=self.driver.find_element_by_xpath("//input[@id='tenantOrder']")
                self.temp.clear()
                self.temp.send_keys("123456")
                time.sleep(2)

                # 修改备注中的内容
                self.temp =self.driver.find_element_by_xpath("//input[@id='remark']")
                self.temp.clear()
                self.temp.send_keys("自动化测试租户修改")
                time.sleep(2)

                # 点击保存按钮
                self.driver.find_element_by_xpath("//span[text()='保存']").click()

                # 退出所有iframe窗体
                self.driver.switch_to.default_content()

                # 用隐式等待方法来处理
                self.driver.implicitly_wait(60)
                self.driver.find_element_by_xpath("//span[contains(text(),'操作成功！')]")
                time.sleep(3)

                # 切入租户设置的iframe窗体
                self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id ='bizSetTenant-tab-iframe']"))

                # 打印成功
                print("修改‘租户’，成功！")
                logging.info("修改‘租户’，成功！")
                time.sleep(2)
            except Exception as err:
                # 发生其他异常时，打印异常堆栈信息
                print(traceback.print_exc())
                logging.debug("修改‘租户’，失败！" + str(traceback.format_exc()))



            # 测试‘禁用租户设置’功能
            try:
                # 勾选
                self.driver.find_element_by_xpath("//div[@title='租户编码:TestTenant']/parent::*/preceding-sibling::*[1]/descendant::*[2]").click()
                time.sleep(1)

                # 点击禁用按钮
                self.driver.find_element_by_xpath("//span[text()='禁用']").click()

                # 点击弹出框的OK键
                self.driver.find_element_by_xpath("//button[@id='f-message-webgen-0-okBnt']").click()

                # 退出所有iframe窗体
                self.driver.switch_to.default_content()

                # 用隐式等待方法等页面出现提示框
                self.driver.implicitly_wait(60)
                self.driver.find_element_by_xpath("//span[contains(text(),'操作成功')]")
                time.sleep(3)

                # 切入租户设置的iframe窗体
                self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id ='bizSetTenant-tab-iframe']"))

                # 打印成功
                print("禁用‘租户’，成功！")
                logging.info("禁用‘租户’，成功！")
                time.sleep(2)
            except Exception as err:
                # 发生其他异常时，打印异常堆栈信息
                print(traceback.print_exc())
                logging.debug("禁用‘租户’，失败！" + str(traceback.format_exc()))


            # 测试‘激活租户设置’功能
            try:
                # 勾选
                self.driver.find_element_by_xpath("//div[@title='租户编码:TestTenant']/parent::*/preceding-sibling::*[1]/descendant::*[2]").click()
                time.sleep(1)

                # 点击激活按钮
                self.driver.find_element_by_xpath("//span[text()='激活']").click()

                # 点击弹出框的OK键
                self.driver.find_element_by_xpath("//button[@id='f-message-webgen-0-okBnt']").click()

                # 退出所有iframe窗体
                self.driver.switch_to.default_content()

                # 用隐式等待方法等页面出现提示框
                self.driver.implicitly_wait(60)
                self.driver.find_element_by_xpath("//span[contains(text(),'操作成功')]")
                time.sleep(3)

                # 切入租户设置的iframe窗体
                self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id ='bizSetTenant-tab-iframe']"))

                # 打印成功
                print("激活‘租户’，成功！")
                logging.info("激活‘租户’，成功！")
                time.sleep(2)
            except Exception as err:
                # 发生其他异常时，打印异常堆栈信息
                print(traceback.print_exc())
                logging.debug("激活‘租户’，失败！" + str(traceback.format_exc()))

            logging.info("操作‘租户’，成功！")


            #测试套餐设置
            logging.info("测试‘套餐设置’")

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 点击套餐设置菜单
            self.driver.find_element_by_xpath("//span[contains(text(),'套餐设置')]").click()
            time.sleep(1)

            # 切入‘套餐设置’设置的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id ='bizSetPackage-tab-iframe']"))
            
            #新增2笔，一笔删除
            for i in range(1,3):
                # 用JS的方法点击新增按钮
                button = self.driver.find_element_by_xpath("//span[text()='新增']")
                self.driver.execute_script("$(arguments[0]).click()", button)

                # 切入新增的iframe窗体
                self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id ='packageaddWin-iframe']"))

                #输入套餐编码
                self.driver.find_element_by_xpath("//input[@id='packageCode']").send_keys("TestPack"+str(i))
                time.sleep(2)

                #输入套餐名称
                self.driver.find_element_by_xpath("//input[@id='packageName']").send_keys("自动化测试套餐"+str(i))
                time.sleep(2)

                #输入描述
                self.driver.find_element_by_xpath("//input[@id='description']").send_keys("自动化测试套餐")
                time.sleep(2)

                # 点击保存按钮
                self.driver.find_element_by_xpath("//span[text()='保存']").click()

                # 退出所有iframe窗体
                self.driver.switch_to.default_content()

                # 用隐式等待方法来处理
                self.driver.implicitly_wait(60)
                self.driver.find_element_by_xpath("//span[contains(text(),'操作成功！')]")
                print("新增‘套餐设置’，第%s笔成功！" % i)
                time.sleep(3)

                # 切入‘套餐设置’设置的iframe窗体
                self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id ='bizSetPackage-tab-iframe']"))

            # 点击查看
            # 用JS的方法点击放大镜
            button = self.driver.find_element_by_xpath("//span[@class='f-contrac-close']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 输入英文简称
            self.temp = self.driver.find_element_by_xpath("//input[@id='packageCode']")
            self.temp.click()
            time.sleep(1)
            self.temp.send_keys("Test")
            time.sleep(1)

            # 点击查询
            self.driver.find_element_by_xpath("//span[text()='查询']").click()
            time.sleep(3)

            # 测试‘修改套餐设置’功能
            try:
                # 勾选
                self.driver.find_element_by_xpath("//div[@title='套餐编码:TestPack1']/parent::*/preceding-sibling::*[1]/descendant::*[2]").click()
                time.sleep(1)

                # 点击修改按钮
                self.driver.find_element_by_xpath("//span[text()='修改']").click()
                time.sleep(1)

                # 切入修改的iframe窗体
                self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='packageeditWin-iframe']"))

                # 修改套餐名称
                self.temp=self.driver.find_element_by_xpath("//input[@id='packageName']")
                self.temp.clear()
                self.temp.send_keys("自动化测试套餐修改")
                time.sleep(2)

                # 修改描述
                self.temp =self.driver.find_element_by_xpath("//input[@id='description']")
                self.temp.clear()
                self.temp.send_keys("自动化测试套餐描述修改")
                time.sleep(2)

                # 点击保存按钮
                self.driver.find_element_by_xpath("//span[text()='保存']").click()

                # 退出所有iframe窗体
                self.driver.switch_to.default_content()

                # 用隐式等待方法来处理
                self.driver.implicitly_wait(60)
                self.driver.find_element_by_xpath("//span[contains(text(),'操作成功！')]")
                time.sleep(3)

                # 切入‘套餐设置’设置的iframe窗体
                self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id ='bizSetPackage-tab-iframe']"))

                # 打印成功
                print("修改‘套餐设置’，成功！")
                logging.info("修改‘套餐设置’，成功！")
                time.sleep(2)
            except Exception as err:
                # 发生其他异常时，打印异常堆栈信息
                print(traceback.print_exc())
                logging.debug("修改‘套餐设置’，失败！" + str(traceback.format_exc()))

            # 测试‘冻结套餐设置’功能
            try:
                # 勾选
                self.driver.find_element_by_xpath("//div[@title='套餐编码:TestPack1']/parent::*/preceding-sibling::*[1]/descendant::*[2]").click()
                time.sleep(1)

                # 点击冻结按钮
                self.driver.find_element_by_xpath("//span[text()='冻结']").click()

                # 点击弹出框的OK键
                self.driver.find_element_by_xpath("//button[@id='f-message-webgen-0-okBnt']").click()

                # 退出所有iframe窗体
                self.driver.switch_to.default_content()

                # 用隐式等待方法等页面出现提示框
                self.driver.implicitly_wait(60)
                self.driver.find_element_by_xpath("//span[contains(text(),'操作成功')]")
                time.sleep(3)

                # 切入‘套餐设置’设置的iframe窗体
                self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id ='bizSetPackage-tab-iframe']"))

                # 打印成功
                print("冻结‘套餐设置’，成功！")
                logging.info("冻结‘套餐设置’，成功！")
                time.sleep(2)
            except Exception as err:
                # 发生其他异常时，打印异常堆栈信息
                print(traceback.print_exc())
                logging.debug("冻结‘套餐设置’，失败！" + str(traceback.format_exc()))


            # 测试‘激活套餐设置’功能
            try:
                # 勾选
                self.driver.find_element_by_xpath("//div[@title='套餐编码:TestPack1']/parent::*/preceding-sibling::*[1]/descendant::*[2]").click()
                time.sleep(1)

                # 点击激活按钮
                self.driver.find_element_by_xpath("//span[text()='激活']").click()

                # 点击弹出框的OK键
                self.driver.find_element_by_xpath("//button[@id='f-message-webgen-0-okBnt']").click()

                # 退出所有iframe窗体
                self.driver.switch_to.default_content()

                # 用隐式等待方法等页面出现提示框
                self.driver.implicitly_wait(60)
                self.driver.find_element_by_xpath("//span[contains(text(),'操作成功')]")
                time.sleep(3)

                # 切入‘套餐设置’设置的iframe窗体
                self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id ='bizSetPackage-tab-iframe']"))

                # 打印成功
                print("激活‘套餐设置’，成功！")
                logging.info("激活‘套餐设置’，成功！")
                time.sleep(2)
            except Exception as err:
                # 发生其他异常时，打印异常堆栈信息
                print(traceback.print_exc())
                logging.debug("激活‘套餐设置’，失败！" + str(traceback.format_exc()))


            # 测试‘删除套餐设置’功能
            try:
                # 勾选
                self.driver.find_element_by_xpath("//div[@title='套餐编码:TestPack1']/parent::*/preceding-sibling::*[1]/descendant::*[2]").click()
                time.sleep(1)

                # 点击删除按钮
                self.driver.find_element_by_xpath("//span[text()='删除']").click()

                # 点击弹出框的OK键
                self.driver.find_element_by_xpath("//button[@id='f-message-webgen-0-okBnt']").click()

                # 退出所有iframe窗体
                self.driver.switch_to.default_content()

                # 用隐式等待方法等页面出现提示框
                self.driver.implicitly_wait(60)
                self.driver.find_element_by_xpath("//span[contains(text(),'操作成功')]")
                time.sleep(3)

                # 切入‘套餐设置’设置的iframe窗体
                self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id ='bizSetPackage-tab-iframe']"))

                # 打印成功
                print("删除‘套餐设置’，成功！")
                logging.info("删除‘套餐设置’，成功！")
                time.sleep(2)
            except Exception as err:
                # 发生其他异常时，打印异常堆栈信息
                print(traceback.print_exc())
                logging.debug("删除‘套餐设置’，失败！" + str(traceback.format_exc()))


            # 测试‘套餐设置的分配权限’功能
            try:
                # 勾选
                self.driver.find_element_by_xpath("//div[@title='套餐编码:TestPack2']/parent::*/preceding-sibling::*[1]/descendant::*[2]").click()
                time.sleep(1)

                # 点击分配权限按钮
                self.driver.find_element_by_xpath("//span[text()='分配权限']").click()
                time.sleep(3)

                # 切入‘分配权限’设置的iframe窗体
                self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id ='allocatePowerWin-iframe']"))

                # 点击展开按钮
                self.driver.find_element_by_xpath("//span[text()='展开']").click()

                # 用隐式等待方法等页面出现提示框
                self.driver.implicitly_wait(60)
                self.driver.find_element_by_xpath("//span[contains(text(),'单位管理')]")
                time.sleep(3)

                # 勾选全部菜单
                #20210629注释
                #self.driver.find_element_by_xpath("//span[@id='node4']").click()
                #20210629修改：双击勾选
                double_click("xpath","//span[@id='node4']")
                time.sleep(3)

                # 点击提交按钮
                self.driver.find_element_by_xpath("//span[text()='提交']").click()

                # 退出所有iframe窗体
                self.driver.switch_to.default_content()

                # 用隐式等待方法等页面出现提示框
                self.driver.implicitly_wait(60)
                self.driver.find_element_by_xpath("//span[contains(text(),'权限分配成功！')]")
                time.sleep(3)

                # 切入‘套餐设置’设置的iframe窗体
                self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id ='bizSetPackage-tab-iframe']"))

                #关闭权限设置页码
                self.driver.find_element_by_xpath("//div[@class='f-win-tool f-win-close']").click()
                time.sleep(3)

                # 打印成功
                print("分配权限‘套餐设置’，成功！")
                logging.info("分配权限‘套餐设置’，成功！")
                time.sleep(2)
            except Exception as err:
                # 发生其他异常时，打印异常堆栈信息
                print(traceback.print_exc())
                logging.debug("分配权限‘套餐设置’，失败！" + str(traceback.format_exc()))

            logging.info("操作‘套餐设置’，成功！")



            #测试协议设置
            logging.info("测试‘协议设置’")

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 点击套餐设置菜单
            self.driver.find_element_by_xpath("//span[contains(text(),'协议设置')]").click()
            time.sleep(1)

            # 切入‘协议设置’设置的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id ='bizSetContract-tab-iframe']"))

            # 新增2笔，一笔删除
            for i in range(1, 3):
                # 用JS的方法点击新增按钮
                button = self.driver.find_element_by_xpath("//span[text()='新增']")
                self.driver.execute_script("$(arguments[0]).click()", button)

                # 切入新增的iframe窗体
                self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id ='contractaddWin-iframe']"))

                # 输入租户名称
                self.temp = self.driver.find_element_by_xpath("//input[@id='combobox-input-tenantid']")
                self.temp.click()
                self.temp.send_keys("自动化测试租户")
                time.sleep(1)
                self.temp.send_keys(Keys.ARROW_DOWN)
                self.temp.send_keys(Keys.ENTER)
                time.sleep(1)

                # 输入套餐名称
                self.temp = self.driver.find_element_by_xpath("//input[@id='combobox-input-packageId']")
                self.temp.click()
                self.temp.send_keys("自动化测试套餐2")
                time.sleep(1)
                self.temp.send_keys(Keys.ARROW_DOWN)
                self.temp.send_keys(Keys.ENTER)
                time.sleep(1)

                # 设置时间变量存储
                temp1 = time.strftime("%Y-%m-%d")
                today = date.today()
                temp2 = today + timedelta(days=3650)

                # 输入生效日期
                # self.driver.find_element_by_xpath("//input[@id='effectiveDate-input']").send_keys(str(temp1))
                # time.sleep(2)
                self.temp = self.driver.find_element_by_xpath("//input[@id='effectiveDate-input']")
                self.temp.click()
                time.sleep(1)
                self.temp.send_keys(str(temp1))
                time.sleep(2)

                # 输入失效日期
                # self.driver.find_element_by_xpath("//input[@id='expiryDate-input']").send_keys(str(temp2))
                # time.sleep(2)
                self.temp = self.driver.find_element_by_xpath("//input[@id='expiryDate-input']")
                self.temp.click()
                time.sleep(1)
                self.temp.send_keys(str(temp2))
                time.sleep(2)

                # 输入描述
                self.driver.find_element_by_xpath("//input[@id='description']").send_keys("自动化测试协议设置")
                time.sleep(2)

                # 点击保存按钮
                self.driver.find_element_by_xpath("//span[text()='保存']").click()

                # 退出所有iframe窗体
                self.driver.switch_to.default_content()

                # 用隐式等待方法来处理
                self.driver.implicitly_wait(60)
                self.driver.find_element_by_xpath("//span[contains(text(),'操作成功！')]")
                print("新增‘协议设置’，第%s笔成功！" % i)
                time.sleep(3)

                # 切入‘协议设置’设置的iframe窗体
                self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id ='bizSetContract-tab-iframe']"))

                #如果i等于1，就删除新建的协议设置
                if i==1:
                    # 勾选
                    self.driver.find_element_by_xpath("//div[@title='租户名称:自动化测试租户']/parent::*/preceding-sibling::*[1]/descendant::*[2]").click()
                    time.sleep(1)

                    # 点击删除按钮
                    self.driver.find_element_by_xpath("//span[text()='删除']").click()

                    # 点击弹出框的OK键
                    self.driver.find_element_by_xpath("//button[@id='f-message-webgen-0-okBnt']").click()

                    # 退出所有iframe窗体
                    self.driver.switch_to.default_content()

                    # 用隐式等待方法等页面出现提示框
                    self.driver.implicitly_wait(60)
                    self.driver.find_element_by_xpath("//span[contains(text(),'操作成功')]")
                    print("删除‘协议设置’，成功！")
                    time.sleep(3)

                    # 切入‘协议设置’设置的iframe窗体
                    self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id ='bizSetContract-tab-iframe']"))

            # 点击查看
            # 用JS的方法点击放大镜
            button = self.driver.find_element_by_xpath("//span[@class='f-contrac-close']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 输入租户名称
            self.temp = self.driver.find_element_by_xpath("//input[@id='tenantName']")
            self.temp.click()
            time.sleep(1)
            self.temp.send_keys("自动化测试租户")
            time.sleep(1)

            # 点击查询
            self.driver.find_element_by_xpath("//span[text()='查询']").click()
            time.sleep(3)

            # 测试‘修改协议设置’功能
            try:
                # 勾选
                self.driver.find_element_by_xpath("//div[@title='租户名称:自动化测试租户']/parent::*/preceding-sibling::*[1]/descendant::*[2]").click()
                time.sleep(1)

                # 点击修改按钮
                self.driver.find_element_by_xpath("//span[text()='修改']").click()
                time.sleep(1)

                # 切入修改的iframe窗体
                self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='contracteditWin-iframe']"))

                # 修改描述
                self.temp=self.driver.find_element_by_xpath("//input[@id='description']")
                self.temp.clear()
                self.temp.send_keys("自动化测试协议设置描述修改")
                time.sleep(2)

                # 点击保存按钮
                self.driver.find_element_by_xpath("//span[text()='保存']").click()

                # 退出所有iframe窗体
                self.driver.switch_to.default_content()

                # 用隐式等待方法来处理
                self.driver.implicitly_wait(60)
                self.driver.find_element_by_xpath("//span[contains(text(),'操作成功！')]")
                time.sleep(3)

                # 打印成功
                print("修改‘协议设置’，成功！")
                logging.info("修改‘协议设置’，成功！")
                time.sleep(2)
            except Exception as err:
                # 发生其他异常时，打印异常堆栈信息
                print(traceback.print_exc())
                logging.debug("修改‘协议设置’，失败！" + str(traceback.format_exc()))

            logging.info("操作‘协议设置’，成功！")

            
            # 测试‘租户设置--功能更新’功能
            logging.info("测试‘租户设置--功能更新’功能")

            # 点击租户设置菜单
            self.driver.find_element_by_xpath("//span[contains(text(),'租户设置')]").click()
            time.sleep(1)

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 切入租户设置的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id ='bizSetTenant-tab-iframe']"))

            # 勾选
            self.driver.find_element_by_xpath("//div[@title='租户编码:TestTenant']/parent::*/preceding-sibling::*[1]/descendant::*[2]").click()
            time.sleep(1)

            # 点击功能更新按钮
            self.driver.find_element_by_xpath("//span[text()='功能更新']").click()

            # 点击弹出框的OK键
            self.driver.find_element_by_xpath("//button[@id='f-message-webgen-0-okBnt']").click()

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 用隐式等待方法等页面出现提示框
            self.driver.implicitly_wait(600)
            self.driver.find_element_by_xpath("//span[contains(text(),'操作成功')]")
            time.sleep(3)

            # 打印成功
            logging.info("操作‘租户设置--功能更新’，成功！")
            print("操作‘租户设置--功能更新’，成功！")


            # 点击页面退出按钮
            self.driver.find_element_by_xpath("//a[contains(.,'退出')]").click()
            time.sleep(1)

            # 点击退出弹窗的'Yes'按钮
            self.driver.find_element_by_xpath("//button[contains(.,'Yes')]").click()
            time.sleep(1)

            #关闭浏览器
            self.driver.quit()
            time.sleep(2)
                        
            #启动浏览器
            self.driver = get("chrome")
            

            logging.info("测试新租户的‘组织’的功能")
            #通过登陆封装函数，以‘SysAdmin’登陆租户‘自动化测试租户’，创建‘组织’
            login( url, "SysAdmin", "88888888","自动化测试租户")

            #修改密码
            # 切入修改密码的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id ='modifyWin2-iframe']"))

            #输入当前密码
            self.driver.find_element_by_xpath("//input[@id='oldPwd']").send_keys("88888888")
            time.sleep(2)

            #输入新的密码
            self.driver.find_element_by_xpath("//input[@id='newPwd']").send_keys("fingard@1")
            time.sleep(2)

            #输入确认输入
            self.driver.find_element_by_xpath("//input[@id='newPwdre']").send_keys("fingard@1")
            time.sleep(2)

            # 点击确定按钮
            self.driver.find_element_by_xpath("//span[text()='确定']").click()
            #time.sleep(2)

            # 点击弹出框的OK键
            #self.driver.find_element_by_xpath("//button[@id='f-message-webgen-0-okBnt']").click()
            time.sleep(2)

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()



            # 登陆测试用
            login( url, "SysAdmin", "fingard@1", "自动化测试租户")

            #点击系统菜单
            self.driver.find_element_by_xpath("//span[contains(text(),'系统菜单')]").click()
            time.sleep(1)
            #点击用户管理菜单
            self.driver.find_element_by_xpath("//span[contains(text(),'用户管理')]").click()
            time.sleep(1)


            # 测试‘组织类别设置’
            logging.info("测试‘组织类别设置’")
            # 点击菜单
            self.driver.find_element_by_xpath("//span[contains(text(),'组织类别设置')]").click()
            time.sleep(1)

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 切入‘组织类别设置’的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id ='bizOrgTypeSet-tab-iframe']"))

            # 新增2笔，一笔删除
            for i in range(1, 3):
                # 用JS的方法点击新增按钮
                button = self.driver.find_element_by_xpath("//span[text()='新增']")
                self.driver.execute_script("$(arguments[0]).click()", button)

                # 切入新增的iframe窗体
                self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id ='addWin-iframe']"))

                # 输入代码
                self.driver.find_element_by_xpath("//input[@id='code']").send_keys("TestOrgType")
                time.sleep(2)

                # 输入名称
                self.driver.find_element_by_xpath("//input[@id='name']").send_keys("测试组织类别设置")
                time.sleep(2)

                # 输入描述
                self.driver.find_element_by_xpath("//textarea[@id='description']").send_keys("自动化测试组织类别设置描述")
                time.sleep(2)

                # 点击保存按钮
                self.driver.find_element_by_xpath("//span[text()='保存']").click()

                # 退出所有iframe窗体
                self.driver.switch_to.default_content()

                # 用隐式等待方法来处理
                self.driver.implicitly_wait(60)
                self.driver.find_element_by_xpath("//span[contains(text(),'操作成功！')]")
                print("新增‘组织类别设置’，第%s笔成功！" % i)
                time.sleep(3)

                # 切入‘组织类别设置’的iframe窗体
                self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id ='bizOrgTypeSet-tab-iframe']"))

                # 如果i等于1，就删除新建的协议设置
                if i == 1:
                    # 勾选
                    self.driver.find_element_by_xpath("//div[@title='代码:TestOrgType']/parent::*/preceding-sibling::*[1]/descendant::*[2]").click()
                    time.sleep(1)

                    # 点击删除按钮
                    self.driver.find_element_by_xpath("//span[text()='删除']").click()

                    # 点击弹出框的OK键
                    self.driver.find_element_by_xpath("//button[@id='f-message-webgen-0-okBnt']").click()

                    # 退出所有iframe窗体
                    self.driver.switch_to.default_content()

                    # 用隐式等待方法等页面出现提示框
                    self.driver.implicitly_wait(60)
                    self.driver.find_element_by_xpath("//span[contains(text(),'操作成功')]")
                    print("删除‘组织类别设置’，成功！")
                    time.sleep(3)

                    # 切入‘组织类别设置’的iframe窗体
                    self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id ='bizOrgTypeSet-tab-iframe']"))

            # 点击查看
            # 用JS的方法点击放大镜
            button = self.driver.find_element_by_xpath("//span[@class='f-contrac-close']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 输入‘组织类别设置’代码
            self.temp = self.driver.find_element_by_xpath("//input[@id='code']")
            self.temp.click()
            time.sleep(1)
            self.temp.send_keys("TestOrgType")
            time.sleep(1)

            # 点击查询
            self.driver.find_element_by_xpath("//span[text()='查询']").click()
            time.sleep(3)

            # 测试修改‘组织类别设置’功能
            try:
                # 勾选
                self.driver.find_element_by_xpath("//div[@title='代码:TestOrgType']/parent::*/preceding-sibling::*[1]/descendant::*[2]").click()
                time.sleep(1)

                # 点击修改按钮
                self.driver.find_element_by_xpath("//span[text()='修改']").click()
                time.sleep(1)

                # 切入修改的iframe窗体
                self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='modWin-iframe']"))

                # 修改描述
                self.temp=self.driver.find_element_by_xpath("//textarea[@id='description']")
                self.temp.clear()
                self.temp.send_keys("自动化测试组织类别设置描述修改")
                time.sleep(2)

                # 点击保存按钮
                self.driver.find_element_by_xpath("//span[text()='保存']").click()

                # 退出所有iframe窗体
                self.driver.switch_to.default_content()

                # 用隐式等待方法来处理
                self.driver.implicitly_wait(60)
                self.driver.find_element_by_xpath("//span[contains(text(),'操作成功！')]")
                time.sleep(3)

                # 打印成功
                print("修改‘组织类别设置’，成功！")
                logging.info("修改‘组织类别设置’，成功！")
                time.sleep(2)
            except Exception as err:
                # 发生其他异常时，打印异常堆栈信息
                print(traceback.print_exc())
                logging.debug("修改‘组织类别设置’，失败！" + str(traceback.format_exc()))

            # 用JS的方法关闭当前的页面
            button = self.driver.find_element_by_xpath("//a[@title='组织类别设置']/child::*[1]")
            self.driver.execute_script("$(arguments[0]).click()", button)

            logging.info("操作‘组织类别设置’，成功！")



            # 测试‘组织分类设置’
            logging.info("测试‘组织分类设置’")
            # 点击菜单
            self.driver.find_element_by_xpath("//span[contains(text(),'组织分类设置')]").click()
            time.sleep(1)

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 切入‘组织分类设置’的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id ='bizOrgClassSet-tab-iframe']"))

            # 新增2笔，一笔删除
            for i in range(1, 3):
                # 用JS的方法点击新增按钮
                button = self.driver.find_element_by_xpath("//span[text()='新增']")
                self.driver.execute_script("$(arguments[0]).click()", button)

                # 切入新增的iframe窗体
                self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id ='addWin-iframe']"))

                # 输入代码
                self.driver.find_element_by_xpath("//input[@id='code']").send_keys("TestOrgClass")
                time.sleep(2)

                # 输入名称
                self.driver.find_element_by_xpath("//input[@id='name']").send_keys("测试组织分类设置")
                time.sleep(2)

                # 输入描述
                self.driver.find_element_by_xpath("//textarea[@id='description']").send_keys("自动化测试组织分类设置描述")
                time.sleep(2)

                # 点击保存按钮
                self.driver.find_element_by_xpath("//span[text()='保存']").click()

                # 退出所有iframe窗体
                self.driver.switch_to.default_content()

                # 用隐式等待方法来处理
                self.driver.implicitly_wait(60)
                self.driver.find_element_by_xpath("//span[contains(text(),'操作成功！')]")
                print("新增‘组织分类设置’，第%s笔成功！" % i)
                time.sleep(3)

                # 切入‘组织分类设置’的iframe窗体
                self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id ='bizOrgClassSet-tab-iframe']"))

                # 如果i等于1，就删除新建的协议设置
                if i == 1:
                    # 勾选
                    self.driver.find_element_by_xpath("//div[@title='代码:TestOrgClass']/parent::*/preceding-sibling::*[1]/descendant::*[2]").click()
                    time.sleep(1)

                    # 点击删除按钮
                    self.driver.find_element_by_xpath("//span[text()='删除']").click()

                    # 点击弹出框的OK键
                    self.driver.find_element_by_xpath("//button[@id='f-message-webgen-0-okBnt']").click()

                    # 退出所有iframe窗体
                    self.driver.switch_to.default_content()

                    # 用隐式等待方法等页面出现提示框
                    self.driver.implicitly_wait(60)
                    self.driver.find_element_by_xpath("//span[contains(text(),'操作成功')]")
                    print("删除‘组织分类设置’，成功！")
                    time.sleep(3)

                    # 切入‘组织分类设置’的iframe窗体
                    self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id ='bizOrgClassSet-tab-iframe']"))

            # 点击查看
            # 用JS的方法点击放大镜
            button = self.driver.find_element_by_xpath("//span[@class='f-contrac-close']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 输入‘组织分类设置’代码
            self.temp = self.driver.find_element_by_xpath("//input[@id='code']")
            self.temp.click()
            time.sleep(1)
            self.temp.send_keys("TestOrgClass")
            time.sleep(1)

            # 点击查询
            self.driver.find_element_by_xpath("//span[text()='查询']").click()
            time.sleep(3)

            # 测试修改‘组织分类设置’功能
            try:
                # 勾选
                self.driver.find_element_by_xpath("//div[@title='代码:TestOrgClass']/parent::*/preceding-sibling::*[1]/descendant::*[2]").click()
                time.sleep(1)

                # 点击修改按钮
                self.driver.find_element_by_xpath("//span[text()='修改']").click()
                time.sleep(1)

                # 切入修改的iframe窗体
                self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='modWin-iframe']"))

                # 修改描述
                self.temp=self.driver.find_element_by_xpath("//textarea[@id='description']")
                self.temp.clear()
                self.temp.send_keys("自动化测试组织分类设置描述修改")
                time.sleep(2)

                # 点击保存按钮
                self.driver.find_element_by_xpath("//span[text()='保存']").click()

                # 退出所有iframe窗体
                self.driver.switch_to.default_content()

                # 用隐式等待方法来处理
                self.driver.implicitly_wait(60)
                self.driver.find_element_by_xpath("//span[contains(text(),'操作成功！')]")
                time.sleep(3)

                # 打印成功
                print("修改‘组织分类设置’，成功！")
                logging.info("修改‘组织分类设置’，成功！")
                time.sleep(2)
            except Exception as err:
                # 发生其他异常时，打印异常堆栈信息
                print(traceback.print_exc())
                logging.debug("修改‘组织分类设置’，失败！" + str(traceback.format_exc()))

            # 用JS的方法关闭当前的页面
            button = self.driver.find_element_by_xpath("//a[@title='组织分类设置']/child::*[1]")
            self.driver.execute_script("$(arguments[0]).click()", button)

            logging.info("操作‘组织分类设置’，成功！")


            # 测试‘组织机构设置’
            logging.info("测试‘组织机构设置’")
            # 点击菜单
            self.driver.find_element_by_xpath("//span[contains(text(),'组织机构设置')]").click()
            time.sleep(1)

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 切入‘组织机构设置’的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id ='bizOrgSet-tab-iframe']"))

            # 新增2笔，一笔删除
            for i in range(1, 3):
                # 用JS的方法点击新增按钮
                button = self.driver.find_element_by_xpath("//span[text()='新增']")
                self.driver.execute_script("$(arguments[0]).click()", button)

                # 切入新增的iframe窗体
                self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id ='orgaddWin-iframe']"))

                # 输入组织编码
                self.driver.find_element_by_xpath("//input[@id='org_code']").send_keys("TestOrgSet")
                time.sleep(2)

                # 输入组织名称
                self.driver.find_element_by_xpath("//input[@id='org_name']").send_keys("测试组织机构设置")
                time.sleep(2)

                #输入组织属性
                self.temp = self.driver.find_element_by_xpath("//input[@id='combobox-input-org_cate']")
                self.temp.click()
                self.temp.clear()
                time.sleep(1)
                self.temp.send_keys("上市公司")
                time.sleep(1)
                self.temp.send_keys(Keys.ARROW_DOWN)
                self.temp.send_keys(Keys.ENTER)
                time.sleep(1)

                #输入组织级别
                self.temp = self.driver.find_element_by_xpath("//input[@id='combobox-input-org_level']")
                self.temp.click()
                self.temp.clear()
                time.sleep(1)
                self.temp.send_keys("集团")
                time.sleep(1)
                self.temp.send_keys(Keys.ARROW_DOWN)
                self.temp.send_keys(Keys.ENTER)
                time.sleep(1)

                #输入上级组织
                self.temp = self.driver.find_element_by_xpath("//input[@id='combobox-input-parent_id']")
                self.temp.click()
                self.temp.clear()
                time.sleep(1)
                self.temp.send_keys("TestTenant-自动化测试租户")
                time.sleep(1)
                self.temp.send_keys(Keys.ARROW_DOWN)
                self.temp.send_keys(Keys.ENTER)
                time.sleep(1)

                #输入主管组织
                self.temp = self.driver.find_element_by_xpath("//input[@id='combobox-input-manage_id']")
                self.temp.click()
                self.temp.clear()
                time.sleep(1)
                self.temp.send_keys("TestTenant-自动化测试租户")
                time.sleep(1)
                self.temp.send_keys(Keys.ARROW_DOWN)
                self.temp.send_keys(Keys.ENTER)
                time.sleep(1)

                # 输入组织简称
                self.driver.find_element_by_xpath("//input[@id='shortorgname']").send_keys("测试机构")
                time.sleep(2)

                #输入组织类别
                self.temp = self.driver.find_element_by_xpath("//input[@id='combobox-input-ext_id']")
                self.temp.click()
                self.temp.clear()
                time.sleep(1)
                self.temp.send_keys(Keys.ARROW_DOWN)
                self.temp.send_keys(Keys.ENTER)
                time.sleep(1)

                #输入统计组织
                self.temp = self.driver.find_element_by_xpath("//input[@id='combobox-input-statistical_id']")
                self.temp.click()
                self.temp.clear()
                time.sleep(1)
                self.temp.send_keys("TestTenant-自动化测试租户")
                time.sleep(1)
                self.temp.send_keys(Keys.ARROW_DOWN)
                self.temp.send_keys(Keys.ENTER)
                time.sleep(1)

                # 输入英文名称
                self.driver.find_element_by_xpath("//input[@id='english_name']").send_keys("OrgSet")
                time.sleep(2)

                #输入组织分类
                self.temp = self.driver.find_element_by_xpath("//input[@id='combobox-input-org_class']")
                self.temp.click()
                self.temp.clear()
                time.sleep(1)
                self.temp.send_keys("TestOrgClass-测试组织分类设置")
                time.sleep(1)
                self.temp.send_keys(Keys.ARROW_DOWN)
                self.temp.send_keys(Keys.ENTER)
                time.sleep(1)

                # 输入备注
                self.driver.find_element_by_xpath("//textarea[@id='remark']").send_keys("自动化测试组织机构设置备注")
                time.sleep(2)

                # 点击保存按钮
                self.driver.find_element_by_xpath("//span[text()='保存']").click()

                # 退出所有iframe窗体
                self.driver.switch_to.default_content()

                # 用隐式等待方法来处理
                self.driver.implicitly_wait(60)
                self.driver.find_element_by_xpath("//span[contains(text(),'操作成功！')]")
                print("新增‘组织机构设置’，第%s笔成功！" % i)
                time.sleep(3)

                # 切入‘组织机构设置’的iframe窗体
                self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id ='bizOrgSet-tab-iframe']"))

                # 如果i等于1，就删除新建的
                if i == 1:
                    # 勾选
                    self.driver.find_element_by_xpath("//div[@title='组织编码:TestOrgSet']/parent::*/preceding-sibling::*[1]/descendant::*[2]").click()
                    #self.driver.find_element_by_xpath("//div[@title='组织编码:TestOrgSet']/parent::*/preceding-sibling::*[2]/descendant::*[2]").click()
                    time.sleep(1)

                    # 点击删除按钮
                    self.driver.find_element_by_xpath("//span[text()='删除']").click()

                    # 点击弹出框的OK键
                    self.driver.find_element_by_xpath("//button[@id='f-message-webgen-0-okBnt']").click()

                    # 退出所有iframe窗体
                    self.driver.switch_to.default_content()

                    # 用隐式等待方法等页面出现提示框
                    self.driver.implicitly_wait(60)
                    self.driver.find_element_by_xpath("//span[contains(text(),'操作成功')]")
                    print("删除‘组织机构设置’，成功！")
                    time.sleep(3)

                    # 切入‘组织机构设置’的iframe窗体
                    self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id ='bizOrgSet-tab-iframe']"))

            # 点击查看
            # 用JS的方法点击放大镜
            button = self.driver.find_element_by_xpath("//span[@class='f-contrac-close']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 输入‘组织分类设置’代码
            self.temp = self.driver.find_element_by_xpath("//input[@id='code']")
            self.temp.click()
            time.sleep(1)
            self.temp.send_keys("TestOrgSet")
            time.sleep(1)

            # 点击查询
            self.driver.find_element_by_xpath("//span[text()='查询']").click()
            time.sleep(3)

            # 测试修改‘组织机构设置’功能
            try:
                # 勾选
                self.driver.find_element_by_xpath("//div[@title='组织编码:TestOrgSet']/parent::*/preceding-sibling::*[1]/descendant::*[2]").click()
                #self.driver.find_element_by_xpath("//div[@title='组织编码:TestOrgSet']/parent::*/preceding-sibling::*[2]/descendant::*[2]").click()
                time.sleep(1)

                # 点击修改按钮
                self.driver.find_element_by_xpath("//span[text()='修改']").click()
                time.sleep(1)

                # 切入修改的iframe窗体
                self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='orgeditWin-iframe']"))

                # 修改备注
                self.temp = self.driver.find_element_by_xpath("//textarea[@id='remark']")
                self.temp.clear()
                self.temp.send_keys("自动化测试组织机构设置备注修改")
                time.sleep(2)

                # 点击保存按钮
                self.driver.find_element_by_xpath("//span[text()='保存']").click()

                # 退出所有iframe窗体
                self.driver.switch_to.default_content()

                # 用隐式等待方法来处理
                self.driver.implicitly_wait(60)
                self.driver.find_element_by_xpath("//span[contains(text(),'操作成功！')]")
                time.sleep(3)

                # 切入‘组织机构设置’的iframe窗体
                self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id ='bizOrgSet-tab-iframe']"))

                # 打印成功
                print("修改‘组织机构设置’，成功！")
                logging.info("修改‘组织机构设置’，成功！")
                time.sleep(2)
            except Exception as err:
                # 发生其他异常时，打印异常堆栈信息
                print(traceback.print_exc())
                logging.debug("修改‘组织机构设置’，失败！" + str(traceback.format_exc()))


            # 测试注销‘组织机构设置’功能
            try:
                # 勾选
                self.driver.find_element_by_xpath("//div[@title='组织编码:TestOrgSet']/parent::*/preceding-sibling::*[1]/descendant::*[2]").click()
                #self.driver.find_element_by_xpath("//div[@title='组织编码:TestOrgSet']/parent::*/preceding-sibling::*[2]/descendant::*[2]").click()
                time.sleep(1)

                # 点击注销按钮
                self.driver.find_element_by_xpath("//span[text()='注销']").click()

                # 点击弹出框的OK键
                self.driver.find_element_by_xpath("//button[@id='f-message-webgen-0-okBnt']").click()

                # 退出所有iframe窗体
                self.driver.switch_to.default_content()

                # 用隐式等待方法等页面出现提示框
                self.driver.implicitly_wait(60)
                self.driver.find_element_by_xpath("//span[contains(text(),'操作成功')]")
                time.sleep(3)

                # 切入‘组织机构设置’的iframe窗体
                self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id ='bizOrgSet-tab-iframe']"))

                # 打印成功
                print("注销‘组织机构设置’，成功！")
                logging.info("注销‘组织机构设置’，成功！")
                time.sleep(2)
            except Exception as err:
                # 发生其他异常时，打印异常堆栈信息
                print(traceback.print_exc())
                logging.debug("注销‘组织机构设置’，失败！" + str(traceback.format_exc()))


            # 测试激活‘组织机构设置’功能
            try:
                # 勾选
                self.driver.find_element_by_xpath("//div[@title='组织编码:TestOrgSet']/parent::*/preceding-sibling::*[1]/descendant::*[2]").click()
                #self.driver.find_element_by_xpath("//div[@title='组织编码:TestOrgSet']/parent::*/preceding-sibling::*[2]/descendant::*[2]").click()
                time.sleep(1)

                # 点击激活按钮
                self.driver.find_element_by_xpath("//span[text()='激活']").click()

                # 点击弹出框的OK键
                self.driver.find_element_by_xpath("//button[@id='f-message-webgen-0-okBnt']").click()

                # 退出所有iframe窗体
                self.driver.switch_to.default_content()

                # 用隐式等待方法等页面出现提示框
                self.driver.implicitly_wait(60)
                self.driver.find_element_by_xpath("//span[contains(text(),'操作成功')]")
                time.sleep(3)

                # 打印成功
                print("激活‘组织机构设置’，成功！")
                logging.info("激活‘组织机构设置’，成功！")
                time.sleep(2)
            except Exception as err:
                # 发生其他异常时，打印异常堆栈信息
                print(traceback.print_exc())
                logging.debug("激活‘组织机构设置’，失败！" + str(traceback.format_exc()))


            # 用JS的方法关闭当前的页面
            button = self.driver.find_element_by_xpath("//a[@title='组织机构设置']/child::*[1]")
            self.driver.execute_script("$(arguments[0]).click()", button)

            logging.info("操作‘组织机构设置’，成功！")

            # 点击页面退出按钮
            self.driver.find_element_by_xpath("//a[contains(.,'退出')]").click()
            time.sleep(1)

            # 点击退出弹窗的'Yes'按钮
            self.driver.find_element_by_xpath("//button[contains(.,'Yes')]").click()
            time.sleep(1)

            #关闭浏览器
            self.driver.quit()
            time.sleep(2)


            #启动浏览器
            self.driver = get("chrome")

            logging.info("测试新租户的创建‘用户’的功能")
            #通过登陆封装函数，以‘UserAdmin’登陆租户‘自动化测试租户’，创建‘组织’
            login( url, "UserAdmin", "88888888","自动化测试租户")

            #修改密码
            # 切入修改密码的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id ='modifyWin2-iframe']"))

            #输入当前密码
            self.driver.find_element_by_xpath("//input[@id='oldPwd']").send_keys("88888888")
            time.sleep(2)

            #输入新的密码
            self.driver.find_element_by_xpath("//input[@id='newPwd']").send_keys("fingard@1")
            time.sleep(2)

            #输入确认输入
            self.driver.find_element_by_xpath("//input[@id='newPwdre']").send_keys("fingard@1")
            time.sleep(2)

            # 点击确定按钮
            self.driver.find_element_by_xpath("//span[text()='确定']").click()
            #time.sleep(2)

            # 点击弹出框的OK键
            #self.driver.find_element_by_xpath("//button[@id='f-message-webgen-0-okBnt']").click()
            time.sleep(2)

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()


            # 登陆测试用
            #login( url, "UserAdmin", "fingard@1", "自动化测试租户")

            # 测试‘用户设置’
            logging.info("测试‘用户设置’")

            #点击系统菜单
            self.driver.find_element_by_xpath("//span[contains(text(),'系统菜单')]").click()
            time.sleep(1)
            #点击用户管理菜单
            self.driver.find_element_by_xpath("//span[contains(text(),'用户管理')]").click()
            time.sleep(1)
            # 点击用户设置菜单
            self.driver.find_element_by_xpath("//span[contains(text(),'用户设置')]").click()
            time.sleep(1)

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 切入‘用户设置’的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id ='bizSetUser-tab-iframe']"))

            # 用JS的方法点击新增按钮
            button = self.driver.find_element_by_xpath("//span[text()='新增']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 切入新增的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id ='custButtonWin1-iframe']"))

            # 输入用户编号
            self.driver.find_element_by_xpath("//input[@id='userId']").send_keys("TestUser")
            time.sleep(2)

            # 输入用户姓名
            self.driver.find_element_by_xpath("//input[@id='userName']").send_keys("测试用户")
            time.sleep(2)

            # 输入所属组织
            self.temp = self.driver.find_element_by_xpath("//input[@id='combobox-input-orgId']")
            self.temp.click()
            self.temp.send_keys("TestOrgSet-测试组织机构设置")
            time.sleep(1)
            self.temp.send_keys(Keys.ARROW_DOWN)
            self.temp.send_keys(Keys.ENTER)
            time.sleep(1)

            # 输入排序
            self.driver.find_element_by_xpath("//input[@id='userOrder-input']").send_keys("123")
            time.sleep(2)

            # 输入登录方式
            self.temp = self.driver.find_element_by_xpath("//input[@id='combobox-input-extField4']")
            self.temp.click()
            self.temp.send_keys("系统密码")
            time.sleep(1)
            self.temp.send_keys(Keys.ENTER)
            time.sleep(1)

            # 输入联系电话
            self.driver.find_element_by_xpath("//input[@id='mobile']").send_keys("13888888888")
            time.sleep(2)

            # 输入邮件地址
            self.driver.find_element_by_xpath("//input[@id='email']").send_keys("testman@test.com")
            time.sleep(2)

            # 输入证件类型
            self.temp = self.driver.find_element_by_xpath("//input[@id='combobox-input-c_identitytype']")
            self.temp.click()
            self.temp.send_keys("身份证")
            time.sleep(1)
            self.temp.send_keys(Keys.ENTER)
            time.sleep(1)

            # 输入证件号码
            self.driver.find_element_by_xpath("//input[@id='c_identityno']").send_keys("12345678901234")
            time.sleep(2)

            # 输入资格证书
            self.driver.find_element_by_xpath("//input[@id='c_credentials']").send_keys("12345678901234")
            time.sleep(2)

            # 输入VPNKeyId
            self.driver.find_element_by_xpath("//input[@id='extField5']").send_keys("12345678901234")
            time.sleep(2)

            # 输入备注
            self.driver.find_element_by_xpath("//textarea[@id='remark']").send_keys("自动化测试用户设置")
            time.sleep(2)

            # 点击保存按钮
            self.driver.find_element_by_xpath("//span[text()='保存']").click()

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 用隐式等待方法来处理
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath("//span[contains(text(),'操作成功！')]")
            print("新增‘用户’，成功！" )
            time.sleep(3)

            # 切入‘用户设置’的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id ='bizSetUser-tab-iframe']"))

            # 点击查看
            # 用JS的方法点击放大镜
            button = self.driver.find_element_by_xpath("//span[@class='f-contrac-close']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 输入用户编号
            self.temp = self.driver.find_element_by_xpath("//input[@id='userIdlrlike']")
            self.temp.click()
            time.sleep(1)
            self.temp.send_keys("TestUser")
            time.sleep(1)

            # 点击查询
            self.driver.find_element_by_xpath("//span[text()='查询']").click()
            time.sleep(3)

            # 测试修改‘用户’功能
            try:
                # 勾选
                self.driver.find_element_by_xpath("//div[@title='用户编号:TestUser']/parent::*/preceding-sibling::*[1]/descendant::*[2]").click()
                time.sleep(1)

                # 点击修改按钮
                self.driver.find_element_by_xpath("//span[text()='修改']").click()
                time.sleep(1)

                # 切入修改的iframe窗体
                self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='allocateAuthorUserPowerWin-iframe']"))

                # 修改排序
                self.temp=self.driver.find_element_by_xpath("//input[@id='userOrder-input']")
                self.temp.clear()
                self.temp.send_keys("123456")
                time.sleep(2)

                # 修改备注
                self.temp=self.driver.find_element_by_xpath("//textarea[@id='remark']")
                self.temp.clear()
                self.temp.send_keys("自动化测试用户设置备注修改")
                time.sleep(2)

                # 点击保存按钮
                self.driver.find_element_by_xpath("//span[text()='保存']").click()

                # 退出所有iframe窗体
                self.driver.switch_to.default_content()

                # 用隐式等待方法来处理
                self.driver.implicitly_wait(60)
                self.driver.find_element_by_xpath("//span[contains(text(),'操作成功！')]")
                time.sleep(3)

                # 切入‘用户设置’的iframe窗体
                self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id ='bizSetUser-tab-iframe']"))

                # 打印成功
                print("修改‘用户设置’，成功！")
                logging.info("修改‘用户设置’，成功！")
                time.sleep(2)
            except Exception as err:
                # 发生其他异常时，打印异常堆栈信息
                print(traceback.print_exc())
                logging.debug("修改‘用户设置’，失败！" + str(traceback.format_exc()))


            # 测试注销‘用户’功能
            try:
                # 勾选
                self.driver.find_element_by_xpath("//div[@title='用户编号:TestUser']/parent::*/preceding-sibling::*[1]/descendant::*[2]").click()
                time.sleep(1)

                # 点击注销按钮
                self.driver.find_element_by_xpath("//span[text()='注销']").click()

                # 点击弹出框的OK键
                self.driver.find_element_by_xpath("//button[@id='f-message-webgen-0-okBnt']").click()

                # 退出所有iframe窗体
                self.driver.switch_to.default_content()

                # 用隐式等待方法等页面出现提示框
                self.driver.implicitly_wait(60)
                self.driver.find_element_by_xpath("//span[contains(text(),'操作成功')]")
                time.sleep(3)

                # 切入‘用户设置’的iframe窗体
                self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id ='bizSetUser-tab-iframe']"))

                # 打印成功
                print("注销‘用户’，成功！")
                logging.info("注销‘用户’，成功！")
                time.sleep(2)
            except Exception as err:
                # 发生其他异常时，打印异常堆栈信息
                print(traceback.print_exc())
                logging.debug("注销‘用户’，失败！" + str(traceback.format_exc()))


            # 测试激活‘用户’功能
            try:
                # 勾选
                self.driver.find_element_by_xpath("//div[@title='用户编号:TestUser']/parent::*/preceding-sibling::*[1]/descendant::*[2]").click()
                time.sleep(1)

                # 点击激活按钮
                self.driver.find_element_by_xpath("//span[text()='激活']").click()

                # 点击弹出框的OK键
                self.driver.find_element_by_xpath("//button[@id='f-message-webgen-0-okBnt']").click()

                # 退出所有iframe窗体
                self.driver.switch_to.default_content()

                # 用隐式等待方法等页面出现提示框
                self.driver.implicitly_wait(60)
                self.driver.find_element_by_xpath("//span[contains(text(),'操作成功')]")
                time.sleep(3)

                # 切入‘用户设置’的iframe窗体
                self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id ='bizSetUser-tab-iframe']"))

                # 打印成功
                print("激活‘用户’，成功！")
                logging.info("激活‘用户’，成功！")
                time.sleep(2)
            except Exception as err:
                # 发生其他异常时，打印异常堆栈信息
                print(traceback.print_exc())
                logging.debug("激活‘用户’，失败！" + str(traceback.format_exc()))

            # 测试密码重置‘用户’功能
            try:
                # 勾选
                self.driver.find_element_by_xpath("//div[@title='用户编号:TestUser']/parent::*/preceding-sibling::*[1]/descendant::*[2]").click()
                time.sleep(1)

                # 点击激活按钮
                self.driver.find_element_by_xpath("//span[text()='密码重置']").click()

                # 点击弹出框的OK键
                self.driver.find_element_by_xpath("//button[@id='f-message-webgen-0-okBnt']").click()

                # 退出所有iframe窗体
                self.driver.switch_to.default_content()

                # 用隐式等待方法等页面出现提示框
                self.driver.implicitly_wait(60)
                self.driver.find_element_by_xpath("//span[contains(text(),'密码重置成功，重置后密码为：88888888')]")
                time.sleep(3)

                # 切入‘用户设置’的iframe窗体
                self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id ='bizSetUser-tab-iframe']"))

                # 打印成功
                print("密码重置‘用户’，成功！")
                logging.info("密码重置‘用户’，成功！")
                time.sleep(2)
            except Exception as err:
                # 发生其他异常时，打印异常堆栈信息
                print(traceback.print_exc())
                logging.debug("密码重置‘用户’，失败！" + str(traceback.format_exc()))


            # 测试‘信息查看’功能
            try:
                # 勾选
                self.driver.find_element_by_xpath("//div[@title='用户编号:TestUser']/parent::*/preceding-sibling::*[1]/descendant::*[2]").click()
                time.sleep(1)

                # 点击激活按钮
                self.driver.find_element_by_xpath("//span[text()='信息查看']").click()

                # 切入‘信息查看’的iframe窗体
                self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id ='viewUserInfoWin-iframe']"))
                self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id ='subTabOne-iframe']"))

                # 用隐式等待方法等页面出现提示框
                self.driver.implicitly_wait(60)
                self.driver.find_element_by_xpath("//input[@value='自动化测试用户设置备注修改']")
                time.sleep(3)

                # 退出所有iframe窗体
                self.driver.switch_to.default_content()

                # 切入‘用户设置’的iframe窗体
                self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id ='bizSetUser-tab-iframe']"))

                #关闭信息查看页面
                self.driver.find_element_by_xpath("//div[@class='f-win-tool f-win-close']").click()
                time.sleep(2)

                # 退出所有iframe窗体
                self.driver.switch_to.default_content()

                # 打印成功
                print("‘用户’查看信息，成功！")
                logging.info("‘用户’查看信息’，成功！")
                time.sleep(2)
            except Exception as err:
                # 发生其他异常时，打印异常堆栈信息
                print(traceback.print_exc())
                logging.debug("‘用户’查看信息，失败！" + str(traceback.format_exc()))

            # 用JS的方法关闭当前的页面
            button = self.driver.find_element_by_xpath("//a[@title='用户设置']/child::*[1]")
            self.driver.execute_script("$(arguments[0]).click()", button)

            logging.info("操作‘用户设置’，成功！")

            # 点击页面退出按钮
            self.driver.find_element_by_xpath("//a[contains(.,'退出')]").click()
            time.sleep(1)

            # 点击退出弹窗的'Yes'按钮
            self.driver.find_element_by_xpath("//button[contains(.,'Yes')]").click()
            time.sleep(1)

            #关闭浏览器
            self.driver.quit()
            time.sleep(2)

            #启动浏览器
            self.driver = get("chrome")

            logging.info("测试新租户的新用户‘分配权限’的功能")
            #通过登陆封装函数，以‘UserAdmin’登陆租户‘自动化测试租户’，创建‘组织’
            login( url, "AuthAdmin", "88888888","自动化测试租户")

            #修改密码
            # 切入修改密码的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id ='modifyWin2-iframe']"))

            #输入当前密码
            self.driver.find_element_by_xpath("//input[@id='oldPwd']").send_keys("88888888")
            time.sleep(2)

            #输入新的密码
            self.driver.find_element_by_xpath("//input[@id='newPwd']").send_keys("fingard@1")
            time.sleep(2)

            #输入确认输入
            self.driver.find_element_by_xpath("//input[@id='newPwdre']").send_keys("fingard@1")
            time.sleep(2)

            # 点击确定按钮
            self.driver.find_element_by_xpath("//span[text()='确定']").click()
            time.sleep(2)

            # 点击弹出框的OK键
            #self.driver.find_element_by_xpath("//button[@id='f-message-webgen-0-okBnt']").click()
            #time.sleep(2)

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()



            # 登陆测试用
            login( url, "AuthAdmin", "fingard@1", "自动化测试租户")

            # 测试‘用户权限管理’
            logging.info("测试‘用户权限管理’")

            #点击系统菜单
            self.driver.find_element_by_xpath("//span[contains(text(),'系统菜单')]").click()
            time.sleep(1)
            #点击用户管理菜单
            self.driver.find_element_by_xpath("//span[contains(text(),'用户管理')]").click()
            time.sleep(1)


            # 测试‘用户设置’
            logging.info("测试‘用户设置’")

            # 点击用户设置菜单
            self.driver.find_element_by_xpath("//span[contains(text(),'用户设置')]").click()
            time.sleep(1)

            # 切入‘用户设置’的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id ='bizSetUser-tab-iframe']"))

            # 点击查看
            # 用JS的方法点击放大镜
            button = self.driver.find_element_by_xpath("//span[@class='f-contrac-close']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 输入用户编号
            self.temp = self.driver.find_element_by_xpath("//input[@id='userIdlrlike']")
            self.temp.click()
            time.sleep(1)
            self.temp.send_keys("TestUser")
            time.sleep(1)

            # 测试‘分配组织’
            logging.info("测试‘分配组织’")

            # 勾选
            self.driver.find_element_by_xpath("//div[@title='用户编号:TestUser']/parent::*/preceding-sibling::*[1]/descendant::*[2]").click()
            time.sleep(1)

            # 点击按钮
            self.driver.find_element_by_xpath("//span[text()='分配组织']").click()
            time.sleep(1)

            # 切入‘分配组织’的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id ='allocateAuthorUserOrgWin-iframe']"))

            # 点击查看
            # 用JS的方法点击放大镜
            button = self.driver.find_element_by_xpath("//span[@class='f-contrac-close']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 输入组织编码
            self.temp = self.driver.find_element_by_xpath("//input[@id='orgcode']")
            self.temp.click()
            time.sleep(1)
            self.temp.send_keys("TestTenant")
            time.sleep(1)

            # 点击查询
            self.driver.find_element_by_xpath("//span[text()='查询']").click()
            time.sleep(3)

            #第一次点分配，然后取消，然后再点分配
            for i in range(1,3):
                # 勾选
                self.driver.find_element_by_xpath("//div[@title='组织编码:TestTenant']/parent::*/preceding-sibling::*[2]/descendant::*[2]").click()
                time.sleep(1)

                # 点击分配按钮
                self.driver.find_element_by_xpath("//span[text()='分配']").click()
                time.sleep(1)

                # 点击弹出框的OK键
                self.driver.find_element_by_xpath("//button[@id='f-message-webgen-0-okBnt']").click()

                # 退出所有iframe窗体
                self.driver.switch_to.default_content()

                # 用隐式等待方法等页面出现提示框
                self.driver.implicitly_wait(60)
                self.driver.find_element_by_xpath("//span[contains(text(),'组织分配成功！')]")
                time.sleep(3)

                # 打印
                print("‘分配组织’，第%s次成功！" % i)
                logging.info("‘分配组织’，第%s次成功！" % i)
                time.sleep(2)

                # 切入‘用户设置’的iframe窗体
                self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id ='bizSetUser-tab-iframe']"))

                # 切入‘分配组织’的iframe窗体
                self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id ='allocateAuthorUserOrgWin-iframe']"))

                if i==1:
                    # 勾选
                    self.driver.find_element_by_xpath("//div[@title='组织编码:TestTenant']/parent::*/preceding-sibling::*[2]/descendant::*[2]").click()
                    time.sleep(1)

                    # 点击取消按钮
                    self.driver.find_element_by_xpath("//span[text()='取消']").click()
                    time.sleep(1)

                    # 点击弹出框的OK键
                    self.driver.find_element_by_xpath("//button[@id='f-message-webgen-0-okBnt']").click()

                    # 退出所有iframe窗体
                    self.driver.switch_to.default_content()

                    # 用隐式等待方法等页面出现提示框
                    self.driver.implicitly_wait(60)
                    self.driver.find_element_by_xpath("//span[contains(text(),'组织取消成功！')]")
                    time.sleep(3)

                    # 打印成功
                    print("取消‘分配组织’，成功！")
                    logging.info("取消‘分配组织’，成功！")
                    time.sleep(2)

                    # 切入‘用户设置’的iframe窗体
                    self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id ='bizSetUser-tab-iframe']"))

                    # 切入‘分配组织’的iframe窗体
                    self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id ='allocateAuthorUserOrgWin-iframe']"))

            # 关闭弹出框
            # 退出分配组织的iframe窗体
            self.driver.switch_to.parent_frame()

            # 关闭窗体
            self.driver.find_element_by_xpath("//div[@class='f-win-tool f-win-close']").click()
            time.sleep(2)

            # 测试‘信息查看’功能
            logging.info("测试‘信息查看’功能")
            try:
                #点击信息查看
                self.driver.find_element_by_xpath("//span[text()='信息查看']").click()
                time.sleep(1)

                #切入‘信息查看’iframe
                self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id ='viewUserInfoWin-iframe']"))

                #点击‘关联组织信息’按钮
                self.driver.find_element_by_xpath("//span[text()='关联组织信息']").click()

                # 切入‘关联组织信息’iframe
                self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id ='subTabTwo-iframe']"))

                # 用隐式等待方法来处理
                self.driver.implicitly_wait(60)
                self.driver.find_element_by_xpath("//div[@title='组织编码:TestTenant']")
                time.sleep(3)

                # 退出所有iframe窗体
                self.driver.switch_to.default_content()

                # 切入‘用户设置’的iframe窗体
                self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id ='bizSetUser-tab-iframe']"))

                # 关闭窗体
                self.driver.find_element_by_xpath("//span[text()='信息查看']/preceding-sibling::*").click()
                time.sleep(2)

                # 打印成功
                print(" 测试‘信息查看’功能，成功！")
                logging.info(" 测试‘信息查看’功能，成功！")
                time.sleep(2)
            except Exception as err:
                # 发生其他异常时，打印异常堆栈信息
                print(traceback.print_exc())
                logging.debug(" 测试‘信息查看’功能，失败！" + str(traceback.format_exc()))

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 用JS的方法关闭当前的页面
            button = self.driver.find_element_by_xpath("//a[@title='用户设置']/child::*[1]")
            self.driver.execute_script("$(arguments[0]).click()", button)

            logging.info(" 测试‘用户设置’功能，完成！")



            # 测试‘角色设置’
            logging.info("测试‘角色设置’")
            # 点击菜单
            self.driver.find_element_by_xpath("//span[contains(text(),'角色设置')]").click()
            time.sleep(1)

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 切入‘角色设置’的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id ='bizSetRole-tab-iframe']"))

            # 新增2笔，一笔删除
            for i in range(1, 3):
                # 用JS的方法点击新增按钮
                button = self.driver.find_element_by_xpath("//span[text()='新增']")
                self.driver.execute_script("$(arguments[0]).click()", button)

                # 切入新增的iframe窗体
                self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id ='custButtonWin1-iframe']"))

                # 输入角色编号
                self.driver.find_element_by_xpath("//input[@id='role_code']").send_keys("TestRole")
                time.sleep(2)

                # 输入角色名称
                self.driver.find_element_by_xpath("//input[@id='role_name']").send_keys("测试角色")
                time.sleep(2)

                # 输入排序
                self.driver.find_element_by_xpath("//input[@id='role_order-input']").send_keys("66")
                time.sleep(2)

                #输入组织
                self.temp = self.driver.find_element_by_xpath("//input[@id='combobox-input-orgId']")
                self.temp.click()
                self.temp.clear()
                time.sleep(1)
                self.temp.send_keys("TestOrgSet-测试组织机构设置")
                time.sleep(1)
                self.temp.send_keys(Keys.ARROW_DOWN)
                self.temp.send_keys(Keys.ENTER)
                time.sleep(1)

                # 输入备注
                self.driver.find_element_by_xpath("//textarea[@id='remark']").send_keys("自动化测试角色设置备注")
                time.sleep(2)

                # 点击保存按钮
                self.driver.find_element_by_xpath("//span[text()='保存']").click()

                # 退出所有iframe窗体
                self.driver.switch_to.default_content()

                # 用隐式等待方法来处理
                self.driver.implicitly_wait(60)
                self.driver.find_element_by_xpath("//span[contains(text(),'操作成功！')]")
                print("新增‘角色设置’，第%s笔成功！" % i)
                time.sleep(3)

                # 切入‘角色设置’的iframe窗体
                self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id ='bizSetRole-tab-iframe']"))

                # 如果i等于1，就删除新建的
                if i == 1:
                    # 勾选
                    self.driver.find_element_by_xpath("//div[@title='角色编号:TestRole']/parent::*/preceding-sibling::*[1]/descendant::*[2]").click()
                    time.sleep(1)

                    # 点击删除按钮
                    self.driver.find_element_by_xpath("//span[text()='删除']").click()

                    # 点击弹出框的OK键
                    self.driver.find_element_by_xpath("//button[@id='f-message-webgen-0-okBnt']").click()

                    # 退出所有iframe窗体
                    self.driver.switch_to.default_content()

                    # 用隐式等待方法等页面出现提示框
                    self.driver.implicitly_wait(60)
                    self.driver.find_element_by_xpath("//span[contains(text(),'操作成功')]")
                    print("删除‘角色设置’，成功！")
                    time.sleep(3)

                    # 切入‘角色设置’的iframe窗体
                    self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id ='bizSetRole-tab-iframe']"))

            # 点击查看
            # 用JS的方法点击放大镜
            button = self.driver.find_element_by_xpath("//span[@class='f-contrac-close']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 输入‘角色代码’
            self.temp = self.driver.find_element_by_xpath("//input[@id='role_code']")
            self.temp.click()
            time.sleep(1)
            self.temp.send_keys("TestRole")
            time.sleep(1)

            # 点击查询
            self.driver.find_element_by_xpath("//span[text()='查询']").click()
            time.sleep(3)

            # 测试修改‘角色设置’功能
            try:
                # 勾选
                self.driver.find_element_by_xpath("//div[@title='角色编号:TestRole']/parent::*/preceding-sibling::*[1]/descendant::*[2]").click()
                time.sleep(1)

                # 点击修改按钮
                self.driver.find_element_by_xpath("//span[text()='修改']").click()
                time.sleep(1)

                # 切入修改的iframe窗体
                self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='allocatePowerWin-iframe']"))

                # 修改排序
                self.temp = self.driver.find_element_by_xpath("//input[@id='role_order-input']")
                self.temp.clear()
                self.temp.send_keys("88")
                time.sleep(2)

                # 修改备注
                self.temp = self.driver.find_element_by_xpath("//textarea[@id='remark']")
                self.temp.clear()
                self.temp.send_keys("自动化测试角色设置备注修改")
                time.sleep(2)

                # 点击保存按钮
                self.driver.find_element_by_xpath("//span[text()='保存']").click()

                # 退出所有iframe窗体
                self.driver.switch_to.default_content()

                # 用隐式等待方法来处理
                self.driver.implicitly_wait(60)
                self.driver.find_element_by_xpath("//span[contains(text(),'操作成功！')]")
                time.sleep(3)

                # 切入‘角色设置’的iframe窗体
                self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id ='bizSetRole-tab-iframe']"))

                # 打印成功
                print("修改‘角色设置’，成功！")
                logging.info("修改‘角色设置’，成功！")
                time.sleep(2)
            except Exception as err:
                # 发生其他异常时，打印异常堆栈信息
                print(traceback.print_exc())
                logging.debug("修改‘角色设置’，失败！" + str(traceback.format_exc()))


            # 测试‘分配权限’功能
            try:

                # 勾选
                self.driver.find_element_by_xpath("//div[@title='角色编号:TestRole']/parent::*/preceding-sibling::*[1]/descendant::*[2]").click()
                time.sleep(1)

                # 点击分配权限按钮
                self.driver.find_element_by_xpath("//span[text()='分配权限']").click()
                time.sleep(3)

                # 切入‘分配权限’设置的iframe窗体
                self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id ='allocatePowerWin-iframe']"))

                # 点击展开按钮
                self.driver.find_element_by_xpath("//span[text()='展开']").click()

                # 用隐式等待方法等页面出现提示框
                self.driver.implicitly_wait(60)
                self.driver.find_element_by_xpath("//span[contains(text(),'系统设置')]")
                time.sleep(3)

                # 勾选全部菜单
                #20210629注释
                #self.driver.find_element_by_xpath("//span[@id='node4']").click()
                #20210629修改：双击勾选
                double_click("xpath","//span[@id='node4']")
                time.sleep(3)

                # 点击提交按钮
                self.driver.find_element_by_xpath("//span[text()='提交']").click()

                # 退出所有iframe窗体
                self.driver.switch_to.default_content()

                # 用隐式等待方法等页面出现提示框
                self.driver.implicitly_wait(60)
                self.driver.find_element_by_xpath("//span[contains(text(),'权限分配成功！')]")
                time.sleep(3)

                # 切入‘角色设置’的iframe窗体
                self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id ='bizSetRole-tab-iframe']"))

                # 关闭权限设置页码
                self.driver.find_element_by_xpath("//span[text()='分配权限']/preceding-sibling::*").click()
                time.sleep(3)

                # 打印成功
                print("分配权限‘角色设置’，成功！")
                logging.info("分配权限‘角色设置’，成功！")
                time.sleep(2)
            except Exception as err:
                # 发生其他异常时，打印异常堆栈信息
                print(traceback.print_exc())
                logging.debug("分配权限‘角色设置’，失败！" + str(traceback.format_exc()))
            
            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 用JS的方法关闭当前的页面
            button = self.driver.find_element_by_xpath("//a[@title='角色设置']/child::*[1]")
            self.driver.execute_script("$(arguments[0]).click()", button)

            logging.info(" 测试‘角色设置’功能，完成！")


            # 测试‘多岗设置’
            logging.info("测试‘多岗设置’")
            # 点击菜单
            self.driver.find_element_by_xpath("//span[contains(text(),'多岗设置')]").click()
            time.sleep(1)

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 切入‘多岗设置’的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id ='bizSetOrgRole-tab-iframe']"))

            # 点击查看
            # 用JS的方法点击放大镜
            button = self.driver.find_element_by_xpath("//span[@class='f-contrac-close']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 输入‘用户编号’
            self.temp = self.driver.find_element_by_xpath("//input[@id='userid']")
            self.temp.click()
            time.sleep(1)
            self.temp.send_keys("TestUser")
            time.sleep(1)

            # 点击查询
            self.driver.find_element_by_xpath("//span[text()='查询']").click()
            time.sleep(3)

            # 勾选
            self.driver.find_element_by_xpath("//div[@title='组织名称:TestOrgSet-测试组织机构设置']/parent::*/preceding-sibling::*[3]/descendant::*[2]").click()
            time.sleep(2)

            # 点击‘分配角色’按钮
            self.driver.find_element_by_xpath("//span[text()='分配角色']").click()
            time.sleep(1)

            # 切入‘分配角色’的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='allocateUserOrgRoleWin-iframe']"))

            # 点击查看
            # 用JS的方法点击放大镜
            button = self.driver.find_element_by_xpath("//span[@class='f-contrac-close']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 输入‘角色名称’
            self.temp = self.driver.find_element_by_xpath("//input[@id='rolecode']")
            self.temp.click()
            time.sleep(1)
            self.temp.send_keys("TestRole")
            time.sleep(1)

            # 点击查询
            self.driver.find_element_by_xpath("//span[text()='查询']").click()
            time.sleep(3)

            # 第一次点分配，然后取消，然后再点分配
            for i in range(1, 3):
                # 勾选
                self.driver.find_element_by_xpath("//div[@title='角色编号:TestRole']/parent::*/preceding-sibling::*[2]/descendant::*[2]").click()
                time.sleep(1)

                # 点击分配按钮
                self.driver.find_element_by_xpath("//span[text()='分配']").click()
                time.sleep(1)

                # 点击弹出框的OK键
                self.driver.find_element_by_xpath("//button[@id='f-message-webgen-0-okBnt']").click()

                # 退出所有iframe窗体
                self.driver.switch_to.default_content()

                # 用隐式等待方法等页面出现提示框
                self.driver.implicitly_wait(60)
                self.driver.find_element_by_xpath("//span[contains(text(),'角色分配成功！')]")
                time.sleep(3)

                # 打印
                print("‘分配角色’，第%s次成功！" % i)
                logging.info("‘分配角色’，第%s次成功！" % i)
                time.sleep(2)

                # 切入‘多岗设置’的iframe窗体
                self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id ='bizSetOrgRole-tab-iframe']"))

                # 切入‘分配角色’的iframe窗体
                self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='allocateUserOrgRoleWin-iframe']"))

                if i == 1:
                    # 勾选
                    self.driver.find_element_by_xpath("//div[@title='角色编号:TestRole']/parent::*/preceding-sibling::*[2]/descendant::*[2]").click()
                    time.sleep(1)

                    # 点击取消按钮
                    self.driver.find_element_by_xpath("//span[text()='取消']").click()
                    time.sleep(1)

                    # 点击弹出框的OK键
                    self.driver.find_element_by_xpath("//button[@id='f-message-webgen-0-okBnt']").click()

                    # 退出所有iframe窗体
                    self.driver.switch_to.default_content()

                    # 用隐式等待方法等页面出现提示框
                    self.driver.implicitly_wait(60)
                    self.driver.find_element_by_xpath("//span[contains(text(),'角色取消成功！')]")
                    time.sleep(3)

                    # 打印成功
                    print("取消‘分配角色’，成功！")
                    logging.info("取消‘分配角色’，成功！")
                    time.sleep(2)

                    # 切入‘多岗设置’的iframe窗体
                    self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id ='bizSetOrgRole-tab-iframe']"))

                    # 切入‘分配角色’的iframe窗体
                    self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='allocateUserOrgRoleWin-iframe']"))

            # 关闭弹出框
            # 退出分配组织的iframe窗体
            self.driver.switch_to.parent_frame()

            # 关闭窗体
            self.driver.find_element_by_xpath("//div[@class='f-win-tool f-win-close']").click()
            time.sleep(2)

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 用JS的方法关闭当前的页面
            button = self.driver.find_element_by_xpath("//a[@title='多岗设置']/child::*[1]")
            self.driver.execute_script("$(arguments[0]).click()", button)

            logging.info(" 测试‘多岗设置’功能，完成！")

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 点击页面退出按钮
            self.driver.find_element_by_xpath("//a[contains(.,'退出')]").click()
            time.sleep(1)

            # 点击退出弹窗的'Yes'按钮
            self.driver.find_element_by_xpath("//button[contains(.,'Yes')]").click()
            time.sleep(2)

            #关闭浏览器
            self.driver.quit()
            time.sleep(2)

            #启动浏览器
            self.driver = get("chrome")

            logging.info("测试新租户的新用户‘登陆’的功能")
            #通过登陆封装函数，以‘TestUser’登陆租户‘自动化测试租户’，进行初始化
            login( url, "TestUser", "88888888","自动化测试租户")

            try:
                #修改密码
                # 切入修改密码的iframe窗体
                self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id ='modifyWin2-iframe']"))

                #输入当前密码
                self.driver.find_element_by_xpath("//input[@id='oldPwd']").send_keys("88888888")
                time.sleep(2)

                #输入新的密码
                self.driver.find_element_by_xpath("//input[@id='newPwd']").send_keys("fingard@1")
                time.sleep(2)

                #输入确认输入
                self.driver.find_element_by_xpath("//input[@id='newPwdre']").send_keys("fingard@1")
                time.sleep(2)

                # 点击确定按钮
                self.driver.find_element_by_xpath("//span[text()='确定']").click()
                time.sleep(2)

                # 点击弹出框的OK键
                #self.driver.find_element_by_xpath("//button[@id='f-message-webgen-0-okBnt']").click()
                #time.sleep(2)
            except Exception as err:
                # 发生其他异常时，打印异常堆栈信息
                print(traceback.print_exc())
                logging.debug("修改密码失败！" + str(traceback.format_exc()))
                # Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
                dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
                dir_path = make_current_hour_dir(dir_path + "\\")
                pic_path = os.path.join(dir_path, get_current_time() + ".png")
                capture(pic_path)

            # 退出所有iframe窗体
            switch_default()

            try:
                #点击基础资料--前端缓存刷新--'对接系统'
                # 点击系统设置菜单
                click("xpath", "//div[@class='sysconfigset']")
                time.sleep(1)
                # 退出所有iframe窗体
                switch_default()
                # 切入系统设置的iframe窗体
                switch_to("xpath", "//iframe[@id ='systemconfig-tab-iframe']")
                # 用JS的方法点击基础资料下的'前端缓存'
                js_click("xpath", "//a[@nname='前端缓存刷新']")
                # 退出所有iframe窗体
                switch_default()
                # 切入前端缓存刷新的iframe窗体
                switch_to("xpath", "//iframe[@id='cacherefresh-tab-iframe']")
                time.sleep(1)
                # 用JS的方法点击放大镜
                js_click("xpath", "//span[@class='f-contrac-close']")
                sleep(1)
                #在'缓存名称'中输入'对接系统'
                input("xpath", "//input[@id='name']", "对接系统")
                sleep(1)
                # 点击查询
                click("xpath", "//span[text()='查询']")
                #勾选
                click("xpath","//div[@title='缓存名称:对接系统']/parent::*/preceding-sibling::*[2]/descendant-or-self::*[3]")
                # 点击刷新按钮
                click("xpath", "//span[text()='刷新']")
                # 退出所有iframe窗体
                switch_default()
                # 用隐式等待方法等页面出现提示框
                implici_wait("xpath", "//span[contains(text(),'缓存刷新成功')]")
                print("对接系统，刷新成功！")
                logging.info("对接系统，刷新成功！")
                time.sleep(3)
            except Exception as err:
                # 发生其他异常时，打印异常堆栈信息
                print(traceback.print_exc())
                logging.debug("对接系统，刷新失败！" + str(traceback.format_exc()))
                # Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
                dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
                dir_path = make_current_hour_dir(dir_path + "\\")
                pic_path = os.path.join(dir_path, get_current_time() + ".png")
                capture(pic_path)

            # 退出所有iframe窗体
            switch_default()

            try:
                # 点击基础资料--前端缓存刷新--'CRM缓存'
                # 切入前端缓存刷新的iframe窗体
                switch_to("xpath", "//iframe[@id='cacherefresh-tab-iframe']")
                time.sleep(1)
                #清空'缓存名称'框
                clear("xpath", "//input[@id='name']")
                # 在'缓存名称'中输入'CRM缓存'
                input("xpath", "//input[@id='name']", "CRM缓存")
                sleep(1)
                # 点击查询
                click("xpath", "//span[text()='查询']")
                # 勾选
                click("xpath", "//div[@title='缓存名称:CRM缓存']/parent::*/preceding-sibling::*[2]/descendant-or-self::*[3]")
                # 点击刷新按钮
                click("xpath", "//span[text()='刷新']")
                # 退出所有iframe窗体
                switch_default()
                # 用隐式等待方法等页面出现提示框
                implici_wait("xpath", "//span[contains(text(),'缓存刷新成功')]")
                print("CRM缓存，刷新成功！")
                logging.info("CRM缓存，刷新成功！")
                time.sleep(3)
                # 用JS的方法关闭前端缓存刷新的页面
                js_click("xpath", "//a[@title='前端缓存刷新']/child::*[1]")
            except Exception as err:
                # 发生其他异常时，打印异常堆栈信息
                print(traceback.print_exc())
                logging.debug("CRM缓存，刷新失败！" + str(traceback.format_exc()))
                # Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
                dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
                dir_path = make_current_hour_dir(dir_path + "\\")
                pic_path = os.path.join(dir_path, get_current_time() + ".png")
                capture(pic_path)

            # 退出所有iframe窗体
            switch_default()

            try:
                #把 直联设置 - -银行 - -直联银行 - -'中国工商银行'设置成直联。
                # 切入系统设置的iframe窗体
                switch_to("xpath", "//iframe[@id ='systemconfig-tab-iframe']")
                #点击'直联设置'按钮
                click("xpath", "//span[text()='直联设置']")
                time.sleep(1)
                # 用JS的方法点击基础资料下的'银行'
                js_click("xpath", "//span[@class='setitem_icon  sysBank_icon']")
                # 退出所有iframe窗体
                switch_default()
                # 切入银行的iframe窗体
                switch_to("xpath", "//iframe[@id='sysBank-tab-iframe']")
                # 点击‘直联银行’页面
                click("xpath", "//span[text()='直联银行']")
                # 切入‘直联银行’的iframe窗体
                switch_to("xpath", "//iframe[@id='subTabTwo-iframe']")
                # 点击查看
                # 用JS的方法点击放大镜
                js_click("xpath", "//span[@class='f-contrac-close']")
                sleep(1)
                # 输入银行名称
                input("xpath", "//input[@id='name']", "中国工商银行")
                time.sleep(2)
                # 点击查询
                click("xpath", "//span[text()='查询']")
                # 勾选
                click("xpath", "//div[@title='代码:ICBC']/parent::*/preceding-sibling::*[1]/descendant-or-self::*[3]")
                # 点击直联按钮
                click("xpath", "//span[text()='直联']")
                # 退出所有iframe窗体
                switch_default()
                # 用隐式等待方法等页面出现提示框
                implici_wait("xpath", "//span[contains(text(),'操作成功')]")
                print("点击'直联'按钮，操作成功！")
                logging.info("点击'直联'按钮，操作成功！")
                time.sleep(3)
                # 用JS的方法关闭银行的页面
                js_click("xpath", "//a[@title='银行']/child::*[1]")
            except Exception as err:
                # 发生其他异常时，打印异常堆栈信息
                print(traceback.print_exc())
                logging.debug("直联银行-'中国工商银行'失败！" + str(traceback.format_exc()))
                # Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
                dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
                dir_path = make_current_hour_dir(dir_path + "\\")
                pic_path = os.path.join(dir_path, get_current_time() + ".png")
                capture(pic_path)

            # 退出所有iframe窗体
            switch_default()

            # 点击页面退出按钮
            self.driver.find_element_by_xpath("//a[contains(.,'退出')]").click()
            time.sleep(1)

            # 点击退出弹窗的'Yes'按钮
            self.driver.find_element_by_xpath("//button[contains(.,'Yes')]").click()
            time.sleep(2)
            logging.info("新租户的新用户‘退出’成功！")

    # def tearDown(self):
    #     self.driver.quit()
        print("结束时间：", time.strftime("%Y-%m-%d %H:%M:%S"))

if __name__ == '__main__':
    #  启动单元测试
    unittest.main(verbosity=2)