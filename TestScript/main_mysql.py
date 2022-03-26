# encoding=utf-8
# @Time : 2020/8/27 21:31
# @Author : Mindy
# @Filename description : main-mysql用来测试mysql版本付款处理模块，共25个文件

import unittest
from ter.Test32_QuanQiuHuiKuan_ZLDBZF import Test32_WaiBiShouFuJieSuan_QQHK_ZLDBZF

from Action.send_mail_cls import send_mail_cls


if __name__ == '__main__':
    #  根据给定的测试类，获取其中的所有以“test”开头的测试方法，并返回一测试套件
    testCase1 = unittest.TestLoader().loadTestsFromTestCase(Test32_WaiBiShouFuJieSuan_QQHK_ZLDBZF)
    
    #  将多个测试类加载到测试套件中
    suite = unittest.TestSuite([testCase1])
    # 设置verbosity = 2,可以打印出更详细的执行信息
    unittest.TextTestRunner(verbosity=2).run(suite)

