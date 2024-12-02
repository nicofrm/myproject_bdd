from browser import Browser
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class Base_Page(Browser):
    def enter_text(self, by, value, search_value):
        self.driver.find_element(by, value).send_keys(search_value)


