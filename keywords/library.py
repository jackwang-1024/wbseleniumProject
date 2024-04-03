from selenium import webdriver
from selenium.webdriver.common.by import By


class Libray:
    def open(self, browser):
        browser = browser.capitalize()
        self.driver = getattr(webdriver,browser)()

        # if browser == "chrome":
        #     self.driver = webdriver.Chrome()
        # elif browser == "firefox":
        #     self.driver = webdriver.Firefox()
        # else:
        #     self.driver = webdriver.Ie()

    def load(self,url):
        self.driver.get(url)

    #元素 loc = (By.ID,"kw")
    def locator(self,loc):
        ele = self.driver.find_element(*loc)
        return ele

    def input(self,loc,value):
        self.locator(loc).send_keys(value)

    def click(self,loc):
        self.locator(loc).click()
