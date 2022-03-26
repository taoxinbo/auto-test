#encoding=utf-8
# 2020-09-04
# TaoXB
# 此文件是自动化测试：系统设置--直联设置，下面的所有模块的增删改查。
import os
import sys
# 当前文件所在目录都添加到sys.path中，系统可以找到需要引用的模块
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)),".."))
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

#print("开始时间：",time.strftime("%Y-%m-%d %H:%M:%S"))

driver = ""
class Syset_config(unittest.TestCase):

    #启动浏览器
    def setUp(self):

        #启动浏览器的另外一个方法：通过封装启动浏览器的驱动，启动不同浏览器
        self.driver = get("chrome")

    # 登陆系统、对系统设置进行操作
    def test_trade(self):

        #通过登陆封装函数，进行登陆
        login( G_Ora_Url,TestUser, Password, "自动化测试租户")
        #login( G_Ora_Url,Tao, Password,"默认租户")
        #login( G_Mys_Url,TestUser,Password, "自动化测试租户")
        #login(G_Mys_Url, Tao, Password, "默认租户")

        #login(G_Ora_Url, judy, Password, "默认租户")

        logging.info("开始测试系统设置--直联设置的页面功能")
        #点击系统设置菜单
        self.driver.find_element_by_xpath("//div[@class='sysconfigset']").click()
        time.sleep(1)
        # 退出所有iframe窗体
        self.driver.switch_to.default_content()
        # 切入系统设置的iframe窗体
        self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id ='systemconfig-tab-iframe']"))
        # # 用JS的方法点击直联设置菜单
        # button = self.driver.find_element_by_xpath("//span[text()='直联设置']")
        # self.driver.execute_script("$(arguments[0]).click()", button)

        #点击‘直联设置’页面
        self.driver.find_element_by_xpath("//span[text()='直联设置']").click()
        time.sleep(2)

        #测试‘银行--银行’功能
        try:
            #退出所有iframe窗体
            self.driver.switch_to.default_content()
            #切入系统设置的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id ='systemconfig-tab-iframe']"))
            logging.info("开始测试‘银行--银行’功能")

            # 用JS的方法点击基础资料下的'银行'
            button = self.driver.find_element_by_xpath("//span[@class='setitem_icon  sysBank_icon']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            #退出所有iframe窗体
            self.driver.switch_to.default_content()
            #切入银行的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='sysBank-tab-iframe']"))
            # 切入‘银行-银行’的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='subTabOne-iframe']"))

            # 点击查看
            # 用JS的方法点击放大镜
            button = self.driver.find_element_by_xpath("//span[@class='f-contrac-close']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 输入银行代码：
            self.temp = self.driver.find_element_by_xpath("//input[@id='code']")
            self.temp.send_keys("BOC")
            time.sleep(2)

            #点击查询
            self.driver.find_element_by_xpath("//span[text()='查询']").click()
            time.sleep(2)

            #勾选
            self.driver.find_element_by_xpath("//div[@title='代码:BOC']/parent::*/preceding-sibling::*[1]/descendant-or-self::*[3]").click()

            #点击外汇业务类别按钮
            self.driver.find_element_by_xpath("//span[text()='外汇业务类别']").click()

            #切入‘外汇交易编码’iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='foreignBusinessTypeWin-iframe']"))
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='subTabTwo-iframe']"))

            # 用JS的点击新增按钮
            button = self.driver.find_element_by_xpath("//span[text()='新增']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 切入新增的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='addWin-iframe']"))

            #填入代码值
            self.driver.find_element_by_xpath("//input[@id='code']").send_keys("test")
            time.sleep(2)

            #名称中填入值
            self.driver.find_element_by_xpath("//input[@id='name']").send_keys("test自动化测试")
            time.sleep(2)

            #选择业务范围
            self.temp = self.driver.find_element_by_xpath("//input[@id='combobox-input-businessscope']")
            self.temp.click()
            time.sleep(1)
            self.temp.send_keys(Keys.ARROW_DOWN)
            self.temp.send_keys(Keys.ENTER)
            time.sleep(1)

            #选择银行
            self.temp = self.driver.find_element_by_xpath("//input[@id='combobox-input-bankid']")
            self.temp.click()
            time.sleep(1)
            self.temp.send_keys(Keys.ARROW_DOWN)
            self.temp.send_keys(Keys.ENTER)
            time.sleep(1)

            # 描述框中填入值
            self.driver.find_element_by_xpath("//textarea[@id='description']").send_keys("test自动化测试")
            time.sleep(2)

            # 点击保存按钮
            self.driver.find_element_by_xpath("//span[text()='保存']").click()

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 用隐式等待方法等页面出现新增成功的提示框
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath("//span[contains(text(),'操作成功！')]")
            print('新增保存‘外汇交易编码’成功！')
            time.sleep(3)

            #切入‘银行--外汇交易编码’的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='sysBank-tab-iframe']"))
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='subTabOne-iframe']"))
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='foreignBusinessTypeWin-iframe']"))
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='subTabTwo-iframe']"))

            # 点击查看
            # 用JS的方法点击放大镜
            button = self.driver.find_element_by_xpath("//span[@class='f-contrac-close']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 输入银行代码：
            self.temp = self.driver.find_element_by_xpath("//input[@id='code']")
            self.temp.send_keys("test")
            time.sleep(2)

            # 点击查询
            self.driver.find_element_by_xpath("//span[text()='查询']").click()
            time.sleep(2)

            # 修改功能
            # 勾选
            self.driver.find_element_by_xpath("//div[@title='代码:test']/parent::*/preceding-sibling::*[1]/descendant::*[2]").click()
            time.sleep(1)

            # 点击修改按钮
            self.driver.find_element_by_xpath("//span[text()='修改']").click()
            time.sleep(1)

            # 切入修改的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='modWin-iframe']"))

            # 修改描述框中的内容
            self.driver.find_element_by_xpath("//textarea[@id='description']").send_keys("自动化测试修改")
            time.sleep(2)

            # 点击保存按钮
            self.driver.find_element_by_xpath("//span[text()='保存']").click()

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 用隐式等待方法等页面出现新增成功的提示框
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath("//span[contains(text(),'操作成功！')]")
            print('修改‘外汇交易编码’，成功！')
            time.sleep(3)

            # 切入‘银行--外汇交易编码’的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='sysBank-tab-iframe']"))
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='subTabOne-iframe']"))
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='foreignBusinessTypeWin-iframe']"))
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='subTabTwo-iframe']"))

            #失效按钮
            #勾选
            self.driver.find_element_by_xpath("//div[@title='代码:test']/parent::*/preceding-sibling::*[1]/descendant::*[2]").click()
            time.sleep(1)

            # 点击失效按钮
            self.driver.find_element_by_xpath("//span[text()='失效']").click()
            time.sleep(1)

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 用隐式等待方法等页面出现新增成功的提示框
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath("//span[contains(text(),'成功失效1条记录！')]")
            print('外汇交易编码，失效成功！')
            time.sleep(3)

            # 切入‘银行--外汇交易编码’的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='sysBank-tab-iframe']"))
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='subTabOne-iframe']"))
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='foreignBusinessTypeWin-iframe']"))
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='subTabTwo-iframe']"))

            # 生效按钮
            # 勾选
            self.driver.find_element_by_xpath("//div[@title='代码:test']/parent::*/preceding-sibling::*[1]/descendant::*[2]").click()
            time.sleep(1)

            # 点击生效按钮
            self.driver.find_element_by_xpath("//span[text()='生效']").click()
            time.sleep(1)

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 用隐式等待方法等页面出现新增成功的提示框
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath("//span[contains(text(),'成功生效1条记录！')]")
            print('外汇交易编码，生效成功！')
            time.sleep(3)

            # 切入‘银行--外汇交易编码’的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='sysBank-tab-iframe']"))
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='subTabOne-iframe']"))
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='foreignBusinessTypeWin-iframe']"))
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='subTabTwo-iframe']"))

            #删除功能
            #勾选
            self.driver.find_element_by_xpath("//div[@title='代码:test']/parent::*/preceding-sibling::*[1]/descendant::*[2]").click()

            #点击删除按钮
            self.driver.find_element_by_xpath("//span[text()='删除']").click()

            # 点击弹出框的OK键
            self.driver.find_element_by_xpath("//button[@id='f-message-webgen-0-okBnt']").click()

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 用隐式等待方法等页面出现提示框
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath("//span[contains(text(),'操作成功！')]")
            print("删除‘外汇交易编码’成功")
            time.sleep(3)

            #打印外汇交易编码成功
            print('外汇交易编码，完成!')
            logging.info("外汇交易编码，完成!")
            time.sleep(2)

            #开始测试‘结汇购汇编码’
            # 切入‘银行--结汇购汇编码’的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='sysBank-tab-iframe']"))
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='subTabOne-iframe']"))
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='foreignBusinessTypeWin-iframe']"))

            #点击‘结汇购汇编码’的页面
            self.driver.find_element_by_xpath("//span[text()='结汇购汇编码']").click()

            #切入iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='subTabOne-iframe']"))

            # 连续新增2笔，一笔购汇，一笔结汇
            for i in range(1, 3):
                # 用JS的方法点击新增按钮
                button = self.driver.find_element_by_xpath("//span[text()='新增']")
                self.driver.execute_script("$(arguments[0]).click()", button)

                # 切入新增的iframe窗体
                self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='addWin-iframe']"))

                # 输入代码
                self.driver.find_element_by_xpath("//input[@id='code']").send_keys("test" + str(i))
                time.sleep(2)

                # 输入名称
                self.driver.find_element_by_xpath("//input[@id='name']").send_keys("测试结汇购汇编码"+ str(i))
                time.sleep(2)

                #选择业务范围
                self.temp = self.driver.find_element_by_xpath("//input[@id='combobox-input-businessscope']")
                self.temp.click()
                time.sleep(1)
                if i==1:
                    self.temp.send_keys(Keys.ENTER)
                else:
                    self.temp.send_keys(Keys.ARROW_DOWN)
                    self.temp.send_keys(Keys.ENTER)

                #选择银行
                self.temp = self.driver.find_element_by_xpath("//input[@id='combobox-input-bankid']")
                self.temp.click()
                time.sleep(1)
                self.temp.send_keys(Keys.ARROW_DOWN)
                self.temp.send_keys(Keys.ENTER)
                time.sleep(2)

                # 描述框中填入值
                self.driver.find_element_by_xpath("//textarea[@id='description']").send_keys("测试结汇购汇编码" + str(i))
                time.sleep(2)

                # 点击保存按钮
                self.driver.find_element_by_xpath("//span[text()='保存']").click()

                # 退出所有iframe窗体
                self.driver.switch_to.default_content()

                # 用隐式等待方法等页面出现提示框
                self.driver.implicitly_wait(60)
                self.driver.find_element_by_xpath("//span[contains(text(),'操作成功！')]")
                print('新增结汇购汇编码，第%s笔成功！' % i)
                time.sleep(3)

                # 切入‘银行--结汇购汇编码’的iframe窗体
                self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='sysBank-tab-iframe']"))
                self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='subTabOne-iframe']"))
                self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='foreignBusinessTypeWin-iframe']"))
                self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='subTabOne-iframe']"))

            # 点击查看
            # 用JS的方法点击放大镜
            button = self.driver.find_element_by_xpath("//span[@class='f-contrac-close']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 输入银行代码：
            self.temp = self.driver.find_element_by_xpath("//input[@id='code']")
            self.temp.send_keys("test")
            time.sleep(2)

            # 点击查询
            self.driver.find_element_by_xpath("//span[text()='查询']").click()
            time.sleep(2)

            # 修改功能
            # 勾选
            self.driver.find_element_by_xpath("//div[@title='代码:test1']/parent::*/preceding-sibling::*[1]/descendant::*[2]").click()
            time.sleep(1)

            # 点击修改按钮
            self.driver.find_element_by_xpath("//span[text()='修改']").click()
            time.sleep(1)

            # 切入修改的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='modWin-iframe']"))

            # 修改描述框中的内容
            self.driver.find_element_by_xpath("//textarea[@id='description']").send_keys("自动化测试修改")
            time.sleep(2)

            # 点击保存按钮
            self.driver.find_element_by_xpath("//span[text()='保存']").click()

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 用隐式等待方法等页面出现新增成功的提示框
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath("//span[contains(text(),'操作成功！')]")
            print('修改‘结汇购汇编码’，成功！')
            time.sleep(3)

            # 切入‘银行--结汇购汇编码’的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='sysBank-tab-iframe']"))
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='subTabOne-iframe']"))
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='foreignBusinessTypeWin-iframe']"))
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='subTabOne-iframe']"))

            # 失效按钮
            # 勾选
            self.driver.find_element_by_xpath("//div[@title='代码:test1']/parent::*/preceding-sibling::*[1]/descendant::*[2]").click()
            time.sleep(1)

            # 点击失效按钮
            self.driver.find_element_by_xpath("//span[text()='失效']").click()
            time.sleep(1)

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 用隐式等待方法等页面出现新增成功的提示框
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath("//span[contains(text(),'成功失效1条记录！')]")
            print('结汇购汇编码，点击失效成功！')
            time.sleep(3)

            # 切入‘银行--结汇购汇编码’的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='sysBank-tab-iframe']"))
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='subTabOne-iframe']"))
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='foreignBusinessTypeWin-iframe']"))
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='subTabOne-iframe']"))

            # 生效按钮
            # 勾选
            self.driver.find_element_by_xpath("//div[@title='代码:test1']/parent::*/preceding-sibling::*[1]/descendant::*[2]").click()
            time.sleep(1)

            # 点击生效按钮
            self.driver.find_element_by_xpath("//span[text()='生效']").click()
            time.sleep(1)

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 用隐式等待方法等页面出现新增成功的提示框
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath("//span[contains(text(),'成功生效1条记录！')]")
            print('结汇购汇编码，点击生效成功！')
            time.sleep(3)

            # 切入‘银行--结汇购汇编码’的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='sysBank-tab-iframe']"))
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='subTabOne-iframe']"))
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='foreignBusinessTypeWin-iframe']"))
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='subTabOne-iframe']"))

            # 删除功能
            # 勾选
            self.driver.find_element_by_xpath("//div[@title='代码:test1']/parent::*/preceding-sibling::*[1]/descendant::*[2]").click()
            self.driver.find_element_by_xpath("//div[@title='代码:test2']/parent::*/preceding-sibling::*[1]/descendant::*[2]").click()

            # 点击删除按钮
            self.driver.find_element_by_xpath("//span[text()='删除']").click()

            # 点击弹出框的OK键
            self.driver.find_element_by_xpath("//button[@id='f-message-webgen-0-okBnt']").click()

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            #用隐式等待方法等页面出现提示框
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath("//span[contains(text(),'操作成功！')]")
            print("删除‘结汇购汇编码’成功")
            time.sleep(3)

            #关闭外汇业务类别页面
            # 切入iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='sysBank-tab-iframe']"))
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='subTabOne-iframe']"))

            # 点击关闭按钮
            self.driver.find_element_by_xpath("//div[@class='f-win-tool f-win-close']").click()

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 打印外汇交易编码成功
            print('结汇购汇编码，完成!')
            logging.info("结汇购汇编码，完成!")
            time.sleep(2)
        except Exception as err:
            #发生其他异常时，打印异常堆栈信息
            print(traceback.print_exc())
            logging.debug("操作‘银行--银行’页面功能失败！" + str(traceback.format_exc()))


        #测试‘银行--直联银行’功能
        try:
            #退出所有iframe窗体
            self.driver.switch_to.default_content()
            #切入系统设置的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id ='systemconfig-tab-iframe']"))
            logging.info("开始测试‘银行--直联银行’功能")

            # 用JS的方法点击基础资料下的'银行'
            button = self.driver.find_element_by_xpath("//span[@class='setitem_icon  sysBank_icon']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            #退出所有iframe窗体
            self.driver.switch_to.default_content()
            #切入银行的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='sysBank-tab-iframe']"))

            # 点击‘直联银行’页面
            self.driver.find_element_by_xpath("//span[text()='直联银行']").click()

            # 切入‘直联银行’的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='subTabTwo-iframe']"))

            # 点击查看
            # 用JS的方法点击放大镜
            button = self.driver.find_element_by_xpath("//span[@class='f-contrac-close']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 输入银行代码：
            self.temp = self.driver.find_element_by_xpath("//input[@id='code']")
            self.temp.send_keys("BOC")
            time.sleep(2)

            #点击查询
            self.driver.find_element_by_xpath("//span[text()='查询']").click()
            time.sleep(2)

            #勾选
            self.driver.find_element_by_xpath("//div[@title='代码:BOCHK']/parent::*/preceding-sibling::*[1]/descendant-or-self::*[3]").click()

            #点击直联按钮
            self.driver.find_element_by_xpath("//span[text()='直联']").click()

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 用隐式等待方法等页面出现提示框
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath("//span[contains(text(),'操作成功！')]")
            print('点击‘直联’按钮，成功！')
            time.sleep(4)

            # 切入‘直联银行’的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='sysBank-tab-iframe']"))
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='subTabTwo-iframe']"))

            # 勾选
            self.driver.find_element_by_xpath("//div[@title='代码:BOCHK']/parent::*/preceding-sibling::*[1]/descendant-or-self::*[3]").click()

            # 点击非直联按钮
            self.driver.find_element_by_xpath("//span[text()='非直联']").click()

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 用隐式等待方法等页面出现提示框
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath("//span[contains(text(),'操作成功！')]")
            print('点击‘非直联’按钮，成功！')
            time.sleep(4)

            #用JS的方法关闭前端缓存刷新的页面
            button = self.driver.find_element_by_xpath("//a[@title='银行']/child::*[1]")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 打印外汇交易编码成功
            print("‘银行--直联银行’，完成!")
            logging.info("‘银行--直联银行’，完成!")
            time.sleep(2)
        except Exception as err:
            #发生其他异常时，打印异常堆栈信息
            print(traceback.print_exc())
            logging.debug("操作‘银行--直联银行’页面功能失败！" + str(traceback.format_exc()))
        

        #测试‘国家’页面功能
        try:
            #退出所有iframe窗体
            self.driver.switch_to.default_content()
            #切入系统设置的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id ='systemconfig-tab-iframe']"))
            logging.info("开始测试‘国家’页面功能")

            # 用JS的方法点击基础资料下的'国家'
            button = self.driver.find_element_by_xpath("//span[@class='setitem_icon  sysCountry_icon']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            #退出所有iframe窗体
            self.driver.switch_to.default_content()
            #切入国家的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='sysCountry-tab-iframe']"))

            # 点击查看
            # 用JS的方法点击放大镜
            button = self.driver.find_element_by_xpath("//span[@class='f-contrac-close']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 输入代码：
            self.temp = self.driver.find_element_by_xpath("//input[@id='code']")
            self.temp.send_keys("C")
            time.sleep(2)

            # 输入名称：
            self.temp = self.driver.find_element_by_xpath("//input[@id='name']")
            self.temp.send_keys("中国")
            time.sleep(2)

            #点击查询
            self.driver.find_element_by_xpath("//span[text()='查询']").click()
            time.sleep(3)

            #用隐式等待方法等页面出现提示框
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath("//div[@title='名称:中国']")
            print("国家查询成功")
            time.sleep(3)

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            #用JS的方法关闭前端缓存刷新的页面
            button = self.driver.find_element_by_xpath("//a[@title='国家']/child::*[1]")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 打印成功
            print("‘国家’页面，完成!")
            logging.info("‘国家’页面，完成!")
            time.sleep(2)
        except Exception as err:
            #发生其他异常时，打印异常堆栈信息
            print(traceback.print_exc())
            logging.debug("操作‘国家’页面功能失败！" + str(traceback.format_exc()))
        

        #测试‘区域’页面功能
        try:
            #退出所有iframe窗体
            self.driver.switch_to.default_content()
            #切入系统设置的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id ='systemconfig-tab-iframe']"))
            logging.info("开始测试‘区域’页面功能")

            # 用JS的方法点击基础资料下的'区域'
            button = self.driver.find_element_by_xpath("//span[@class='setitem_icon  sysArea_icon']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            #退出所有iframe窗体
            self.driver.switch_to.default_content()
            #切入区域的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='sysArea-tab-iframe']"))

            # 点击查看
            # 用JS的方法点击放大镜
            button = self.driver.find_element_by_xpath("//span[@class='f-contrac-close']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 输入代码：
            self.temp = self.driver.find_element_by_xpath("//input[@id='code']")
            self.temp.send_keys("3301")
            time.sleep(2)

            # 输入名称：
            self.temp = self.driver.find_element_by_xpath("//input[@id='name']")
            self.temp.send_keys("浙江省_杭州市")
            time.sleep(2)

            #点击查询
            self.driver.find_element_by_xpath("//span[text()='查询']").click()
            time.sleep(3)

            #用隐式等待方法等页面出现提示框
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath("//div[@title='名称:浙江省_杭州市']")
            print("区域查询成功")
            time.sleep(3)

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            #用JS的方法关闭前端缓存刷新的页面
            button = self.driver.find_element_by_xpath("//a[@title='区域']/child::*[1]")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 打印成功
            print("‘区域’页面，完成!")
            logging.info("‘区域’页面，完成!")
            time.sleep(2)
        except Exception as err:
            #发生其他异常时，打印异常堆栈信息
            print(traceback.print_exc())
            logging.debug("操作‘区域’页面功能失败！" + str(traceback.format_exc()))
        

        #测试‘开户银行’功能
        try:
            #退出所有iframe窗体
            self.driver.switch_to.default_content()
            #切入系统设置的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id ='systemconfig-tab-iframe']"))
            logging.info("开始测试‘开户银行’功能")

            # 用JS的方法点击基础资料下的'开户银行'
            button = self.driver.find_element_by_xpath("//span[@class='setitem_icon  sysBankLocations_icon']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            #退出所有iframe窗体
            self.driver.switch_to.default_content()
            #切入开户银行的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='sysBankLocations-tab-iframe']"))

            # 用JS的方法点击新增按钮
            button = self.driver.find_element_by_xpath("//span[text()='新增']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            #切入新增的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='addWin-iframe']"))

            #设置时间的变成存储
            temp=time.strftime("%Y%m%d%H%M%S")

            # 输入代码
            self.driver.find_element_by_xpath("//input[@id='code']").send_keys("test" + str(temp))
            time.sleep(2)

            # 输入名称
            self.driver.find_element_by_xpath("//input[@id='name']").send_keys("测试开户银行功能" + str(temp))
            time.sleep(2)

            #选择银行
            self.temp = self.driver.find_element_by_xpath("//input[@id='combobox-input-bankid']")
            self.temp.click()
            time.sleep(1)
            self.temp.send_keys("HZCB-杭州银行")
            time.sleep(1)
            self.temp.send_keys(Keys.ARROW_DOWN)
            self.temp.send_keys(Keys.ENTER)
            time.sleep(2)

            #选择区域
            self.temp = self.driver.find_element_by_xpath("//input[@id='combobox-input-areaid']")
            self.temp.click()
            time.sleep(1)
            self.temp.send_keys("3301-浙江省_杭州市")
            time.sleep(1)
            self.temp.send_keys(Keys.ARROW_DOWN)
            self.temp.send_keys(Keys.ENTER)
            time.sleep(2)

            #输入‘SWIFT CODE’
            self.driver.find_element_by_xpath("//input[@id='swiftcode']").send_keys("SWIFT CODE")
            time.sleep(2)

            #输入‘SWIFT NAME’
            self.driver.find_element_by_xpath("//input[@id='swiftname']").send_keys("SWIFT NAME")
            time.sleep(2)

            # 描述框中填入值
            self.driver.find_element_by_xpath("//input[@id='description']").send_keys("自动化测试")
            time.sleep(2)

            # 点击保存按钮
            self.driver.find_element_by_xpath("//span[text()='保存']").click()

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 用隐式等待方法等页面出现提示框
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath("//span[contains(text(),'操作成功！')]")
            print("新增‘开户银行’，成功！")
            time.sleep(3)

            # 切入开户银行的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='sysBankLocations-tab-iframe']"))

            # 点击查看
            # 用JS的方法点击放大镜
            button = self.driver.find_element_by_xpath("//span[@class='f-contrac-close']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            temp1 = time.strftime("%Y%m%d")

            # 输入银行代码：
            self.temp = self.driver.find_element_by_xpath("//input[@id='code']")
            self.temp.send_keys("test"+ str(temp1))
            time.sleep(2)

            #输入是否有效
            self.temp = self.driver.find_element_by_xpath("//input[@id='combobox-input-isactive']")
            self.temp.click()
            time.sleep(1)
            self.temp.send_keys("是")
            time.sleep(1)
            self.temp.send_keys(Keys.ENTER)
            time.sleep(1)

            # 点击查询
            self.driver.find_element_by_xpath("//span[text()='查询']").click()
            time.sleep(2)

            # 修改功能
            # 勾选
            #self.driver.find_element_by_xpath("//div[@title='代码:test+str(temp)']/parent::*/preceding-sibling::*[1]/descendant::*[2]").click()
            self.driver.find_element_by_xpath("//button[@class='f-grid-checkbox']").click()
            time.sleep(1)

            # 点击修改按钮
            self.driver.find_element_by_xpath("//span[text()='修改']").click()
            time.sleep(1)

            # 切入修改的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='modWin-iframe']"))

            # 修改描述框中的内容
            self.driver.find_element_by_xpath("//input[@id='description']").send_keys("自动化测试修改")
            time.sleep(2)

            #去掉是否有效按钮的勾
            self.driver.find_element_by_xpath("//input[@id='isactive']").click()
            time.sleep(2)

            # 点击保存按钮
            self.driver.find_element_by_xpath("//span[text()='保存']").click()

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 用隐式等待方法等页面出现新增成功的提示框
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath("//span[contains(text(),'操作成功！')]")
            print('修改‘开户银行’，成功！')
            time.sleep(3)

            #用JS的方法关闭前端缓存刷新的页面
            button = self.driver.find_element_by_xpath("//a[@title='开户银行']/child::*[1]")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 打印外汇交易编码成功
            print("‘开户银行’，完成!")
            logging.info("‘开户银行’，完成!")
            time.sleep(2)
        except Exception as err:
            #发生其他异常时，打印异常堆栈信息
            print(traceback.print_exc())
            logging.debug("操作‘开户银行’功能失败！" + str(traceback.format_exc()))
        


        #测试‘交易信息码’页面功能
        try:
            #退出所有iframe窗体
            self.driver.switch_to.default_content()
            #切入系统设置的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id ='systemconfig-tab-iframe']"))
            logging.info("开始测试‘交易信息码’页面功能")

            # 用JS的方法点击基础资料下的'交易信息码'
            button = self.driver.find_element_by_xpath("//span[@class='setitem_icon  sysTransCode_icon']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            #退出所有iframe窗体
            self.driver.switch_to.default_content()
            #切入交易信息码的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='sysTransCode-tab-iframe']"))

            # 点击查看
            # 用JS的方法点击放大镜
            button = self.driver.find_element_by_xpath("//span[@class='f-contrac-close']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 输入代码：
            self.temp = self.driver.find_element_by_xpath("//input[@id='code']")
            self.temp.send_keys("E1057")
            time.sleep(2)

            #点击查询
            self.driver.find_element_by_xpath("//span[text()='查询']").click()
            time.sleep(3)

            #用隐式等待方法等页面出现查询记录
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath("//div[@title='代码:E1057']")
            print("交易信息码，查询成功")
            time.sleep(3)

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            #用JS的方法关闭前端缓存刷新的页面
            button = self.driver.find_element_by_xpath("//a[@title='交易信息码']/child::*[1]")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 打印成功
            print("‘交易信息码’页面，完成!")
            logging.info("‘交易信息码’页面，完成!")
            time.sleep(2)
        except Exception as err:
            #发生其他异常时，打印异常堆栈信息
            print(traceback.print_exc())
            logging.debug("操作‘交易信息码’页面功能失败！" + str(traceback.format_exc()))
        


        #测试‘代收付用途’页面功能
        try:
            #退出所有iframe窗体
            self.driver.switch_to.default_content()
            #切入系统设置的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id ='systemconfig-tab-iframe']"))
            logging.info("开始测试‘代收付用途’页面功能")

            # 用JS的方法点击基础资料下的'代收付用途'
            button = self.driver.find_element_by_xpath("//span[@class='setitem_icon  sysPurposes_icon']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            #退出所有iframe窗体
            self.driver.switch_to.default_content()
            #切入代收付用途的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='sysPurposes-tab-iframe']"))

            # 把‘交易方向’放到一个字典中
            temp = {1: '支出', 2: '收入'}
            # 连续新增2笔，一笔支出，一笔收入
            for k, v in temp.items():
                # 用JS的方法点击新增按钮
                button = self.driver.find_element_by_xpath("//span[text()='新增']")
                self.driver.execute_script("$(arguments[0]).click()", button)

                # 切入新增的iframe窗体
                self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='addWin-iframe']"))

                # 输入代码
                self.driver.find_element_by_xpath("//input[@id='code']").send_keys("test" + str(k))
                time.sleep(2)

                # 输入名称
                self.driver.find_element_by_xpath("//input[@id='name']").send_keys("测试" + str(v))
                time.sleep(2)

                #输入交易方向
                self.temp = self.driver.find_element_by_xpath("//input[@id='combobox-input-moneyway']")
                self.temp.click()
                self.temp.send_keys(v)
                time.sleep(1)
                self.temp.send_keys(Keys.ARROW_DOWN)
                self.temp.send_keys(Keys.ENTER)

                # 描述框中填入值
                self.driver.find_element_by_xpath("//textarea[@id='description']").send_keys("自动化测试" + str(v))
                time.sleep(2)

                # 点击保存按钮
                self.driver.find_element_by_xpath("//span[text()='保存']").click()

                # 退出所有iframe窗体
                self.driver.switch_to.default_content()

                # 用隐式等待方法等页面出现提示框
                self.driver.implicitly_wait(60)
                self.driver.find_element_by_xpath("//span[contains(text(),'操作成功！')]")
                print('保存代收付用途第%s笔：交易方向为%s成功！' % (k, v))
                time.sleep(3)

                # 切入代收付用途的iframe窗体
                self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='sysPurposes-tab-iframe']"))


            # 点击查看
            # 用JS的方法点击放大镜
            button = self.driver.find_element_by_xpath("//span[@class='f-contrac-close']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 输入代码：
            self.temp = self.driver.find_element_by_xpath("//input[@id='code']")
            self.temp.send_keys("test")
            time.sleep(2)

            #点击查询
            self.driver.find_element_by_xpath("//span[text()='查询']").click()
            time.sleep(3)

            #修改
            # 勾选
            self.driver.find_element_by_xpath("//div[@title='代码:test2']/parent::*/preceding-sibling::*[1]/descendant::*[2]").click()
            time.sleep(1)

            # 点击修改按钮
            self.driver.find_element_by_xpath("//span[text()='修改']").click()
            time.sleep(1)

            # 切入修改的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='modWin-iframe']"))

            #去掉是否有效按钮的勾
            self.driver.find_element_by_xpath("//input[@id='isactive']").click()
            time.sleep(2)

            # 修改描述框中的内容
            self.driver.find_element_by_xpath("//textarea[@id='description']").send_keys("自动化测试修改")
            time.sleep(2)

            # 点击保存按钮
            self.driver.find_element_by_xpath("//span[text()='保存']").click()

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 用隐式等待方法等页面出现新增成功的提示框
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath("//span[contains(text(),'操作成功！')]")
            print('代收付用途，修改成功！')
            time.sleep(3)

            # 切入代收付用途的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='sysPurposes-tab-iframe']"))

            #删除功能
            #勾选2笔
            #self.driver.find_element_by_xpath("//div[@title='代码:test1']/parent::*/preceding-sibling::*[1]/descendant::*[2]").click()
            self.driver.find_element_by_xpath("//div[@title='代码:test2']/parent::*/preceding-sibling::*[1]/descendant::*[2]").click()

            #点击删除按钮
            self.driver.find_element_by_xpath("//span[text()='删除']").click()

            # 点击弹出框的OK键
            self.driver.find_element_by_xpath("//button[@id='f-message-webgen-0-okBnt']").click()

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 用隐式等待方法等页面出现删除的提示框
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath("//span[contains(text(),'操作成功')]")
            print("删除‘代收付用途’,成功！")
            time.sleep(3)

            #用JS的方法关闭前端缓存刷新的页面
            button = self.driver.find_element_by_xpath("//a[@title='代收付用途']/child::*[1]")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 打印成功
            print("‘代收付用途’页面，完成!")
            logging.info("‘代收付用途’页面，完成!")
            time.sleep(2)
        except Exception as err:
            #发生其他异常时，打印异常堆栈信息
            print(traceback.print_exc())
            logging.debug("操作‘代收付用途’页面功能失败！" + str(traceback.format_exc()))
        


        # 测试‘直联渠道’页面功能
        try:
            # 退出所有iframe窗体
            self.driver.switch_to.default_content()
            # 切入系统设置的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id ='systemconfig-tab-iframe']"))
            logging.info("开始测试‘直联渠道’页面功能")

            # 用JS的方法点击基础资料下的'直联渠道'
            button = self.driver.find_element_by_xpath("//span[@class='setitem_icon  sysDirectChannel_icon']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()
            # 切入'直联渠道'的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='sysDirectChannel-tab-iframe']"))

            # 点击查看
            # 用JS的方法点击放大镜
            button = self.driver.find_element_by_xpath("//span[@class='f-contrac-close']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 输入名称：
            self.temp = self.driver.find_element_by_xpath("//input[@id='name']")
            self.temp.send_keys("杭州银行")
            time.sleep(2)

            # 点击查询
            self.driver.find_element_by_xpath("//span[text()='查询']").click()
            time.sleep(3)

            # 用隐式等待方法等页面出现提示框
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath("//div[@title='银行:杭州银行股份有限公司']")
            print("‘直联渠道’查询成功")
            time.sleep(3)

            #测试失效按钮功能
            # 勾选
            self.driver.find_element_by_xpath("//div[@title='银行:杭州银行股份有限公司']/parent::*/preceding-sibling::*[1]/descendant-or-self::*[3]").click()

            #点击失效按钮
            self.driver.find_element_by_xpath("//span[text()='失效']").click()

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 用隐式等待方法来处理
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath("//span[contains(text(),'失效成功！')]")
            print("‘失效’按钮，成功！")
            time.sleep(3)

            # 切入'直联渠道'的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='sysDirectChannel-tab-iframe']"))

            # 测试生效按钮功能
            # 勾选
            self.driver.find_element_by_xpath("//div[@title='银行:杭州银行股份有限公司']/parent::*/preceding-sibling::*[1]/descendant-or-self::*[3]").click()

            # 点击生效按钮
            self.driver.find_element_by_xpath("//span[text()='生效']").click()

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 用隐式等待方法来处理
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath("//span[contains(text(),'生效成功！')]")
            print("‘生效’按钮，成功！")
            time.sleep(3)

            # 用JS的方法关闭前端缓存刷新的页面
            button = self.driver.find_element_by_xpath("//a[@title='直联渠道']/child::*[1]")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 打印成功
            print("‘直联渠道’页面，完成!")
            logging.info("‘直联渠道’页面，完成!")
            time.sleep(2)
        except Exception as err:
            # 发生其他异常时，打印异常堆栈信息
            print(traceback.print_exc())
            logging.debug("操作‘直联渠道’页面功能失败！" + str(traceback.format_exc()))
        

        # 测试‘直联渠道区域及国家’页面功能
        try:
            # 退出所有iframe窗体
            self.driver.switch_to.default_content()
            # 切入系统设置的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id ='systemconfig-tab-iframe']"))
            logging.info("开始测试‘直联渠道区域及国家’页面功能")

            # 用JS的方法点击基础资料下的'直联渠道区域及国家'
            button = self.driver.find_element_by_xpath("//span[@class='setitem_icon  sysDirectChannelAreas_icon']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()
            # 切入‘直联渠道区域及国家--直联渠道国家’的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='sysDirectChannelAreas-tab-iframe']"))
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='subTabTwo-iframe']"))

            # 点击查看
            # 用JS的方法点击放大镜
            button = self.driver.find_element_by_xpath("//span[@class='f-contrac-close']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 输入代码：
            self.temp = self.driver.find_element_by_xpath("//input[@id='code']")
            self.temp.send_keys("CHN")
            time.sleep(2)

            # 输入名称：
            self.temp = self.driver.find_element_by_xpath("//input[@id='name']")
            self.temp.send_keys("中国")
            time.sleep(2)

            # 点击查询
            self.driver.find_element_by_xpath("//span[text()='查询']").click()
            time.sleep(3)

            #用隐式等待方法等页面出现提示框
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath("//div[@title='名称:中国']")
            print("‘直联渠道区域及国家--直联渠道国家’，查询成功")
            time.sleep(3)

            #退出‘直联渠道区域及国家--直联渠道国家’iframe窗体
            self.driver.switch_to.parent_frame()

            #点击‘直联渠道区域及国家--直联渠道区域’
            self.driver.find_element_by_xpath("//span[text()='直联渠道区域']").click()

            #切入‘直联渠道区域及国家--直联渠道区域’的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='subTabOne-iframe']"))

            # 点击查看
            # 用JS的方法点击放大镜
            button = self.driver.find_element_by_xpath("//span[@class='f-contrac-close']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 输入代码：
            self.temp = self.driver.find_element_by_xpath("//input[@id='code']")
            self.temp.send_keys("1202")
            time.sleep(2)

            # 输入名称：
            self.temp = self.driver.find_element_by_xpath("//input[@id='name']")
            self.temp.send_keys("杭州")
            time.sleep(2)

            # 点击查询
            self.driver.find_element_by_xpath("//span[text()='查询']").click()
            time.sleep(3)

            # 用隐式等待方法等页面出现提示框
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath("//div[@title='名称:杭州']")
            print("‘直联渠道区域及国家--直联渠道区域’，查询成功")
            time.sleep(3)

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 用JS的方法关闭前端缓存刷新的页面
            button = self.driver.find_element_by_xpath("//a[@title='直联渠道区域及国家']/child::*[1]")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 打印成功
            print("‘直联渠道区域及国家’页面，完成!")
            logging.info("‘直联渠道区域及国家’页面，完成!")
            time.sleep(2)
        except Exception as err:
            # 发生其他异常时，打印异常堆栈信息
            print(traceback.print_exc())
            logging.debug("操作‘直联渠道区域及国家’页面，功能失败！" + str(traceback.format_exc()))



        # 测试‘直联渠道指令’页面功能
        try:
            # 退出所有iframe窗体
            self.driver.switch_to.default_content()
            # 切入系统设置的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id ='systemconfig-tab-iframe']"))
            logging.info("开始测试‘直联渠道指令’页面功能")

            # 用JS的方法点击基础资料下的'国家'
            button = self.driver.find_element_by_xpath("//span[@class='setitem_icon  sysDirectChannelCmd_icon']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()
            # 切入‘直联渠道指令’的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='sysDirectChannelCmd-tab-iframe']"))

            # 点击查看
            # 用JS的方法点击放大镜
            button = self.driver.find_element_by_xpath("//span[@class='f-contrac-close']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 输入名称：
            self.temp = self.driver.find_element_by_xpath("//input[@id='name']")
            self.temp.send_keys("对外支付（实时单笔）")
            time.sleep(2)

            # 输入直联渠道：
            self.temp = self.driver.find_element_by_xpath("//input[@id='combobox-input-directchannelid']")
            self.temp.click()
            time.sleep(1)
            self.temp.send_keys("邦付宝")
            time.sleep(2)
            # 勾选
            self.driver.find_element_by_xpath("//div[@title='代码-名称:BFB01-邦付宝']/parent::*/preceding-sibling::*[1]/descendant::*[2]").click()
            time.sleep(1)

            # 点击查询
            self.driver.find_element_by_xpath("//span[text()='查询']").click()
            time.sleep(2)

            # 用隐式等待方法等页面出现提示框
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath("//div[@title='名称:对外支付（实时单笔）']")
            print("‘直联渠道指令’查询，成功!")
            time.sleep(1)

            #增加手续费配置
            # 勾选
            self.driver.find_element_by_xpath("//button[@class='f-grid-checkbox']").click()
            time.sleep(1)

            #点击‘手续费配置’按钮
            self.driver.find_element_by_xpath("//span[text()='手续费配置']").click()
            time.sleep(2)

            #切入新增‘手续费配置’的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='editWin-iframe']"))

            #新增2行
            for i in range(1,3):
                self.driver.find_element_by_xpath("//span[text()='新增行']").click()

            #第一行的‘交易金额从’输入值
            self.temp = self.driver.find_element_by_xpath("//input[@id='editgrid-amountfrom-0-input']")
            self.temp.clear()
            self.temp.send_keys("111.11")
            time.sleep(2)

            # 第一行的‘交易金额到’输入值
            self.temp = self.driver.find_element_by_xpath("//input[@id='editgrid-amountto-0-input']")
            self.temp.clear()
            self.temp.send_keys("1111.11")
            time.sleep(2)

            # 第一行的‘费用/百分比’输入值
            self.temp = self.driver.find_element_by_xpath("//input[@id='editgrid-costs-0-input']")
            self.temp.clear()
            self.temp.send_keys("11.1111")
            time.sleep(2)

            # 第一行的‘最小费用’输入值
            self.temp = self.driver.find_element_by_xpath("//input[@id='editgrid-mincosts-0-input']")
            self.temp.clear()
            self.temp.send_keys("22.22")
            time.sleep(2)

            # 第一行的‘最大费用’输入值
            self.temp = self.driver.find_element_by_xpath("//input[@id='editgrid-maxcosts-0-input']")
            self.temp.clear()
            self.temp.send_keys("333.33")
            time.sleep(2)

            #第二行‘计费场景’输入值
            self.temp = self.driver.find_element_by_xpath("//input[@id='combobox-input-editgrid-chargescenarios-1']")
            self.temp.click()
            time.sleep(1)
            self.temp.clear()
            time.sleep(1)
            self.temp.send_keys("跨行网银互联")
            time.sleep(1)
            self.temp.send_keys(Keys.ENTER)

            # 第二行的‘交易金额从’输入值
            self.temp = self.driver.find_element_by_xpath("//input[@id='editgrid-amountfrom-1-input']")
            self.temp.clear()
            self.temp.send_keys("111.11")
            time.sleep(2)

            # 第二行的‘交易金额到’输入值
            self.temp = self.driver.find_element_by_xpath("//input[@id='editgrid-amountto-1-input']")
            self.temp.clear()
            self.temp.send_keys("1111.11")
            time.sleep(2)

            # 第二行的‘计费模式’输入值
            self.temp = self.driver.find_element_by_xpath("//input[@id='combobox-input-editgrid-chargemode-1']")
            self.temp.click()
            time.sleep(1)
            self.temp.clear()
            time.sleep(1)
            self.temp.send_keys("固定费用")
            time.sleep(1)
            self.temp.send_keys(Keys.ENTER)

            # 第二行的‘费用/百分比’输入值
            self.temp = self.driver.find_element_by_xpath("//input[@id='editgrid-costs-1-input']")
            self.temp.clear()
            self.temp.send_keys("12.34")
            time.sleep(2)

            # 点击保存按钮
            self.driver.find_element_by_xpath("//span[text()='保存']").click()

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 用隐式等待方法来处理
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath("//span[contains(text(),'操作成功！')]")
            print("‘手续费配置’保存，成功！")
            time.sleep(3)

            # 切入‘直联渠道指令’的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='sysDirectChannelCmd-tab-iframe']"))

            #点击‘手续费详情’链接
            self.driver.find_element_by_xpath("//a[contains(text(),'手续费详情')]").click()

            #切入‘手续费详情’链接的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='detailWin-iframe']"))

            #点击‘设置’按钮
            self.driver.find_element_by_xpath("//span[text()='设置']").click()
            time.sleep(1)

            # 退出‘手续费详情’链接的iframe窗体
            self.driver.switch_to.parent_frame()

            # 切入编辑‘手续费详情’的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='editWin-iframe']"))

            #勾选新增的第1行
            self.driver.find_element_by_xpath("//input[@type='checkbox' and @class='syscheckitem']").click()
            time.sleep(1)
            #点击移出行
            self.driver.find_element_by_xpath("//span[contains(text(),'移出行')]").click()
            time.sleep(1)

            #勾选新增的第2行
            self.driver.find_element_by_xpath("//input[@type='checkbox' and @class='syscheckitem']").click()
            time.sleep(1)
            #点击移出行
            self.driver.find_element_by_xpath("//span[contains(text(),'移出行')]").click()
            time.sleep(1)

            # 点击保存按钮
            self.driver.find_element_by_xpath("//span[text()='保存']").click()

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 用隐式等待方法来处理
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath("//span[contains(text(),'操作成功！')]")
            print("‘手续费配置’删除，成功！")
            time.sleep(3)

            # 用JS的方法关闭前端缓存刷新的页面
            button = self.driver.find_element_by_xpath("//a[@title='直联渠道指令']/child::*[1]")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 打印成功
            print("‘直联渠道指令’页面功能，完成!")
            logging.info("‘直联渠道指令’页面功能，完成!")
            time.sleep(2)
        except Exception as err:
            # 发生其他异常时，打印异常堆栈信息
            print(traceback.print_exc())
            logging.debug("操作‘直联渠道指令’页面功能，失败！" + str(traceback.format_exc()))


        #测试‘直联渠道指令参数定义’页面功能
        try:
            #退出所有iframe窗体
            self.driver.switch_to.default_content()
            #切入系统设置的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id ='systemconfig-tab-iframe']"))
            logging.info("开始测试‘直联渠道指令参数定义’页面功能")

            # 用JS的方法点击基础资料下的'直联渠道指令参数定义'
            button = self.driver.find_element_by_xpath("//span[@class='setitem_icon  sysDirectChannelCmdParamDef_icon']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            #退出所有iframe窗体
            self.driver.switch_to.default_content()
            #切入国家的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='sysDirectChannelCmdParamDef-tab-iframe']"))

            # 点击查看
            # 用JS的方法点击放大镜
            button = self.driver.find_element_by_xpath("//span[@class='f-contrac-close']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 输入名称：
            self.temp = self.driver.find_element_by_xpath("//input[@id='name']")
            self.temp.send_keys("组包规则")
            time.sleep(2)

            # 输入直联渠道指令：
            self.temp = self.driver.find_element_by_xpath("//input[@id='combobox-input-directchannelcmdid']")
            self.temp.click()
            time.sleep(1)
            self.temp.send_keys("批量代付（非财务室）")
            time.sleep(2)
            # 勾选
            self.driver.find_element_by_xpath("//div[@title='代码-名称:198802-批量代付（非财务室）-ICBC02']/parent::*/preceding-sibling::*[1]/descendant::*[2]").click()
            time.sleep(1)

            #点击查询
            self.driver.find_element_by_xpath("//span[text()='查询']").click()
            time.sleep(3)

            #用隐式等待方法等页面出现提示框
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath("//div[@title='直联渠道:工行银企互联推广版']")
            print("‘直联渠道指令参数定义’查询成功")
            time.sleep(3)

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            #用JS的方法关闭前端缓存刷新的页面
            button = self.driver.find_element_by_xpath("//a[@title='直联渠道指令参数定义']/child::*[1]")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 打印成功
            print("‘直联渠道指令参数定义’页面功能，完成!")
            logging.info("‘直联渠道指令参数定义’页面功能，完成!")
            time.sleep(2)
        except Exception as err:
            #发生其他异常时，打印异常堆栈信息
            print(traceback.print_exc())
            logging.debug("操作‘直联渠道指令参数定义’页面功能，失败！" + str(traceback.format_exc()))
        
        

        #测试‘直联渠道指令参数值’页面功能
        try:
            #退出所有iframe窗体
            self.driver.switch_to.default_content()
            #切入系统设置的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id ='systemconfig-tab-iframe']"))
            logging.info("开始测试‘直联渠道指令参数值’页面功能")

            # 用JS的方法点击基础资料下的'直联渠道指令参数值'
            button = self.driver.find_element_by_xpath("//span[@class='setitem_icon  sysDirectChannelCmParamVal_icon']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            #退出所有iframe窗体
            self.driver.switch_to.default_content()
            #切入'直联渠道指令参数值'的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='sysDirectChannelCmParamVal-tab-iframe']"))

            # 点击查看
            # 用JS的方法点击放大镜
            button = self.driver.find_element_by_xpath("//span[@class='f-contrac-close']")
            self.driver.execute_script("$(arguments[0]).click()", button)
            time.sleep(2)

            # 输入参数定义：
            self.temp = self.driver.find_element_by_xpath("//input[@id='combobox-input-paramdefid']")
            self.temp.click()
            time.sleep(1)
            self.temp.send_keys("P3101-拆分笔数-批量代收-浦发银企互联1")
            time.sleep(1)
            # 勾选
            self.driver.find_element_by_xpath("//div[@title='代码-名称:P3101-拆分笔数-批量代收-浦发银企互联1.x']/parent::*/preceding-sibling::*[1]/descendant::*[2]").click()
            time.sleep(1)

            #点击查询
            self.driver.find_element_by_xpath("//span[text()='查询']").click()
            time.sleep(3)

            #用隐式等待方法等页面出现提示框
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath("//div[@title='描述:浦发代收支付包拆分笔数']")
            print("‘直联渠道指令参数值’查询成功")
            time.sleep(3)

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            #用JS的方法关闭前端缓存刷新的页面
            button = self.driver.find_element_by_xpath("//a[@title='直联渠道指令参数值']/child::*[1]")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 打印成功
            print("‘直联渠道指令参数值’页面功能，完成!")
            logging.info("‘直联渠道指令参数值’页面功能，完成!")
            time.sleep(2)
        except Exception as err:
            #发生其他异常时，打印异常堆栈信息
            print(traceback.print_exc())
            logging.debug("操作‘直联渠道指令参数值’页面功能，失败！" + str(traceback.format_exc()))

        

        # 测试‘直联渠道交易信息码’页面功能
        try:
            # 退出所有iframe窗体
            self.driver.switch_to.default_content()
            # 切入系统设置的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id ='systemconfig-tab-iframe']"))
            logging.info("开始测试‘直联渠道交易信息码’页面功能")

            # 用JS的方法点击基础资料下的'直联渠道交易信息码'
            button = self.driver.find_element_by_xpath("//span[@class='setitem_icon  sysDirectChannelTransCodes_icon']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()
            # 切入'直联渠道交易信息码'的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='sysDirectChannelTransCodes-tab-iframe']"))

            # 点击查看
            # 用JS的方法点击放大镜
            button = self.driver.find_element_by_xpath("//span[@class='f-contrac-close']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 输入代码：
            self.temp = self.driver.find_element_by_xpath("//input[@id='code']")
            self.temp.send_keys("真实姓名不匹配")
            time.sleep(2)

            # 输入直联渠道：
            self.temp = self.driver.find_element_by_xpath("//input[@id='combobox-input-directchannelid']")
            self.temp.click()
            time.sleep(1)
            self.temp.send_keys("微保支付")
            time.sleep(1)
            # 勾选
            self.driver.find_element_by_xpath("//div[@title='代码-名称:VBAO01-微保支付']/parent::*/preceding-sibling::*[1]/descendant::*[2]").click()
            time.sleep(1)

            # 点击查询
            self.driver.find_element_by_xpath("//span[text()='查询']").click()
            time.sleep(3)

            # 用隐式等待方法等页面出现提示框
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath("//div[@title='交易信息码:证件号码或姓名与账户不符']")
            print("‘直联渠道交易信息码’查询成功")
            time.sleep(3)

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 用JS的方法关闭前端缓存刷新的页面
            button = self.driver.find_element_by_xpath("//a[@title='直联渠道交易信息码']/child::*[1]")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 打印成功
            print("‘直联渠道交易信息码’页面功能，完成!")
            logging.info("‘直联渠道交易信息码’页面功能，完成!")
            time.sleep(2)
        except Exception as err:
            # 发生其他异常时，打印异常堆栈信息
            print(traceback.print_exc())
            logging.debug("操作‘直联渠道交易信息码’页面功能，失败！" + str(traceback.format_exc()))

        

        # 测试‘直联渠道交易结果’页面功能
        try:
            # 退出所有iframe窗体
            self.driver.switch_to.default_content()
            # 切入系统设置的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id ='systemconfig-tab-iframe']"))
            logging.info("开始测试‘直联渠道交易结果’页面功能")

            # 用JS的方法点击基础资料下的'直联渠道交易结果'
            button = self.driver.find_element_by_xpath("//span[@class='setitem_icon  sysDirectChannelTransResults_icon']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()
            # 切入'直联渠道交易结果'的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='sysDirectChannelTransResults-tab-iframe']"))

            # 点击查看
            # 用JS的方法点击放大镜
            button = self.driver.find_element_by_xpath("//span[@class='f-contrac-close']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 输入直联渠道：
            #self.temp = self.driver.find_element_by_xpath("//input[@id='combobox-input-directchannelid']")
            #self.temp.click()
            self.temp = self.driver.find_element_by_xpath("//input[@id='combobox-input-directchannelid']")
            self.driver.execute_script("$(arguments[0]).click()", self.temp)
            time.sleep(1)
            self.temp.send_keys("翼支付")
            time.sleep(1)
            # 勾选
            self.driver.find_element_by_xpath("//div[@title='代码-名称:BESTPAY01-翼支付']/parent::*/preceding-sibling::*[1]/descendant::*[2]").click()
            time.sleep(1)

            # 输入报文类型
            self.temp = self.driver.find_element_by_xpath("//input[@id='combobox-input-packettype']")
            self.temp.click()
            time.sleep(1)
            self.temp.send_keys(Keys.ENTER)
            time.sleep(1)

            # 输入收付状态
            # self.temp = self.driver.find_element_by_xpath("//input[@id='combobox-input-paystate']")
            # self.temp.click()
            # button = self.driver.find_element_by_xpath("//input[@id='combobox-input-paystate']")
            # self.driver.execute_script("$(arguments[0]).click()", button)
            # time.sleep(1)
            # button.send_keys(Keys.ARROW_DOWN)
            # button.send_keys(Keys.ARROW_DOWN)
            # button.send_keys(Keys.ARROW_DOWN)
            # button.send_keys(Keys.ENTER)
            # time.sleep(1)

            # 点击查询
            self.driver.find_element_by_xpath("//span[text()='查询']").click()
            time.sleep(3)

            # 用隐式等待方法等页面出现提示框
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath("//div[@title='直联渠道:翼支付']")
            print("‘直联渠道交易结果’查询成功")
            time.sleep(3)

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 用JS的方法关闭前端缓存刷新的页面
            button = self.driver.find_element_by_xpath("//a[@title='直联渠道交易结果']/child::*[1]")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 打印成功
            print("‘直联渠道交易结果’页面功能，完成!")
            logging.info("‘直联渠道交易结果’页面功能，完成!")
            time.sleep(2)
        except Exception as err:
            # 发生其他异常时，打印异常堆栈信息
            print(traceback.print_exc())
            logging.debug("操作‘直联渠道交易结果’页面功能，失败！" + str(traceback.format_exc()))
        
        

        # 测试‘直联渠道代收付用途’页面功能
        try:
            # 退出所有iframe窗体
            self.driver.switch_to.default_content()
            # 切入系统设置的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id ='systemconfig-tab-iframe']"))
            logging.info("开始测试‘直联渠道代收付用途’页面功能")

            # 用JS的方法点击基础资料下的'直联渠道代收付用途'
            button = self.driver.find_element_by_xpath("//span[@class='setitem_icon  sysDirectChannelPurposes_icon']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()
            # 切入'直联渠道代收付用途'的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='sysDirectChannelPurposes-tab-iframe']"))

            # 点击查看
            # 用JS的方法点击放大镜
            button = self.driver.find_element_by_xpath("//span[@class='f-contrac-close']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 输入代码：
            self.temp = self.driver.find_element_by_xpath("//input[@id='code']")
            self.temp.send_keys("1050201")
            time.sleep(2)

            # 输入名称：
            self.temp = self.driver.find_element_by_xpath("//input[@id='name']")
            self.temp.send_keys("工资")
            time.sleep(2)

            # 点击查询
            self.driver.find_element_by_xpath("//span[text()='查询']").click()
            time.sleep(3)

            # 用隐式等待方法等页面出现提示框
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath("//div[@title='直联渠道:建行网银外联平台']")
            print("‘直联渠道代收付用途’查询成功")
            time.sleep(3)

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 用JS的方法关闭前端缓存刷新的页面
            button = self.driver.find_element_by_xpath("//a[@title='直联渠道代收付用途']/child::*[1]")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 打印成功
            print("‘直联渠道代收付用途’页面功能，完成!")
            logging.info("‘直联渠道代收付用途’页面功能，完成!")
            time.sleep(2)
        except Exception as err:
            # 发生其他异常时，打印异常堆栈信息
            print(traceback.print_exc())
            logging.debug("操作‘直联渠道代收付用途’页面功能，失败！" + str(traceback.format_exc()))

        

        # 测试‘直联渠道代收付用途映射’页面功能
        try:
            # 退出所有iframe窗体
            self.driver.switch_to.default_content()
            # 切入系统设置的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id ='systemconfig-tab-iframe']"))
            logging.info("开始测试‘直联渠道代收付用途映射’页面功能")

            # 用JS的方法点击基础资料下的'直联渠道代收付用途映射'
            button = self.driver.find_element_by_xpath("//span[@class='setitem_icon  sysDirectChannelPurposesMap_icon']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()
            # 切入'直联渠道代收付用途映射'的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='sysDirectChannelPurposesMap-tab-iframe']"))

            # 用JS的方法点击新增按钮
            button = self.driver.find_element_by_xpath("//span[text()='新增']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 切入新增的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='addWin-iframe']"))

            # 输入‘直联渠道代收付用途’
            self.temp = self.driver.find_element_by_xpath("//input[@id='combobox-input-directchannelpurposeid']")
            self.temp.click()
            self.temp.send_keys("1020102-工资")
            time.sleep(1)
            self.temp.send_keys(Keys.ARROW_DOWN)
            self.temp.send_keys(Keys.ENTER)

            # 输入‘代收付用途’
            self.temp = self.driver.find_element_by_xpath("//input[@id='combobox-input-purposeid']")
            self.temp.click()
            self.temp.send_keys("test1-测试支出")
            time.sleep(1)
            self.temp.send_keys(Keys.ARROW_DOWN)
            self.temp.send_keys(Keys.ENTER)

            # 描述框中填入值
            self.driver.find_element_by_xpath("//textarea[@id='description']").send_keys("自动化测试")
            time.sleep(2)

            # 点击保存按钮
            self.driver.find_element_by_xpath("//span[text()='保存']").click()

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 用隐式等待方法等页面出现提示框
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath("//span[contains(text(),'操作成功！')]")
            print('保存‘直联渠道代收付用途’,成功！')
            time.sleep(3)

            # 切入'直联渠道代收付用途映射'的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='sysDirectChannelPurposesMap-tab-iframe']"))

            # 点击查看
            # 用JS的方法点击放大镜
            button = self.driver.find_element_by_xpath("//span[@class='f-contrac-close']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 输入代收付用途：
            self.temp = self.driver.find_element_by_xpath("//input[@id='combobox-input-purposeid']")
            self.temp.click()
            time.sleep(1)
            self.temp.send_keys("test1-测试支出")
            time.sleep(1)
            # 勾选
            self.driver.find_element_by_xpath("//div[@title='代码-名称:test1-测试支出']/parent::*/preceding-sibling::*[1]/descendant::*[2]").click()
            time.sleep(1)

            # 输入直联渠道代收付用途：
            self.temp = self.driver.find_element_by_xpath("//input[@id='combobox-input-directchannelpurposeid']")
            self.temp.click()
            time.sleep(1)
            self.temp.send_keys("1020102-工资")
            time.sleep(1)
            # 勾选
            self.driver.find_element_by_xpath("//div[@title='代码-名称:1020102-工资']/parent::*/preceding-sibling::*[1]/descendant::*[2]").click()
            time.sleep(1)

            # 点击查询
            self.driver.find_element_by_xpath("//span[text()='查询']").click()
            time.sleep(3)

            # 修改
            # 勾选
            #self.driver.find_element_by_xpath("//button[@class='f-grid-checkbox']").click()
            self.driver.find_element_by_xpath("//div[@title='直联渠道代收付用途:工资']/parent::*/preceding-sibling::*[1]/descendant::*[2]").click()
            time.sleep(1)

            # 点击修改按钮
            self.driver.find_element_by_xpath("//span[text()='修改']").click()
            time.sleep(1)

            # 切入修改的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='modWin-iframe']"))

            # 去掉是否有效按钮的勾
            self.driver.find_element_by_xpath("//input[@id='isactive']").click()
            time.sleep(2)

            # 修改描述框中的内容
            self.driver.find_element_by_xpath("//textarea[@id='description']").send_keys("自动化测试修改")
            time.sleep(2)

            # 点击保存按钮
            self.driver.find_element_by_xpath("//span[text()='保存']").click()

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 用隐式等待方法等页面出现新增成功的提示框
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath("//span[contains(text(),'操作成功！')]")
            print("修改‘直联渠道代收付用途映射’，成功！")
            time.sleep(3)

            # 切入'直联渠道代收付用途映射'的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='sysDirectChannelPurposesMap-tab-iframe']"))

            # 删除功能
            # 勾选
            #self.driver.find_element_by_xpath("//button[@class='f-grid-checkbox']").click()
            self.driver.find_element_by_xpath("//div[@title='直联渠道代收付用途:工资']/parent::*/preceding-sibling::*[1]/descendant::*[2]").click()
            time.sleep(1)

            # 点击删除按钮
            self.driver.find_element_by_xpath("//span[text()='删除']").click()

            # 点击弹出框的OK键
            self.driver.find_element_by_xpath("//button[@id='f-message-webgen-0-okBnt']").click()

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 用隐式等待方法等页面出现删除的提示框
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath("//span[contains(text(),'操作成功')]")
            print("删除‘直联渠道代收付用途映射’,成功！")
            time.sleep(3)

            # 用JS的方法关闭前端缓存刷新的页面
            button = self.driver.find_element_by_xpath("//a[@title='直联渠道代收付用途映射']/child::*[1]")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 打印成功
            print("‘直联渠道代收付用途映射’页面功能，完成!")
            logging.info("‘直联渠道代收付用途映射’页面功能，完成!")
            time.sleep(2)
        except Exception as err:
            # 发生其他异常时，打印异常堆栈信息
            print(traceback.print_exc())
            logging.debug("操作‘直联渠道代收付用途映射’页面功能，失败！" + str(traceback.format_exc()))



        #删除‘代收付用途’的‘test1’的数据
        try:
            #退出所有iframe窗体
            self.driver.switch_to.default_content()
            #切入系统设置的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id ='systemconfig-tab-iframe']"))
            logging.info("开始测试‘代收付用途’页面功能")

            # 用JS的方法点击基础资料下的'代收付用途'
            button = self.driver.find_element_by_xpath("//span[@class='setitem_icon  sysPurposes_icon']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            #退出所有iframe窗体
            self.driver.switch_to.default_content()
            #切入代收付用途的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='sysPurposes-tab-iframe']"))

            # 点击查看
            # 用JS的方法点击放大镜
            button = self.driver.find_element_by_xpath("//span[@class='f-contrac-close']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 输入代码：
            self.temp = self.driver.find_element_by_xpath("//input[@id='code']")
            self.temp.send_keys("test")
            time.sleep(2)

            #点击查询
            self.driver.find_element_by_xpath("//span[text()='查询']").click()
            time.sleep(3)

            #删除功能
            #勾选‘test1’内容
            self.driver.find_element_by_xpath("//div[@title='代码:test1']/parent::*/preceding-sibling::*[1]/descendant::*[2]").click()
            time.sleep(1)

            #点击删除按钮
            self.driver.find_element_by_xpath("//span[text()='删除']").click()

            # 点击弹出框的OK键
            self.driver.find_element_by_xpath("//button[@id='f-message-webgen-0-okBnt']").click()

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 用隐式等待方法等页面出现删除的提示框
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath("//span[contains(text(),'操作成功')]")
            time.sleep(3)

            #用JS的方法关闭前端缓存刷新的页面
            button = self.driver.find_element_by_xpath("//a[@title='代收付用途']/child::*[1]")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 打印成功
            print("删除‘代收付用途为test1的数据’,成功！")
            logging.info("删除‘代收付用途为test1的数据’,成功！")
            time.sleep(2)
        except Exception as err:
            #发生其他异常时，打印异常堆栈信息
            print(traceback.print_exc())
            logging.debug("删除‘代收付用途为test1的数据’,失败！" + str(traceback.format_exc()))


        
        # 测试‘直联查询指令配置’页面功能
        try:
            # 退出所有iframe窗体
            self.driver.switch_to.default_content()
            # 切入系统设置的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id ='systemconfig-tab-iframe']"))
            logging.info("开始测试‘直联查询指令配置’页面功能")

            # 用JS的方法点击基础资料下的'直联查询指令配置'
            button = self.driver.find_element_by_xpath("//span[@class='setitem_icon  sysDirectQueryCmdConfigs_icon']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()
            # 切入'直联查询指令配置'的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='sysDirectQueryCmdConfigs-tab-iframe']"))

            # 点击查看
            # 用JS的方法点击放大镜
            button = self.driver.find_element_by_xpath("//span[@class='f-contrac-close']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 输入银行：
            #self.temp = self.driver.find_element_by_xpath("//input[@id='combobox-input-bankid']")
            #self.temp.click()
            self.temp = self.driver.find_element_by_xpath("//input[@id='combobox-input-bankid']")
            self.driver.execute_script("$(arguments[0]).click()", self.temp)
            time.sleep(1)
            self.temp.send_keys("工商银行")
            time.sleep(1)
            # 勾选
            self.driver.find_element_by_xpath("//div[@title='代码-名称:ICBC-工商银行']/parent::*/preceding-sibling::*[1]/descendant::*[2]").click()
            time.sleep(3)

            # 输入指令类型：
            self.temp = self.driver.find_element_by_xpath("//input[@id='combobox-input-commandtype']")
            self.temp.click()
            # self.temp = self.driver.find_element_by_xpath("//input[@id='combobox-input-commandtype']")
            # self.driver.execute_script("$(arguments[0]).click()", self.temp)
            time.sleep(1)
            self.temp.send_keys(Keys.ENTER)
            time.sleep(1)

            # 点击查询
            self.driver.find_element_by_xpath("//span[text()='查询']").click()
            time.sleep(3)

            # 删除功能
            # 勾选
            # self.driver.find_element_by_xpath("//button[@class='f-grid-checkbox']").click()
            self.driver.find_element_by_xpath("//div[@title='指令类型:银行账户今日余额']/parent::*/preceding-sibling::*[4]/descendant::*[2]").click()
            time.sleep(1)

            # 点击删除按钮
            self.driver.find_element_by_xpath("//span[text()='删除']").click()

            # 点击弹出框的OK键
            self.driver.find_element_by_xpath("//button[@id='f-message-webgen-0-okBnt']").click()

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 用隐式等待方法等页面出现删除的提示框
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath("//span[contains(text(),'操作成功')]")
            print("删除‘直联查询指令配置’,成功！")
            time.sleep(3)

            # 切入'直联查询指令配置'的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='sysDirectQueryCmdConfigs-tab-iframe']"))

            # 用JS的方法点击新增按钮
            button = self.driver.find_element_by_xpath("//span[text()='新增']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 切入新增的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='addWin-iframe']"))

            # 输入‘银行’
            self.temp = self.driver.find_element_by_xpath("//input[@id='combobox-input-bankid']")
            self.temp.click()
            self.temp.send_keys("工商银行")
            time.sleep(1)
            self.temp.send_keys(Keys.ARROW_DOWN)
            self.temp.send_keys(Keys.ENTER)

            # 输入‘指令类型’
            self.temp = self.driver.find_element_by_xpath("//input[@id='combobox-input-commandtype']")
            self.temp.click()
            self.temp.send_keys("银行账户今日余额")
            time.sleep(1)
            self.temp.send_keys(Keys.ARROW_DOWN)
            self.temp.send_keys(Keys.ENTER)

            # 输入‘直联渠道’
            self.temp = self.driver.find_element_by_xpath("//input[@id='combobox-input-directchannelid']")
            self.temp.click()
            time.sleep(1)
            self.temp.send_keys(Keys.ARROW_DOWN)
            self.temp.send_keys(Keys.ARROW_DOWN)
            self.temp.send_keys(Keys.ENTER)

            # 输入‘直联渠道指令’
            self.temp = self.driver.find_element_by_xpath("//input[@id='combobox-input-directchannelcmdid']")
            self.temp.click()
            self.temp.send_keys("银行账户今日余额")
            time.sleep(1)
            self.temp.send_keys(Keys.ARROW_DOWN)
            self.temp.send_keys(Keys.ENTER)

            # 描述框中填入值
            self.driver.find_element_by_xpath("//textarea[@id='description']").send_keys("工商银行当日余额")
            time.sleep(2)

            # 点击保存按钮
            self.driver.find_element_by_xpath("//span[text()='保存']").click()

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 用隐式等待方法等页面出现提示框
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath("//span[contains(text(),'操作成功！')]")
            print('保存‘直联查询指令配置’,成功！')
            time.sleep(3)

            # 切入'直联查询指令配置'的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='sysDirectQueryCmdConfigs-tab-iframe']"))

            # 修改
            # 勾选
            self.driver.find_element_by_xpath("//div[@title='指令类型:银行账户今日余额']/parent::*/preceding-sibling::*[4]/descendant::*[2]").click()
            time.sleep(1)

            # 点击修改按钮
            self.driver.find_element_by_xpath("//span[text()='修改']").click()
            time.sleep(1)

            # 切入修改的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='modWin-iframe']"))

            # 修改描述框中的内容
            self.driver.find_element_by_xpath("//textarea[@id='description']").send_keys("自动化测试修改")
            time.sleep(2)

            # 点击保存按钮
            self.driver.find_element_by_xpath("//span[text()='保存']").click()

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 用隐式等待方法等页面出现新增成功的提示框
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath("//span[contains(text(),'操作成功！')]")
            print("修改‘直联查询指令配置’，成功！")
            time.sleep(3)

            # 用JS的方法关闭前端缓存刷新的页面
            button = self.driver.find_element_by_xpath("//a[@title='直联查询指令配置']/child::*[1]")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 打印成功
            print("‘直联查询指令配置’页面功能，完成!")
            logging.info("‘直联查询指令配置’页面功能，完成!")
            time.sleep(2)
        except Exception as err:
            # 发生其他异常时，打印异常堆栈信息
            print(traceback.print_exc())
            logging.debug("操作‘直联查询指令配置’页面功能，失败！" + str(traceback.format_exc()))




        # 测试‘加密工具’页面功能
        try:
            # 退出所有iframe窗体
            self.driver.switch_to.default_content()
            # 切入系统设置的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id ='systemconfig-tab-iframe']"))
            logging.info("开始测试‘加密工具’页面功能")

            # 用JS的方法点击基础资料下的'加密工具'
            button = self.driver.find_element_by_xpath("//span[@class='setitem_icon  sysEncryptTools_icon']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()
            # 切入'加密工具'的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='sysEncryptTools-tab-iframe']"))

            # 输入代码：
            self.temp = self.driver.find_element_by_xpath("//input[@id='password']")
            self.temp.send_keys("123456")

            # 点击加密按钮
            self.driver.find_element_by_xpath("//span[text()='加密']").click()

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 用隐式等待方法等页面出现提示框
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath("//span[contains(text(),'=#MjA')]")
            print("‘加密工具’成功")
            time.sleep(3)

            # 用JS的方法关闭前端缓存刷新的页面
            button = self.driver.find_element_by_xpath("//a[@title='加密工具']/child::*[1]")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 打印成功
            print("‘加密工具’页面功能，完成!")
            logging.info("‘加密工具’页面功能，完成!")
            time.sleep(2)
        except Exception as err:
            # 发生其他异常时，打印异常堆栈信息
            print(traceback.print_exc())
            logging.debug("操作‘加密工具’页面功能，失败！" + str(traceback.format_exc()))


        #测试‘银行分类’页面功能
        try:
            #退出所有iframe窗体
            self.driver.switch_to.default_content()
            #切入系统设置的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id ='systemconfig-tab-iframe']"))
            logging.info("开始测试‘银行分类’页面功能")

            # 用JS的方法点击基础资料下的'银行分类'
            button = self.driver.find_element_by_xpath("//span[@class='setitem_icon  syBankClass_icon']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            #退出所有iframe窗体
            self.driver.switch_to.default_content()
            #切入'银行分类'的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='syBankClass-tab-iframe']"))

            # 点击查看
            # 用JS的方法点击放大镜
            button = self.driver.find_element_by_xpath("//span[@class='f-contrac-close']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 输入代码：
            self.temp = self.driver.find_element_by_xpath("//input[@id='code']")
            self.temp.send_keys("0006")
            time.sleep(2)

            # 输入名称：
            self.temp = self.driver.find_element_by_xpath("//input[@id='name']")
            self.temp.send_keys("外资银行")
            time.sleep(2)

            #点击查询
            self.driver.find_element_by_xpath("//span[text()='查询']").click()
            time.sleep(3)

            #用隐式等待方法等页面出现提示框
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath("//div[@title='名称:外资银行']")
            print("银行分类查询成功!")
            logging.info("银行分类查询成功!")
            time.sleep(3)

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            #用JS的方法关闭前端缓存刷新的页面
            button = self.driver.find_element_by_xpath("//a[@title='银行分类']/child::*[1]")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 打印成功
            print("‘银行分类’页面，完成!")
            logging.info("‘银行分类’页面，完成!")
            time.sleep(2)
        except Exception as err:
            #发生其他异常时，打印异常堆栈信息
            print(traceback.print_exc())
            logging.debug("操作‘银行分类’页面功能失败！" + str(traceback.format_exc()))


        # 测试‘直联渠道款项性质’页面功能
        try:
            # 退出所有iframe窗体
            switch_default()
            # 切入系统设置的iframe窗体
            switch_to("xpath", "//iframe[@id='systemconfig-tab-iframe']")
            logging.info("开始测试‘直联渠道款项性质’功能")

            # 用JS的方法点击基础资料下的'贸易合同'
            js_click("xpath", "//a[@nname='直联渠道款项性质']")

            # 退出所有iframe窗体
            switch_default()
            # 切入'直联渠道款项性质'的iframe窗体
            switch_to("xpath", "//iframe[@id='sysDirectChannelFundProperty-tab-iframe']")

            # 点击查看
            # 用JS的方法点击放大镜
            js_click("xpath", "//span[@class='f-contrac-close']")
            sleep(1)

            #选择银行：
            #点击银行选择框
            click("xpath", "//input[@id='combobox-input-bankid']")
            sleep(1)
            #在选择区域框中输入‘CITIC-中信银行’
            input("xpath", "//input[@id='combobox-input-bankid']", "CITIC-中信银行")
            sleep(1)
            #鼠标往下，并且选择
            input_down("xpath", "//input[@id='combobox-input-bankid']")
            input_enter("xpath", "//input[@id='combobox-input-bankid']")

            # 点击查询
            click("xpath", "//span[text()='查询']")
            sleep(2)

            # 用隐式等待方法等页面出现提示框
            implici_wait("xpath", "//div[@title='银行:中信银行']")
            print("'直联渠道款项性质',查询成功!")
            logging.info("'直联渠道款项性质',查询成功！")
            time.sleep(3)

            # 退出所有iframe窗体
            switch_default()

            # 用JS的方法关闭自定义字段的页面
            js_click("xpath", "//a[@title='直联渠道款项性质']/child::*[1]")

            # 打印成功
            print("‘直联渠道款项性质’操作成功!")
            logging.info("‘直联渠道款项性质’操作成功!")
            time.sleep(2)
        except Exception as err:
            # 发生其他异常时，打印异常堆栈信息
            print(traceback.print_exc())
            logging.debug("操作‘直联渠道款项性质’，操作失败！" + str(traceback.format_exc()))


        # 测试‘直联账户地址’页面功能
        try:
            # 退出所有iframe窗体
            switch_default()
            # 切入系统设置的iframe窗体
            switch_to("xpath", "//iframe[@id='systemconfig-tab-iframe']")
            logging.info("开始测试‘直联账户地址’页面功能")

            # 用JS的方法点击直联设置下的'直联账户地址'
            js_click("xpath", "//a[@nname='直联账户地址']")

            # 退出所有iframe窗体
            switch_default()
            # 切入'直联账户地址'的iframe窗体
            switch_to("xpath", "//iframe[@id='sysDirectAccountAddr-tab-iframe']")

            # 用JS的方法点击新增按钮
            js_click("xpath", "//span[text()='新增']")

            # 切入新增的iframe窗体
            switch_to("xpath", "//iframe[@id='addWin-iframe']")

            # 输入‘国家’
            click("xpath", "//input[@id='combobox-input-countryid']")
            input("xpath", "//input[@id='combobox-input-countryid']", "中国")
            sleep(1)
            # 按键往下，选择‘中国’
            input_down("xpath", "//input[@id='combobox-input-countryid']")
            input_down("xpath", "//input[@id='combobox-input-countryid']")
            input_enter("xpath", "//input[@id='combobox-input-countryid']")
            sleep(1)

            # 输入‘省/州’
            click("xpath", "//input[@id='combobox-input-stateid']")
            input("xpath", "//input[@id='combobox-input-stateid']", "浙江")
            sleep(1)
            # 按键往下，选择‘浙江’
            input_down("xpath", "//input[@id='combobox-input-stateid']")
            input_enter("xpath", "//input[@id='combobox-input-stateid']")
            sleep(1)

            # 输入‘城市’
            input("xpath", "//input[@id='city']", "余杭区")
            sleep(1)

            # 输入‘街道’
            input("xpath", "//input[@id='street']", "余杭塘路")
            sleep(1)

            # 输入‘门牌号’
            input("xpath", "//input[@id='doorplate']", "1993号")
            sleep(1)

            # 输入‘邮政编码’
            input("xpath", "//input[@id='postcode']", "312000")
            sleep(1)

            # 描述框中填入值
            input("xpath", "//textarea[@id='description']", "自动化测试直联账户地址描述框")
            sleep(1)

            # 点击保存按钮
            click("xpath", "//span[text()='保存']")

            # 退出所有iframe窗体
            switch_default()

            # 用隐式等待方法等页面出现新增成功的提示框
            implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
            print("直联账户地址，保存成功！")
            logging.info("直联账户地址，保存成功！")
            time.sleep(3)

            # 切入'直联账户地址'的iframe窗体
            switch_to("xpath", "//iframe[@id='sysDirectAccountAddr-tab-iframe']")

            # 点击查看
            # 用JS的方法点击放大镜
            js_click("xpath", "//span[@class='f-contrac-close']")
            sleep(1)

            # 输入城市
            input("xpath", "//input[@id='city']", "余杭区")
            sleep(1)

            # 点击查询
            click("xpath", "//span[text()='查询']")

            # 修改
            # 勾选
            #click("xpath","//div[contains(@title,'组织:TestOrgSet-')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")
            #20210329修改
            click("xpath","//div[contains(@title,'国家:C-中国')]/parent::*/preceding-sibling::*[2]/descendant::*[2]")
            # 点击修改按钮
            click("xpath", "//span[text()='修改']")

            # 切入修改的iframe窗体
            switch_to("xpath", "//iframe[@id='modWin-iframe']")
            sleep(1)

            # 修改描述框中的内容
            input("xpath", "//textarea[@id='description']", "自动化测试修改")
            sleep(1)

            # 点击保存按钮
            click("xpath", "//span[text()='保存']")

            # 退出所有iframe窗体
            switch_default()

            # 用隐式等待方法等页面出现新增成功的提示框
            implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
            print("直联账户地址，修改成功！")
            logging.info("直联账户地址，修改成功！")
            time.sleep(3)

            # 切入'直联账户地址'的iframe窗体
            switch_to("xpath", "//iframe[@id='sysDirectAccountAddr-tab-iframe']")

            # 勾选
            #click("xpath","//div[contains(@title,'组织:TestOrgSet-')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")
            # 20210329修改
            click("xpath", "//div[contains(@title,'国家:C-中国')]/parent::*/preceding-sibling::*[2]/descendant::*[2]")
            # 点击删除按钮
            click("xpath", "//span[text()='删除']")

            # 点击弹出框的OK键
            click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

            # 退出所有iframe窗体
            switch_default()

            # 用隐式等待方法等页面出现删除的提示框
            implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
            print("直联账户地址，删除成功！")
            logging.info("直联账户地址，删除成功！")
            time.sleep(3)

            # 用JS的方法关闭当前页面
            js_click("xpath", "//a[@title='直联账户地址']/child::*[1]")

            # 打印操作成功日志
            print("直联账户地址，操作成功!")
            logging.info("直联账户地址，操作成功!")
            time.sleep(2)
        except Exception as err:
            # 发生其他异常时，打印异常堆栈信息
            print(traceback.print_exc())
            logging.debug("直联账户地址失败！" + str(traceback.format_exc()))
            # Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
            dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
            dir_path = make_current_hour_dir(dir_path + "\\")
            pic_path = os.path.join(dir_path, get_current_time() + ".png")
            capture(pic_path)

        # 退出所有iframe窗体
    #     switch_default()
    #
    #     # 点击页面退出按钮
    #     self.driver.find_element_by_xpath("//a[contains(.,'退出')]").click()
    #     time.sleep(1)
    #
    #     # 点击退出弹窗的'Yes'按钮
    #     self.driver.find_element_by_xpath("//button[contains(.,'Yes')]").click()
    #     time.sleep(2)
    #
    # def tearDown(self):
    #     self.driver.quit()
        print("结束时间：", time.strftime("%Y-%m-%d %H:%M:%S"))

if __name__ == '__main__':
    #  启动单元测试
    unittest.main(verbosity=2)