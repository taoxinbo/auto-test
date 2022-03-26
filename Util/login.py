# encoding=utf-8
# 2021-06-30
# TaoXB
# 此文件是自动化测试：综合查询系统--报表数据填报--公司盈利情况：新增、修改、删除、生效、失效
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
class Test_login(unittest.TestCase):

    # 启动浏览器
    def setUp(self):
        logging.info("启动Chrome浏览器")
        get("chrome")

    # 登陆系统、对综合查询系统--报表数据填报--公司盈利情况，进行操作
    def test_trade(self):

        logging.info("登陆系统")
        # login( G_Ora_Url,TestUser,Password, "自动化测试租户")
        # login( G_Ora_Url,Tao, Password,"默认租户")
        # login( G_Mys_Url,TestUser,Password, "自动化测试租户")
        # login(G_Mys_Url, Felix, Password, "默认租户")
        login(G_Mys_Url, mindy, Password, "亚唐科技")
        #login(G_Mys_Url_Bd, Felix, Password, "默认租户")
        # login(G_Ora_Url, 'judy', Password, "默认租户")
        # login(G_Mys_Url, 'Felix', Password, "默认租户")

        logging.info("用JS方法滚动至 综合查询系统  菜单")
        js_gd("xpath", "//span[contains(text(),'综合查询系统')]")
        logging.info("点击 综合查询系统 菜单")
        click("xpath", "//span[contains(text(),'综合查询系统')]")


    # def tearDown(self):
    #     logging.info("关闭浏览器")
    #     quit()

        print("结束时间：", time.strftime("%Y-%m-%d %H:%M:%S"))
        logging.info("结束时间：%s" % (time.strftime("%Y-%m-%d %H:%M:%S")))


if __name__ == '__main__':
    #  启动单元测试
    unittest.main(verbosity=2)