class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} поехала')

    def stop(self):
        print(f'{self.name} остановилась')

    def turn(self, side):
        print(f'{self.name} повернула на {side}')

    def show_speed(self):
        print(f'{self.name} едет со скоростью {self.speed}')


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('Превышен лимит сорости 60')


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print('Превышен лимит сорости 60')


class SportCar(Car):
    pass


class PoliceCar(Car):
    def designed(self):
        if self.is_police is True:
            print('Это полицейская машина')


work_car = WorkCar(70, 'black', 'Рабочая машина Toyta', False)
town_car = TownCar(50, 'blue', 'Рабочая машина Volga', False)
sport_car = SportCar(160, 'red', 'Спортивная машина Honda', False)
police_car = PoliceCar(160, 'white-blu', 'Полицейская машина YAZ', True)

work_car.go()
work_car.show_speed()
work_car.turn('лево')
work_car.stop()
