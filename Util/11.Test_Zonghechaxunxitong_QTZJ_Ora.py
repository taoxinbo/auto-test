# encoding=utf-8
# 2021-06-30
# TaoXB
# 此文件是自动化测试：综合查询系统--资金--其他资金：新增、修改、删除、生效、失效
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

@pytest.mark.oracle
@pytest.mark.flaky(reruns=pytest_flaky,reruns_delay=10)
class Test_Zonghechaxunxitong_QTZJ(unittest.TestCase):

    # 启动浏览器
    def setUp(self):
        logging.info("启动Chrome浏览器")
        get("chrome")

    # 登陆系统、对内部借款管理--基础设置--借款类型，进行操作
    def test_trade(self):

        # 用来统计 每个关键节点 跑失败的个数，定义格式：文件名+‘_Num’
        Test_Zonghechaxunxitong_QTZJ_Num = 0

        try:
            logging.info("登陆系统")
            #login(G_Mys_Url, mindy, Password, "亚唐科技")
            login(G_Ora_Url, mindy, Password, "亚唐科技")

            # login( G_Ora_Url,TestUser,Password, "自动化测试租户")

            # login( G_Ora_Url,Tao, Password,"默认租户")
            # login( G_Mys_Url,TestUser,Password, "自动化测试租户")
            # login(G_Mys_Url, Felix, Password, "默认租户")
            #login(G_Mys_Url_Bd, Felix, Password, "默认租户")
            # login(G_Ora_Url, 'judy', Password, "默认租户")
            # login(G_Mys_Url, 'Felix', Password, "默认租户")

            logging.info("用JS方法滚动至 综合查询系统  菜单")
            js_gd("xpath", "//span[contains(text(),'综合查询系统')]")
            logging.info("点击 综合查询系统 菜单")
            click("xpath", "//span[contains(text(),'综合查询系统')]")
            logging.info("点击 综合查询系统--资金 菜单")
            click("xpath", "//span[contains(text(),'报表数据填报')]/ancestor-or-self::*[4]/descendant-or-self::*[6]")
            logging.info("点击 综合查询系统--资金--其他资金")
            click("xpath", "//span[contains(text(),'其他资金')]")

            logging.info("开始测试：综合查询系统--资金--银行资金限额管理")

            logging.info("退出所有iframe窗体")
            switch_default()

            logging.info("测试新增功能")
            logging.info("切入 其他资金 的iframe窗体")
            switch_to("xpath", "//iframe[@id='availableFundBalance-tab-iframe']")
            logging.info("用JS的方法点击新增按钮")
            js_click("xpath", "//span[text()='新增']")

            logging.info("切入新增的iframe窗体")
            switch_to("xpath", "//iframe[@id='addWin-iframe']")

            logging.info("在新增页面的'独资安全资金'框里输入'123456' ")
            input("xpath", "//input[@id='safefundsofsingle-input']", "123456")
            sleep(2)

            logging.info("在新增页面的'合资安全资金'框里输入'234567' ")
            input("xpath", "//input[@id='safefundsoftotal-input']", "234567")
            sleep(2)

            logging.info("在新增页面的'独资专项资金'框里输入'345678' ")
            input("xpath", "//input[@id='specificfundofsingle-input']", "345678")
            sleep(2)

            logging.info("在新增页面的'合资专项资金'框里输入'456789' ")
            input("xpath", "//input[@id='specificfundoftotal-input']", "456789")
            sleep(2)

            logging.info("在新增页面的'独资土地竞买保证金'框里输入'567890' ")
            input("xpath", "//input[@id='landbiddingdepositofsingle-input']", "567890")
            sleep(2)

            logging.info("在新增页面的'合资土地竞买保证金'框里输入'678901' ")
            input("xpath", "//input[@id='landbiddingdepositoftotal-input']", "678901")
            sleep(2)

            logging.info("在新增页面的'备注'框里输入 自动化测试描述框")
            input("xpath", "//textarea[@id='description']", "自动化测试描述框")
            sleep(2)

            logging.info("点击保存按钮")
            click("xpath", "//span[text()='保存']")

            logging.info("退出所有iframe窗体")
            switch_default()

            logging.info("用隐式等待方法等页面出现'保存成功'的提示框")
            implici_wait("xpath", "//span[contains(text(),'操作成功')]")
            print("其他资金，保存成功！")
            logging.info("其他资金，保存成功！")
            time.sleep(3)

            logging.info("测试修改功能")
            try:
                logging.info("切入 其他资金 的iframe窗体")
                switch_to("xpath", "//iframe[@id='availableFundBalance-tab-iframe']")

                logging.info("测试查询功能")
                logging.info("用JS的方法点击放大镜")
                js_click("xpath", "//span[@class='f-contrac-close']")
                sleep(1)

                logging.info("在查询条件的'数据来源'框中选择'手工录入' ")
                click("xpath", "//input[@id='combobox-input-source']")
                sleep(1)
                logging.info("模拟回车键")
                keyDown('enter')
                keyUp('enter')
                time.sleep(2)

                logging.info("点击查询")
                js_click("xpath", "//span[text()='查询']")
                sleep(2)

                logging.info("勾选数据")
                click("xpath", "//div[@title='独资安全资金:123,456.00']/parent::*/preceding-sibling::*[2]/descendant::*[2]")
                sleep(1)

                logging.info("点击修改按钮")
                click("xpath", "//span[text()='修改']")
                sleep(1)

                logging.info("切入修改的iframe窗体")
                switch_to("xpath", "//iframe[@id='modWin-iframe']")

                logging.info("在备注框里输入 自动化测试修改")
                input("xpath", "//textarea[@id='description']", "，自动化测试修改")
                sleep(2)

                logging.info("点击保存按钮")
                click("xpath", "//span[text()='保存']")

                logging.info("退出所有iframe窗体")
                switch_default()

                logging.info("用隐式等待方法等页面出现'修改成功'的提示框")
                implici_wait("xpath", "//span[contains(text(),'操作成功')]")
                print("其他资金，修改成功！")
                logging.info("其他资金，修改成功！")
                sleep(3)
            except Exception as err:
                # 发生其他异常时，打印异常堆栈信息
                Test_Zonghechaxunxitong_QTZJ_Num += 1
                print(traceback.print_exc())
                logging.debug("其他资金，修改失败！" + str(traceback.format_exc()))
                # Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
                dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
                dir_path = make_current_hour_dir(dir_path + "\\")
                pic_path = os.path.join(dir_path, get_current_time() + ".png")
                capture(pic_path)
                raise err

            logging.info("测试失效功能")
            try:
                logging.info("切入 其他资金 的iframe窗体")
                switch_to("xpath", "//iframe[@id='availableFundBalance-tab-iframe']")

                logging.info("勾选数据")
                click("xpath", "//div[@title='独资安全资金:123,456.00']/parent::*/preceding-sibling::*[2]/descendant::*[2]")
                sleep(1)

                logging.info("点击失效按钮")
                click("xpath", "//span[text()='失效']")
                sleep(1)

                logging.info("点击弹出框的OK键")
                click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

                logging.info("退出所有iframe窗体")
                switch_default()

                logging.info("用隐式等待方法等页面出现'失效1条'提示框")
                implici_wait("xpath", "//span[contains(text(),'失效1条')]")
                print("其他资金，点击失效成功！")
                logging.info("其他资金，点击失效成功！")
                time.sleep(3)
            except Exception as err:
                # 发生其他异常时，打印异常堆栈信息
                Test_Zonghechaxunxitong_QTZJ_Num += 1
                print(traceback.print_exc())
                logging.debug("其他资金，点击失效失败！" + str(traceback.format_exc()))
                # Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
                dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
                dir_path = make_current_hour_dir(dir_path + "\\")
                pic_path = os.path.join(dir_path, get_current_time() + ".png")
                capture(pic_path)
                raise err

            logging.info("测试生效功能")
            try:
                logging.info("切入 其他资金 的iframe窗体")
                switch_to("xpath", "//iframe[@id='availableFundBalance-tab-iframe']")

                logging.info("勾选数据")
                click("xpath", "//div[@title='独资安全资金:123,456.00']/parent::*/preceding-sibling::*[2]/descendant::*[2]")
                sleep(1)

                logging.info("点击生效按钮")
                click("xpath", "//span[text()='生效']")
                sleep(1)

                logging.info("点击弹出框的OK键")
                click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

                logging.info("退出所有iframe窗体")
                switch_default()

                logging.info("用隐式等待方法等页面出现'生效1条'提示框")
                implici_wait("xpath", "//span[contains(text(),'生效1条')]")
                print("其他资金，点击生效成功！")
                logging.info("其他资金，点击生效成功！")
                time.sleep(3)
            except Exception as err:
                # 发生其他异常时，打印异常堆栈信息
                Test_Zonghechaxunxitong_QTZJ_Num += 1
                print(traceback.print_exc())
                logging.debug("其他资金，点击生效失败！" + str(traceback.format_exc()))
                # Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
                dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
                dir_path = make_current_hour_dir(dir_path + "\\")
                pic_path = os.path.join(dir_path, get_current_time() + ".png")
                capture(pic_path)
                raise err

            logging.info("测试删除功能")
            try:
                logging.info("切入 其他资金 的iframe窗体")
                switch_to("xpath", "//iframe[@id='availableFundBalance-tab-iframe']")

                logging.info("勾选数据")
                click("xpath", "//div[@title='独资安全资金:123,456.00']/parent::*/preceding-sibling::*[2]/descendant::*[2]")
                sleep(1)

                logging.info("点击删除按钮")
                click("xpath", "//span[text()='删除']")

                logging.info("点击弹出框的OK键")
                click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

                logging.info("退出所有iframe窗体")
                switch_default()

                # 用隐式等待方法等页面出现撤销送审成功的提示框
                logging.info("用隐式等待方法等页面出现'操作成功！'的提示框")
                implici_wait("xpath", "//span[contains(text(),'操作成功')]")
                print("其他资金，删除成功！")
                logging.info("其他资金，删除成功！")
                sleep(2)
            except Exception as err:
                # 发生其他异常时，打印异常堆栈信息
                Test_Zonghechaxunxitong_QTZJ_Num += 1
                print(traceback.print_exc())
                logging.debug("其他资金，删除失败！" + str(traceback.format_exc()))
                # Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
                dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
                dir_path = make_current_hour_dir(dir_path + "\\")
                pic_path = os.path.join(dir_path, get_current_time() + ".png")
                capture(pic_path)
                raise err


        except Exception as err:
            # 发生其他异常时，打印异常堆栈信息
            Test_Zonghechaxunxitong_QTZJ_Num += 1
            print(traceback.print_exc())
            logging.debug("其他资金，操作失败！" + str(traceback.format_exc()))
            # Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
            dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
            dir_path = make_current_hour_dir(dir_path + "\\")
            pic_path = os.path.join(dir_path, get_current_time() + ".png")
            capture(pic_path)
            raise err

        print('Test_Zonghechaxunxitong_QTZJ_Num 的值:',Test_Zonghechaxunxitong_QTZJ_Num)
        if Test_Zonghechaxunxitong_QTZJ_Num ==0:
            logging.info("用JS的方法关闭当前页面")
            js_click("xpath", "//a[@title='其他资金']/child::*[1]")
            sleep(2)

            print("'其他资金'，操作成功!")
            logging.info("'其他资金'，操作成功!")
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
            print("'其他资金'，有关键节点功能测试失败!")
            logging.info("'其他资金'，有关键节点功能测试失败!")

    # def tearDown(self):
    #     logging.info("关闭浏览器")
    #     quit()

        print("结束时间：", time.strftime("%Y-%m-%d %H:%M:%S"))
        logging.info("结束时间：%s" % (time.strftime("%Y-%m-%d %H:%M:%S")))


if __name__ == '__main__':
    #  启动单元测试
    unittest.main(verbosity=2)