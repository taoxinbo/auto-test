#encoding=utf-8
# 2020-09-04
# TaoXB
# 此文件是自动化测试：系统设置--基础资料，下面的所有模块的增删改查，除了个性化模块除外（金融交易对手、龙湖组织架构、发薪信息）
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
class Syset_base(unittest.TestCase):

    #启动浏览器
    def setUp(self):

        #启动浏览器的另外一个方法：通过封装启动浏览器的驱动，启动不同浏览器

        self.driver = get("chrome")

    # 登陆系统、对系统设置进行操作
    def test_trade(self):

        #通过登陆封装函数，进行登陆
        #login( G_Ora_Url,TestUser,Password, "自动化测试租户")
        #login( G_Ora_Url,Tao, Password,"默认租户")
        #login( G_Mys_Url,TestUser,Password, "自动化测试租户")
        #login(G_Mys_Url, Tao, Password, "默认租户")

        #login(G_Ora_Url, 'judy', Password, "默认租户")
        #login(G_Mys_Url, 'Felix', Password, "默认租户")

        login(G_Ora_Url_Bd, 'Felix', Password, "默认租户")

        logging.info("开始测试系统设置--基础资料的页面功能")
        #点击菜单：系统设置
        click("xpath", "//div[@class='sysconfigset']")
        
        #测试前端刷新缓存功能
        try:
            #退出所有iframe窗体
            self.driver.switch_to.default_content()
            #切入系统设置的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("// iframe[ @ id = 'systemconfig-tab-iframe']"))
            logging.info("开始测试前端缓存刷新功能")

            # 用JS的方法点击基础资料下的'前端缓存'
            button = self.driver.find_element_by_xpath("//a[@nname='前端缓存刷新']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            #退出所有iframe窗体
            self.driver.switch_to.default_content()
            #切入前端缓存刷新的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='cacherefresh-tab-iframe']"))
            time.sleep(1)

            #勾选币种的缓存
            self.driver.find_element_by_xpath("//div[@title='缓存名称:币种']/parent::*/preceding-sibling::*[2]/descendant-or-self::*[3]").click()

            #点击刷新按钮
            self.driver.find_element_by_xpath("//span[text()='刷新']").click()

            #退出所有iframe窗体
            self.driver.switch_to.default_content()

            #用隐式等待方法等页面出现提示框
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath("//span[contains(text(),'缓存刷新成功!')]")
            time.sleep(3)

            #用JS的方法关闭前端缓存刷新的页面
            button = self.driver.find_element_by_xpath("//a[@title='前端缓存刷新']/child::*[1]")
            self.driver.execute_script("$(arguments[0]).click()", button)

            #打印操作成功日志
            print('前端缓存刷新成功!')
            logging.info("前端缓存刷新成功!")
            time.sleep(2)
        except Exception as err:
            #发生其他异常时，打印异常堆栈信息
            print(traceback.print_exc())
            logging.debug("前端缓存刷新失败！" + str(traceback.format_exc()))

        

        #测试：日历管理--日历的功能
        try:
            # 退出所有iframe窗体
            self.driver.switch_to.default_content()
            #切入系统设置的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("// iframe[ @ id = 'systemconfig-tab-iframe']"))
            logging.info("开始测试‘日历管理--日历’功能")

            # 用JS的方法点击基础资料下的'日历管理'
            button = self.driver.find_element_by_xpath("//a[@nname='日历管理']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            #退出所有iframe窗体
            self.driver.switch_to.default_content()
            #切入‘日历管理--日历’的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='calManager-tab-iframe']"))
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='subTabOne-iframe']"))
            time.sleep(1)

            # 连续新增2笔，第一笔用来测试删除按钮
            for i in range(1, 3):
                # 用JS的点击新增按钮
                button = self.driver.find_element_by_xpath("//span[text()='新增']")
                self.driver.execute_script("$(arguments[0]).click()", button)

                #切入新增的iframe窗体
                self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='addWin-iframe']"))

                #名称中填入值
                self.driver.find_element_by_xpath("//input[@id='name']").send_keys("自动化测试"+str(i))
                time.sleep(2)

                #勾选工作日是星期一前面的框
                self.driver.find_element_by_xpath("//input[@id='monday']").click()
                time.sleep(1)

                #描述框中填入值
                self.driver.find_element_by_xpath("//textarea[@id='description']").send_keys("自动化测试" + str(i))
                time.sleep(2)

                #点击保存按钮
                self.driver.find_element_by_xpath("//span[text()='保存']").click()

                #退出所有iframe窗体
                self.driver.switch_to.default_content()

                #用隐式等待方法等页面出现新增成功的提示框
                self.driver.implicitly_wait(60)
                self.driver.find_element_by_xpath("//span[contains(text(),'操作成功！')]")
                print('新增保存日历，第%s笔成功！' % i)
                time.sleep(3)

                #切入‘日历管理--日历’的iframe窗体
                self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='calManager-tab-iframe']"))
                self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='subTabOne-iframe']"))

            # 点击查看
            #用JS的方法点击放大镜
            button = self.driver.find_element_by_xpath("//span[@class='f-contrac-close']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 输入日历名称：
            self.temp = self.driver.find_element_by_xpath("//input[@id='name']")
            self.temp.send_keys("自动化测试")
            time.sleep(2)
            # 模拟回车键
            #keyDown('enter')
            #keyUp('enter')
            time.sleep(1)

            # 点击查询
            self.driver.find_element_by_xpath("//span[text()='查询']").click()
            time.sleep(2)

            #删除功能
            #勾选一个新增的日历
            self.driver.find_element_by_xpath("//div[@title='名称:自动化测试1']/parent::*/preceding-sibling::*[1]/descendant::*[2]").click()

            #点击删除按钮
            self.driver.find_element_by_xpath("//span[text()='删除']").click()

            # 点击弹出框的OK键
            self.driver.find_element_by_xpath("//button[@id='f-message-webgen-0-okBnt']").click()

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 用隐式等待方法等页面出现撤销送审成功的提示框
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath("//span[contains(text(),'操作成功！')]")
            print("删除‘日历’，成功")
            time.sleep(2)

            # 切入‘日历管理--日历’的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='calManager-tab-iframe']"))
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='subTabOne-iframe']"))

            #修改功能
            #勾选一个新增的日历
            self.driver.find_element_by_xpath("//div[@title='名称:自动化测试2']/parent::*/preceding-sibling::*[1]/descendant::*[2]").click()
            time.sleep(1)

            #点击修改按钮
            self.driver.find_element_by_xpath("//span[text()='修改']").click()
            time.sleep(1)

            #切入修改的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='modWin-iframe']"))

            # 勾选工作日是星期一前面的框
            self.driver.find_element_by_xpath("//input[@id='tuesday']").click()
            time.sleep(1)

            #修改描述框中的内容
            self.driver.find_element_by_xpath("//textarea[@id='description']").send_keys("自动化测试修改")
            time.sleep(2)

            #点击保存按钮
            self.driver.find_element_by_xpath("//span[text()='保存']").click()

            #退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 用隐式等待方法等页面出现新增成功的提示框
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath("//span[contains(text(),'操作成功！')]")
            print('修改‘日历’，成功！' )
            time.sleep(3)

            # 切入‘日历管理--日历’的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='calManager-tab-iframe']"))
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='subTabOne-iframe']"))

            #失效按钮
            #勾选一个新增的日历
            self.driver.find_element_by_xpath("//div[@title='名称:自动化测试2']/parent::*/preceding-sibling::*[1]/descendant::*[2]").click()
            time.sleep(1)

            # 点击失效按钮
            self.driver.find_element_by_xpath("//span[text()='失效']").click()
            time.sleep(1)

            # 点击弹出框的OK键
            self.driver.find_element_by_xpath("//button[@id='f-message-webgen-0-okBnt']").click()

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 用隐式等待方法等页面出现新增成功的提示框
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath("//span[contains(text(),'失效成功！')]")
            print('点击失效成功！')
            time.sleep(3)

            # 切入‘日历管理--日历’的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='calManager-tab-iframe']"))
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='subTabOne-iframe']"))

            # 生效按钮
            # 勾选一个新增的日历
            self.driver.find_element_by_xpath("//div[@title='名称:自动化测试2']/parent::*/preceding-sibling::*[1]/descendant::*[2]").click()
            time.sleep(1)

            # 点击生效按钮
            self.driver.find_element_by_xpath("//span[text()='生效']").click()
            time.sleep(1)

            # 点击弹出框的OK键
            self.driver.find_element_by_xpath("//button[@id='f-message-webgen-0-okBnt']").click()

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 用隐式等待方法等页面出现新增成功的提示框
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath("//span[contains(text(),'生效成功！')]")
            print('点击生效成功！')
            time.sleep(3)

            #用JS的方法关闭前端缓存刷新的页面
            button = self.driver.find_element_by_xpath("//a[@title='日历管理']/child::*[1]")
            self.driver.execute_script("$(arguments[0]).click()", button)

            #打印操作成功日志
            print('‘日历管理--日历’，操作成功!')
            logging.info("‘日历管理--日历’，操作成功!")
            time.sleep(2)
        except Exception as err:
            # 发生其他异常时，打印异常堆栈信息
            print(traceback.print_exc())
            logging.debug("‘日历管理--日历’，操作失败！" + str(traceback.format_exc()))



        # 测试：日历管理--特殊节假日的功能
        try:
            # 退出所有iframe窗体
            self.driver.switch_to.default_content()
            # 切入系统设置的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("// iframe[@id= 'systemconfig-tab-iframe']"))
            logging.info("开始测试‘日历管理--特殊节假日’功能")

            # 用JS的方法点击基础资料下的'日历管理'
            button = self.driver.find_element_by_xpath("//a[@nname='日历管理']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            #退出所有iframe窗体
            self.driver.switch_to.default_content()
            # 切入‘日历管理--特殊节假日’的第一个iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='calManager-tab-iframe']"))

            #点击特殊节假日页面
            self.driver.find_element_by_xpath("//span[text()='特殊节假日']").click()

            #切入‘日历管理--特殊节假日’的第二个iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='subTabTwo-iframe']"))
            time.sleep(1)


            # 用JS的点击新增按钮
            button = self.driver.find_element_by_xpath("//span[text()='新增']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 切入新增的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='addWin-iframe']"))

            #选择日历内容
            self.temp=self.driver.find_element_by_xpath("//input[@id='combobox-input-calendarid']")
            self.temp.click()
            self.temp.send_keys("自动化测试2")
            time.sleep(1)
            self.temp.send_keys(Keys.ARROW_DOWN)
            self.temp.send_keys(Keys.ENTER)
            time.sleep(1)

            #输入日期名称
            self.driver.find_element_by_xpath("//input[@id='name']").send_keys("自动化测试" )
            time.sleep(2)

            #描述框中填入值
            self.driver.find_element_by_xpath("//textarea[@id='description']").send_keys("自动化测试" )
            time.sleep(2)

            #选择日期
            today = date.today()
            self.driver.find_element_by_xpath("//input[@id='specialdate-input']").send_keys(str(today))
            # 模拟回车键
            keyDown('enter')
            keyUp('enter')
            time.sleep(2)

            #点击保存按钮
            self.driver.find_element_by_xpath("//span[text()='保存']").click()

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 用隐式等待方法等页面出现新增成功的提示框
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath("//span[contains(text(),'操作成功！')]")
            print('新增‘特殊节假日’，成功！')
            time.sleep(3)

            # 切入‘日历管理--特殊节假日’的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='calManager-tab-iframe']"))
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='subTabTwo-iframe']"))

            # 点击查看
            #用JS的方法点击放大镜
            button = self.driver.find_element_by_xpath("//span[@class='f-contrac-close']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 输入日历名称：
            self.temp = self.driver.find_element_by_xpath("//input[@id='name']")
            self.temp.send_keys("自动化测试")
            time.sleep(2)

            # 点击查询
            self.driver.find_element_by_xpath("//span[text()='查询']").click()
            time.sleep(2)

            #修改功能
            #勾选
            self.driver.find_element_by_xpath("//div[@title='日期名称:自动化测试']/parent::*/preceding-sibling::*[3]/descendant::*[2]").click()
            time.sleep(1)

            #点击修改按钮
            self.driver.find_element_by_xpath("//span[text()='修改']").click()
            time.sleep(1)

            #切入修改的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='modWin-iframe']"))

            #修改描述框中的内容
            self.driver.find_element_by_xpath("//textarea[@id='description']").send_keys("自动化测试修改")
            time.sleep(2)

            #点击保存按钮
            self.driver.find_element_by_xpath("//span[text()='保存']").click()

            #退出所有iframe窗体
            self.driver.switch_to.default_content()

            #用隐式等待方法等页面出现新增成功的提示框
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath("//span[contains(text(),'操作成功！')]")
            print('‘特殊节假日’，修改成功！' )
            time.sleep(3)

            # 切入‘日历管理--特殊节假日’的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='calManager-tab-iframe']"))
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='subTabTwo-iframe']"))

            #失效按钮
            #勾选一个新增的日历
            self.driver.find_element_by_xpath("//div[@title='日期名称:自动化测试']/parent::*/preceding-sibling::*[3]/descendant::*[2]").click()
            time.sleep(1)

            # 点击失效按钮
            self.driver.find_element_by_xpath("//span[text()='失效']").click()
            time.sleep(1)

            # 点击弹出框的OK键
            self.driver.find_element_by_xpath("//button[@id='f-message-webgen-0-okBnt']").click()

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 用隐式等待方法等页面出现新增成功的提示框
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath("//span[contains(text(),'失效成功！')]")
            print('点击失效成功！')
            time.sleep(3)

            # 切入‘日历管理--特殊节假日’的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='calManager-tab-iframe']"))
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='subTabTwo-iframe']"))

            # 生效按钮
            # 勾选一个新增的日历
            self.driver.find_element_by_xpath("//div[@title='日期名称:自动化测试']/parent::*/preceding-sibling::*[3]/descendant::*[2]").click()
            time.sleep(1)

            # 点击生效按钮
            self.driver.find_element_by_xpath("//span[text()='生效']").click()
            time.sleep(1)

            # 点击弹出框的OK键
            self.driver.find_element_by_xpath("//button[@id='f-message-webgen-0-okBnt']").click()

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 用隐式等待方法等页面出现新增成功的提示框
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath("//span[contains(text(),'生效成功！')]")
            print('点击生效成功！')
            time.sleep(3)

            # 切入‘日历管理--特殊节假日’的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='calManager-tab-iframe']"))
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='subTabTwo-iframe']"))

            # 删除功能
            # 勾选
            self.driver.find_element_by_xpath("//div[@title='日期名称:自动化测试']/parent::*/preceding-sibling::*[3]/descendant::*[2]").click()

            # 点击删除按钮
            self.driver.find_element_by_xpath("//span[text()='删除']").click()

            # 点击弹出框的OK键
            self.driver.find_element_by_xpath("//button[@id='f-message-webgen-0-okBnt']").click()

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 用隐式等待方法等页面出现撤销送审成功的提示框
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath("//span[contains(text(),'操作成功！')]")
            print("‘特殊节假日’，删除成功")
            time.sleep(2)

            #删除‘日历管理-日历’的数据
            #切入‘日历管理’的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='calManager-tab-iframe']"))

            #点击‘日历管理-日历’页面
            self.driver.find_element_by_xpath("//span[text()='日历']").click()

            # 切入‘日历管理-日历’的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='subTabOne-iframe']"))

            # 勾选另外一个日历
            self.driver.find_element_by_xpath("//div[@title='名称:自动化测试2']/parent::*/preceding-sibling::*[1]/descendant::*[2]").click()

            # 点击删除按钮
            self.driver.find_element_by_xpath("//span[text()='删除']").click()

            # 点击弹出框的OK键
            self.driver.find_element_by_xpath("//button[@id='f-message-webgen-0-okBnt']").click()

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 用隐式等待方法等页面出现撤销送审成功的提示框
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath("//span[contains(text(),'操作成功！')]")
            print("删除第二个‘日历’，成功")
            time.sleep(2)

            #用JS的方法关闭前端缓存刷新的页面
            button = self.driver.find_element_by_xpath("//a[@title='日历管理']/child::*[1]")
            self.driver.execute_script("$(arguments[0]).click()", button)

            #打印操作成功日志
            print('‘日历管理--特殊节假日’，操作成功!')
            logging.info("‘日历管理--特殊节假日’，操作成功!")
            time.sleep(2)
        except Exception as err:
            # 发生其他异常时，打印异常堆栈信息
            print(traceback.print_exc())
            logging.debug("‘日历管理--特殊节假日’，操作失败！" + str(traceback.format_exc()))

        
        
        # 测试：日历管理--工作周的功能
        try:
            # 退出所有iframe窗体
            self.driver.switch_to.default_content()
            # 切入系统设置的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("// iframe[@id= 'systemconfig-tab-iframe']"))
            logging.info("开始测试‘日历管理--工作周’功能")

            # 用JS的方法点击基础资料下的'日历管理'
            button = self.driver.find_element_by_xpath("//a[@nname='日历管理']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            #退出所有iframe窗体
            self.driver.switch_to.default_content()
            # 切入‘日历管理--工作周’的第一个iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='calManager-tab-iframe']"))

            #点击特殊节假日页面
            self.driver.find_element_by_xpath("//span[text()='工作周']").click()

            #切入‘日历管理--特殊节假日’的第二个iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='subTabThree-iframe']"))
            time.sleep(1)

            # 连续新增2笔
            for i in range(1, 3):
                # 用JS的点击新增按钮
                button = self.driver.find_element_by_xpath("//span[text()='新增']")
                self.driver.execute_script("$(arguments[0]).click()", button)

                # 切入新增的iframe窗体
                self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='addWin-iframe']"))

                # 选择年份
                #点击年份输入框
                self.driver.find_element_by_xpath("//input[@id='budgetyear-input']").click()
                # 退出所有iframe窗体
                self.driver.switch_to.default_content()
                # 切入年份的iframe窗体
                self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@hidefocus='true']"))
                #点击清库按钮
                self.driver.find_element_by_xpath("//input[@value='清空']").click()

                # 退出所有iframe窗体
                self.driver.switch_to.default_content()
                # 切入‘日历管理--工作周’的第一个iframe窗体
                self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='calManager-tab-iframe']"))
                # 切入‘日历管理--特殊节假日’的第二个iframe窗体
                self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='subTabThree-iframe']"))
                # 切入新增的iframe窗体
                self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='addWin-iframe']"))

                temp = int(time.strftime("%Y")) + i
                #print(temp)
                self.driver.find_element_by_xpath("//input[@id='budgetyear-input']").send_keys(str(temp))
                # 模拟回车键
                keyDown('enter')
                keyUp('enter')
                time.sleep(2)

                #选择是否跨月
                self.driver.find_element_by_xpath("//input[@id='isovermonth']").click()

                #描述框中填入值
                self.driver.find_element_by_xpath("//textarea[@id='description']").send_keys("自动化测试" + str(i))
                time.sleep(2)

                #工作明细的名称中输入值
                self.driver.find_element_by_xpath("//input[@id='detailgrid-name-0']").send_keys("自动化测试" + str(i))
                time.sleep(2)

                # 工作明细的描述中输入值
                self.driver.find_element_by_xpath("//input[@id='detailgrid-description-0']").send_keys("自动化测试" + str(i))
                time.sleep(2)

                #点击保存按钮
                self.driver.find_element_by_xpath("//span[text()='保存']").click()

                # 退出所有iframe窗体
                self.driver.switch_to.default_content()

                # 用隐式等待方法等页面出现新增成功的提示框
                self.driver.implicitly_wait(60)
                self.driver.find_element_by_xpath("//span[contains(text(),'操作成功！')]")
                print('新增保存第%s笔成功！' % i)
                time.sleep(3)

                # 切入‘日历管理--工作周’的iframe窗体
                self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='calManager-tab-iframe']"))
                self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='subTabThree-iframe']"))

            # 点击查看
            #用JS的方法点击放大镜
            button = self.driver.find_element_by_xpath("//span[@class='f-contrac-close']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 输入日历名称：
            self.temp = self.driver.find_element_by_xpath("//input[@id='combobox-input-isovermonth']")
            self.temp.click()
            self.temp.send_keys("是")
            time.sleep(1)
            self.temp.send_keys(Keys.ARROW_DOWN)
            self.temp.send_keys(Keys.ENTER)

            # 点击查询
            self.driver.find_element_by_xpath("//span[text()='查询']").click()
            time.sleep(2)

            #删除功能
            #勾选一个新增的日历
            self.driver.find_element_by_xpath("//div[@title='描述:自动化测试1']/parent::*/preceding-sibling::*[5]/descendant::*[2]").click()

            #点击删除按钮
            self.driver.find_element_by_xpath("//span[text()='删除']").click()

            # 点击弹出框的OK键
            self.driver.find_element_by_xpath("//button[@id='f-message-webgen-0-okBnt']").click()

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 用隐式等待方法等页面出现撤销送审成功的提示框
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath("//span[contains(text(),'操作成功！')]")
            print("删除‘第一个工作周’，成功")
            time.sleep(3)

            # 切入‘日历管理--工作周’的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='calManager-tab-iframe']"))
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='subTabThree-iframe']"))

            # 修改功能
            # 勾选一个新增的日历
            self.driver.find_element_by_xpath("//div[@title='描述:自动化测试2']/parent::*/preceding-sibling::*[5]/descendant::*[2]").click()
            time.sleep(1)

            # 点击修改按钮
            self.driver.find_element_by_xpath("//span[text()='修改']").click()
            time.sleep(1)

            # 切入修改的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='modWin-iframe']"))

            # 修改描述框中的内容
            self.driver.find_element_by_xpath("//textarea[@id='description']").send_keys("修改")
            time.sleep(2)

            # 点击保存按钮
            self.driver.find_element_by_xpath("//span[text()='保存']").click()

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 用隐式等待方法等页面出现新增成功的提示框
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath("//span[contains(text(),'操作成功！')]")
            print('修改成功！')
            time.sleep(3)

            # 切入‘日历管理--工作周’的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='calManager-tab-iframe']"))
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='subTabThree-iframe']"))

            # 删除新增的第二个工作周
            # 勾选第二个工作周
            self.driver.find_element_by_xpath("//div[@title='描述:自动化测试2修改']/parent::*/preceding-sibling::*[5]/descendant::*[2]").click()

            # 点击删除按钮
            self.driver.find_element_by_xpath("//span[text()='删除']").click()

            # 点击弹出框的OK键
            self.driver.find_element_by_xpath("//button[@id='f-message-webgen-0-okBnt']").click()

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 用隐式等待方法等页面出现撤销送审成功的提示框
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath("//span[contains(text(),'操作成功！')]")
            print("删除‘第二个工作周’，成功")
            time.sleep(3)

            #用JS的方法关闭前端缓存刷新的页面
            button = self.driver.find_element_by_xpath("//a[@title='日历管理']/child::*[1]")
            self.driver.execute_script("$(arguments[0]).click()", button)

            #打印操作成功日志
            print('‘日历管理--工作周’，操作成功!')
            logging.info("‘日历管理--工作周’，操作成功!")
            time.sleep(2)
        except Exception as err:
            # 发生其他异常时，打印异常堆栈信息
            print(traceback.print_exc())
            logging.debug("‘日历管理--工作周’，操作失败！" + str(traceback.format_exc()))



        
        # 测试：币种功能
        try:
            # 退出所有iframe窗体
            self.driver.switch_to.default_content()
            #切入系统设置的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id ='systemconfig-tab-iframe']"))
            logging.info("开始测试‘币种’功能")

            # 用JS的方法点击基础资料下的'币种'
            button = self.driver.find_element_by_xpath("//a[@nname='币种']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            #退出所有iframe窗体
            self.driver.switch_to.default_content()
            #切入币种的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='currencyManager-tab-iframe']"))

            # 连续新增2笔，第一笔用来测试删除按钮
            for i in range(1, 3):
                # 用JS的方法点击新增按钮
                button = self.driver.find_element_by_xpath("//span[text()='新增']")
                self.driver.execute_script("$(arguments[0]).click()", button)

                #切入新增的iframe窗体
                self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='addWin-iframe']"))

                #输入代码
                self.driver.find_element_by_xpath("//input[@id='code']").send_keys("test" + str(i))
                time.sleep(2)

                #输入名称
                self.driver.find_element_by_xpath("//input[@id='name']").send_keys("自动化测试" + str(i))
                time.sleep(2)

                #选择直联币种代码
                self.temp = self.driver.find_element_by_xpath("//input[@id='directcurcode']")
                self.temp.click()
                self.temp.send_keys("人民币-123")
                time.sleep(1)
                #self.temp.send_keys(Keys.ARROW_DOWN)
                #self.temp.send_keys(Keys.ENTER)

                #描述框中填入值
                self.driver.find_element_by_xpath("//textarea[@id='description']").send_keys("自动化测试" + str(i))
                time.sleep(2)

                # 点击保存按钮
                self.driver.find_element_by_xpath("//span[text()='保存']").click()

                # 退出所有iframe窗体
                self.driver.switch_to.default_content()

                # 用隐式等待方法等页面出现新增成功的提示框
                self.driver.implicitly_wait(60)
                self.driver.find_element_by_xpath("//span[contains(text(),'操作成功！')]")
                print('新增保存币种，第%s笔成功！' % i)
                time.sleep(3)

                # 切入‘币种’的iframe窗体
                self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='currencyManager-tab-iframe']"))

            # 点击查看
            #用JS的方法点击放大镜
            button = self.driver.find_element_by_xpath("//span[@class='f-contrac-close']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 输入币种代码：
            self.temp = self.driver.find_element_by_xpath("//input[@id='code']")
            self.temp.send_keys("test")
            time.sleep(1)

            # 点击查询
            self.driver.find_element_by_xpath("//span[text()='查询']").click()
            time.sleep(2)

            #删除功能
            #勾选一个新增的币种
            self.driver.find_element_by_xpath("//div[@title='代码:test1']/parent::*/preceding-sibling::*[1]/descendant::*[2]").click()

            #点击删除按钮
            self.driver.find_element_by_xpath("//span[text()='删除']").click()

            # 点击弹出框的OK键
            self.driver.find_element_by_xpath("//button[@id='f-message-webgen-0-okBnt']").click()

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 用隐式等待方法等页面出现撤销送审成功的提示框
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath("//span[contains(text(),'操作成功！')]")
            print("删除‘币种’，成功")
            time.sleep(3)

            # 切入‘日历管理--工作周’的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='currencyManager-tab-iframe']"))

            # 修改功能
            # 勾选
            self.driver.find_element_by_xpath("//div[@title='代码:test2']/parent::*/preceding-sibling::*[1]/descendant::*[2]").click()
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
            print('修改‘币种’，成功！')
            time.sleep(3)

            # 用JS的方法关闭币种的页面
            button = self.driver.find_element_by_xpath("//a[@title='币种']/child::*[1]")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 打印操作成功日志
            print('币种操作成功!')
            logging.info("币种操作成功!")
            time.sleep(2)
        except Exception as err:
            # 发生其他异常时，打印异常堆栈信息
            print(traceback.print_exc())
            logging.debug("‘币种’，操作失败！" + str(traceback.format_exc()))
    


        # 测试：币种对
        try:
            # 退出所有iframe窗体
            self.driver.switch_to.default_content()
            #切入系统设置的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='systemconfig-tab-iframe']"))
            logging.info("开始测试‘币种对’功能")

            # 用JS的方法点击基础资料下的'币种书'
            button = self.driver.find_element_by_xpath("//a[@nname='币种对']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            #退出所有iframe窗体
            self.driver.switch_to.default_content()
            #切入币种的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='currencyPairManager-tab-iframe']"))

            # 用JS的方法点击新增按钮
            button = self.driver.find_element_by_xpath("//span[text()='新增']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 切入新增的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='addWin-iframe']"))

            # 输入基准货币
            click("xpath", "//input[@id='combobox-input-sourcecurrencyid']")
            input("xpath", "//input[@id='combobox-input-sourcecurrencyid']","test2-自动化测试2")
            sleep(1)
            input_down("xpath", "//input[@id='combobox-input-sourcecurrencyid']")
            input_enter("xpath", "//input[@id='combobox-input-sourcecurrencyid']")


            # 输入询价货币
            self.temp = self.driver.find_element_by_xpath("//input[@id='combobox-input-targetcecurrencyid']")
            self.temp.click()
            self.temp.send_keys("CNY-人民币")
            time.sleep(1)
            self.temp.send_keys(Keys.ARROW_DOWN)
            self.temp.send_keys(Keys.ENTER)

            #输入小数点位数
            self.driver.find_element_by_xpath("//input[@id='rounding-input']").send_keys("4")
            time.sleep(1)

            # 描述框中填入值
            self.driver.find_element_by_xpath("//textarea[@id='description']").send_keys("自动化测试")
            time.sleep(2)

            # 点击保存按钮
            self.driver.find_element_by_xpath("//span[text()='保存']").click()

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 用隐式等待方法等页面出现新增成功的提示框
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath("//span[contains(text(),'操作成功！')]")
            print('新增保存‘币种对’，成功！')
            time.sleep(3)

            # 切入‘币种对’的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='currencyPairManager-tab-iframe']"))

            # 点击查看
            #用JS的方法点击放大镜
            button = self.driver.find_element_by_xpath("//span[@class='f-contrac-close']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            #输入基准货币：
            self.temp = self.driver.find_element_by_xpath("//input[@id='combobox-input-sourcecurrencyid']")
            self.temp.click()
            sleep(1)
            clear("xpath", "//input[@id='combobox-input-sourcecurrencyid']")
            sleep(1)
            self.temp.send_keys("test2-自动化测试2")
            time.sleep(1)
            #选中"test2-自动化测试2"前面的复选框
            self.driver.find_element_by_xpath("//div[@title='代码-名称:test2-自动化测试2']/parent::*/preceding-sibling::*[1]/descendant::*[2]").click()
            time.sleep(1)

            #点击查询
            self.driver.find_element_by_xpath("//span[text()='查询']").click()
            time.sleep(2)

            #修改
            # 修改功能
            # 勾选一个新增的货币对
            self.driver.find_element_by_xpath("//div[@title='基准货币:test2-自动化测试2']/parent::*/preceding-sibling::*[1]/descendant::*[2]").click()
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
            print('修改‘币种对’，成功！')
            time.sleep(3)

            # 切入‘币种对’的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='currencyPairManager-tab-iframe']"))

            #删除功能
            #勾选一个新增的日历
            self.driver.find_element_by_xpath("//div[@title='基准货币:test2-自动化测试2']/parent::*/preceding-sibling::*[1]/descendant::*[2]").click()

            #点击删除按钮
            self.driver.find_element_by_xpath("//span[text()='删除']").click()

            # 点击弹出框的OK键
            self.driver.find_element_by_xpath("//button[@id='f-message-webgen-0-okBnt']").click()

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 用隐式等待方法等页面出现撤销送审成功的提示框
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath("//span[contains(text(),'操作成功！')]")
            print("删除‘币种对’，成功")
            time.sleep(3)

            # 用JS的方法关闭币种的页面
            button = self.driver.find_element_by_xpath("//a[@title='币种对']/child::*[1]")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 打印操作成功日志
            print('币种对操作成功!')
            logging.info("币种对操作成功!")
            time.sleep(2)

            #删除新增的第二‘币种：test2’
            # 退出所有iframe窗体
            self.driver.switch_to.default_content()
            # 切入系统设置的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id ='systemconfig-tab-iframe']"))

            # 用JS的方法点击基础资料下的'币种'
            button = self.driver.find_element_by_xpath("//a[@nname='币种']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()
            # 切入币种的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='currencyManager-tab-iframe']"))

            # 点击查看
            #用JS的方法点击放大镜
            button = self.driver.find_element_by_xpath("//span[@class='f-contrac-close']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 输入币种代码：
            self.temp = self.driver.find_element_by_xpath("//input[@id='code']")
            self.temp.send_keys("test")
            time.sleep(1)

            # 点击查询
            self.driver.find_element_by_xpath("//span[text()='查询']").click()
            time.sleep(2)

            #删除功能
            #勾选第二个币种
            self.driver.find_element_by_xpath("//div[@title='代码:test2']/parent::*/preceding-sibling::*[1]/descendant::*[2]").click()

            #点击删除按钮
            self.driver.find_element_by_xpath("//span[text()='删除']").click()

            # 点击弹出框的OK键
            self.driver.find_element_by_xpath("//button[@id='f-message-webgen-0-okBnt']").click()

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 用隐式等待方法等页面出现撤销送审成功的提示框
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath("//span[contains(text(),'操作成功！')]")
            print("删除第二个币种成功")
            time.sleep(3)

            # 用JS的方法关闭币种的页面
            button = self.driver.find_element_by_xpath("//a[@title='币种']/child::*[1]")
            self.driver.execute_script("$(arguments[0]).click()", button)

        except Exception as err:
            # 发生其他异常时，打印异常堆栈信息
            print(traceback.print_exc())
            logging.debug("‘币种对’，操作失败！" + str(traceback.format_exc()))



        # 测试：汇率--汇率类型
        try:
            # 退出所有iframe窗体
            self.driver.switch_to.default_content()
            #切入系统设置的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='systemconfig-tab-iframe']"))
            logging.info("开始测试‘汇率--汇率类型’功能")

            # 用JS的方法点击基础资料下的'汇率'
            button = self.driver.find_element_by_xpath("//a[@nname='汇率']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            #退出所有iframe窗体
            self.driver.switch_to.default_content()
            #切入汇率的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='currencyRateManager-tab-iframe']"))
            # 切入‘汇率--汇率类型’的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='subTabOne-iframe']"))

            # 连续新增2笔
            for i in range(1, 3):
                # 用JS的方法点击新增按钮
                button = self.driver.find_element_by_xpath("//span[text()='新增']")
                self.driver.execute_script("$(arguments[0]).click()", button)

                # 切入新增的iframe窗体
                self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='addWin-iframe']"))

                #输入代码
                self.driver.find_element_by_xpath("//input[@id='code']").send_keys("test" + str(i))
                time.sleep(2)

                #输入名称
                self.driver.find_element_by_xpath("//input[@id='name']").send_keys("自动化测试" + str(i))
                time.sleep(2)

                #描述框中填入值
                self.driver.find_element_by_xpath("//textarea[@id='description']").send_keys("自动化测试" + str(i))
                time.sleep(2)

                # 点击保存按钮
                self.driver.find_element_by_xpath("//span[text()='保存']").click()

                # 退出所有iframe窗体
                self.driver.switch_to.default_content()

                # 用隐式等待方法等页面出现新增成功的提示框
                self.driver.implicitly_wait(60)
                self.driver.find_element_by_xpath("//span[contains(text(),'操作成功！')]")
                print('新增保存汇率类型，第%s笔成功！' % i)
                time.sleep(3)

                # 切入汇率的iframe窗体
                self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='currencyRateManager-tab-iframe']"))
                # 切入‘汇率--汇率类型’的iframe窗体
                self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='subTabOne-iframe']"))

            # 点击查看
            #用JS的方法点击放大镜
            button = self.driver.find_element_by_xpath("//span[@class='f-contrac-close']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 输入币种代码：
            self.temp = self.driver.find_element_by_xpath("//input[@id='code']")
            self.temp.send_keys("test1")
            time.sleep(1)

            # 点击查询
            self.driver.find_element_by_xpath("//span[text()='查询']").click()
            time.sleep(2)

            #修改功能
            #勾选一个查询出的汇率
            self.driver.find_element_by_xpath("//div[@title='代码:test1']/parent::*/preceding-sibling::*[1]/descendant::*[2]").click()
            time.sleep(1)

            #点击修改按钮
            self.driver.find_element_by_xpath("//span[text()='修改']").click()
            time.sleep(1)

            #切入修改的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='modWin-iframe']"))

            #修改描述框中的内容
            self.driver.find_element_by_xpath("//textarea[@id='description']").send_keys("自动化测试修改")
            time.sleep(2)

            #点击保存按钮
            self.driver.find_element_by_xpath("//span[text()='保存']").click()

            #退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 用隐式等待方法等页面出现新增成功的提示框
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath("//span[contains(text(),'操作成功！')]")
            print('修改汇率类型，成功！' )
            time.sleep(3)

            #切入汇率的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='currencyRateManager-tab-iframe']"))
            # 切入‘汇率--汇率类型’的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='subTabOne-iframe']"))

            #失效按钮
            #勾选一个新增的日历
            self.driver.find_element_by_xpath("//div[@title='代码:test1']/parent::*/preceding-sibling::*[1]/descendant::*[2]").click()
            time.sleep(1)

            # 点击失效按钮
            self.driver.find_element_by_xpath("//span[text()='失效']").click()
            time.sleep(1)

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 用隐式等待方法等页面出现新增成功的提示框
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath("//span[contains(text(),'失效成功！')]")
            print('点击失效成功！')
            time.sleep(3)

            #切入汇率的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='currencyRateManager-tab-iframe']"))
            # 切入‘汇率--汇率类型’的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='subTabOne-iframe']"))

            # 生效按钮
            # 勾选一个新增的日历
            self.driver.find_element_by_xpath("//div[@title='代码:test1']/parent::*/preceding-sibling::*[1]/descendant::*[2]").click()
            time.sleep(1)

            # 点击生效按钮
            self.driver.find_element_by_xpath("//span[text()='生效']").click()
            time.sleep(1)

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 用隐式等待方法等页面出现新增成功的提示框
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath("//span[contains(text(),'生效成功！')]")
            print('点击生效成功！')
            time.sleep(3)

            #切入汇率的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='currencyRateManager-tab-iframe']"))
            # 切入‘汇率--汇率类型’的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='subTabOne-iframe']"))

            #点击‘重置’查询
            #点击查询按钮旁边的倒三角
            self.driver.find_element_by_xpath("//em[@class='f-btngroup-click']").click()
            time.sleep(1)
            # 点击重置按钮
            self.driver.find_element_by_xpath("//a[text()='重置']").click()
            time.sleep(1)

            #删除功能
            #勾选2个
            self.driver.find_element_by_xpath("//div[@title='代码:test1']/parent::*/preceding-sibling::*[1]/descendant::*[2]").click()
            self.driver.find_element_by_xpath("//div[@title='代码:test2']/parent::*/preceding-sibling::*[1]/descendant::*[2]").click()

            #点击删除按钮
            self.driver.find_element_by_xpath("//span[text()='删除']").click()

            # 点击弹出框的OK键
            self.driver.find_element_by_xpath("//button[@id='f-message-webgen-0-okBnt']").click()

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 用隐式等待方法等页面出现撤销送审成功的提示框
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath("//span[contains(text(),'操作成功！')]")
            print("删除汇率类型，成功")
            time.sleep(2)

            # 用JS的方法关闭汇率的页面
            button = self.driver.find_element_by_xpath("//a[@title='汇率']/child::*[1]")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 打印操作成功日志
            print('‘汇率--汇率类型’操作成功!')
            logging.info("‘汇率--汇率类型’操作成功!")
            time.sleep(2)
        except Exception as err:
            # 发生其他异常时，打印异常堆栈信息
            print(traceback.print_exc())
            logging.debug("‘汇率--汇率类型’，操作失败！" + str(traceback.format_exc()))

        
        
        # 测试：汇率--汇率
        try:
            # 退出所有iframe窗体
            self.driver.switch_to.default_content()
            #切入系统设置的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='systemconfig-tab-iframe']"))
            logging.info("开始测试‘汇率--汇率’功能")

            # 用JS的方法点击基础资料下的'汇率'
            button = self.driver.find_element_by_xpath("//a[@nname='汇率']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            #退出所有iframe窗体
            self.driver.switch_to.default_content()
            #切入汇率的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='currencyRateManager-tab-iframe']"))

            #点击汇率页面
            self.driver.find_element_by_xpath("//span[text()='汇率']").click()

            # 切入‘汇率--汇率’的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='subTabTwo-iframe']"))

            # 连续新增2笔
            for i in range(1, 3):
                # 用JS的方法点击新增按钮
                button = self.driver.find_element_by_xpath("//span[text()='新增']")
                self.driver.execute_script("$(arguments[0]).click()", button)

                # 切入新增的iframe窗体
                self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='addWin-iframe']"))

                #选择币种对
                self.temp = self.driver.find_element_by_xpath("//input[@id='combobox-input-currencypairid']")
                self.temp.click()
                self.temp.send_keys("人民币/美元")
                time.sleep(1)
                self.temp.send_keys(Keys.ARROW_DOWN)
                self.temp.send_keys(Keys.ENTER)

                #选择日期
                #点击日期控件
                self.driver.find_element_by_xpath("//input[@id='ratedate-input']").click()
                #退出所有iframe窗体
                self.driver.switch_to.default_content()
                #进入选择日期iframe窗体
                self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@hidefocus='true']"))
                #选择日期为‘今天’的按钮
                self.driver.find_element_by_xpath("//input[@value='今天']").click()

                # 退出所有iframe窗体
                self.driver.switch_to.default_content()
                # 切入汇率的iframe窗体
                self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='currencyRateManager-tab-iframe']"))
                # 切入‘汇率--汇率’的iframe窗体
                self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='subTabTwo-iframe']"))
                # 切入新增的iframe窗体
                self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='addWin-iframe']"))

                #选择银行
                self.temp = self.driver.find_element_by_xpath("//input[@id='combobox-input-bankid']")
                self.temp.click()
                self.temp.send_keys("BOC-中国银行")
                time.sleep(1)
                self.temp.send_keys(Keys.ARROW_DOWN)
                self.temp.send_keys(Keys.ENTER)

                #选择汇率类型
                self.temp = self.driver.find_element_by_xpath("//input[@id='combobox-input-currencyratetypeid']")
                self.temp.click()
                #self.temp.send_keys("BOC-中国银行")
                time.sleep(1)
                self.temp.send_keys(Keys.ARROW_DOWN)
                self.temp.send_keys(Keys.ENTER)

                #输入汇率
                self.driver.find_element_by_xpath("//input[@id='rate-input']").send_keys("7")
                time.sleep(2)

                # 输入汇买价
                self.driver.find_element_by_xpath("//input[@id='buyrate-input']").send_keys("98")
                time.sleep(2)

                # 输入汇卖价
                self.driver.find_element_by_xpath("//input[@id='sellrate-input']").send_keys("99")
                time.sleep(2)

                # 输入钞买价
                self.driver.find_element_by_xpath("//input[@id='buynote-input']").send_keys("100")
                time.sleep(2)

                # 输入钞卖价
                self.driver.find_element_by_xpath("//input[@id='sellnote-input']").send_keys("101")
                time.sleep(2)

                #描述框中填入值
                self.driver.find_element_by_xpath("//textarea[@id='description']").send_keys("自动化测试" + str(i))
                time.sleep(2)

                # 点击保存按钮
                self.driver.find_element_by_xpath("//span[text()='保存']").click()

                # 退出所有iframe窗体
                self.driver.switch_to.default_content()

                # 用隐式等待方法等页面出现新增成功的提示框
                self.driver.implicitly_wait(60)
                self.driver.find_element_by_xpath("//span[contains(text(),'操作成功！')]")
                print('新增保存汇率，第%s笔成功！' % i)
                time.sleep(3)

                # 切入汇率的iframe窗体
                self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='currencyRateManager-tab-iframe']"))
                # 切入‘汇率--汇率’的iframe窗体
                self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='subTabTwo-iframe']"))


            # 点击查看
            #用JS的方法点击放大镜
            button = self.driver.find_element_by_xpath("//span[@class='f-contrac-close']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            #输入货币对：
            # self.temp = self.driver.find_element_by_xpath("//input[@id='combobox-input-currencypairid']")
            # self.temp.click()
            self.temp = self.driver.find_element_by_xpath("//input[@id='combobox-input-currencypairid']")
            self.driver.execute_script("$(arguments[0]).click()", self.temp)
            self.temp.send_keys("人民币/美元")
            time.sleep(1)
            #选中"人民币/美元"前面的复选框
            self.driver.find_element_by_xpath("//div[@title='代码-名称:CNY-人民币/USD-美元']/parent::*/preceding-sibling::*[1]/descendant::*[2]").click()
            time.sleep(1)

            #输入银行：
            self.temp = self.driver.find_element_by_xpath("//input[@id='combobox-input-bankid']")
            self.driver.execute_script("$(arguments[0]).click()", self.temp)
            #self.temp.click()
            self.temp.send_keys("BOC-中国银行")
            time.sleep(1)
            #选中"人民币/美元"前面的复选框
            self.driver.find_element_by_xpath("//div[@title='代码-名称:BOC-中国银行']/parent::*/preceding-sibling::*[1]/descendant::*[2]").click()
            time.sleep(1)

            #点击查询
            self.driver.find_element_by_xpath("//span[text()='查询']").click()
            time.sleep(2)

            #修改
            # 修改功能
            # 勾选一个新增的货币对
            self.driver.find_element_by_xpath("//div[@title='银行:BOC-中国银行']/parent::*/preceding-sibling::*[1]/descendant::*[2]").click()
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
            print('修改汇率成功！')
            time.sleep(3)

            # 切入汇率的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='currencyRateManager-tab-iframe']"))
            # 切入‘汇率--汇率’的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='subTabTwo-iframe']"))

            # 实时外汇牌价查询
            # 勾选一个新增的货币对
            self.driver.find_element_by_xpath("//div[@title='银行:BOC-中国银行']/parent::*/preceding-sibling::*[1]/descendant::*[2]").click()
            time.sleep(1)

            # 点击'实时外汇牌价'按钮
            self.driver.find_element_by_xpath("//span[text()='实时外汇牌价']").click()
            time.sleep(1)

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 用隐式等待方法等页面出现新增成功的提示框
            #self.driver.implicitly_wait(60)
            #self.driver.find_element_by_xpath("//span[contains(text(),'外汇牌价查询')]")
            print('已点击‘实时外汇牌价’！')
            time.sleep(3)

            #点击复核按钮
            # 切入汇率的iframe窗体
            switch_to("xpath", "//iframe[@id='currencyRateManager-tab-iframe']")
            # 切入‘汇率--汇率’的iframe窗体
            switch_to("xpath", "//iframe[@id='subTabTwo-iframe']")

            #勾选
            click("xpath", "//div[@title='银行:BOC-中国银行']/parent::*/preceding-sibling::*[1]/descendant::*[2]")

            #点击复核按钮
            click("xpath", "//span[text()='复核']")

            # 点击弹出框的OK键
            click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

            # 退出所有iframe窗体
            switch_default()

            # 用隐式等待方法等页面出现提示框
            implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
            print("外汇数据，复核成功！")
            time.sleep(3)

            # 点击取消复核按钮
            # 切入汇率的iframe窗体
            switch_to("xpath", "//iframe[@id='currencyRateManager-tab-iframe']")
            # 切入‘汇率--汇率’的iframe窗体
            switch_to("xpath", "//iframe[@id='subTabTwo-iframe']")

            # 勾选
            click("xpath", "//div[@title='银行:BOC-中国银行']/parent::*/preceding-sibling::*[1]/descendant::*[2]")

            # 用JS方便点击‘复核’按钮旁边的倒三角形
            js_click("xpath", "//span[text()='复核']/parent::*/following-sibling::*/child::*")
            sleep(1)

            # 点击取消复核按钮
            click("xpath", "//a[contains(text(),'取消复核')]")

            # 点击弹出框的OK键
            click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

            # 退出所有iframe窗体
            switch_default()

            # 用隐式等待方法等页面出现提示框
            implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
            print("外汇数据，取消复核成功！")
            time.sleep(3)

            # 切入汇率的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='currencyRateManager-tab-iframe']"))
            # 切入‘汇率--汇率’的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='subTabTwo-iframe']"))

            #删除功能
            #勾选
            self.driver.find_element_by_xpath("//div[@title='银行:BOC-中国银行']/parent::*/preceding-sibling::*[1]/descendant::*[2]").click()

            #点击删除按钮
            self.driver.find_element_by_xpath("//span[text()='删除']").click()

            # 点击弹出框的OK键
            self.driver.find_element_by_xpath("//button[@id='f-message-webgen-0-okBnt']").click()

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 用隐式等待方法等页面出现删除的提示框
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath("//span[contains(text(),'删除成功')]")
            print("删除汇率成功！")
            time.sleep(3)

            # 用JS的方法关闭汇率的页面
            button = self.driver.find_element_by_xpath("//a[@title='汇率']/child::*[1]")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 打印操作成功日志
            print('‘汇率--汇率’操作成功!')
            logging.info("‘汇率--汇率’操作成功!")
            time.sleep(2)
        except Exception as err:
            # 发生其他异常时，打印异常堆栈信息
            print(traceback.print_exc())
            logging.debug("‘汇率--汇率’，操作失败！" + str(traceback.format_exc()))




        # 测试：汇率--汇率查看
        try:
            # 退出所有iframe窗体
            self.driver.switch_to.default_content()
            #切入系统设置的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='systemconfig-tab-iframe']"))
            logging.info("开始测试‘汇率--汇率查看’功能")

            # 用JS的方法点击基础资料下的'汇率'
            button = self.driver.find_element_by_xpath("//a[@nname='汇率']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            #退出所有iframe窗体
            self.driver.switch_to.default_content()
            #切入汇率的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='currencyRateManager-tab-iframe']"))

            #点击汇率查看页面
            self.driver.find_element_by_xpath("//span[text()='汇率查看']").click()

            # 切入‘汇率--汇率查看’的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='subTabThree-iframe']"))

            # 点击查看
            #用JS的方法点击放大镜
            button = self.driver.find_element_by_xpath("//span[@class='f-contrac-close']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            #输入货币对：
            # self.temp = self.driver.find_element_by_xpath("//input[@id='combobox-input-currencypairid']")
            # self.temp.click()
            self.temp = self.driver.find_element_by_xpath("//input[@id='combobox-input-currencypairid']")
            self.driver.execute_script("$(arguments[0]).click()", self.temp)
            self.temp.send_keys("人民币/美元")
            time.sleep(1)
            #选中"人民币/美元"前面的复选框
            self.driver.find_element_by_xpath("//div[@title='代码-名称:CNY-人民币/USD-美元']/parent::*/preceding-sibling::*[1]/descendant::*[2]").click()
            time.sleep(1)

            #输入银行：
            self.temp = self.driver.find_element_by_xpath("//input[@id='combobox-input-bankid']")
            self.driver.execute_script("$(arguments[0]).click()", self.temp)
            #self.temp.click()
            self.temp.send_keys("BOC-中国银行")
            time.sleep(1)
            #选中"BOC-中国银行"前面的复选框
            self.driver.find_element_by_xpath("//div[@title='代码-名称:BOC-中国银行']/parent::*/preceding-sibling::*[1]/descendant::*[2]").click()
            time.sleep(1)

            #点击查询
            self.driver.find_element_by_xpath("//span[text()='查询']").click()
            time.sleep(2)

            # 双击汇率为‘7’的数据
            # 获取页面元素
            temp = self.driver.find_element_by_xpath("//div[contains(text(),'7.0')]")
            # 导入支持双击操作的模块
            from selenium.webdriver import ActionChains
            # 开始模拟鼠标双击操作
            action_chains = ActionChains(self.driver)
            action_chains.double_click(temp).perform()
            time.sleep(3)

            #切入双击的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='detailWin-iframe']"))

            # 用隐式等待方法等页面页面出现'自动化测试1'字段，说明新增汇率存在
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath("//textarea[contains(text(),'自动化测试')]")
            print("新增汇率存在！")
            time.sleep(3)

            #关闭弹出框
            # 退出双击出现的iframe窗体
            self.driver.switch_to.parent_frame()
            #关闭窗体
            self.driver.find_element_by_xpath("//div[@class='f-win-tool f-win-close']").click()
            time.sleep(2)

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 打印操作成功日志
            print('‘汇率--汇率查看’操作成功!')
            logging.info("‘汇率--汇率查看’操作成功!")
            time.sleep(2)

            #删除‘汇率--汇率’数据
            # 切入汇率的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='currencyRateManager-tab-iframe']"))
            #点击‘汇率--汇率’页面
            self.driver.find_element_by_xpath("//span[text()='汇率']").click()
            # 切入‘汇率--汇率’的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='subTabTwo-iframe']"))

            #勾选
            self.driver.find_element_by_xpath("//div[@title='银行:BOC-中国银行']/parent::*/preceding-sibling::*[1]/descendant::*[2]").click()

            #点击删除按钮
            self.driver.find_element_by_xpath("//span[text()='删除']").click()

            # 点击弹出框的OK键
            self.driver.find_element_by_xpath("//button[@id='f-message-webgen-0-okBnt']").click()

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 用隐式等待方法等页面出现删除的提示框
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath("//span[contains(text(),'删除成功')]")
            print("删除第二个汇率，成功！")
            time.sleep(3)

            # 用JS的方法关闭汇率的页面
            button = self.driver.find_element_by_xpath("//a[@title='汇率']/child::*[1]")
            self.driver.execute_script("$(arguments[0]).click()", button)
        except Exception as err:
            # 发生其他异常时，打印异常堆栈信息
            print(traceback.print_exc())
            logging.debug("‘汇率--汇率查看’，操作失败！" + str(traceback.format_exc()))


        
        # 测试：部门
        try:
            # 退出所有iframe窗体
            self.driver.switch_to.default_content()
            #切入系统设置的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='systemconfig-tab-iframe']"))
            logging.info("开始测试‘部门’功能")

            # 用JS的方法点击基础资料下的'部门'
            button = self.driver.find_element_by_xpath("//a[@nname='部门']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            #退出所有iframe窗体
            self.driver.switch_to.default_content()
            #切入部门的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='deptManager-tab-iframe']"))

            # 用JS的方法点击新增按钮
            button = self.driver.find_element_by_xpath("//span[text()='新增']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 切入新增的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='addWin-iframe']"))

            #输入部门的代码
            self.driver.find_element_by_xpath("//input[@id='code']").send_keys("test")
            time.sleep(2)

            #输入部门的名称
            self.driver.find_element_by_xpath("//input[@id='name']").send_keys("自动化测试")
            time.sleep(2)

            #输入外部系统部门代码
            self.driver.find_element_by_xpath("//input[@id='othercode']").send_keys("test")
            time.sleep(2)

            #选中是否有效按钮
            #self.driver.find_element_by_xpath("//input[@id='isactive']").click()
            #time.sleep(2)

            # 描述框中填入值
            self.driver.find_element_by_xpath("//textarea[@id='description']").send_keys("自动化测试")
            time.sleep(2)

            # 点击保存按钮
            self.driver.find_element_by_xpath("//span[text()='保存']").click()

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 用隐式等待方法等页面出现新增成功的提示框
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath("//span[contains(text(),'操作成功！')]")
            print('保存成功！')
            time.sleep(3)

            #切入部门的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='deptManager-tab-iframe']"))

            # 点击查看
            #用JS的方法点击放大镜
            button = self.driver.find_element_by_xpath("//span[@class='f-contrac-close']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 输入部门代码：
            self.driver.find_element_by_xpath("//input[@id='code']").send_keys("test")
            time.sleep(1)

            #点击查询
            self.driver.find_element_by_xpath("//span[text()='查询']").click()
            time.sleep(2)

            #修改
            # 勾选一个新增的部门
            #self.driver.find_element_by_xpath("//div[@title='部门代码:test']/parent::*/preceding-sibling::*[1]/descendant::*[2]").click()
            click("xpath","//button[@buz_type='single']")
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
            print('修改成功！')
            time.sleep(3)

            # 添加下级部门
            #切入部门的iframe窗体
            switch_to("xpath", "//iframe[@id='deptManager-tab-iframe']")

            # 勾选一个部门
            # self.driver.find_element_by_xpath("//div[@title='部门代码:test']/parent::*/preceding-sibling::*[1]/descendant::*[2]").click()
            click("xpath", "//button[@buz_type='single']")
            time.sleep(1)

            # 点击添加下级部门按钮
            click("xpath", "//span[text()='添加下级部门']")

            # 切入添加下级部门的iframe窗体
            switch_to("xpath", "//iframe[@id='addlowDepartmentWin-iframe']")

            # 输入下级部门的代码
            input("xpath", "//input[@id='code']", "test-1")
            time.sleep(1)

            # 输入下级部门的名称
            input("xpath", "//input[@id='name']", "自动化测试-1")
            sleep(1)

            # 输入外部系统部门代码
            input("xpath", "//input[@id='othercode']", "test-1-1")
            sleep(1)

            # 选中是否有效按钮
            #click("xpath", "//input[@id='isactive']")
            #time.sleep(2)

            # 描述框中填入值
            input("xpath", "//textarea[@id='description']", "自动化测试-1的描述框")
            time.sleep(2)

            # 点击保存按钮
            click("xpath", "//span[text()='保存']")

            # 退出所有iframe窗体
            switch_default()

            # 用隐式等待方法等页面出现新增成功的提示框
            implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
            print("下级部门，保存成功！")
            time.sleep(3)

            # 添加同级部门
            # 切入部门的iframe窗体
            switch_to("xpath", "//iframe[@id='deptManager-tab-iframe']")

            # 勾选一个部门
            # self.driver.find_element_by_xpath("//div[@title='部门代码:test']/parent::*/preceding-sibling::*[1]/descendant::*[2]").click()
            click("xpath", "//button[@buz_type='single']")
            time.sleep(1)

            # 点击添加同级部门按钮
            click("xpath", "//span[text()='添加同级部门']")

            # 切入添加部门的iframe窗体
            switch_to("xpath", "//iframe[@id='addDepartmentWin-iframe']")

            # 输入部门的代码
            input("xpath", "//input[@id='code']", "test2")
            time.sleep(1)

            # 输入部门的名称
            input("xpath", "//input[@id='name']", "自动化测试2")
            sleep(1)

            # 输入外部系统部门代码
            input("xpath", "//input[@id='othercode']", "test2")
            sleep(1)

            # 选中是否有效按钮
            #click("xpath", "//input[@id='isactive']")
            #time.sleep(2)

            # 描述框中填入值
            input("xpath", "//textarea[@id='description']", "自动化测试2的描述框")
            time.sleep(2)

            # 点击保存按钮
            click("xpath", "//span[text()='保存']")

            # 退出所有iframe窗体
            switch_default()

            # 用隐式等待方法等页面出现新增成功的提示框
            implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
            print("同级部门，保存成功！")
            time.sleep(3)

            # 切入部门的iframe窗体
            switch_to("xpath", "//iframe[@id='deptManager-tab-iframe']")

            #删除功能
            #先勾选下级部门test-1
            #self.driver.find_element_by_xpath("//div[@title='部门代码:test']/parent::*/preceding-sibling::*[1]/descendant::*[2]").click()
            click("xpath", "//tr[@id='t1_t0_t0-fixed']/child::*[2]/descendant::*[2]")
            #click("xpath", "//tr[@id='t1_t1_t0-fixed']/child::*[2]/descendant::*[2]") #20210126修改
            #再勾选部门test
            click("xpath", "//tr[@id='t1_t0-fixed']/child::*[2]/descendant::*[2]")
            #再勾选部门test2
            click("xpath", "//tr[@id='t1_t1-fixed']/child::*[2]/descendant::*[2]")

            #点击删除按钮
            click("xpath", "//span[text()='删除']")

            # 点击弹出框的OK键
            click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

            # 退出所有iframe窗体
            switch_default()

            # 用隐式等待方法等页面出现删除的提示框
            implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
            print("删除成功！")
            time.sleep(3)

            # 用JS的方法关闭部门的页面
            js_click("xpath", "//a[@title='部门']/child::*[1]")

            # 打印操作成功日志
            print('部门操作成功!')
            logging.info("部门操作成功!")
            time.sleep(2)
        except Exception as err:
            # 发生其他异常时，打印异常堆栈信息
            print(traceback.print_exc())
            logging.debug("‘部门’，操作失败！" + str(traceback.format_exc()))
            # Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
            dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
            dir_path = make_current_hour_dir(dir_path + "\\")
            pic_path = os.path.join(dir_path, get_current_time() + ".png")
            capture(pic_path)

                
        # 测试：资金类别
        try:
            # 退出所有iframe窗体
            self.driver.switch_to.default_content()
            #切入系统设置的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='systemconfig-tab-iframe']"))
            logging.info("开始测试‘资金类别’功能")

            # 用JS的方法点击基础资料下的'资金类别'
            button = self.driver.find_element_by_xpath("//a[@nname='资金类别']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            #退出所有iframe窗体
            self.driver.switch_to.default_content()
            #切入资金类别的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='fundCategoriesManager-tab-iframe']"))

            # 用JS的方法点击新增按钮
            button = self.driver.find_element_by_xpath("//span[text()='新增']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 切入新增的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='addWin-iframe']"))

            #输入资金类别的代码
            self.driver.find_element_by_xpath("//input[@id='code']").send_keys("test1")
            time.sleep(2)

            #输入资金类别的名称
            self.driver.find_element_by_xpath("//input[@id='name']").send_keys("自动化测试")
            time.sleep(2)

            # 描述框中填入值
            self.driver.find_element_by_xpath("//textarea[@id='description']").send_keys("自动化测试")
            time.sleep(2)

            # 点击保存按钮
            self.driver.find_element_by_xpath("//span[text()='保存']").click()

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 用隐式等待方法等页面出现新增成功的提示框
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath("//span[contains(text(),'操作成功！')]")
            print('保存成功！')
            time.sleep(3)

            #切入资金类别的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='fundCategoriesManager-tab-iframe']"))

            # 点击查看
            #用JS的方法点击放大镜
            button = self.driver.find_element_by_xpath("//span[@class='f-contrac-close']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 输入部门代码：
            self.driver.find_element_by_xpath("//input[@id='code']").send_keys("test1")
            time.sleep(1)

            #点击查询
            self.driver.find_element_by_xpath("//span[text()='查询']").click()
            time.sleep(2)

            #修改
            # 勾选
            #self.driver.find_element_by_xpath("//div[@title='代码:test']/parent::*/preceding-sibling::*[1]/descendant::*[2]").click()
            #20210429
            click("xpath", "//button[@class='f-grid-checkbox' and @buz_type='single']")
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
            print('修改成功！')
            time.sleep(3)

            #切入资金类别的iframe窗体
            switch_to("xpath", "//iframe[@id='fundCategoriesManager-tab-iframe']")

            #添加下级项目
            #勾选
            click("xpath", "//button[@class='f-grid-checkbox' and @buz_type='single']")
            time.sleep(1)

            #点击'添加下级项目'按钮
            click("xpath", "//span[text()='添加下级项目']")

            # 切入添加下级项目的iframe窗体
            switch_to("xpath", "//iframe[@id='addWin-iframe']")

            # 输入下级项目的代码
            input("xpath", "//input[@id='code']", "test1-1")
            time.sleep(1)

            # 输入下级项目的名称
            input("xpath", "//input[@id='name']", "自动化测试-1")
            sleep(1)

            # 描述框中填入值
            input("xpath", "//textarea[@id='description']", "自动化测试-1的描述框")
            time.sleep(2)

            # 点击保存按钮
            click("xpath", "//span[text()='保存']")

            # 退出所有iframe窗体
            switch_default()

            # 用隐式等待方法等页面出现新增成功的提示框
            implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
            print("下级项目，保存成功！")
            time.sleep(3)

            # 切入资金类别的iframe窗体
            switch_to("xpath", "//iframe[@id='fundCategoriesManager-tab-iframe']")

            # '添加同级项目'
            # 勾选'test1-1'这条数据
            getElements(self.driver, "xpath", "//button[@class='f-grid-checkbox' and @buz_type='single']")[1].click()
            time.sleep(1)

            # 点击添加同级项目按钮
            click("xpath", "//span[text()='添加同级项目']")

            # 切入添加项目的iframe窗体
            switch_to("xpath", "//iframe[@id='addWin-iframe']")

            # 输入项目的代码
            input("xpath", "//input[@id='code']", "test1-2")
            time.sleep(1)

            # 输入项目的名称
            input("xpath", "//input[@id='name']", "自动化测试2")
            sleep(1)

            # 描述框中填入值
            input("xpath", "//textarea[@id='description']", "自动化测试2的描述框")
            time.sleep(2)

            # 点击保存按钮
            click("xpath", "//span[text()='保存']")

            # 退出所有iframe窗体
            switch_default()

            # 用隐式等待方法等页面出现新增成功的提示框
            implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
            print("同级项目，保存成功！")
            time.sleep(3)

            # 切入资金类别的iframe窗体
            switch_to("xpath", "//iframe[@id='fundCategoriesManager-tab-iframe']")

            #删除功能
            #先勾选test2
            getElements(self.driver, "xpath", "//button[@class='f-grid-checkbox' and @buz_type='single']")[2].click()
            # 再勾选test-1
            getElements(self.driver, "xpath", "//button[@class='f-grid-checkbox' and @buz_type='single']")[1].click()
            # 再勾选test
            getElements(self.driver, "xpath", "//button[@class='f-grid-checkbox' and @buz_type='single']")[0].click()

            #点击删除按钮
            self.driver.find_element_by_xpath("//span[text()='删除']").click()

            # 点击弹出框的OK键
            self.driver.find_element_by_xpath("//button[@id='f-message-webgen-0-okBnt']").click()

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 用隐式等待方法等页面出现删除的提示框
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath("//span[contains(text(),'操作成功')]")
            print("删除成功！")
            time.sleep(3)

            # 用JS的方法关闭资金类别的页面
            button = self.driver.find_element_by_xpath("//a[@title='资金类别']/child::*[1]")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 打印操作成功日志
            print('资金类别成功!')
            logging.info("资金类别成功!")
            time.sleep(2)
        except Exception as err:
            # 发生其他异常时，打印异常堆栈信息
            print(traceback.print_exc())
            logging.debug("‘资金类别’，操作失败！" + str(traceback.format_exc()))
                

        
        # 测试：利率--利率类型
        try:
            # 退出所有iframe窗体
            self.driver.switch_to.default_content()
            #切入系统设置的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='systemconfig-tab-iframe']"))
            logging.info("开始测试‘利率--利率类型’功能")

            # 用JS的方法点击基础资料下的'利率'
            button = self.driver.find_element_by_xpath("//a[@nname='利率']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            #退出所有iframe窗体
            self.driver.switch_to.default_content()
            #切入‘利率--利率’的第一iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='interestRateValues-tab-iframe']"))

            #点击利率类型页面
            self.driver.find_element_by_xpath("//span[text()='利率类型']").click()

            # 切入‘利率--利率’的第二iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='subTabTwo-iframe']"))

            # 把利率类型放到一个列表中
            temp = {1: '浮动利率', 2: '固定利率'}
            #新增2笔
            for k, v in temp.items():

                #用JS的方法点击新增按钮
                button = self.driver.find_element_by_xpath("//span[text()='新增']")
                self.driver.execute_script("$(arguments[0]).click()", button)

                #切入新增的iframe窗体
                self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='addWin-iframe']"))

                #输入名称
                self.driver.find_element_by_xpath("//input[@id='name']").send_keys("test" + v)
                time.sleep(2)

                #输入别名
                self.driver.find_element_by_xpath("//input[@id='t1symbol']").send_keys("test" + v)
                time.sleep(2)

                #输入利率方式
                self.temp = self.driver.find_element_by_xpath("//input[@id='combobox-input-classification']")
                self.temp.click()
                self.temp.send_keys(v)
                time.sleep(1)
                self.temp.send_keys(Keys.ARROW_DOWN)
                self.temp.send_keys(Keys.ENTER)

                #输入计息基准
                self.temp = self.driver.find_element_by_xpath("//input[@id='combobox-input-daycountconvention']")
                self.temp.click()
                self.temp.send_keys('ACT/365')
                time.sleep(1)
                self.temp.send_keys(Keys.ARROW_DOWN)
                self.temp.send_keys(Keys.ENTER)

                # 描述框中填入值
                self.driver.find_element_by_xpath("//textarea[@id='description']").send_keys("自动化测试"+str(k)+"："+v)
                time.sleep(2)

                # 点击保存按钮
                self.driver.find_element_by_xpath("//span[text()='保存']").click()

                # 退出所有iframe窗体
                self.driver.switch_to.default_content()

                # 用隐式等待方法等页面出现新增成功的提示框
                self.driver.implicitly_wait(60)
                self.driver.find_element_by_xpath("//span[contains(text(),'操作成功！')]")
                print('新增保存第%s笔：利率为%s成功！' %(k,v))
                time.sleep(3)

                # 切入‘利率--利率类型’的iframe窗体
                self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='interestRateValues-tab-iframe']"))
                self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='subTabTwo-iframe']"))


            # 点击查看
            #用JS的方法点击放大镜
            button = self.driver.find_element_by_xpath("//span[@class='f-contrac-close']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 输入部门代码：
            self.driver.find_element_by_xpath("//input[@id='name']").send_keys("test")
            time.sleep(1)

            #点击查询
            self.driver.find_element_by_xpath("//span[text()='查询']").click()
            time.sleep(2)

            # 修改
            # 勾选一个新增的利率
            self.driver.find_element_by_xpath("//div[@title='利率方式:固定利率']/parent::*/preceding-sibling::*[1]/descendant::*[2]").click()
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
            print('修改成功！')
            time.sleep(3)

            # 用JS的方法关闭利率的页面
            button = self.driver.find_element_by_xpath("//a[@title='利率']/child::*[1]")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 打印操作成功日志
            print("‘利率--利率类型’,成功!")
            logging.info("‘利率--利率类型’,成功!")
            time.sleep(2)
        except Exception as err:
            # 发生其他异常时，打印异常堆栈信息
            print(traceback.print_exc())
            logging.debug("‘利率--利率类型’，操作失败！" + str(traceback.format_exc()))


        # 测试：利率--利率
        try:
            # 退出所有iframe窗体
            self.driver.switch_to.default_content()
            #切入系统设置的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='systemconfig-tab-iframe']"))
            logging.info("开始测试‘利率--利率’功能")

            # 用JS的方法点击基础资料下的'利率'
            button = self.driver.find_element_by_xpath("//a[@nname='利率']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            #退出所有iframe窗体
            self.driver.switch_to.default_content()
            #切入‘利率--利率’的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='interestRateValues-tab-iframe']"))
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='subTabOne-iframe']"))

            # 把利率类型放到一个列表中
            temp = {1: 'test浮动利率', 2: 'test固定利率'}
            #新增2笔
            for k, v in temp.items():

                # 用JS的方法点击新增按钮
                button = self.driver.find_element_by_xpath("//span[text()='新增']")
                self.driver.execute_script("$(arguments[0]).click()", button)

                # 切入新增的iframe窗体
                self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='addWin-iframe']"))

                #输入利率类型
                self.temp = self.driver.find_element_by_xpath("//input[@id='combobox-input-interestratetypeid']")
                self.temp.click()
                self.temp.send_keys(v)
                time.sleep(1)
                self.temp.send_keys(Keys.ARROW_DOWN)
                self.temp.send_keys(Keys.ENTER)

                #选择日期
                #点击日期控件
                self.driver.find_element_by_xpath("//input[@id='ratedate-input']").click()
                #退出所有iframe窗体
                self.driver.switch_to.default_content()
                #进入选择日期iframe窗体
                self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@hidefocus='true']"))
                #选择日期为‘今天’的按钮
                self.driver.find_element_by_xpath("//input[@value='今天']").click()

                # 退出所有iframe窗体
                self.driver.switch_to.default_content()
                # 切入‘利率--利率’的iframe窗体
                self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='interestRateValues-tab-iframe']"))
                self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='subTabOne-iframe']"))
                # 切入新增的iframe窗体
                self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='addWin-iframe']"))

                #输入利率值
                self.driver.find_element_by_xpath("//input[@id='rate-input']").send_keys("3.65")
                time.sleep(2)

                # 描述框中填入值
                self.driver.find_element_by_xpath("//textarea[@id='description']").send_keys("自动化测试"+str(k)+"："+v)
                time.sleep(2)

                # 点击保存按钮
                self.driver.find_element_by_xpath("//span[text()='保存']").click()

                # 退出所有iframe窗体
                self.driver.switch_to.default_content()

                # 用隐式等待方法等页面出现新增成功的提示框
                self.driver.implicitly_wait(60)
                self.driver.find_element_by_xpath("//span[contains(text(),'操作成功！')]")
                print('新增保存第%s笔：利率为%s成功！' %(k,v))
                time.sleep(3)

                # 切入‘利率--利率’的iframe窗体
                self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='interestRateValues-tab-iframe']"))
                self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='subTabOne-iframe']"))


            # 点击查看
            #用JS的方法点击放大镜
            button = self.driver.find_element_by_xpath("//span[@class='f-contrac-close']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 选择日期
            # 点击日期控件
            self.driver.find_element_by_xpath("//input[@id='ratedatestart-input']").click()
            # 退出所有iframe窗体
            self.driver.switch_to.default_content()
            # 进入选择日期iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@hidefocus='true']"))
            # 选择日期为‘今天’的按钮
            self.driver.find_element_by_xpath("//input[@value='今天']").click()

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()
            # 切入‘利率--利率’的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='interestRateValues-tab-iframe']"))
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='subTabOne-iframe']"))

            #点击查询
            self.driver.find_element_by_xpath("//span[text()='查询']").click()
            time.sleep(2)

            #修改
            # 勾选一个新增的利率
            self.driver.find_element_by_xpath("//div[@title='利率类型:test固定利率']/parent::*/preceding-sibling::*[1]/descendant::*[2]").click()
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
            print('修改成功！')
            time.sleep(3)

            # 切入‘利率--利率’的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='interestRateValues-tab-iframe']"))
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='subTabOne-iframe']"))

            #删除功能
            #勾选2笔
            self.driver.find_element_by_xpath("//div[@title='利率类型:test浮动利率']/parent::*/preceding-sibling::*[1]/descendant::*[2]").click()
            self.driver.find_element_by_xpath("//div[@title='利率类型:test固定利率']/parent::*/preceding-sibling::*[1]/descendant::*[2]").click()

            #点击删除按钮
            self.driver.find_element_by_xpath("//span[text()='删除']").click()

            # 点击弹出框的OK键
            self.driver.find_element_by_xpath("//button[@id='f-message-webgen-0-okBnt']").click()

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 用隐式等待方法等页面出现删除的提示框
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath("//span[contains(text(),'操作成功')]")
            print("删除‘利率--利率’,成功！")
            time.sleep(3)


             # 切入‘利率’的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='interestRateValues-tab-iframe']"))

            # 点击利率类型页面
            self.driver.find_element_by_xpath("//span[text()='利率类型']").click()

            # 切入‘利率--利率类型’的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='subTabTwo-iframe']"))


            # 点击查看
            #用JS的方法点击放大镜
            button = self.driver.find_element_by_xpath("//span[@class='f-contrac-close']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 输入代码：
            self.driver.find_element_by_xpath("//input[@id='name']").send_keys("test")
            time.sleep(1)

            #点击查询
            self.driver.find_element_by_xpath("//span[text()='查询']").click()
            time.sleep(2)

             #删除2个数据功能
             #勾选2个
            self.driver.find_element_by_xpath("//div[@title='利率方式:浮动利率']/parent::*/preceding-sibling::*[1]/descendant::*[2]").click()
            self.driver.find_element_by_xpath("//div[@title='利率方式:固定利率']/parent::*/preceding-sibling::*[1]/descendant::*[2]").click()

             #点击删除按钮
            self.driver.find_element_by_xpath("//span[text()='删除']").click()

             # 点击弹出框的OK键
            self.driver.find_element_by_xpath("//button[@id='f-message-webgen-0-okBnt']").click()

             # 退出所有iframe窗体
            self.driver.switch_to.default_content()

             # 用隐式等待方法等页面出现删除的提示框
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath("//span[contains(text(),'操作成功')]")
            print("删除‘利率--利率类型’，成功！")
            time.sleep(3)

            # 用JS的方法关闭利率的页面
            button = self.driver.find_element_by_xpath("//a[@title='利率']/child::*[1]")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 打印操作成功日志
            print("‘利率--利率’,成功!")
            logging.info("‘利率--利率’,成功!")
            time.sleep(2)
        except Exception as err:
            # 发生其他异常时，打印异常堆栈信息
            print(traceback.print_exc())
            logging.debug("‘利率--利率’，操作失败！" + str(traceback.format_exc()))
        


        # 测试：利率方案
        try:
            # 退出所有iframe窗体
            self.driver.switch_to.default_content()
            #切入系统设置的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='systemconfig-tab-iframe']"))
            logging.info("开始测试‘利率方案’功能")

            # 用JS的方法点击基础资料下的'利率方案'
            button = self.driver.find_element_by_xpath("//a[@nname='利率方案']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            #退出所有iframe窗体
            self.driver.switch_to.default_content()
            #切入利率方案的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='interestRateSchemes-tab-iframe']"))

            # 用JS的方法点击新增按钮
            button = self.driver.find_element_by_xpath("//span[text()='新增']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 切入新增的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='addWin-iframe']"))

            #输入利率方案的代码
            self.driver.find_element_by_xpath("//input[@id='code']").send_keys("test")
            time.sleep(2)

            #输入利率方案的名称
            self.driver.find_element_by_xpath("//input[@id='name']").send_keys("自动化测试")
            time.sleep(2)

            # 输入单据对象
            self.temp = self.driver.find_element_by_xpath("//input[@id='combobox-input-noteobjectid']")
            self.temp.click()
            self.temp.send_keys("YHDK-银行贷款单")
            time.sleep(1)
            self.temp.send_keys(Keys.ARROW_DOWN)
            self.temp.send_keys(Keys.ENTER)
            time.sleep(1)

            # 输入利率类型
            self.temp = self.driver.find_element_by_xpath("//input[@id='combobox-input-interestratetypeid']")
            self.temp.click()
            self.temp.send_keys("固定")
            time.sleep(1)
            self.temp.send_keys(Keys.ARROW_DOWN)
            self.temp.send_keys(Keys.ENTER)
            time.sleep(1)

            # 描述框中填入值
            self.driver.find_element_by_xpath("//textarea[@id='description']").send_keys("自动化测试")
            time.sleep(2)

            # 输入共享模式
            self.temp = self.driver.find_element_by_xpath("//input[@id='combobox-input-includemode']")
            self.temp.click()
            self.temp.send_keys("适用组织共享")
            time.sleep(1)
            self.temp.send_keys(Keys.ARROW_DOWN)
            self.temp.send_keys(Keys.ENTER)
            time.sleep(1)

            # 输入适用组织
            self.temp = self.driver.find_element_by_xpath("//input[@id='combobox-input-schemeorgids']")
            self.temp.click()
            self.temp.send_keys("TestOrgSet")
            time.sleep(1)
            # 勾选
            self.driver.find_element_by_xpath("//div[contains(text(),'TestOrgSet')]/parent::*/preceding-sibling::*[1]/descendant-or-self::*[3]").click()
            time.sleep(1)

            # 点击保存按钮
            self.driver.find_element_by_xpath("//span[text()='保存']").click()

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 用隐式等待方法等页面出现新增成功的提示框
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath("//span[contains(text(),'操作成功！')]")
            print('保存成功！')
            time.sleep(3)

            #切入利率方案的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='interestRateSchemes-tab-iframe']"))

            # 点击查看
            #用JS的方法点击放大镜
            button = self.driver.find_element_by_xpath("//span[@class='f-contrac-close']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 输入部门代码：
            self.driver.find_element_by_xpath("//input[@id='code']").send_keys("test")
            time.sleep(1)

            #点击查询
            self.driver.find_element_by_xpath("//span[text()='查询']").click()
            time.sleep(2)

            #修改
            # 勾选一个新增的利率方案
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
            print('修改成功！')
            time.sleep(3)

            # 切入利率方案的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='interestRateSchemes-tab-iframe']"))

            #删除功能
            #勾选一个新增的利率方案
            self.driver.find_element_by_xpath("//div[@title='代码:test']/parent::*/preceding-sibling::*[1]/descendant::*[2]").click()

            #点击删除按钮
            self.driver.find_element_by_xpath("//span[text()='删除']").click()

            # 点击弹出框的OK键
            self.driver.find_element_by_xpath("//button[@id='f-message-webgen-0-okBnt']").click()

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 用隐式等待方法等页面出现删除的提示框
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath("//span[contains(text(),'操作成功')]")
            print("删除‘利率方案’，成功！")
            time.sleep(3)

            # 用JS的方法关闭利率方案的页面
            button = self.driver.find_element_by_xpath("//a[@title='利率方案']/child::*[1]")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 打印操作成功日志
            print('利率方案成功!')
            logging.info("利率方案成功!")
            time.sleep(2)
        except Exception as err:
            # 发生其他异常时，打印异常堆栈信息
            print(traceback.print_exc())
            logging.debug("‘利率方案’，操作失败！" + str(traceback.format_exc()))
        
        
        # 测试：单据对象
        try:
            # 退出所有iframe窗体
            self.driver.switch_to.default_content()
            # 切入系统设置的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='systemconfig-tab-iframe']"))
            logging.info("开始测试‘单据对象’功能")

            # 用JS的方法点击基础资料下的'单据对象'
            button = self.driver.find_element_by_xpath("//a[@nname='单据对象']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()
            # 切入单据对象的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='noteObjects-tab-iframe']"))

            # 点击查看
            # 用JS的方法点击放大镜
            button = self.driver.find_element_by_xpath("//span[@class='f-contrac-close']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 输入单据对象代码：
            self.driver.find_element_by_xpath("//input[@id='code']").send_keys("XBSQ")
            time.sleep(1)

            # 点击查询
            self.driver.find_element_by_xpath("//span[text()='查询']").click()
            time.sleep(2)

            # 第一次修改
            # 勾选一个单据对象
            self.driver.find_element_by_xpath("//div[contains(@title,'代码:XBSQ')]/parent::*/preceding-sibling::*[1]/descendant::*[2]").click()
            time.sleep(1)

            # 点击修改按钮
            self.driver.find_element_by_xpath("//span[text()='修改']").click()
            time.sleep(1)

            # 切入修改的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='modWin-iframe']"))

            # 修改单据对象的代码
            self.driver.find_element_by_xpath("//input[@id='code']").send_keys("test")
            time.sleep(2)

            # 点击保存按钮
            self.driver.find_element_by_xpath("//span[text()='保存']").click()

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 用隐式等待方法等页面出现新增成功的提示框
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath("//span[contains(text(),'操作成功！')]")
            print('单据对象第一次修改成功！')
            time.sleep(3)

            # 第二次修改
            # 切入单据对象的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='noteObjects-tab-iframe']"))

            # 勾选一个单据对象
            self.driver.find_element_by_xpath("//div[contains(@title,'代码:XBSQtest')]/parent::*/preceding-sibling::*[1]/descendant::*[2]").click()
            time.sleep(1)

            # 点击修改按钮
            self.driver.find_element_by_xpath("//span[text()='修改']").click()
            time.sleep(1)

            # 切入修改的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='modWin-iframe']"))

            # 修改单据对象的代码
            self.driver.find_element_by_xpath("//input[@id='code']").clear()
            self.driver.find_element_by_xpath("//input[@id='code']").send_keys("XBSQ")
            time.sleep(2)

            # 点击保存按钮
            self.driver.find_element_by_xpath("//span[text()='保存']").click()

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 用隐式等待方法等页面出现新增成功的提示框
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath("//span[contains(text(),'操作成功！')]")
            print('单据对象第二次修改成功！')
            time.sleep(3)

            # 用JS的方法关闭利率方案的页面
            button = self.driver.find_element_by_xpath("//a[@title='单据对象']/child::*[1]")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 打印操作成功日志
            print('单据对象成功!')
            logging.info("单据对象成功!")
            time.sleep(2)
        except Exception as err:
            # 发生其他异常时，打印异常堆栈信息
            print(traceback.print_exc())
            logging.debug("‘单据对象’，操作失败！" + str(traceback.format_exc()))

        

        # 测试：现金流量项目
        try:
            # 退出所有iframe窗体
            self.driver.switch_to.default_content()
            #切入系统设置的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='systemconfig-tab-iframe']"))
            logging.info("开始测试‘现金流量项目’功能")

            # 用JS的方法点击基础资料下的'利率方案'
            button = self.driver.find_element_by_xpath("//a[@nname='现金流量项目']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            #退出所有iframe窗体
            self.driver.switch_to.default_content()
            #切入现金流量项目的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='cashFlowItem-tab-iframe']"))

            # 用JS的方法点击新增按钮
            button = self.driver.find_element_by_xpath("//span[text()='新增']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 切入新增的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='modWin-iframe']"))

            #输入现金流项目的代码
            self.driver.find_element_by_xpath("//input[@id='code']").send_keys("test1")
            time.sleep(2)

            #输入现金流项目的名称
            self.driver.find_element_by_xpath("//input[@id='name']").send_keys("自动化测试1")
            time.sleep(2)

            # 输入现金流项目的交易方向
            self.temp = self.driver.find_element_by_xpath("//input[@id='combobox-input-moneyway']")
            self.temp.click()
            self.temp.send_keys("收入")
            time.sleep(1)
            self.temp.send_keys(Keys.ARROW_DOWN)
            self.temp.send_keys(Keys.ENTER)

            # 描述框中填入值
            self.driver.find_element_by_xpath("//textarea[@id='description']").send_keys("自动化测试1")
            time.sleep(2)

            # 点击保存按钮
            self.driver.find_element_by_xpath("//span[text()='保存']").click()

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 用隐式等待方法等页面出现新增成功的提示框
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath("//span[contains(text(),'操作成功！')]")
            print('保存成功！')
            time.sleep(3)

            #切入现金流项目的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='cashFlowItem-tab-iframe']"))

            # 点击查看
            #用JS的方法点击放大镜
            button = self.driver.find_element_by_xpath("//span[@class='f-contrac-close']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 输入代码：
            self.driver.find_element_by_xpath("//input[@id='code']").send_keys("test")
            time.sleep(1)

            #点击查询
            self.driver.find_element_by_xpath("//span[text()='查询']").click()
            time.sleep(2)

            #修改
            # 勾选一个新增的现金流量项目
            self.driver.find_element_by_xpath("//tr[@id='t1_t0-fixed' and @tid='t1_t0']/child::*[2]/descendant-or-self::*[3]").click()
            time.sleep(1)

            # 点击修改按钮
            self.driver.find_element_by_xpath("//span[text()='修改']").click()
            time.sleep(1)

            # 切入修改的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='modWin-iframe']"))

            # 输入现金流项目的交易方向
            self.temp = self.driver.find_element_by_xpath("//input[@id='combobox-input-moneyway']")
            self.temp.click()
            self.temp.send_keys("支持")
            time.sleep(1)
            self.temp.send_keys(Keys.ARROW_DOWN)
            self.temp.send_keys(Keys.ENTER)

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
            print('修改成功！')
            time.sleep(3)

            # 切入利率方案的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='cashFlowItem-tab-iframe']"))


            #添加下级项目
            # 勾选一个新增的现金流量项目
            self.driver.find_element_by_xpath("//tr[@id='t1_t0-fixed' and @tid='t1_t0']/child::*[2]/descendant-or-self::*[3]").click()
            time.sleep(1)

            #点击添加下级项目按钮
            self.driver.find_element_by_xpath("//span[text()='添加下级项目']").click()

            # 切入添加下级项目的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='addlowbudgetitemsWin-iframe']"))

            #输入现金流项目的代码
            self.driver.find_element_by_xpath("//input[@id='code']").send_keys("test2")
            time.sleep(2)

            #输入现金流项目的名称
            self.driver.find_element_by_xpath("//input[@id='name']").send_keys("自动化测试2")
            time.sleep(2)

            # 输入现金流项目的交易方向
            self.temp = self.driver.find_element_by_xpath("//input[@id='combobox-input-moneyway']")
            self.temp.click()
            self.temp.send_keys("支出")
            time.sleep(1)
            self.temp.send_keys(Keys.ARROW_DOWN)
            self.temp.send_keys(Keys.ENTER)

            # 描述框中填入值
            self.driver.find_element_by_xpath("//textarea[@id='description']").send_keys("自动化测试2")
            time.sleep(2)

            # 点击保存按钮
            self.driver.find_element_by_xpath("//span[text()='保存']").click()

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 用隐式等待方法等页面出现新增成功的提示框
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath("//span[contains(text(),'操作成功！')]")
            print('保存成功！')
            time.sleep(3)

            #切入现金流项目的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='cashFlowItem-tab-iframe']"))


            #添加同级项目
            # 勾选一个新增的现金流量项目
            self.driver.find_element_by_xpath("//tr[@id='t1_t0_t0-fixed' and @tid='t1_t0_t0']/child::*[2]/descendant-or-self::*[3]").click()
            time.sleep(1)

            # 点击添加同级项目按钮
            self.driver.find_element_by_xpath("//span[text()='添加同级项目']").click()

            # 切入添加同级项目的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='addsamebudgetitemsWin-iframe']"))

            # 输入现金流项目的代码
            self.driver.find_element_by_xpath("//input[@id='code']").send_keys("test3")
            time.sleep(2)

            # 输入现金流项目的名称
            self.driver.find_element_by_xpath("//input[@id='name']").send_keys("自动化测试3")
            time.sleep(2)

            # 输入现金流项目的交易方向
            self.temp = self.driver.find_element_by_xpath("//input[@id='combobox-input-moneyway']")
            self.temp.click()
            self.temp.send_keys("支出")
            time.sleep(1)
            self.temp.send_keys(Keys.ARROW_DOWN)
            self.temp.send_keys(Keys.ENTER)

            # 描述框中填入值
            self.driver.find_element_by_xpath("//textarea[@id='description']").send_keys("自动化测试3")
            time.sleep(2)

            # 点击保存按钮
            self.driver.find_element_by_xpath("//span[text()='保存']").click()

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 用隐式等待方法等页面出现新增成功的提示框
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath("//span[contains(text(),'操作成功！')]")
            print('保存成功！')
            time.sleep(3)

            # 切入现金流项目的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='cashFlowItem-tab-iframe']"))

            #删除功能
            #勾选一个新增的现金流量项目test3
            self.driver.find_element_by_xpath("//tr[@id='t1_t0_t1-fixed' and @tid='t1_t0_t1']/child::*[2]/descendant-or-self::*[3]").click()
            time.sleep(1)
            # 勾选一个新增的现金流量项目test2
            self.driver.find_element_by_xpath("//tr[@id='t1_t0_t0-fixed' and @tid='t1_t0_t0']/child::*[2]/descendant-or-self::*[3]").click()
            time.sleep(1)
            # 勾选一个新增的现金流量项目test1
            self.driver.find_element_by_xpath("//tr[@id='t1_t0-fixed' and @tid='t1_t0']/child::*[2]/descendant-or-self::*[3]").click()
            time.sleep(1)

            #点击删除按钮
            self.driver.find_element_by_xpath("//span[text()='删除']").click()

            # 点击弹出框的OK键
            self.driver.find_element_by_xpath("//button[@id='f-message-webgen-0-okBnt']").click()

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 用隐式等待方法等页面出现删除的提示框
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath("//span[contains(text(),'删除')]")
            print("删除成功！")
            time.sleep(3)

            # 用JS的方法关闭利率方案的页面
            button = self.driver.find_element_by_xpath("//a[@title='现金流量项目']/child::*[1]")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 打印操作成功日志
            print('现金流量项目成功!')
            logging.info("现金流量项目成功!")
            time.sleep(2)
        except Exception as err:
            # 发生其他异常时，打印异常堆栈信息
            print(traceback.print_exc())
            logging.debug("‘现金流量项目’，操作失败！" + str(traceback.format_exc()))

        
        

        # 测试：日志
        try:
            # 退出所有iframe窗体
            self.driver.switch_to.default_content()
            #切入系统设置的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='systemconfig-tab-iframe']"))
            logging.info("开始测试‘日志’功能")

            # 用JS的方法点击基础资料下的'日志'
            button = self.driver.find_element_by_xpath("//a[@nname='日志']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            #退出所有iframe窗体
            self.driver.switch_to.default_content()
            #切入日志的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='logmanager-tab-iframe']"))

            """
            
            “日志--运行日志”，需要配置环境，暂时不写
            
            """
            #点击‘日志--操作日志’页面
            self.driver.find_element_by_xpath("//span[text()='操作日志']").click()
            time.sleep(1)

            # 切入‘日志--操作日志’的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='subTabTwo-iframe']"))

            # 点击查看
            #用JS的方法点击放大镜
            button = self.driver.find_element_by_xpath("//span[@class='f-contrac-close']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 输入功能UC：
            self.driver.find_element_by_xpath("//input[@id='operationuc']").send_keys("UC_BD_CASHFLOWITEMS_ADD")
            time.sleep(1)

            # 用JS的方法点击查询
            button = self.driver.find_element_by_xpath("//span[text()='查询']")
            self.driver.execute_script("$(arguments[0]).click()", button)
            time.sleep(5)

            #点击右下角的直接翻到底的翻页按钮
            self.driver.find_element_by_xpath("//span[@id='gridbar-page-last']").click()

            # 用隐式等待方法等页面出现提示
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath("//div[text()='UC_BD_CASHFLOWITEMS_ADD']")
            print('翻页成功！')
            time.sleep(3)

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 用JS的方法关闭利率方案的页面
            button = self.driver.find_element_by_xpath("//a[@title='日志']/child::*[1]")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 打印操作成功日志
            print('日志操作成功!')
            logging.info("日志操作成功!")
            time.sleep(2)
        except Exception as err:
            # 发生其他异常时，打印异常堆栈信息
            print(traceback.print_exc())
            logging.debug("‘日志’，操作失败！" + str(traceback.format_exc()))




        # 测试：预警分类
        try:
            # 退出所有iframe窗体
            self.driver.switch_to.default_content()
            #切入系统设置的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='systemconfig-tab-iframe']"))
            logging.info("开始测试‘预警分类’功能")

            # 用JS的方法点击基础资料下的'预警分类'
            button = self.driver.find_element_by_xpath("//a[@nname='预警分类']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            #退出所有iframe窗体
            self.driver.switch_to.default_content()
            #切入预警分类的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='warningtypes-tab-iframe']"))

            # 用JS的方法点击新增按钮
            button = self.driver.find_element_by_xpath("//span[text()='新增']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 切入新增的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='addWin-iframe']"))

            #输入代码
            self.driver.find_element_by_xpath("//input[@id='code']").send_keys("test")
            time.sleep(2)

            #输入的名称
            self.driver.find_element_by_xpath("//input[@id='name']").send_keys("自动化测试")
            time.sleep(2)

            # 描述框中填入值
            self.driver.find_element_by_xpath("//textarea[@id='description']").send_keys("自动化测试")
            time.sleep(2)

            # 点击保存按钮
            self.driver.find_element_by_xpath("//span[text()='保存']").click()

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 用隐式等待方法等页面出现新增成功的提示框
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath("//span[contains(text(),'操作成功！')]")
            print('保存成功！')
            time.sleep(3)

            #切入预警分类的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='warningtypes-tab-iframe']"))

            # 点击查看
            #用JS的方法点击放大镜
            button = self.driver.find_element_by_xpath("//span[@class='f-contrac-close']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 输入部门代码：
            self.driver.find_element_by_xpath("//input[@id='code']").send_keys("test")
            time.sleep(1)

            #点击查询
            self.driver.find_element_by_xpath("//span[text()='查询']").click()
            time.sleep(2)

            #修改
            # 勾选一个新增的利率方案
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
            print('修改成功！')
            time.sleep(3)

            # 切入预警分类的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='warningtypes-tab-iframe']"))

            #删除功能
            #勾选一个新增的利率方案
            self.driver.find_element_by_xpath("//div[@title='代码:test']/parent::*/preceding-sibling::*[1]/descendant::*[2]").click()

            #点击删除按钮
            self.driver.find_element_by_xpath("//span[text()='删除']").click()

            # 点击弹出框的OK键
            self.driver.find_element_by_xpath("//button[@id='f-message-webgen-0-okBnt']").click()

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 用隐式等待方法等页面出现删除的提示框
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath("//span[contains(text(),'操作成功')]")
            print("删除‘预警分类’，成功！")
            time.sleep(3)

            # 用JS的方法关闭利率方案的页面
            button = self.driver.find_element_by_xpath("//a[@title='预警分类']/child::*[1]")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 打印操作成功日志
            print('预警分类，操作成功!')
            logging.info("预警分类，操作成功!")
            time.sleep(2)
        except Exception as err:
            # 发生其他异常时，打印异常堆栈信息
            print(traceback.print_exc())
            logging.debug("‘预警分类’，操作失败！" + str(traceback.format_exc()))


       

        # 测试：预警对象
        try:
            # 退出所有iframe窗体
            self.driver.switch_to.default_content()
            #切入系统设置的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='systemconfig-tab-iframe']"))
            logging.info("开始测试‘预警对象’功能")

            # 用JS的方法点击基础资料下的'预警分类'
            button = self.driver.find_element_by_xpath("//a[@nname='预警对象']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            #退出所有iframe窗体
            self.driver.switch_to.default_content()
            #切入预警对象的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='warningobject-tab-iframe']"))

            # 用JS的方法点击新增按钮
            button = self.driver.find_element_by_xpath("//span[text()='新增']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 切入新增的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='addWin-iframe']"))

            #输入代码
            self.driver.find_element_by_xpath("//input[@name='code']").send_keys("test")
            time.sleep(2)

            #输入的名称
            self.driver.find_element_by_xpath("//input[@id='name']").send_keys("自动化测试")
            time.sleep(2)

            # 输入预警分类
            self.temp = self.driver.find_element_by_xpath("//input[@id='combobox-input-noteobjectid']")
            self.temp.click()
            self.temp.send_keys("settlement-资金结算管理")
            time.sleep(1)
            self.temp.send_keys(Keys.ARROW_DOWN)
            self.temp.send_keys(Keys.ENTER)

            #输入数据唯一标识字段
            self.driver.find_element_by_xpath("//input[@class='f-textField ' and @name='uniquefield']").send_keys("t_se_payments")
            time.sleep(2)

            #查询SQL框中填入值
            self.temp =self.driver.find_element_by_xpath("//textarea[@id='sqlstatement']")
            self.temp.send_keys("SELECT org.Org_Name,t.orgid,t.notecode,t.ouramount,t.paydate,suser.user_name FROM t_se_payments t\
            LEFT OUTER JOIN tsys_organization org ON t.orgid=org.org_id LEFT OUTER JOIN tsys_user suser ON t.paypersonid=suser.user_id")
            time.sleep(2)

            # 描述框中填入值
            self.driver.find_element_by_xpath("//textarea[@id='description']").send_keys("自动化测试")
            time.sleep(2)

            #第一次增加一行
            self.driver.find_element_by_xpath("//span[text()='新增行']").click()
            time.sleep(1)
            #第二次增加一行
            self.driver.find_element_by_xpath("//span[text()='新增行']").click()
            time.sleep(1)

            #第一行里增加数据
            #增加代码
            self.driver.find_element_by_xpath("//input[@id='warningconditions-fieldcode-0']").send_keys("t.ouramount")
            time.sleep(1)

            # 增加名称
            self.driver.find_element_by_xpath("//input[@id='warningconditions-fieldname-0']").send_keys("金额")
            time.sleep(1)

            # 选择字段类型
            self.temp = self.driver.find_element_by_xpath("//input[@id='combobox-input-warningconditions-fieldtype-0']")
            self.temp.click()
            self.temp.send_keys("浮点数")
            time.sleep(1)
            self.temp.send_keys(Keys.ARROW_DOWN)
            self.temp.send_keys(Keys.ENTER)

            #第二行里增加数据
            #增加代码
            self.driver.find_element_by_xpath("//input[@id='warningconditions-fieldcode-1']").send_keys("t.orgid")
            time.sleep(1)

            # 增加名称
            self.driver.find_element_by_xpath("//input[@id='warningconditions-fieldname-1']").send_keys("组织")
            time.sleep(1)

            # 选择字段类型
            self.temp = self.driver.find_element_by_xpath("//input[@id='combobox-input-warningconditions-fieldtype-1']")
            self.temp.click()
            self.temp.send_keys("辅助查询")
            time.sleep(1)
            self.temp.send_keys(Keys.ARROW_DOWN)
            self.temp.send_keys(Keys.ENTER)

            # 选择输入字段值
            self.temp = self.driver.find_element_by_xpath("//input[@id='combobox-input-warningconditions-fieldvalue-1']")
            self.temp.click()
            self.temp.send_keys("组织")
            time.sleep(1)
            self.temp.send_keys(Keys.ARROW_DOWN)
            self.temp.send_keys(Keys.ENTER)

            #点击消息模板插页
            self.driver.find_element_by_xpath("//span[text()='消息模板']").click()
            time.sleep(1)

            # 第一次增加一行
            self.driver.find_element_by_xpath("//div[@id='warningnotices']/following-sibling::*/descendant-or-self::*[8]").click()
            time.sleep(1)
            # 第二次增加一行
            self.driver.find_element_by_xpath("//div[@id='warningnotices']/following-sibling::*/descendant-or-self::*[8]").click()
            time.sleep(1)

            # 第一行里增加数据
            # 增加代码
            self.driver.find_element_by_xpath("//input[@id='warningnotices-fieldcode-0']").send_keys("xiaoxi")
            time.sleep(1)

            # 增加名称
            self.driver.find_element_by_xpath("//input[@id='warningnotices-fieldname-0']").send_keys("消息")
            time.sleep(1)

            # 第二行里增加数据
            # 增加代码
            self.driver.find_element_by_xpath("//input[@id='warningnotices-fieldcode-1']").send_keys("moban")
            time.sleep(1)

            # 增加名称
            self.driver.find_element_by_xpath("//input[@id='warningnotices-fieldname-1']").send_keys("模板")
            time.sleep(1)

            # 点击通知方式插页
            self.driver.find_element_by_xpath("//span[text()='通知方式']").click()
            time.sleep(1)

            # 第一次增加一行
            self.driver.find_element_by_xpath("//div[@id='warningnoticesway']/following-sibling::*/descendant-or-self::*[8]").click()
            time.sleep(1)
            # 第二次增加一行
            self.driver.find_element_by_xpath("//div[@id='warningnoticesway']/following-sibling::*/descendant-or-self::*[8]").click()
            time.sleep(1)

            # 第一行里增加数据
            # 增加代码
            self.driver.find_element_by_xpath("//input[@id='warningnoticesway-fieldcode-0']").send_keys("tongzhi")
            time.sleep(1)

            # 增加名称
            self.driver.find_element_by_xpath("//input[@id='warningnoticesway-fieldname-0']").send_keys("通知")
            time.sleep(1)

            # 第二行里增加数据
            # 增加代码
            self.driver.find_element_by_xpath("//input[@id='warningnoticesway-fieldcode-1']").send_keys("fangsi")
            time.sleep(1)

            # 增加名称
            self.driver.find_element_by_xpath("//input[@id='warningnoticesway-fieldname-1']").send_keys("方式")
            time.sleep(1)

            # 点击保存按钮
            self.driver.find_element_by_xpath("//span[text()='保存']").click()

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 用隐式等待方法等页面出现新增成功的提示框
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath("//span[contains(text(),'操作成功！')]")
            print('保存成功！')
            time.sleep(3)

            #切入预警对象的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='warningobject-tab-iframe']"))

            # 点击查看
            #用JS的方法点击放大镜
            button = self.driver.find_element_by_xpath("//span[@class='f-contrac-close']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 输入部门代码：
            self.driver.find_element_by_xpath("//input[@id='code']").send_keys("test")
            time.sleep(1)

            #点击查询
            self.driver.find_element_by_xpath("//span[text()='查询']").click()
            time.sleep(2)

            #修改
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

            # 修改‘金额’变成‘金额（元）’
            self.driver.find_element_by_xpath("//input[@id='warningconditions-fieldname-0']").clear()
            self.driver.find_element_by_xpath("//input[@id='warningconditions-fieldname-0']").send_keys("金额（元）")
            time.sleep(2)

            #切换到消息模板，删掉一条内容
            self.driver.find_element_by_xpath("//span[text()='消息模板']").click()
            time.sleep(1)

            #勾选一个消息模板内容
            self.driver.find_element_by_xpath("//input[@id='warningnotices-syscheck-0']").click()
            time.sleep(1)

            #移除一行消息模板内容
            self.driver.find_element_by_xpath("//div[@id='warningnotices']/following-sibling::*/descendant-or-self::*[10]").click()
            time.sleep(1)

            # 切换到通知方式，新增一条内容
            self.driver.find_element_by_xpath("//span[text()='通知方式']").click()
            time.sleep(1)

            # 新增加一行
            self.driver.find_element_by_xpath("//div[@id='warningnoticesway']/following-sibling::*/descendant-or-self::*[8]").click()
            time.sleep(1)

            # 第三行里增加数据
            # 增加代码
            self.driver.find_element_by_xpath("//input[@id='warningnoticesway-fieldcode-2']").send_keys("XinZengYiHang")
            time.sleep(1)

            # 增加名称
            self.driver.find_element_by_xpath("//input[@id='warningnoticesway-fieldname-2']").send_keys("新增第三行")
            time.sleep(1)

            # 点击保存按钮
            self.driver.find_element_by_xpath("//span[text()='保存']").click()

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 用隐式等待方法等页面出现新增成功的提示框
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath("//span[contains(text(),'操作成功！')]")
            print('修改成功！')
            time.sleep(3)

            # 切入预警对象的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='warningobject-tab-iframe']"))

            #删除功能
            #勾选
            self.driver.find_element_by_xpath("//div[@title='代码:test']/parent::*/preceding-sibling::*[1]/descendant::*[2]").click()

            #点击删除按钮
            self.driver.find_element_by_xpath("//span[text()='删除']").click()

            # 点击弹出框的OK键
            self.driver.find_element_by_xpath("//button[@id='f-message-webgen-0-okBnt']").click()

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 用隐式等待方法等页面出现删除的提示框
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath("//span[contains(text(),'操作成功')]")
            print("删除成功！")
            time.sleep(3)

            # 用JS的方法关闭利率方案的页面
            button = self.driver.find_element_by_xpath("//a[@title='预警对象']/child::*[1]")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 打印操作成功日志
            print('预警对象，操作成功!')
            logging.info("预警对象，操作成功!")
            time.sleep(2)
        except Exception as err:
            # 发生其他异常时，打印异常堆栈信息
            print(traceback.print_exc())
            logging.debug("‘预警对象’，操作失败！" + str(traceback.format_exc()))


        # 测试：预警规则
        try:
            # 退出所有iframe窗体
            self.driver.switch_to.default_content()
            #切入系统设置的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='systemconfig-tab-iframe']"))
            logging.info("开始测试‘预警规则’功能")

            # 用JS的方法点击基础资料下的'预警分类'
            button = self.driver.find_element_by_xpath("//a[@nname='预警规则']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            #退出所有iframe窗体
            self.driver.switch_to.default_content()
            #切入预警规则的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='warningrule-tab-iframe']"))

            # 用JS的方法点击新增按钮
            button = self.driver.find_element_by_xpath("//span[text()='新增']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 切入新增的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='addWin-iframe']"))

            #输入的名称
            self.driver.find_element_by_xpath("//input[@id='name']").send_keys("自动化测试")
            time.sleep(1)

            # 输入预警对象
            self.temp = self.driver.find_element_by_xpath("//input[@id='combobox-input-warningobjid']")
            self.temp.click()
            self.temp.send_keys("付款成功邮件提醒")
            time.sleep(1)
            self.temp.send_keys(Keys.ARROW_DOWN)
            self.temp.send_keys(Keys.ENTER)
            time.sleep(2)

            #增加一行
            self.driver.find_element_by_xpath("//span[text()='新增行']").click()
            time.sleep(1)

            #第一行里增加数据
            #增加顺序号
            self.driver.find_element_by_xpath("//input[@id='warningruleconditions-displayorder-0-input']").send_keys("1")
            time.sleep(1)

            # 选择左括号
            self.temp = self.driver.find_element_by_xpath("//input[@id='combobox-input-warningruleconditions-leftbracket-0']")
            self.temp.click()
            self.temp.send_keys("(")
            time.sleep(1)
            # 模拟回车键
            keyDown('enter')
            keyUp('enter')

            # 选择预警属性
            self.temp = self.driver.find_element_by_xpath("//input[@id='combobox-input-warningruleconditions-warningobjattrid-0']")
            self.temp.click()
            self.temp.send_keys("支付状态")
            time.sleep(1)
            self.temp.send_keys(Keys.ARROW_DOWN)
            self.temp.send_keys(Keys.ENTER)

            #选择比较关系
            self.temp = self.driver.find_element_by_xpath("//input[@id='combobox-input-warningruleconditions-operatesign-0']")
            self.temp.click()
            self.temp.send_keys("=")
            time.sleep(1)
            self.temp.send_keys(Keys.ARROW_DOWN)
            self.temp.send_keys(Keys.ENTER)
            time.sleep(2)

            #选择值
            self.temp = self.driver.find_element_by_xpath("//input[@id='combobox-input-warningruleconditions-fieldvalue-0']")
            self.temp.click()
            self.temp.send_keys("已收付")
            time.sleep(1)
            self.temp.send_keys(Keys.ARROW_DOWN)
            self.temp.send_keys(Keys.ENTER)

            #选择右括号
            self.temp = self.driver.find_element_by_xpath("//input[@id='combobox-input-warningruleconditions-rightbracket-0']")
            self.temp.click()
            self.temp.send_keys(")")
            time.sleep(1)
            # 模拟回车键
            keyDown('enter')
            keyUp('enter')

            #选择逻辑关系
            self.temp = self.driver.find_element_by_xpath("//input[@id='combobox-input-warningruleconditions-logicoperate-0']")
            self.temp.click()
            self.temp.send_keys("并且")
            time.sleep(1)
            self.temp.send_keys(Keys.ARROW_DOWN)
            self.temp.send_keys(Keys.ENTER)

            #消息模板增加内容
            #点击消息模块
            self.driver.find_element_by_xpath("//span[text()='消息模板']").click()
            time.sleep(1)

            #输入主题
            self.driver.find_element_by_xpath("//input[@id='subject']").send_keys("付款提示")
            time.sleep(1)

            #输入消息模板
            self.driver.find_element_by_xpath("//textarea[@id='msgbody']").send_keys("自动化测试消息模板")
            time.sleep(1)

            #用JS的方法增加第1行
            #self.driver.find_element_by_xpath("//span[text()='新增行']").click()
            button = self.driver.find_element_by_xpath("//div[@id='warningrulemsgtemplates']/following-sibling::*/descendant-or-self::*[8]")
            self.driver.execute_script("$(arguments[0]).click()", button)
            time.sleep(1)

            #用JS的方法增加第2行
            # self.driver.find_element_by_xpath("//span[text()='新增行']").click()
            button = self.driver.find_element_by_xpath("//div[@id='warningrulemsgtemplates']/following-sibling::*/descendant-or-self::*[8]")
            self.driver.execute_script("$(arguments[0]).click()", button)
            time.sleep(1)

            #增加第1行的文本中输入内容
            self.driver.find_element_by_xpath("//input[@id='warningrulemsgtemplates-msgtext-0']").send_keys("{0}")
            time.sleep(1)

            #增加第1行的属性值输入内容
            self.temp = self.driver.find_element_by_xpath("//input[@id='combobox-input-warningrulemsgtemplates-msgwarningobjattrid-0']")
            self.temp.click()
            self.temp.send_keys("币种")
            time.sleep(1)
            self.temp.send_keys(Keys.ARROW_DOWN)
            self.temp.send_keys(Keys.ENTER)

            #增加第2行的文本中输入内容
            self.driver.find_element_by_xpath("//input[@id='warningrulemsgtemplates-msgtext-1']").send_keys("{1}")
            time.sleep(1)

            #增加第2行的属性值输入内容
            self.temp = self.driver.find_element_by_xpath("//input[@id='combobox-input-warningrulemsgtemplates-msgwarningobjattrid-1']")
            self.temp.click()
            self.temp.send_keys("记账日期(年月日)")
            time.sleep(1)
            self.temp.send_keys(Keys.ARROW_DOWN)
            self.temp.send_keys(Keys.ENTER)

            #通知方式增加内容
            #点击通知方式
            self.driver.find_element_by_xpath("//span[text()='通知方式']").click()
            time.sleep(1)

            #输入消息通知方式
            self.temp = self.driver.find_element_by_xpath("//input[@id='combobox-input-noticemode']")
            self.temp.click()
            self.temp.send_keys("外部系统")
            time.sleep(1)
            self.temp.send_keys(Keys.ARROW_DOWN)
            self.temp.send_keys(Keys.ENTER)

            #输入消息通知对象
            self.temp = self.driver.find_element_by_xpath("//input[@id='combobox-input-noticeobject']")
            self.temp.click()
            self.temp.send_keys("系统用户")
            time.sleep(1)
            self.temp.send_keys(Keys.ARROW_DOWN)
            self.temp.send_keys(Keys.ENTER)

            #点击固定配置按钮
            self.driver.find_element_by_xpath("//input[@id='noticeobjectsource' and @value='2']").click()

            #选择组织
            #点击组织框的下拉按钮
            #self.driver.find_element_by_xpath("//input[@id='combobox-input-orgids2']/following-sibling::*[1]").click()
            button = self.driver.find_element_by_xpath("//input[@id='combobox-input-orgids2']/following-sibling::*[1]")
            self.driver.execute_script("$(arguments[0]).click()", button)
            time.sleep(1)
            #在组织框里输入‘TestOrgSet’
            self.driver.find_element_by_xpath("//input[@id='combobox-input-orgids2']").send_keys("TestOrgSet")
            time.sleep(1)
            #勾选组织‘TestOrgSet-测试组织机构设置’
            button = self.driver.find_element_by_xpath("//div[contains(text(),'TestOrgSet')]/parent::*/preceding-sibling::*[1]/descendant-or-self::*[3]")
            self.driver.execute_script("$(arguments[0]).click()", button)
            time.sleep(1)

            # 选择角色
            # 点击角色的框的下拉按钮
            #self.driver.find_element_by_xpath("//input[@id='combobox-input-roleids2']/following-sibling::*[1]").click()
            button = self.driver.find_element_by_xpath("//input[@id='combobox-input-roleids2']/following-sibling::*[1]")
            self.driver.execute_script("$(arguments[0]).click()", button)
            time.sleep(1)
            # 勾选角色‘测试角色’
            button = self.driver.find_element_by_xpath("//div[@title='名称:测试角色']/parent::*/preceding-sibling::*[1]/descendant-or-self::*[3]")
            self.driver.execute_script("$(arguments[0]).click()", button)
            time.sleep(1)

            # 选择用户
            # 点击用户的框的下拉按钮
            #self.driver.find_element_by_xpath("//input[@id='combobox-input-userids2']/following-sibling::*[1]").click()
            button = self.driver.find_element_by_xpath("//input[@id='combobox-input-userids2']/following-sibling::*[1]")
            self.driver.execute_script("$(arguments[0]).click()", button)
            time.sleep(1)
            # 在用户框里输入‘测试’
            self.driver.find_element_by_xpath("//input[@id='combobox-input-userids2']").send_keys("测试")
            time.sleep(1)
            # 勾选用户‘测试组织机构设置-测试用户’
            button = self.driver.find_element_by_xpath("//div[contains(text(),'测试用户')]/parent::*/preceding-sibling::*[1]/descendant-or-self::*[3]")
            self.driver.execute_script("$(arguments[0]).click()", button)
            time.sleep(1)

            #输入发送平台
            # 点击发送平台的框
            self.temp = self.driver.find_element_by_xpath("//input[@id='combobox-input-sendplatform2']")
            self.temp.click()
            self.temp.send_keys("OA系统")
            time.sleep(1)
            self.temp.send_keys(Keys.ARROW_DOWN)
            self.temp.send_keys(Keys.ENTER)

            # 点击保存按钮
            self.driver.find_element_by_xpath("//span[text()='保存']").click()

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 用隐式等待方法等页面出现新增成功的提示框
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath("//span[contains(text(),'操作成功！')]")
            print('保存成功！')
            time.sleep(3)

            #切入预警规则的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='warningrule-tab-iframe']"))

            # 点击查看
            #用JS的方法点击放大镜
            button = self.driver.find_element_by_xpath("//span[@class='f-contrac-close']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 输入部门代码：
            self.driver.find_element_by_xpath("//input[@id='name']").send_keys("自动化测试")
            time.sleep(1)

            #点击查询
            self.driver.find_element_by_xpath("//span[text()='查询']").click()
            time.sleep(2)

            #修改
            # 勾选一个新增的利率方案
            self.driver.find_element_by_xpath("//div[@title='名称:自动化测试']/parent::*/preceding-sibling::*[1]/descendant::*[2]").click()
            time.sleep(1)

            # 点击修改按钮
            self.driver.find_element_by_xpath("//span[text()='修改']").click()
            time.sleep(1)

            # 切入修改的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='modWin-iframe']"))

            # 修改规则名称
            self.driver.find_element_by_xpath("//input[@id='name']").send_keys("修改")
            time.sleep(2)

            #增加一行
            self.driver.find_element_by_xpath("//span[text()='新增行']").click()
            time.sleep(1)

            #新增行里增加数据
            #增加顺序号
            self.driver.find_element_by_xpath("//input[@id='warningruleconditions-displayorder-1-input']").send_keys("2")
            time.sleep(1)

            # 选择左括号
            self.temp = self.driver.find_element_by_xpath("//input[@id='combobox-input-warningruleconditions-leftbracket-1']")
            self.temp.click()
            self.temp.send_keys("(")
            time.sleep(1)
            # 模拟回车键
            keyDown('enter')
            keyUp('enter')

            # 选择预警属性
            self.temp = self.driver.find_element_by_xpath("//input[@id='combobox-input-warningruleconditions-warningobjattrid-1']")
            self.temp.click()
            self.temp.send_keys("操作人")
            time.sleep(1)
            self.temp.send_keys(Keys.ARROW_DOWN)
            self.temp.send_keys(Keys.ENTER)

            #选择比较关系
            self.temp = self.driver.find_element_by_xpath("//input[@id='combobox-input-warningruleconditions-operatesign-1']")
            self.temp.click()
            self.temp.send_keys("=")
            time.sleep(1)
            self.temp.send_keys(Keys.ARROW_DOWN)
            self.temp.send_keys(Keys.ENTER)
            time.sleep(2)

            #选择值
            self.temp = self.driver.find_element_by_xpath("//input[@id='warningruleconditions-fieldvalue-1']")
            self.temp.click()
            self.temp.send_keys("测试用户")
            time.sleep(1)

            #选择右括号
            self.temp = self.driver.find_element_by_xpath("//input[@id='combobox-input-warningruleconditions-rightbracket-1']")
            self.temp.click()
            self.temp.send_keys(")")
            time.sleep(1)
            # 模拟回车键
            keyDown('enter')
            keyUp('enter')

            #选择逻辑关系
            self.temp = self.driver.find_element_by_xpath("//input[@id='combobox-input-warningruleconditions-logicoperate-1']")
            self.temp.click()
            self.temp.send_keys("或者")
            time.sleep(1)
            self.temp.send_keys(Keys.ARROW_DOWN)
            self.temp.send_keys(Keys.ENTER)

            #消息模板增加内容
            #点击消息模块
            self.driver.find_element_by_xpath("//span[text()='消息模板']").click()
            time.sleep(1)

            #用JS的方法增加第2行
            # self.driver.find_element_by_xpath("//span[text()='新增行']").click()
            button = self.driver.find_element_by_xpath("//div[@id='warningrulemsgtemplates']/following-sibling::*/descendant-or-self::*[8]")
            self.driver.execute_script("$(arguments[0]).click()", button)
            time.sleep(1)

            # 新增行里的文本中输入内容
            self.driver.find_element_by_xpath("//input[@id='warningrulemsgtemplates-msgtext-2']").send_keys("{2}")
            time.sleep(1)

            # 新增行里的属性值输入内容
            self.temp = self.driver.find_element_by_xpath("//input[@id='combobox-input-warningrulemsgtemplates-msgwarningobjattrid-2']")
            self.temp.click()
            self.temp.send_keys("金额(分)")
            time.sleep(1)
            self.temp.send_keys(Keys.ARROW_DOWN)
            self.temp.send_keys(Keys.ENTER)

            #通知方式增加内容
            #点击通知方式
            self.driver.find_element_by_xpath("//span[text()='通知方式']").click()
            time.sleep(1)

            # # 选择角色
            # # 点击角色的框的下拉按钮
            # #self.driver.find_element_by_xpath("//input[@id='combobox-input-roleids2']/following-sibling::*[1]").click()
            # button = self.driver.find_element_by_xpath("//input[@id='combobox-input-roleids2']/following-sibling::*[1]")
            # self.driver.execute_script("$(arguments[0]).click()", button)
            # time.sleep(1)
            # # 勾选角色‘测试角色’
            # button = self.driver.find_element_by_xpath("//div[@title='名称:制单']/parent::*/preceding-sibling::*[1]/descendant-or-self::*[3]")
            # self.driver.execute_script("$(arguments[0]).click()", button)
            # time.sleep(1)

            # 点击保存按钮
            self.driver.find_element_by_xpath("//span[text()='保存']").click()

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 用隐式等待方法等页面出现新增成功的提示框
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath("//span[contains(text(),'操作成功！')]")
            print('修改成功！')
            time.sleep(3)

            # 切入预警规则的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='warningrule-tab-iframe']"))

            #删除功能
            #勾选
            self.driver.find_element_by_xpath("//div[@title='名称:自动化测试修改']/parent::*/preceding-sibling::*[1]/descendant::*[2]").click()

            #点击删除按钮
            self.driver.find_element_by_xpath("//span[text()='删除']").click()

            # 点击弹出框的OK键
            self.driver.find_element_by_xpath("//button[@id='f-message-webgen-0-okBnt']").click()

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 用隐式等待方法等页面出现删除的提示框
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath("//span[contains(text(),'操作成功')]")
            print("删除成功！")
            time.sleep(3)

            # 用JS的方法关闭利率方案的页面
            button = self.driver.find_element_by_xpath("//a[@title='预警规则']/child::*[1]")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 打印操作成功日志
            print('预警规则，操作成功!')
            logging.info("预警规则，操作成功!")
            time.sleep(2)
        except Exception as err:
            # 发生其他异常时，打印异常堆栈信息
            print(traceback.print_exc())
            logging.debug("‘预警规则’，操作失败！" + str(traceback.format_exc()))


        # 测试：界面元素管理
        try:
            # 退出所有iframe窗体
            self.driver.switch_to.default_content()
            #切入系统设置的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='systemconfig-tab-iframe']"))
            logging.info("开始测试‘界面元素管理’功能")

            # 用JS的方法点击基础资料下的'预警分类'
            button = self.driver.find_element_by_xpath("//a[@nname='界面元素管理']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            #退出所有iframe窗体
            self.driver.switch_to.default_content()
            #切入界面元素管理的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='pagecontrolsmanager-tab-iframe']"))
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='subTabOne-iframe']"))

            # 用JS的方法点击新增按钮
            button = self.driver.find_element_by_xpath("//span[text()='新增']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 切入新增的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='addWin-iframe']"))

            #输入控制类型
            self.temp = self.driver.find_element_by_xpath("//input[@id='combobox-input-pagetype']")
            self.temp.click()
            self.temp.send_keys("快捷付款单")
            time.sleep(1)
            #直接选择
            self.temp.send_keys(Keys.ENTER)
            time.sleep(2)

            #输入字段信息
            self.temp = self.driver.find_element_by_xpath("//input[@id='combobox-input-fieldid']")
            self.temp.click()
            self.temp.send_keys("工程项目")
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

            # 用隐式等待方法等页面出现新增成功的提示框
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath("//span[contains(text(),'操作成功！')]")
            print('保存成功！')
            time.sleep(3)

            # 切入界面元素管理的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='pagecontrolsmanager-tab-iframe']"))
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='subTabOne-iframe']"))

            # 点击查看
            #用JS的方法点击放大镜
            button = self.driver.find_element_by_xpath("//span[@class='f-contrac-close']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            #输入控制类型
            self.temp = self.driver.find_element_by_xpath("//input[@id='combobox-input-pagetype']")
            self.temp.click()
            # self.temp.send_keys("快捷付款单")
            # time.sleep(1)
            # # 模拟回车键
            # keyDown('enter')
            # keyUp('enter')
            #选择快捷付款单单选框
            time.sleep(1)
            self.driver.find_element_by_xpath("//div[@title='快捷付款单']/preceding-sibling::*").click()

            #点击查询
            self.driver.find_element_by_xpath("//span[text()='查询']").click()
            time.sleep(2)

            #修改
            # 勾选一个新增的内容
            self.driver.find_element_by_xpath("//div[@title='字段名称:工程项目']/parent::*/preceding-sibling::*[2]/descendant::*[2]").click()
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
            print('修改成功！')
            time.sleep(3)

            # 切入界面元素管理的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='pagecontrolsmanager-tab-iframe']"))
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='subTabOne-iframe']"))

            #删除功能
            #勾选一个新增的内容
            self.driver.find_element_by_xpath("//div[@title='字段名称:工程项目']/parent::*/preceding-sibling::*[2]/descendant::*[2]").click()

            #点击删除按钮
            self.driver.find_element_by_xpath("//span[text()='删除']").click()

            # 点击弹出框的OK键
            self.driver.find_element_by_xpath("//button[@id='f-message-webgen-0-okBnt']").click()

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 用隐式等待方法等页面出现删除的提示框
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath("//span[contains(text(),'操作成功')]")
            print("删除成功！")
            time.sleep(3)

            #测试界面信息查看
            # 切入界面元素管理的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='pagecontrolsmanager-tab-iframe']"))

            # 点击界面信息查看
            self.driver.find_element_by_xpath("//span[text()='界面信息查看']").click()

            # 切入界面信息查看的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='subTabTwo-iframe']"))

            # 点击查看
            #用JS的方法点击放大镜
            button = self.driver.find_element_by_xpath("//span[@class='f-contrac-close']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            #输入字段名称
            self.driver.find_element_by_xpath("//input[@id='name']").send_keys("工程项目")
            time.sleep(2)

            #点击查询
            self.driver.find_element_by_xpath("//span[text()='查询']").click()
            time.sleep(2)

            # 勾选‘字段名称:工程项目’
            self.driver.find_element_by_xpath("//div[@title='字段名称:工程项目']/parent::*/preceding-sibling::*[2]/descendant::*[2]").click()
            time.sleep(2)

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 用JS的方法关闭利率方案的页面
            button = self.driver.find_element_by_xpath("//a[@title='界面元素管理']/child::*[1]")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 打印操作成功日志
            print('界面元素管理，操作成功!')
            logging.info("界面元素管理，操作成功!")
            time.sleep(2)
        except Exception as err:
            # 发生其他异常时，打印异常堆栈信息
            print(traceback.print_exc())
            logging.debug("‘界面元素管理’，操作失败！" + str(traceback.format_exc()))

        
        # 测试：单位管理
        try:
            # 退出所有iframe窗体
            self.driver.switch_to.default_content()
            #切入系统设置的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='systemconfig-tab-iframe']"))
            logging.info("开始测试‘单位管理’功能")

            # 用JS的方法点击基础资料下的'单位管理'
            button = self.driver.find_element_by_xpath("//a[@nname='单位管理']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            #退出所有iframe窗体
            self.driver.switch_to.default_content()

            #切入‘单位管理’的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='companyManager-tab-iframe']"))
            # 切入‘单位管理--区域管理’的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='subTabOne-iframe']"))

            # 用JS的方法点击新增按钮
            button = self.driver.find_element_by_xpath("//span[text()='新增']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 切入新增的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='addWin-iframe']"))

            #输入区域代码
            self.temp = self.driver.find_element_by_xpath("//input[@id='code']").send_keys("test")
            time.sleep(1)

            #输入区域名称
            self.temp = self.driver.find_element_by_xpath("//input[@id='name']").send_keys("自动化测试")
            time.sleep(1)

            #输入区域负责人
            self.temp = self.driver.find_element_by_xpath("//input[@id='director']").send_keys("自动化测试")
            time.sleep(1)

            # 描述框中填入值
            self.driver.find_element_by_xpath("//textarea[@id='description']").send_keys("自动化测试")
            time.sleep(2)

            # 点击保存按钮
            self.driver.find_element_by_xpath("//span[text()='保存']").click()

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 用隐式等待方法等页面出现新增成功的提示框
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath("//span[contains(text(),'操作成功！')]")
            print('区域管理数据，保存成功！')
            time.sleep(3)

            #切入‘单位管理’的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='companyManager-tab-iframe']"))
            # 切入‘单位管理--区域管理’的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='subTabOne-iframe']"))

            # 点击查看
            #用JS的方法点击放大镜
            button = self.driver.find_element_by_xpath("//span[@class='f-contrac-close']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            #输入区域代码
            self.driver.find_element_by_xpath("//input[@id='code']").send_keys("test")
            time.sleep(2)

            #点击查询
            self.driver.find_element_by_xpath("//span[text()='查询']").click()
            time.sleep(2)

            #修改
            # 勾选一个新增的内容
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
            print('区域管理数据，修改成功！')
            time.sleep(3)

            #进入‘单位管理--单位台账’进行操作
            #切入‘单位管理’的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='companyManager-tab-iframe']"))

            #点击单位台账页面
            self.driver.find_element_by_xpath("//span[text()='单位台帐']").click()
            time.sleep(2)

            #切入‘单位管理--单位台账’的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='subTabTwo-iframe']"))

            # 用JS的方法点击新增按钮
            button = self.driver.find_element_by_xpath("//span[text()='新增']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 切入新增的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='addWin-iframe']"))

            #输入区域
            self.temp = self.driver.find_element_by_xpath("//input[@id='combobox-input-regionid']")
            self.temp.click()
            self.temp.send_keys("test-自动化测试")
            time.sleep(1)
            self.temp.send_keys(Keys.ARROW_DOWN)
            self.temp.send_keys(Keys.ENTER)

            #输入单位类型
            self.temp = self.driver.find_element_by_xpath("//input[@id='combobox-input-companytype']")
            self.temp.click()
            time.sleep(1)
            self.temp.send_keys(Keys.ARROW_DOWN)
            self.temp.send_keys(Keys.ENTER)
            time.sleep(1)

            #输入单位代码
            self.driver.find_element_by_xpath("//input[@id='code']").send_keys("test")
            time.sleep(2)

            #输入单位名称
            self.driver.find_element_by_xpath("//input[@id='name']").send_keys("自动化测试公司")
            time.sleep(2)

            #输入法定代表人
            self.driver.find_element_by_xpath("//input[@id='legalentity']").send_keys("testman")
            time.sleep(2)

            #输入设立日期
            today = date.today()
            self.driver.find_element_by_xpath("//input[@id='registerdate-input']").send_keys(str(today))
            # 模拟回车键
            keyDown('enter')
            keyUp('enter')
            time.sleep(2)

            #输入注册资本
            self.driver.find_element_by_xpath("//input[@id='registercapital-input']").clear()
            self.driver.find_element_by_xpath("//input[@id='registercapital-input']").send_keys("10000000")
            time.sleep(2)

            # 输入集团持股比例(%)
            self.driver.find_element_by_xpath("//input[@id='groupholdingratio-input']").send_keys("85")
            time.sleep(2)

            #股权结构增加一行
            self.driver.find_element_by_xpath("//span[text()='新增行']").click()
            time.sleep(1)

            #增加‘股权类型’
            self.temp = self.driver.find_element_by_xpath("//input[@id='combobox-input-equitystructuresgrid-equitytype-0']")
            self.temp.click()
            self.temp.send_keys("非内部单位")
            time.sleep(1)
            self.temp.send_keys(Keys.ARROW_DOWN)
            self.temp.send_keys(Keys.ENTER)
            time.sleep(1)

            # 增加‘股东’
            self.driver.find_element_by_xpath("//input[@id='equitystructuresgrid-shareholder-0']").send_keys("testman")
            time.sleep(2)

            # 增加‘证件号码’
            self.driver.find_element_by_xpath("//input[@id='equitystructuresgrid-certnumber-0']").send_keys("330326199009099010")
            time.sleep(2)

            # 增加‘认缴出资金额’
            self.driver.find_element_by_xpath("//input[@id='equitystructuresgrid-subscribedcapital-0-input']").send_keys("2000000")
            time.sleep(2)

            # 增加‘出资比例(%)’
            self.driver.find_element_by_xpath("//input[@id='equitystructuresgrid-contributionrate-0-input']").send_keys("20")
            time.sleep(2)

            # 增加‘出资期限’
            today = date.today()
            self.driver.find_element_by_xpath("//input[@id='equitystructuresgrid-contributionterm-0-input']").send_keys(str(today))
            # 模拟回车键
            keyDown('enter')
            keyUp('enter')
            time.sleep(2)

            # 增加‘实缴出资金额’
            self.driver.find_element_by_xpath("//input[@id='equitystructuresgrid-paidactualcapital-0-input']").send_keys("2000000")
            time.sleep(2)

            # 增加‘实缴出资日期’
            today = date.today()
            self.driver.find_element_by_xpath("//input[@id='equitystructuresgrid-paidactualdate-0-input']").send_keys(str(today))
            # 模拟回车键
            keyDown('enter')
            keyUp('enter')
            time.sleep(2)

            #增加质押情况内容
            #点击质押情况页面
            self.driver.find_element_by_xpath("//span[text()='质押情况']").click()
            time.sleep(1)

            #增加一行
            button = self.driver.find_element_by_xpath("//div[@id='equitypledgegrid']/following-sibling::*/descendant-or-self::*[8]")
            self.driver.execute_script("$(arguments[0]).click()", button)
            time.sleep(1)

            # 增加‘出质人’
            self.driver.find_element_by_xpath("//input[@id='equitypledgegrid-pledgor-0']").send_keys("testman")
            time.sleep(2)

            # 增加‘质权人’
            self.driver.find_element_by_xpath("//input[@id='equitypledgegrid-pledgee-0']").send_keys("testman")
            time.sleep(2)

            # 增加‘出质股权数额’
            self.driver.find_element_by_xpath("//input[@id='equitypledgegrid-pledgedamount-0-input']").send_keys("1000000")
            time.sleep(2)

            # 增加‘出质比例(%)’
            self.driver.find_element_by_xpath("//input[@id='equitypledgegrid-pledgedrate-0-input']").send_keys("10")
            time.sleep(2)

            # 增加‘被担保债权数额’
            self.driver.find_element_by_xpath("//input[@id='equitypledgegrid-secureddebtamount-0-input']").send_keys("500000")
            time.sleep(2)

            # 增加‘股权出质设立登记日期’
            today = date.today()
            self.driver.find_element_by_xpath("//input[@id='equitypledgegrid-registerdate-0-input']").send_keys(str(today))
            # 模拟回车键
            keyDown('enter')
            keyUp('enter')
            time.sleep(2)

            # 增加‘登记编号’
            self.driver.find_element_by_xpath("//input[@id='equitypledgegrid-registrationnumber-0']").send_keys("A88888888")
            time.sleep(2)

            # 增加‘对应业务’
            self.driver.find_element_by_xpath("//input[@id='equitypledgegrid-business-0']").send_keys("项目融资")
            time.sleep(2)

            # 增加‘退出时间’
            today = date.today()
            self.driver.find_element_by_xpath("//input[@id='equitypledgegrid-exittime-0-input']").send_keys(str(today))
            # 模拟回车键
            keyDown('enter')
            keyUp('enter')
            time.sleep(2)

            #切换到‘组织结构’页面
            #点击‘组织结构’
            self.driver.find_element_by_xpath("//span[text()='组织机构']").click()

            #选择‘产生方式’
            self.temp = self.driver.find_element_by_xpath("//input[@id='combobox-input-administrationgrid-establishtype-0']")
            self.temp.click()
            self.temp.send_keys("委派")
            time.sleep(1)
            self.temp.send_keys(Keys.ARROW_DOWN)
            self.temp.send_keys(Keys.ENTER)

            # 输入‘成员姓名’
            self.driver.find_element_by_xpath("//input[@id='administrationgrid-member-0']").send_keys("testman")
            time.sleep(2)

            # 输入‘职权’
            self.driver.find_element_by_xpath("//input[@id='administrationgrid-authority-0']").send_keys("董事")
            time.sleep(2)

            # 输入‘议事规则’
            self.driver.find_element_by_xpath("//input[@id='administrationgrid-debaterules-0']").send_keys("暂定")
            time.sleep(2)

            #切换到‘印章/证照’页面
            #点击‘印章/证照’页面
            self.driver.find_element_by_xpath("//span[text()='印章/证照']").click()

            #新增一行
            button = self.driver.find_element_by_xpath("//div[@id='certificationsgrid']/following-sibling::*/descendant-or-self::*[8]")
            self.driver.execute_script("$(arguments[0]).click()", button)
            time.sleep(1)

            # 输入‘印章、证照’
            self.driver.find_element_by_xpath("//input[@id='certificationsgrid-name-0']").send_keys("印章")
            time.sleep(2)

            # 输入‘保管地点’
            self.driver.find_element_by_xpath("//input[@id='certificationsgrid-storageaddress-0']").send_keys("杭州")
            time.sleep(2)

            # 输入‘保管人’
            self.driver.find_element_by_xpath("//input[@id='certificationsgrid-keeper-0']").send_keys("testman")
            time.sleep(2)

            # 增加‘入库时间’
            today = date.today()
            self.driver.find_element_by_xpath("//input[@id='certificationsgrid-storagetime-0-input']").send_keys(str(today))
            # 模拟回车键
            keyDown('enter')
            keyUp('enter')
            time.sleep(2)

            # 输入‘对接人’
            self.driver.find_element_by_xpath("//input[@id='certificationsgrid-director-0']").send_keys("testman2")
            time.sleep(2)

            # 点击保存按钮
            self.driver.find_element_by_xpath("//span[text()='保存']").click()

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 用隐式等待方法等页面出现新增成功的提示框
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath("//span[contains(text(),'操作成功！')]")
            print('单位台账数据，保存成功！')
            time.sleep(3)

            #切入‘单位管理’的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='companyManager-tab-iframe']"))
            #切入‘单位管理--单位台账’的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='subTabTwo-iframe']"))

            # 点击查看
            #用JS的方法点击放大镜
            button = self.driver.find_element_by_xpath("//span[@class='f-contrac-close']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 输入单位代码
            self.driver.find_element_by_xpath("//input[@id='code']").send_keys("test")
            time.sleep(1)

            #点击查询
            self.driver.find_element_by_xpath("//span[text()='查询']").click()
            time.sleep(2)

            #修改
            # 勾选
            self.driver.find_element_by_xpath("//div[@title='区域:test-自动化测试']/parent::*/preceding-sibling::*[1]/descendant::*[2]").click()
            time.sleep(1)

            # 点击修改按钮
            self.driver.find_element_by_xpath("//span[text()='修改']").click()
            time.sleep(1)

            # 切入修改的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='modWin-iframe']"))

            # 修改单位名称
            self.driver.find_element_by_xpath("//input[@id='name']").send_keys("修改")
            time.sleep(2)

            # 点击保存按钮
            self.driver.find_element_by_xpath("//span[text()='保存']").click()

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 用隐式等待方法等页面出现新增成功的提示框
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath("//span[contains(text(),'操作成功！')]")
            print('单位台账数据，修改成功！')
            time.sleep(3)

            # 切入‘单位管理’的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='companyManager-tab-iframe']"))
            # 切入‘单位管理--单位台账’的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='subTabTwo-iframe']"))

            #股权结构变更
            # 勾选
            self.driver.find_element_by_xpath("//div[@title='区域:test-自动化测试']/parent::*/preceding-sibling::*[1]/descendant::*[2]").click()
            time.sleep(1)

            # 点击‘股权结构变更’按钮
            self.driver.find_element_by_xpath("//span[text()='股权结构变更']").click()
            time.sleep(1)

            # #输入‘股权变更日期’
            # today = date.today()
            # self.driver.find_element_by_xpath("//input[@id='changeEquityStructureDate-input']").clear()
            # self.driver.find_element_by_xpath("//input[@id='changeEquityStructureDate-input']").send_keys(str(today))
            # time.sleep(2)
            # # 模拟回车键
            # keyDown('enter')
            # keyUp('enter')
            # time.sleep(2)

            #点击确认
            self.driver.find_element_by_xpath("//span[text()='确定']").click()

            # 切入‘股权变更’的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='subwin-iframe']"))

            # 修改股东
            self.driver.find_element_by_xpath("//input[@id='equitystructuresgrid-shareholder-0']").send_keys("1")
            time.sleep(2)

            # 点击保存按钮
            self.driver.find_element_by_xpath("//span[text()='保存']").click()

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 用隐式等待方法等页面出现新增成功的提示框
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath("//span[contains(text(),'操作成功！')]")
            print('股权结构变更，成功！')
            time.sleep(3)

            # 切入‘单位管理’的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='companyManager-tab-iframe']"))
            # 切入‘单位管理--单位台账’的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='subTabTwo-iframe']"))

            #持股结构图
            # 勾选
            self.driver.find_element_by_xpath("//div[@title='区域:test-自动化测试']/parent::*/preceding-sibling::*[1]/descendant::*[2]").click()
            time.sleep(1)

            # 点击‘持股结构图’按钮
            self.driver.find_element_by_xpath("//span[text()='持股结构图']").click()
            time.sleep(1)

            #点击确认
            self.driver.find_element_by_xpath("//span[text()='确定']").click()

            # 切入‘持股结构图’的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='subwin-iframe']"))

            # 用隐式等待方法等页面出现删除的提示框
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath("//div[@align='center']/*[name()='svg']/*[2]/*/child::*[4]/child::*[2]/descendant-or-self::*[6]")
            print("持股结构图，成功！")
            time.sleep(3)

            # 退出‘持股结构图’的iframe窗体
            self.driver.switch_to.parent_frame()

            #关闭窗口
            button = self.driver.find_element_by_xpath("//div[@id='f-win-title-subwin']/child::*[1]/descendant-or-self::*[2]")
            self.driver.execute_script("$(arguments[0]).click()", button)
            time.sleep(2)

            #股权结构图
            # 点击‘股权结构图’按钮
            self.driver.find_element_by_xpath("//span[text()='股权结构图']").click()
            time.sleep(1)

            #点击确认
            self.driver.find_element_by_xpath("//span[text()='确定']").click()

            # 切入‘股权结构图’的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='subwin-iframe']"))

            # 用隐式判断里面有‘testman1’字体
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath("//div[@align='center']/*[name()='svg']/*[2]/*/child::*[4]/child::*[2]/descendant-or-self::*[6]")
            print("股权结构图，成功！")
            time.sleep(3)

            # 退出‘股权结构图’的iframe窗体
            self.driver.switch_to.parent_frame()

            #关闭窗口
            button = self.driver.find_element_by_xpath("//div[@id='f-win-title-subwin']/child::*[1]/descendant-or-self::*[2]")
            self.driver.execute_script("$(arguments[0]).click()", button)
            time.sleep(2)

            #删除功能
            #点击删除按钮
            self.driver.find_element_by_xpath("//span[text()='删除']").click()

            # 点击弹出框的OK键
            self.driver.find_element_by_xpath("//button[@id='f-message-webgen-0-okBnt']").click()

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 用隐式等待方法等页面出现删除的提示框
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath("//span[contains(text(),'成功删除')]")
            print("单位台账数据，删除成功！")
            time.sleep(3)
            
            # 进入‘单位管理--公司信息’进行操作
            # 切入‘单位管理’的iframe窗体
            switch_to("xpath", "//iframe[@id='companyManager-tab-iframe']")

            # 点击‘公司信息’页面
            click("xpath", "//span[text()='公司信息']")
            time.sleep(2)

            # 切入‘单位管理--公司信息’的iframe窗体
            switch_to("xpath", "//iframe[@id='subTabThree-iframe']")

            # 用JS的方法点击新增按钮
            js_click("xpath", "//span[text()='新增']")

            # 切入新增的iframe窗体
            switch_to("xpath", "//iframe[@id='addWin-iframe']")

            # 输入公司代码
            input("xpath", "//input[@id='code']", "TestComplete")
            time.sleep(1)

            # ‘状态’改成‘睡眠’
            clear("xpath", "//input[@id='combobox-input-status']")
            input("xpath", "//input[@id='combobox-input-status']", "睡眠")
            time.sleep(1)
            input_down("xpath", "//input[@id='combobox-input-status']")
            time.sleep(1)
            input_enter("xpath", "//input[@id='combobox-input-status']")
            sleep(1)

            # 选择经营区域
            click("xpath", "//input[@id='combobox-input-regionid']")
            time.sleep(1)
            input("xpath", "//input[@id='combobox-input-regionid']", "test-自动化测试")
            time.sleep(1)
            input_down("xpath", "//input[@id='combobox-input-regionid']")
            time.sleep(1)
            input_enter("xpath", "//input[@id='combobox-input-regionid']")
            # 模拟回车键
            keyDown('enter')
            keyUp('enter')
            time.sleep(1)

            # 输入‘统一社会信用代码’
            input("xpath", "//input[@id='bizlicenseno']", "bizlicenseno001")
            time.sleep(1)

            # 输入‘注册地址’
            input("xpath", "//input[@id='regaddr']", "浙江杭州")
            time.sleep(1)

            # 输入‘关闭日期’
            today = date.today()
            input("xpath", "//input[@id='canceldate-input']", str(today + timedelta(days=365)))

            # 输入‘备注’
            input("xpath", "//textarea[@id='remark']", "单位管理-公司信息备注")
            sleep(1)

            # 点击保存按钮
            click("xpath", "//span[text()='保存']")

            # 退出所有iframe窗体
            switch_default()

            # 用隐式等待方法等页面出现提示框
            implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
            print("单位管理--公司信息，保存成功！")
            logging.info("单位管理--公司信息，保存成功！" )
            time.sleep(3)

            # 切入‘单位管理’的iframe窗体
            switch_to("xpath", "//iframe[@id='companyManager-tab-iframe']")
            # 切入‘单位管理--公司信息’的iframe窗体
            switch_to("xpath", "//iframe[@id='subTabThree-iframe']")

            # 点击查看
            # 用JS的方法点击放大镜
            js_click("xpath", "//span[@class='f-contrac-close']")
            sleep(1)

            # 输入注册代码：TestComplete
            input("xpath", "//input[@id='code']", "TestComplete")
            sleep(1)

            # 点击查询
            click("xpath", "//span[text()='查询']")

            # 修改
            # 勾选
            click("xpath", "//div[contains(text(),'TestComplete')]/parent::*/preceding-sibling::*[2]//descendant::*[2]")

            # 点击修改按钮
            click("xpath", "//span[text()='修改']")

            # 切入修改的iframe窗体
            switch_to("xpath", "//iframe[@id='modWin-iframe']")
            sleep(1)

            # ‘状态’改成‘活跃’
            clear("xpath", "//input[@id='combobox-input-status']")
            input("xpath", "//input[@id='combobox-input-status']", "活跃")
            time.sleep(1)
            input_down("xpath", "//input[@id='combobox-input-status']")
            time.sleep(1)
            input_enter("xpath", "//input[@id='combobox-input-status']")
            sleep(1)

            # 备注框中输入新内容
            input("xpath", "//textarea[@id='remark']", "修改备注")
            sleep(1)

            # 点击保存按钮
            click("xpath", "//span[text()='保存']")

            # 退出所有iframe窗体
            switch_default()

            # 用隐式等待方法等页面出现提示框
            implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
            print("单位管理--公司信息，修改成功！")
            logging.info("单位管理--公司信息，修改成功！")
            time.sleep(3)
            
            # # 切入‘单位管理’的iframe窗体
            # switch_to("xpath", "//iframe[@id='companyManager-tab-iframe']")
            # # 切入‘单位管理--公司信息’的iframe窗体
            # switch_to("xpath", "//iframe[@id='subTabThree-iframe']")
            #
            # # 删除
            # # 勾选
            # click("xpath", "//div[contains(text(),'TestComplete')]/parent::*/preceding-sibling::*[2]//descendant::*[2]")
            #
            # # 点击删除按钮
            # click("xpath", "//span[text()='删除']")
            #
            # # 点击弹出框的OK键
            # click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
            #
            # # 退出所有iframe窗体
            # switch_default()
            #
            # # 用隐式等待方法等页面出现删除的提示框
            # implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
            # print("单位管理--公司信息，删除成功！")
            # logging.info("单位管理--公司信息，删除成功！")
            # time.sleep(3)
            
            # 进入‘单位管理--人员信息’进行操作
            # 切入‘单位管理’的iframe窗体
            switch_to("xpath", "//iframe[@id='companyManager-tab-iframe']")

            # 点击‘人员信息’页面
            click("xpath", "//span[text()='人员信息']")
            time.sleep(2)

            # 切入‘单位管理--人员信息’的iframe窗体
            switch_to("xpath", "//iframe[@id='subTabFour-iframe']")

            # 用JS的方法点击新增按钮
            js_click("xpath", "//span[text()='新增']")

            # 切入新增的iframe窗体
            switch_to("xpath", "//iframe[@id='addWin-iframe']")

            # 输入中文名
            input("xpath", "//input[@id='name']", "测试人员")
            time.sleep(1)

            # 输入英文名
            input("xpath", "//input[@id='enname']", "testman")
            time.sleep(1)

            # 输入人员编码
            input("xpath", "//input[@id='code']", "0001")
            time.sleep(1)

            #选择用户
            click("xpath", "//input[@id='combobox-input-userid']")
            time.sleep(1)
            input_down("xpath", "//input[@id='combobox-input-userid']")
            time.sleep(1)
            input_enter("xpath", "//input[@id='combobox-input-userid']")

            # 点击保存按钮
            click("xpath", "//span[text()='保存']")

            # 退出所有iframe窗体
            switch_default()

            # 用隐式等待方法等页面出现提示框
            implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
            print("单位管理--人员信息，保存成功！")
            logging.info("单位管理--人员信息，保存成功！")
            time.sleep(3)

            # 切入‘单位管理’的iframe窗体
            switch_to("xpath", "//iframe[@id='companyManager-tab-iframe']")
            # 切入‘单位管理--人员信息’的iframe窗体
            switch_to("xpath", "//iframe[@id='subTabFour-iframe']")

            # 点击查看
            # 用JS的方法点击放大镜
            js_click("xpath", "//span[@class='f-contrac-close']")
            sleep(1)

            # 输入英文名：testman
            input("xpath", "//input[@id='enname']", "testman")
            sleep(1)

            # 点击查询
            click("xpath", "//span[text()='查询']")

            # 修改
            # 勾选
            click("xpath", "//div[contains(text(),'testman')]/parent::*/preceding-sibling::*[2]//descendant::*[2]")

            # 点击修改按钮
            click("xpath", "//span[text()='修改']")

            # 切入修改的iframe窗体
            switch_to("xpath", "//iframe[@id='modWin-iframe']")
            sleep(1)

            #中文名由‘测试人员’改成‘测试人员001’
            input("xpath", "//input[@id='name']", "001")
            sleep(1)

            # 点击保存按钮
            click("xpath", "//span[text()='保存']")

            # 退出所有iframe窗体
            switch_default()

            # 用隐式等待方法等页面出现提示框
            implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
            print("单位管理--人员信息，修改成功！")
            logging.info("单位管理--人员信息，修改成功！")
            time.sleep(3)

            # 切入‘单位管理’的iframe窗体
            switch_to("xpath", "//iframe[@id='companyManager-tab-iframe']")
            # 切入‘单位管理--人员信息’的iframe窗体
            switch_to("xpath", "//iframe[@id='subTabFour-iframe']")

            # 测试‘失效’按钮
            # 勾选
            click("xpath", "//div[contains(text(),'testman')]/parent::*/preceding-sibling::*[2]//descendant::*[2]")

            #点击‘失效’按钮
            click("xpath", "//span[text()='失效']")

            # 点击弹出框的OK键
            click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

            # 退出所有iframe窗体
            switch_default()

            # 用隐式等待方法等页面出现删除的提示框
            implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
            print("单位管理--人员信息，失效成功！")
            logging.info("单位管理--人员信息，失效成功！")
            time.sleep(3)

            # 切入‘单位管理’的iframe窗体
            switch_to("xpath", "//iframe[@id='companyManager-tab-iframe']")
            # 切入‘单位管理--人员信息’的iframe窗体
            switch_to("xpath", "//iframe[@id='subTabFour-iframe']")

            # 测试‘生效’按钮
            # 勾选
            click("xpath", "//div[contains(text(),'testman')]/parent::*/preceding-sibling::*[2]//descendant::*[2]")

            # 点击‘生效’按钮
            click("xpath", "//span[text()='生效']")

            # 点击弹出框的OK键
            click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

            # 退出所有iframe窗体
            switch_default()

            # 用隐式等待方法等页面出现删除的提示框
            implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
            print("单位管理--人员信息，生效成功！")
            logging.info("单位管理--人员信息，生效成功！")
            time.sleep(3)
            
            # # 切入‘单位管理’的iframe窗体
            # switch_to("xpath", "//iframe[@id='companyManager-tab-iframe']")
            # # 切入‘单位管理--人员信息’的iframe窗体
            # switch_to("xpath", "//iframe[@id='subTabFour-iframe']")
            #
            # # 测试‘删除’按钮
            # # 勾选
            # click("xpath", "//div[contains(text(),'testman')]/parent::*/preceding-sibling::*[2]//descendant::*[2]")
            #
            # # 点击‘生效’按钮
            # click("xpath", "//span[text()='删除']")
            #
            # # 点击弹出框的OK键
            # click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
            #
            # # 退出所有iframe窗体
            # switch_default()
            #
            # # 用隐式等待方法等页面出现删除的提示框
            # implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
            # print("单位管理--人员信息，删除成功！")
            # logging.info("单位管理--人员信息，删除成功！")
            # time.sleep(3)
            
            #进入‘单位管理--区域管理’页面，删除区域管理的数据
            # 切入‘单位管理’的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='companyManager-tab-iframe']"))

            #点击‘单位管理--区域管理’页面
            self.driver.find_element_by_xpath("//span[text()='区域管理']").click()
            time.sleep(1)

            # 切入‘单位管理--区域管理’的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='subTabOne-iframe']"))

            # 勾选一个新增的内容
            self.driver.find_element_by_xpath("//div[@title='代码:test']/parent::*/preceding-sibling::*[1]/descendant::*[2]").click()
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
            print("区域管理数据，删除成功！")
            time.sleep(3)

            # 用JS的方法关闭利率方案的页面
            button = self.driver.find_element_by_xpath("//a[@title='单位管理']/child::*[1]")
            self.driver.execute_script("$(arguments[0]).click()", button)
            
            # 打印操作成功日志
            print('单位管理，操作成功!')
            logging.info("单位管理，操作成功!")
            time.sleep(2)
        except Exception as err:
            # 发生其他异常时，打印异常堆栈信息
            print(traceback.print_exc())
            logging.debug("‘单位管理’，操作失败！" + str(traceback.format_exc()))
        
        
        
        # 测试：工程项目管理
        try:
            # 退出所有iframe窗体
            self.driver.switch_to.default_content()
            #切入系统设置的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='systemconfig-tab-iframe']"))
            logging.info("开始测试‘工程项目管理’功能")

            # 用JS的方法点击基础资料下的'工程项目管理'
            button = self.driver.find_element_by_xpath("//a[@nname='工程项目管理']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            #退出所有iframe窗体
            self.driver.switch_to.default_content()
            #切入‘工程项目管理’的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='projectItemsManage-tab-iframe']"))
            #切入‘项目信息登记’的iframe窗体
            #20210628注释
            #self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='subTabOne-iframe']"))

            # 用JS的方法点击新增按钮
            button = self.driver.find_element_by_xpath("//span[text()='新增']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 切入新增的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='addWin-iframe']"))

            #输入‘工程项目管理’的项目编码
            self.driver.find_element_by_xpath("//input[@id='code']").send_keys("test1")
            time.sleep(2)

            #输入‘工程项目管理’的项目名称
            self.driver.find_element_by_xpath("//input[@id='name']").send_keys("自动化测试1")
            time.sleep(2)

            # 选择组织
            self.temp = self.driver.find_element_by_xpath("//input[@id='combobox-input-orgid']")
            self.temp.click()
            #self.temp.send_keys("收入")
            time.sleep(1)
            self.temp.send_keys(Keys.ARROW_DOWN)
            self.temp.send_keys(Keys.ENTER)
            time.sleep(2)

            # 备注框中填入值
            self.driver.find_element_by_xpath("//textarea[@id='memo']").send_keys("自动化测试1")
            time.sleep(2)

            # 点击保存按钮
            self.driver.find_element_by_xpath("//span[text()='保存']").click()

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 用隐式等待方法等页面出现新增成功的提示框
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath("//span[contains(text(),'操作成功！')]")
            print('第一个项目保存成功！')
            time.sleep(3)

            #切入‘工程项目管理’的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='projectItemsManage-tab-iframe']"))
            #切入‘项目信息登记’的iframe窗体
            # 20210628注释
            #self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='subTabOne-iframe']"))

            # 点击查看
            #用JS的方法点击放大镜
            js_click("xpath", "//span[@class='f-contrac-close']")
            sleep(1)

            # 输入代码：
            self.driver.find_element_by_xpath("//input[@id='code']").send_keys("test1")
            time.sleep(1)

            #点击查询
            self.driver.find_element_by_xpath("//span[text()='查询']").click()
            time.sleep(2)

            #修改
            # 勾选
            self.driver.find_element_by_xpath("//tr[@id='t1_t0-fixed' and @tid='t1_t0']/child::*[2]/descendant-or-self::*[3]").click()
            time.sleep(1)

            # 点击修改按钮
            self.driver.find_element_by_xpath("//span[text()='修改']").click()
            time.sleep(1)

            # 切入修改的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='modWin-iframe']"))

            # 修改描述框中的内容
            self.driver.find_element_by_xpath("//textarea[@id='memo']").send_keys("自动化测试修改")
            time.sleep(2)

            # 点击保存按钮
            self.driver.find_element_by_xpath("//span[text()='保存']").click()

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 用隐式等待方法等页面出现新增成功的提示框
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath("//span[contains(text(),'操作成功！')]")
            print('第一个项目修改成功！')
            time.sleep(3)

            #切入‘工程项目管理’的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='projectItemsManage-tab-iframe']"))
            #切入‘项目信息登记’的iframe窗体
            # 20210628注释
            #self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='subTabOne-iframe']"))

            #添加下级项目
            # 勾选
            self.driver.find_element_by_xpath("//tr[@id='t1_t0-fixed' and @tid='t1_t0']/child::*[2]/descendant-or-self::*[3]").click()
            time.sleep(1)

            #点击添加下级项目按钮
            self.driver.find_element_by_xpath("//span[text()='添加下级项目']").click()

            # 切入添加下级项目的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='addlowWin-iframe']"))

            #输入项目编号
            self.driver.find_element_by_xpath("//input[@id='code']").send_keys("test2")
            time.sleep(2)

            #输入项目名称
            self.driver.find_element_by_xpath("//input[@id='name']").send_keys("自动化测试2")
            time.sleep(2)

            #选择组织
            self.temp = self.driver.find_element_by_xpath("//input[@id='combobox-input-orgid']")
            self.temp.click()
            #self.temp.send_keys("支出")
            time.sleep(1)
            self.temp.send_keys(Keys.ARROW_DOWN)
            self.temp.send_keys(Keys.ENTER)
            time.sleep(2)

            # 备注中填入值
            self.driver.find_element_by_xpath("//textarea[@id='memo']").send_keys("自动化测试2")
            time.sleep(2)

            # 点击保存按钮
            self.driver.find_element_by_xpath("//span[text()='保存']").click()

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 用隐式等待方法等页面出现新增成功的提示框
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath("//span[contains(text(),'操作成功！')]")
            print('下级项目，保存成功！')
            time.sleep(3)

            #切入‘工程项目管理’的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='projectItemsManage-tab-iframe']"))
            #切入‘项目信息登记’的iframe窗体
            # 20210628注释
            #self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='subTabOne-iframe']"))

            #清除查询代码输入框
            clear("xpath", "//input[@id='code']")

            # 输入代码：
            self.driver.find_element_by_xpath("//input[@id='code']").send_keys("test2")
            time.sleep(1)

            #点击查询
            self.driver.find_element_by_xpath("//span[text()='查询']").click()
            time.sleep(2)


            #添加同级项目
            # 勾选
            self.driver.find_element_by_xpath("//tr[@id='t1_t0_t0-fixed' and @tid='t1_t0_t0']/child::*[2]/descendant-or-self::*[3]").click()
            time.sleep(1)

            # 点击添加同级项目按钮
            self.driver.find_element_by_xpath("//span[text()='添加同级项目']").click()

            # 切入添加同级项目的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='addsameWin-iframe']"))

            # 输入项目编号
            self.driver.find_element_by_xpath("//input[@id='code']").send_keys("test3")
            time.sleep(2)

            # 输入项目名称
            self.driver.find_element_by_xpath("//input[@id='name']").send_keys("自动化测试3")
            time.sleep(2)

            #选择组织
            self.temp = self.driver.find_element_by_xpath("//input[@id='combobox-input-orgid']")
            self.temp.click()
            #self.temp.send_keys("支出")
            time.sleep(1)
            self.temp.send_keys(Keys.ARROW_DOWN)
            self.temp.send_keys(Keys.ENTER)
            time.sleep(2)

            #备注框中填入值
            self.driver.find_element_by_xpath("//textarea[@id='memo']").send_keys("自动化测试3")
            time.sleep(2)

            # 点击保存按钮
            self.driver.find_element_by_xpath("//span[text()='保存']").click()

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 用隐式等待方法等页面出现新增成功的提示框
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath("//span[contains(text(),'操作成功！')]")
            print('同级项目，保存成功！')
            time.sleep(3)

            #切入‘工程项目管理’的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='projectItemsManage-tab-iframe']"))
            #切入‘项目信息登记’的iframe窗体
            # 20210628注释
            #self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='subTabOne-iframe']"))

            # 清除查询代码输入框
            clear("xpath", "//input[@id='code']")

            # 输入代码：
            self.driver.find_element_by_xpath("//input[@id='code']").send_keys("test1")
            time.sleep(1)

            #点击查询
            self.driver.find_element_by_xpath("//span[text()='查询']").click()
            time.sleep(2)

            #删除功能
            #勾选一个新增的test3
            #self.driver.find_element_by_xpath("//tr[@id='t1_t0_t1-fixed' and @tid='t1_t0_t1']/child::*[2]/descendant-or-self::*[3]").click()
            #time.sleep(1)
            # 勾选一个新增的test2
            #self.driver.find_element_by_xpath("//tr[@id='t1_t0_t0-fixed' and @tid='t1_t0_t0']/child::*[2]/descendant-or-self::*[3]").click()
            #time.sleep(1)
            # 勾选一个新增的test1
            self.driver.find_element_by_xpath("//tr[@id='t1_t0-fixed' and @tid='t1_t0']/child::*[2]/descendant-or-self::*[3]").click()
            time.sleep(1)

            #点击删除按钮
            self.driver.find_element_by_xpath("//span[text()='删除']").click()

            # 点击弹出框的OK键
            self.driver.find_element_by_xpath("//button[@id='f-message-webgen-0-okBnt']").click()

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 用隐式等待方法等页面出现删除的提示框
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath("//span[contains(text(),'成功删除3条')]")
            print("删除成功！")
            time.sleep(3)

            # 用JS的方法关闭工程项目管理的页面
            button = self.driver.find_element_by_xpath("//a[@title='工程项目管理']/child::*[1]")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 打印操作成功日志
            print('工程项目管理，成功!')
            logging.info("工程项目管理，成功!")
            time.sleep(2)
        except Exception as err:
            # 发生其他异常时，打印异常堆栈信息
            print(traceback.print_exc())
            logging.debug("‘工程项目管理’，操作失败！" + str(traceback.format_exc()))
        

        
        # 测试：账户标签
        try:
            # 退出所有iframe窗体
            self.driver.switch_to.default_content()
            #切入系统设置的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='systemconfig-tab-iframe']"))
            logging.info("开始测试‘账户标签’功能")

            # 用JS的方法点击基础资料下的'账户标签'
            button = self.driver.find_element_by_xpath("//a[@nname='账户标签']")
            self.driver.execute_script("$(arguments[0]).click()", button)
            time.sleep(1)

            #退出所有iframe窗体
            self.driver.switch_to.default_content()
            #切入‘账户标签’的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='accountTags-tab-iframe']"))

            # 用JS的方法点击新增按钮
            button = self.driver.find_element_by_xpath("//span[text()='新增']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 切入新增的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='addWin-iframe']"))

            #输入代码
            self.driver.find_element_by_xpath("//input[@name='code']").send_keys("test")
            time.sleep(2)

            #输入的名称
            self.driver.find_element_by_xpath("//input[@id='name']").send_keys("自动化测试")
            time.sleep(2)

            # 描述框中填入值
            self.driver.find_element_by_xpath("//textarea[@id='description']").send_keys("自动化测试")
            time.sleep(2)

            # 点击保存按钮
            self.driver.find_element_by_xpath("//span[text()='保存']").click()

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 用隐式等待方法等页面出现新增成功的提示框
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath("//span[contains(text(),'操作成功！')]")
            print('保存成功！')
            time.sleep(3)

            # 切入‘账户标签’的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='accountTags-tab-iframe']"))

            # 点击查看
            #用JS的方法点击放大镜
            button = self.driver.find_element_by_xpath("//span[@class='f-contrac-close']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 输入代码：
            self.driver.find_element_by_xpath("//input[@id='code']").send_keys("test")
            time.sleep(1)

            #点击查询
            self.driver.find_element_by_xpath("//span[text()='查询']").click()
            time.sleep(2)

            #修改
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
            print('修改成功！')
            time.sleep(3)

            # 切入‘账户标签’的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='accountTags-tab-iframe']"))

            #删除功能
            #勾选
            self.driver.find_element_by_xpath("//div[@title='代码:test']/parent::*/preceding-sibling::*[1]/descendant::*[2]").click()

            #点击删除按钮
            self.driver.find_element_by_xpath("//span[text()='删除']").click()

            # 点击弹出框的OK键
            self.driver.find_element_by_xpath("//button[@id='f-message-webgen-0-okBnt']").click()

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 用隐式等待方法等页面出现删除的提示框
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath("//span[contains(text(),'操作成功')]")
            print("删除成功！")
            time.sleep(3)

            # 用JS的方法关闭当前页面
            button = self.driver.find_element_by_xpath("//a[@title='账户标签']/child::*[1]")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 打印操作成功日志
            print('账户标签，操作成功!')
            logging.info("账户标签，操作成功!")
            time.sleep(2)
        except Exception as err:
            # 发生其他异常时，打印异常堆栈信息
            print(traceback.print_exc())
            logging.debug("‘账户标签’，操作失败！" + str(traceback.format_exc()))



        

        # 暂不写‘自定义字段--自定义字段配置’
        
        


        
        # 测试：自定义字段--自定义字段属性配置
        try:
            # 退出所有iframe窗体
            switch_default()
            # 切入系统设置的iframe窗体
            switch_to("xpath", "//iframe[@id='systemconfig-tab-iframe']")
            logging.info("开始测试‘自定义字段--自定义字段属性配置’功能")

            # 用JS的方法点击基础资料下的'自定义字段'
            js_click("xpath", "//a[@nname='自定义字段']")

            # 退出所有iframe窗体
            switch_default()
            # 切入自定义字段配置的iframe窗体
            switch_to("xpath", "//iframe[@id='custom-tab-iframe']")

            # 点击自定义字段属性配置的页面
            click("xpath", "//span[text()='自定义字段属性配置']")

            # 切入‘自定义字段--自定义字段属性配置’的iframe窗体
            switch_to("xpath", "//iframe[@id='subTabTwo-iframe']")

            # 连续新增2笔
            for i in range(1, 3):
                # 用JS的方法点击新增按钮
                js_click("xpath", "//span[text()='新增']")

                # 切入新增的iframe窗体
                switch_to("xpath", "//iframe[@id='addproductsWin-iframe']")

                # 输入代码
                input("xpath", "//input[@name='code']", "test" + str(i))
                sleep(2)

                # 输入名称
                input("xpath", "//input[@id='name']", "自动化测试" + str(i))
                sleep(2)

                # 描述框中填入值
                input("xpath", "//textarea[@id='description']", "自动化测试" + str(i))
                sleep(2)

                # 点击保存按钮
                click("xpath", "//span[text()='保存']")

                # 退出所有iframe窗体
                switch_default()

                # 用隐式等待方法等页面出现新增成功的提示框
                implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
                print("自定义字段属性配置，第%s笔成功！"% i)
                time.sleep(3)

                # 切入自定义字段配置的iframe窗体
                switch_to("xpath", "//iframe[@id='custom-tab-iframe']")
                # 切入‘自定义字段--自定义字段属性配置’的iframe窗体
                switch_to("xpath", "//iframe[@id='subTabTwo-iframe']")

            # 点击查看
            # 用JS的方法点击放大镜
            js_click("xpath", "//span[@class='f-contrac-close']")
            sleep(1)

            # 输入代码：
            input("xpath", "//input[@id='code']", "test1")
            sleep(1)

            # 点击查询
            click("xpath", "//span[text()='查询']")
            sleep(2)

            # 修改功能
            # 勾选一个查询出的数据
            click("xpath", "//div[@title='代码:test1']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
            sleep(1)

            # 点击修改按钮
            click("xpath", "//span[text()='修改']")
            sleep(1)

            # 切入修改的iframe窗体
            switch_to("xpath", "//iframe[@id='modWin-iframe']")

            # 修改描述框中的内容
            input("xpath", "//textarea[@id='description']", "自动化测试修改")
            sleep(2)

            # 点击保存按钮
            click("xpath", "//span[text()='保存']")

            # 退出所有iframe窗体
            switch_default()

            # 用隐式等待方法等页面出现新增成功的提示框
            implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
            print("自定义字段属性配置，修改成功！")
            sleep(3)

            # 切入自定义字段配置的iframe窗体
            switch_to("xpath", "//iframe[@id='custom-tab-iframe']")
            # 切入‘自定义字段--自定义字段属性配置’的iframe窗体
            switch_to("xpath", "//iframe[@id='subTabTwo-iframe']")

            # 失效按钮
            # 勾选
            click("xpath", "//div[@title='代码:test1']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
            sleep(1)

            # 点击失效按钮
            click("xpath", "//span[text()='失效']")
            sleep(1)

            # 退出所有iframe窗体
            switch_default()

            # 用隐式等待方法等页面出现提示框
            implici_wait("xpath", "//span[contains(text(),'失效成功！')]")
            print("自定义字段属性配置，点击失效成功！")
            time.sleep(3)

            # 切入自定义字段配置的iframe窗体
            switch_to("xpath", "//iframe[@id='custom-tab-iframe']")
            # 切入‘自定义字段--自定义字段属性配置’的iframe窗体
            switch_to("xpath", "//iframe[@id='subTabTwo-iframe']")

            # 生效按钮
            # 勾选
            click("xpath", "//div[@title='代码:test1']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
            sleep(1)

            # 点击生效按钮
            click("xpath", "//span[text()='生效']")
            sleep(1)

            # 退出所有iframe窗体
            switch_default()

            # 用隐式等待方法等页面出现新增成功的提示框
            implici_wait("xpath", "//span[contains(text(),'生效成功！')]")
            print("自定义字段属性配置，点击生效成功！")
            time.sleep(3)

            # 切入自定义字段配置的iframe窗体
            switch_to("xpath", "//iframe[@id='custom-tab-iframe']")
            # 切入‘自定义字段--自定义字段属性配置’的iframe窗体
            switch_to("xpath", "//iframe[@id='subTabTwo-iframe']")

            # 删除功能
            # 勾选1个
            click("xpath", "//div[@title='代码:test1']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
            sleep(1)

            # 点击删除按钮
            click("xpath", "//span[text()='删除']")

            # 点击弹出框的OK键
            click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

            # 退出所有iframe窗体
            switch_default()

            # 用隐式等待方法等页面出现撤销送审成功的提示框
            implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
            print("自定义字段属性配置test1，删除成功！")
            sleep(2)

            # 用JS的方法关闭自定义字段的页面
            js_click("xpath", "//a[@title='自定义字段']/child::*[1]")

            # 打印操作成功日志
            print('‘自定义字段--自定义字段属性配置’操作成功!')
            logging.info("‘自定义字段--自定义字段属性配置’操作成功!")
            sleep(2)
        except Exception as err:
            # 发生其他异常时，打印异常堆栈信息
            print(traceback.print_exc())
            logging.debug("‘自定义字段--自定义字段属性配置’，操作失败！" + str(traceback.format_exc()))
          


        # 测试：自定义字段--自定义字段属性值配置
        try:
            # 退出所有iframe窗体
            switch_default()
            # 切入系统设置的iframe窗体
            switch_to("xpath", "//iframe[@id='systemconfig-tab-iframe']")
            logging.info("开始测试‘自定义字段--自定义字段属性值配置’功能")

            # 用JS的方法点击基础资料下的'自定义字段'
            js_click("xpath", "//a[@nname='自定义字段']")

            # 退出所有iframe窗体
            switch_default()
            # 切入自定义字段配置的iframe窗体
            switch_to("xpath", "//iframe[@id='custom-tab-iframe']")

            # 点击自定义字段属性值配置的页面
            click("xpath", "//span[text()='自定义字段属性值配置']")

            # 切入‘自定义字段--自定义字段属性值配置’的iframe窗体
            switch_to("xpath", "//iframe[@id='subTabThree-iframe']")

            #新增
            # 用JS的方法点击新增按钮
            js_click("xpath", "//span[text()='新增']")

            # 切入新增的iframe窗体
            switch_to("xpath", "//iframe[@id='addproductsWin-iframe']")

            #选择自定义属性
            click("xpath", "//input[@id='combobox-input-customattrid']")
            sleep(1)
            input("xpath", "//input[@id='combobox-input-customattrid']", "test2-自动化测试2")
            sleep(1)
            input_down("xpath", "//input[@id='combobox-input-customattrid']")
            input_enter("xpath", "//input[@id='combobox-input-customattrid']")
            sleep(1)

            # 输入代码
            input("xpath", "//input[@name='code']", "test2-2" )
            sleep(2)

            # 输入名称
            input("xpath", "//input[@id='name']", "自动化测试2-2")
            sleep(2)

            # 描述框中填入值
            input("xpath", "//textarea[@id='description']", "自动化测试2-2")
            sleep(2)

            # 点击保存按钮
            click("xpath", "//span[text()='保存']")

            # 退出所有iframe窗体
            switch_default()

            # 用隐式等待方法等页面出现新增成功的提示框
            implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
            print("自定义字段属性值配置，保存成功！" )
            time.sleep(3)

            # 切入自定义字段配置的iframe窗体
            switch_to("xpath", "//iframe[@id='custom-tab-iframe']")
            # 切入‘自定义字段--自定义字段属性值配置’的iframe窗体
            switch_to("xpath", "//iframe[@id='subTabThree-iframe']")

            # 点击查看
            # 用JS的方法点击放大镜
            js_click("xpath", "//span[@class='f-contrac-close']")
            sleep(1)

            # 输入代码：
            input("xpath", "//input[@id='code']", "test2-2")
            sleep(1)

            # 点击查询
            click("xpath", "//span[text()='查询']")
            sleep(2)

            # 修改功能
            # 勾选一个查询出的数据
            click("xpath", "//div[@title='代码:test2-2']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
            sleep(1)

            # 点击修改按钮
            click("xpath", "//span[text()='修改']")
            sleep(1)

            # 切入修改的iframe窗体
            switch_to("xpath", "//iframe[@id='modWin-iframe']")

            # 修改描述框中的内容
            input("xpath", "//textarea[@id='description']", "自动化测试修改")
            sleep(2)

            # 点击保存按钮
            click("xpath", "//span[text()='保存']")

            # 退出所有iframe窗体
            switch_default()

            # 用隐式等待方法等页面出现新增成功的提示框
            implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
            print("自定义字段属性值配置，修改成功！")
            sleep(3)

            # 切入自定义字段配置的iframe窗体
            switch_to("xpath", "//iframe[@id='custom-tab-iframe']")
            # 切入‘自定义字段--自定义字段属性值配置’的iframe窗体
            switch_to("xpath", "//iframe[@id='subTabThree-iframe']")

            # 失效按钮
            # 勾选
            click("xpath", "//div[@title='代码:test2-2']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
            sleep(1)

            # 点击失效按钮
            click("xpath", "//span[text()='失效']")
            sleep(1)

            # 退出所有iframe窗体
            switch_default()

            # 用隐式等待方法等页面出现提示框
            implici_wait("xpath", "//span[contains(text(),'失效成功！')]")
            print("自定义字段属性值配置，点击失效成功！")
            time.sleep(3)

            # 切入自定义字段配置的iframe窗体
            switch_to("xpath", "//iframe[@id='custom-tab-iframe']")
            # 切入‘自定义字段--自定义字段属性值配置’的iframe窗体
            switch_to("xpath", "//iframe[@id='subTabThree-iframe']")

            # 生效按钮
            # 勾选
            click("xpath", "//div[@title='代码:test2-2']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
            sleep(1)

            # 点击生效按钮
            click("xpath", "//span[text()='生效']")
            sleep(1)

            # 退出所有iframe窗体
            switch_default()

            # 用隐式等待方法等页面出现新增成功的提示框
            implici_wait("xpath", "//span[contains(text(),'生效成功！')]")
            print("自定义字段属性值配置，点击生效成功！")
            time.sleep(3)

            # 切入自定义字段配置的iframe窗体
            switch_to("xpath", "//iframe[@id='custom-tab-iframe']")
            # 切入‘自定义字段--自定义字段属性值配置’的iframe窗体
            switch_to("xpath", "//iframe[@id='subTabThree-iframe']")

            #添加下级属性值
            # 勾选
            click("xpath", "//div[@title='代码:test2-2']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
            sleep(1)

            #点击‘添加下级熟悉值’按钮
            click("xpath", "//span[text()='添加下级属性值']")
            sleep(1)

            # 切入新增的iframe窗体
            switch_to("xpath", "//iframe[@id='modWin-iframe']")

            # 输入代码
            input("xpath", "//input[@name='code']", "test2-2-2")
            sleep(2)

            # 输入名称
            input("xpath", "//input[@id='name']", "自动化测试2-2-2")
            sleep(2)

            # 描述框中填入值
            input("xpath", "//textarea[@id='description']", "自动化测试2-2-2")
            sleep(2)

            # 点击保存按钮
            click("xpath", "//span[text()='保存']")

            # 退出所有iframe窗体
            switch_default()

            # 用隐式等待方法等页面出现新增成功的提示框
            implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
            print("添加下级属性值，保存成功！" )
            time.sleep(3)

            # 切入自定义字段配置的iframe窗体
            switch_to("xpath", "//iframe[@id='custom-tab-iframe']")
            # 切入‘自定义字段--自定义字段属性值配置’的iframe窗体
            switch_to("xpath", "//iframe[@id='subTabThree-iframe']")

            # 点击‘重置’查询
            # 点击查询按钮旁边的倒三角
            click("xpath", "//em[@class='f-btngroup-click']")
            time.sleep(1)
            # 点击重置按钮
            click("xpath", "//a[text()='重置']")
            time.sleep(1)

            # 输入代码：
            input("xpath", "//input[@id='code']", "test2-2-2")
            sleep(1)

            # 点击查询
            click("xpath", "//span[text()='查询']")
            sleep(2)

            # 修改功能
            # 勾选一个查询出的数据
            click("xpath", "//div[@title='代码:test2-2-2']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
            sleep(1)

            # 点击修改按钮
            click("xpath", "//span[text()='修改']")
            sleep(1)

            # 切入修改的iframe窗体
            switch_to("xpath", "//iframe[@id='modWin-iframe']")

            # 修改描述框中的内容
            input("xpath", "//textarea[@id='description']", "自动化测试修改")
            sleep(2)

            # 点击保存按钮
            click("xpath", "//span[text()='保存']")

            # 退出所有iframe窗体
            switch_default()

            # 用隐式等待方法等页面出现新增成功的提示框
            implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
            print("添加下级属性值，修改成功！")
            sleep(3)

            # 切入自定义字段配置的iframe窗体
            switch_to("xpath", "//iframe[@id='custom-tab-iframe']")
            # 切入‘自定义字段--自定义字段属性值配置’的iframe窗体
            switch_to("xpath", "//iframe[@id='subTabThree-iframe']")

            # 失效按钮
            # 勾选
            click("xpath", "//div[@title='代码:test2-2-2']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
            sleep(1)

            # 点击失效按钮
            click("xpath", "//span[text()='失效']")
            sleep(1)

            # 退出所有iframe窗体
            switch_default()

            # 用隐式等待方法等页面出现提示框
            implici_wait("xpath", "//span[contains(text(),'失效成功！')]")
            print("添加下级属性值，点击失效成功！")
            time.sleep(3)

            # 切入自定义字段配置的iframe窗体
            switch_to("xpath", "//iframe[@id='custom-tab-iframe']")
            # 切入‘自定义字段--自定义字段属性值配置’的iframe窗体
            switch_to("xpath", "//iframe[@id='subTabThree-iframe']")

            # 生效按钮
            # 勾选
            click("xpath", "//div[@title='代码:test2-2-2']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
            sleep(1)

            # 点击生效按钮
            click("xpath", "//span[text()='生效']")
            sleep(1)

            # 退出所有iframe窗体
            switch_default()

            # 用隐式等待方法等页面出现新增成功的提示框
            implici_wait("xpath", "//span[contains(text(),'生效成功！')]")
            print("添加下级属性值，点击生效成功！")
            time.sleep(3)

            # 切入自定义字段配置的iframe窗体
            switch_to("xpath", "//iframe[@id='custom-tab-iframe']")
            # 切入‘自定义字段--自定义字段属性值配置’的iframe窗体
            switch_to("xpath", "//iframe[@id='subTabThree-iframe']")

            # 删除功能
            # 勾选
            click("xpath", "//div[@title='代码:test2-2-2']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
            sleep(1)

            # 点击删除按钮
            click("xpath", "//span[text()='删除']")

            # 点击弹出框的OK键
            click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

            # 退出所有iframe窗体
            switch_default()

            # 用隐式等待方法等页面出现提示框
            implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
            print("添加下级属性值，删除成功！")
            sleep(2)

            # 切入自定义字段配置的iframe窗体
            switch_to("xpath", "//iframe[@id='custom-tab-iframe']")
            # 切入‘自定义字段--自定义字段属性值配置’的iframe窗体
            switch_to("xpath", "//iframe[@id='subTabThree-iframe']")

            # 点击‘重置’查询
            # 点击查询按钮旁边的倒三角
            click("xpath", "//em[@class='f-btngroup-click']")
            time.sleep(1)
            # 点击重置按钮
            click("xpath", "//a[text()='重置']")
            time.sleep(1)

            # 输入代码：
            input("xpath", "//input[@id='code']", "test2-2")
            sleep(1)

            # 点击查询
            click("xpath", "//span[text()='查询']")
            sleep(2)

            # 删除功能
            # 勾选
            click("xpath", "//div[@title='代码:test2-2']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
            sleep(1)

            # 点击删除按钮
            click("xpath", "//span[text()='删除']")

            # 点击弹出框的OK键
            click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

            # 退出所有iframe窗体
            switch_default()

            # 用隐式等待方法等页面出现提示框
            implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
            print("自定义字段属性值配置，删除成功！")
            sleep(2)

            # 切入自定义字段配置的iframe窗体
            switch_to("xpath", "//iframe[@id='custom-tab-iframe']")

            # 点击自定义字段属性配置页面
            click("xpath", "//span[text()='自定义字段属性配置']")

            # 切入‘自定义字段--自定义字段属性配置’的iframe窗体
            switch_to("xpath", "//iframe[@id='subTabTwo-iframe']")

            # 点击查看
            # 用JS的方法点击放大镜
            js_click("xpath", "//span[@class='f-contrac-close']")
            sleep(1)

            # 输入代码：
            input("xpath", "//input[@id='code']", "test2")
            sleep(1)

            # 点击查询
            click("xpath", "//span[text()='查询']")
            sleep(2)

            # 删除功能
            # 勾选
            click("xpath", "//div[@title='代码:test2']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
            sleep(1)

            # 点击删除按钮
            click("xpath", "//span[text()='删除']")

            # 点击弹出框的OK键
            click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

            # 退出所有iframe窗体
            switch_default()

            # 用隐式等待方法等页面出现提示框
            implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
            print("自定义字段属性配置test2，删除成功！")
            sleep(2)

            # 用JS的方法关闭自定义字段的页面
            js_click("xpath", "//a[@title='自定义字段']/child::*[1]")

            # 打印操作成功日志
            print('‘自定义字段--自定义字段属性值配置’操作成功!')
            logging.info("‘自定义字段--自定义字段属性值配置’操作成功!")
            sleep(2)
        except Exception as err:
            # 发生其他异常时，打印异常堆栈信息
            print(traceback.print_exc())
            logging.debug("‘自定义字段--自定义字段属性值配置’，操作失败！" + str(traceback.format_exc()))
        


        # 测试：金融机构
        try:
            # 退出所有iframe窗体
            switch_default()
            # 切入系统设置的iframe窗体
            switch_to("xpath", "//iframe[@id='systemconfig-tab-iframe']")
            logging.info("开始测试‘金融机构’功能")

            # 用JS的方法点击基础资料下的'金融机构'
            js_click("xpath", "//a[@nname='金融机构']")

            # 退出所有iframe窗体
            switch_default()
            # 切入'金融机构'的iframe窗体
            switch_to("xpath", "//iframe[@id='financialInstitutions-tab-iframe']")

            # 连续新增2笔
            for i in range(1, 3):
                # 用JS的方法点击新增按钮
                js_click("xpath", "//span[text()='新增']")

                # 切入新增的iframe窗体
                switch_to("xpath", "//iframe[@id='addWin-iframe']")

                # 输入代码
                input("xpath", "//input[@name='code']", "test" + str(i))
                sleep(2)

                # 输入名称
                input("xpath", "//input[@id='name']", "自动化测试" + str(i))
                sleep(2)

                # 输入简称
                input("xpath", "//input[@id='shortname']", "自动化测试--简称" + str(i))
                sleep(2)

                # 描述框中填入值
                input("xpath", "//textarea[@id='description']", "自动化测试--描述框" + str(i))
                sleep(2)

                #选择一个分类
                click("xpath", "//input[@id='combobox-input-classification']")
                input_enter("xpath", "//input[@id='combobox-input-classification']")

                #选择类型
                click("xpath", "//input[@id='combobox-input-type']")
                sleep(1)
                if i==1:
                    #第1次选择‘融资’
                    input_enter("xpath", "//input[@id='combobox-input-type']")
                else:
                    # 第2次选择‘投资’
                    input_down("xpath", "//input[@id='combobox-input-type']")
                    input_enter("xpath", "//input[@id='combobox-input-type']")

                # 点击保存按钮
                click("xpath", "//span[text()='保存']")

                # 退出所有iframe窗体
                switch_default()

                # 用隐式等待方法等页面出现提示框
                implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
                print("金融机构，保存第%s笔成功！" % i)
                time.sleep(3)

                # 切入'金融机构'的iframe窗体
                switch_to("xpath", "//iframe[@id='financialInstitutions-tab-iframe']")

            # 点击查看
            # 用JS的方法点击放大镜
            js_click("xpath", "//span[@class='f-contrac-close']")
            sleep(1)

            # 输入代码：
            input("xpath", "//input[@id='code']", "test1")
            sleep(1)

            # 点击查询
            click("xpath", "//span[text()='查询']")
            sleep(2)

            # 修改功能
            # 勾选一个查询出的数据
            click("xpath", "//div[@title='代码:test1']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
            sleep(1)

            # 点击修改按钮
            click("xpath", "//span[text()='修改']")
            sleep(1)

            # 切入修改的iframe窗体
            switch_to("xpath", "//iframe[@id='modWin-iframe']")

            # 修改描述框中的内容
            input("xpath", "//textarea[@id='description']", "自动化测试修改")
            sleep(2)

            # 点击保存按钮
            click("xpath", "//span[text()='保存']")

            # 退出所有iframe窗体
            switch_default()

            # 用隐式等待方法等页面出现新增成功的提示框
            implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
            print("金融机构，修改成功！")
            sleep(3)

            # 切入'金融机构'的iframe窗体
            switch_to("xpath", "//iframe[@id='financialInstitutions-tab-iframe']")

            # 失效按钮
            # 勾选
            click("xpath", "//div[@title='代码:test1']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
            sleep(1)

            # 点击失效按钮
            click("xpath", "//span[text()='失效']")
            sleep(1)

            # 点击弹出框的OK键
            click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

            # 退出所有iframe窗体
            switch_default()

            # 用隐式等待方法等页面出现提示框
            implici_wait("xpath", "//span[contains(text(),'失效成功！')]")
            print("金融机构，点击失效成功！")
            time.sleep(3)

            # 切入'金融机构'的iframe窗体
            switch_to("xpath", "//iframe[@id='financialInstitutions-tab-iframe']")

            # 生效按钮
            # 勾选
            click("xpath", "//div[@title='代码:test1']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
            sleep(1)

            # 点击生效按钮
            click("xpath", "//span[text()='生效']")
            sleep(1)

            # 点击弹出框的OK键
            click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

            # 退出所有iframe窗体
            switch_default()

            # 用隐式等待方法等页面出现新增成功的提示框
            implici_wait("xpath", "//span[contains(text(),'生效成功！')]")
            print("金融机构，点击生效成功！")
            time.sleep(3)

            # 切入'金融机构'的iframe窗体
            switch_to("xpath", "//iframe[@id='financialInstitutions-tab-iframe']")

            # 删除功能
            # 勾选1个
            click("xpath", "//div[@title='代码:test1']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
            sleep(1)

            # 点击删除按钮
            click("xpath", "//span[text()='删除']")

            # 点击弹出框的OK键
            click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

            # 退出所有iframe窗体
            switch_default()

            # 用隐式等待方法等页面出现撤销送审成功的提示框
            implici_wait("xpath", "//span[contains(text(),'成功删除1条记录！')]")
            print("金融机构test1，删除成功！")
            sleep(2)

            # 切入'金融机构'的iframe窗体
            switch_to("xpath", "//iframe[@id='financialInstitutions-tab-iframe']")

            #点击按钮‘引入银行数据’
            click("xpath", "//span[text()='引入银行数据']")

            # 退出所有iframe窗体
            switch_default()

            # 用隐式等待方法等页面出现提示框
            implici_wait("xpath", "//span[contains(text(),'引入成功')]")
            print("引入银行数据，按钮正常！")
            sleep(3)

            # 切入'金融机构'的iframe窗体
            switch_to("xpath", "//iframe[@id='financialInstitutions-tab-iframe']")

            # 点击按钮‘引入内部组织’
            click("xpath", "//span[text()='引入内部组织']")

            # 退出所有iframe窗体
            switch_default()

            # 用隐式等待方法等页面出现提示框
            implici_wait("xpath", "//span[contains(text(),'引入成功')]")
            print("引入内部组织，按钮正常！")
            sleep(3)

            # 用JS的方法关闭自定义字段的页面
            js_click("xpath", "//a[@title='金融机构']/child::*[1]")

            # 打印操作成功日志
            print('‘金融机构’操作成功!')
            logging.info("‘金融机构’操作成功!")
            sleep(2)
        except Exception as err:
            # 发生其他异常时，打印异常堆栈信息
            print(traceback.print_exc())
            logging.debug("‘金融机构’，操作失败！" + str(traceback.format_exc()))

        
        # 测试：金融机构网点
        try:
            # 退出所有iframe窗体
            switch_default()
            # 切入系统设置的iframe窗体
            switch_to("xpath", "//iframe[@id='systemconfig-tab-iframe']")
            logging.info("开始测试‘金融机构网点’功能")

            # 用JS的方法点击基础资料下的'金融机构网点'
            js_click("xpath", "//a[@nname='金融机构网点']")

            # 退出所有iframe窗体
            switch_default()
            # 切入'金融机构网点'的iframe窗体
            switch_to("xpath", "//iframe[@id='financialInstitutionNetworks-tab-iframe']")

            # 新增
            # 用JS的方法点击新增按钮
            js_click("xpath", "//span[text()='新增']")

            # 切入新增的iframe窗体
            switch_to("xpath", "//iframe[@id='addWin-iframe']")

            # 输入代码
            input("xpath", "//input[@name='code']", "test2-2" )
            sleep(2)

            # 输入名称
            input("xpath", "//input[@id='name']", "自动化测试2-2")
            sleep(2)

            # 描述框中填入值
            input("xpath", "//textarea[@id='description']", "自动化测试2-2-描述框" )
            sleep(2)

            #选择区域
            #点击选择区域框
            js_click("xpath", "//input[@id='combobox-input-areaid']")
            sleep(1)
            #在选择区域框中输入‘杭州’
            input("xpath", "//input[@id='combobox-input-areaid']", "杭州")
            sleep(1)
            #鼠标往下，并且选择‘杭州的区域’
            input_down("xpath", "//input[@id='combobox-input-areaid']")
            input_enter("xpath", "//input[@id='combobox-input-areaid']")

            # 选择金融机构
            # 点击金融机构框
            click("xpath", "//input[@id='combobox-input-financialinstitutionid']")
            sleep(1)
            # 在金融机构框中输入‘test2’
            input("xpath", "//input[@id='combobox-input-financialinstitutionid']", "test2")
            sleep(1)
            # 鼠标往下，并且选择‘test2的数据’
            input_down("xpath", "//input[@id='combobox-input-financialinstitutionid']")
            input_enter("xpath", "//input[@id='combobox-input-financialinstitutionid']")

            # 点击保存按钮
            click("xpath", "//span[text()='保存']")

            # 退出所有iframe窗体
            switch_default()

            # 用隐式等待方法等页面出现提示框
            implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
            print("金融机构网点，保存成功！" )
            time.sleep(3)

            # 切入'金融机构网点'的iframe窗体
            switch_to("xpath", "//iframe[@id='financialInstitutionNetworks-tab-iframe']")

            # 点击查看
            # 用JS的方法点击放大镜
            js_click("xpath", "//span[@class='f-contrac-close']")
            sleep(1)

            # 输入代码：
            input("xpath", "//input[@id='code']", "test2-2")
            sleep(1)

            # 点击查询
            js_click("xpath", "//span[text()='查询']")
            sleep(2)

            # 修改功能
            # 勾选一个查询出的数据
            click("xpath", "//div[@title='代码:test2-2']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
            sleep(1)

            # 点击修改按钮
            click("xpath", "//span[text()='修改']")
            sleep(1)

            # 切入修改的iframe窗体
            switch_to("xpath", "//iframe[@id='modWin-iframe']")

            # 修改描述框中的内容
            input("xpath", "//textarea[@id='description']", "自动化测试修改")
            sleep(2)

            # 点击保存按钮
            click("xpath", "//span[text()='保存']")

            # 退出所有iframe窗体
            switch_default()

            # 用隐式等待方法等页面出现新增成功的提示框
            implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
            print("金融机构网点，修改成功！")
            sleep(3)

            # 切入'金融机构网点'的iframe窗体
            switch_to("xpath", "//iframe[@id='financialInstitutionNetworks-tab-iframe']")

            # 失效按钮
            # 勾选
            click("xpath", "//div[@title='代码:test2-2']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
            sleep(1)

            # 点击失效按钮
            click("xpath", "//span[text()='失效']")
            sleep(1)

            # 点击弹出框的OK键
            click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

            # 退出所有iframe窗体
            switch_default()

            # 用隐式等待方法等页面出现提示框
            implici_wait("xpath", "//span[contains(text(),'失效成功！')]")
            print("金融机构网点，点击失效成功！")
            time.sleep(3)

            # 切入'金融机构网点'的iframe窗体
            switch_to("xpath", "//iframe[@id='financialInstitutionNetworks-tab-iframe']")

            # 生效按钮
            # 勾选
            click("xpath", "//div[@title='代码:test2-2']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
            sleep(1)

            # 点击生效按钮
            click("xpath", "//span[text()='生效']")
            sleep(1)

            # 点击弹出框的OK键
            click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

            # 退出所有iframe窗体
            switch_default()

            # 用隐式等待方法等页面出现新增成功的提示框
            implici_wait("xpath", "//span[contains(text(),'生效成功！')]")
            print("金融机构网点，点击生效成功！")
            time.sleep(3)

            # 切入'金融机构网点'的iframe窗体
            switch_to("xpath", "//iframe[@id='financialInstitutionNetworks-tab-iframe']")

            # 删除功能
            # 勾选1个
            click("xpath", "//div[@title='代码:test2-2']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
            sleep(1)

            # 点击删除按钮
            click("xpath", "//span[text()='删除']")

            # 点击弹出框的OK键
            click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

            # 退出所有iframe窗体
            switch_default()

            # 用隐式等待方法等页面出现撤销送审成功的提示框
            implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
            print("金融机构网点，删除成功！")
            sleep(2)

            # # 切入'金融机构网点'的iframe窗体
            # switch_to("xpath", "//iframe[@id='financialInstitutionNetworks-tab-iframe']")
            #
            # # 点击‘引入开户行数据’按钮
            # click("xpath", "//span[text()='引入开户行数据']")
            #
            # # 退出所有iframe窗体
            # switch_default()
            #
            # # 用隐式等待方法等页面出现撤销送审成功的提示框
            # implici_wait("xpath", "//span[contains(text(),'引入成功')]")
            # print("引入开户行数据，点击成功！")
            # sleep(2)
            
            # 用JS的方法关闭自定义字段的页面
            js_click("xpath", "//a[@title='金融机构网点']/child::*[1]")

            #删除金融机构中的test2数据
            # 退出所有iframe窗体
            switch_default()
            # 切入系统设置的iframe窗体
            switch_to("xpath", "//iframe[@id='systemconfig-tab-iframe']")

            # 用JS的方法点击基础资料下的'金融机构'
            js_click("xpath", "//a[@nname='金融机构']")

            # 退出所有iframe窗体
            switch_default()
            # 切入'金融机构'的iframe窗体
            switch_to("xpath", "//iframe[@id='financialInstitutions-tab-iframe']")

            # 点击查看
            # 用JS的方法点击放大镜
            js_click("xpath", "//span[@class='f-contrac-close']")
            sleep(1)

            # 输入代码：
            input("xpath", "//input[@id='code']", "test2")
            sleep(1)

            # 点击查询
            click("xpath", "//span[text()='查询']")
            sleep(2)

            # 删除功能
            # 勾选
            click("xpath", "//div[@title='代码:test2']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
            sleep(1)

            # 点击删除按钮
            click("xpath", "//span[text()='删除']")

            # 点击弹出框的OK键
            click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

            # 退出所有iframe窗体
            switch_default()

            # 用隐式等待方法等页面出现撤销送审成功的提示框
            implici_wait("xpath", "//span[contains(text(),'成功删除1条记录！')]")
            print("金融机构test2，删除成功！")
            sleep(2)

            # 用JS的方法关闭自定义字段的页面
            js_click("xpath", "//a[@title='金融机构']/child::*[1]")

            # 打印操作成功日志
            print('‘金融机构网点’操作成功!')
            logging.info("‘金融机构网点’操作成功!")
            sleep(2)
        except Exception as err:
            # 发生其他异常时，打印异常堆栈信息
            print(traceback.print_exc())
            logging.debug("‘金融机构网点’，操作失败！" + str(traceback.format_exc()))
        

        # 测试：单据对象说明
        try:
            # 退出所有iframe窗体
            switch_default()
            # 切入系统设置的iframe窗体
            switch_to("xpath", "//iframe[@id='systemconfig-tab-iframe']")
            logging.info("开始测试‘单据对象说明’功能")

            # 用JS的方法点击基础资料下的'单据对象说明'
            js_click("xpath", "//a[@nname='单据对象说明']")

            # 退出所有iframe窗体
            switch_default()
            # 切入'单据对象说明'的iframe窗体
            switch_to("xpath", "//iframe[@id='explain-tab-iframe']")

            # 新增
            # 用JS的方法点击新增按钮
            js_click("xpath", "//span[text()='新增']")

            # 切入新增的iframe窗体
            switch_to("xpath", "//iframe[@id='addWin-iframe']")

            # 输入标题
            input("xpath", "//input[@id='name']", "自动化测试-债券登记")
            sleep(2)

            # 选择单据表单类型
            # 点击单据表单类型框
            click("xpath", "//input[@id='combobox-input-noteformcategoryid']")
            sleep(1)
            # 在选择区域框中输入
            input("xpath", "//input[@id='combobox-input-noteformcategoryid']", "债券登记")
            sleep(1)
            # 鼠标往下，并且选择‘债券登记’
            input_down("xpath", "//input[@id='combobox-input-noteformcategoryid']")
            input_enter("xpath", "//input[@id='combobox-input-noteformcategoryid']")

            # 点击保存按钮
            click("xpath", "//span[text()='保存']")

            # 退出所有iframe窗体
            switch_default()

            # 用隐式等待方法等页面出现提示框
            implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
            print("单据对象说明，保存成功！")
            time.sleep(3)

            # 切入'单据对象说明'的iframe窗体
            switch_to("xpath", "//iframe[@id='explain-tab-iframe']")

            # 点击查看
            # 用JS的方法点击放大镜
            js_click("xpath", "//span[@class='f-contrac-close']")
            sleep(1)

            # 输入名称：
            input("xpath", "//input[@id='name']", "自动化测试")
            sleep(1)

            # 点击查询
            click("xpath", "//span[text()='查询']")
            sleep(2)

            # 修改功能
            # 勾选一个查询出的数据
            click("xpath", "//div[@title='名称:自动化测试-债券登记']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
            sleep(1)

            # 点击修改按钮
            click("xpath", "//span[text()='修改']")
            sleep(1)

            # 切入修改的iframe窗体
            switch_to("xpath", "//iframe[@id='modWin-iframe']")

            # 修改标题中的内容
            input("xpath", "//input[@id='name']", "自动化测试修改")
            sleep(2)

            # 点击保存按钮
            click("xpath", "//span[text()='保存']")

            # 退出所有iframe窗体
            switch_default()

            # 用隐式等待方法等页面出现新增成功的提示框
            implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
            print("单据对象说明，修改成功！")
            sleep(3)

            # 切入'单据对象说明'的iframe窗体
            switch_to("xpath", "//iframe[@id='explain-tab-iframe']")

            # 删除功能
            # 勾选1个
            click("xpath", "//div[@title='名称:自动化测试-债券登记自动化测试修改']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
            sleep(1)

            # 点击删除按钮
            click("xpath", "//span[text()='删除']")

            # 点击弹出框的OK键
            click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

            # 退出所有iframe窗体
            switch_default()

            # 用隐式等待方法等页面出现撤销送审成功的提示框
            implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
            print("单据对象说明，删除成功！")
            sleep(2)

            # 用JS的方法关闭自定义字段的页面
            js_click("xpath", "//a[@title='单据对象说明']/child::*[1]")

            # 打印操作成功日志
            print('‘单据对象说明’操作成功!')
            logging.info("‘单据对象说明’操作成功!")
            sleep(2)
        except Exception as err:
            # 发生其他异常时，打印异常堆栈信息
            print(traceback.print_exc())
            logging.debug("‘单据对象说明’，操作失败！" + str(traceback.format_exc()))
        


        # 测试：附件分类
        try:
            # 退出所有iframe窗体
            switch_default()
            # 切入系统设置的iframe窗体
            switch_to("xpath", "//iframe[@id='systemconfig-tab-iframe']")
            logging.info("开始测试‘附件分类’功能")

            # 用JS的方法点击基础资料下的'附件分类'
            js_click("xpath", "//a[@nname='附件分类']")

            # 退出所有iframe窗体
            switch_default()
            # 切入'附件分类'的iframe窗体
            switch_to("xpath", "//iframe[@id='attachcate-tab-iframe']")

            #新增
            # 用JS的方法点击新增按钮
            js_click("xpath", "//span[text()='新增']")

            # 切入新增的iframe窗体
            switch_to("xpath", "//iframe[@id='addproductsWin-iframe']")

            # 输入代码
            input("xpath", "//input[@name='code']", "test1" )
            sleep(2)

            # 输入名称
            input("xpath", "//input[@id='name']", "自动化测试附件分类")
            sleep(2)

            # 描述框中填入值
            input("xpath", "//textarea[@id='description']", "自动化测试附件分类-描述框")
            sleep(2)

            # 点击保存按钮
            click("xpath", "//span[text()='保存']")

            # 退出所有iframe窗体
            switch_default()

            # 用隐式等待方法等页面出现新增成功的提示框
            implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
            print("附件分类，保存成功！" )
            time.sleep(3)

            # 切入'附件分类'的iframe窗体
            switch_to("xpath", "//iframe[@id='attachcate-tab-iframe']")

            # 点击查看
            # 用JS的方法点击放大镜
            js_click("xpath", "//span[@class='f-contrac-close']")
            sleep(1)

            # 输入代码：
            input("xpath", "//input[@id='code']", "test1")
            sleep(1)

            # 点击查询
            click("xpath", "//span[text()='查询']")
            sleep(2)

            # 修改功能
            # 勾选一个查询出的数据
            click("xpath", "//div[@title='代码:test1']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
            sleep(1)

            # 点击修改按钮
            click("xpath", "//span[text()='修改']")
            sleep(1)

            # 切入修改的iframe窗体
            switch_to("xpath", "//iframe[@id='modWin-iframe']")

            # 修改描述框中的内容
            input("xpath", "//textarea[@id='description']", "自动化测试修改")
            sleep(2)

            # 点击保存按钮
            click("xpath", "//span[text()='保存']")

            # 退出所有iframe窗体
            switch_default()

            # 用隐式等待方法等页面出现新增成功的提示框
            implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
            print("附件分类，修改成功！")
            sleep(3)

            # 切入'附件分类'的iframe窗体
            switch_to("xpath", "//iframe[@id='attachcate-tab-iframe']")

            # 失效按钮
            # 勾选
            click("xpath", "//div[@title='代码:test1']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
            sleep(1)

            # 点击失效按钮
            click("xpath", "//span[text()='失效']")
            sleep(1)

            # 退出所有iframe窗体
            switch_default()

            # 用隐式等待方法等页面出现提示框
            implici_wait("xpath", "//span[contains(text(),'失效成功！')]")
            print("附件分类，点击失效成功！")
            time.sleep(3)

            # 切入'附件分类'的iframe窗体
            switch_to("xpath", "//iframe[@id='attachcate-tab-iframe']")

            # 生效按钮
            # 勾选
            click("xpath", "//div[@title='代码:test1']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
            sleep(1)

            # 点击生效按钮
            click("xpath", "//span[text()='生效']")
            sleep(1)

            # 退出所有iframe窗体
            switch_default()

            # 用隐式等待方法等页面出现新增成功的提示框
            implici_wait("xpath", "//span[contains(text(),'生效成功！')]")
            print("附件分类，点击生效成功！")
            time.sleep(3)

            # 切入'附件分类'的iframe窗体
            switch_to("xpath", "//iframe[@id='attachcate-tab-iframe']")

            #分配功能
            # 勾选一个查询出的数据
            click("xpath", "//div[@title='代码:test1']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
            sleep(1)

            # 点击分配按钮
            click("xpath", "//span[text()='分配']")
            sleep(1)

            # 切入分配的iframe窗体
            switch_to("xpath", "//iframe[@id='setscopeWin-iframe']")
            switch_to("xpath", "//iframe[@id='subTab-iframe']")

            # 点击查看
            # 用JS的方法点击放大镜
            js_click("xpath", "//span[@class='f-contrac-close']")
            sleep(1)

            # 输入代码：
            input("xpath", "//input[@id='code']", "JHTZ")
            sleep(1)

            # 点击查询
            click("xpath", "//span[text()='查询']")
            sleep(2)

            t=('选择本页','取消本页','选择全部','取消全部','选择本页',)
            for i in range(5):
                # 勾选
                click("xpath", "//div[@title='代码:JHTZ']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
                sleep(1)

                # 点击分配按钮
                click("xpath", "//span[text()='分配']")
                sleep(1)

                # 切入‘分配-分配’的iframe窗体
                switch_to("xpath", "//iframe[@id='distributeWin-iframe']")

                #点击‘分配授附件分类’旁边的倒三角
                click("xpath", "//span[@class='editgrid-opmenu']")
                sleep(1)

                if i==0:
                    # 第1次点击‘选择本页’的按钮
                    click("xpath", "//div[text()='选择本页']")
                    sleep(1)

                elif i==1:
                    # 第2次点击‘取消本页’的按钮
                    click("xpath", "//div[text()='取消本页']")
                    sleep(1)

                elif i==2:
                    # 第3次点击‘选择全部’的按钮
                    click("xpath", "//div[text()='选择全部']")
                    sleep(1)

                elif i==3:
                    # 第3次点击‘取消全部’的按钮
                    click("xpath", "//div[text()='取消全部']")
                    sleep(1)

                elif i==4:
                    # 第3次点击‘取消全部’的按钮
                    click("xpath", "//div[text()='选择本页']")
                    sleep(1)

                #点击‘保存’按钮
                click("xpath", "//span[text()='保存']")

                # 退出所有iframe窗体
                switch_default()

                # 用隐式等待方法等页面出现新增成功的提示框
                implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
                print(t[i]+'，保存成功！')
                sleep(3)

                # 切入'附件分类'的iframe窗体
                switch_to("xpath", "//iframe[@id='attachcate-tab-iframe']")
                # 切入分配的iframe窗体
                switch_to("xpath", "//iframe[@id='setscopeWin-iframe']")
                switch_to("xpath", "//iframe[@id='subTab-iframe']")


            #重置
            # 勾选
            click("xpath", "//div[@title='代码:JHTZ']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
            sleep(1)

            # 点击重置按钮
            click("xpath", "//span[text()='重置']")
            sleep(1)

            # 切入‘重置’的iframe窗体
            switch_to("xpath", "//iframe[@id='resetWin-iframe']")

            # 点击保存按钮
            click("xpath", "//span[text()='保存']")

            # 退出所有iframe窗体
            switch_default()

            # 用隐式等待方法等页面出现新增成功的提示框
            implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
            print("附件分类，重置成功！")
            time.sleep(3)

            #关闭分配权限页面
            # 切入'附件分类'的iframe窗体
            switch_to("xpath", "//iframe[@id='attachcate-tab-iframe']")

            #点击关闭分配权限页面按钮
            click("xpath", "//span[text()='设置适用范围']/preceding-sibling::*")
            sleep(1)

            # 删除功能
            # 点击删除按钮
            click("xpath", "//span[text()='删除']")

            # 点击弹出框的OK键
            click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

            # 退出所有iframe窗体
            switch_default()

            # 用隐式等待方法等页面出现撤销送审成功的提示框
            implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
            print("附件分类，删除成功！")
            sleep(2)

            # 用JS的方法关闭自定义字段的页面
            js_click("xpath", "//a[@title='附件分类']/child::*[1]")

            # 打印操作成功日志
            print('‘附件分类’操作成功!')
            logging.info("‘附件分类’操作成功!")
            sleep(2)
        except Exception as err:
            # 发生其他异常时，打印异常堆栈信息
            print(traceback.print_exc())
            logging.debug("‘附件分类’，操作失败！" + str(traceback.format_exc()))


        # 测试：计提方案
        try:
            # 退出所有iframe窗体
            switch_default()
            # 切入系统设置的iframe窗体
            switch_to("xpath", "//iframe[@id='systemconfig-tab-iframe']")
            logging.info("开始测试‘计提方案’功能")

            # 用JS的方法点击基础资料下的'计提方案'
            js_click("xpath", "//a[@nname='计提方案']")

            # 退出所有iframe窗体
            switch_default()
            # 切入'计提方案'的iframe窗体
            switch_to("xpath", "//iframe[@id='accrualschemes-tab-iframe']")

            # 新增
            # 用JS的方法点击新增按钮
            js_click("xpath", "//span[text()='新增']")

            # 切入新增的iframe窗体
            switch_to("xpath", "//iframe[@id='addWin-iframe']")

            # 输入方案代码
            input("xpath", "//input[@name='code']", "test1")
            sleep(2)

            # 输入方案名称
            input("xpath", "//input[@id='name']", "自动化测试计提方案")
            sleep(2)

            # 选择计提频率
            # 点击计提频率区域框
            click("xpath", "//input[@id='combobox-input-accrualfrequencymode']")
            sleep(1)
            # 鼠标往下，并且选择‘杭州的区域’
            input_down("xpath", "//input[@id='combobox-input-accrualfrequencymode']")
            input_enter("xpath", "//input[@id='combobox-input-accrualfrequencymode']")

            # 选择计提业务
            # 点击计提业务区域框
            click("xpath", "//input[@id='combobox-input-businessid']")
            sleep(1)
            # 鼠标往下，并且选择‘杭州的区域’
            input_down("xpath", "//input[@id='combobox-input-businessid']")
            input_enter("xpath", "//input[@id='combobox-input-businessid']")

            # 选择融资产品
            # 点击融资产品区域框
            click("xpath", "//input[@id='combobox-input-financeproductid']")
            sleep(1)
            # 在选择区域框中输入‘银行-项目贷款’
            input("xpath", "//input[@id='combobox-input-financeproductid']", "银行-项目贷款")
            sleep(1)
            # 勾选一个查询出的数据
            click("xpath", "//div[@title='代码-名称:101-银行-项目贷款']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
            sleep(1)

            # 描述框中填入值
            input("xpath", "//textarea[@id='memo']", "自动化测试计提方案--描述框" )
            sleep(2)

            # 点击保存按钮
            click("xpath", "//span[text()='保存']")

            # 退出所有iframe窗体
            switch_default()

            # 用隐式等待方法等页面出现提示框
            implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
            print("计提方案，保存成功！")
            time.sleep(3)

            # 切入'计提方案'的iframe窗体
            switch_to("xpath", "//iframe[@id='accrualschemes-tab-iframe']")

            # 点击查看
            # 用JS的方法点击放大镜
            js_click("xpath", "//span[@class='f-contrac-close']")
            sleep(1)

            # 输入代码：
            input("xpath", "//input[@id='code']", "test1")
            sleep(1)

            # 点击查询
            click("xpath", "//span[text()='查询']")
            sleep(2)

            # 修改功能
            # 勾选一个查询出的数据
            click("xpath", "//div[@title='方案编号:test1']/parent::*/preceding-sibling::*[2]/descendant::*[2]")
            sleep(1)

            # 点击修改按钮
            click("xpath", "//span[text()='修改']")
            sleep(1)

            # 切入修改的iframe窗体
            switch_to("xpath", "//iframe[@id='modWin-iframe']")

            # 修改描述框中的内容
            input("xpath", "//textarea[@id='memo']", "自动化测试修改")
            sleep(2)

            # 点击保存按钮
            click("xpath", "//span[text()='保存']")

            # 退出所有iframe窗体
            switch_default()

            # 用隐式等待方法等页面出现新增成功的提示框
            implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
            print("计提方案，修改成功！")
            sleep(3)

            # 切入'计提方案'的iframe窗体
            switch_to("xpath", "//iframe[@id='accrualschemes-tab-iframe']")

            # 失效按钮
            # 勾选
            click("xpath", "//div[@title='方案编号:test1']/parent::*/preceding-sibling::*[2]/descendant::*[2]")
            sleep(1)

            # 点击失效按钮
            click("xpath", "//span[text()='失效']")
            sleep(1)

            # 退出所有iframe窗体
            switch_default()

            # 用隐式等待方法等页面出现提示框
            implici_wait("xpath", "//span[contains(text(),'失效')]")
            print("计提方案，点击失效成功！")
            time.sleep(3)

            # 切入'计提方案'的iframe窗体
            switch_to("xpath", "//iframe[@id='accrualschemes-tab-iframe']")

            # 生效按钮
            # 勾选
            click("xpath", "//div[@title='方案编号:test1']/parent::*/preceding-sibling::*[2]/descendant::*[2]")
            sleep(1)

            # 点击生效按钮
            click("xpath", "//span[text()='生效']")
            sleep(1)

            # 退出所有iframe窗体
            switch_default()

            # 用隐式等待方法等页面出现新增成功的提示框
            implici_wait("xpath", "//span[contains(text(),'生效')]")
            print("计提方案，点击生效成功！")
            time.sleep(3)

            # 切入'计提方案'的iframe窗体
            switch_to("xpath", "//iframe[@id='accrualschemes-tab-iframe']")

            # 删除功能
            # 勾选1个
            click("xpath", "//div[@title='方案编号:test1']/parent::*/preceding-sibling::*[2]/descendant::*[2]")
            sleep(1)

            # 点击删除按钮
            click("xpath", "//span[text()='删除']")

            # 点击弹出框的OK键
            click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

            # 退出所有iframe窗体
            switch_default()

            # 用隐式等待方法等页面出现撤销送审成功的提示框
            implici_wait("xpath", "//span[contains(text(),'删除成功')]")
            print("计提方案，删除成功！")
            sleep(2)

            # 用JS的方法关闭自定义字段的页面
            js_click("xpath", "//a[@title='计提方案']/child::*[1]")

            # 打印操作成功日志
            print('‘计提方案’操作成功!')
            logging.info("‘计提方案’操作成功!")
            sleep(2)
        except Exception as err:
            # 发生其他异常时，打印异常堆栈信息
            print(traceback.print_exc())
            logging.debug("‘计提方案’，操作失败！" + str(traceback.format_exc()))
        


        # 测试：费用分类
        try:
            # 退出所有iframe窗体
            switch_default()
            # 切入系统设置的iframe窗体
            switch_to("xpath", "//iframe[@id='systemconfig-tab-iframe']")
            logging.info("开始测试‘费用分类’功能")

            # 用JS的方法点击基础资料下的'费用分类'
            js_click("xpath", "//a[@nname='费用分类']")

            # 退出所有iframe窗体
            switch_default()
            # 切入'费用分类'的iframe窗体
            switch_to("xpath", "//iframe[@id='feecate-tab-iframe']")

            # 新增
            # 用JS的方法点击新增按钮
            js_click("xpath", "//span[text()='新增']")

            # 切入新增的iframe窗体
            switch_to("xpath", "//iframe[@id='addproductsWin-iframe']")

            # 输入代码
            input("xpath", "//input[@id='code']", "test1")
            sleep(2)

            # 输入名称
            input("xpath", "//input[@id='name']", "自动化测试-费用分类")
            sleep(2)

            # 修改描述框中的内容
            input("xpath", "//textarea[@id='description']", "自动化测试描述框-费用分类")
            sleep(2)

            # 选择费用交易对手分类
            # 点击费用交易对手分类
            click("xpath", "//input[@id='combobox-input-feecounterpartycate']")
            sleep(1)
            # 鼠标往下，并且选择‘费用交易对手分类’
            input_down("xpath", "//input[@id='combobox-input-feecounterpartycate']")
            input_down("xpath", "//input[@id='combobox-input-feecounterpartycate']")
            input_enter("xpath", "//input[@id='combobox-input-feecounterpartycate']")

            # 点击保存按钮
            click("xpath", "//span[text()='保存']")

            # 退出所有iframe窗体
            switch_default()

            # 用隐式等待方法等页面出现提示框
            implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
            print("费用分类，保存成功！")
            time.sleep(3)

            # 切入'费用分类'的iframe窗体
            switch_to("xpath", "//iframe[@id='feecate-tab-iframe']")

            # 点击查看
            # 用JS的方法点击放大镜
            js_click("xpath", "//span[@class='f-contrac-close']")
            sleep(1)

            # 输入代码：
            input("xpath", "//input[@id='code']", "test1")
            sleep(1)

            # 点击查询
            click("xpath", "//span[text()='查询']")
            sleep(2)

            # 修改功能
            # 勾选一个查询出的数据
            click("xpath", "//div[@title='代码:test1']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
            sleep(1)

            # 点击修改按钮
            click("xpath", "//span[text()='修改']")
            sleep(1)

            # 切入修改的iframe窗体
            switch_to("xpath", "//iframe[@id='modWin-iframe']")

            # 修改描述框中的内容
            input("xpath", "//textarea[@id='description']", "自动化测试修改")
            sleep(2)

            # 点击保存按钮
            click("xpath", "//span[text()='保存']")

            # 退出所有iframe窗体
            switch_default()

            # 用隐式等待方法等页面出现新增成功的提示框
            implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
            print("费用分类，修改成功！")
            sleep(3)

            # 切入'费用分类'的iframe窗体
            switch_to("xpath", "//iframe[@id='feecate-tab-iframe']")

            # 删除功能
            # 勾选1个
            click("xpath", "//div[@title='代码:test1']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
            sleep(1)

            # 点击删除按钮
            click("xpath", "//span[text()='删除']")

            # 点击弹出框的OK键
            click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

            # 退出所有iframe窗体
            switch_default()

            # 用隐式等待方法等页面出现撤销送审成功的提示框
            implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
            print("费用分类，删除成功！")
            sleep(2)

            # 用JS的方法关闭自定义字段的页面
            js_click("xpath", "//a[@title='费用分类']/child::*[1]")

            # 打印操作成功日志
            print('‘费用分类’操作成功!')
            logging.info("‘费用分类’操作成功!")
            sleep(2)
        except Exception as err:
            # 发生其他异常时，打印异常堆栈信息
            print(traceback.print_exc())
            logging.debug("‘费用分类’，操作失败！" + str(traceback.format_exc()))


        # 测试：贸易合同
        try:
            # 退出所有iframe窗体
            switch_default()
            # 切入系统设置的iframe窗体
            switch_to("xpath", "//iframe[@id='systemconfig-tab-iframe']")
            logging.info("开始测试‘贸易合同’功能")

            # 用JS的方法点击基础资料下的'贸易合同'
            js_click("xpath", "//a[@nname='贸易合同']")

            # 退出所有iframe窗体
            switch_default()
            # 切入'贸易合同'的iframe窗体
            switch_to("xpath", "//iframe[@id='tradecontracts-tab-iframe']")

            # 新增
            # 用JS的方法点击新增按钮
            js_click("xpath", "//span[text()='新增']")

            # 切入新增的iframe窗体
            switch_to("xpath", "//iframe[@id='addWin-iframe']")

            # 输入合同年度
            temp1 = time.strftime("%Y")
            input("xpath", "//input[@id='year']", str(temp1))
            sleep(1)

            # 输入合同开始日期
            today = date.today()
            input("xpath", "//input[@id='begindate-input']", str(today))
            # 模拟回车键
            keyDown('enter')
            keyUp('enter')
            time.sleep(1)

            # 输入合同结束日期
            today1 = today + timedelta(days=360)
            input("xpath", "//input[@id='enddate-input']", str(today1))
            # 模拟回车键
            keyDown('enter')
            keyUp('enter')
            time.sleep(1)

            # 输入合同号
            input("xpath", "//input[@id='contractcode']", "test1")
            sleep(2)

            # 输入合同名称
            input("xpath", "//input[@id='contractname']", "自动化测试贸易合同")
            sleep(2)

            # 输入合同数量
            clear("xpath", "//input[@id='quantity-input']")
            input("xpath", "//input[@id='quantity-input']", "50")
            sleep(2)

            # 输入合同单价
            clear("xpath", "//input[@id='price-input']")
            input("xpath", "//input[@id='price-input']", "10000")
            sleep(2)

            # 输入合同金额
            clear("xpath", "//input[@id='amount-input']")
            input("xpath", "//input[@id='amount-input']", "500000")
            sleep(2)

            #选择币种
            #点击币种框
            click("xpath", "//input[@id='combobox-input-currencyid']")
            sleep(1)
            #在选择区域框中输入‘人民币’
            input("xpath", "//input[@id='combobox-input-currencyid']", "人民币")
            sleep(1)
            #鼠标往下，并且选择
            input_down("xpath", "//input[@id='combobox-input-currencyid']")
            input_enter("xpath", "//input[@id='combobox-input-currencyid']")

            # 输入供应商名称
            input("xpath", "//input[@id='combobox-input-supplierid']", "自动化测试")
            sleep(2)

            # 输入供应商编码
            temp = time.strftime("%Y%m%d%H%M%S")
            # 输入供应商编码
            input("xpath", "//input[@id='suppliercode']", "Test" + str(temp))
            sleep(1)

            # 输入计量单位
            input("xpath", "//input[@id='unit']", "单位(元)")
            sleep(2)

            # 备注框中填入值
            input("xpath", "//textarea[@id='description']", "自动化测试贸易合同-备注框" )
            sleep(2)

            # 点击保存按钮
            click("xpath", "//span[text()='保存']")

            # 退出所有iframe窗体
            switch_default()

            # 用隐式等待方法等页面出现提示框
            implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
            print("贸易合同，保存成功！")
            time.sleep(3)

            # 切入'贸易合同'的iframe窗体
            switch_to("xpath", "//iframe[@id='tradecontracts-tab-iframe']")

            # 点击查看
            # 用JS的方法点击放大镜
            js_click("xpath", "//span[@class='f-contrac-close']")
            sleep(1)

            # 输入合同号：
            input("xpath", "//input[@id='contractcode']", "test1")
            sleep(1)

            # 点击查询
            click("xpath", "//span[text()='查询']")
            sleep(2)

            # 修改功能
            # 勾选
            click("xpath", "//div[@title='合同号:test1']/parent::*/preceding-sibling::*[3]/descendant::*[2]")
            sleep(1)

            # 点击修改按钮
            click("xpath", "//span[text()='修改']")
            sleep(1)

            # 切入修改的iframe窗体
            switch_to("xpath", "//iframe[@id='modWin-iframe']")

            # 修改描述框中的内容
            input("xpath", "//textarea[@id='description']", "自动化测试修改")
            sleep(2)

            # 点击保存按钮
            click("xpath", "//span[text()='保存']")

            # 退出所有iframe窗体
            switch_default()

            # 用隐式等待方法等页面出现新增成功的提示框
            implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
            print("贸易合同，修改成功！")
            sleep(3)

            # 切入'贸易合同'的iframe窗体
            switch_to("xpath", "//iframe[@id='tradecontracts-tab-iframe']")

            # 失效按钮
            # 勾选
            click("xpath", "//div[@title='合同号:test1']/parent::*/preceding-sibling::*[3]/descendant::*[2]")
            sleep(1)

            # 点击失效按钮
            click("xpath", "//span[text()='失效']")
            sleep(1)

            # 点击弹出框的OK键
            click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

            # 退出所有iframe窗体
            switch_default()

            # 用隐式等待方法等页面出现提示框
            implici_wait("xpath", "//span[contains(text(),'共处理1条')]")
            print("贸易合同，点击失效成功！")
            time.sleep(3)

            # 切入'贸易合同'的iframe窗体
            switch_to("xpath", "//iframe[@id='tradecontracts-tab-iframe']")

            # 生效按钮
            # 勾选
            click("xpath", "//div[@title='合同号:test1']/parent::*/preceding-sibling::*[3]/descendant::*[2]")
            sleep(1)

            # 点击生效按钮
            click("xpath", "//span[text()='生效']")
            sleep(1)

            # 退出所有iframe窗体
            switch_default()

            # 用隐式等待方法等页面出现新增成功的提示框
            implici_wait("xpath", "//span[contains(text(),'共处理1条')]")
            print("贸易合同，点击生效成功！")
            time.sleep(3)

            # 切入'贸易合同'的iframe窗体
            switch_to("xpath", "//iframe[@id='tradecontracts-tab-iframe']")

            # 删除功能
            # 勾选1个
            click("xpath", "//div[@title='合同号:test1']/parent::*/preceding-sibling::*[3]/descendant::*[2]")
            sleep(1)

            # 点击删除按钮
            click("xpath", "//span[text()='删除']")

            # 点击弹出框的OK键
            click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

            # 退出所有iframe窗体
            switch_default()

            # 用隐式等待方法等页面出现撤销送审成功的提示框
            implici_wait("xpath", "//span[contains(text(),'成功删除')]")
            print("贸易合同，删除成功！")
            sleep(2)

            # 用JS的方法关闭自定义字段的页面
            js_click("xpath", "//a[@title='贸易合同']/child::*[1]")

            # 打印操作成功日志
            print('‘贸易合同’操作成功!')
            logging.info("‘贸易合同’操作成功!")
            sleep(2)
        except Exception as err:
            # 发生其他异常时，打印异常堆栈信息
            print(traceback.print_exc())
            logging.debug("‘贸易合同’，操作失败！" + str(traceback.format_exc()))
            


        # 测试：法人授权书
        try:
            # 退出所有iframe窗体
            switch_default()
            # 切入系统设置的iframe窗体
            switch_to("xpath", "//iframe[@id='systemconfig-tab-iframe']")
            logging.info("开始测试‘法人授权书’功能")

            # 用JS的方法点击基础资料下的'法人授权书'
            js_click("xpath", "//a[@nname='法人授权书']")

            # 退出所有iframe窗体
            switch_default()
            # 切入'法人授权书'的iframe窗体
            switch_to("xpath", "//iframe[@id='letterOfAuth-tab-iframe']")

            # 用JS的方法点击新增按钮
            js_click("xpath", "//span[text()='新增']")

            # 切入新增的iframe窗体
            switch_to("xpath", "//iframe[@id='addWin-iframe']")

            # 输入授权书编号
            input("xpath", "//input[@name='code']", "Test001")
            sleep(2)

            # 选择法人
            click("xpath", "//input[@id='combobox-input-legalrep']")
            sleep(1)
            # 在选择区域框中输入‘testman-测试人员001’
            input("xpath", "//input[@id='combobox-input-legalrep']", "test" )
            sleep(1)
            # 鼠标往下，并且选择
            input_down("xpath", "//input[@id='combobox-input-legalrep']")
            input_enter("xpath", "//input[@id='combobox-input-legalrep']")

            # 选择被授权人
            click("xpath", "//input[@id='combobox-input-authedperson']")
            sleep(1)
            # 在选择区域框中输入‘testman-测试人员001’
            input("xpath", "//input[@id='combobox-input-authedperson']", "test")
            sleep(1)
            # 勾选'testman-测试人员001'
            #click("xpath", "//div[contains(@title,'代码-名称:testman-')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")
            getElements(self.driver, "xpath", "//div[contains(@title,'代码-名称:testman-')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")[1].click()

            # 输入备注
            input("xpath", "//textarea[@id='remark']", "自动化测试--法人授权书")
            sleep(1)

            #输入生效日期
            #设置时间的变成存储
            # a = datetime.datetime.now().strftime("%Y-%m-%d")
            # # 输入
            # input("xpath", "//input[@id='effectdate-input']", a)
            # sleep(1)

            #输入失效日期
            # 设置时间的变成存储
            b = (datetime.datetime.now() + datetime.timedelta(days=10)).strftime("%Y-%m-%d")
            # 输入
            input("xpath", "//input[@id='canceldate-input']", b)
            sleep(1)

            # 点击保存按钮
            click("xpath", "//span[text()='保存']")

            # 退出所有iframe窗体
            switch_default()

            # 用隐式等待方法等页面出现提示框
            implici_wait("xpath", "//span[contains(text(),'操作成功')]")
            print("法人授权书，保存成功！")
            logging.info("法人授权书，保存成功！")
            time.sleep(3)

            # 切入'法人授权书'的iframe窗体
            switch_to("xpath", "//iframe[@id='letterOfAuth-tab-iframe']")

            # 点击查看
            # 用JS的方法点击放大镜
            js_click("xpath", "//span[@class='f-contrac-close']")
            sleep(1)

            # 输入代码：
            input("xpath", "//input[@id='code']", "Test001")
            sleep(1)

            # 点击查询
            click("xpath", "//span[text()='查询']")
            sleep(2)

            # 修改功能
            # 勾选一个查询出的数据
            click("xpath", "//div[@title='授权书编号:Test001']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
            sleep(1)

            # 点击修改按钮
            click("xpath", "//span[text()='修改']")
            sleep(1)

            # 切入修改的iframe窗体
            switch_to("xpath", "//iframe[@id='modWin-iframe']")

            # 修改描述框中的内容
            input("xpath", "//textarea[@id='remark']", "，自动化测试修改。")
            sleep(2)

            # 点击保存按钮
            click("xpath", "//span[text()='保存']")

            # 退出所有iframe窗体
            switch_default()

            # 用隐式等待方法等页面出现新增成功的提示框
            implici_wait("xpath", "//span[contains(text(),'操作成功')]")
            print("法人授权书，修改成功！")
            logging.info("法人授权书，修改成功！")
            sleep(3)

            # 切入'法人授权书'的iframe窗体
            switch_to("xpath", "//iframe[@id='letterOfAuth-tab-iframe']")

            # 失效按钮
            # 勾选
            click("xpath", "//div[@title='授权书编号:Test001']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
            sleep(1)

            # 点击失效按钮
            click("xpath", "//span[text()='失效']")
            sleep(1)

            #点击确定按钮
            click("xpath", "//div[text()='确定']")

            # 退出所有iframe窗体
            switch_default()

            # 用隐式等待方法等页面出现提示框
            implici_wait("xpath", "//span[contains(text(),'成功失效')]")
            print("法人授权书，点击失效成功！")
            logging.info("法人授权书，点击失效成功！")
            time.sleep(3)

            # 切入'法人授权书'的iframe窗体
            switch_to("xpath", "//iframe[@id='letterOfAuth-tab-iframe']")

            # 生效按钮
            # 勾选
            click("xpath", "//div[@title='授权书编号:Test001']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
            sleep(1)

            # 点击生效按钮
            click("xpath", "//span[text()='生效']")
            sleep(1)

            # 点击确定按钮
            click("xpath", "//div[text()='确定']")

            # 退出所有iframe窗体
            switch_default()

            # 用隐式等待方法等页面出现新增成功的提示框
            implici_wait("xpath", "//span[contains(text(),'成功生效')]")
            print("法人授权书，点击生效成功！")
            logging.info("法人授权书，点击生效成功！")
            time.sleep(3)

            # 切入'法人授权书'的iframe窗体
            switch_to("xpath", "//iframe[@id='letterOfAuth-tab-iframe']")

            # 删除功能
            # 勾选1个
            click("xpath", "//div[@title='授权书编号:Test001']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
            sleep(1)

            # 点击删除按钮
            click("xpath", "//span[text()='删除']")

            # 点击弹出框的OK键
            click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

            # 退出所有iframe窗体
            switch_default()

            # 用隐式等待方法等页面出现撤销送审成功的提示框
            implici_wait("xpath", "//span[contains(text(),'操作成功')]")
            print("法人授权书，删除成功！")
            logging.info("法人授权书，删除成功！")
            sleep(2)

            # 用JS的方法关闭自定义字段的页面
            js_click("xpath", "//a[@title='法人授权书']/child::*[1]")

            # 打印操作成功日志
            print('‘法人授权书’操作成功!')
            logging.info("‘法人授权书’操作成功!")
            sleep(2)
        except Exception as err:
            # 发生其他异常时，打印异常堆栈信息
            print(traceback.print_exc())
            logging.debug("‘法人授权书’，操作失败！" + str(traceback.format_exc()))
            # Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
            dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
            dir_path = make_current_hour_dir(dir_path + "\\")
            pic_path = os.path.join(dir_path, get_current_time() + ".png")
            capture(pic_path)

        
        # 测试：印鉴信息
        try:
            # 退出所有iframe窗体
            switch_default()
            # 切入系统设置的iframe窗体
            switch_to("xpath", "//iframe[@id='systemconfig-tab-iframe']")
            logging.info("开始测试‘印鉴信息’功能")

            # 用JS的方法点击基础资料下的'印鉴信息'
            js_click("xpath", "//a[@nname='印鉴信息']")

            # 退出所有iframe窗体
            switch_default()
            # 切入'印鉴信息'的iframe窗体
            switch_to("xpath", "//iframe[@id='signInfo-tab-iframe']")

            # 用JS的方法点击新增按钮
            js_click("xpath", "//span[text()='新增']")

            # 切入新增的iframe窗体
            switch_to("xpath", "//iframe[@id='addWin-iframe']")

            # 输入印鉴编码
            input("xpath", "//input[@name='code']", "Test001")
            sleep(1)

            # 选择签字人
            click("xpath", "//input[@id='combobox-input-signatoryid']")
            sleep(1)
            # 在选择区域框中输入‘testman-测试人员001’
            input("xpath", "//input[@id='combobox-input-signatoryid']", "test")
            sleep(1)
            # 勾选'testman-测试人员001'
            click("xpath", "//div[contains(@title,'代码-名称:testman-')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")
            #getElements(self.driver, "xpath","//div[contains(@title,'代码-名称:testman-')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")[1].click()

            # 输入印鉴版本
            # 设置时间的变成存储
            temp = time.strftime("%Y%m%d%H%M%S")
            input("xpath", "//input[@id='signversion']", "Test"+str(temp))
            sleep(1)

            # 输入失效日期
            # 设置时间的变成存储
            b = (datetime.datetime.now() + datetime.timedelta(days=10)).strftime("%Y-%m-%d")
            # 输入
            input("xpath", "//input[@id='canceldate-input']", b)
            sleep(1)

            # 输入备注
            input("xpath", "//textarea[@id='remark']", "自动化测试--印鉴信息")
            sleep(1)

            # 输入生效日期
            # 设置时间的变成存储
            # a = datetime.datetime.now().strftime("%Y-%m-%d")
            # # 输入
            # input("xpath", "//input[@id='effectdate-input']", a)
            # sleep(1)


            # 点击保存按钮
            click("xpath", "//span[text()='保存']")

            # 退出所有iframe窗体
            switch_default()

            # 用隐式等待方法等页面出现提示框
            implici_wait("xpath", "//span[contains(text(),'操作成功')]")
            print("印鉴信息，保存成功！")
            logging.info("印鉴信息，保存成功！")
            time.sleep(3)

            # 切入'印鉴信息'的iframe窗体
            switch_to("xpath", "//iframe[@id='signInfo-tab-iframe']")

            # 点击查看
            # 用JS的方法点击放大镜
            js_click("xpath", "//span[@class='f-contrac-close']")
            sleep(1)

            # 输入代码：
            input("xpath", "//input[@id='code']", "Test001")
            sleep(1)

            # 点击查询
            click("xpath", "//span[text()='查询']")
            sleep(2)

            # 修改功能
            # 勾选一个查询出的数据
            click("xpath", "//div[@title='印鉴编码:Test001']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
            sleep(1)

            # 点击修改按钮
            click("xpath", "//span[text()='修改']")
            sleep(1)

            # 切入修改的iframe窗体
            switch_to("xpath", "//iframe[@id='modWin-iframe']")

            # 修改描述框中的内容
            input("xpath", "//textarea[@id='remark']", "，自动化测试修改。")
            sleep(2)

            # 点击保存按钮
            click("xpath", "//span[text()='保存']")

            # 退出所有iframe窗体
            switch_default()

            # 用隐式等待方法等页面出现新增成功的提示框
            implici_wait("xpath", "//span[contains(text(),'操作成功')]")
            print("印鉴信息，修改成功！")
            logging.info("印鉴信息，修改成功！")
            sleep(3)

            # 切入'印鉴信息'的iframe窗体
            switch_to("xpath", "//iframe[@id='signInfo-tab-iframe']")

            # 失效按钮
            # 勾选
            click("xpath", "//div[@title='印鉴编码:Test001']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
            sleep(1)

            # 点击失效按钮
            click("xpath", "//span[text()='失效']")
            sleep(1)

            # 点击确定按钮
            click("xpath", "//div[text()='确定']")

            # 退出所有iframe窗体
            switch_default()

            # 用隐式等待方法等页面出现提示框
            implici_wait("xpath", "//span[contains(text(),'成功失效')]")
            print("印鉴信息，点击失效成功！")
            logging.info("印鉴信息，点击失效成功！")
            time.sleep(3)

            # 切入'印鉴信息'的iframe窗体
            switch_to("xpath", "//iframe[@id='signInfo-tab-iframe']")

            # 生效按钮
            # 勾选
            click("xpath", "//div[@title='印鉴编码:Test001']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
            sleep(1)

            # 点击生效按钮
            click("xpath", "//span[text()='生效']")
            sleep(1)

            # 点击确定按钮
            click("xpath", "//div[text()='确定']")

            # 退出所有iframe窗体
            switch_default()

            # 用隐式等待方法等页面出现新增成功的提示框
            implici_wait("xpath", "//span[contains(text(),'成功生效')]")
            print("印鉴信息，点击生效成功！")
            logging.info("印鉴信息，点击生效成功！")
            time.sleep(3)

            # 切入'印鉴信息'的iframe窗体
            switch_to("xpath", "//iframe[@id='signInfo-tab-iframe']")

            # 删除功能
            # 勾选1个
            click("xpath", "//div[@title='印鉴编码:Test001']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
            sleep(1)

            # 点击删除按钮
            click("xpath", "//span[text()='删除']")

            # 点击弹出框的OK键
            click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

            # 退出所有iframe窗体
            switch_default()

            # 用隐式等待方法等页面出现撤销送审成功的提示框
            implici_wait("xpath", "//span[contains(text(),'操作成功')]")
            print("印鉴信息，删除成功！")
            logging.info("印鉴信息，删除成功！")
            sleep(2)

            # 用JS的方法关闭自定义字段的页面
            js_click("xpath", "//a[@title='印鉴信息']/child::*[1]")

            # 打印操作成功日志
            print('‘印鉴信息’操作成功!')
            logging.info("‘印鉴信息’操作成功!")
            sleep(2)
        except Exception as err:
            # 发生其他异常时，打印异常堆栈信息
            print(traceback.print_exc())
            logging.debug("‘印鉴信息’，操作失败！" + str(traceback.format_exc()))
            # Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
            dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
            dir_path = make_current_hour_dir(dir_path + "\\")
            pic_path = os.path.join(dir_path, get_current_time() + ".png")
            capture(pic_path)
            
        
        # 测试‘门店信息’页面功能
        try:
            # 退出所有iframe窗体
            switch_default()
            # 切入系统设置的iframe窗体
            switch_to("xpath", "//iframe[@id='systemconfig-tab-iframe']")
            logging.info("开始测试‘门店信息’页面功能")

            # 用JS的方法点击直联设置下的'门店信息'
            js_click("xpath", "//a[@nname='门店信息']")

            # 退出所有iframe窗体
            switch_default()
            # 切入'门店信息'的iframe窗体
            switch_to("xpath", "//iframe[@id='storeinfo-tab-iframe']")

            # 用JS的方法点击新增按钮
            js_click("xpath", "//span[text()='新增']")

            # 切入新增的iframe窗体
            switch_to("xpath", "//iframe[@id='addWin-iframe']")

            # 输入‘公司’
            click("xpath", "//input[@id='combobox-input-companyid']")
            input("xpath", "//input[@id='combobox-input-companyid']", "Test")
            sleep(1)
            # 按键往下，选择
            input_down("xpath","//input[@id='combobox-input-companyid']")
            input_enter("xpath","//input[@id='combobox-input-companyid']")
            sleep(1)

            # 输入‘门店号’
            # 设置时间的变成存储
            temp = time.strftime("%Y%m%d%H%M%S")
            input("xpath", "//input[@id='code']", "Test"+str(temp))
            sleep(1)

            # 输入‘门店信息’
            input("xpath", "//input[@id='name']", "Test门店信息")
            sleep(1)

            # 输入关店日期
            # 设置时间的变成存储
            b = (datetime.datetime.now() + datetime.timedelta(days=100)).strftime("%Y-%m-%d")
            # 输入
            input("xpath", "//input[@id='closedate-input']", b)
            sleep(1)

            # 点击保存按钮
            click("xpath", "//span[text()='保存']")

            # 退出所有iframe窗体
            switch_default()

            # 用隐式等待方法等页面出现新增成功的提示框
            implici_wait("xpath", "//span[contains(text(),'操作成功')]")
            print("门店信息，保存成功！")
            logging.info("门店信息，保存成功！")
            time.sleep(3)

            # 切入'门店信息'的iframe窗体
            switch_to("xpath", "//iframe[@id='storeinfo-tab-iframe']")

            # 点击查看
            # 用JS的方法点击放大镜
            js_click("xpath", "//span[@class='f-contrac-close']")
            sleep(1)

            # 输入门店信息
            input("xpath", "//input[@id='name']", "Test门店信息")
            sleep(1)

            # 点击查询
            click("xpath", "//span[text()='查询']")

            # 修改
            # 勾选
            click("xpath", "//div[contains(@title,'门店名称:Test门店信息')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")
            sleep(1)
            # 点击修改按钮
            click("xpath", "//span[text()='修改']")

            # 切入修改的iframe窗体
            switch_to("xpath", "//iframe[@id='modWin-iframe']")
            sleep(1)

            # 修改关店日期
            # 设置时间的变成存储
            c = (datetime.datetime.now() + datetime.timedelta(days=50)).strftime("%Y-%m-%d")
            #清空关店日期
            clear("xpath", "//input[@id='closedate-input']")
            # 输入
            input("xpath", "//input[@id='closedate-input']", c)
            sleep(1)

            # 点击保存按钮
            click("xpath", "//span[text()='保存']")

            # 退出所有iframe窗体
            switch_default()

            # 用隐式等待方法等页面出现新增成功的提示框
            implici_wait("xpath", "//span[contains(text(),'操作成功')]")
            print("门店信息，修改成功！")
            logging.info("门店信息，修改成功！")
            time.sleep(3)

            # 切入'门店信息'的iframe窗体
            switch_to("xpath", "//iframe[@id='storeinfo-tab-iframe']")

            # 勾选
            click("xpath", "//div[contains(@title,'门店名称:Test门店信息')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")
            sleep(1)
            # 点击删除按钮
            click("xpath", "//span[text()='删除']")

            # 点击弹出框的OK键
            click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

            # 退出所有iframe窗体
            switch_default()

            # 用隐式等待方法等页面出现删除的提示框
            implici_wait("xpath", "//span[contains(text(),'操作成功')]")
            print("门店信息，删除成功！")
            logging.info("门店信息，删除成功！")
            time.sleep(3)

            # 用JS的方法关闭当前页面
            js_click("xpath", "//a[@title='门店信息']/child::*[1]")

            # 打印操作成功日志
            print("门店信息，操作成功!")
            logging.info("门店信息，操作成功!")
            time.sleep(2)
        except Exception as err:
            # 发生其他异常时，打印异常堆栈信息
            print(traceback.print_exc())
            logging.debug("'门店信息',操作失败！" + str(traceback.format_exc()))
            # Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
            dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
            dir_path = make_current_hour_dir(dir_path + "\\")
            pic_path = os.path.join(dir_path, get_current_time() + ".png")
            capture(pic_path)

        
        # 测试：计划号
        try:
            # 退出所有iframe窗体
            switch_default()
            # 切入系统设置的iframe窗体
            switch_to("xpath", "//iframe[@id='systemconfig-tab-iframe']")
            logging.info("开始测试‘计划号’功能")

            # 用JS的方法点击基础资料下的'计划号'
            js_click("xpath", "//a[@nname='计划号']")

            # 退出所有iframe窗体
            switch_default()
            # 切入'计划号'的iframe窗体
            switch_to("xpath", "//iframe[@id='plancode-tab-iframe']")

            # 用JS的方法点击新增按钮
            js_click("xpath", "//span[text()='新增']")

            # 切入新增的iframe窗体
            switch_to("xpath", "//iframe[@id='addWin-iframe']")

            # 输入代码
            input("xpath", "//input[@name='code']", "Test001")
            sleep(1)

            # 输入名称
            input("xpath", "//input[@name='name']", "Test名称")
            sleep(1)

            #选中'是否系统初始'按钮
            click("xpath", "//input[@id='issysteminit']")

            # 输入备注
            input("xpath", "//textarea[@id='description']", "自动化测试--计划号")
            sleep(1)

            # 输入生效日期
            # 设置时间的变成存储
            # a = datetime.datetime.now().strftime("%Y-%m-%d")
            # # 输入
            # input("xpath", "//input[@id='effectdate-input']", a)
            # sleep(1)

            # 点击保存按钮
            click("xpath", "//span[text()='保存']")

            # 退出所有iframe窗体
            switch_default()

            # 用隐式等待方法等页面出现提示框
            implici_wait("xpath", "//span[contains(text(),'操作成功')]")
            print("计划号，保存成功！")
            logging.info("计划号，保存成功！")
            time.sleep(3)

            # 切入'计划号'的iframe窗体
            switch_to("xpath", "//iframe[@id='plancode-tab-iframe']")

            # 点击查看
            # 用JS的方法点击放大镜
            js_click("xpath", "//span[@class='f-contrac-close']")
            sleep(1)

            # 输入代码：
            input("xpath", "//input[@id='code']", "Test001")
            sleep(1)

            # 点击查询
            click("xpath", "//span[text()='查询']")
            sleep(2)

            # 修改功能
            # 勾选一个查询出的数据
            click("xpath", "//div[@title='代码:Test001']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
            sleep(1)

            # 点击修改按钮
            click("xpath", "//span[text()='修改']")
            sleep(1)

            # 切入修改的iframe窗体
            switch_to("xpath", "//iframe[@id='modWin-iframe']")

            # 修改描述框中的内容
            input("xpath", "//textarea[@id='description']", "，自动化测试修改。")
            sleep(2)

            # 点击保存按钮
            click("xpath", "//span[text()='保存']")

            # 退出所有iframe窗体
            switch_default()

            # 用隐式等待方法等页面出现新增成功的提示框
            implici_wait("xpath", "//span[contains(text(),'操作成功')]")
            print("计划号，修改成功！")
            logging.info("计划号，修改成功！")
            sleep(3)

            # 切入'计划号'的iframe窗体
            switch_to("xpath", "//iframe[@id='plancode-tab-iframe']")

            # 失效按钮
            # 勾选
            click("xpath", "//div[@title='代码:Test001']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
            sleep(1)

            # 点击失效按钮
            click("xpath", "//span[text()='失效']")
            sleep(1)

            # 点击弹出框的OK键
            click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

            # 退出所有iframe窗体
            switch_default()

            # 用隐式等待方法等页面出现提示框
            implici_wait("xpath", "//span[contains(text(),'操作成功')]")
            print("计划号，点击失效成功！")
            logging.info("计划号，点击失效成功！")
            time.sleep(3)

            # 切入'计划号'的iframe窗体
            switch_to("xpath", "//iframe[@id='plancode-tab-iframe']")

            # 生效按钮
            # 勾选
            click("xpath", "//div[@title='代码:Test001']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
            sleep(1)

            # 点击生效按钮
            click("xpath", "//span[text()='生效']")
            sleep(1)

            # 点击弹出框的OK键
            click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

            # 退出所有iframe窗体
            switch_default()

            # 用隐式等待方法等页面出现新增成功的提示框
            implici_wait("xpath", "//span[contains(text(),'操作成功')]")
            print("计划号，点击生效成功！")
            logging.info("计划号，点击生效成功！")
            time.sleep(3)

            # 切入'计划号'的iframe窗体
            switch_to("xpath", "//iframe[@id='plancode-tab-iframe']")

            # 删除功能
            # 勾选1个
            click("xpath", "//div[@title='代码:Test001']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
            sleep(1)

            # 点击删除按钮
            click("xpath", "//span[text()='删除']")

            # 点击弹出框的OK键
            click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

            # 退出所有iframe窗体
            switch_default()

            # 用隐式等待方法等页面出现撤销送审成功的提示框
            implici_wait("xpath", "//span[contains(text(),'操作成功')]")
            print("计划号，删除成功！")
            logging.info("计划号，删除成功！")
            sleep(2)

            # 用JS的方法关闭自定义字段的页面
            js_click("xpath", "//a[@title='计划号']/child::*[1]")

            # 打印操作成功日志
            print('‘计划号’操作成功!')
            logging.info("‘计划号’操作成功!")
            sleep(2)
        except Exception as err:
            # 发生其他异常时，打印异常堆栈信息
            print(traceback.print_exc())
            logging.debug("‘计划号’，操作失败！" + str(traceback.format_exc()))
            # Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
            dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
            dir_path = make_current_hour_dir(dir_path + "\\")
            pic_path = os.path.join(dir_path, get_current_time() + ".png")
            capture(pic_path)

            
        # 删除单位管理下的：公司信息中的'TestComplete',人员信息中的'testman'
        try:
            # 退出所有iframe窗体
            switch_default()
            # 切入系统设置的iframe窗体
            switch_to("xpath", "//iframe[@id='systemconfig-tab-iframe']")
            logging.info("删除单位管理下的：公司信息中的'TestComplete',人员信息中的'testman'")

            # 用JS的方法点击直联设置下的'单位管理'
            js_click("xpath", "//a[@nname='单位管理']")

            # 退出所有iframe窗体
            switch_default()

            # 切入‘单位管理’的iframe窗体
            switch_to("xpath", "//iframe[@id='companyManager-tab-iframe']")

            # 点击‘公司信息’页面
            click("xpath", "//span[text()='公司信息']")
            time.sleep(2)

            # 切入‘单位管理--公司信息’的iframe窗体
            switch_to("xpath", "//iframe[@id='subTabThree-iframe']")

            # 删除
            # 勾选
            click("xpath", "//div[contains(text(),'TestComplete')]/parent::*/preceding-sibling::*[2]//descendant::*[2]")

            # 点击删除按钮
            click("xpath", "//span[text()='删除']")

            # 点击弹出框的OK键
            click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

            # 退出所有iframe窗体
            switch_default()

            # 用隐式等待方法等页面出现删除的提示框
            implici_wait("xpath", "//span[contains(text(),'操作成功')]")
            print("单位管理--公司信息，删除成功！")
            logging.info("单位管理--公司信息，删除成功！")
            time.sleep(3)

            # 进入‘单位管理--人员信息’进行操作
            # 切入‘单位管理’的iframe窗体
            switch_to("xpath", "//iframe[@id='companyManager-tab-iframe']")

            # 点击‘人员信息’页面
            click("xpath", "//span[text()='人员信息']")
            time.sleep(2)

            # 切入‘单位管理--人员信息’的iframe窗体
            switch_to("xpath", "//iframe[@id='subTabFour-iframe']")

            # 测试‘删除’按钮
            # 勾选
            click("xpath", "//div[contains(text(),'testman')]/parent::*/preceding-sibling::*[2]//descendant::*[2]")

            # 点击‘生效’按钮
            click("xpath", "//span[text()='删除']")

            # 点击弹出框的OK键
            click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

            # 退出所有iframe窗体
            switch_default()

            # 用隐式等待方法等页面出现删除的提示框
            implici_wait("xpath", "//span[contains(text(),'操作成功')]")
            print("单位管理--人员信息，删除成功！")
            logging.info("单位管理--人员信息，删除成功！")
            time.sleep(3)

            # 用JS的方法关闭当前页面
            js_click("xpath", "//a[@title='单位管理']/child::*[1]")

            # 打印操作成功日志
            print("删除单位管理下的：公司信息中的'TestComplete',人员信息中的'testman'，操作成功!")
            logging.info("删除单位管理下的：公司信息中的'TestComplete',人员信息中的'testman'，操作成功!")
            time.sleep(2)
        except Exception as err:
            # 发生其他异常时，打印异常堆栈信息
            print(traceback.print_exc())
            logging.debug("删除单位管理下的：公司信息中的'TestComplete',人员信息中的'testman'，操作失败！" + str(traceback.format_exc()))
            # Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
            dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
            dir_path = make_current_hour_dir(dir_path + "\\")
            pic_path = os.path.join(dir_path, get_current_time() + ".png")
            capture(pic_path)

        
        # 测试‘钉钉机器人’页面功能
        try:
            # 退出所有iframe窗体
            switch_default()
            # 切入系统设置的iframe窗体
            switch_to("xpath", "//iframe[@id='systemconfig-tab-iframe']")
            logging.info("开始测试‘钉钉机器人’页面功能")

            # 用JS的方法点击直联设置下的'钉钉机器人'
            js_click("xpath", "//a[@nname='钉钉机器人']")

            # 退出所有iframe窗体
            switch_default()
            # 切入'钉钉机器人'的iframe窗体
            switch_to("xpath", "//iframe[@id='dingrobot-tab-iframe']")

            # 用JS的方法点击新增按钮
            js_click("xpath", "//span[text()='新增']")

            # 切入新增的iframe窗体
            switch_to("xpath", "//iframe[@id='addWin-iframe']")

            # 输入‘机器人代码’
            input("xpath", "//input[@id='code']", "TestJiQiRen")
            sleep(1)

            # 输入‘机器人名称’
            input("xpath", "//input[@id='name']", "测试钉钉机器人")
            sleep(1)

            # 输入‘webhook’
            input("xpath", "//input[@id='webhook']", "www.test.com")
            sleep(1)

            # 输入‘推送群名’
            input("xpath", "//input[@id='pushgroupname']", "TestDD")
            sleep(1)

            # 选择‘交易类型’
            click("xpath", "//input[@id='combobox-input-paytypeid']")
            sleep(1)
            # 按键往下
            input_down("xpath","//input[@id='combobox-input-paytypeid']")
            input_enter("xpath","//input[@id='combobox-input-paytypeid']")
            sleep(1)

            # 输入‘查询SQL’
            input("xpath", "//textarea[@id='sqlstatement']", "select a.tenantid,a.* from TSYS_TENANT a where a.tenant_code='TestTenant'")
            sleep(1)

            # 输入‘模板内容’
            input("xpath", "//textarea[@id='templatecontent']", "查询租户，把'tenantid'的值，放到下面的delete语句中")
            sleep(1)

            # 点击保存按钮
            click("xpath", "//span[text()='保存']")

            # 退出所有iframe窗体
            switch_default()

            # 用隐式等待方法等页面出现新增成功的提示框
            implici_wait("xpath", "//span[contains(text(),'操作成功')]")
            print("钉钉机器人，保存成功！")
            logging.info("钉钉机器人，保存成功！")
            time.sleep(3)

            # 切入'钉钉机器人'的iframe窗体
            switch_to("xpath", "//iframe[@id='dingrobot-tab-iframe']")

            # 点击查看
            # 用JS的方法点击放大镜
            js_click("xpath", "//span[@class='f-contrac-close']")
            sleep(1)

            # 输入'机器人代码'
            input("xpath", "//input[@id='code']", "TestJiQiRen")
            sleep(1)

            # 点击查询
            click("xpath", "//span[text()='查询']")

            # 修改
            # 勾选
            click("xpath","//div[contains(@title,'机器人名称:测试钉钉机器人')]/parent::*/preceding-sibling::*[2]/descendant::*[2]")
            # 点击修改按钮
            click("xpath", "//span[text()='修改']")

            # 切入修改的iframe窗体
            switch_to("xpath", "//iframe[@id='modWin-iframe']")
            sleep(1)

            # 修改模板内容
            input("xpath", "//textarea[@id='templatecontent']", "，自动化测试修改")
            sleep(1)

            # 点击保存按钮
            click("xpath", "//span[text()='保存']")

            # 退出所有iframe窗体
            switch_default()

            # 用隐式等待方法等页面出现新增成功的提示框
            implici_wait("xpath", "//span[contains(text(),'操作成功')]")
            print("钉钉机器人，修改成功！")
            logging.info("钉钉机器人，修改成功！")
            time.sleep(3)

            # 切入'钉钉机器人'的iframe窗体
            switch_to("xpath", "//iframe[@id='dingrobot-tab-iframe']")

            #勾选
            click("xpath", "//div[contains(@title,'机器人名称:测试钉钉机器人')]/parent::*/preceding-sibling::*[2]/descendant::*[2]")
            # 点击删除按钮
            click("xpath", "//span[text()='删除']")

            # 点击弹出框的OK键
            click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

            # 退出所有iframe窗体
            switch_default()

            # 用隐式等待方法等页面出现删除的提示框
            implici_wait("xpath", "//span[contains(text(),'操作成功')]")
            print("钉钉机器人，删除成功！")
            logging.info("钉钉机器人，删除成功！")
            time.sleep(3)

            # 用JS的方法关闭当前页面
            js_click("xpath", "//a[@title='钉钉机器人']/child::*[1]")

            # 打印操作成功日志
            print("钉钉机器人，操作成功!")
            logging.info("钉钉机器人，操作成功!")
            time.sleep(2)
        except Exception as err:
            # 发生其他异常时，打印异常堆栈信息
            print(traceback.print_exc())
            logging.debug("钉钉机器人失败！" + str(traceback.format_exc()))
            # Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
            dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
            dir_path = make_current_hour_dir(dir_path + "\\")
            pic_path = os.path.join(dir_path, get_current_time() + ".png")
            capture(pic_path)

        
        # 测试‘工作委托’页面功能
        try:
            # 退出所有iframe窗体
            switch_default()
            # 切入系统设置的iframe窗体
            switch_to("xpath", "//iframe[@id='systemconfig-tab-iframe']")
            logging.info("开始测试‘工作委托’页面功能")

            # 用JS的方法点击直联设置下的'工作委托'
            js_click("xpath", "//a[@nname='工作委托']")

            # 退出所有iframe窗体
            switch_default()
            # 切入'工作委托'的iframe窗体
            switch_to("xpath", "//iframe[@id='delegate-tab-iframe']")

            for i in range(1,3):
                # 用JS的方法点击‘添加委托关系’
                js_click("xpath", "//span[text()='添加委托关系']")

                # 切入新增的iframe窗体
                switch_to("xpath", "//iframe[@id='custButtonWin1-iframe']")



                # 输入‘委托结束时间’
                # 设置时间的变成存储
                b = (datetime.datetime.now() + datetime.timedelta(days=10)).strftime("%Y-%m-%d %H:%M:%S")
                # 输入
                input("xpath", "//input[@id='endDate-input']", b)
                sleep(1)

                if i==2:
                    # 选择‘委托方式’
                    click("xpath", "//input[@id='combobox-input-delegateType']")
                    # 清空内容
                    clear("xpath", "//input[@id='combobox-input-delegateType']")
                    input("xpath", "//input[@id='combobox-input-delegateType']", "流程委托")
                    sleep(1)
                    input_enter("xpath", "//input[@id='combobox-input-delegateType']")
                    sleep(1)

                else:
                    # 选择‘委托方式’
                    click("xpath", "//input[@id='combobox-input-delegateType']")
                    # 清空内容
                    clear("xpath", "//input[@id='combobox-input-delegateType']")
                    input("xpath", "//input[@id='combobox-input-delegateType']", "全权委托")
                    sleep(1)
                    input_enter("xpath", "//input[@id='combobox-input-delegateType']")
                    sleep(1)

                # 输入‘委托开始时间’
                # 设置时间的变成存储
                a = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                # 输入
                input("xpath", "//input[@id='startDate-input']", a)
                sleep(1)

                # 输入‘代理人’
                click("xpath", "//input[@id='combobox-input-delegateUserId']")
                #input("xpath", "//input[@id='combobox-input-delegateUserId']", "Tao")
                sleep(1)
                # 按键往下
                input_down("xpath","//input[@id='combobox-input-delegateUserId']")
                input_enter("xpath","//input[@id='combobox-input-delegateUserId']")
                sleep(1)

                # 点击保存按钮
                click("xpath", "//span[text()='保存']")

                # 退出所有iframe窗体
                switch_default()

                # 用隐式等待方法等页面出现新增成功的提示框
                implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
                print("工作委托第%s次，保存成功！" % i)
                logging.info("工作委托第%s次，保存成功！" % i)
                time.sleep(3)

                # 切入'工作委托'的iframe窗体
                switch_to("xpath", "//iframe[@id='delegate-tab-iframe']")

            #点击'废除委托关系'按钮
            # 点击查看
            # 用JS的方法点击放大镜
            js_click("xpath", "//span[@class='f-contrac-close']")
            sleep(1)

            # 输入‘委托方式’为‘全权委托’
            click("xpath", "//input[@id='combobox-input-delegatetype']")
            input("xpath", "//input[@id='combobox-input-delegatetype']", "全权委托")
            sleep(1)
            input_enter("xpath", "//input[@id='combobox-input-delegatetype']")
            sleep(1)

            # 输入‘代理人’为‘Tao’
            #input("xpath", "//input[@id='delegateuser']", "Tao")
            #sleep(1)

            # 点击查询
            click("xpath", "//span[text()='查询']")

            # 废除委托关系
            # 勾选
            click("xpath", "//div[contains(@title,'委托方式:全权委托')]/parent::*/preceding-sibling::*[3]/descendant::*[2]")
            # 点击废除委托关系按钮
            click("xpath", "//span[text()='废除委托关系']")
            # 退出所有iframe窗体
            switch_default()

            # 用隐式等待方法等页面出现新增成功的提示框
            implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
            print("废除委托关系，操作成功！")
            logging.info("废除委托关系，操作成功！")
            time.sleep(3)

            # 切入'工作委托'的iframe窗体
            switch_to("xpath", "//iframe[@id='delegate-tab-iframe']")

            for i in range(1,3):

                # 点击'停用委托关系'和‘启用委托关系’按钮
                # 点击查看
                # 用JS的方法点击放大镜
                js_click("xpath", "//span[@class='f-contrac-close']")
                sleep(1)

                # 输入‘委托方式’为‘流程委托’
                click("xpath", "//input[@id='combobox-input-delegatetype']")
                input("xpath", "//input[@id='combobox-input-delegatetype']", "流程委托")
                sleep(1)
                input_enter("xpath", "//input[@id='combobox-input-delegatetype']")
                sleep(1)

                # 输入‘代理人’为‘Tao’
                #input("xpath", "//input[@id='delegateuser']", "Tao")
                #sleep(1)

                # 点击查询
                click("xpath", "//span[text()='查询']")

                if i==1:
                    # 点击'停用委托关系'按钮
                    # 勾选
                    click("xpath", "//div[contains(@title,'委托方式:流程委托')]/parent::*/preceding-sibling::*[3]/descendant::*[2]")
                    click("xpath", "//span[text()='停用委托关系']")
                    # 退出所有iframe窗体
                    switch_default()

                    # 用隐式等待方法等页面出现新增成功的提示框
                    implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
                    print("停用委托关系，操作成功！")
                    logging.info("停用委托关系，操作成功！")
                    time.sleep(3)

                    # 切入'工作委托'的iframe窗体
                    switch_to("xpath", "//iframe[@id='delegate-tab-iframe']")

                else:

                    # 点击'启用委托关系'按钮
                    # 勾选
                    click("xpath", "//div[contains(@title,'委托方式:流程委托')]/parent::*/preceding-sibling::*[3]/descendant::*[2]")
                    click("xpath", "//span[text()='启用委托关系']")
                    # 退出所有iframe窗体
                    switch_default()

                    # 用隐式等待方法等页面出现新增成功的提示框
                    implici_wait("xpath", "//span[contains(text(),'操作成功！')]")
                    print("启用委托关系，操作成功！")
                    logging.info("启用委托关系，操作成功！")
                    time.sleep(3)

                    # 切入'工作委托'的iframe窗体
                    switch_to("xpath", "//iframe[@id='delegate-tab-iframe']")

            #点击'委托流程设置'
            # 点击查看
            # 用JS的方法点击放大镜
            js_click("xpath", "//span[@class='f-contrac-close']")
            sleep(1)

            # 输入‘委托方式’为‘流程委托’
            click("xpath", "//input[@id='combobox-input-delegatetype']")
            input("xpath", "//input[@id='combobox-input-delegatetype']", "流程委托")
            sleep(1)
            input_enter("xpath", "//input[@id='combobox-input-delegatetype']")
            sleep(1)

            # 点击'委托流程设置'按钮
            # 勾选
            click("xpath", "//div[contains(@title,'委托方式:流程委托')]/parent::*/preceding-sibling::*[3]/descendant::*[2]")
            click("xpath", "//span[text()='委托流程设置']")

            #进入选择'工作委托流程'页面
            #切入'工作委托流程'的iframe窗体
            switch_to("xpath", "//iframe[@id='setUpDelegateWin-iframe']")

            # 点击查看
            # 用JS的方法点击放大镜
            js_click("xpath", "//span[@class='f-contrac-close']")
            sleep(1)

            #输入流程名称
            input("xpath", "//input[@id='processname']","支付备案调整申请")
            sleep(1)

            # 点击查询
            click("xpath", "//span[text()='查询']")

            #勾选
            click("xpath", "//div[contains(@title,'流程名称:支付备案调整申请')]/parent::*/preceding-sibling::*[2]/descendant::*[2]")

            #点击确定
            click("xpath", "//span[text()='确定']")

            # 退出所有iframe窗体
            switch_default()

            # 用隐式等待方法等页面出现新增成功的提示框
            implici_wait("xpath", "//span[contains(text(),'操作成功')]")
            print("委托流程设置，操作成功！")
            logging.info("委托流程设置，操作成功！")
            time.sleep(3)

            # 切入'工作委托'的iframe窗体
            switch_to("xpath", "//iframe[@id='delegate-tab-iframe']")

            #关闭当前页面
            click("xpath", "//div[@class='f-win-tool f-win-close']")
            
            #点击'查看委托流程'按钮
            click("xpath", "//span[text()='查看委托流程']")

            # 切入'查看委托流程'的iframe窗体
            switch_to("xpath", "//iframe[@id='viewDelegateInfoWin-iframe']")

            # 用隐式等待方法等页面出现'支付备案调整申请'字段
            implici_wait("xpath", "//div[contains(text(),'支付备案调整申请')]")
            time.sleep(1)

            #删除工作流
            # 勾选
            click("xpath","//div[contains(@title,'流程名称:支付备案调整申请')]/parent::*/preceding-sibling::*[1]/descendant::*[2]")
            # 点击删除按钮
            click("xpath", "//span[text()='删除']")

            # 点击弹出框的OK键
            click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

            # 退出所有iframe窗体
            switch_default()

            # 用隐式等待方法等页面出现删除的提示框
            implici_wait("xpath", "//span[contains(text(),'操作成功')]")
            print("工作流，删除成功！")
            logging.info("工作流，删除成功！")
            time.sleep(3)

            # 切入'工作委托'的iframe窗体
            switch_to("xpath", "//iframe[@id='delegate-tab-iframe']")

            # 关闭当前页面
            #click("xpath", "//div[@class='f-win-tool f-win-close']")
            getElements(self.driver, "xpath", "//div[@class='f-win-tool f-win-close']")[1].click()

            #对当前工作委托进行'废除'
            # 点击废除委托关系按钮
            click("xpath", "//span[text()='废除委托关系']")

            # 退出所有iframe窗体
            switch_default()

            # 用隐式等待方法等页面出现新增成功的提示框
            implici_wait("xpath", "//span[contains(text(),'操作成功')]")
            print("废除委托关系，操作成功！")
            logging.info("废除委托关系，操作成功！")
            time.sleep(3)

            # 退出所有iframe窗体
            switch_default()

            # 用JS的方法关闭当前页面
            js_click("xpath", "//a[@title='工作委托']/child::*[1]")

            # 打印操作成功日志
            print("工作委托，操作成功!")
            logging.info("工作委托，操作成功!")
            time.sleep(2)
        except Exception as err:
            # 发生其他异常时，打印异常堆栈信息
            print(traceback.print_exc())
            logging.debug("工作委托失败！" + str(traceback.format_exc()))
            # Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
            dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
            dir_path = make_current_hour_dir(dir_path + "\\")
            pic_path = os.path.join(dir_path, get_current_time() + ".png")
            capture(pic_path)
        


        # 测试：税种
        try:
            logging.info("退出所有iframe窗体")
            switch_default()

            logging.info("切入系统设置的iframe窗体")
            switch_to("xpath", "//iframe[@id='systemconfig-tab-iframe']")
            logging.info("开始测试'税种'功能")

            logging.info("用JS的方法点击基础资料下的'税种'")
            js_click("xpath", "//a[@nname='税种']")

            logging.info("退出所有iframe窗体")
            switch_default()

            logging.info("切入'税种'的iframe窗体")
            switch_to("xpath", "//iframe[@id='taxManager-tab-iframe']")

            logging.info("用JS的方法点击新增按钮")
            js_click("xpath", "//span[text()='新增']")

            logging.info("切入新增的iframe窗体")
            switch_to("xpath", "//iframe[@id='addWin-iframe']")

            logging.info("输入税种编码")
            input("xpath", "//input[@name='code']", "Test001")
            sleep(1)

            logging.info("输入税种名称")
            input("xpath", "//input[@name='name']", "Test税种")
            sleep(1)

            logging.info("先清空'税率%'框，再输入：10")
            clear("xpath", "//input[@id='rate-input']")
            sleep(1)
            input("xpath", "//input[@id='rate-input']", "10")
            sleep(1)

            logging.info("在新增页面的'总账科目'框里选择'一个科目'，模拟往下键")
            click("xpath", "//input[@id='combobox-input-glaccountid']")
            sleep(1)
            input_down("xpath", "//input[@id='combobox-input-glaccountid']")
            input_enter("xpath", "//input[@id='combobox-input-glaccountid']")
            sleep(1)

            logging.info("点击保存按钮")
            click("xpath", "//span[text()='保存']")

            logging.info("退出所有iframe窗体")
            switch_default()

            logging.info("用隐式等待方法等页面出现'保存成功'的提示框")
            implici_wait("xpath", "//span[contains(text(),'操作成功')]")
            print("税种，保存成功！")
            logging.info("税种，保存成功！")
            time.sleep(3)

            logging.info("切入'税种'的iframe窗体")
            switch_to("xpath", "//iframe[@id='taxManager-tab-iframe']")

            logging.info("点击查看,用JS的方法点击放大镜")
            js_click("xpath", "//span[@class='f-contrac-close']")
            sleep(1)

            logging.info("输入代码：Test001")
            input("xpath", "//input[@id='code']", "Test001")
            sleep(1)

            logging.info("点击查询")
            click("xpath", "//span[text()='查询']")
            sleep(2)

            logging.info("修改功能:勾选一个查询出的数据")
            click("xpath", "//div[@title='税种编码:Test001']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
            sleep(1)

            logging.info("点击修改按钮")
            click("xpath", "//span[text()='修改']")
            sleep(1)

            logging.info("切入修改的iframe窗体")
            switch_to("xpath", "//iframe[@id='modWin-iframe']")

            logging.info("修改税种名称")
            input("xpath", "//input[@id='name']", "自动化测试修改")
            sleep(2)

            logging.info("点击保存按钮")
            click("xpath", "//span[text()='保存']")

            logging.info("退出所有iframe窗体")
            switch_default()

            logging.info("用隐式等待方法等页面出现'操作成功'的提示框")
            implici_wait("xpath", "//span[contains(text(),'操作成功')]")
            print("税种，修改成功！")
            logging.info("税种，修改成功！")
            time.sleep(3)

            logging.info("切入'税种'的iframe窗体")
            switch_to("xpath", "//iframe[@id='taxManager-tab-iframe']")

            logging.info("测试'失效按钮' ")
            logging.info("勾选")
            click("xpath", "//div[@title='税种编码:Test001']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
            sleep(1)

            logging.info("点击失效按钮")
            click("xpath", "//span[text()='失效']")
            sleep(1)

            logging.info("退出所有iframe窗体")
            switch_default()

            logging.info("用隐式等待方法等页面出现'代码为Test001的失效成功！'的提示框")
            implici_wait("xpath", "//span[contains(text(),'失效成功')]")
            print("税种，点击失效成功！")
            logging.info("税种，点击失效成功！")
            time.sleep(3)

            logging.info("切入'税种'的iframe窗体")
            switch_to("xpath", "//iframe[@id='taxManager-tab-iframe']")

            logging.info("测试'生效按钮' ")
            logging.info("勾选")
            click("xpath", "//div[@title='税种编码:Test001']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
            sleep(1)

            logging.info("点击生效按钮")
            click("xpath", "//span[text()='生效']")
            sleep(1)

            logging.info("退出所有iframe窗体")
            switch_default()

            logging.info("用隐式等待方法等页面出现'代码为Test001的生效成功！'的提示框")
            implici_wait("xpath", "//span[contains(text(),'生效成功')]")
            print("税种，点击生效成功！")
            logging.info("税种，点击生效成功！")
            time.sleep(3)

            logging.info("切入'税种'的iframe窗体")
            switch_to("xpath", "//iframe[@id='taxManager-tab-iframe']")

            logging.info("测试'删除按钮' ")
            logging.info("勾选")
            click("xpath", "//div[@title='税种编码:Test001']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
            sleep(1)

            logging.info("点击'删除按钮' ")
            click("xpath", "//span[text()='删除']")

            logging.info("点击弹出框的OK键")
            click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

            logging.info("退出所有iframe窗体")
            switch_default()

            logging.info("用隐式等待方法等页面出现'操作成功'的提示框")
            implici_wait("xpath", "//span[contains(text(),'操作成功')]")
            print("税种，删除成功！")
            logging.info("税种，删除成功！")
            time.sleep(3)

            logging.info("用JS的方法关闭自定义字段的页面")
            js_click("xpath", "//a[@title='税种']/child::*[1]")

            print("'税种',操作成功!")
            logging.info("'税种',操作成功!")
            sleep(2)
        except Exception as err:
            # 发生其他异常时，打印异常堆栈信息
            print(traceback.print_exc())
            logging.debug("'税种',操作失败！" + str(traceback.format_exc()))
            # Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
            dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
            dir_path = make_current_hour_dir(dir_path + "\\")
            pic_path = os.path.join(dir_path, get_current_time() + ".png")
            capture(pic_path)
        


        # 测试：本位币维护
        try:
            logging.info("退出所有iframe窗体")
            switch_default()

            logging.info("切入系统设置的iframe窗体")
            switch_to("xpath", "//iframe[@id='systemconfig-tab-iframe']")
            logging.info("开始测试'本位币维护'功能")

            logging.info("用JS的方法点击基础资料下的'本位币维护'")
            js_click("xpath", "//a[@nname='本位币维护']")

            logging.info("退出所有iframe窗体")
            switch_default()

            logging.info("切入'本位币维护'的iframe窗体")
            switch_to("xpath", "//iframe[@id='standardcurrency-tab-iframe']")

            logging.info("用JS的方法点击新增按钮")
            js_click("xpath", "//span[text()='新增']")

            logging.info("切入新增的iframe窗体")
            switch_to("xpath", "//iframe[@id='addWin-iframe']")

            logging.info("在新增页面的'组织代码-组织机构'框里选择'一个组织'，模拟往下键")
            click("xpath", "//input[@id='combobox-input-orgid']")
            sleep(1)
            input_down("xpath","//input[@id='combobox-input-orgid']")
            input_enter("xpath","//input[@id='combobox-input-orgid']")
            sleep(1)

            logging.info("选择本币位币种为'CAD-加元' ")
            click("xpath", "//input[@id='combobox-input-currencyid']")
            sleep(1)
            input("xpath", "//input[@id='combobox-input-currencyid']", "CAD-加元")
            sleep(1)
            input_down("xpath", "//input[@id='combobox-input-currencyid']")
            input_enter("xpath", "//input[@id='combobox-input-currencyid']")
            sleep(1)

            logging.info("点击保存按钮")
            click("xpath", "//span[text()='保存']")

            logging.info("退出所有iframe窗体")
            switch_default()

            logging.info("用隐式等待方法等页面出现'操作成功'的提示框")
            implici_wait("xpath", "//span[contains(text(),'操作成功')]")
            print("本位币维护，保存成功！")
            logging.info("本位币维护，保存成功！")
            time.sleep(3)

            logging.info("切入'本位币维护'的iframe窗体")
            switch_to("xpath", "//iframe[@id='standardcurrency-tab-iframe']")

            logging.info("点击查看,用JS的方法点击放大镜")
            js_click("xpath", "//span[@class='f-contrac-close']")
            sleep(1)

            logging.info("输入本位币币种：CAD-加元")
            click("xpath", "//input[@id='combobox-input-currencyid']")
            sleep(1)
            input("xpath", "//input[@id='combobox-input-currencyid']", "CAD-加元")
            sleep(1)

            logging.info("勾选本位币币种为'CAD-加元'的选项")
            click("xpath", "//div[@title='代码-名称:CAD-加元']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
            sleep(1)

            logging.info("点击查询")
            click("xpath", "//span[text()='查询']")
            sleep(2)

            logging.info("修改功能:勾选一个查询出的数据")
            click("xpath", "//div[@title='本位币币种:CAD-加元']/parent::*/preceding-sibling::*[2]/descendant::*[2]")
            sleep(1)

            logging.info("点击修改按钮")
            click("xpath", "//span[text()='修改']")
            sleep(1)

            logging.info("清空'本位币币种'内容")
            clear("xpath", "//input[@id='combobox-input-currency']")
            sleep(1)

            logging.info("输入'CAD-加元',并且选中")
            input("xpath", "//input[@id='combobox-input-currency']", "CAD-加元")
            sleep(1)
            input_down("xpath", "//input[@id='combobox-input-currency']")
            input_enter("xpath", "//input[@id='combobox-input-currency']")
            sleep(1)

            logging.info("点击保存按钮")
            click("xpath", "//span[text()='保存']")

            logging.info("退出所有iframe窗体")
            switch_default()

            logging.info("用隐式等待方法等页面出现'操作成功'的提示框")
            implici_wait("xpath", "//span[contains(text(),'操作成功')]")
            print("本位币维护，修改成功！")
            logging.info("本位币维护，修改成功！")
            time.sleep(3)

            logging.info("切入'本位币维护'的iframe窗体")
            switch_to("xpath", "//iframe[@id='standardcurrency-tab-iframe']")

            logging.info("测试'删除按钮' ")
            logging.info("勾选")
            click("xpath", "//div[@title='本位币币种:CAD-加元']/parent::*/preceding-sibling::*[2]/descendant::*[2]")
            sleep(1)

            logging.info("点击'删除按钮' ")
            click("xpath", "//span[text()='删除']")

            logging.info("点击弹出框的OK键")
            click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

            logging.info("退出所有iframe窗体")
            switch_default()

            logging.info("用隐式等待方法等页面出现'操作成功'的提示框")
            implici_wait("xpath", "//span[contains(text(),'操作成功')]")
            print("本位币维护，删除成功！")
            logging.info("本位币维护，删除成功！")
            time.sleep(3)

            logging.info("用JS的方法关闭自定义字段的页面")
            js_click("xpath", "//a[@title='本位币维护']/child::*[1]")

            print("'本位币维护',操作成功!")
            logging.info("'本位币维护',操作成功!")
            sleep(2)
        except Exception as err:
            # 发生其他异常时，打印异常堆栈信息
            print(traceback.print_exc())
            logging.debug("'本位币维护',操作失败！" + str(traceback.format_exc()))
            # Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
            dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
            dir_path = make_current_hour_dir(dir_path + "\\")
            pic_path = os.path.join(dir_path, get_current_time() + ".png")
            capture(pic_path)


            

        #         # 退出所有iframe窗体
    #     self.driver.switch_to.default_content()
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