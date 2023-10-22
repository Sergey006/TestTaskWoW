from selenium import webdriver
from selenium.webdriver.common.by import By

from first_task.utils import extract_text


class Browser:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def find_elements(self, locator):
        return self.driver.find_elements(By.XPATH, locator)

    def find_element(self, locator):
        return self.driver.find_element(By.XPATH, locator)

    def click(self, locator):
        self.find_element(locator).click()

    def get_element_text(self, element):
        return extract_text(element)
