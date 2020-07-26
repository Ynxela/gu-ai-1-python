"""Реализовать базовый класс Worker (работник), в котором определить атрибуты:
name, surname, position (должность), income (доход).

Последний атрибут должен быть защищенным и ссылаться на словарь,
содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.

Создать класс Position (должность) на базе класса Worker.

В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода
с учетом премии (get_total_income).

Проверить работу примера на реальных данных
(создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров)."""


class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return sum(self._income.values())


workers = [
    Position('John', 'Doe', 'Middle Python developer', 120000, 20000),
    Position('Mister', 'Freeman', 'Junior JS developer', 50000, 10000)
]

for worker in workers:
    print('-' * 20)
    print(worker.get_full_name())
    print(worker.position)
    print(worker.get_total_income())
