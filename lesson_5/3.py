"""Создать текстовый файл (не программно),
построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32
"""
from pprint import pprint

FILENAME = 'file_3.txt'
THRESHOLD = 20000


def filter_income(file_with_incomes: str, threshold: int) -> dict:
    """
    Функция читает файл с доходами, находит всех сотрудников,
    которые получают доход ниже указанного и считает средний доход
    """
    with open(file_with_incomes, encoding='utf-8') as f:
        employees = [(item[0], int(item[1])) for item in map(lambda itm: itm.strip().split(), f.readlines())]
        employees.sort(key=lambda item: item[1], reverse=True)
        income_less_than_threshold = list(filter(lambda item: item[1] < threshold, employees))
        average_income = round(sum([item[1] for item in employees]) / len(employees), 2)

        return {
            'threshold': threshold,
            'average_income': average_income,
            'income_less_than_threshold': income_less_than_threshold
        }


income_data = filter_income(FILENAME, THRESHOLD)

pprint(income_data)
