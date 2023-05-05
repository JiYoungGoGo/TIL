from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome() 
browser.get("http://naver.com")

elem = browser.find_element(By.CLASS_NAME, "link_login")
elem.click()

browser.find_element(By.XPATH)