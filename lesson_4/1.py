"""Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами."""

from sys import argv


def calculate_salary(args):
    _, hours, rate, bonus, *others = args
    return (int(hours) * int(rate)) + int(bonus)


salary = calculate_salary(argv)

print(salary)
