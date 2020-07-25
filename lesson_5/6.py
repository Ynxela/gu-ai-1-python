"""Необходимо создать (не программно) текстовый файл,
где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести словарь на экран.

Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб).
                     Физика:   30(л)   —   10(лаб)
                     Физкультура:   —   30(пр)   —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""
from pprint import pprint

FILENAME = 'file_6.txt'
import re

re_num = re.compile('\d+')


def get_total_lessons(path) -> dict:
    """
    Функция читает файл и возвращает словарь с ключами - названиями предмета и значениями - общим количеством занятий.
    Типов занятий может быть неограниченное количество.
    """
    with open(path, 'r', encoding='utf-8') as f:
        subj_dict = {}
        subjects = f.readlines()
        for subject in subjects:
            subj, *lessons = subject.split()

            total_lessons = [
                int(re_num.search(lesson).group(0))
                for lesson in filter(lambda lesson: re_num.search(lesson), lessons)
            ]

            subj_dict[subj.replace(':', '')] = sum(total_lessons)

        return subj_dict


data = get_total_lessons(FILENAME)

pprint(data)
