"""Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой."""

print_params = lambda name, surname, year, city, email, phone: print(f'{name} {surname} {year} {city} {email} {phone}')

user1 = {
    'name': 'Aleksandr',
    'surname': 'Sofronov',
    'year': 1992,
    'city': 'Moscow',
    'email': 'hidden',
    'phone': 'hidden'
}

user2 = {
    'name': 'Vasya',
    'surname': 'Ivanov',
    'year': 1990,
    'city': 'Vologda',
    'email': 'hidden',
    'phone': 'hidden'
}

print_params(**user1)
print_params(**user2)
