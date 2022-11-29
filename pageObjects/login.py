from pageObjects.homepage import Homepage
from selenium.webdriver.common.by import By


class Login:
    def __init__(self, driver):
        self.driver = driver

    username = (By.XPATH, "//input[@type='text']")
    password = (By.XPATH, "//input[@type='password']")
    button = (By.XPATH, "//input[@value='Login']")

    def user_login(self):
        return self.driver.find_element(*Login.username)

    def user_password(self):
        return self.driver.find_element(*Login.password)

    def user_button(self):
        self.driver.find_element(*Login.button).click()
        # homepage page object creation
        cart = Homepage(self.driver)
        return cart



