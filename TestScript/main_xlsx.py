#encoding=utf-8
from Action.execute import *

if __name__ == "__main__":
    # 遍历执行所有测试用例
    test_data_excel_file_path1 = parentDirPath+"\\TestData\\Syset_base.xlsx"
    test_data_excel_file_path2 = parentDirPath + "\\TestData\\Syset_config.xlsx"
    #test_data_excel_file_path=parentDirPath+"\\TestData\\Syset_config.xlsx"
    #把所有excel用例放到一个列表中
    test_data_excel_file_path=[test_data_excel_file_path1,test_data_excel_file_path2]
    #test_data_excel_file_path = [test_data_excel_file_path]
    #遍历每个excel用例
    for test_data_excel_file_path_L in test_data_excel_file_path:
        clear_test_data_file_info(test_data_excel_file_path_L)
        for test_case_sheet in get_test_case_sheet(test_data_excel_file_path_L):
            execute(test_data_excel_file_path_L,test_case_sheet[0],test_case_sheet[1])
    send_mail()

