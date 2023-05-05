import requests
from bs4 import BeautifulSoup

url = "https://novel.munpia.com/345463"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

novels = soup.find_all("td", attrs={"class":"subject"})
# title = comics[6].a.get_text()
# link = comics[6].a["href"]
# print(title)
# print("https://novel.munpia.com"+ link)

# for novel in novels:
#     title = novel.a.get_text()
#     link = "https://novel.munpia.com"+ novel.a["href"]
#     print(title, link)

# 추천 구하기
total_up = 0
novels = soup.find_all("span", attrs={"class":"up"})
for novel in novels:
    up = novel.get_text()
    print(up)
    total_up += float(up)

print("평균추천 : ", total_up / len(novels))