from selenium.webdriver.common.by import By
from pages.base_page import Base_Page

class LoginPage(Base_Page):
    EMAIL_INPUT = (By.XPATH, '//input[@title="Email"]')

    def insert_email(self, login_email):
        self.enter_text(*self.EMAIL_INPUT, login_email)
