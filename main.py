from requests import Session
from bs4 import BeautifulSoup
headers = headers = {"User-Agent":
               "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}

work = Session()


work.get("https://quotes.toscrape.com/", headers=headers)

response = work.get("http://quotes.toscrape.com/login", headers=headers)

soup = BeautifulSoup(response.text, "lxml")

token = soup.find("form").find("input").get("value")

data = {"csrf_token": token, "username": "noname", "password": "password"}

result = work.post("http://quotes.toscrape.com/login", headers=headers, data=data, allow_redirects=True)

result = soup.find_all("span", class_="text")
author = soup.find_all("small", class_="author")



