# encoding=utf-8
import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))
# 导入模拟组合按键需要的包 pip install pywin32 这个包安装有点慢
import win32api
import win32con
import time
import cx_Oracle
import pymysql
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from Action.Log import *
from Config.VarConfig import *
from Action.Calendar import *
from Action.find import *
import zipfile
#导入上传附件模块
from pymouse import PyMouse
from pykeyboard import PyKeyboard

VK_CODE = {'enter': 0x0D, 'ctrl': 0x11, 'a': 0x41, 'v': 0x56, 'x': 0x58, 't': 0x54, 'tab': 0x09}


# 键盘键按下
def keyDown(keyName):
    win32api.keybd_event(VK_CODE[keyName], 0, 0, 0)


# 键盘键抬起
def keyUp(keyName):
    win32api.keybd_event(VK_CODE[keyName], 0, win32con.KEYEVENTF_KEYUP, 0)


# 封装的按键方法
def simulateKey(firstKey, secondKey):
    keyDown(firstKey)
    keyDown(secondKey)
    keyUp(secondKey)
    keyUp(firstKey)


# 封装启动浏览器的驱动
def get(browser_type):
    global driver
    if browser_type =="chrome":
        driver = webdriver.Chrome(executable_path = "e:\\chromedriver")
    elif browser_type =="ie":
        driver = webdriver.Ie(executable_path = "e:\\IEDriverServer")
    else:
        driver = webdriver.Firefox(executable_path = "e:\\geckodriver")
    logging.info("启动浏览器")
    driver.maximize_window()
    print("浏览器打开，并且最大化")
    # time.sleep(3)
    return driver


# 封装登陆的方法--excel用
def login_xlsx(username, password, tenant):
    global driver
    # 用户名
    user_name = driver.find_element_by_xpath("//input[@placeholder='请输入用户名']")
    #  清空用户名
    user_name.clear()
    #  输入用户名
    user_name.send_keys(username)
    sleep(1)


    # 选择租户
    if username not in L1:
        ten_id = driver.find_element_by_xpath("//input[@id='combobox-input-tenantid']")
        ten_id.click()
        ten_id.clear()
        time.sleep(1)
        ten_id.send_keys(tenant)
        time.sleep(2)
        ten_id.send_keys(Keys.ARROW_DOWN)
        ten_id.send_keys(Keys.ENTER)
        time.sleep(1)
        # click("xpath","//input[@id='combobox-input-tenantid']")
        # clear("xpath","//input[@id='combobox-input-tenantid']")
        # input("xpath","//input[@id='combobox-input-tenantid']",tenant)
        # input_down("xpath","//input[@id='combobox-input-tenantid']")
        # input_enter("xpath","//input[@id='combobox-input-tenantid']")

        # 模拟回车键
        # keyDown('enter')
        # keyUp('enter')

    # 通过JavaScript代码点击首页上的登陆按钮
    # searchButtonJS = "document.getElementById('loing_btntext').click()"
    # driver.execute_script(searchButtonJS)
    # time.sleep(1)

    # 密码
    pass_wd = driver.find_element_by_xpath("//input[@placeholder='请输入密码']")
    pass_wd.send_keys(password)

    #js_click("xpath", "//span[@id='loing_btntext']")
    click("xpath", "//span[@id='loing_btntext']")

    # 用隐式等待方法等页面页面出现'退出'按钮，说明登陆成功
    # driver.implicitly_wait(60)
    # driver.find_element_by_xpath("//a[contains(text(),'退出')]")
    implici_wait("xpath", "//a[contains(text(),'退出')]")
    logging.info("柜员：" + username + "登录成功！")
    print("柜员：" + username + "登录成功！")


