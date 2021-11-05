from selenium.webdriver.common.by import By
from selenium import webdriver

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REG_FORM = (By.CSS_SELECTOR, "#register_form")
class BasketPageLocators():
    BASKET_LINK = (By.CSS_SELECTOR, "#add_to_basket_form")
class ProductPageLocators():
    PRODUCT_LINK = (By.CSS_SELECTOR, "div.col-sm-6.product_main>h1")
class PricePageLocators():
    PRICE_LINK = (By.CSS_SELECTOR, "p.price_color")
class MessProductPageLocators():
    MESSPROD_LINK = (By.CSS_SELECTOR, "div.alert.alert-safe.alert-noicon.alert-success.fade.in:nth-of-type(1)>div.alertinner>strong")
class MessPricePageLocators():
    MESSPRICE_LINK = (By.CSS_SELECTOR, "div.alert.alert-safe.alert-noicon.alert-info.fade.in>.alertinner>p>strong")
