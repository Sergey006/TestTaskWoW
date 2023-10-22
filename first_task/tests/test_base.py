import pytest
from selenium import webdriver

from first_task.browser import Browser


@pytest.mark.usefixtures('driver_setup')
class TestBase:
    driver: webdriver
    browser: Browser

    @pytest.fixture
    def driver_setup(self):
        self.driver = webdriver.Chrome()
        self.browser = Browser(self.driver)
        yield
        self.driver.close()
        self.driver.quit()
