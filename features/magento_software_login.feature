Feature: We want to check login functionality
  Scenario: Verify that when the user inserts invalid data into login fields, then he is not able to login into the application
    Given I am on magento software testing homepage
    When I click on the sign in link
    When I insert email as "sdfdfsdasa"
    When I insert password as "ksdfjl"