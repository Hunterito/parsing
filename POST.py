from requests import Session  
from bs4 import BeautifulSoup
from time import sleep


headers = {"User-Agent":
               "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5 (.NET CLR 3.5.30729)"}

work = Session() 

work.get("https://quotes.toscrape.com/", headers=headers) 

response = work.get("https://quotes.toscrape.com/login", headers=headers)

soup = BeautifulSoup(response.text, "lxml")

TOKEN = soup.find("form").find("input").get("value") # поиск токена на сайте ( токен является одноразовым )

# передача пост-запроса
data = {"csrf_token": TOKEN,
        "username": "noname",
        "password": "password"}

result = work.post("https://quotes.toscrape.com/login", headers=headers, data=data, allow_redirects=True).text
