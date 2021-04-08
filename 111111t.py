from audioop import reverse

from Page.BasePage import BasePage
from Page.PageObject.LoginPage import LoginPage


# a = ["a", "b", "cds" ]
# b = ["a", "b", "cds", None ]
# upload_file_data = {
#         "case": "上传多个类型文件",
#
#         "expected": ['保存的分享', '撒旦.wav', '我爱你中国.wmv', '做我老婆好不好.mp3', '三步走做好年终报告PPT.pptx', 'Uninstall.xml',
#                      'test部门成员.xls', 'sho.3gb', 'sdasdas11111.doc', 'QQ视频.mp4', 'my.conf', 'mv.avi', 'hhh.ini',
#                      'G.jpeg', 'dfsdf.mov', 'chrome.exe', 'che.rmvb', '55555555.docx', '2323.png', '2019_PDF.pdf',
#                      '222.bat', '123.zip', '123.gif', '121.rar', '12 SWEET.m4a', '2.jpg', '1kb00.txt']
#     }



# print(upload_file_data["expected"])
# c = ['保存的分享', '撒旦.wav', '我爱你中国.wmv', '做我老婆好不好.mp3', '三步走做好年终报告PPT.pptx', 'Uninstall.xml', 'test部门成员.xls', 'sho.3gb', 'sdasdas11111.doc', 'QQ视频.mp4', 'my.conf', 'mv.avi', 'hhh.ini', 'G.jpeg', 'dfsdf.mov', 'chrome.exe', 'che.rmvb', '55555555.docx', '2323.png', '2019_PDF.pdf', '222.bat', '123.zip', '123.gif', '121.rar', '12 SWEET.m4a', '2.jpg', '1kb00.txt']

# class FHJJJJ(LoginPage):
#
#
#
#     def isElementExist(self):
#         self.login("admin", "admin2003")
#         flag = True
#         try:
#             self.driver.find_element_by_css_selector("//body/div[8]/h2")
#             return flag
#
#         except:
#             flag = False
#             return flag
#
# FHJJJJ().isElementExist()

# a = ['保存的分享', '撒旦.wav', '我爱你中国.wmv', '做我老婆好不好.mp3', '三步走做好年终报告PPT.pptx', 'Uninstall.xml', 'test部门成员.xls', 'sho.3gb', 'sdasdas11111.doc', 'QQ视频.mp4', 'my.conf', 'mv.avi', 'hhh.ini', 'G.jpeg', 'dfsdf.mov', 'chrome.exe', 'che.rmvb', '55555555.docx', '2323.png', '2019_PDF.pdf', '222.bat', '123.zip', '123.gif', '121.rar', '12 SWEET.m4a', '2.jpg', '1kb00.txt']
#
# b = list(reversed(a))
# print(b)
# from selenium import webdriver
# import time
# from selenium.webdriver.support import expected_conditions as EC
# dr = webdriver.Chrome()
#
# dr.get("https://192.168.0.67")
# dr.find_element_by_xpath("//*[@id='user']").send_keys("admin")
# dr.find_element_by_xpath('//*[@id="password"]').send_keys("admin2003")
# dr.find_element_by_xpath('//*[@id="submit"]').click()
# time.sleep(3)
# # dr.find_element_by_xpath("//tr[2]/td/label").click()
# # time.sleep(3)
# # name = dr.find_element_by_xpath("//tr[2]").get_attribute("class")
# # data = EC.element_to_be_selected("//tr[2]/td/label")
# url = dr.current_url
# print(url)
# dr.quit()
# print(name)
# import os
#
#
# name = os.listdir("E:/testDownload")
# print(name)
# a = ["7 个文件夹 和 23 个文件"]
# assert a[0]  in ["7 个文件夹 和 23 个文件 (包括 1 个隐藏文件)"][0], "11"

import os
import shutil
# os.remove(path)  # 删除文件
# os.removedirs(path)  # 删除空文件夹
# shutil.rmtree(r"E:\受到收到的")  # 递归删除文件夹
# 得到进程当前工作目录
# currentpath = os.getcwd()
# 将当前工作目录修改为待修改文件夹的位置
# os.chdir(r"E:\testDownload")
# os.rename("hahha.hon","config.conf", )
# print(os.listdir(r"E:\testDownload"))

# a = os.path.realpath("config.conf")
# print(a)

# a = 1
#
# while a <= 17:
#     c = ["file_path" + str(a)]
#     b = "data" + str(c)
#     with open(r'E:\PytestAuto_Security_WP_Test\TestCases\1.txt', 'a') as f:
#         f.write(b + ',')
#     a += 1

# def my_function():
#     """这个没啥用"""
#
#     return None
#
#
#
# print(my_function.__doc__)

# print("Using help:")
# help(my_function)

# 装饰器
import functools


# def func(fu):
#
#     def func1(a):
#         if a == 1:
#             print("验证")
#         else:
#             print("cuowu ")
#         fu(a)
#
#     return func1
#
# @func
# def func2(a):
#     print("wancheng")
#
#
# func2(1)

# def func(fu):
#
#     def func1(a, b):
#         if a == 1:
#             print("验证")
#         else:
#             print("cuowu ")
#         fu(a,b)
#
#     return func1
#
# @func
# def func2(a, b):
#     n = a + b
#     print("wancheng")
#     print(n)
#
#
# func2(2, 3)


# class Test():
#     xx = False
#
#
#     def test(func):
#         def wrapper(self, *args, **kwargs):
#             print(self.xx)
#             return func(self, *args, **kwargs)
#
#         return wrapper
#
#     @test
#     def test_a(self, a, b):
#         print(f'ok,{a} {b}')
#
# Test().test_a(1,2)

# import re
# d = "11 个文件夹 和 29 个文件"
#
# a = re.findall("\d+", "11 个文件夹 和 29 个文件" )
# print(a)
# b = int(a[0]) + int(a[1])
# print(b)
# b = re.match()

# testreport = r"E:\PytestAuto_Security_WP_Test\report"
# lists = os.listdir(testreport)
# lists.sort(key=lambda fn: os.path.getmtime(testreport + "\\" + fn))
# file_new = os.path.join(testreport, lists[-1])
# print(file_new)


# def main():
#     fin = open(r'E:\PytestAuto_Security_WP_Test\report\金电网安文件管理系统自动化测试报告14_57.html', 'r', encoding='utf-8')
#     fout = open('b.html', 'w', encoding='utf-8')
#     with open("./report/assets/style.css", 'r') as f:
#         text = f.read()
#     print(text)
#     for line in fin:
#         if line.strip() == '<head>':
#             fout.write("<style>\n" + text + "\n</style>")
#         fout.write(line)
#
# if __name__ == '__main__':
#   main()



# file_list = os.listdir(r"E:\testDownload")
# print(file_list)
# a_name = "my.conf"
# for i in file_list:
#     if i != a_name:
#         os.remove(r"E:\testDownload\\" + i)



"""排列组合"""
from itertools import combinations,permutations


a=["开始时间", "结束时间", "数据库关联ID", "同步方向", "同步表名称", "事件类型", "结果状态"]



c = list(combinations(a,7)) # 每一种没有重复的

# d = list(permutations(a,3)) # 有重复的数据,但顺序不同


for i in c:

    print(i[0] + ", " + i[1] + ", " + i[2] + ", " + i[3] + ", " + i[4] + ", " + i[5] + ", " + i[6])





