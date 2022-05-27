from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://localhost:8000")

assert 'The install worked successfully! Congratulations!' in driver.title

driver.quit()