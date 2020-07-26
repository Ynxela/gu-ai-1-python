"""Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""

from random import randint, choice

DIRECTIONS = ('налево', 'направо')
COLORS = ('черный', 'белый', 'красный', 'зеленый', 'синий', 'серый')


class Car:
    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self._speed = speed
        self.is_police = is_police
        self._is_driving = False

    def go(self):
        print('Автомобиль начал движение')
        self._is_driving = True

    def stop(self):
        print('Автомобиль остановился')
        self._is_driving = False

    def turn(self, direction):
        print(f'Автомобиль повернул в направлении: {direction}')

    def show_speed(self):
        if self._is_driving:
            print(f'Скорость автомобиля: {self._speed}')
        else:
            print('Автомобиль стоит на месте')


class RestrictedSpeed:

    @property
    def max_speed(self):
        raise NotImplementedError

    def show_speed(self):
        super().show_speed()
        if self._is_driving and self._speed > self.max_speed:
            print('Скорость превышена!')


class TownCar(RestrictedSpeed, Car):
    max_speed = 60


class SportCar(Car):
    pass


class WorkCar(RestrictedSpeed, Car):
    max_speed = 40


class PoliceCar(Car):
    pass


cars = [
    TownCar('Lexus', choice(COLORS), randint(40, 150)),
    SportCar('Ferrari', choice(COLORS), randint(50, 200)),
    WorkCar('БелАз', choice(COLORS), randint(30, 90)),
    PoliceCar('BMW', choice(COLORS), randint(70, 160), True)
]

for car in cars:
    print('-' * 20)
    print('Название:', car.name)
    print('Цвет:', car.color)
    print('Полиция:', car.is_police)

    print('*')
    car.show_speed()
    car.go()
    car.show_speed()
    car.turn(choice(DIRECTIONS))
    car.stop()
    car.show_speed()
