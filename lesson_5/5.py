"""Создать (программно) текстовый файл, записать в него программно набор чисел,разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран."""

from lesson_5.utils import get_or_create_file

FILENAME = 'file_5.txt'


def sum_file_nums(path):
    """Функция выводит сумму всех чисел, введенных пользователем и записанных в указанный файл"""
    file = get_or_create_file(path)
    while True:
        data = ' ' + input('Введите числа, разделенные пробелами или пустую строку для выхода: ').strip()
        if not data.strip():
            break
        file.write(data)
        file.seek(0)
        nums = (int(num) for num in file.readline().split())
        print(f'Сумма всех числе в файле: {sum(nums)}')
    file.close()


sum_file_nums(FILENAME)
