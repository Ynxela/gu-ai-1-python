"""Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке."""

FILENAME = 'file_2.txt'


def count_rows_and_words(path):
    """Функция считает количество строк и слов в каждой строке"""
    with open(path, encoding='utf-8') as f:
        rows = f.readlines()
        rows_count = len(rows)
        print('Количество слов в строках: ')
        for count, string in enumerate(rows, 1):
            print(f'В {count} строке: {len(string.split())}.')
        print('Общее количество строк:', rows_count)


count_rows_and_words(FILENAME)
