#encoding=utf-8
# 2021-06-30
# TaoXB
# 此文件是自动化测试：内部借款管理--担保管理--担保额度调整：新增、修改、删除、送审、撤销送审
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
import traceback,pytest
import time
from datetime import datetime, date, timedelta
from Action.dir_opration import make_current_date_dir, make_current_hour_dir
from Action.send_mail import *

#print("开始时间：",time.strftime("%Y-%m-%d %H:%M:%S"))


driver = ""

@pytest.mark.oracle
@pytest.mark.flaky(reruns=pytest_flaky,reruns_delay=10)
class Test_Danbaoguanli_DBEDTZ(unittest.TestCase):

    #启动浏览器
    def setUp(self):
        logging.info("启动Chrome浏览器")
        get("chrome")

    # 登陆系统、对内部借款管理--担保管理--担保额度调整，进行操作
    def test_trade(self):

        # 用来统计 每个关键节点 跑失败的个数，定义格式：文件名+‘_Num’
        Test_Danbaoguanli_DBEDTZ_Num = 0

        try:
            logging.info("登陆系统")
            #login(G_Mys_Url, mindy, Password, "亚唐科技")
            login(G_Ora_Url, mindy, Password, "亚唐科技")

            # login( G_Ora_Url,TestUser,Password, "自动化测试租户")
            # login( G_Ora_Url,Tao, Password,"默认租户")
            # login( G_Mys_Url,TestUser,Password, "自动化测试租户")
            # login(G_Mys_Url, Felix, Password, "默认租户")
            # login(G_Ora_Url, 'judy', Password, "默认租户")
            # login(G_Mys_Url, 'Felix', Password, "默认租户")

            logging.info("用JS方法滚动至 内部借款管理 菜单")
            js_gd("xpath", "//span[contains(text(),'内部借款管理')]")
            logging.info("点击 内部借款管理 菜单")
            click("xpath", "//span[contains(text(),'内部借款管理')]")
            logging.info("点击 内部借款管理--担保管理")
            click("xpath", "//span[contains(text(),'担保管理')]")
            logging.info("点击 内部借款管理--担保管理--担保额度调整")
            click("xpath", "//span[contains(text(),'担保额度调整')]")

            logging.info("开始测试：内部借款管理--担保管理--担保额度调整")

            logging.info("退出所有iframe窗体")
            switch_default()

            logging.info("测试新增功能")
            logging.info("切入 担保额度调整 的iframe窗体")
            switch_to("xpath", "//iframe[@id='extguarantamountadjust-tab-iframe']")
            logging.info("用JS的方法点击新增按钮")
            js_click("xpath", "//span[text()='新增']")

            logging.info("切入新增的iframe窗体")
            switch_to("xpath", "//iframe[@id='addWin-iframe']")

            logging.info("在新增页面的'调整类型'框里选择'调增',击在新增页面的'调整类型'框")
            click("xpath", "//input[@id='combobox-input-adjusttype']")
            sleep(1)
            logging.info("模拟回车键")
            keyDown('enter')
            keyUp('enter')
            time.sleep(2)

            logging.info("测试输入'调整金额'，先清空，再输入：123456789")
            clear("xpath", "//input[@id='adjustamount-input']")
            sleep(1)
            input("xpath", "//input[@id='adjustamount-input']", "123456789")
            sleep(1)

            logging.info("在新增页面的'币种'框里选择'人民币'，模拟往下键")
            click("xpath", "//input[@id='combobox-input-currencyid']")
            sleep(1)
            input_down("xpath","//input[@id='combobox-input-currencyid']")
            input_enter("xpath","//input[@id='combobox-input-currencyid']")
            sleep(1)

            logging.info("在新增页面的'被调剂组织'框里选择一个组织，模拟往下键")
            click("xpath", "//input[@id='combobox-input-adjustorg']")
            sleep(1)
            input_down("xpath", "//input[@id='combobox-input-adjustorg']")
            input_enter("xpath", "//input[@id='combobox-input-adjustorg']")
            sleep(1)

            logging.info("在新增页面的备注框里输入 自动化测试描述框")
            input("xpath", "//textarea[@id='description']", "自动化测试描述框")
            sleep(2)

            logging.info("点击保存按钮")
            click("xpath", "//span[text()='保存']")

            logging.info("退出所有iframe窗体")
            switch_default()

            logging.info("用隐式等待方法等页面出现'保存成功'的提示框")
            implici_wait("xpath", "//span[contains(text(),'操作成功')]")
            print("担保额度调整，保存成功！")
            logging.info("担保额度调整，保存成功！")
            time.sleep(3)
            
            logging.info("测试修改功能")
            try:
                logging.info("切入 担保额度调整 的iframe窗体")
                switch_to("xpath", "//iframe[@id='extguarantamountadjust-tab-iframe']")

                logging.info("测试查询功能")
                logging.info("用JS的方法点击放大镜")
                js_click("xpath", "//span[@class='f-contrac-close']")
                sleep(1)

                logging.info("在查询条件的'是否调剂其他组织额度'中选择'是'，模拟往下键 ")
                click("xpath", "//input[@id='combobox-input-adjustotherorg']")
                sleep(1)
                input_down("xpath", "//input[@id='combobox-input-adjustotherorg']")
                input_enter("xpath", "//input[@id='combobox-input-adjustotherorg']")
                sleep(1)

                logging.info("点击查询")
                js_click("xpath", "//span[text()='查询']")
                sleep(2)

                logging.info("勾选查找出来的数据")
                click("xpath","//div[contains(text(),'123,45')]/parent::*/preceding-sibling::*[4]/descendant::*[2]")
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
                print("担保额度调整，修改成功！")
                logging.info("担保额度调整，修改成功！")
                sleep(3)
            except Exception as err:
                # 发生其他异常时，打印异常堆栈信息
                Test_Danbaoguanli_DBEDTZ_Num +=1
                print(traceback.print_exc())
                logging.debug("担保额度调整，修改失败！" + str(traceback.format_exc()))
                # Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
                dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
                dir_path = make_current_hour_dir(dir_path + "\\")
                pic_path = os.path.join(dir_path, get_current_time() + ".png")
                capture(pic_path)
                raise err
            
            logging.info("测试'送审、撤销送审'功能")
            try:
                logging.info("退出所有iframe窗体")
                switch_default()

                logging.info("切入 担保额度调整 的iframe窗体")
                switch_to("xpath", "//iframe[@id='extguarantamountadjust-tab-iframe']")

                logging.info("勾选数据")
                click("xpath","//div[contains(text(),'123,45')]/parent::*/preceding-sibling::*[4]/descendant::*[2]")
                sleep(1)

                logging.info("测试'送审'功能")
                logging.info("点击'送审'按钮")
                click("xpath", "//span[text()='送审']")
                sleep(1)

                logging.info("退出所有iframe窗体")
                switch_default()

                logging.info("用隐式等待方法等页面出现'成功送审'的提示框")
                implici_wait("xpath", "//span[contains(text(),'成功送审1条记录')]")
                print("送审，成功！")
                logging.info("送审，成功！")
                sleep(3)

                logging.info("切入 担保额度调整 的iframe窗体")
                switch_to("xpath", "//iframe[@id='extguarantamountadjust-tab-iframe']")

                logging.info("勾选数据")
                click("xpath", "//div[contains(text(),'123,45')]/parent::*/preceding-sibling::*[4]/descendant::*[2]")
                sleep(1)

                logging.info("点击'送审'旁边的倒三角 ")
                click("xpath", "//span[text()='送审']/parent::*/following-sibling::*/child::*")
                sleep(1)

                logging.info("测试'撤销送审'功能")
                logging.info("点击'撤销送审'按钮")
                click("xpath", "//a[contains(.,'撤销送审')]")
                sleep(1)

                logging.info("点击弹窗的'OK'按钮")
                click("xpath", "//button[contains(.,'OK')]")
                time.sleep(2)

                logging.info("退出所有iframe窗体")
                switch_default()

                logging.info("用隐式等待方法等页面出现'成功撤销送审'的提示框")
                implici_wait("xpath", "//span[contains(text(),'成功撤销送审1条记录')]")
                print("撤销送审，成功！")
                logging.info("撤销送审，成功！")
                sleep(3)

                logging.info("切入 担保额度调整 的iframe窗体")
                switch_to("xpath", "//iframe[@id='extguarantamountadjust-tab-iframe']")

                logging.info("勾选数据")
                click("xpath", "//div[contains(text(),'123,45')]/parent::*/preceding-sibling::*[4]/descendant::*[2]")
                sleep(1)

                logging.info("第二次'送审'")
                logging.info("点击'送审'按钮")
                click("xpath", "//span[text()='送审']")
                sleep(1)

                logging.info("退出所有iframe窗体")
                switch_default()

                logging.info("用隐式等待方法等页面出现'成功送审'的提示框")
                implici_wait("xpath", "//span[contains(text(),'成功送审1条记录')]")
                print("第二次'送审'，成功！")
                logging.info("第二次'送审'，成功！")
                sleep(3)

                logging.info("切入 担保额度调整 的iframe窗体")
                switch_to("xpath", "//iframe[@id='extguarantamountadjust-tab-iframe']")

                logging.info("双击当前数据，进入审批页面")
                double_click("xpath", "//div[contains(text(),'123,45')]")

                logging.info("切入 审批页面的 的iframe窗体")
                switch_to("xpath", "//iframe[@id='wf_taskProcessing_win-iframe']")

                logging.info("测试'拒绝'按钮，点击'拒绝' ")
                click("xpath", "//span[contains(text(),'拒绝')]")

                logging.info("输入'拒绝'意见")
                input("xpath", "//textarea[@class='f-textarea']", "自动化测试")

                logging.info("点击'OK'键")
                click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

                logging.info("退出所有iframe窗体")
                switch_default()

                logging.info("用隐式等待方法等页面出现'操作成功'的提示框")
                implici_wait("xpath", "//span[contains(text(),'操作成功')]")
                print("审批'拒绝'，成功！")
                logging.info("审批'拒绝'，成功！")
                sleep(3)

                logging.info("切入 担保额度调整 的iframe窗体")
                switch_to("xpath", "//iframe[@id='extguarantamountadjust-tab-iframe']")

                logging.info("勾选数据")
                click("xpath","//div[contains(text(),'123,45')]/parent::*/preceding-sibling::*[4]/descendant::*[2]")
                sleep(1)

                logging.info("第三次'送审'")
                logging.info("点击'送审'按钮")
                click("xpath", "//span[text()='送审']")
                sleep(1)

                logging.info("退出所有iframe窗体")
                switch_default()

                logging.info("用隐式等待方法等页面出现'成功送审'的提示框")
                implici_wait("xpath", "//span[contains(text(),'成功送审1条记录')]")
                print("第三次'送审'，成功！")
                logging.info("第三次'送审'，成功！")
                sleep(3)

                logging.info("切入 担保额度调整 的iframe窗体")
                switch_to("xpath", "//iframe[@id='extguarantamountadjust-tab-iframe']")

                logging.info("双击当前数据，进入审批页面")
                double_click("xpath", "//div[contains(text(),'123,45')]")
                sleep(3)

                logging.info("切入 审批页面的 的iframe窗体")
                switch_to("xpath", "//iframe[@id='wf_taskProcessing_win-iframe']")

                logging.info("测试'同意'按钮，点击'同意' ")
                click("xpath", "//span[contains(text(),'同意')]")

                logging.info("退出所有iframe窗体")
                switch_default()

                logging.info("用隐式等待方法等页面出现'操作成功'的提示框")
                implici_wait("xpath", "//span[contains(text(),'操作成功')]")
                print("审批'同意'，成功！")
                logging.info("审批'同意'，成功！")
                sleep(3)
            except Exception as err:
                # 发生其他异常时，打印异常堆栈信息
                Test_Danbaoguanli_DBEDTZ_Num += 1
                print(traceback.print_exc())
                logging.debug("'送审、撤销送审'，失败！" + str(traceback.format_exc()))
                # Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
                dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
                dir_path = make_current_hour_dir(dir_path + "\\")
                pic_path = os.path.join(dir_path, get_current_time() + ".png")
                capture(pic_path)
                raise err

            logging.info("测试删除功能")
            try:
                logging.info("把测试数据的'审批状态'更新为'1'--'未审批' ")
                sql = " update  t_gu_extguarantamountadjust a set a.approvestate='1' where a.description like'%自动化测试%' "
                #my_sql(my_host, my_port, my_user, my_passwd, my_db, sql)
                ora_sql(ora_ip, ora_sid, ora_user, ora_pwd, sql)
                sleep(2)

                logging.info("切入 担保额度调整 的iframe窗体")
                switch_to("xpath", "//iframe[@id='extguarantamountadjust-tab-iframe']")

                logging.info("勾选")
                click("xpath", "//div[contains(text(),'123,45')]/parent::*/preceding-sibling::*[4]/descendant::*[2]")
                sleep(1)

                logging.info("点击删除按钮")
                click("xpath", "//span[text()='删除']")

                logging.info("点击弹出框的OK键")
                click("xpath", "//button[@id='f-message-webgen-0-okBnt']")

                logging.info("退出所有iframe窗体")
                switch_default()

                # 用隐式等待方法等页面出现撤销送审成功的提示框
                logging.info("用隐式等待方法等页面出现'成功删除1条记录！'的提示框")
                implici_wait("xpath", "//span[contains(text(),'成功删除')]")
                print("担保额度调整，删除成功！")
                logging.info("担保额度调整，删除成功！")
                sleep(2)
            except Exception as err:
                # 发生其他异常时，打印异常堆栈信息
                Test_Danbaoguanli_DBEDTZ_Num += 1
                print(traceback.print_exc())
                logging.debug("担保额度调整，删除失败！" + str(traceback.format_exc()))
                # Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
                dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
                dir_path = make_current_hour_dir(dir_path + "\\")
                pic_path = os.path.join(dir_path, get_current_time() + ".png")
                capture(pic_path)
                raise err

            #logging.info("用JS的方法关闭当前页面")
            #js_click("xpath", "//a[@title='担保额度调整']/child::*[1]")

            print("'担保额度调整'，操作成功!")
            logging.info("'担保额度调整'，操作成功!")
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


        except Exception as err:
            # 发生其他异常时，打印异常堆栈信息
            Test_Danbaoguanli_DBEDTZ_Num += 1
            print(traceback.print_exc())
            logging.debug("担保额度调整，操作失败！" + str(traceback.format_exc()))
            # Action中新增dir_operation.py，生成日期目录，创建日期目录，存放错误截屏信息
            dir_path = make_current_date_dir(parentDirPath + "\\" + "ScreenCapture\\")
            dir_path = make_current_hour_dir(dir_path + "\\")
            pic_path = os.path.join(dir_path, get_current_time() + ".png")
            capture(pic_path)
            raise err

        print('Test_Danbaoguanli_DBEDTZ_Num 的值:', Test_Danbaoguanli_DBEDTZ_Num)
        if Test_Danbaoguanli_DBEDTZ_Num == 0:
            logging.info("用JS的方法关闭当前页面")
            js_click("xpath", "//a[@title='担保额度调整']/child::*[1]")
            sleep(2)

            print("'担保额度调整'，操作成功!")
            logging.info("'担保额度调整'，操作成功!")
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
            print("'担保额度调整'，有关键节点功能测试失败!")
            logging.info("'担保额度调整'，有关键节点功能测试失败!")

    # def tearDown(self):
    #     logging.info("关闭浏览器")
    #     quit()

        print("结束时间：", time.strftime("%Y-%m-%d %H:%M:%S"))
        logging.info("结束时间：%s" % (time.strftime("%Y-%m-%d %H:%M:%S")))

if __name__ == '__main__':
    #  启动单元测试
    unittest.main(verbosity=2)
