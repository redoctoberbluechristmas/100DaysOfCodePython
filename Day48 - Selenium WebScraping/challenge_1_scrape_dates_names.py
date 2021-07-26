from selenium import webdriver
edge_driver_path = "C:\Development\edgedriver_win64\msedgedriver.exe"
driver = webdriver.Edge(executable_path=edge_driver_path)

# Get dictionary of upcoming events on python.org

dates = []
events = []

driver.get("https://www.python.org/")

scraped_dates = driver.find_elements_by_css_selector(".event-widget time")
for i in scraped_dates:
    dates.append(i.text)

scraped_names = driver.find_elements_by_css_selector(".event-widget li a")
for i in scraped_names:
    events.append(i.text)

event_dict = [
    {
        "Date": date,
        "Event": event,
    }
    for date, event in zip(dates, events)
]

print(event_dict)

driver.quit()