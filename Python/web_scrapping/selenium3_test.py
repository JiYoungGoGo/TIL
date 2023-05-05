from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_experimental_option("detach", True) # 브라우저 바로 닫힘 방지
options.add_experimental_option('excludeSwitches', ['enable-logging']) #불필요한 메세지 제거

# 알아서 설치 해준다. 
chrome_driver = ChromeDriverManager().install()

browser = webdriver.Chrome(chrome_driver, options=options)
url = "https://naver.com"

# url 로 이동
browser.get(url)
