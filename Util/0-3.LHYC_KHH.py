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
from Config.Orgid import *

#对Oracle数据库进行update、install、delete的封装
def ora_sql(ora_ip,ora_sid,ora_user,ora_pwd,sql):
    #创建数据库连接,配置监听并连接
    #cx_Oracle.connect('username','pwd','ora的tns信息')
    #oracle数据库的tns信息，从tnsnames.ora中找到plsql可用的配置项，将该配置项直接拷贝过来即可
    ora_tns=cx_Oracle.makedsn(ora_ip,1521,ora_sid)
    conn=cx_Oracle.connect(ora_user,ora_pwd,ora_tns)
    # 操作游标
    cursor = conn.cursor()
    # 执行语句
    cursor.execute(sql)
    # 执行查询
    #cursor.execute("select a.paystate,a.cancelstate,a.* from T_SE_PAYMENTS a where  a.oppbankaccountname='张三' and a.createdby='test001' and a.paystate='7'and a.cancelstate='1'")
    # 打印查询
    #print(cursor.fetchall())
    # 关闭游标
    cursor.close()
    # 提交事务
    conn.commit()
    # 关闭数据库连接
    conn.close()

if __name__ == '__main__':
    # #本机Oracle数据库对应信息
    # ora_ip = "127.0.0.1"
    # # ora_ip="192.168.254.1"
    # # Oracle数据库对应的实例
    # ora_sid = "ATSDB"
    # # Oracle数据库对应的用户名
    # ora_user = "jats001"
    # # Oracle数据库对应的密码
    # ora_pwd = "jats001"

    #  10.60.44.178数据库对应信息
    ora_ip = " 10.60.44.178"
    # Oracle数据库对应的实例
    ora_sid = "orcl"
    # Oracle数据库对应的用户名
    ora_user = "ms_ats_pt_hrjt"
    # Oracle数据库对应的密码
    ora_pwd = "ms_ats_pt_hrjt"

    # SQL2="select t.editstartcalendarid,t.editendcalendarid,t.editstartdate,t.editenddate,t.controlstartcalendarid,t.controlendcalendarid,t.controlstartdate,t.controlenddate from T_BU_BUDGET  t where t.notecode = '9_JGA0000_202111_00000012' "
    #
    # ora_tns = cx_Oracle.makedsn(ora_ip, 1521, ora_sid)
    # conn = cx_Oracle.connect(ora_user, ora_pwd, ora_tns)
    # # 操作游标
    # cursor = conn.cursor()
    # cursor.execute(SQL2)
    # number1 = cursor.fetchone()
    # print(number1)
    # print(number1[2])
    # print(type(number1[2]))
    # print(str(number1[2])[0:4])
    # print(str(number1[2])[5:7])


    # #主表插入语句
    # SQL="insert into T_BU_BUDGET (URID, TEMPLATEID, EDITLEVEL, SCHEMEID, ORGID, DEPTID, PROJECTITEMID, NOTECODE, CURRENCYID, DRAFTSBEGINBALANCE, CURRENCYBEGINBALANCE, BEGINBALANCE, TOTALREVENUE, TOTALEXPENDITURE, ENDBALANCE, UNIT, EDITSTARTCALENDARID, EDITENDCALENDARID, EDITSTARTDATE, EDITENDDATE, CONTROLSTARTCALENDARID, CONTROLENDCALENDARID, CONTROLSTARTDATE, CONTROLENDDATE, SOURCE, BUDGETSTATE, APPROVESTATE, SUBMITAPPROVEDATE, FINALAPPROVEDATE, CANCELSTATE, DESCRIPTION, CREATEDON, CREATEDBY, LASTMODIFIEDON, LASTMODIFIEDBY, ROWVERSION, TENANTID, EXPORTSTATE, EXPORTDATE, EXPORTINFO, BALANCESTATE, SUMMARYSTATE, REJECTORGID, REJECTREASON, ORGBUDGETID, VERSION, FINANCING, INVESTMENT, OPERATING, CUTAMOUNT, ISTRADE, ISCONSOLIDATE, RECDRAFT, PAYDRAFT) \
    # values (%s, '2392d7cb418a40f09debfef447496430', '1', 'cb1a44c4542342bc9928b40aa522730e', %s, null, null, %s, '1', 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, '1', 'f33adb5836ae4187b6ef0b20c410c7ea', 'ba044ebb8c39415cba560e87f1d2a7e2', to_date('02-03-2020', 'dd-mm-yyyy'), to_date('29-03-2020', 'dd-mm-yyyy'), 'f33adb5836ae4187b6ef0b20c410c7ea', 'f33adb5836ae4187b6ef0b20c410c7ea', to_date('02-03-2020', 'dd-mm-yyyy'), to_date('08-03-2020', 'dd-mm-yyyy'), '1', '1', '1', null, null, '1', null, to_date('04-11-2021 10:06:02', 'dd-mm-yyyy hh24:mi:ss'), 'Felix', to_date('04-11-2021 10:06:02', 'dd-mm-yyyy hh24:mi:ss'), 'Felix', 2, 10001, '1', null, null, '1', null, null, null, null, 1, '0.00', '0.00', '0.00', '0.00', null, null, '0.00', '0.00')"
    #
    # #子表插入语句
    # SQL1="INSERT INTO T_BU_BUDGETDETAIL(URID, BUDGETID, BUDGETITEMID, CURRENCYID, SETTLEMENTMODEID,COUNTERPARTYID, CALENDARID, STARTDATE, ENDDATE, ISCONTROL, BUDGETAMOUNT, SUREAMOUNT, ADJUSTAMOUNT, REGULATEAMOUNT, CONTROLAMOUNT, DESCRIPTION, CREATEDON, CREATEDBY, LASTMODIFIEDON, LASTMODIFIEDBY, ROWVERSION, TENANTID, EXTFIELD1, EXTFIELD2, EXTFIELD3, CLASSFICATION) \
    #     VALUES (%s, %s, '0af72347a11947a0b5e195d7375ccb9a', '1', NULL, NULL, '67019f608ab34abdbd0e2704f76168b1', TO_DATE('2021-01-11 00:00:00', 'SYYYY-MM-DD HH24:MI:SS'), TO_DATE('2021-01-17 00:00:00', 'SYYYY-MM-DD HH24:MI:SS'), '0', '0', '0', '0', '0', '0', NULL, TO_DATE('2021-11-03 18:57:21', 'SYYYY-MM-DD HH24:MI:SS'), 'Felix', TO_DATE('2021-11-03 18:57:21', 'SYYYY-MM-DD HH24:MI:SS'), 'Felix', '1', '10001', NULL, NULL, NULL, '1')"
    #
    # #测试使用的列表
    # orgid1 = [
    #     "0002483d59ff4b13a971746abdfdabcd",
    #     "0015a6a185af4d72b48691579852450e"]

    #SQL="INSERT INTO T_SY_BANKLOCATIONS (URID, CODE, NAME, BANKID, AREAID, ISACTIVE, CREATEDBY, CREATEDON, LASTMODIFIEDBY, LASTMODIFIEDON, ROWVERSION, DESCRIPTION, COUNTRYID, CNAPSTYPE, SWIFTCODE, SWIFTNAME, RTGSCODE, RTGSNAME, SOURCE) VALUES (%s, %s, %s, '104', '5101', '1', 'admin', TO_DATE('2021-11-12 16:38:14', 'SYYYY-MM-DD HH24:MI:SS'), 'admin', TO_DATE('2021-11-12 16:38:14', 'SYYYY-MM-DD HH24:MI:SS'), '1', NULL, '156', '1', 'PCBCCNBJXXX', 'CHINA CONSTRUCTION BANK', NULL, NULL, '1')"
    SQL="INSERT INTO T_SY_BANKLOCATIONS (URID, CODE, NAME, BANKID, AREAID, ISACTIVE, CREATEDBY, CREATEDON, LASTMODIFIEDBY, LASTMODIFIEDON, ROWVERSION, DESCRIPTION, COUNTRYID, CNAPSTYPE, SWIFTCODE, SWIFTNAME, RTGSCODE, RTGSNAME) VALUES (%s, %s, %s, '104', '5101', '1', 'admin', TO_DATE('2021-11-12 16:38:14', 'SYYYY-MM-DD HH24:MI:SS'), 'admin', TO_DATE('2021-11-12 16:38:14', 'SYYYY-MM-DD HH24:MI:SS'), '1', NULL, '156', '1', 'PCBCCNBJXXX', 'CHINA CONSTRUCTION BANK', NULL, NULL)"

    print("开始时间：",time.strftime("%Y-%m-%d %H:%M:%S"))

    try:
        os.remove("test.sql")
        print("test.sql,删除完毕")
    except(FileNotFoundError):
        print("test.sql,不存在")

    # doc=open('FU.sql','w')
    # doc1=open('ZI.sql','w')
    doc = open('test.sql', 'w')

    temp = time.strftime("%Y%m%d%H%M%S")
    for i in range(1,8008):

        #设置时间的变成存储
        temp = time.strftime("%Y%m%d%H%M%S")
        #生成urid的规则，给主表的字段‘URID’和‘NOTECODE’使用，给子表的字段‘URID’和‘BUDGETID’使用
        uird="'" +'lhyc'+str(temp)+str(i)+ "'"
        #print('uird内容：',uird)
        print('第%s笔,uird内容：%s' % (i, uird))

        #主表替换3个字段
        sql=SQL%(uird,uird,uird)
        ##print(sql)
        #ora_sql(ora_ip, ora_sid, ora_user, ora_pwd,sql)
        print(sql+';',file=doc)

    print('commit;', file=doc)
    #print('commit;',file=doc1)
    doc.close()
    #doc1.close()

    print("结束时间：", time.strftime("%Y-%m-%d %H:%M:%S"))



