import pytest
from selenium import webdriver
from pages.api_module import ApiClient
from selenium.webdriver.common.by import By
from selenium.webdriver.android.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def get_driver(request):
    driver: WebDriver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    request.cls.driver = driver
    driver.maximize_window()
    yield
    driver.find_element(By.XPATH, '//button[@data-test="clear-button"]').click()
    driver.quit()


@pytest.fixture(scope="function")
def clear_data_after_tests():
    api_module = ApiClient()
    yield
    api_module.delete_subscriptions()


"""@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    marker = item.get_closest_marker("ui")
    if marker:
        if rep.when == "call" and rep.failed:  # we only look at actual failing test calls, not setup/teardown
            try:
                allure.attach(item.instance.driver.get_screenshot_as_png(),
                              name=item.name,
                              attachment_type=allure.attachment_type.PNG)
            except Exception as e:
                print(e)"""