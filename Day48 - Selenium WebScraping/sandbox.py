# Selenium is better than BeautifulSoup at simulating an actual user

from selenium import webdriver
edge_driver_path = "C:\Development\edgedriver_win64\msedgedriver.exe"
driver = webdriver.Edge(executable_path=edge_driver_path)

driver.get("https://www.python.org/")
#price = driver.find_element_by_id("price")

name = driver.find_element_by_name("q") #<--- useful for filling in web forms.
print(name.tag_name) #<--- Selenium will return an element as a Selenium WebElement.
#print(price.text)
class_ = driver.find_element_by_class_name("python-logo")

print(class_.size)

css_selector = driver.find_element_by_css_selector(".documentation-widget a")  #<--- looking for an anchor tag inside the class, documentation-widget.
print(css_selector.text)

xpath_selector = driver.find_element_by_xpath('//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(xpath_selector.text)

#driver.close()  #<---- closes the browser.
driver.quit() #<---- close closes a specific tab, quit quits the browser.