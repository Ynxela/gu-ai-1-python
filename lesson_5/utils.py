import os


def get_or_create_file(path):
    if os.path.exists(path):
        file = open(path, 'a+', encoding='utf-8')
    else:
        file = open(path, 'x+', encoding='utf-8')
    return file
