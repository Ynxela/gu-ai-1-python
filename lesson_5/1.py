"""Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка."""

from lesson_5.utils import get_or_create_file

FILENAME = 'file_1.txt'


def user_input(path):
    """Функция построчно записывает в файл ввод пользователя"""

    file = get_or_create_file(path)

    while True:
        try:
            data = input('Введите текст: ') + '\n'

            if not data.strip():
                break

            file.write(data)

        except KeyboardInterrupt:
            file.close()

    file.close()


user_input(FILENAME)
