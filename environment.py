from browser import Browser
from pages.base_page import BasePage


def before_all(context):
    context.browser = Browser()
    context.base_page = BasePage()



def after_all(context):
    context.browser.close()