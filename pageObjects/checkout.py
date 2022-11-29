from selenium.webdriver.common.by import By


class Checkout:
    def __init__(self, driver):
        self.driver = driver

    checkout_btn = (By.NAME, "checkout")
    fname = (By.XPATH, "//input[@name='firstName']")
    lname = (By.XPATH, "//input[@name='lastName']")
    zipcode = (By.XPATH, "//input[@name='postalCode']")
    message = (By.XPATH, "//div[@class='summary_total_label']")
    continue_btn = (By.ID, "continue")
    finish_btn = (By.XPATH, "//button[@id='finish']")
    success_message = (By.XPATH, "//h2[@class='complete-header']")

    def btn(self):
        return self.driver.find_element(*Checkout.checkout_btn)

    def f_name(self):
        return self.driver.find_element(*Checkout.fname)

    def l_name(self):
        return self.driver.find_element(*Checkout.lname)

    def zip_code(self):
        return self.driver.find_element(*Checkout.zipcode)

    def continue_payment(self):
        return self.driver.find_element(*Checkout.continue_btn)

    def verify_price(self):
        return self.driver.find_element(*Checkout.message)

    def finish(self):
        return self.driver.find_element(*Checkout.finish_btn)

    def success_msg(self):
        return self.driver.find_element(*Checkout.success_message)
