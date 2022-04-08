import time
from selenium import webdriver
from selenium.webdriver import Keys

driver = webdriver.Chrome()
driver.get("https://www.onetravel.com/")
driver.maximize_window()

time.sleep(1)
signUpClick = driver.find_element_by_xpath("//*[@class='navigation__link dropdown-toggle ml-0']").click()
username = driver.find_element_by_name("email").send_keys("pavanteli6@gmail.com" + Keys.ENTER)
print(username)
time.sleep(2)
driver.find_element_by_xpath("//button[@class='btn btn-block btn-default btn-lg mb-3 undefined']").click()
time.sleep(5)
password = driver.find_element_by_name("password").send_keys("pavan@123" + Keys.ENTER)
print(password)
time.sleep(2)

try:
    loginMsg = driver.find_element_by_xpath("//span[contains(text(),'Welcome')]").text
except:
    driver.close()
    assert False, "Test case failed"

if loginMsg == "Welcome":
    driver.close()
    assert True, "Test case passed"

driver.find_element_by_xpath("//a[@aria-label='Select Currency']").click()
time.sleep(2)
driver.find_element_by_xpath("//span[@class='flag-INR']").click()
time.sleep(2)

driver.close()
