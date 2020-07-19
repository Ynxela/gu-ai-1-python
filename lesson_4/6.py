"""Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
"""

from datetime import timedelta, datetime
from itertools import count, cycle


# a
def generate_nums(start):
    for num in count(start):
        yield num
        if num == start + 10:
            return


gen = generate_nums(10)

for num in gen:
    print(num)

print('-' * 50)

# b
waves = ['_', '_' * 2, '_' * 3, '_' * 4, '_' * 5, '_' * 6, '_' * 5, '_' * 4, '_' * 3, '_' * 2]


def repeater(iterable):
    start_time = datetime.now()
    delta = timedelta(seconds=0.1)
    stop = start_time + delta
    for el in cycle(iterable):
        if stop < datetime.now():
            return
        yield el


rep = repeater(waves)

for el in rep:
    print(el)
