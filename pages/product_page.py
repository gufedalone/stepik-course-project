from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def add_item_to_cart(self):
        add_to_cart_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        add_to_cart_button.click()

    def verify_name_and_price_of_added_item(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        added_product_name = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_NAME).text
        cart_price = self.browser.find_element(*ProductPageLocators.CART_PRICE).text
        assert [product_name, product_price] == [added_product_name, cart_price]

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def success_message_should_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared, but should be"


