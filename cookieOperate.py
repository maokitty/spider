from selenium import webdriver
driver = webdriver.PhantomJS(executable_path="/usr/local/Cellar/phantomjs-2.1.1-macosx/bin/phantomjs")
driver.get("http://pythonscraping.com")
driver.implicitly_wait(1)
for cookie in driver.get_cookies():
	for key,value in cookie.items():
		print(key.encode('ascii'))
		print(value)