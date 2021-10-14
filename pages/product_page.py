from selenium.common.exceptions import NoAlertPresentException
from . import base_page
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By
from selenium import webdriver
import math
import time

class BasketPage(base_page.BasePage):
    def should_be_basket_page(self):
        self.should_be_basket_url()

    def should_be_basket_url(self):
        # реализуйте проверку на корректный url адрес
        assert "?promo=newYear" in self.browser.current_url, "Current link is not correct"

    def go_to_basket_page(self):
        link = self.browser.find_element(*ProductPageLocators.BASKET_LINK)
        link.click()

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
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
