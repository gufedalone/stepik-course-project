from pages.product_page import ProductPage

url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'


def test_guest_can_add_product_to_basket(browser):
    product_page = ProductPage(browser, url)
    product_page.open()
    product_page.add_item_to_cart()
    product_page.solve_quiz_and_get_code()

    product_page.verify_name_and_price_of_added_item()
