import time

from selenium import webdriver
from behave import *

@given('Open the chrome and start application')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://opensource-demo.orangehrmlive.com/")
    context.driver.maximize_window()
    time.sleep(5)

@when('I enter valid <username> and <password>')
def step_impl(context):
    time.sleep(1)


@when('click on login button')
def step_impl(context):
    time.sleep(2)

@then('user should be able to login successfully')
def step_impl(context):
    context.driver.close()