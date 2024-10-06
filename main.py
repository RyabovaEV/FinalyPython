import matplotlib.pyplot as plt
from datetime import datetime, timezone

sales_file = []
sales_list = []
food_dict = {}
date_dict = {}

def read_sales_data(file_path):
    """Принимает путь к файлу и возвращает список продаж"""
    sales_file = open(file_path, encoding="UTF8")
    for line in sales_file.readlines():
        product_name, quantity, price, date = line.strip().split(', ')
        sales_list.append({"product_name": product_name,
                           "quantity": int(quantity),
                           "price": int(price),
                           "date": date})
    return sales_list

def total_sales_per_product(sales_list):
    """принимает список продаж и возвращает словарь, где ключ - название продукта, а значение - общая сумма продаж этого продукта"""
    for line in sales_list:
        if line['product_name'] not in food_dict:
            food_dict[line['product_name']] = 0
        food_dict[line['product_name']] += line['price'] * line['quantity']
    return food_dict

def sales_over_time(sales_data):
    """принимает список продаж и возвращает словарь, где ключ - дата, а значение общая сумма продаж за эту дату"""
    for line in sales_list:
        if line['date'] not in date_dict:
            date_dict[line['date']] = 0
        date_dict[line['date']] += line['price'] * line['quantity']
    return date_dict

def get_graf(food_dict,date_dict):
    """Строим графики"""
    # Преводим к типу даты ключи из словаря date_dict
    dates = []
    for key in date_dict:
        dates.append(datetime.strptime(key, '%Y-%m-%d'))

    plt.figure(figsize=(12, 12))
    plt.subplots_adjust(hspace=0.5)

    ax1 = plt.subplot2grid((2, 1), (0, 0), rowspan=1, colspan=1)
    ax2 = plt.subplot2grid((2, 1), (1, 0), rowspan=1, colspan=1)

    # Рисуем первую гистограмму
    ax1.bar(dates, date_dict.values(), align='center', color='r', alpha=0.5)
    ax1.set_title('График общей суммы продаж по дням')
    ax1.set_xlabel('Дата')
    ax1.set_ylabel('Значение')
    ax1.grid(axis='y', linestyle='--')

    # Рисуем вторую гистограмму
    ax2.bar(list(food_dict.keys()), food_dict.values(), align='center', color='b', alpha=0.5)
    ax2.set_title('График общей суммы продаж по каждому продукту')
    ax2.set_xlabel('Наименование продукта')
    ax2.set_ylabel('Количество')
    ax2.grid(axis='y', linestyle='--')

    plt.show()

#вызов функций
read_sales_data(input())
total_sales_per_product(sales_list)
sales_over_time(sales_list)

#Наилучшая выручка
best_product = max(food_dict, key=food_dict.get)
#Наилучшие продажи
best_date = max(date_dict,key=date_dict.get)

#выводим результаты
print("Наилучшую выручку принесли:", best_product)
print("Наилучшие продажи были:", best_date)
get_graf(food_dict,date_dict)



