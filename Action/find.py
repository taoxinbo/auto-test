#encoding=utf-8
import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)),".."))
from selenium.webdriver.support.ui import WebDriverWait

# 获取单个页面元素对象
def getElement(driver, locationType, locatorExpression):
    try:
        element = WebDriverWait(driver, 60).until\
            (lambda x: x.find_element(by=locationType, value = locatorExpression))
        return element
    except Exception as err:
        raise err

# 获取多个相同页面元素对象，以list返回
def getElements(driver, locationType, locatorExpression):
    try:
        elements = WebDriverWait(driver, 60).until\
            (lambda x:x.find_elements(by=locationType, value = locatorExpression))
        return elements
    except Exception as err:
        raise err

if __name__ == '__main__':
    from selenium import webdriver
    # 进行单元测试
    driver = webdriver.Chrome(executable_path="e:\\chromedriver")
    driver.get("http://www.baidu.com")
    searchBox = getElement(driver, "id", "kw")
    # 打印页面对象的标签名
    print(searchBox.tag_name)
    aList = getElements(driver, "tag name", "a")
    # for i in aList:
    #     print(i.get_attribute('textContent'))
    print(aList[4].get_attribute('textContent'))
    print(len(aList))
    driver.quit()