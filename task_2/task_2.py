"""
2. Задание на закрепление знаний по модулю json. Есть файл orders
в формате JSON с информацией о заказах. Написать скрипт, автоматизирующий
его заполнение данными.

Для этого:
Создать функцию write_order_to_json(), в которую передается
5 параметров — товар (item), количество (quantity), цена (price),
покупатель (buyer), дата (date). Функция должна предусматривать запись
данных в виде словаря в файл orders.json. При записи данных указать
величину отступа в 4 пробельных символа;
Проверить работу программы через вызов функции write_order_to_json()
с передачей в нее значений каждого параметра.

ПРОШУ ВАС НЕ УДАЛЯТЬ ИСХОДНЫЙ JSON-ФАЙЛ
ПРИМЕР ТОГО, ЧТО ДОЛЖНО ПОЛУЧИТЬСЯ

{
    "orders": []
}

вам нужно подгрузить JSON-объект
и достучаться до списка, который и нужно пополнять
а потом сохранять все в файл
"""

import json


def write_order_to_json(item, quantity, price, buyer, date):
    with open('orders.json', 'r', encoding='utf-8') as orders_file:
        orders = json.load(orders_file)
        values = [item, quantity, price, buyer, date]
        temp_dict = dict(zip(orders["orders"][0].keys(), values))
        orders["orders"].append(temp_dict)
        orders_file.close()
    with open('orders.json', 'w', encoding='utf-8') as orders_file:
        json.dump(orders, orders_file, indent=4)


write_order_to_json(1, 2, 3, 4, 5)
write_order_to_json(6, 7, 8, 9, 10)
write_order_to_json(11, 12, 13, 14, 15)
