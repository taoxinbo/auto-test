import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)),".."))
from Action.Calendar import *
from Config.VarConfig import *
def make_dir(dir_path):
    if not os.path.exists(dir_path):
        try:
            os.mkdir(dir_path)
        except Exception as e:
            print("创建%s目录失败" %dir_path)
            raise e

def make_current_date_dir(default_dir_path = None):# 'default_dir_path = None’的意思：在函数中对于参数 可以传 也可以 不传。
    if default_dir_path is None:
        dir_path = get_current_date()
    else:
        dir_path = os.path.join(default_dir_path,get_current_date())
    if not os.path.exists(dir_path):
        try:
            os.mkdir(dir_path)
        except Exception as e:
            print("创建%s目录失败" % dir_path)
            raise e
    return dir_path

def make_current_hour_dir(default_dir_path = None):
    if default_dir_path is None:
        dir_path = get_current_hour()
    else:
        dir_path = os.path.join(default_dir_path,get_current_hour())
    if not os.path.exists(dir_path):
        try:
            os.mkdir(dir_path)
        except Exception as e:
            print("创建%s目录失败" % dir_path)
            raise e
    return dir_path

if __name__ == "__main__":
    make_dir(parentDirPath+"\\"+"ScreenCapture\\"+"pic")
    dir_path = make_current_date_dir(parentDirPath+"\\"+"ScreenCapture\\")
    dir_path=make_current_hour_dir(dir_path+"\\")
    print(dir_path)
