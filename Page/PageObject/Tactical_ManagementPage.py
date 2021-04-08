from Page.BasePage import BasePage
from util.parseConFile import ParseConFile


class TacticalManagement(BasePage):

    # 配置文件读取元素
    do_conf = ParseConFile()
    #




    TacticalManagementBtn = do_conf.get_locators_or_account('TacticalManagementElements', 'TacticalManagementBtn')
    clientAddressBtn = do_conf.get_locators_or_account('TacticalManagementElements', 'clientAddressBtn')
    ftpBtn = do_conf.get_locators_or_account('TacticalManagementElements', 'ftpBtn')
    PolicySetsAddBtn = do_conf.get_locators_or_account('TacticalManagementElements', 'PolicySetsAddBtn')
    PolicySetsNameInputBtn = do_conf.get_locators_or_account('TacticalManagementElements', 'PolicySetsNameInputBtn')
    blackBtn = do_conf.get_locators_or_account('TacticalManagementElements', 'blackBtn')
    saveBtn = do_conf.get_locators_or_account('TacticalManagementElements', 'saveBtn')

    # 创建客户端地址策略集
    def add_client_address_tactical(self):

        # 点击策略管理
        self.click(*TacticalManagement.TacticalManagementBtn)
        self.sleep(1)
        # 点击客户端地址
        self.click(*TacticalManagement.ftpBtn)
        self.sleep(1)
        # iframe跳转
        self.switch_to_iframe(0)
        self.sleep(1)

        for i in range(1000):

            # 点击添加
            self.click(*TacticalManagement.PolicySetsAddBtn)
            self.sleep(0.2)
            # 输入名称
            self.send_keys(*TacticalManagement.PolicySetsNameInputBtn, "策略集" + str(i))
            self.sleep(0.2)
            # 选择黑/白名单
            self.click(*TacticalManagement.blackBtn)
            self.sleep(0.2)
            # 保存
            self.click(*TacticalManagement.saveBtn)
            self.sleep(0.2)





















