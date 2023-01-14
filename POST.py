from requests import Session  # импортируем класс "Сессия" для сохранения файлов cookie
from bs4 import BeautifulSoup
from time import sleep

# POST запрос содаёт словарь с логином и паролем ( {username: "123"}, например)
# Нам нужно получить token, котоырй появляется при регистрации
headers = {"User-Agent":
               "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5 (.NET CLR 3.5.30729)"}

work = Session()  # подключаем класс

work.get("https://quotes.toscrape.com/", headers=headers) # Сначала заходим на сайт, а уже потом в тот раздел, где расположена регистрация

response = work.get("https://quotes.toscrape.com/login", headers=headers)

soup = BeautifulSoup(response.text, "lxml")

TOKEN = soup.find("form").find("input").get("value") # поиск токена на сайте ( токен является одноразовым )

# передача пост-запроса
data = {"csrf_token": TOKEN,
        "username": "noname",
        "password": "password"} # создаём словарь с информацией о пользователе. А также добавляем изменяемый токен

result = work.post("https://quotes.toscrape.com/login", headers=headers, data=data, allow_redirects=True).text
# создание пост-запроса. Словарь data передаётся в закрытой форме, а последний аргумент функции post() является разрешением на то, чтобы сайт мог переносить нас на уже зарегистрированную страницу


