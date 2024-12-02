from behave import *

@when('I insert email as "{email_value}"')
def step_impl(context, email_value):
    context.login_page.insert_email(email_value)

