import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service # 셀레니움 버전 4에서는 이걸 써야 한다. 
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_experimental_option("detach", True) # 브라우저 바로 닫힘 방지
options.add_experimental_option('excludeSwitches', ['enable-logging']) #불필요한 메세지 제거

service = Service(ChromeDriverManager().install())

browser = webdriver.Chrome(service=service, options=options)
url = "https://naver.com"

# url 로 이동
browser.get(url)

elem = browser.find_element(By.CLASS_NAME, "link_login")
elem.click()
browser.back()
time.sleep(1)

"""
<input id="query" name="query" type="search" title="검색어 입력"
maxlength="255" class="input_text" tabindex="1" accesskey="s"
style="ime-mode:active;" autocomplete="off" placeholder="검색어를 입력해 주세요."
onclick="document.getElementById('fbm').value=1;" value="" data-atcmp-element="">
"""

browser.find_element(By.CLASS_NAME, "input_text").send_keys("블랙핑크")
time.sleep(1)

browser.find_element(By.ID, "query").send_keys("뉴진스")
time.sleep(1)
browser.find_element(By.NAME, "query").send_keys("트와이스")

time.sleep(1)
browser.find_element(By.CSS_SELECTOR, "#query").send_keys("에스파")

time.sleep(1)

# CSS_SELECTOR 이걸 가장 많이 쓴다. 
browser.find_element(By.CSS_SELECTOR, "[title='검색어 입력']").send_keys("르세라핌")
time.sleep(1)

browser.find_element(By.CSS_SELECTOR, "[placeholder='검색어를 입력해 주세요.']").send_keys("아이들")
time.sleep(1)

browser.find_element(By.XPATH, '//*[@id="query"]').send_keys("하입보이")
time.sleep(1)

"""
<a href="https://shoppinglive.naver.com/home" class="nav shoplive" 
data-clk="svc.shoppinglive">
<span class="blind">쇼핑LIVE</span>
</a>
"""
browser.find_element(By.LINK_TEXT, "쇼핑LIVE").click()
time.sleep(1)

browser.find_element(By.PARTIAL_LINK_TEXT, "핑LI").click()
time.sleep(1)

navs = browser.find_elements(By.CSS_SELECTOR, ".nav_item")

for nav in navs:
    print(nav.get_attribute("outerHTML"))
    print()