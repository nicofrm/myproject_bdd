import self
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from pages.base_page import Base_Page

class Home_page(Base_Page):

    SEARCH_INPUT_BOX = (By.ID, 'search')
    ACCEPT_COOKIES_BUTTON = (By.CSS_SELECTOR, 'button[class="fc-button fc-cta-consent fc-primary-button"')
    LOGIN_LINK = (By.LINK_TEXT, 'Sign In')

    def navigate_to_login_page(self):
        self.driver.get('https://magento.softwaretestingboard.com/')
    def enter_search_value(self, search_value):
        self.enter_text(*self.SEARCH_INPUT_BOX, search_value)

    def enter_key_from_keyword(self, key_entered):
        #self.enter_text(*self.SEARCH_INPUT_BOX,f"{Keys.}{key_entered}")
        if key_entered.upper() == 'ENTER':
            self.enter_text(*self.SEARCH_INPUT_BOX, Keys.ENTER)

    def accept_cookies(self):
        try:
            self.driver.find_element(*self.ACCEPT_COOKIES_BUTTON).click()
        except:
            pass

    def click_on_sign_in_link(self):
        self.driver.find_element(*self.LOGIN_LINK).click()