# 封装登陆的方法--非excel用
def login(url, username, password, tenant):
    global driver
    # 输入测试环境
    driver.get(url)
    logging.info("打开测试地址:" + url)
    print("打开测试地址:" + url)

    # 用户名
    user_name = driver.find_element_by_xpath("//input[@placeholder='请输入用户名']")
    #  清空用户名
    user_name.clear()
    #  输入用户名
    user_name.send_keys(username)
    sleep(1)

    # 选择租户
    if username not in L1:
        ten_id = driver.find_element_by_xpath("//input[@id='combobox-input-tenantid']")
        ten_id.click()
        ten_id.clear()
        time.sleep(1)
        ten_id.send_keys(tenant)
        time.sleep(2)
        ten_id.send_keys(Keys.ARROW_DOWN)
        ten_id.send_keys(Keys.ENTER)
        time.sleep(1)
        # click("xpath", "//input[@id='combobox-input-tenantid']")
        # clear("xpath", "//input[@id='combobox-input-tenantid']")
        # input("xpath", "//input[@id='combobox-input-tenantid']", tenant)
        # input_down("xpath", "//input[@id='combobox-input-tenantid']")
        # input_enter("xpath", "//input[@id='combobox-input-tenantid']")

        # 模拟回车键
        # keyDown('enter')
        # keyUp('enter')

    # 通过JavaScript代码点击首页上的登陆按钮
    # searchButtonJS = "document.getElementById('loing_btntext').click()"
    # driver.execute_script(searchButtonJS)

    # 密码
    pass_wd = driver.find_element_by_xpath("//input[@placeholder='请输入密码']")
    pass_wd.send_keys(password)

    #time.sleep(2)
    #js_click("xpath", "//span[@id='loing_btntext']")
    click("xpath", "//span[@id='loing_btntext']")
    #sleep(1)
    # 用隐式等待方法等页面页面出现'退出'按钮，说明登陆成功
    # driver.implicitly_wait(60)
    # driver.find_element_by_xpath("//a[contains(text(),'退出')]")
    implici_wait("xpath", "//a[contains(text(),'退出')]")
    logging.info("柜员：" + username + "登录成功！")
    print("柜员：" + username + "登录成功！")


def login2(url, username, password):
    global driver
    # 输入测试环境
    driver.get(url)
    logging.info("打开测试地址:" + url)
    print("打开测试地址:" + url)

    # 用户名
    user_name = driver.find_element_by_xpath("//input[@placeholder='请输入用户名']")
    #  清空用户名
    user_name.clear()
    #  输入用户名
    user_name.send_keys(username)

    # 密码
    pass_wd = driver.find_element_by_xpath("//input[@placeholder='请输入密码']")
    pass_wd.send_keys(password)

    click("xpath", "//span[@id='loing_btntext']")
    sleep(1)
    # 用隐式等待方法等页面页面出现'退出'按钮，说明登陆成功
    implici_wait("xpath", "//a[contains(text(),'退出')]")
    logging.info("柜员：" + username + "登录成功！")
    print("柜员：" + username + "登录成功！")


# 输入网址
def visit(url):
    global driver
    driver.get(url)
    logging.info("打开测试地址:" + url)
    print("打开测试地址:" + url)


# 暂停
def sleep(times):
    try:
        time.sleep(int(times))
    except Exception as e:
        raise e


# 在框中输入值
def input(locator_method, locator_exp, content):
    global driver
    try:
        element = getElement(driver, locator_method, locator_exp)
        element.send_keys(content)
    except Exception as e:
        raise e


# 点击页面元素
def click(locator_method, locator_exp):
    global driver
    try:
        element = getElement(driver, locator_method, locator_exp)
        element.click()
    except Exception as e:
        raise e


# 点击页面元素含有span标签的
def span_click(x):
    path = "//span[text()='" + x + "']"
    click("xpath", path)
    sleep(1)


# 点击页面元素含有倒三角的
def triangle_cick(x):
    path = "//span[text()='" + x + "']/parent::*/following-sibling::*/child::*"
    click("xpath", path)
    sleep(1)


# 点击页面元素含有倒三角的,以及下拉框的内容
def triangle_cick_and_element(x, y):
    path = "//span[text()='" + x + "']/parent::*/following-sibling::*/child::*"
    path2 = "//a[contains(text(),'" + y + "')]"
    click("xpath", path)
    sleep(1)
    click("xpath", path2)
    sleep(1)


# 点击页面元素跳出来的ok
def ok_click():
    click("xpath", "//button[@id='f-message-webgen-0-okBnt']")
    sleep(1)


# 输入框，向下回车
def up_enter_click(x):
    input_down("xpath", x)
    sleep(1)
    input_enter("xpath", x)
    sleep(1)


# 输入框，输入内容，选择第一条数据
def input_up_click(x, y):
    clear("xpath", x)
    sleep(1)
    input("xpath", x, y)
    sleep(1)
    up_enter_click(x)


