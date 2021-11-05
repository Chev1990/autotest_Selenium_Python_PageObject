from selenium.webdriver.common.by import By
from selenium import webdriver

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REG_FORM = (By.CSS_SELECTOR, "#register_form")

    REGISTER_LOGIN_TEXTBOX = (By.ID, 'id_registration-email')
    REGISTER_PASSPORT_TEXTBOX = (By.ID, 'id_registration-password1')
    REGISTER_CONFIRM_PASSPORT_TEXTBOX = (By.ID, 'id_registration-password2')
    REGISTER_SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[name^="registration_submit"]')
    SUCCESS_REGISTER = (By.CSS_SELECTOR, 'div#messages>div>div>i.icon-ok-sign')

class BasketPageLocators():
    BASKET_LINK = (By.CSS_SELECTOR, "#add_to_basket_form")

class ProductPageLocators():
    PRODUCT_LINK = (By.CSS_SELECTOR, "div.col-sm-6.product_main>h1")
    BASKET_BUTTON = (By.CSS_SELECTOR, '.basket-mini>span>a')
    BASKET_EMPTY_MESSAGE = (By.XPATH, '//div[@id="content_inner"]//p[contains(text(),"Your basket is empty.")]')

    ADD_ITEM_BUTTON = (By.CSS_SELECTOR, '#add_to_basket_form>button[type^="submit"]')
    PRODUCT_NAME_TEXT = (By.CSS_SELECTOR, '.product_main>h1')
    SUCCESS_ADD_PRODUCT_TO_BASKET_TEXT = (By.CSS_SELECTOR, '.alertinner>strong:nth-child(1)')
    PRICE_TEXT = (By.CSS_SELECTOR, '.product_main>.price_color')
    MESSAGE_PRICE_TEXT = (By.CSS_SELECTOR, '.alertinner>p>strong')

class PricePageLocators():
    PRICE_LINK = (By.CSS_SELECTOR, "p.price_color")
class MessProductPageLocators():
    MESSPROD_LINK = (By.CSS_SELECTOR, "div.alert.alert-safe.alert-noicon.alert-success.fade.in:nth-of-type(1)>div.alertinner>strong")
class MessPricePageLocators():
    MESSPRICE_LINK = (By.CSS_SELECTOR, "div.alert.alert-safe.alert-noicon.alert-info.fade.in>.alertinner>p>strong")
