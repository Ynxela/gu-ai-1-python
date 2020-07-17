"""Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.

Продолжить работу над заданием.
В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func()."""


# 1
def int_func(word):
    min_pos, max_pos = ord('a'), ord('z')
    for letter in word:
        if not min_pos <= ord(letter) <= max_pos:
            raise ValueError('You should use letters in range a-z')
    return word.title()


titled = int_func('today')
print(titled)

# 2
multiple_titling = lambda _string: ' '.join([int_func(word) for word in _string.split()])

string = multiple_titling('today was a good day')
print(string)
