# Created by BrandonFox at 2/18/2017
Feature: Admin User can Log In to Admin Backend
  # Description of feature
  As an admin user
  I should be able to log into {{Domain Name}}/admin
  and be greeted with the admin user panel

#  Scenario: Access Admin Login Page
#    Given I access the URL "/admin"
#    Then I see the admin login

  Scenario: An Administrator User Attempts to Login
    Given I am an Admin User
    When I log in
    Then Login is a Success

 # Scenario: Non-Admin Login Attempt
 #   Given I am on URL "/admin"
 #   And I enter an INVALID Administrator Account
 #   Then DIV ID="Content" should contain P CLASS="errornote"
 #   And contain text="Please enter the correct username and password for a staff account"