# 输入框，点击，选择第一条数据
def click_up_click(x):
    click("xpath", x)
    sleep(1)
    up_enter_click(x)


# 切换组织
def choose_organization(x):
    refresh()
    sleep(1)
    js_click("xpath", "//input[@id='combobox-input-orgidswitch']")
    sleep(1)
    clear("xpath", "//input[@id='combobox-input-orgidswitch']")
    sleep(1)
    input("xpath", "//input[@id='combobox-input-orgidswitch']", x)
    sleep(1)
    input_down("xpath", "//in"
                        "put[@id='combobox-input-orgidswitch']")
    input_enter("xpath", "//input[@id='combobox-input-orgidswitch']")
    sleep(3)


# 清空元素框里的内容
def clear(locator_method, locator_exp):
    global driver
    try:
        element = getElement(driver, locator_method, locator_exp)
        element.clear()
    except Exception as e:
        raise e


# 点开框中的内容，键盘往下
def input_down(locator_method, locator_exp):
    global driver
    try:
        element = getElement(driver, locator_method, locator_exp)
        element.send_keys(Keys.ARROW_DOWN)
    except Exception as e:
        raise e


# 点开框中的内容，选中框中的值
def input_enter(locator_method, locator_exp):
    global driver
    try:
        element = getElement(driver, locator_method, locator_exp)
        element.send_keys(Keys.ENTER)
    except Exception as e:
        raise e


# 定义关键字方法1
def assert_word(content):
    global driver
    try:
        assert content in driver.page_source
    except AssertionError as e:
        raise e


# 定义关键字方法2
def assert_keyword(locator_method, locator_exp, keyword):
    global driver
    try:
        element = getElement(driver, locator_method, locator_exp)
        print(element.get_attribute('textContent'))
        assert keyword in element.get_attribute('textContent')
    except Exception as e:
        raise e


# 切入系统设置的iframe窗体
def switch_to(locator_method,locator_exp):
    global driver
    try:
        driver.switch_to.frame(getElement(driver, locator_method, locator_exp))
    except Exception as e:
        raise e


# 退出所有iframe窗体
def switch_default():
    global driver
    try:
        driver.switch_to.default_content()
    except Exception as e:
        raise e


# 退出当前的iframe窗体
def switch_parent():
    global driver
    try:
        driver.switch_to.parent_frame()
    except Exception as e:
        raise e


# 用JS的方法点击
def js_click(locator_method, locator_exp):
    global driver
    try:
        button = getElement(driver, locator_method, locator_exp)
        driver.execute_script("$(arguments[0]).click()", button)
    except Exception as e:
        raise e


# 用JS的方法滚动到那个元素可见
def js_gd(locator_method, locator_exp):
    global driver
    try:
        button = getElement(driver, locator_method, locator_exp)
        driver.execute_script("arguments[0].scrollIntoView();", button)
    except Exception as e:
        raise e


# 用隐式等待方法等页面出现提示框
def implici_wait(locator_method, locator_exp):
    global driver
    try:
        driver.implicitly_wait(60)
        getElement(driver, locator_method, locator_exp)
    except Exception as e:
        raise e


# 关闭浏览器
def quit():
    global driver
    try:
        driver.quit()
    except Exception as e:
        raise e


# 封装截屏函数
def capture(file_path):
    global driver
    try:
        driver.save_screenshot(file_path)
    except Exception as e:
        raise e


# 封装压缩文件夹的方法
def zipDir(dirpath, outFullName):
    """
    压缩指定文件夹
    :param dirpath: 目标文件夹路径
    :param outFullName: 压缩文件保存路径+xxxx.zip
    :return: 无
    """
    zip = zipfile.ZipFile(outFullName, "w", zipfile.ZIP_DEFLATED)
    for path, dirnames, filenames in os.walk(dirpath):
        # 去掉目标跟路径，只对目标文件夹下边的文件及文件夹进行压缩
        fpath = path.replace(dirpath, '')

        for filename in filenames:
            zip.write(os.path.join(path, filename), os.path.join(fpath, filename))
    zip.close()


# 双击页面元素
def double_click(locator_method, locator_exp):
    global driver
    try:
        element = getElement(driver, locator_method, locator_exp)
        # 导入支持双击操作的模块
        from selenium.webdriver import ActionChains
        # 开始模拟鼠标双击操作
        action_chains = ActionChains(driver)
        action_chains.double_click(element).perform()
    except Exception as e:
        raise e


