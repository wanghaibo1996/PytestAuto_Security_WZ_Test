class LoginData(object):
    """用户登录测试数据"""

    admin_login_success_data = [
        {
            "case": "用户名正确, 密码正确",
            "username": "admin",
            "password": "admin2004",
            "expected": "首页11"
        }
    ]
    admin_login_fail_data = [
        {
            "case": "用户名正确, 密码错误",
            "username": "admin",
            "password": "admin",
            "expected": "用户名或密码或指纹错误"
        },
        {
            "case": "用户名错误, 密码正确",
            "username": "admin111",
            "password": "admin2004",
            "expected": "用户名或密码或指纹错误"
        },
        {
            "case": "用户名错误, 密码错误",
            "username": "admin123",
            "password": "admin",
            "expected": "用户名或密码或指纹错误"
        }
    ]

    secrecy_login_success_data = [
        {
            "case": "用户名正确, 密码正确",
            "username": "secrecy",
            "password": "secrecy2004",
            "expected": "首页"
        }
    ]
    secrecy_login_fail_data = [
        {
            "case": "用户名正确, 密码错误",
            "username": "secrecy",
            "password": "secrecy",
            "expected": "用户名或密码或指纹错误"
        },
        {
            "case": "用户名错误, 密码正确",
            "username": "secrecy111",
            "password": "secrecy2004",
            "expected": "用户名或密码或指纹错误"
        },
        {
            "case": "用户名错误, 密码错误",
            "username": "secrecy123",
            "password": "secrecy",
            "expected": "用户名或密码或指纹错误"
        }
    ]

    audit_login_success_data = [
        {
            "case": "用户名正确, 密码正确",
            "username": "audit",
            "password": "audit2004",
            "expected": "首页"
        }
    ]

    audit_login_fail_data = [
        {
            "case": "用户名正确, 密码错误",
            "username": "audit",
            "password": "audit",
            "expected": "用户名或密码或指纹错误"
        },
        {
            "case": "用户名错误, 密码正确",
            "username": "audit111",
            "password": "audit2004",
            "expected": "用户名或密码或指纹错误"
        },
        {
            "case": "用户名错误, 密码错误",
            "username": "audit123",
            "password": "audit",
            "expected": "用户名或密码或指纹错误"
        }
    ]


if __name__ == '__main__':
    pass
