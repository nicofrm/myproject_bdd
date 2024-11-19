from browser import Browser
from pages.search_results_page import Search_Results_Page
from pages.base_page import Base_Page
from pages.home_page import Home_page


def before_all(context):
    context.home_page = Home_page()
    context.browser = Browser()
    context.search_result_page = Search_Results_Page()


def after_all(context):
    context.browser.close()