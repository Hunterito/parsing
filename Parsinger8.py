# Полная форма кода для записи в Excel таблицу

import requests
from bs4 import BeautifulSoup
from time import sleep

headers = {"User-Agent":
               "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5 (.NET CLR 3.5.30729)"}

def download(URL):
    resp = requests.get(URL, stream=True) # stream нужен для того чтобы картинка грузилась частями ( в том случае если    картинка весит много, она не будет нагружать память )
    # создание файла
    r = open("D:\\PyCharm Community Edition 2022.2.4\\PARSING\\image\\" + URL.split("/")[-1], "wb") # создается список с адресами, и мы берём последний элемент, который будет выглядеть так xxx.jpg
    for value in resp.iter_content(1024*1024): # iter.content помогает пробежаться по потоку передаваемых данных в переменную resp ( В скобках - кол-во байт, которое будет получено за один проход )
        r.write(value) # запись в файл
    r.close() # закрытие файла

def get_url():
    for count in range(1, 8):
        URL = f"https://scrapingclub.com/exercise/list_basic/?page={count}"
        response = requests.get(URL, headers=headers)
        soup = BeautifulSoup(response.text, "lxml")
        data = soup.find_all("div", class_="col-lg-4 col-md-6 mb-4")
        for i in data:
            card_url = "https://scrapingclub.com" + i.find("a").get(
                "href")
            yield card_url
def array():
    for card_url in get_url():
        response = requests.get(card_url, headers=headers)
        sleep(1)
        soup = BeautifulSoup(response.text, "lxml")
        data = soup.find("div",
                         class_="card mt-4 my-4")
        name = data.find("h3", class_="card-title").text
        price = data.find("h4").text
        text = data.find("p", class_="card-text").text
        url_img = "https://scrapingclub.com" + data.find("img", class_="card-img-top img-fluid").get("src")
        download(url_img)
        yield name, price, text, url_img
