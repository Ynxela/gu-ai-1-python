"""Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
"""

from functools import reduce


# 1
def calculate_1(x, y):
    return 1 / x ** abs(y)


# 2
def calculate_2(x, y):
    divider = 1
    for i in range(abs(y)):
        divider *= x
    return 1 / divider


# 3 - если совсем в одну строку :)
calculate_3 = lambda x, y: 1 / reduce(lambda f, s: f * s, [x] * abs(y), 1)

assert calculate_1(121, -123) == calculate_2(121, -123) == calculate_3(121, -123)

print(calculate_1(2, -4))
print(calculate_2(2, -4))
print(calculate_3(2, -4))

print(calculate_1(3, -7))
print(calculate_2(3, -7))
print(calculate_3(3, -7))
