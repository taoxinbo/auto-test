# encoding=utf-8
# 2021-06-30
# TaoXB
# 此文件是自动化测试：综合查询系统--报表数据填报--公司基本情况：新增、修改、删除、生效、失效
import os
import sys
# 当前文件所在目录都添加到sys.path中，系统可以找到需要引用的模块
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Action.keyword_action import *
# 从文件所在目录中导入Log.py文件中所有内容
from Action.Log import *
from Config.VarConfig import *
from selenium.common.exceptions import WebDriverException
import traceback,pytest
import time
from datetime import datetime, date, timedelta
from Action.dir_opration import make_current_date_dir, make_current_hour_dir
from Action.send_mail import *

# print("开始时间：",time.strftime("%Y-%m-%d %H:%M:%S"))

driver = ""

@pytest.mark.mysql
@pytest.mark.flaky(reruns=pytest_flaky,reruns_delay=10)
class Test_Baobiaoshujutianbao_GSJBQK_Num(unittest.TestCase):

    # 启动浏览器
    def setUp(self):
        logging.info("启动Chrome浏览器")
        get("chrome")

    # 登陆系统、对综合查询系统--报表数据填报--公司基本情况，进行操作
    def test_trade(self):

        # 用来统计 每个关键节点 跑失败的个数，定义格式：文件名+‘_Num’
        Test_Baobiaoshujutianbao_GSJBQK_Num = 0

        try:
            logging.info("登陆系统")
            login(G_Mys_Url, mindy, Password, "亚唐科技")
            #login(G_Ora_Url, mindy, Password, "亚唐科技")

            # login( G_Ora_Url,TestUser,Password, "自动化测试租户")
            # login( G_Ora_Url,Tao, Password,"默认租户")
            # login( G_Mys_Url,TestUser,Password, "自动化测试租户")
            # login(G_Mys_Url, Felix, Password, "默认租户")
            #login(G_Mys_Url, mindy, Password, "亚唐科技")
            #login(G_Mys_Url_Bd, Felix, Password, "默认租户")
            # login(G_Ora_Url, 'judy', Password, "默认租户")
            # login(G_Mys_Url, 'Felix', Password, "默认租户")

            logging.info("用JS方法滚动至 综合查询系统  菜单")
            js_gd("xpath", "//span[contains(text(),'综合查询系统')]")
            logging.info("点击 综合查询系统 菜单")
            click("xpath", "//span[contains(text(),'综合查询系统')]")
            logging.info("点击 综合查询系统--报表数据填报 菜单")
            click("xpath", "//span[contains(text(),'报表数据填报')]")
            logging.info("点击 综合查询系统--报表数据填报--公司基本情况")
            click("xpath", "//span[contains(text(),'公司基本情况')]")

            logging.info("开始测试：综合查询系统--报表数据填报--公司基本情况")

            logging.info("退出所有iframe窗体")
            switch_default()

            logging.info("测试新增功能")
            logging.info("切入 公司基本情况 的iframe窗体")
            switch_to("xpath", "//iframe[@id='secondarycominfo_sctt-tab-iframe']")
            logging.info("用JS的方法点击新增按钮")
            js_click("xpath", "//span[text()='新增']")

            logging.info("切入新增的iframe窗体")
            switch_to("xpath", "//iframe[@id='addWin-iframe']")

            logging.info("选择一个'组织类型' ")
            click("xpath", "//input[@id='combobox-input-orgtype']")
            sleep(1)
            input_down("xpath", "//input[@id='combobox-input-orgtype']")
            input_enter("xpath", "//input[@id='combobox-input-orgtype']")
            sleep(1)

            logging.info("选择'21002-亚唐科技'的'组织' ")
            click("xpath", "//input[@id='combobox-input-orgid']")
            sleep(1)
            input("xpath", "//input[@id='combobox-input-orgid']", "21002-亚唐科技")
            sleep(1)
            input_down("xpath", "//input[@id='combobox-input-orgid']")
            input_enter("xpath", "//input[@id='combobox-input-orgid']")
            sleep(1)

            logging.info("测试输入'注册资本'，先清空，再输入：5000000000")
            clear("xpath", "//input[@id='registeredcapital-input']")
            sleep(1)
            input("xpath", "//input[@id='registeredcapital-input']", "5000000000")
            sleep(1)

            logging.info("测试输入'持股比例(%)'，先清空，再输入：20")
            clear("xpath", "//input[@id='insto-input']")
            sleep(1)
            input("xpath", "//input[@id='insto-input']", "20")
            sleep(1)

            logging.info("在'业务范围'中输入'自动化测试'")
            input("xpath", "//textarea[@id='businessscope']", "自动化测试")
            sleep(1)

            logging.info("在'核算方法'中输入'普通核算'")
            input("xpath", "//textarea[@id='accountingmethod']", "普通核算")
            sleep(1)

            logging.info("在'公司简介'中输入'自动化测试公司介绍'")
            input("xpath", "//textarea[@id='companyprofile']", "自动化测试公司介绍")
            sleep(1)

            logging.info("新增一行,点击'新增行'按钮")
            click("xpath", "//span[text()='新增行']")
            sleep(1)

            logging.info("选择一个'季度' ")
            click("xpath", "//input[@id='combobox-input-editgrid-quarter-0']")
            sleep(1)
            input_down("xpath", "//input[@id='combobox-input-editgrid-quarter-0']")
            sleep(1)
            input_down("xpath", "//input[@id='combobox-input-editgrid-quarter-0']")
            input_enter("xpath", "//input[@id='combobox-input-editgrid-quarter-0']")
            sleep(1)

            logging.info("测试输入'总资产'，先清空，再输入：5000000000")
            clear("xpath", "//input[@id='editgrid-totalasset-0-input']")
            sleep(1)
            input("xpath", "//input[@id='editgrid-totalasset-0-input']", "5000000000")
            sleep(1)

            logging.info("测试输入'净资产'，先清空，再输入：1000000000")
            clear("xpath", "//input[@id='editgrid-netasset-0-input']")
            sleep(1)
            input("xpath", "//input[@id='editgrid-netasset-0-input']", "1000000000")
            sleep(1)

            logging.info("测试输入'收入'，先清空，再输入：500000000")
            clear("xpath", "//input[@id='editgrid-revenue-0-input']")
            sleep(1)
            input("xpath", "//input[@id='editgrid-revenue-0-input']", "500000000")
            sleep(1)

            logging.info("测试输入'净利润'，先清空，再输入：100000000")
            clear("xpath", "//input[@id='editgrid-netrevenue-0-input']")
            sleep(1)
            input("xpath", "//input[@id='editgrid-netrevenue-0-input']", "100000000")
            sleep(1)

            logging.info("在'亏损原因'中输入'超过预估风险多'")
            input("xpath", "//input[@id='editgrid-deficitreason-0']", "超过预估风险多")
            sleep(1)

            logging.info("点击保存按钮")
            click("xpath", "//span[text()='保存']")

            logging.info("退出所有iframe窗体")
            switch_default()

            logging.info("用隐式等待方法等页面出现'保存成功'的提示框")
            implici_wait("xpath", "//span[contains(text(),'操作成功')]")
            print("公司基本情况，保存成功！")
            logging.info("公司基本情况，保存成功！")
            time.sleep(3)

            logging.info("测试修改功能")
            try:
                logging.info("切入 公司基本情况 的iframe窗体")
                switch_to("xpath", "//iframe[@id='secondarycominfo_sctt-tab-iframe']")

                logging.info("测试查询功能")
                logging.info("用JS的方法点击放大镜")
                js_click("xpath", "//span[@class='f-contrac-close']")
                sleep(1)

                logging.info("点击查询")
                js_click("xpath", "//span[text()='查询']")
                sleep(2)

                logging.info("勾选数据")
                click("xpath", "//div[@title='组织:21002-亚唐科技']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
                sleep(1)

                logging.info("点击修改按钮")
                click("xpath", "//span[text()='修改']")
                sleep(1)

                logging.info("切入修改的iframe窗体")
                switch_to("xpath", "//iframe[@id='modWin-iframe']")

                logging.info("修改'公司简介'，再输入：，自动化测试。")
                input("xpath", "//textarea[@id='companyprofile']", "，自动化测试。")
                sleep(1)

                logging.info("点击保存按钮")
                click("xpath", "//span[text()='保存']")

                logging.info("退出所有iframe窗体")
                switch_default()

                logging.info("用隐式等待方法等页面出现'修改成功'的提示框")
                implici_wait("xpath", "//span[contains(text(),'操作成功')]")
                print("公司基本情况，修改成功！")
                logging.info("公司基本情况，修改成功！")
                sleep(3)
            except Exception as err:
                # 发生其他异常时，打印异常堆栈信息
                Test_Baobiaoshujutianbao_GSJBQK_Num += 1
                print(traceback.print_exc())
                logging.debug("公司基本情况，修改失败！" + str(traceback.format_exc()))
                # Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
                dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
                dir_path = make_current_hour_dir(dir_path + "\\")
                pic_path = os.path.join(dir_path, get_current_time() + ".png")
                capture(pic_path)
                raise err

            logging.info("测试生效功能")
            try:
                logging.info("切入 公司基本情况 的iframe窗体")
                switch_to("xpath", "//iframe[@id='secondarycominfo_sctt-tab-iframe']")

                logging.info("勾选数据")
                click("xpath", "//div[@title='组织:21002-亚唐科技']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
                sleep(1)

                logging.info("点击生效按钮")
                click("xpath", "//span[text()='生效']")
                sleep(1)

                logging.info("点击弹出框的OK键")
                click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

                logging.info("退出所有iframe窗体")
                switch_default()

                logging.info("用隐式等待方法等页面出现'生效1条'提示框")
                implici_wait("xpath", "//span[contains(text(),'共处理1条')]")
                print("公司基本情况，点击生效成功！")
                logging.info("公司基本情况，点击生效成功！")
                time.sleep(3)
            except Exception as err:
                # 发生其他异常时，打印异常堆栈信息
                Test_Baobiaoshujutianbao_GSJBQK_Num += 1
                print(traceback.print_exc())
                logging.debug("公司基本情况，点击生效失败！" + str(traceback.format_exc()))
                # Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
                dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
                dir_path = make_current_hour_dir(dir_path + "\\")
                pic_path = os.path.join(dir_path, get_current_time() + ".png")
                capture(pic_path)
                raise err

            logging.info("测试失效功能")
            try:
                logging.info("切入 公司基本情况 的iframe窗体")
                switch_to("xpath", "//iframe[@id='secondarycominfo_sctt-tab-iframe']")

                logging.info("勾选数据")
                click("xpath", "//div[@title='组织:21002-亚唐科技']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
                sleep(1)

                logging.info("点击失效按钮")
                click("xpath", "//span[text()='失效']")
                sleep(1)

                logging.info("点击弹出框的OK键")
                click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

                logging.info("退出所有iframe窗体")
                switch_default()

                logging.info("用隐式等待方法等页面出现'失效1条'提示框")
                implici_wait("xpath", "//span[contains(text(),'共处理1条')]")
                print("公司基本情况，点击失效成功！")
                logging.info("公司基本情况，点击失效成功！")
                time.sleep(3)
            except Exception as err:
                # 发生其他异常时，打印异常堆栈信息
                Test_Baobiaoshujutianbao_GSJBQK_Num += 1
                print(traceback.print_exc())
                logging.debug("公司基本情况，点击失效失败！" + str(traceback.format_exc()))
                # Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
                dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
                dir_path = make_current_hour_dir(dir_path + "\\")
                pic_path = os.path.join(dir_path, get_current_time() + ".png")
                capture(pic_path)
                raise err

            logging.info("测试删除功能")
            try:
                logging.info("切入 公司基本情况 的iframe窗体")
                switch_to("xpath", "//iframe[@id='secondarycominfo_sctt-tab-iframe']")

                logging.info("勾选数据")
                click("xpath", "//div[@title='组织:21002-亚唐科技']/parent::*/preceding-sibling::*[1]/descendant::*[2]")
                sleep(1)

                logging.info("点击删除按钮")
                click("xpath", "//span[text()='删除']")
                sleep(4)

                logging.info("点击弹出框的OK键")
                click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

                logging.info("退出所有iframe窗体")
                switch_default()

                logging.info("用隐式等待方法等页面出现'成功删除！'的提示框")
                implici_wait("xpath", "//span[contains(text(),'成功删除')]")
                print("公司基本情况，成功删除！")
                logging.info("公司基本情况，成功删除！")
                sleep(2)
            except Exception as err:
                # 发生其他异常时，打印异常堆栈信息
                Test_Baobiaoshujutianbao_GSJBQK_Num += 1
                print(traceback.print_exc())
                logging.debug("公司基本情况，删除失败！" + str(traceback.format_exc()))
                # Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
                dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
                dir_path = make_current_hour_dir(dir_path + "\\")
                pic_path = os.path.join(dir_path, get_current_time() + ".png")
                capture(pic_path)
                raise err


        except Exception as err:
            # 发生其他异常时，打印异常堆栈信息
            Test_Baobiaoshujutianbao_GSJBQK_Num += 1
            print(traceback.print_exc())
            logging.debug("公司基本情况，保存失败！" + str(traceback.format_exc()))
            # Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
            dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
            dir_path = make_current_hour_dir(dir_path + "\\")
            pic_path = os.path.join(dir_path, get_current_time() + ".png")
            capture(pic_path)
            raise err

        print('Test_Baobiaoshujutianbao_GSJBQK_Num 的值:',Test_Baobiaoshujutianbao_GSJBQK_Num)
        if Test_Baobiaoshujutianbao_GSJBQK_Num ==0:
            print("'公司基本情况'，操作成功!")
            logging.info("'公司基本情况'，操作成功!")

            logging.info("用JS的方法关闭当前页面")
            js_click("xpath", "//a[@title='公司基本情况']/child::*[1]")
            sleep(2)

            # logging.info("退出所有iframe窗体")
            # switch_default()
            #
            # logging.info("点击页面'退出'按钮")
            # click("xpath", "//a[contains(.,'退出')]")
            # time.sleep(1)
            #
            # logging.info("点击退出弹窗的'Yes'按钮")
            # click("xpath", "//button[contains(.,'Yes')]")
            # time.sleep(2)

        else:
            print("'公司基本情况'，有关键节点功能测试失败!")
            logging.info("'公司基本情况'，有关键节点功能测试失败!")

    # def tearDown(self):
    #     logging.info("关闭浏览器")
    #     quit()

        print("结束时间：", time.strftime("%Y-%m-%d %H:%M:%S"))
        logging.info("结束时间：%s" % (time.strftime("%Y-%m-%d %H:%M:%S")))


if __name__ == '__main__':
    #  启动单元测试
    unittest.main(verbosity=2)