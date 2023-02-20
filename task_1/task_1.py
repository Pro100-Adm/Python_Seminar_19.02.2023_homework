"""
1. Задание на закрепление знаний по модулю CSV. Написать скрипт,
осуществляющий выборку определенных данных из файлов info_1.txt, info_2.txt,
info_3.txt и формирующий новый «отчетный» файл в формате CSV.

Для этого:

Создать функцию get_data(), в которой в цикле осуществляется перебор файлов
с данными, их открытие и считывание данных. В этой функции из считанных данных
необходимо с помощью регулярных выражений извлечь значения параметров
«Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
Значения каждого параметра поместить в соответствующий список. Должно
получиться четыре списка — например, os_prod_list, os_name_list,
os_code_list, os_type_list. В этой же функции создать главный список
для хранения данных отчета — например, main_data — и поместить в него
названия столбцов отчета в виде списка: «Изготовитель системы»,
«Название ОС», «Код продукта», «Тип системы». Значения для этих
столбцов также оформить в виде списка и поместить в файл main_data
(также для каждого файла);

Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл.
В этой функции реализовать получение данных через вызов функции get_data(),
а также сохранение подготовленных данных в соответствующий CSV-файл;

Пример того, что должно получиться:

Изготовитель системы,Название ОС,Код продукта,Тип системы

1,LENOVO,Windows 7,00971-OEM-1982661-00231,x64-based

2,ACER,Windows 10,00971-OEM-1982661-00231,x64-based

3,DELL,Windows 8.1,00971-OEM-1982661-00231,x86-based

Обязательно проверьте, что у вас получается примерно то же самое.

ПРОШУ ВАС НЕ УДАЛЯТЬ СЛУЖЕБНЫЕ ФАЙЛЫ TXT И ИТОГОВЫЙ ФАЙЛ CSV!!!
"""

import csv,re


#os_prod_list.append(os_prod_reg.findall(data)[0].split()[2])
def get_data():
    system_vendor = re.compile(r'Изготовитель системы:\s*\S*')
    os_name = re.compile(r'Название ОС:\s*\S*\s?\S*\s?\S*\s?\S*')
    os_product_key = re.compile(r'Код продукта:\s*\S*')
    os_type = re.compile(r'Тип системы:\s*\S*')
    system_vendor_list, os_name_list, os_product_key_list, os_type_list = [], [], [], []

    for i in range(3):
        with open(f"info_{i+1}.txt") as csv_table:
            csv_table_reader = csv.reader(csv_table)
            for row in csv_table_reader:
                if len(system_vendor.findall(row[0])):
                    system_vendor_list.append(f"{system_vendor.findall(row[0])[0].split()[2]}")
                if len(os_name.findall(row[0])):
                    os_name_list.append(f"{os_name.findall(row[0])[0].split()[3]}"
                                        f" {os_name.findall(row[0])[0].split()[4]}")
                if len(os_product_key.findall(row[0])):
                    os_product_key_list.append(f"{os_product_key.findall(row[0])[0].split()[2]}")
                if len(os_type.findall(row[0])):
                    os_type_list.append(f"{os_type.findall(row[0])[0].split()[2]}")

    result_data = []
    for i in range(len(system_vendor_list)):
        result_data.append({})
        result_data[i].update({"№": i})
        result_data[i].update({"Изготовитель системы":system_vendor_list[i]})
        result_data[i].update({"Название ОС": os_name_list[i]})
        result_data[i].update({"Код продукта": os_product_key_list[i]})
        result_data[i].update({"Тип системы": os_type_list[i]})
    return result_data

def write_to_csv(filename):
    result_data = get_data()
    with open(filename, 'w') as f_n:
        F_N_WRITER = csv.DictWriter(f_n, fieldnames=list(result_data[0].keys()),
                                    quoting=csv.QUOTE_NONNUMERIC)
        F_N_WRITER.writeheader()
        for result in result_data:
            F_N_WRITER.writerow(result)

write_to_csv('result.csv')

