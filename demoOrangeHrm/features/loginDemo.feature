Feature: Test traveller login scenario
  Scenario: Login with valid credentials
    Given Open the chrome and start application
	When I enter valid <username> and <password>
	And click on login button
	Then user should be able to login successfully
