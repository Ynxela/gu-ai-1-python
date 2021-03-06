"""Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел,
то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу."""


def summator():
    _sum = 0
    flag = True
    while flag:
        nums = input('Введите числа через пробел или q для выхода: ')
        if 'q' in nums:
            idx = nums.index('q')
            nums = nums[:idx]
            flag = False
        _sum += sum([float(num) for num in nums.split()])
        print(f'Сумма: {_sum}')
    return _sum


summator()
