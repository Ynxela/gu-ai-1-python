"""Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.”
Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов метод должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра."""


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(f'Вы взяли инструмент: {self.title}. Он прекрасно подходит для записей!')


class Pencil(Stationery):
    def draw(self):
        print(f'В ваших руках: {self.title}. Сделайте скетч!')


class Handle(Stationery):
    def draw(self):
        print(f'{self.title.title()}. Напишите что-нибудь на маркерной доске!')


stationeries = [
    Pen('ручка'),
    Pencil('карандаш'),
    Handle('маркер'),
]

for st in stationeries:
    print('-' * 20)
    st.draw()
