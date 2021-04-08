import pytest
from data.tactical_management_data import TacticalManagementData


client_address_ids = [
    "测试：{}->[预期:{}]".
        format(data["case"], data["expected"]) for data in TacticalManagementData.add_client_address_data
]


@pytest.mark.TacticalManagement
class TestTacticalManagement(object):
    """策略管理"""
    tactical_data = TacticalManagementData

    @pytest.mark.parametrize("data", tactical_data.add_client_address_data, ids=client_address_ids)
    def test_add_client_address_tactical(self, secrecy_login, ini_pages_secrecy, data):
        """创建客户端地址策略集"""
        add_client_address_tactical = ini_pages_secrecy[2]
        add_client_address_tactical.add_client_address_tactical()
        # result = add_client_address_tactical.get_user_list()
        assert data["expected"] is not None, "admin创建用户失败"






















