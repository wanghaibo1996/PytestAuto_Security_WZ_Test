import allure
import pytest
from selenium import webdriver
from py._xmlgen import html



driver = None


# 测试失败时添加截图和测试用例描述(用例的注释信息)

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    当测试失败的时候，自动截图，展示到html报告中
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            screen_img = _capture_screenshot()
            if file_name:
                html = '<div><img src="data:image/png;base64,%s" alt="screenshot" style="width:600px;height:400px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % screen_img
                extra.append(pytest_html.extras.html(html))
            # 添加allure失败截图
            allure.attach(driver.get_screenshot_as_png(), "失败截图", allure.attachment_type.PNG)

        report.extra = extra
    extra.append(pytest_html.extras.text('some string', name='Different title'))
    report.description = str(item.function.__doc__)
    report.nodeid = report.nodeid.encode("utf-8").decode("unicode_escape")  # 解决乱码


def pytest_configure(config):
    # 添加测试地址与项目名称
    config._metadata["项目名称"] = "金电网安安全隔离与信息交换系统FerryWay V2.0"
    config._metadata["测试地址"] = "https://192.168.0.28"
    # 删除无用环境信息Java_Home
    config._metadata.pop("JAVA_HOME")


@pytest.mark.optionalhook
def pytest_html_results_summary(prefix):
    prefix.extend([html.p("所属部门: 郑州测试分部")])
    prefix.extend([html.p("测试人员: 汪海波,刘孝")])


@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    cells.insert(1, html.th('描述'))
    cells.insert(2, html.th('用例描述'))
    cells.pop(3)
    cells.pop(-1)


@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    cells.insert(1, html.td(report.description))
    cells.insert(2, html.td(report.nodeid))
    cells.pop(3)
    cells.pop(-1)



def _capture_screenshot():
    """
    截图保存为base64
    :return:
    """
    return driver.get_screenshot_as_base64()


# 设置为session，全部用例执行一次
@pytest.fixture(scope='session')
def driver():
    global driver
    print('------------open browser------------')
    chromeOptions = webdriver.ChromeOptions()

    # 设定下载文件的保存目录，
    # 如果该目录不存在，将会自动创建
    prefs = {"download.default_directory": "E:\\GAP_Download"}
    # 将自定义设置添加到Chrome配置对象实例中
    chromeOptions.add_experimental_option("prefs", prefs)
    # chromeOptions.add_argument("--user-data-dir=C:/Users/Me/AppData/Local/Google/Chrome/User Data/Default")
    chromeOptions.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome(options=chromeOptions)

    driver.maximize_window()
    yield driver
    print('------------close browser------------')
    driver.quit()
