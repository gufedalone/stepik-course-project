from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_INNER), \
            "Basket is not empty, but should be"
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), \
            "Empty basket message is not displayed, but should be"

    def should_not_be_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_INNER), \
            "Basket is empty, but should not be"
        assert self.is_not_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), \
            "Empty basket message is displayed, but should not be"
