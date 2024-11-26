# vrem sa testam credentiale invalide-> The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later.
# sa incercam sa ne logam fara credentiale, si sa ne asiguram ca mesajul "This is a required field." apare in ambele locuri
# sa ne logam cu user corect, parola gresita si respectiv cu user gresit/parola corecta
# sa ne logam cu credentiale corecte si sa ne asiguram logarea in aplicatie


@T2
Feature: This feature will verify the behaviour of the create account functionality
          in order to ensure proper functionality
  Scenario: Verify that when the user inserts valid data into the input fields, then he will be able to create account
    Given I am on magento software testing homepage
    When I click on the Create an Account link
    When I insert "Nicoleta" on the first name field
    When I insert "Frumosu" on the last name field
    When I insert "nicoleta.frumosu@gmail.com" on the email fields
    When I insert "123ASdffd" on the password field
    When I insert "123ASdffd" on the confirm password field
    When I click on the Create Account button
    Then The account should be created and the user should be direct to homepage