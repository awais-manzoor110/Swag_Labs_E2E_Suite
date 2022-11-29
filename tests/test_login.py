from time import sleep
import pytest
from pageObjects.login import Login
from testdata.userdata import UserData
from utilities.baseclass import BaseClass


# inherit the baseclass
class TestLogin_user(BaseClass):
    def test_login(self, getdata):
        # login page object creation
        user = Login(self.driver)

        user.user_login().send_keys("standard_user")
        user.user_password().send_keys("secret_sauce")
        # add_to_cart object initialization
        cart = user.user_button()
        products = cart.item()
        for product in products:
            product_name = product.text
            if product_name == 'Sauce Labs Bike Light':
                cart.add_to_cart().click()
        # check_out object initialization
        check_out = cart.added_cart()
        check_out.btn().click()
        check_out.f_name().send_keys(getdata["fname"])
        check_out.l_name().send_keys(getdata["lname"])
        check_out.zip_code().send_keys(getdata["zipcode"])
        check_out.continue_payment().click()
        price_check = check_out.verify_price().text
        assert "Total: $32.39" in price_check
        check_out.finish().click()
        success = check_out.success_msg().text
        assert "THANK YOU FOR YOUR ORDER" in success
        sleep(4)

    # user data
    @pytest.fixture(params=UserData.user_detail)
    def getdata(self, request):
        return request.param
