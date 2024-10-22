from browser import Browser
from browser import Browser
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class BasePage(Browser):
    def find(self, locator):
        return self.driver.find_element(*locator)

    def click(self, locator):
        self.find(locator).click()

    def type(self, locator, text):
        self.find(locator).send_keys(text)

    def get_text(self, locator):
        return self.find(locator).text

    def is_displayed(self, locator):
        return self.find(locator).is_displayed()

    def element_is_present(self, locator, number_seconds):
        wait = WebDriverWait(self.driver, number_seconds)
        return wait.until(EC.presence_of_element_located(locator))

    def element_is_not_present(self, locator, number_seconds):
        wait = WebDriverWait(self.driver, number_seconds)
        return wait.until(EC.none_of(EC.presence_of_element_located(locator)))