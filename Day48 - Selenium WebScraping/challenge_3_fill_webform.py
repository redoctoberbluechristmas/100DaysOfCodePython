from selenium import webdriver
from selenium.webdriver.common.keys import Keys

path = "C:\Development\edgedriver_win64\msedgedriver.exe"

driver = webdriver.Edge(executable_path=path)
driver.get(url="http://secure-retreat-92358.herokuapp.com/")

#first_name = driver.find_element_by_css_selector("fName")
first_name = driver.find_element_by_name("fName")
last_name = driver.find_element_by_name("lName")
email = driver.find_element_by_name("email")
submit = driver.find_element_by_css_selector("form button")

first_name.send_keys("Bill")
last_name.send_keys("Brasky")
email.send_keys("kyle@email.com")

submit.send_keys(Keys.ENTER)

#driver.quit()
