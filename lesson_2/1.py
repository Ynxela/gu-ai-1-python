"""Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента.
Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе."""

my_list = ['string', True, None, [1, 2, 3], (1, 0), {0, 1}, {'f': 'first'}, 100, 100.1, 1 + 2j, type, b'0']

for item in my_list:
    print(type(item))
