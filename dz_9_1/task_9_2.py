class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def get_mass(self):
        mass = int(self._length * self._width * 25 * 5 / 1000)
        return mass


road_1 = Road(20, 5000)
print(road_1.get_mass())

