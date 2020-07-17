"""Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.

Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.

Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].
"""

rating = [9, 7, 1]

while True:
    new_element = int(input('Enter new rating: '))
    if new_element in rating:
        new_element_count = rating.count(new_element)
        idx = rating.index(new_element) + new_element_count
        rating.insert(idx, str(new_element))
        print(rating)
        rating[idx] = int(rating[idx])
    else:
        for e_idx, element in enumerate(rating):
            if element < new_element:
                rating.insert(e_idx, str(new_element))
                print(rating)
                rating[e_idx] = int(rating[e_idx])
                break
            elif e_idx != len(rating) - 1:
                continue
            rating.append(str(new_element))
            last_idx = len(rating) - 1
            print(rating)
            rating[last_idx] = int(rating[last_idx])
            break
