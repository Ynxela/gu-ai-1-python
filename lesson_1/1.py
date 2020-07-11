"""Поработайте с переменными, создайте несколько, выведите на экран,
запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран."""

first = 100
second = 'foo'

print(f'first: {first}, second: {second}')

user_name = input('Enter your name: ')
user_age = int(input('How old are you? '))

print(f'Hello, {user_name}! Next year you will celebrate your {user_age + 1} B-day!')
