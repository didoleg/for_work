class Stationery:
    def __init__(self, name):
        self.title = name

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(f'{self.title} пишет')


class Pencil(Stationery):
    def draw(self):
        print(f'{self.title} чертит')


class Handle(Stationery):
    def draw(self):
        print(f'{self.title} рисует')


pen = Pen('Ручка')
pencil = Pencil('Карандаш')
handle = Handle('Маркер')

pen.draw()
pencil.draw()
handle.draw()
