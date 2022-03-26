# encoding=utf-8
import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))
# 获取当前文件所在目录的父目录的绝对路径
parentDirPath = os.path.dirname(os.path.dirname(__file__))

##########=======测试用例集合sheet对应的序号====############

test_step_id_col_no = 0
test_step_result_col_no = 8
test_step_error_info_col_no = 9
test_step_capture_pic_path_col_no = 10

##########=======测试用例sheet对应的序号====############

test_case_id_col_no = 0
test_case_sheet_name = 2
test_case_is_executed_flag_row_no = 3
test_case_start_time_col_no = 5
test_case_end_time_col_no = 6
test_case_elapsed_time_col_no = 7
test_case_result_col_no = 8

###############=======超级管理员和密码======###############

# 超级管理员和密码
SupAdmin = 'SupAdmin'
privatecloud = 'privatecloud@1'

# 列表L1存放不需要选择套餐的用户
L1 = [SupAdmin]

###############========用户名和密码========###############

# "自动化测试租户"下用户
TestUser = "TestUser"

# 测试用户名
mindy = "mindy"
Tao='Tao'
judy='judy'
Felix='Felix'

# 密码
Password = "fingard@1"

# 把‘用户名和密码’放到一个字典中
dict = {"test001": "fingard@1", "mindy": "fingard@1"}

###############====本机测试地址======###############

# 本机Oracle测试地址
B_Ora_Url_1 = "http://127.0.0.1:8080/newmbs"
# 虚拟机Oracle测试地址
B_Ora_Url_2 = "http://192.168.254.1:8080/newmbs"

########====本机Oracle数据库对应的参数====##########

# #Oracle数据库对应的IP地址
# ora_ip="127.0.0.1"
# #ora_ip="192.168.254.1"
# #Oracle数据库对应的实例
# ora_sid="ATSDB"
# #Oracle数据库对应的用户名
# ora_user="jats001"
# #Oracle数据库对应的密码
# ora_pwd="jats001"

########====本机mysql数据库对应的参数====##########

# mysql数据库对应的IP地址
# my_host = "127.0.0.1"
# # mysql数据库对应的端口
# my_port = 3306
# # mysql数据库对应的用户名
# my_user = "root"
# # mysql数据库对应的密码
# my_passwd = "123456"
# # mysql数据库对应的数据库
# my_db = "test"

###############====公司测试地址======###############

#ATS2.0开发分支Oracle测试地址
G_Ora_Url_Bd = "http://10.60.44.222:3130/newmbs"
#自动化Oracle测试地址
G_Ora_Url = "http://10.60.48.155:3130/newmbs"
#金田铜业测试地址
#G_Ora_Url = "http://10.60.48.177:3130/newmbs"
#通威股份测试地址
#G_Ora_Url = "http://10.60.48.177:8080/ats"

#新和成：weblogic-19C测试地址
#G_Ora_Url = "http://10.60.48.152:7001/front/bizframe/default/jsp/login.jsp"

# 万达测试地址
# G_Ora_Url = "http://10.60.47.117:3130/newmbs/bizframe/default/jsp/login.jsp "
# G_Ora_Url = "http://10.60.46.196:8080/newmbs"
#公司补丁mysql测试地址
G_Mys_Url_Bd = "http://10.60.44.245:7170/newmbs/"

#自动化mysql测试地址
G_Mys_Url = "http://10.60.48.155:5150/newmbs/"

#其他临时mysql测试地址
#G_Mys_Url = "http://10.60.48.177:3130/newmbs/"

# http://10.60.44.245:5150/newmbs
# 本地MySQL测试地址
# G_Mys_Url = "http://10.60.51.176:8080/newmbs"
#############====测试地址放到一个列表中====###########

# Url_L = [G_Ora_Url,G_Mys_Url]
#Url_L = [G_Ora_Url]
Url_L = [G_Mys_Url]



# ########====公司主线Oracle数据库对应的参数====##########
#
# Oracle数据库对应的IP地址
ora_ip = "10.60.44.92"
# ora_ip="192.168.254.1"
#新和成：weblogic-19C数据库IP
#ora_ip = "10.60.48.152"
# Oracle数据库对应的实例
ora_sid = "atsdb"
#新和成：weblogic-19C数据库的实例
#ora_sid = "orcl"
# Oracle数据库对应的用户名
ora_user = "jats_auto"
##新和成：weblogic-19C数据库的用户名
#ora_user = "jats005"
# Oracle数据库对应的密码
ora_pwd = "jats_auto"
##新和成：weblogic-19C数据库的密码
#ora_pwd = "jats005"

########====公司mysql自动化环境对应数据库的参数====##########

# mysql数据库对应的IP地址
my_host = "10.60.44.221"
# mysql数据库对应的端口
my_port = 3306
# mysql数据库对应的用户名
my_user = "root"
# mysql数据库对应的密码
my_passwd = "Mysql@123"
# mysql数据库对应的数据库
my_db = "jats_auto"

########====公司补丁mysql数据库对应的参数====##########

# mysql数据库对应的IP地址
my_host_bd = "10.60.44.221"
# mysql数据库对应的端口
my_port_bd = 3306
# mysql数据库对应的用户名
my_user_bd = "root"
# mysql数据库对应的密码
my_passwd_bd = "Mysql@123"
# mysql数据库对应的数据库
my_db_bd = "jats2613reg"

# 失败后的重试次数
pytest_flaky = 2