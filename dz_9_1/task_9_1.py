import time


class TrafficLight:
    def __init__(self):
        self.__color = {'красный': 7, 'желтый': 2, 'зеленый': 4}

    def get_running(self):
        while True:
            for colors, delay in self.color.items():
                print(f'загорелся: {colors}')
                time.sleep(delay)


traffic_light = TrafficLight()
print(traffic_light.get_running())