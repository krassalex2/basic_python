class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return self._income.get("wage") + self._income.get("bonus")


position1 = Position("Иван", "Петров", "Дворник", 100000, 10000)
print("Должность:", position1.surname)
print("Полное имя:", position1.get_full_name())
print("Полный оклад:", position1.get_total_income(), "\n")

position2 = Position("Иван", "Сидоров", "Помощник дворника", 50000, 5000)
print("Должность:", position2.surname)
print("Полное имя:", position2.get_full_name())
print("Полный оклад:", position2.get_total_income())
