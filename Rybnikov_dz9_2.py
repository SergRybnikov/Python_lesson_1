
class Road:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def count(self):
        self.weigth = 25
        self.tickness = 0.05
        count = self.length * self.width * self.weigth * self.tickness / 1000
        print(f'Необходимо {count} тонн для строительства.')

road = Road(20000, 5)
road.count()