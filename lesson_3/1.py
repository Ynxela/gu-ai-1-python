"""Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль."""


def division(num_1, num_2):
    try:
        return num_1 / num_2
    except ZeroDivisionError:
        return float('inf')


first = float(input('введите 1 число: '))
second = float(input('введите 2 число: '))

quotient = division(first, second)

print(quotient)
