"""Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов."""


def my_func(one, two, tree):
    params = [one, two, tree]
    params.remove(min(params))
    return sum(params)


result = my_func(1, -1, 3)
print(result)
