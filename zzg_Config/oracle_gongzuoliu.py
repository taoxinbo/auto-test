# -*- coding: utf-8 -*-
# @Time    : 2021/5/30 14:25
# @Author  : fanek
# @FileName: oracle_gongzuoliu.py
# @Software: PyCharm


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
import random

driver = ""


class PZ(unittest.TestCase):

    # 启动浏览器
    def setUp(self):
        # 启动浏览器的另外一个方法：通过封装启动浏览器的驱动，启动不同浏览器
        self.driver = get("chrome")

    # 登陆系统、对系统设置进行操作
    def test_trade(self):

        login(G_Ora_Url, "SysAdmin", "fingard@1", "亚唐科技")

        try:

            click("xpath", '/html/body/div[1]/div[1]/div/div[2]/div/div[2]/div/div/div/div[3]/span[2]')
            sleep(1)
            click("xpath",
                  '/html/body/div[1]/div[1]/div/div[2]/div/div[2]/div/div/div/div[4]/div/div/ul/li[2]/a/span[2]')
            sleep(1)
            click("xpath",
                  '/html/body/div[1]/div[1]/div/div[2]/div/div[2]/div/div/div/div[4]/div/div/ul/li[2]/ul/li[1]/a/span[2]')
            sleep(1)
            switch_default()

            # 切入流程设计窗体
            switch_to("xpath", '//*[@id="flowManaDesign-tab-iframe"]')
            # 清空数据
            clear("xpath", '//*[@id="gridbar-page-size-input"]')
            sleep(1)
            # 输入200条记录
            input("xpath", '//*[@id="gridbar-page-size-input"]', 200)
            sleep(2)
            # 点击刷新
            click("xpath", '//*[@id="gridbar-page-refresh"]')
            sleep(1)

            for i in range(1, 114):
                path = '//*[@id="grid-body-table"]/tbody/tr[' + str(i) + ']/td[2]/div/button'
                js_gd("xpath", path)
                js_click("xpath", path)
                sleep(1)
                span_click("设计")
                sleep(1)
                # 切入发布窗体
                switch_to("xpath", '/html/body/div[2]/div[17]/div/div[2]/div[1]/div/iframe')
                click("xpath", '//*[@id="root"]/div/div/div[1]/div[2]/div[1]/button[4]/span')
                sleep(1)
                implici_wait("xpath", "//span[contains(text(),'发布成功！')]")
                switch_parent()
                click("xpath", '//*[@id="f-win-title-designWin"]/div[1]/div')
                sleep(1)




        except Exception as err:
            # 发生其他异常时，打印异常堆栈信息
            print(traceback.print_exc())
            logging.debug("现金收款失败！" + str(traceback.format_exc()))
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