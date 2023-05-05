import requests
from bs4 import BeautifulSoup


url = "https://www.liebherr.com/en/usa/latest-news/news-press-releases/news-press-releases.html"
res = requests.get(url)
res.raise_for_status()

print(res.status_code)
soup = BeautifulSoup(res.text, "lxml")

article = soup.find_all("article", attrs={"class":"contentColumn"})
print(article)

print(article[0].a.test)