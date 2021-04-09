class TacticalManagementData(object):
    """策略管理数据"""

    add_client_address_no_name_data = [
        {
            "case": "客户端地址策略集名称为空或不选择过滤类型",
            "PolicySetsName": " ",
            "num": 1,
            "expected": "策略集名称不能为空！"
        }]

    add_client_address_no_select_data = [
        {
            "case": "添加客户端地址策略集不选择过滤类型",
            "PolicySetsName": "不选择过滤类型",
            "num": 1,
            "expected": "这是必填字段"
        }
    ]

    add_client_address_name_code_data = [
        {
            "case": "客户端地址策略集名称为代码",
            "PolicySetsName": "<p>'a'</p>",
            "num": 1,
            "expected": "<p>'a'</p>"
        }
    ]

    add_client_address_name_long_data = [

        {
            "case": "客户端地址策略集名称大于64位",
            "PolicySetsName": "dgshdshdsduuerrweweedgshdshdsduuerrweweedgshdshdsduuerrweweedgshx",
            "num": 1,
            "expected": "策略集名称长度不能超过64位！"
        }
    ]
    add_client_address_name_repetition_data = [
        {
            "case": "客户端地址策略集名称为已存在的名称",
            "PolicySetsName": "<p>'a'</p>",
            "num": 1,
            "expected": "名称已存在！"
        },
    ]


    add_client_address_data = [
        {
            "case": "客户端地址策略集添加",
            "PolicySetsName":"",
            "num": 999,
            "expected": "策略集999"
        }
    ]


    del_client_address_data = [
        {
            "case": "客户端地址策略集删除",
            "expected": None
        }
    ]


