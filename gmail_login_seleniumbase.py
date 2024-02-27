from seleniumbase import SB

with SB(uc=True) as sb:
    sb.open("https://www.google.com/gmail/about/")
    sb.click('a[data-action="sign in"]')
    sb.type('input[type="email"]', "a8delhadi@gmail.com")
    sb.click('button:contains("Next")')
    sb.sleep(5)
    sb.type('input[type="password"]', 'abdelhadi@@0109')
    sb.click('button:contains("Next")')
    sb.sleep(5)
    sb.sleep(5)
    sb.sleep(5)
    sb.sleep(5)
    sb.sleep(5)


# from seleniumbase import BaseCase
# BaseCase.main(__name__, __file__)

# class MyTestClass(BaseCase):
#     def test_swag_labs(self):
#         self.open("https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&emr=1&followup=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&ifkv=ATuJsjzlJs213I39XF9RAAMfEyrZVy7PXlHOB5-hFyPWLbuLkHBWaPbmSBYjn0sYV7xHQVAQwDtPRg&osid=1&passive=1209600&service=mail&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S1946388061%3A1709038695681833&theme=glif#inbox")
#         self.type("#identifierId", "a8delhadi@gmail.com")
#         # self.type("#password", "secret_sauce\n")
#         # self.assert_element("div.inventory_list")
#         # self.assert_exact_text("Products", "span.title")
#         # self.click('button[name*="backpack"]')
#         # self.click("#shopping_cart_container a")
#         # self.assert_exact_text("Your Cart", "span.title")
#         # self.assert_text("Backpack", "div.cart_item")
#         # self.click("button#checkout")
#         # self.type("#first-name", "SeleniumBase")
#         # self.type("#last-name", "Automation")
#         # self.type("#postal-code", "77123")
#         # self.click("input#continue")
#         # self.assert_text("Checkout: Overview")
#         # self.assert_text("Backpack", "div.cart_item")
#         # self.assert_text("29.99", "div.inventory_item_price")
#         # self.click("button#finish")
#         # self.assert_exact_text("Thank you for your order!", "h2")
#         # self.assert_element('img[alt="Pony Express"]')
#         # self.js_click("a#logout_sidebar_link")
#         # self.assert_element("div#login_button_container")
