# Created by BrandonFox at 2/18/2017
Feature: Admin Backend
  # Description of feature
  As an admin user
  I want to be able to log into /admin/
  So that I can administer server

  Background: Set server address, create admin user and setup database
    Given I am an Administrator
    And I am using server "http://127.0.0.1:8000"

  Scenario: An Administrator User Attempts to Login
    When I visit "/admin/"
    And I enter Administrator Username and Password
    Then Login is Success
    And I am redirected to Admin Backend

#  Scenario: Access Admin Login Page
#    Given I access the URL "/admin"
#    Then I see the admin login

 # Scenario: Non-Admin Login Attempt
 #   Given I am on URL "/admin"
 #   And I enter an INVALID Administrator Account
 #   Then DIV ID="Content" should contain P CLASS="errornote"
 #   And contain text="Please enter the correct username and password for a staff account"