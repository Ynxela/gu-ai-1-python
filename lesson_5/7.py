"""Создать вручную и заполнить несколькими строками текстовый файл,
в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1   ООО   10000   5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.

Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]"""

import json
from pprint import pprint

FILENAME = 'file_7.txt'
OUTPUT_FILENAME = 'audition.json'


def write_json(data, path):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def get_audition(companies_file, output_file):
    """
    Фирма считает прибыли для всех компаний и среднюю прибыль для прибыльных компаний.
    Записывает данные в файл в формате json.
    """
    with open(companies_file, encoding='utf-8') as f:
        audition = [{}]
        companies_data = f.readlines()
        total_profit = 0
        profit_companies = 0
        for company in companies_data:
            *name, opf, income, costs = company.split()
            name = ' '.join(name)

            income = int(income)
            costs = int(costs)
            profit = income - costs

            if profit > 0:
                total_profit += profit
                profit_companies += 1

            audition[0][name] = profit

        audition.append(
            dict(average_profit=round(total_profit / profit_companies, 2))
        )

        write_json(audition, output_file)

    return audition


audition = get_audition(FILENAME, OUTPUT_FILENAME)

pprint(audition)
