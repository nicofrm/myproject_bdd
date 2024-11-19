from behave import *

@given('I am on magento software testing homepage')
def step_impl(context):
    context.home_page.navigate_to_login_page()
    context.home_page.accept_cookies()

@when('I click on the search input and I enter "{search_value}" text')
def step_impl(context, search_value):
    context.home_page.enter_text(search_value)

@when('I click "{key_entered}"')
def step_impl(context, key_entered):
    context.home_page.enter_key_from_keyword(key_entered)


