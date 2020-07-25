"""Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""
from lesson_5.utils import get_or_create_file

FILENAME = 'file_4.txt'
NEW_FILENAME = 'file_4_1.txt'

words_mapping = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре'
}


def get_row(sp):
    return sp.readline().strip()


def rewrite_translated(source_path, destination_path):
    """
    Функция осуществяет перевод из файла с английского языка на русский и записывает новые данные в указанный файл.
    """
    destination_file = get_or_create_file(destination_path)
    with open(source_path, encoding='utf-8') as sp:
        row = get_row(sp)
        while row:
            row = row.split()
            row[0] = words_mapping[row[0].lower()].title()
            row = ' '.join(row) + '\n'

            destination_file.write(row)

            row = get_row(sp)

    destination_file.close()


rewrite_translated(FILENAME, NEW_FILENAME)
