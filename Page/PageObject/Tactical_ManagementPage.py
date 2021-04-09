from Page.BasePage import BasePage
from util.parseConFile import ParseConFile


class TacticalManagement(BasePage):

    # 配置文件读取元素
    do_conf = ParseConFile()
    # 策略管理按钮
    TacticalManagementBtn = do_conf.get_locators_or_account('TacticalManagementElements', 'TacticalManagementBtn')
    # 客户端地址按钮
    clientAddressBtn = do_conf.get_locators_or_account('TacticalManagementElements', 'clientAddressBtn')
    # ftp按钮
    ftpBtn = do_conf.get_locators_or_account('TacticalManagementElements', 'ftpBtn')
    # 策略集添加按钮
    PolicySetsAddBtn = do_conf.get_locators_or_account('TacticalManagementElements', 'PolicySetsAddBtn')
    # 策略集名称输入框
    PolicySetsNameInputBtn = do_conf.get_locators_or_account('TacticalManagementElements', 'PolicySetsNameInputBtn')
    # 白名单选择
    whiteBtn = do_conf.get_locators_or_account('TacticalManagementElements', 'whiteBtn')
    # 黑名单选择
    blackBtn = do_conf.get_locators_or_account('TacticalManagementElements', 'blackBtn')
    # 保存按钮
    saveBtn = do_conf.get_locators_or_account('TacticalManagementElements', 'saveBtn')
    # 策略集总数
    PolicySetsNum = do_conf.get_locators_or_account('TacticalManagementElements', 'PolicySetsNum')
    # 选择第一条策略集
    PolicySetsSelectBtn = do_conf.get_locators_or_account('TacticalManagementElements', 'PolicySetsSelectBtn')
    # 删除策略集按钮
    PolicySetsDelBtn = do_conf.get_locators_or_account('TacticalManagementElements', 'PolicySetsDelBtn')
    # 确认删除
    ConfirmDeleteBtn = do_conf.get_locators_or_account('TacticalManagementElements', 'ConfirmDeleteBtn')
    # 名称错误提示信息
    # inputNameErrorMsg = do_conf.get_locators_or_account('TacticalManagementElements', 'inputNameErrorMsg')
    # 过滤类型错误提示信息
    inputTypeErrorMsg = do_conf.get_locators_or_account('TacticalManagementElements', 'inputTypeErrorMsg')
    # 名称太长提示信息/名称重复
    nameTooLongErrorMsg = do_conf.get_locators_or_account('TacticalManagementElements', 'nameTooLongErrorMsg')


    # 添加客户端地址策略集不选择过滤类型
    def add_client_address_tactical_no_select(self, PolicySetsName):
        # 点击策略管理
        self.click(*TacticalManagement.TacticalManagementBtn)
        self.sleep(1)
        # 点击客户端地址
        self.click(*TacticalManagement.clientAddressBtn)
        self.sleep(1)
        # iframe跳转
        self.switch_to_iframe(0)
        self.sleep(1)
        # 点击添加
        self.click(*TacticalManagement.PolicySetsAddBtn)
        self.sleep(0.2)
        # 输入名称
        self.send_keys(*TacticalManagement.PolicySetsNameInputBtn, PolicySetsName)
        self.sleep(0.2)
        # 选择黑/白名单
        # self.click(*TacticalManagement.blackBtn)
        self.sleep(0.2)
        # 保存
        self.click(*TacticalManagement.saveBtn)
        self.sleep(0.2)

    # 创建客户端地址策略集
    def add_client_address_tactical(self, PolicySetsName, num):
        # 点击策略管理
        self.click(*TacticalManagement.TacticalManagementBtn)
        self.sleep(0.5)
        # 点击客户端地址
        self.click(*TacticalManagement.clientAddressBtn)
        self.sleep(0.5)
        # iframe跳转
        self.switch_to_iframe(0)
        self.sleep(0.5)

        if num > 1:
            for i in range(num):
                # 点击添加
                self.click(*TacticalManagement.PolicySetsAddBtn)
                self.sleep(0.2)
                # 输入名称
                self.send_keys(*TacticalManagement.PolicySetsNameInputBtn, "策略集" + str(i+1))
                self.sleep(0.2)
                # 选择黑/白名单
                self.click(*TacticalManagement.blackBtn)
                self.sleep(0.2)
                # 保存
                self.click(*TacticalManagement.saveBtn)
                self.sleep(0.2)
        else:
            # 点击添加
            self.click(*TacticalManagement.PolicySetsAddBtn)
            self.sleep(0.2)
            # 输入名称
            self.send_keys(*TacticalManagement.PolicySetsNameInputBtn, PolicySetsName)
            self.sleep(0.2)
            # 选择黑/白名单
            self.click(*TacticalManagement.blackBtn)
            self.sleep(0.2)
            # 保存
            self.click(*TacticalManagement.saveBtn)
            self.sleep(0.2)

    # 删除客户端地址策略集
    def del_client_address_tactical(self):
        # 点击策略管理
        self.click(*TacticalManagement.TacticalManagementBtn)
        self.sleep(1)
        # 点击客户端地址
        self.click(*TacticalManagement.clientAddressBtn)
        self.sleep(1)
        # iframe跳转
        self.switch_to_iframe(0)
        self.sleep(1)

        if self.find_elements(*TacticalManagement.PolicySetsNum):
            for i in self.find_elements(*TacticalManagement.PolicySetsNum):
                # 选择策略集
                self.click(*TacticalManagement.PolicySetsSelectBtn)
                self.sleep(0.2)
                # 点击删除
                self.click(*TacticalManagement.PolicySetsDelBtn)
                self.sleep(0.5)
                # 确认删除
                self.click(*TacticalManagement.ConfirmDeleteBtn)
                self.sleep(0.2)
                # ok
                self.click(*TacticalManagement.ConfirmDeleteBtn)
                self.sleep(0.2)

    # 获取客户端地址所有策略集名称
    def get_policy_sets_names(self):
        if self.find_elements(*TacticalManagement.PolicySetsNum):
            return self.get_elements_text(*TacticalManagement.PolicySetsNum)
        else:
            return None

    # 获取添加客户端地址策略集过滤类型错误提示信息
    def get_type_error_msg(self):
        return self.get_element_text(*TacticalManagement.inputTypeErrorMsg)

    # 名称太长或名称重复提示信息
    def get_name_too_long_error_msg(self):
        return self.get_element_text(*TacticalManagement.nameTooLongErrorMsg)













