"""Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк. """

seconds = int(input('Enter a seconds: '))

hours = seconds // 3600
seconds -= hours * 3600
minutes = seconds // 60
seconds -= minutes * 60

print(
    f'{hours if hours > 9 else f"0{hours}"}:'
    f'{minutes if minutes > 9 else f"0{minutes}"}:'
    f'{seconds if seconds > 9 else f"0{seconds}"}'
)
