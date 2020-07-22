"""Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать итоговый массив чисел, соответствующих требованию.
Элементы вывести в порядке их следования в исходном списке.
Для выполнения задания обязательно использовать генератор.
Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
Результат: [23, 1, 3, 10, 4, 11]
"""

uniq = lambda _list: [num for num in _list if _list.count(num) == 1]

uniq_nums = uniq([2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11])

assert uniq_nums == [23, 1, 3, 10, 4, 11]

print(uniq_nums)