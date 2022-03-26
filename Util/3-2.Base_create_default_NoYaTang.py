#encoding=utf-8
# 2020-09-04
# TaoXB
# 此文件是自动化测试‘默认租户’下：测试系统管理、测试新增用户、测试权限、 新用户（登陆/退出）、新用户（修改登陆密码/修改支付密码/重置支付密码）
# 把组织 "001000-亚唐科技"，注释掉。

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

# print("开始时间：",time.strftime("%Y-%m-%d %H:%M:%S"))

driver = ""
class Base_create_default(unittest.TestCase):

    # 启动浏览器
    def setUp(self):

        # 启动浏览器的另外一个方法：通过封装启动浏览器的驱动，启动不同浏览器
        self.driver = get("chrome")

    # 登陆系统、对系统设置进行操作
    def test_trade(self):

        logging.info("新建‘默认租户’的‘组织、用户、权限’的功能")

        for url in Url_L:

            logging.info("新建‘默认租户’的‘组织’")
            # 通过登陆封装函数，以‘SysAdmin’登陆租户‘自动化测试租户’，创建‘组织’
            login(url, "SysAdmin", "fingard@1", "默认租户")

            # 点击系统菜单
            self.driver.find_element_by_xpath("//span[contains(text(),'系统菜单')]").click()
            time.sleep(1)
            # 点击用户管理菜单
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
                self.driver.switch_to.frame(
                    self.driver.find_element_by_xpath("//iframe[@id ='bizOrgTypeSet-tab-iframe']"))

                # 如果i等于1，就删除新建的协议设置
                if i == 1:

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

                    #缩回放大镜
                    self.driver.find_element_by_xpath("//span[@class='']").click()
                    time.sleep(2)



            # 点击查看
            # 用JS的方法点击放大镜
            button = self.driver.find_element_by_xpath("//span[@class='f-contrac-close']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 输入‘组织类别设置’代码
            self.temp = self.driver.find_element_by_xpath("//input[@id='code']")
            self.temp.click()
            time.sleep(1)
            self.temp.clear()
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
                self.temp = self.driver.find_element_by_xpath("//textarea[@id='description']")
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

                    #缩回放大镜
                    self.driver.find_element_by_xpath("//span[@class='']").click()
                    time.sleep(2)


            # 点击查看
            # 用JS的方法点击放大镜
            button = self.driver.find_element_by_xpath("//span[@class='f-contrac-close']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 输入‘组织分类设置’代码
            self.temp = self.driver.find_element_by_xpath("//input[@id='code']")
            self.temp.click()
            time.sleep(1)
            self.temp.clear()
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
                self.temp = self.driver.find_element_by_xpath("//textarea[@id='description']")
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
                self.driver.find_element_by_xpath("//input[@id='org_name']").send_keys("默认租户的组织机构设置")
                time.sleep(2)

                # 输入组织属性
                self.temp = self.driver.find_element_by_xpath("//input[@id='combobox-input-org_cate']")
                self.temp.click()
                self.temp.clear()
                time.sleep(1)
                self.temp.send_keys("上市公司")
                time.sleep(1)
                self.temp.send_keys(Keys.ARROW_DOWN)
                self.temp.send_keys(Keys.ENTER)
                time.sleep(1)

                # 输入组织级别
                self.temp = self.driver.find_element_by_xpath("//input[@id='combobox-input-org_level']")
                self.temp.click()
                self.temp.clear()
                time.sleep(1)
                self.temp.send_keys("集团")
                time.sleep(1)
                self.temp.send_keys(Keys.ARROW_DOWN)
                self.temp.send_keys(Keys.ENTER)
                time.sleep(1)

                # 输入上级组织
                self.temp = self.driver.find_element_by_xpath("//input[@id='combobox-input-parent_id']")
                self.temp.click()
                self.temp.clear()
                time.sleep(1)
                #self.temp.send_keys("001000-亚唐科技")
                #input_down("xpath", "//input[@id='combobox-input-parent_id']")
                #time.sleep(1)
                self.temp.send_keys(Keys.ARROW_DOWN)
                self.temp.send_keys(Keys.ENTER)
                time.sleep(1)

                # 输入主管组织
                self.temp = self.driver.find_element_by_xpath("//input[@id='combobox-input-manage_id']")
                self.temp.click()
                self.temp.clear()
                time.sleep(1)
                #self.temp.send_keys("001000-亚唐科技")
                #time.sleep(1)
                self.temp.send_keys(Keys.ARROW_DOWN)
                self.temp.send_keys(Keys.ENTER)
                time.sleep(1)

                # 输入组织简称
                self.driver.find_element_by_xpath("//input[@id='shortorgname']").send_keys("组织机构设置")
                time.sleep(2)

                # 输入组织类别
                self.temp = self.driver.find_element_by_xpath("//input[@id='combobox-input-ext_id']")
                self.temp.click()
                self.temp.clear()
                time.sleep(1)
                self.temp.send_keys(Keys.ARROW_DOWN)
                self.temp.send_keys(Keys.ENTER)
                time.sleep(1)

                # 输入统计组织
                self.temp = self.driver.find_element_by_xpath("//input[@id='combobox-input-statistical_id']")
                self.temp.click()
                self.temp.clear()
                time.sleep(1)
                #self.temp.send_keys("001000-亚唐科技")
                #time.sleep(1)
                self.temp.send_keys(Keys.ARROW_DOWN)
                self.temp.send_keys(Keys.ENTER)
                time.sleep(1)

                # 输入英文名称
                self.driver.find_element_by_xpath("//input[@id='english_name']").send_keys("OrgSet")
                time.sleep(2)

                # 输入组织分类
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

                    # 勾选
                    #self.driver.find_element_by_xpath("//div[@title='组织编码:TestOrgSet']/parent::*/preceding-sibling::*[1]/descendant::*[2]").click()
                    self.driver.find_element_by_xpath("//div[@title='组织编码:TestOrgSet']/parent::*/preceding-sibling::*[2]/descendant::*[2]").click()
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
            self.temp.clear()
            time.sleep(1)
            self.temp.send_keys("TestOrgSet")
            time.sleep(1)

            # 点击查询
            self.driver.find_element_by_xpath("//span[text()='查询']").click()
            time.sleep(3)

            # 测试修改‘组织机构设置’功能
            try:
                # 勾选
                #self.driver.find_element_by_xpath("//div[@title='组织编码:TestOrgSet']/parent::*/preceding-sibling::*[1]/descendant::*[2]").click()
                self.driver.find_element_by_xpath("//div[@title='组织编码:TestOrgSet']/parent::*/preceding-sibling::*[2]/descendant::*[2]").click()
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

            # 点击查看
            # 用JS的方法点击放大镜
            button = self.driver.find_element_by_xpath("//span[@class='f-contrac-close']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 输入‘组织分类设置’代码
            self.temp = self.driver.find_element_by_xpath("//input[@id='code']")
            self.temp.click()
            time.sleep(1)
            self.temp.clear()
            time.sleep(1)
            self.temp.send_keys("TestOrgSet")
            time.sleep(1)

            # 点击查询
            self.driver.find_element_by_xpath("//span[text()='查询']").click()
            time.sleep(3)

            # 测试注销‘组织机构设置’功能
            try:
                # 勾选
                #self.driver.find_element_by_xpath("//div[@title='组织编码:TestOrgSet']/parent::*/preceding-sibling::*[1]/descendant::*[2]").click()
                self.driver.find_element_by_xpath("//div[@title='组织编码:TestOrgSet']/parent::*/preceding-sibling::*[2]/descendant::*[2]").click()
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

            # 点击查看
            # 用JS的方法点击放大镜
            button = self.driver.find_element_by_xpath("//span[@class='f-contrac-close']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 输入‘组织分类设置’代码
            self.temp = self.driver.find_element_by_xpath("//input[@id='code']")
            self.temp.click()
            time.sleep(1)
            self.temp.clear()
            time.sleep(1)
            self.temp.send_keys("TestOrgSet")
            time.sleep(1)

            # 点击查询
            self.driver.find_element_by_xpath("//span[text()='查询']").click()
            time.sleep(3)

            # 测试激活‘组织机构设置’功能
            try:
                # 勾选
                #self.driver.find_element_by_xpath("//div[@title='组织编码:TestOrgSet']/parent::*/preceding-sibling::*[1]/descendant::*[2]").click()
                self.driver.find_element_by_xpath("//div[@title='组织编码:TestOrgSet']/parent::*/preceding-sibling::*[2]/descendant::*[2]").click()
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

            # 关闭浏览器
            self.driver.quit()
            time.sleep(2)
            
            # 启动浏览器
            self.driver = get("chrome")

            logging.info("新建‘默认租户’的‘用户’")
            # 通过登陆封装函数，以‘UserAdmin’登陆
            login(url, "UserAdmin", "fingard@1", "默认租户")

            # 点击系统菜单
            self.driver.find_element_by_xpath("//span[contains(text(),'系统菜单')]").click()
            time.sleep(1)
            # 点击用户管理菜单
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
            self.driver.find_element_by_xpath("//input[@id='userId']").send_keys("Tao")
            time.sleep(2)

            # 输入用户姓名
            self.driver.find_element_by_xpath("//input[@id='userName']").send_keys("默认租户的测试用户")
            time.sleep(2)

            # 输入所属组织
            self.temp = self.driver.find_element_by_xpath("//input[@id='combobox-input-orgId']")
            self.temp.click()
            self.temp.send_keys("TestOrgSet-默认租户的组织机构设置")
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
            print("新增‘用户’，成功！")
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
            self.temp.send_keys("Tao")
            time.sleep(1)

            # 点击查询
            self.driver.find_element_by_xpath("//span[text()='查询']").click()
            time.sleep(3)

            # 测试修改‘用户’功能
            try:
                # 勾选
                self.driver.find_element_by_xpath("//div[@title='用户编号:Tao']/parent::*/preceding-sibling::*[1]/descendant::*[2]").click()
                time.sleep(1)

                # 点击修改按钮
                self.driver.find_element_by_xpath("//span[text()='修改']").click()
                time.sleep(1)

                # 切入修改的iframe窗体
                self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='allocateAuthorUserPowerWin-iframe']"))

                # 修改排序
                self.temp = self.driver.find_element_by_xpath("//input[@id='userOrder-input']")
                self.temp.clear()
                self.temp.send_keys("123456")
                time.sleep(2)

                # 修改备注
                self.temp = self.driver.find_element_by_xpath("//textarea[@id='remark']")
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

            # 点击查看
            # 用JS的方法点击放大镜
            button = self.driver.find_element_by_xpath("//span[@class='f-contrac-close']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 输入用户编号
            self.temp = self.driver.find_element_by_xpath("//input[@id='userIdlrlike']")
            self.temp.click()
            time.sleep(1)
            self.temp.clear()
            time.sleep(1)
            self.temp.send_keys("Tao")
            time.sleep(1)

            # 点击查询
            self.driver.find_element_by_xpath("//span[text()='查询']").click()
            time.sleep(3)

            # 测试注销‘用户’功能
            try:
                # 勾选
                self.driver.find_element_by_xpath("//div[@title='用户编号:Tao']/parent::*/preceding-sibling::*[1]/descendant::*[2]").click()
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

            # 点击查看
            # 用JS的方法点击放大镜
            button = self.driver.find_element_by_xpath("//span[@class='f-contrac-close']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 输入用户编号
            self.temp = self.driver.find_element_by_xpath("//input[@id='userIdlrlike']")
            self.temp.click()
            time.sleep(1)
            self.temp.clear()
            time.sleep(1)
            self.temp.send_keys("Tao")
            time.sleep(1)

            # 点击查询
            self.driver.find_element_by_xpath("//span[text()='查询']").click()
            time.sleep(3)

            # 测试激活‘用户’功能
            try:
                # 勾选
                self.driver.find_element_by_xpath("//div[@title='用户编号:Tao']/parent::*/preceding-sibling::*[1]/descendant::*[2]").click()
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

            # 点击查看
            # 用JS的方法点击放大镜
            button = self.driver.find_element_by_xpath("//span[@class='f-contrac-close']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 输入用户编号
            self.temp = self.driver.find_element_by_xpath("//input[@id='userIdlrlike']")
            self.temp.click()
            time.sleep(1)
            self.temp.clear()
            time.sleep(1)
            self.temp.send_keys("Tao")
            time.sleep(1)

            # 点击查询
            self.driver.find_element_by_xpath("//span[text()='查询']").click()
            time.sleep(3)

            # 测试密码重置‘用户’功能
            try:
                # 勾选
                self.driver.find_element_by_xpath("//div[@title='用户编号:Tao']/parent::*/preceding-sibling::*[1]/descendant::*[2]").click()
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

            # 点击查看
            # 用JS的方法点击放大镜
            button = self.driver.find_element_by_xpath("//span[@class='f-contrac-close']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 输入用户编号
            self.temp = self.driver.find_element_by_xpath("//input[@id='userIdlrlike']")
            self.temp.click()
            time.sleep(1)
            self.temp.clear()
            time.sleep(1)
            self.temp.send_keys("Tao")
            time.sleep(1)

            # 点击查询
            self.driver.find_element_by_xpath("//span[text()='查询']").click()
            time.sleep(3)

            # 测试‘信息查看’功能
            try:
                # 勾选
                self.driver.find_element_by_xpath("//div[@title='用户编号:Tao']/parent::*/preceding-sibling::*[1]/descendant::*[2]").click()
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

                # 关闭信息查看页面
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

            # 关闭浏览器
            self.driver.quit()
            time.sleep(2)

            
            # 启动浏览器
            self.driver = get("chrome")

            logging.info("新建‘默认租户’的‘权限’")
            # 通过登陆封装函数，以‘AuthAdmin’登陆
            login(url, "AuthAdmin", "fingard@1", "默认租户")

            # 点击系统菜单
            self.driver.find_element_by_xpath("//span[contains(text(),'系统菜单')]").click()
            time.sleep(1)
            # 点击用户管理菜单
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
            self.temp.send_keys("Tao")
            time.sleep(1)

            # 点击查询
            self.driver.find_element_by_xpath("//span[text()='查询']").click()
            time.sleep(3)

            # 测试‘分配组织’
            logging.info("测试‘分配组织’")

            # 勾选
            self.driver.find_element_by_xpath("//div[@title='用户编号:Tao']/parent::*/preceding-sibling::*[1]/descendant::*[2]").click()
            time.sleep(1)

            # 点击按钮
            self.driver.find_element_by_xpath("//span[text()='分配组织']").click()
            time.sleep(1)

            # 切入‘分配组织’的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id ='allocateAuthorUserOrgWin-iframe']"))

            # 第一次点分配，然后取消，然后再点分配
            for i in range(1, 3):

                # 点击查看
                # 用JS的方法点击放大镜
                button = self.driver.find_element_by_xpath("//span[@class='f-contrac-close']")
                self.driver.execute_script("$(arguments[0]).click()", button)

                # 输入组织编码
                self.temp = self.driver.find_element_by_xpath("//input[@id='orgcode']")
                self.temp.click()
                time.sleep(1)
                self.temp.send_keys("001000")
                time.sleep(1)

                # 点击查询
                self.driver.find_element_by_xpath("//span[text()='查询']").click()
                time.sleep(3)

                # 勾选
                self.driver.find_element_by_xpath("//div[@title='组织编码:001000']/parent::*/preceding-sibling::*[2]/descendant::*[2]").click()
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

                if i == 1:

                    # 点击查看
                    # 用JS的方法点击放大镜
                    button = self.driver.find_element_by_xpath("//span[@class='f-contrac-close']")
                    self.driver.execute_script("$(arguments[0]).click()", button)

                    # 输入组织编码
                    self.temp = self.driver.find_element_by_xpath("//input[@id='orgcode']")
                    self.temp.click()
                    time.sleep(1)
                    self.temp.send_keys("001000")
                    time.sleep(1)

                    # 点击查询
                    self.driver.find_element_by_xpath("//span[text()='查询']").click()
                    time.sleep(3)

                    # 勾选
                    self.driver.find_element_by_xpath("//div[@title='组织编码:001000']/parent::*/preceding-sibling::*[2]/descendant::*[2]").click()
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
                # 点击信息查看
                self.driver.find_element_by_xpath("//span[text()='信息查看']").click()
                time.sleep(1)

                # 切入‘信息查看’iframe
                self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id ='viewUserInfoWin-iframe']"))

                # 点击‘关联组织信息’按钮
                self.driver.find_element_by_xpath("//span[text()='关联组织信息']").click()

                # 切入‘关联组织信息’iframe
                self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id ='subTabTwo-iframe']"))

                # 用隐式等待方法来处理
                self.driver.implicitly_wait(60)
                self.driver.find_element_by_xpath("//div[@title='组织编码:001000']")
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

                # 输入组织
                self.temp = self.driver.find_element_by_xpath("//input[@id='combobox-input-orgId']")
                self.temp.click()
                self.temp.clear()
                time.sleep(1)
                self.temp.send_keys("TestOrgSet-默认租户的组织机构设置")
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

            # 缩回放大镜
            self.driver.find_element_by_xpath("//span[@class='']").click()
            time.sleep(2)

            # 点击查看
            # 用JS的方法点击放大镜
            button = self.driver.find_element_by_xpath("//span[@class='f-contrac-close']")
            self.driver.execute_script("$(arguments[0]).click()", button)

            # 输入‘角色代码’
            self.temp = self.driver.find_element_by_xpath("//input[@id='role_code']")
            self.temp.click()
            time.sleep(1)
            self.temp.clear()
            time.sleep(1)
            self.temp.send_keys("TestRole")
            time.sleep(1)

            # 点击查询
            self.driver.find_element_by_xpath("//span[text()='查询']").click()
            time.sleep(3)


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
                # 20210629注释
                # self.driver.find_element_by_xpath("//span[@id='node4']").click()
                # 20210629修改：双击勾选
                double_click("xpath", "//span[@id='node4']")
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
            self.temp.send_keys("Tao")
            time.sleep(1)

            # 点击查询
            self.driver.find_element_by_xpath("//span[text()='查询']").click()
            time.sleep(3)

            # 勾选
            self.driver.find_element_by_xpath("//div[@title='组织名称:TestOrgSet-默认租户的组织机构设置']/parent::*/preceding-sibling::*[3]/descendant::*[2]").click()
            #self.driver.find_element_by_xpath("//div[@title='组织名称:默认租户的组织机构设置']/parent::*/preceding-sibling::*[3]/descendant::*[2]").click()
            time.sleep(2)

            # 点击‘分配角色’按钮
            self.driver.find_element_by_xpath("//span[text()='分配角色']").click()
            time.sleep(1)

            # 切入‘分配角色’的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='allocateUserOrgRoleWin-iframe']"))

            # 第一次点分配，然后取消，然后再点分配
            for i in range(1, 3):

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

            # 关闭浏览器
            self.driver.quit()
            time.sleep(2)
            
            # 启动浏览器
            self.driver = get("chrome")

            logging.info("测试新租户的新用户‘登陆’的功能")
            # 通过登陆封装函数，以‘Tao’登陆租户‘自动化测试租户’，进行初始化
            login(url, "Tao", "88888888", "默认租户")

            # 修改密码
            # 切入修改密码的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id ='modifyWin2-iframe']"))

            # 输入当前密码
            self.driver.find_element_by_xpath("//input[@id='oldPwd']").send_keys("88888888")
            time.sleep(2)

            # 输入新的密码
            self.driver.find_element_by_xpath("//input[@id='newPwd']").send_keys("fingard@2")
            time.sleep(2)

            # 输入确认输入
            self.driver.find_element_by_xpath("//input[@id='newPwdre']").send_keys("fingard@2")
            time.sleep(2)

            # 点击确定按钮
            self.driver.find_element_by_xpath("//span[text()='确定']").click()
            time.sleep(2)

            # 点击弹出框的OK键
            # self.driver.find_element_by_xpath("//button[@id='f-message-webgen-0-okBnt']").click()
            time.sleep(2)

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            for i in range(1,3):

                #点击修改密码按钮
                self.driver.find_element_by_xpath("//a[contains(.,'修改密码')]").click()
                time.sleep(2)

                # 点击修改登陆密码按钮
                self.driver.find_element_by_xpath("//a[contains(.,'修改登录密码')]").click()
                time.sleep(2)

                # 切入修改密码的iframe窗体
                self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id ='modifyWin-iframe']"))

                # 输入当前密码
                self.driver.find_element_by_xpath("//input[@id='oldPwd']").send_keys("fingard@2")
                time.sleep(2)

                # 输入新的密码
                self.driver.find_element_by_xpath("//input[@id='newPwd']").send_keys("fingard@1")
                time.sleep(2)

                # 输入确认输入
                self.driver.find_element_by_xpath("//input[@id='newPwdre']").send_keys("fingard@1")
                time.sleep(2)

                # 测试重置、取消按钮
                if i==1:

                    # 点击重置按钮
                    self.driver.find_element_by_xpath("//span[text()='重置']").click()
                    time.sleep(2)

                    # 点击取消按钮
                    self.driver.find_element_by_xpath("//span[text()='取消']").click()
                    time.sleep(2)

                    # 退出所有iframe窗体
                    self.driver.switch_to.default_content()

                #密码重置为：fingard@1
                elif i==2:

                    # 点击确定按钮
                    self.driver.find_element_by_xpath("//span[text()='确定']").click()
                    #time.sleep(2)

                    # 点击弹出框的OK键
                    # self.driver.find_element_by_xpath("//button[@id='f-message-webgen-0-okBnt']").click()
                    #time.sleep(2)

                    # 退出所有iframe窗体
                    self.driver.switch_to.default_content()

                    # 用隐式等待方法等页面出现提示框
                    self.driver.implicitly_wait(60)
                    self.driver.find_element_by_xpath("//span[contains(text(),'密码修改成功')]")
                    print('密码重置为：fingard@1' )
                    time.sleep(3)


            # 设置支付密码
            # 点击修改密码按钮
            self.driver.find_element_by_xpath("//a[contains(.,'修改密码')]").click()
            time.sleep(2)

            # 点击修改支付密码按钮
            self.driver.find_element_by_xpath("//a[contains(.,'修改支付密码')]").click()
            time.sleep(2)

            # 切入设置支付密码的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id ='modifyPayPasswordWin-iframe']"))

            # 输入支付密码
            self.driver.find_element_by_xpath("//input[@id='newPwd']").send_keys("fingard@2")
            time.sleep(2)

            # 输入确定输入
            self.driver.find_element_by_xpath("//input[@id='newPwdre']").send_keys("fingard@2")
            time.sleep(2)

            # 点击确定按钮
            self.driver.find_element_by_xpath("//span[text()='确定']").click()

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 用隐式等待方法等页面出现提示框
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath("//span[contains(text(),'当前用户支付密码修改成功！')]")
            print('支付密码设置成功！')
            time.sleep(3)

            #重置支付密码
            # 点击修改密码按钮
            self.driver.find_element_by_xpath("//a[contains(.,'修改密码')]").click()
            time.sleep(2)

            # 点击重置支付密码按钮
            self.driver.find_element_by_xpath("//a[contains(.,'重置支付密码')]").click()
            time.sleep(2)

            # 切入重置支付密码的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id ='resetPayPasswordWin-iframe']"))

            # 输入登录密码
            self.driver.find_element_by_xpath("//input[@id='loginPwd']").send_keys("fingard@1")
            time.sleep(2)

            # 点击确定按钮
            self.driver.find_element_by_xpath("//span[text()='确定']").click()

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 用隐式等待方法等页面出现提示框
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath("//span[contains(text(),'支付密码成功重置为88888888')]")
            print('重置支付密码成功！')
            time.sleep(6)

            # 重置支付密码
            # 点击修改密码按钮
            self.driver.find_element_by_xpath("//a[contains(.,'修改密码')]").click()
            time.sleep(2)

            # 点击修改支付密码按钮
            self.driver.find_element_by_xpath("//a[contains(.,'修改支付密码')]").click()
            time.sleep(2)

            # 切入设置支付密码的iframe窗体
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id ='modifyPayPasswordWin-iframe']"))

            # 输入当前支付密码
            self.driver.find_element_by_xpath("//input[@id='oldPwd']").send_keys("88888888")
            time.sleep(2)

            # 输入新的支付密码
            self.driver.find_element_by_xpath("//input[@id='newPwd']").send_keys("fingard@1")
            time.sleep(2)

            # 输入确定输入
            self.driver.find_element_by_xpath("//input[@id='newPwdre']").send_keys("fingard@1")
            time.sleep(2)

            # 点击确定按钮
            self.driver.find_element_by_xpath("//span[text()='确定']").click()

            # 退出所有iframe窗体
            self.driver.switch_to.default_content()

            # 用隐式等待方法等页面出现提示框
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath("//span[contains(text(),'当前用户支付密码修改成功')]")
            print('支付密码设置成功！')
            time.sleep(3)

            # 点击页面退出按钮
            self.driver.find_element_by_xpath("//a[contains(.,'退出')]").click()
            time.sleep(1)

            # 点击退出弹窗的'Yes'按钮
            self.driver.find_element_by_xpath("//button[contains(.,'Yes')]").click()
            time.sleep(2)
            logging.info("默认租户下的新用户‘退出’成功！")

        # def tearDown(self):
        #     self.driver.quit()
        print("结束时间：", time.strftime("%Y-%m-%d %H:%M:%S"))


if __name__ == '__main__':
    #  启动单元测试
    unittest.main(verbosity=2)