class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки", end=' ')


class Pen(Stationery):
    def draw(self):
        super().draw()
        print(f"ручкой c названием {self.title}")


class Pencil(Stationery):
    def draw(self):
        super().draw()
        print(f"карандашом c названием {self.title}")


class Handle(Stationery):
    def draw(self):
        super().draw()
        print(f"маркером c названием {self.title}")


pen = Pen("Ручка")
pencil = Pencil("Карандаш")
handle = Handle("Маркер")

pen.draw()
pencil.draw()
handle.draw()
