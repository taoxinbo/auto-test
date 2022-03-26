# encoding=utf-8
# @Time : 2020/8/27 21:31
# @Author : Mindy
# @Filename description : main-oracle用来测试oracle版本付款处理模块，共25个文件

import unittest
from Util.Test_Fkcl_Zldbzf_Oracle import Test_Fkcl_Zldbzf_Oracle
from Util.Test_Fkcl_Zlplfk_Oracle import Test_Fkcl_Zlplfk_Oracle
from Util.Test_Fkcl_Cdhpzf_Oracle import Test_Fkcl_Cdhpzf_Oracle
from Util.Test_Fkcl_Zpzf_Oracle import Test_Fkcl_Zpzf_Oracle
from Util.Test_Fkcl_Xjzf_Oracle import Test_Fkcl_Xjzf_Oracle
from Util.Test_Fkcl_Qtzf_Oracle import Test_Fkcl_Qtzf_Oracle
from Util.Test_Jzfk_Zldbfk_Oracle import Test_Jzfk_Zldbfk_Oracle
from Util.Test_Jzfk_Zlplfk_Oracle import Test_Jzfk_Zlplfk_Oracle
from Util.Test_Jzfk_Kcz_Zldbfk_Oracle import Test_Jzfk_Kcz_Zldbfk_Oracle
from Util.Test_Jzfk_Kcz_Zlplfk_Oracle import Test_Jzfk_Kcz_Zlplfk_Oracle
from Util.Test_Jzfk_Qtzf_Oracle import Test_Jzfk_Qtzf_Oracle
from Util.Test_Skcl_Yhzhsk_Oracle import Test_Skcl_Yhzhsk_Oracle
from Util.Test_Skcl_Cdhpsp_Oracle import Test_Skcl_Cdhpsp_Oracle
from Util.Test_Skcl_Xjsk_Oracle import Test_Skcl_Xjsk_Oracle
from Util.Test_Skcl_Zldbsk_Oracle import Test_Skcl_Zldbsk_Oracle
from Util.Test_Skcl_Zlplsk_Oracle import Test_Skcl_Zlplsk_Oracle
from Util.Test_JgHh_ZljgHh_Oracle import Test_JgHh_ZljgHh_Oracle
from Util.Test_JgHh_QtjgHh_Oracle import Test_JgHh_QtjgHh_Oracle
from Util.Test_Kjwb_Zldbzf_Oracle import Test_Kjwb_Zldbzf_Oracle
from Util.Test_Kjwb_Qtzf_Oracle import Test_Kjwb_Qtzf_Oracle
from Util.Test_Qqhk_Zldbzf_Oracle import Test_Qqhk_Zldbzf_Oracle
from Util.Test_Qqhk_Zlplzf_Oracle import Test_Qqhk_Zlplzf_Oracle
from Util.Test_Qqhk_Qtzf_Oracle import Test_Qqhk_Qtzf_Oracle
from Util.Test_Jnwb_Zldbzf_Oracle import Test_Jnwb_Zldbzf_Oracle
from Util.Test_Jnwb_Qtzf_Oracle import Test_Jnwb_Qtzf_Oracle


from Action.send_mail_cls import send_mail_cls


if __name__ == '__main__':
    #  根据给定的测试类，获取其中的所有以“test”开头的测试方法，并返回一测试套件
    testCase1 = unittest.TestLoader().loadTestsFromTestCase(Test_Fkcl_Zldbzf_Oracle)
    testCase2 = unittest.TestLoader().loadTestsFromTestCase(Test_Fkcl_Zlplfk_Oracle)
    testCase3 = unittest.TestLoader().loadTestsFromTestCase(Test_Fkcl_Cdhpzf_Oracle)
    testCase4 = unittest.TestLoader().loadTestsFromTestCase(Test_Fkcl_Zpzf_Oracle)
    testCase5 = unittest.TestLoader().loadTestsFromTestCase(Test_Fkcl_Xjzf_Oracle)
    testCase6 = unittest.TestLoader().loadTestsFromTestCase(Test_Fkcl_Qtzf_Oracle)
    testCase7 = unittest.TestLoader().loadTestsFromTestCase(Test_Jzfk_Zldbfk_Oracle)
    testCase8 = unittest.TestLoader().loadTestsFromTestCase(Test_Jzfk_Zlplfk_Oracle)
    testCase9 = unittest.TestLoader().loadTestsFromTestCase(Test_Jzfk_Kcz_Zldbfk_Oracle)
    testCase10 = unittest.TestLoader().loadTestsFromTestCase(Test_Jzfk_Kcz_Zlplfk_Oracle)
    testCase11 = unittest.TestLoader().loadTestsFromTestCase(Test_Jzfk_Qtzf_Oracle)
    testCase12 = unittest.TestLoader().loadTestsFromTestCase(Test_Skcl_Yhzhsk_Oracle)
    testCase13 = unittest.TestLoader().loadTestsFromTestCase(Test_Skcl_Cdhpsp_Oracle)
    testCase14 = unittest.TestLoader().loadTestsFromTestCase(Test_Skcl_Xjsk_Oracle)
    testCase15 = unittest.TestLoader().loadTestsFromTestCase(Test_Skcl_Zldbsk_Oracle)
    testCase16 = unittest.TestLoader().loadTestsFromTestCase(Test_Skcl_Zlplsk_Oracle)
    testCase17 = unittest.TestLoader().loadTestsFromTestCase(Test_JgHh_ZljgHh_Oracle)
    testCase18 = unittest.TestLoader().loadTestsFromTestCase(Test_JgHh_QtjgHh_Oracle)
    testCase19 = unittest.TestLoader().loadTestsFromTestCase(Test_Kjwb_Zldbzf_Oracle)
    testCase20 = unittest.TestLoader().loadTestsFromTestCase(Test_Kjwb_Qtzf_Oracle)
    testCase21 = unittest.TestLoader().loadTestsFromTestCase(Test_Qqhk_Zldbzf_Oracle)
    testCase22 = unittest.TestLoader().loadTestsFromTestCase(Test_Qqhk_Zlplzf_Oracle)
    testCase23 = unittest.TestLoader().loadTestsFromTestCase(Test_Qqhk_Qtzf_Oracle)
    testCase24 = unittest.TestLoader().loadTestsFromTestCase(Test_Jnwb_Zldbzf_Oracle)
    testCase25 = unittest.TestLoader().loadTestsFromTestCase(Test_Jnwb_Qtzf_Oracle)
    #  将多个测试类加载到测试套件中
    suite = unittest.TestSuite([testCase1, testCase2, testCase3, testCase4, testCase5, testCase6, testCase7, testCase8, testCase9, testCase10, testCase11, testCase12, testCase13, testCase14, testCase15, testCase16, testCase17, testCase18, testCase19, testCase20, testCase21, testCase22, testCase23, testCase24, testCase25])
    # 设置verbosity = 2,可以打印出更详细的执行信息
    unittest.TextTestRunner(verbosity=2).run(suite)

