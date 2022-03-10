# Начните работу над проектом «Склад оргтехники».
# Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определите параметры, общие для приведённых типов.
# В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.

# Продолжить работу над первым заданием.
# Разработайте методы, которые отвечают за приём оргтехники на склад и передачу в определённое подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
# можно использовать любую подходящую структуру (например, словарь).

# Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.


class Warehouse:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return f'name: {self.name} | address: {self.address}'


class OfficeEquipment:
    def __init__(self, name, brand, weight):
        self.name = name
        self.brand = brand
        self.weight = weight

    def __str__(self):
        return f'name: {self.name} | brand: {self.brand} | weight: {self.weight}'


class Printer(OfficeEquipment):
    def __init__(self, name, brand, weight, printing_technology):
        super().__init__(name, brand, weight)
        self.printing_technology = printing_technology

    def __str__(self):
        return f'{super().__str__()}  | printing_technology: {self.printing_technology}'


class Scanner(OfficeEquipment):
    def __init__(self, name, brand, weight, dpi):
        super().__init__(name, brand, weight)
        self.dpi = dpi

    def __str__(self):
        return f'{super().__str__()}  | dpi: {self.dpi}'


class Xerox(OfficeEquipment):
    def __init__(self, name, brand, weight, printing_technology, dpi):
        super().__init__(name, brand, weight)
        self.printing_technology = printing_technology
        self.dpi = dpi

    def __str__(self):
        return f'{OfficeEquipment.__str__(self)} | printing_technology: {self.printing_technology}  | dpi: {self.dpi}'


warehouse = Warehouse('Северный', 'г. Москва, улица Васи Пупкина')
printer_1 = Printer('Brother HL-1110R', 'Brother', 5.3, 'laser')
printer_2 = Printer('Xerox Phaser 3020', 'Xerox', 5, 'laser')
scanner_1 = Scanner('Xerox Phaser 3020', 'Xerox', 5, 300)
xerox = Xerox('Xerox Phaser 3020', 'Xerox', weight=10, printing_technology='scanner', dpi=300)

print(warehouse)
print(printer_1)
print(printer_2)
print(scanner_1)
print(xerox)
