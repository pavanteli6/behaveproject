import time
from behave import *
from behave.textutil import text
from selenium import webdriver
from selenium.webdriver import Keys


@given('Open the chrome and start application')
def openAndStartApplication(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.onetravel.com/")
    context.driver.maximize_window()

    time.sleep(1)
    signUpClick = context.driver.find_element_by_xpath("//*[@class='navigation__link dropdown-toggle ml-0']").click()


@when('I enter valid username "{user}" and password "{pwd}"')
def enterUsernamesAndPassword(context, user, pwd):
    username = context.driver.find_element_by_name("email").send_keys(user + Keys.ENTER)
    print(username)
    time.sleep(2)
    context.driver.find_element_by_xpath("//button[@class='btn btn-block btn-default btn-lg mb-3 undefined']").click()
    time.sleep(5)
    password = context.driver.find_element_by_name("password").send_keys(pwd + Keys.ENTER)
    print(password)
    time.sleep(2)


@when('click on login button')
def ClickLogin(context):
    print("...........")


@then('user should be able to login successfully')
def SuccessfullyLogInMsg(context):
    try:
        loginMsg = context.driver.find_element_by_xpath("//span[contains(text(),'Welcome')]").text
    except:
        context.driver.close()
        assert False, "Test case failed"

    if loginMsg == "Welcome":
        context.driver.close()
        assert True, "Test case passed"


@when('Change Currency and then close window')
def currency_change(context):
    context.driver.find_element_by_xpath("//a[@aria-label='Select Currency']").click()
    time.sleep(2)
    context.driver.find_element_by_xpath("//span[@class='flag-INR']").click()
    time.sleep(2)
