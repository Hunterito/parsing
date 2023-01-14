# Запись информации о товаре в Excel (Код для записи)
import xlsxwriter
from Parsinger8 import array

def writer(array):  # функция, в которую передаётся массив данных array из файла Parsinger7
    book = xlsxwriter.Workbook(r"D:\PyCharm Community Edition 2022.2.4\PARSING\data.xlsx")  # Создание файла для работы
    page = book.add_worksheet("Товар")  # создание страницы таблицы

    row = 0  # строка
    column = 0 # столбец

    page.set_column("A:A", 20)  # Установка ширины колонок
    page.set_column("B:B", 20)
    page.set_column("C:C", 50)
    page.set_column("D:D", 50)

    for item in array():
        # Запись будет производиться с колонки (0:0), т.к на начальном этапе row и column равны 0
        # Запись данных в ячейки по координатам ( Данные: название товара, описание, цена, ссылка на изображение )
        page.write(row, column, item[0])  # Название товара
        page.write(row, column + 1, item[1]) # Цена
        page.write(row, column + 2, item[2]) # Описание
        page.write(row, column + 3, item[3]) # Ссылка на изображение

        row += 1

    book.close()

writer(array)
