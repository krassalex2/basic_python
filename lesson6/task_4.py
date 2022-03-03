class Car:
    def __init__(self, name, speed, color, is_police):
        self.color = color
        self.name = name
        self.speed = speed
        self.is_police = is_police

    def go(self):
        print(f"{self.name} едет")

    def stop(self):
        print(f"{self.name} останавливается")

    def turn(self, direction):
        print(f"{self.name} поворачивает {direction}")

    def show_speed(self):
        print(f"У автомобиля {self.name} текущая скорость: {self.speed}")


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print("Превышение скорости!!!")


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print("Превышение скорости!!!")


class PoliceCar(Car):
    pass


class SportCar(Car):
    pass


town_car = TownCar("Авто 1", 50, "Красный", False)
work_car = WorkCar("Авто 2", 100, "Красный", False)
police_car = PoliceCar("Авто 3", 50, "Красный", False)
sport_car = SportCar("Авто 4", 50, "Красный", False)

print(f"{town_car.name} полицейская? {'Да' if town_car.is_police else 'Нет'}")
town_car.go()
town_car.stop()
town_car.turn("налево")

town_car.show_speed()
work_car.show_speed()
police_car.show_speed()
sport_car.show_speed()
