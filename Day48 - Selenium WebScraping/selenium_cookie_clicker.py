import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

path = "C:\Development\edgedriver_win64\msedgedriver.exe"

driver = webdriver.Edge(executable_path=path)
driver.get(url="https://orteil.dashnet.org/cookieclicker/")


cookie = driver.find_element_by_id("bigCookie")

cookie.click()

money = driver.find_element_by_id("cookies").text
money_list = money.split()
money_amount = int(money_list[0])

timeout = time.time() + 5
five_min = time.time() + (60*5)

while True:
    cookie.click()
    if time.time() > timeout:
        # money = driver.find_element_by_id("cookies").text
        # money_list = money.split()
        # money_amount = int(money_list[0])

        #Make sure we're always taking the most expensive, available item.
        try:
            clickable_upgrades = driver.find_elements_by_css_selector(".crate.upgrade.enabled")
            most_expensive_upgrade_available = clickable_upgrades[-1]
            most_expensive_upgrade_available.click()

        except (IndexError, selenium.common.exceptions.ElementClickInterceptedException):
            pass

        try:
            clickable_items = driver.find_elements_by_css_selector(".product.unlocked.enabled")
            most_expensive_available_item = clickable_items[-1]
            most_expensive_available_item.click()

        except (IndexError, selenium.common.exceptions.ElementClickInterceptedException):
            pass

        timeout = time.time() + 5

#driver.quit()