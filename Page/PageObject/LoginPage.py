from Page.BasePage import BasePage
from util.parseConFile import ParseConFile


class LoginPage(BasePage):
    # 配置文件读取元素
    do_conf = ParseConFile()
    # 用户名输入框
    username = do_conf.get_locators_or_account('LoginPageElements', 'username')
    # 密码输入框
    password = do_conf.get_locators_or_account('LoginPageElements', 'password')
    # 登录按钮
    loginBtn = do_conf.get_locators_or_account('LoginPageElements', 'loginBtn')
    # 登录失败的提示信息
    loginFailMsg = do_conf.get_locators_or_account('LoginPageElements', 'loginFailMsg')
    # 登录成功后的显示元素
    fileText = do_conf.get_locators_or_account('HomePageElements', 'fileText')
    # error_head = do_conf.get_locators_or_account('LoginPageElements', 'errorHead')

    def login(self, username, password):
        """用户登录流程"""
        self.open_url()
        self.sleep(1)
        self.input_username(username)
        self.input_password(password)
        self.click_login_btn()
        self.sleep(0.5)
        # 如果没有登录成功，就重新登录
        # if self.find_element(*LoginPage.fileText):
        #     pass
        # else:
        #     self.input_username(username)
        #     self.input_password(password)
        #     self.click_login_btn()

    def open_url(self):
        return self.load_url('http://192.168.0.28')

    def clear_username(self):
        return self.clear(*LoginPage.username)

    def input_username(self, username):
        self.clear_username()
        return self.send_keys(*LoginPage.username, username)

    def clear_password(self):
        return self.clear(*LoginPage.password)

    def input_password(self, password):
        self.clear_password()
        return self.send_keys(*LoginPage.password, password)

    def click_login_btn(self):
        return self.click(*LoginPage.loginBtn)

    def get_error_text(self):
        return self.get_element_text(*LoginPage.loginFailMsg)

    def get_login_success_text(self):
        return self.get_element_text(*LoginPage.fileText)



if __name__ == "__main__":
    pass
