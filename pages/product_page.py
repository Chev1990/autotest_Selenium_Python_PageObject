from selenium.common.exceptions import NoAlertPresentException
from . import base_page
from .locators import BasketPageLocators
from .locators import PricePageLocators
from .locators import ProductPageLocators
from .locators import MessProductPageLocators
from .locators import MessPricePageLocators
from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import math
import time

class ProductPage(base_page.BasePage):
    def should_be_basket_page(self):
        self.should_be_basket_url()

    def should_be_basket_url(self):
        # реализуйте проверку на корректный url адрес
        assert "?promo=newYear" in self.browser.current_url, "Current link is not correct"

    def go_to_basket_page(self):
        link = self.browser.find_element(*BasketPageLocators.BASKET_LINK)
        link.click()

    def find_price_page(self):
        #price = is_element_present
        price = self.browser.find_element(*PricePageLocators.PRICE_LINK)
        return price.text

    def find_product_page(self):
        product = self.browser.find_element(*ProductPageLocators.PRODUCT_LINK)
        return product.text

    def check_product_page(self,product):
        mes_flag = self.is_element_present(By.CSS_SELECTOR, "div.alert.alert-safe.alert-noicon.alert-success.fade.in:nth-of-type(1)>div.alertinner")
        print(f"Your mes_flag1!!!!!: {mes_flag}")
        if mes_flag:
            print(f"Your mes_flag2!!!!!: {mes_flag}")
            mes_product=self.browser.find_element(*MessProductPageLocators.MESSPROD_LINK)
            print(f"Your product_basket!!!!!: {mes_product.text}")
            #mes_product1 = product + " has been added to your basket"
            print(f"Your product_new_basket!!!!!: {mes_product.text}")
            assert mes_product.text == product, "NOT EQUAL CHOOSE PRODUCT!!!"
        else:
            raise Exception("No message with add product")

    def check_price_page(self,price):
        mes_flag = self.is_element_present(By.CSS_SELECTOR, "div.alert.alert-safe.alert-noicon.alert-info.fade.in>.alertinner")
        print(f"Your mes_flagprice!!!!!: {mes_flag}")
        if mes_flag:
            mes_price=self.browser.find_element(*MessPricePageLocators.MESSPRICE_LINK)
            print(f"Your price_basket!!!!!: {mes_price.text}")
            #mes_product1 = product + " has been added to your basket"
            assert mes_price.text == price, "NOT EQUAL PRICES!!!"
        else:
            raise Exception("No message with price")

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            time.sleep(1)
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*MessProductPageLocators.MESSPROD_LINK), \
        "Success message is presented, but should not be"

    def should_disappeared_success_message(self):
        assert self.is_disappeared(*MessProductPageLocators.MESSPROD_LINK), \
        "Success message is disappeared, but should not be"

    def add_to_card(self)->bool:
        try:
            self.browser.find_element(*ProductPageLocators.ADD_ITEM_BUTTON).click()
            return True
        except NoSuchElementException:
            return False

    def get_product_name(self)->str:
        try:
            return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_TEXT).text
        except NoSuchElementException:
            return None

    def get_success_message_after_add_product_to_basket(self)->str:
        WebDriverWait(self.browser, 20).until(expected_conditions.presence_of_element_located(ProductPageLocators.SUCCESS_ADD_PRODUCT_TO_BASKET_TEXT))
        try:
            return self.browser.find_element(*ProductPageLocators.SUCCESS_ADD_PRODUCT_TO_BASKET_TEXT).text
        except NoSuchElementException:
            return None

    def check_product_name_on_page_and_in_message(self):
        result = self.get_success_message_after_add_product_to_basket()
        product_name = self.get_product_name()
        assert result == product_name, 'Product name not equal'


