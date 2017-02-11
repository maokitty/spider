from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement

driver = webdriver.PhantomJS("/usr/local/Cellar/phantomjs-2.1.1-macosx/bin/phantomjs")
driver.get("http://pythonscraping.com/pages/itsatrap.html")
links = driver.find_elements_by_tag_name("a")
for link in links:
	if not link.is_displayed():
		print("not display:"+link.get_attribute("href"))