# 刷新当前整个页面，等同于F5功能
def refresh():
    global driver
    try:
        driver.refresh()
    except Exception as e:
        raise e


# 上传附件
def upload_click(locator_method, locator_exp, file, dir):  # locator_method:元素定位方法，locator_exp：元素定位路径，file：盘符所在位置，dir：文件名
    global driver
    try:
        kk = PyKeyboard()
        click(locator_method, locator_exp)  # 点击你的上传文件元素位置
        sleep(1)
        kk.tap_key(kk.shift_key)  # 切换为英文，看实际情况是否需要
        sleep(1)
        kk.type_string(file)  # 打开文件所在目录，方便多个文件上传
        sleep(1)
        kk.tap_key(kk.enter_key)
        sleep(1)
        kk.type_string(dir)  # 可以多文件上传
        sleep(1)
        kk.tap_key(kk.enter_key)
        sleep(1)
    except Exception as e:
        raise e


# 封装修改数据库函数把支付状态是'支付失败'改为'收付结果无法识别'
def fun_update(ora_ip, ora_sid, ora_user, ora_pwd):
    # 创建数据库连接,配置监听并连接
    # cx_Oracle.connect('username','pwd','ora的tns信息')
    # oracle数据库的tns信息，从tnsnames.ora中找到plsql可用的配置项，将该配置项直接拷贝过来即可
    ora_tns = cx_Oracle.makedsn(ora_ip, 1521, ora_sid)
    conn = cx_Oracle.connect(ora_user, ora_pwd, ora_tns)
    # 操作游标
    cursor = conn.cursor()
    # 更新语句
	
    cursor.execute( "update T_SE_PAYMENTS a set a.paystate='7' where  a.oppbankaccountname='张三' and a.createdby='test001' and a.paystate='5'")
    # 执行查询
    # cursor.execute("select a.paystate,a.cancelstate,a.* from T_SE_PAYMENTS a where  a.oppbankaccountname='张三' and a.createdby='test001' and a.paystate='7'and a.cancelstate='1'")
    # 查询一条数据
    # print( cursor.fetchall())
    # 关闭游标
    cursor.close()
    # 提交事务
    conn.commit()
    # 关闭数据库连接
    conn.close()


# 对Oracle数据库进行update、install、delete的封装
def ora_sql(ora_ip, ora_sid, ora_user, ora_pwd, sql):
    # 创建数据库连接,配置监听并连接
    # cx_Oracle.connect('username','pwd','ora的tns信息')
    # oracle数据库的tns信息，从tnsnames.ora中找到plsql可用的配置项，将该配置项直接拷贝过来即可
    ora_tns = cx_Oracle.makedsn(ora_ip, 1521, ora_sid)
    conn = cx_Oracle.connect(ora_user, ora_pwd, ora_tns)
    # 操作游标
    cursor = conn.cursor()
    # 执行语句
    cursor.execute(sql)
    # 执行查询
    # cursor.execute("select a.paystate,a.cancelstate,a.* from T_SE_PAYMENTS a where  a.oppbankaccountname='张三' and a.createdby='test001' and a.paystate='7'and a.cancelstate='1'")
    # 查询一条数据
    # print( cursor.fetchall())
    # 关闭游标
    cursor.close()
    # 提交事务
    conn.commit()
    # 关闭数据库连接
    conn.close()


# 对mysql数据库进行update、install、delete的封装
def my_sql(my_host, my_port, my_user, my_passwd, my_db, sql):
    conn = pymysql.connect(host=my_host, port=my_port, user=my_user, passwd=my_passwd, db=my_db, charset="utf8")
    # 使用cursor()方法获取数据库的操作游标
    cursor = conn.cursor()
    # 执行语句
    cursor.execute(sql)
    # 关闭游标
    cursor.close()
    # 提交事务
    conn.commit()
    # 关闭数据库连接
    conn.close()

#if __name__ == '__main__':
#     # get("chrome")
#     #capture(parentDirPath + "\\ScreenCapture\\" + get_current_time() + ".png")
#     #zipDir(parentDirPath + "\\ScreenCapture", parentDirPath + "\\" + "ScreenCapture.zip")
#     my_sql(my_host, my_port, my_user, my_passwd, my_db, "update test a set a.name='张33' where a.name='张三'")

