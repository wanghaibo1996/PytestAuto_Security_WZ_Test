import pytest
from data.user_news_data import UserNewsData

# 改变输出结果
create_user_ids = [
    "测试：{}->[用户名:{}-密码:{}-预期:{}]".
        format(data["case"], data["username"], data["password"], data["expected"]) for data in UserNewsData.create_user_data
]


@pytest.mark.CreateUserTest
class TestCreateUser(object):
    """用户管理，菜单管理"""
    create_data = UserNewsData

    @pytest.mark.parametrize("data", create_data.create_user_data, ids=create_user_ids)
    def test_admin_create_user(self, admin_login, ini_pages_admin, data):
        """admin创建用户"""
        create_page = ini_pages_admin[2]
        create_page.create_user()
        result = create_page.get_user_list()
        assert data["expected"] in result, "admin创建用户失败"

    @pytest.mark.parametrize("data", create_data.create_user_data, ids=create_user_ids)
    def test_audit_create_user(self, audit_login, ini_pages_audit, data):
        """audit创建用户"""
        create_page = audit_login[2]
        create_page.create_user()
        result = create_page.get_user_list()
        assert data["expected"] in result, "audit创建用户失败"

























