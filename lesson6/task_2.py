class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculate(self):
        print(f"Масса асфальта: {self._length * self._width * 25 * 5} кг.")


road = Road(20, 5000)
road.calculate()
