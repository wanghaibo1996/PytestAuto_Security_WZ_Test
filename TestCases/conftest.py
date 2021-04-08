import pytest
from util.parseConFile import ParseConFile
from Page.PageObject.LoginPage import LoginPage
from Page.PageObject.user_newsPage import UserNews
from Page.PageObject.Tactical_ManagementPage import TacticalManagement


do_conf = ParseConFile()
# 从配置文件中获取正确的用户名和密码
admin_name = do_conf.get_locators_or_account('LoginAccount', 'admin_name')
admin_pwd = do_conf.get_locators_or_account('LoginAccount', 'admin_pwd')
secrecy_name = do_conf.get_locators_or_account('LoginAccount', 'secrecy_name')
secrecy_pwd = do_conf.get_locators_or_account('LoginAccount', 'secrecy_pwd')
audit_name = do_conf.get_locators_or_account('LoginAccount', 'audit_name')
audit_pwd = do_conf.get_locators_or_account('LoginAccount', 'audit_pwd')


# @pytest.fixture(scope='function')
# def login(driver):
#     """除登录用例，每一个用例的前置条件"""
#     print('------------staring login------------')
#     login_action = LoginPage(driver, 30)
#     login_action.login(userName, passWord)
#     yield
#     print('------------end login------------')
#     driver.delete_all_cookies()




@pytest.fixture(scope='function')
def open_url(ini_pages):
    driver = ini_pages[0]
    login_page = ini_pages[1]
    yield login_page
    driver.delete_all_cookies()


# admin用户
@pytest.fixture(scope='class')
def ini_pages_admin(driver):
    login_page = LoginPage(driver)
    create_page = UserNews(driver)
    yield driver, login_page, create_page

@pytest.fixture(scope='class')
def admin_login(ini_pages_admin):
    driver, login_page, create_page = ini_pages_admin
    login_page.login(admin_name, admin_pwd)
    yield login_page, create_page
    driver.delete_all_cookies()


# secrecy用户
@pytest.fixture(scope='class')
def ini_pages_secrecy(driver):
    login_page = LoginPage(driver)
    tactical_management_page = TacticalManagement(driver)
    yield driver, login_page, tactical_management_page

@pytest.fixture(scope='class')
def secrecy_login(ini_pages_secrecy):
    driver, login_page, tactical_management_page = ini_pages_secrecy
    login_page.login(secrecy_name, secrecy_pwd)
    yield login_page, tactical_management_page
    driver.delete_all_cookies()


# audit用户
@pytest.fixture(scope='class')
def ini_pages_audit(driver):
    login_page = LoginPage(driver)
    create_page = create_page(driver)
    yield driver, login_page, create_page

@pytest.fixture(scope='class')
def audit_login(ini_pages_audit):
    driver, login_page, create_page = ini_pages_audit
    login_page.login(audit_name, audit_pwd)
    yield login_page, create_page
    driver.delete_all_cookies()


@pytest.fixture(scope='function')
def refresh_page(ini_pages):
    driver = ini_pages[0]
    yield
    driver.refresh()

