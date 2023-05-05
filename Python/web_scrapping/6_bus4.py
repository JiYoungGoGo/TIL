import requests
from bs4 import BeautifulSoup

url = "https://www.munpia.com/"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
print(soup.title)
print(soup.title.get_text())
print(soup.div)
print(soup.div.attrs) # 속성
print(soup.div["id"]) # 속성값 출력

# print(soup.find("section")) # 처음으로 발견되는 엘리먼트를 가져온다. 
# print(soup.find(attrs={"id":"main-best-platinum"})) # 처음으로 발견되는 엘리먼트를 가져온다. 

rank1 = soup.find("li", attrs={"class":"hero"})

# print(rank1.p.get_text())
rank2 = rank1.next_sibling.next_sibling # 개행 같은 거 때문에, sibiling 을 두번 해줘야 할 때가 있다. 
rank3 = rank2.next_sibling.next_sibling
# print(rank3)
# print(rank3.previous_sibling.previous_sibling)

# print(rank1.parent)

# print(rank1.find_next_sibling("li")) # 이러면 개행정보는 제외하고 li 만 찾는다. 
# print(rank2.span.get_text())

# print(rank1.find_next_siblings("li")) # 형제를 모두 찾는다. 

novel = soup.find("span", text="짐꾼이었던 내가 마력이 무한?")
print(novel)