"""Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict. """

q1 = 'winter'
q2 = 'spring'
q3 = 'summer'
q4 = 'autumn'

month_mapping = {
    1: q1,
    2: q1,
    3: q2,
    4: q2,
    5: q2,
    6: q3,
    7: q3,
    8: q3,
    9: q4,
    10: q4,
    11: q4,
    12: q1
}

month_mapping_list = [q1, q1, q2, q2, q2, q3, q3, q3, q4, q4, q4, q1]

month_num = int(input('Enter number of month: '))

print(month_mapping[month_num])
print(month_mapping_list[month_num - 1])
