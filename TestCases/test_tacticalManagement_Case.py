import pytest
from data.tactical_management_data import TacticalManagementData


add_client_address_no_name_ids = [
    "测试：{}->[策略名称:{}-创建个数:{}-预期:{}]".
        format(data["case"], data["PolicySetsName"], data["num"], data["expected"]) for data in TacticalManagementData.add_client_address_no_name_data
]
add_client_address_no_select_ids = [
    "测试：{}->[策略名称:{}-预期:{}]".
        format(data["case"], data["PolicySetsName"], data["expected"]) for data in TacticalManagementData.add_client_address_no_select_data
]
add_client_address_name_code_ids = [
    "测试：{}->[策略名称:{}-创建个数:{}-预期:{}]".
        format(data["case"], data["PolicySetsName"], data["num"], data["expected"]) for data in TacticalManagementData.add_client_address_name_code_data
]
add_client_address_name_long_ids = [
    "测试：{}->[策略名称:{}-创建个数:{}-预期:{}]".
        format(data["case"], data["PolicySetsName"], data["num"], data["expected"]) for data in TacticalManagementData.add_client_address_name_long_data
]
add_client_address_name_repetition_ids = [
    "测试：{}->[策略名称:{}-创建个数:{}-预期:{}]".
        format(data["case"], data["PolicySetsName"], data["num"], data["expected"]) for data in TacticalManagementData.add_client_address_name_repetition_data
]



add_client_address_ids = [
    "测试：{}->创建个数:{}-[预期:{}]".
        format(data["case"], data["num"], data["expected"]) for data in TacticalManagementData.add_client_address_data
]
del_client_address_ids = [
    "测试：{}->[预期:{}]".
        format(data["case"], data["expected"]) for data in TacticalManagementData.del_client_address_data
]

@pytest.mark.TacticalManagement
class TestTacticalManagement(object):
    """策略管理"""
    tactical_data = TacticalManagementData

    @pytest.mark.parametrize("data", tactical_data.add_client_address_no_name_data, ids=add_client_address_no_name_ids)
    def test_add_client_address_no_name(self, secrecy_login, ini_pages_secrecy, data):
        """创建客户端地址策略集名称不输入"""
        add_client_address_tactical = ini_pages_secrecy[2]
        add_client_address_tactical.add_client_address_tactical(data["PolicySetsName"], data["num"])
        result = add_client_address_tactical.get_name_too_long_error_msg()
        assert data["expected"] == result, "客户端地址策略集名称不输入创建成功"

    @pytest.mark.parametrize("data", tactical_data.add_client_address_no_select_data, ids=add_client_address_no_select_ids)
    def test_add_client_address_no_select(self, secrecy_login, ini_pages_secrecy, data):
        """创建客户端地址策略集名称不选择过滤类型"""
        add_client_address_tactical = ini_pages_secrecy[2]
        add_client_address_tactical.add_client_address_tactical_no_select(data["PolicySetsName"])
        result = add_client_address_tactical.get_type_error_msg()
        assert data["expected"] == result, "创建客户端地址策略集名称不选择过滤类型创建成功"

    @pytest.mark.parametrize("data", tactical_data.add_client_address_name_code_data, ids=add_client_address_name_code_ids)
    def test_add_client_address_name_code(self, secrecy_login, ini_pages_secrecy, data):
        """客户端地址策略集名称为代码"""
        add_client_address_tactical = ini_pages_secrecy[2]
        add_client_address_tactical.add_client_address_tactical(data["PolicySetsName"], data["num"])
        result = add_client_address_tactical.get_policy_sets_names()
        assert data["expected"] in result, "客户端地址策略集名称为代码创建失败"

    @pytest.mark.parametrize("data", tactical_data.add_client_address_name_long_data, ids=add_client_address_name_long_ids)
    def test_add_client_address_name_long(self, secrecy_login, ini_pages_secrecy, data):
        """客户端地址策略集名称过长"""
        add_client_address_tactical = ini_pages_secrecy[2]
        add_client_address_tactical.add_client_address_tactical(data["PolicySetsName"], data["num"])
        result = add_client_address_tactical.get_name_too_long_error_msg()
        assert data["expected"] == result, "客户端地址策略集名称过长创建成功"

    @pytest.mark.parametrize("data", tactical_data.add_client_address_name_repetition_data, ids=add_client_address_name_repetition_ids)
    def test_add_client_address_name_repetition(self, secrecy_login, ini_pages_secrecy, data):
        """客户端地址策略集名称重复"""
        add_client_address_tactical = ini_pages_secrecy[2]
        add_client_address_tactical.add_client_address_tactical(data["PolicySetsName"], data["num"])
        result = add_client_address_tactical.get_name_too_long_error_msg()
        assert data["expected"] == result, "客户端地址策略集名称重复创建成功"

    @pytest.mark.parametrize("data", tactical_data.add_client_address_data, ids=add_client_address_ids)
    def test_add_client_address_tactical(self, secrecy_login, ini_pages_secrecy, data):
        """创建客户端地址策略集1000条"""
        add_client_address_tactical = ini_pages_secrecy[2]
        add_client_address_tactical.add_client_address_tactical(data["PolicySetsName"], data["num"])
        result = add_client_address_tactical.get_policy_sets_names()
        assert data["expected"] in result, "创建客户端地址策略集1000条失败"

    @pytest.mark.parametrize("data", tactical_data.del_client_address_data, ids=del_client_address_ids)
    def test_del_client_address_tactical(self,secrecy_login, ini_pages_secrecy, data):
        """删除所有客户端地址策略集"""
        del_client_address_tactical = ini_pages_secrecy[2]
        del_client_address_tactical.del_client_address_tactical()
        result = del_client_address_tactical.get_policy_sets_names()
        assert data["expected"] == result, "删除客户端地址策略集失败"
















