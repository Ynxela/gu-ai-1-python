"""Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции."""

num = int(input('Enter natural number: '))
max_digit = 0
while num != 0:
    last_digit = num % 10
    if last_digit > max_digit:
        max_digit = last_digit
    num //= 10

print(f'Max digit is {max_digit}')
