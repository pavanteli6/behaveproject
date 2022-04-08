Feature: Test traveller login scenario
  Background:Common Steps to be executed
    Given Open the chrome and start application

  Scenario: Login with valid credentials
    When I enter valid username "pavanteli6@gmail.com" and password "pavan@123"
    And click on login button
    Then user should be able to login successfully

  Scenario: Login with valid credentials
    When I enter valid username "pavanteli6@gmail.com" and password "pavan@123"
    And click on login button
    And Change Currency and then close window
    Then user should be able to login successfully

  Scenario Outline: Login with multiple valid credentials
    When I enter valid username "<username>" and password "<password>"
    And click on login button
    Then user should be able to login successfully
    Examples:
      | username             | password  |
      | pavant@gmail.com     | aspkdaf   |
