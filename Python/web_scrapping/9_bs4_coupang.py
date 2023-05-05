import requests
import re
from bs4 import BeautifulSoup

print("hello world11")
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}

url = "https://search.tmon.co.kr/search/?keyword=%EB%85%B8%ED%8A%B8%EB%B6%81&thr=hs&page=1"
res = requests.get(url, headers=headers)
print("hello world22")
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
print(soup)

items = soup.find_all("li", attrs={"class":"item"}) # re.compile("^deal_info")
print(items)

