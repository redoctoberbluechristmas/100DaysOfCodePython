from selenium import webdriver
edge_driver_path = "C:\Development\edgedriver_win64\msedgedriver.exe"
driver = webdriver.Edge(executable_path=edge_driver_path)

# Get dictionary of upcoming events on python.org

driver.get("https://www.python.org/")

scraped_dates = driver.find_elements_by_css_selector(".event-widget li time")
scraped_names = driver.find_elements_by_css_selector(".event-widget li a")
events = {}

# Method 1 for adding elements to dictionary.
# for n in range(len(scraped_dates)):
#     events[n] = {
#         "time": scraped_dates[n].text,
#         "name": scraped_names[n].text,
#     }
#
# print(events)
# Output: {0: {'time': '2021-07-26', 'name': 'EuroPython 2021'}, 1: {'time': '2021-07-31', 'name': 'PyOhio 2021'}}

# Method 2 for adding elements to dictionary, housed in list.
# events = [
#     {
#         "Date": date.text,
#         "Event": event.text,
#     }
#     for date, event in zip(scraped_dates, scraped_names)
# ]

# print(event_dict)

driver.quit()