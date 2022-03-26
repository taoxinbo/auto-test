#coding:utf-8
import unittest
from Util.Test_XinxQx import Test_XinxQx
from Util.Test_Xtcs import Test_Xtcs
from Util.Syset_base import Syset_base
from Util.Syset_config import Syset_config
from Action.send_mail_cls import send_mail_cls


if __name__ == '__main__':
    #  根据给定的测试类，获取其中的所有以“test”开头的测试方法，并返回一测试套件
    testCase1 = unittest.TestLoader().loadTestsFromTestCase(Test_XinxQx)
    testCase2 = unittest.TestLoader().loadTestsFromTestCase(Test_Xtcs)
    testCase3 = unittest.TestLoader().loadTestsFromTestCase(Syset_base)
    testCase4 = unittest.TestLoader().loadTestsFromTestCase(Syset_config)
    testCase5 = unittest.TestLoader().loadTestsFromTestCase(send_mail_cls)

    #  将多个测试类加载到测试套件中
    suite = unittest.TestSuite([testCase1, testCase2])
    #  suite = unittest.TestSuite([testCase3, testCase4, testCase5, testCase6])
    # 设置verbosity = 2,可以打印出更详细的执行信息
    unittest.TextTestRunner(verbosity=2).run(suite)

