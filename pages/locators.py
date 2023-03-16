from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'p.price_color')
    ADDED_PRODUCT_NAME = (By.CSS_SELECTOR, 'div.alert-success:first-child .alertinner strong')
    CART_PRICE = (By.CSS_SELECTOR, '.alert-info .alertinner strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alert-success')


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".basket-mini a")


class BasketPageLocators():
    BASKET_INNER = (By.CSS_SELECTOR, ".basket-title")
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")
