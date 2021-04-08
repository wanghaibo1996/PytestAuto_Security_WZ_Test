import sys
from email.mime.multipart import MIMEMultipart

import pytest
from config.conf import *
from email.mime.text import MIMEText
from email.header import Header
import smtplib
import os


"""

"""

def main():
    if ROOT_DIR not in sys.path:
        sys.path.append(ROOT_DIR)
    # 执行用例
    args = ['--reruns', '0', '--html=' + './report/' + HTML_NAME]
    # print(args)
    pytest.main(args)

    # 将生成的results放到jenkins中的项目中
    # args = ['--reruns', '1', '--html=' + './report/' + HTML_NAME, '-s', '-q', '--alluredir=D:/Jenkins/workspace/网盘web端/target/allure-results']
    # args = ['-s', '-q', '--alluredir=D:/Jenkins/workspace/网盘web端/target/allure-results']
    # print(args)
    # pytest.main(args)
    # 生成allure报告
    # os.system(
    #     "allure generate D:/Jenkins/workspace/网盘web端/target/allure-results -o --clean-alluredir D:/Jenkins/workspace/网盘web端/target/allure-report/html ")

    # # 删除生成的
    # file_a_path = "./report/a.html"
    # if os.path.exists(file_a_path):  # 如果文件存在
    #     # 删除文件
    #     os.remove(file_a_path)
    #
    # # 获取最新的测试报告
    # testreport = "./report"
    # lists = os.listdir(testreport)
    # lists.sort(key=lambda fn: os.path.getmtime(testreport + "\\" + fn))
    # file_new = os.path.join(testreport, lists[-1])
    # #
    # # 将样式写入报告中
    # # 原报告
    # fin = open(file_new, 'r', encoding='utf-8')
    # # 加入样式的生成的新报告
    # fout = open('./report/金电网安文件管理系统4.5.8自动化测试报告.html', 'w', encoding='utf-8')
    # # 样式css读出
    # with open("./report/assets/style.css", 'r', encoding='utf-8') as f:
    #     text = f.read()
    # # 写入到<head>标签
    # for line in fin:
    #     if line.strip() == '<head>':
    #         fout.write("<style>\n" + text + "\n</style>")
    #     fout.write(line)
    #
    # # 获取修改的测试报告
    # testreport = "./report"
    # lists = os.listdir(testreport)
    # lists.sort(key=lambda fn: os.path.getmtime(testreport + "\\" + fn))
    # file_new = os.path.join(testreport, lists[-1])
    #
    # # 收信方邮箱（因为是发送给多个人，所以我们可以用列表进行储存）
    # to_addrs = ['wanghb@goldensecurity.com.cn',]
    # # a = ['liuxiao@goldensecurity.com.cn', "huep@goldensecurity.com.cn"]
    #
    # # 读取html
    # f = open(file_new, 'rb')
    # mail_body = f.read()
    # f.close()
    #
    # # 构造html附件
    # msg = MIMEText(mail_body, 'html', 'utf-8')
    # msg['Subject'] = Header("网盘自动化测试报告", 'utf-8')
    # msg["Content-Type"] = 'application/octet-stream'
    # msg["Content-Disposition"] = 'attachment; filename="report.html"'
    #
    # # 创建一个带附件的邮件实例
    # message = MIMEMultipart()
    # message.attach(msg)
    #
    #
    # # 发送邮件
    # try:
    #     smtp = smtplib.SMTP()
    #     smtp.connect("smtp.goldensecurity.com.cn")
    #     smtp.login("wanghb@goldensecurity.com.cn", "Whb123456")
    #     smtp.sendmail("wanghb@goldensecurity.com.cn", to_addrs, msg.as_string())
    #     smtp.quit()
    #     print('email has send success!')
    # except smtplib.SMTPException:
    #     print("Error: 无法发送邮件")



if __name__ == '__main__':
    main()
