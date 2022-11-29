from pageObjects.checkout import Checkout
from selenium.webdriver.common.by import By


class Homepage:
    def __init__(self, driver):
        self.driver = driver

    items = (By.XPATH, "//div[@class='inventory_item']/div/div/a")
    cart_button = (By.XPATH, "//div//button[@class= 'btn btn_primary btn_small btn_inventory']")
    cart = (By.XPATH, "//a[@class='shopping_cart_link']")

    def item(self):
        return self.driver.find_elements(*Homepage.items)

    def add_to_cart(self):
        return self.driver.find_element(*Homepage.cart_button)

    def added_cart(self):
        self.driver.find_element(*Homepage.cart).click()
        # check_out page object creation
        check_out = Checkout(self.driver)
        return check_out
