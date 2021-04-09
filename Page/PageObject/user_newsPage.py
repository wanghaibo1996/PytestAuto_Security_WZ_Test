from Page.BasePage import BasePage
from util.parseConFile import ParseConFile


class UserNews(BasePage):
    # 配置文件读取元素
    do_conf = ParseConFile()
    UsersAndPermissionsBtn = do_conf.get_locators_or_account('UserNewsPageElements', 'UsersAndPermissionsBtn')
    UserManagementBtn = do_conf.get_locators_or_account('UserNewsPageElements', 'UserManagementBtn')
    NewsManagementBtn = do_conf.get_locators_or_account('UserNewsPageElements', 'NewsManagementBtn')
    userNames = do_conf.get_locators_or_account('UserNewsPageElements', 'userNames')


    # 创建用户
    def create_user(self):
        # 点击用户及权限管理菜单
        self.click(*UserNews.UsersAndPermissionsBtn)
        # 点击用户管理
        self.click(*UserNews.UserManagementBtn)

        # iframe跳转
        self.switch_to_iframe(0)
        self.sleep(1)


    def get_user_list(self):
        return self.get_elements_text(*UserNews.userNames)

