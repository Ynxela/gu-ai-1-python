"""Узнайте у пользователя число n.
Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369."""

num = input('Enter n to get n + nn + nnn: ')

summ = int(num * 3) + int(num * 2) + int(num)

print(summ)
