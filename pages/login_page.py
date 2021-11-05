from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import MainPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "Current link is not correct"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REG_FORM), "Register form  is not presented"

    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()

    def register_new_user(self, email, password):
        self.browser.get('http://selenium1py.pythonanywhere.com/ru/accounts/login/')
        self.browser.find_element(*LoginPageLocators.REGISTER_LOGIN_TEXTBOX).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASSPORT_TEXTBOX).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_CONFIRM_PASSPORT_TEXTBOX).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_SUBMIT_BUTTON).click()
        '''try:
            WebDriverWait(self.browser, 20).until(expected_conditions.presence_of_element_located(*LoginPageLocators.SUCCESS_REGISTER))
            return True
        except:
            return False'''
