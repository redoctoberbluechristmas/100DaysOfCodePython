from selenium import webdriver
driver_path = "C:\Development\edgedriver_win64\msedgedriver.exe"

driver = webdriver.Edge(executable_path=driver_path)

driver.get(url="https://en.wikipedia.org/wiki/Main_Page")

# article_count = driver.find_element_by_xpath('//*[@id="articlecount"]/a[1]').text
# print(article_count)

article_count = driver.find_element_by_css_selector("#articlecount a") #<--- will return first element

article_count.click()




driver.quit()