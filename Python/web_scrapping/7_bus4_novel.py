import requests
from bs4 import BeautifulSoup

url = "https://novel.munpia.com/page/hd.novel/group/nv.regular"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

novels = soup.find_all("a", attrs={"class":"title"})

for novel in novels:
    print(novel.get_text())