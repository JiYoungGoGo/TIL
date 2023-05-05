import requests

# res = requests.get("http://naver.com")
print("hello world")
res = requests.get("http://google.com")
print(res.status_code)

print(len(res.text))

with open("mygoogle.html", "w", encoding="utf8") as f:
    f.write(res.text)
