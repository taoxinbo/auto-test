#encoding=utf-8
import cx_Oracle
import time
import traceback
import xlsxwriter
import xlwt  # 操作excel模块
# 从文件所在目录中导入Log.py文件中所有内容
from Action.Log import *
from Config.VarConfig import *
from Config.SQL import *

def Clean_Oracle_DB(ora_ip,ora_sid,ora_user,ora_pwd,sql1,sql2,sql3,sql4,sql5,sql6_ora,sql7,sql8,sql9,sql10,sql11):
    #创建数据库连接,配置监听并连接
    #cx_Oracle.connect('username','pwd','ora的tns信息')
    #oracle数据库的tns信息，从tnsnames.ora中找到plsql可用的配置项，将该配置项直接拷贝过来即可
    ora_tns=cx_Oracle.makedsn(ora_ip,1521,ora_sid)
    conn=cx_Oracle.connect(ora_user,ora_pwd,ora_tns)
    # 操作游标
    cursor = conn.cursor()

    print("开始清除Oracle环境的数据......")
    logging.info("开始清除Oracle环境的数据......")

    try:
        #一、删除'自动化测试租户'下的数据
        # 执行sql1 先判断新租户是否存在，存在的话 把租户'tenantid'值作为变量赋值给执行删除sql2中的SQL
        cursor.execute(sql1)
        number1 =cursor.fetchone()
        #print(number1)
        if number1 is None:
            print("自动化测试租户，不存在！")
            logging.info("自动化测试租户，不存在")
        else:
            tenantid=str(number1[0])
            # print(number1)
            # print(type(number1))
            # print(tenantid)
            # print(type(tenantid))

            #遍历sql2语句 把'tenantid'值赋值给SQL
            for sql in sql2:
                #cursor.execute(sql,tenantid)
                 cursor.execute(sql%tenantid)
                # number2 = cursor.fetchall()
                # for loanNumber in number3:
                #     print(loanNumber)
            print("已删除：自动化测试租户！")
            logging.info("已删除：自动化测试租户！")

        # 先执行sql3 判断'tsys_package'表中字段'description'为'自动化测试套餐'的数据是否存在，存在就执行sql4 删除相关信息。
        cursor.execute(sql3)
        number = cursor.fetchone()
        #print(number)
        if number is None:
            print("'tsys_package'表中字段'description'为'自动化测试套餐'的数据，不存在！")
            logging.info("'tsys_package'表中字段'description'为'自动化测试套餐'的数据，不存在！")
        else:
            cursor.execute(sql4)
            print("已删除：'tsys_package'表中字段'description'为'自动化测试套餐'的数据！")
            logging.info("已删除：'tsys_package'表中字段'description'为'自动化测试套餐'的数据！")
    except Exception as err:
        # 发生其他异常时，打印异常堆栈信息
        print(traceback.print_exc())
        logging.debug("执行SQL报错：" + str(traceback.format_exc()))


    # 二、设置清除'默认租户'下的数据
    try:
        # 在'默认租户'下，检查并设置：直联设置--银行--直联银行--'中国工商银行'设置成直联。
        # 先执行sql5 判断'中国工商银行'是否为直联，不直联就执行sql6_ora 变成直联。
        cursor.execute(sql5)
        number = cursor.fetchone()
        # print(number)
        if number is None:
            cursor.execute(sql6_ora)
            print("默认租户下的'中国工商银行'，直联设置成功！")
            logging.info("默认租户下的'中国工商银行'，直联设置成功！")
        else:
            print("默认租户下的'中国工商银行'，已存在直联！")
            logging.info("默认租户下的'中国工商银行'，已存在直联！")
    except Exception as err:
        # 发生其他异常时，打印异常堆栈信息
        print(traceback.print_exc())
        logging.debug("执行SQL报错：" + str(traceback.format_exc()))


    try:
        #在'默认租户'下，检查并设置：直联设置--银行--直联银行--'中国银行（香港）'设置成非直联。
        #先执行sql7 判断'中国银行（香港）'是否为直联，如果是直联就执行sql8 变成非直联。
        cursor.execute(sql7)
        number = cursor.fetchone()
        #print(number)
        if number is None:
            print("默认租户下的'中国银行（香港）'，已是非直联银行！")
            logging.info("默认租户下的'中国银行（香港）'，已是非直联银行！")
        else:
            cursor.execute(sql8)
            print("默认租户下的'中国银行（香港），设置非直联成功！")
            logging.info("默认租户下的'中国银行（香港），设置非直联成功！")
    except Exception as err:
        # 发生其他异常时，打印异常堆栈信息
        print(traceback.print_exc())
        logging.debug("执行SQL报错：" + str(traceback.format_exc()))


    try:
        # 判断默认租户下是否有'Tao'用户，没有的话 就不执行
        cursor.execute("select * from tsys_user a where a.user_id='Tao' and a.tenantid=10001")
        number3 = cursor.fetchone()
        if number3 is None:
            print("默认租户下，没有Tao的用户！")
            logging.info("默认租户下，没有Tao的用户！")
        else:
            # 遍历sql9语句
            # '默认租户下的用户设置'中，用户编号是'Tao'的用户，取消掉所有分配的组织。
            # '默认租户下的多岗设置'中，用户的角色编码如果是'TestRole'中文名称'测试角色'，都取消掉。
            # '默认租户下的角色设置'中，删掉角色编码是'TestRole'的数据。
            for sql in sql9:
                cursor.execute(sql)
                # number2 = cursor.fetchall()
                # for loanNumber in number3:
                #     print(loanNumber)
            print("默认租户下的用户设置、多岗设置、角色设置,已处理！")
            logging.info("默认租户下的用户设置、多岗设置、角色设置,已处理！")

            # 遍历sql10语句，删除默认租户下的用户Tao
            for sql in sql10:
                cursor.execute(sql)
                # number2 = cursor.fetchall()
                # for loanNumber in number3:
                #     print(loanNumber)
            print("已删除：默认租户下的用户'Tao'！")
            logging.info("已删除：默认租户下的用户'Tao'！")
    except Exception as err:
        # 发生其他异常时，打印异常堆栈信息
        print(traceback.print_exc())
        logging.debug("执行SQL报错：" + str(traceback.format_exc()))


    try:
        # 遍历sql11语句
        # '默认租户下的组织机构设置'中，删掉组织编码是'TestOrgSet'的数据。
        # '默认租户下的组织类别设置'中，删掉代码是'TestOrgType'的数据。
        # '默认租户下的组织分类设置'中，删掉代码是'TestOrgClass'的数据。
        for sql in sql11:
            cursor.execute(sql)
            # number2 = cursor.fetchall()
            # for loanNumber in number3:
            #     print(loanNumber)
        print("已删除：默认租户下组织机构是'TestOrgSet'、组织类别是'TestOrgType'、组织分类是'TestOrgClass'！")
        logging.info("已删除：默认租户下组织机构是'TestOrgSet'、组织类别是'TestOrgType'、组织分类是'TestOrgClass'！")
    except Exception as err:
        # 发生其他异常时，打印异常堆栈信息
        print(traceback.print_exc())
        logging.debug("执行SQL报错：" + str(traceback.format_exc()))

    # 关闭游标
    cursor.close()
    # 提交事务
    conn.commit()
    # 关闭数据库连接
    conn.close()

if __name__ == '__main__':

    Clean_Oracle_DB(ora_ip,ora_sid,ora_user,ora_pwd,sql1,sql2,sql3,sql4,sql5,sql6_ora,sql7,sql8,sql9,sql10,sql11)

