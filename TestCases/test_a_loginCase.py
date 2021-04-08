import pytest
from data.login_data import LoginData

# 改变输出结果
admin_login_ids = [
    "测试：{}->[用户名:{}-密码:{}-预期:{}]".
        format(data["case"], data["username"], data["password"], data["expected"]) for data in LoginData.admin_login_success_data
]
admin_fail_ids = [
    "测试：{}->[用户名:{}-密码:{}-预期:{}]".
        format(data["case"], data["username"], data["password"], data["expected"]) for data in LoginData.admin_login_fail_data
]
secrecy_login_ids = [
    "测试：{}->[用户名:{}-密码:{}-预期:{}]".
        format(data["case"], data["username"], data["password"], data["expected"]) for data in LoginData.secrecy_login_success_data
]
secrecy_fail_ids = [
    "测试：{}->[用户名:{}-密码:{}-预期:{}]".
        format(data["case"], data["username"], data["password"], data["expected"]) for data in LoginData.secrecy_login_fail_data
]
audit_login_ids = [
    "测试：{}->[用户名:{}-密码:{}-预期:{}]".
        format(data["case"], data["username"], data["password"], data["expected"]) for data in LoginData.audit_login_success_data
]
audit_fail_ids = [
    "测试：{}->[用户名:{}-密码:{}-预期:{}]".
        format(data["case"], data["username"], data["password"], data["expected"]) for data in LoginData.audit_login_fail_data
]


@pytest.mark.loginTest
class TestLogin(object):
    """登录测试"""
    login_data = LoginData

    @pytest.mark.parametrize("data", login_data.admin_login_success_data, ids=admin_login_ids)
    def test_admin_login(self, open_url, data):
        """admin用户登录测试"""
        login_page = open_url
        login_page.login(data["username"], data["password"])
        result = login_page.get_login_success_text()
        assert data["expected"] == result, "admin用户登录失败"

    @pytest.mark.parametrize('data', login_data.admin_login_fail_data, ids=admin_fail_ids)
    def test_admin_login_fail(self, open_url, data):
        """admin用户登录失败测试"""
        login_page = open_url
        login_page.login(data["username"], data["password"])
        actual = login_page.get_error_text()
        assert data["expected"] == actual, "admin用户登录成功"

    @pytest.mark.parametrize("data", login_data.secrecy_login_success_data, ids=secrecy_login_ids)
    def test_secrecy_login(self, open_url, data):
        """secrecy用户登录测试"""
        login_page = open_url
        login_page.login(data["username"], data["password"])
        result = login_page.get_login_success_text()
        assert data["expected"] == result, "secrecy用户登录失败"

    @pytest.mark.parametrize('data', login_data.secrecy_login_fail_data, ids=secrecy_fail_ids)
    def test_secrecy_login_fail(self, open_url, data):
        """secrecy用户登录失败测试"""
        login_page = open_url
        login_page.login(data["username"], data["password"])
        actual = login_page.get_error_text()
        assert data["expected"] == actual, "secrecy用户登录成功"

    @pytest.mark.parametrize("data", login_data.audit_login_success_data, ids=audit_login_ids)
    def test_audit_login(self, open_url, data):
        """audit用户登录测试"""
        login_page = open_url
        login_page.login(data["username"], data["password"])
        result = login_page.get_login_success_text()
        assert data["expected"] == result, "audit用户登录失败"

    @pytest.mark.parametrize('data', login_data.audit_login_fail_data, ids=audit_fail_ids)
    def test_audit_login_fail(self, open_url, data):
        """audit用户登录失败测试"""
        login_page = open_url
        login_page.login(data["username"], data["password"])
        actual = login_page.get_error_text()
        assert data["expected"] == actual, "audit用户登录成功"


if __name__ == "__main__":
    pytest.main()
