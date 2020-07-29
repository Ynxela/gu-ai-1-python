"""Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный.
В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
третьего (зеленый) — на ваше усмотрение
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов,
и при его нарушении выводить соответствующее сообщение и завершать скрипт.
"""

from collections import deque
from time import sleep


class Color:
    def __init__(self, color, delay):
        self._color = color
        self._delay = delay

    def info(self):
        print(f'{self._color} свет горит {self._delay} секунд.')

    def sleep(self):
        sleep(self._delay)


class TrafficLight:
    __color = deque(
        (
            Color('красный', 7),
            Color('желтый', 2),
            Color('зеленый', 4)
        )
    )

    def running(self):
        while True:
            self._switch_color()

    def _switch_color(self):
        color = self.__color.popleft()
        color.info()
        color.sleep()
        self.__color.append(color)


tl = TrafficLight()
tl.running()
