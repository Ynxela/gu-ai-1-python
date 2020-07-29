"""Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса.
Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см*число см толщины полотна. Проверить работу метода.
Например: 20м*5000м*25кг*5см = 12500 т
"""


class Asphalt:
    mass_for_square_meter = 25


class Road:
    material = Asphalt

    def __init__(self, length, width):
        self._width = width
        self._length = length

    def calculate_material_mass_by_thickness(self, thickness) -> int:
        """Возвращает массу материала в тоннах для дороги с толщиной в сантиметрах (thickness)"""
        return self.material.mass_for_square_meter * self._length * self._width * thickness / 1000


road = Road(5000, 20)
mass = road.calculate_material_mass_by_thickness(thickness=5)
print(mass)
assert mass == 12500
