class Road:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def get_mass(self, deep=1):
        mass = int((self.__length * self.__width * 25 * deep) / 1000)
        return mass


road_1 = Road(20, 5000)
print(road_1.get_mass(5))

