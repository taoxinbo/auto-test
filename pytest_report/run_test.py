# coding=utf-8
import pytest, time
from selenium.webdriver import Chrome
import multiprocessing
from multiprocessing import Process, Queue
import sys
sys.path.append(r"E:/ATS/ter_Oracle/")


def copy(index):
    pytest.main([f'{index}', r'--alluredir=report/dirallure'])
    time.sleep(1)


if __name__ == '__main__':
    def main():
        List = ["E:/ATS/ter_Oracle/Test56_WaiBiYeWuDuiJie.py::Test56_WaiBiYeWuDuiJie::test_trade"]
        # List = ["E:/ATS/ter_Oracle/Test01_ZhangHuZiJinJianKong.py::Test_Zhzj::test_trade",
        #         "E:/ATS/ter_Oracle/Test02_XinXiQuanXian.py::Test_XinxQx::test_trade",
        #         "E:/ATS/ter_Oracle/Test03_JiHuaRenWu.py::Test_Jhrw::test_trade",
        #         "E:/ATS/ter_Oracle/Test04_ZiJinJieSuan.py::Test_Zjjs::test_trade",
        #         "E:/ATS/ter_Oracle/Test05_PiaoJuGuanLi.py::Test36_WaiBiShouFuJieSuan_JNWBHK_QTZF::test_trade",
        #         "E:/ATS/ter_Oracle/Test06_TouZiGuanLi.py::Test_Tzgl::test_trade",
        #         "E:/ATS/ter_Oracle/Test07_ZhaiQuanFaXing.py::Test_Zqfx::test_trade",
        #         "E:/ATS/ter_Oracle/Test08_NeiBuJieKuan_zzg.py::Test_Dbsq::test_trade",
        #         "E:/ATS/ter_Oracle/Test09_DanBaoguanLi.py::Test_Dbgl::test_trade",
        #         "E:/ATS/ter_Oracle/Test10_DanBaoShenQing.py::Test_Dbsq::test_trade",
        #         "E:/ATS/ter_Oracle/Test11_BaoZhengJinGuanLi.py::Test_Bzjgl::test_trade",
        #         "E:/ATS/ter_Oracle/Test12_FUKuanChuLi_ZLDB.py::Test_Fkcl_Zldbzf_Mysql::test_trade",
        #         "E:/ATS/ter_Oracle/Test13_FuKuanChuLi_PLFK.py::Test_Fkcl_Zlplfk_Mysql::test_trade",
        #         "E:/ATS/ter_Oracle/Test14_FuKuanChuLi_CDHPZF.py::Test14_FuKuanChuLi_CDHPZF::test_trade",
        #         "E:/ATS/ter_Oracle/Test15_FuanKuanChuLi_ZPZF.py::Test15_FuanKuanChuLi_ZPZF::test_trade",
        #         "E:/ATS/ter_Oracle/Test16_FuKuanChuLi_XJZF.py::Test16_FuKuanChuLi_XJZF::test_trade",
        #         "E:/ATS/ter_Oracle/Test17_FuKuanChuLi_QTZF.py::Test17_FuKuanChuLi_QTZF::test_trade",
        #         "E:/ATS/ter_Oracle/Test18_JiZhongFuKuan_ZLDBFK.py::Test18_JiZhongFuKuan_ZLDBFK::test_trade",
        #         "E:/ATS/ter_Oracle/Test19_JiZhongFuKuan_ZLPLFK.py::Test19_JiZhongFuKuan_ZLPLFK::test_trade",
        #         "E:/ATS/ter_Oracle/Test20_JiZhongFuKuan_KCZZLDB.py::Test20_JiZhongFuKuan_KCZZLDB::test_trade",
        #         "E:/ATS/ter_Oracle/Test21_JiZhongFuKuan_KCZZLPL.py::Test21_JiZhongFuKuan_KCZZLPL::test_trade",
        #         "E:/ATS/ter_Oracle/Test22_JiZhongFuKuan_QTZF.py::Test22_JiZhongFuKuan_QTZF::test_trade",
        #         "E:/ATS/ter_Oracle/Test23_ShouKuanChuLi_YHZHSK.py::Test23_ShouKuanChuLi_YHZHSK::test_trade",
        #         "E:/ATS/ter_Oracle/Test24_ShouKuanChuLi_CDHPSP.py::Test24_ShouKuanChuLi_CDHPSP::test_trade",
        #         "E:/ATS/ter_Oracle/Test25_ShouKuanChuLi_XJSK.py::Test25_ShouKuanChuLi_XJSK::test_trade",
        #         "E:/ATS/ter_Oracle/Test26_ShouKuanChuLi_ZLDBSK.py::Test26_ShouKuanChuLi_ZLDBSK::test_trade",
        #         "E:/ATS/ter_Oracle/Test27_ShouKuanGuanLi_ZLPLFK.py::Test27_ShouKuanGuanLi_ZLPLFK::test_trade",
        #         "E:/ATS/ter_Oracle/Test28_JieGouHuanHui_ZLJGHH.py::Test28_JieGouHuanHui_ZLJGHH::test_trade",
        #         "E:/ATS/ter_Oracle/Test29_JieGouHuanHui_QTJGHH.py::Test29_JieGouHuanHui_QTJGHH::test_trade",
        #         "E:/ATS/ter_Oracle/Test30_KuaJingWaiBiHuiKuan_ZLDBZF.py::Test30_KuaJingWaiBiHuiKuan_ZLDBZF::test_trade",
        #         "E:/ATS/ter_Oracle/Test31_KuaJingWaiBiHuiKuan_QTZF.py::Test31_KuaJingWaiBiHuiKuan_QTZF::test_trade",
        #         "E:/ATS/ter_Oracle/Test32_QuanQiuHuiKuan_ZLDBZF.py::Test32_QuanQiuHuiKuan_ZLDBZF::test_trade",
        #         "E:/ATS/ter_Oracle/Test33_QuanQiuHuiKuan_ZLPLZF.py::Test33_QuanQiuHuiKuan_ZLPLZF::test_trade",
        #         "E:/ATS/ter_Oracle/Test34_QuanQiuHuiKuan_QTZF.py::Test34_QuanQiuHuiKuan_QTZF::test_trade",
        #         "E:/ATS/ter_Oracle/Test35_JingNeiWaiBiHuiKuan_ZLDB.py::Test35_JingNeiWaiBiHuiKuan_ZLDB::test_trade",
        #         "E:/ATS/ter_Oracle/Test36_JingNeiWaiBiHuiKuan_QTZF.py::Test36_JingNeiWaiBiHuiKuan_QTZF::test_trade",
        #         "E:/ATS/ter_Oracle/Test37_KuaiJieFuKuan_FKSQ.py::Test37_KuaiJieFuKuan_FKSQ::test_trade",
        #         "E:/ATS/ter_Oracle/Test38_KuaiJieFuKuan_DBFKCL.py::Test38_KuaiJieFuKuan_DBFKCL::test_trade",
        #         "E:/ATS/ter_Oracle/Test39_KuaiJieFuKuan_ZLPLFKCL.py::Test39_KuaiJieFuKuan_ZLPLFKCL::test_trade",
        #         "E:/ATS/ter_Oracle/Test40_KuaiJieFuKuan_CDHPFKCL.py::Test40_KuaiJieFuKuan_CDHPFKCL::test_trade",
        #         "E:/ATS/ter_Oracle/Test41_KuaiJieFuKuan_ZPZFCL.py::Test41_KuaiJieFuKuan_ZPZFCL::test_trade",
        #         "E:/ATS/ter_Oracle/Test42_KuaiJieFuKuan_KCZZZPLDF.py::Test42_KuaiJieFuKuan_KCZZZPLDF::test_trade",
        #         "E:/ATS/ter_Oracle/Test43_KuaiJieFuKuan_PLSSCL.py::Test43_KuaiJieFuKuan_PLSSCL::test_trade",
        #         "E:/ATS/ter_Oracle/Test44_KuaiJieShouKuan_DBSKCK.py::Test44_KuaiJieShouKuan_DBSKCK::test_trade",
        #         "E:/ATS/ter_Oracle/Test45_KuaiJieShouKuan_PLFKCL.py::Test45_KuaiJieShouKuan_PLFKCL::test_trade",
        #         "E:/ATS/ter_Oracle/Test46_KuaiJieShouKuan_LXSK.py::Test46_KuaiJieShouKuan_LXSK::test_trade",
        #         "E:/ATS/ter_Oracle/Test47_KuaiJieJiZhongFuKuan_KCZZZKJFKSQ.py::Test47_KuaiJieJiZhongFuKuan_KCZZZKJFKSQ::test_trade",
        #         "E:/ATS/ter_Oracle/Test48_KuaiJieJiZhongFuKuan_KCZZZDBFKCL.py::Test48_KuaiJieJiZhongFuKuan_KCZZZDBFKCL::test_trade",
        #         "E:/ATS/ter_Oracle/Test49_KuaiJieJiZhongFuKuan_KCZZZCDHPFKCL.py::Test49_KuaiJieJiZhongFuKuan_KCZZZCDHPFKCL::test_trade",
        #         "E:/ATS/ter_Oracle/Test50_KuaiJieJiZhongFuKuan_KCZZZKJZPFKCL.py::Test50_KuaiJieJiZhongFuKuan_KCZZZKJZPFKCL::test_trade",
        #         "E:/ATS/ter_Oracle/Test51_KuaiJieJiZhongFuKuan_KCZZZKJPLFKCL.py::Test51_KuaiJieJiZhongFuKuan_KCZZZKJPLFKCL::test_trade",
        #         "E:/ATS/ter_Oracle/Test52_KuaiJieJiZhongFuKuan_BJHXJZZKJPLFKCL.py::Test52_KuaiJieJiZhongFuKuan_BJHXJZZKJPLFKCL::test_trade",
        #         "E:/ATS/ter_Oracle/Test53_FuKuanBianGengShenQing.py::Test53_FuKuanBianGengShenQing::test_trade",
        #         "E:/ATS/ter_Oracle/Test54_ZiJinJieSuanGuanLi_JSZXSF.py::Test54_ZiJinJieSuanGuanLi_JSZXSF::test_trade",
        #         "E:/ATS/ter_Oracle/Test55_ZiJinJieSuanGuanLi_JSZXSF_02.py::Test55_ZiJinJieSuanGuanLi_JSZXSF_02::test_trade",
        #         "E:/ATS/ter_Oracle/Test56_WaiBiYeWuDuiJie.py::Test56_WaiBiYeWuDuiJie::test_trade",
        #         "E:/ATS/ter_Oracle/Test57_NeiBuZiJinChi.py::Test57_NeiBuZiJinChi::test_trade",
        #         "E:/ATS/ter_Oracle/Test58_ZiJinJiHua.py::Test58_ZiJinJiHua::test_trade"]
        pool = multiprocessing.Pool(5)
        for i in List:
            pool.apply_async(copy, (i,))
        pool.close()
        pool.join()
    main()





