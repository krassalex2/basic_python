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
        self.items = dict()

    def __str__(self):
        return f'name: {self.name} | address: {self.address}'

    def put(self, item):
        self.items.setdefault(item.__class__, set())
        self.items[item.__class__].add(item)

    def get(self, department, equipment_type):
        item = self.items[equipment_type].pop()
        item.department = department
        return item

    def print_store(self):
        for type_items in self.items.values():
            for item in type_items:
                print(item)


class OfficeEquipment:

    next_id = 0

    def __init__(self, name, brand, weight):
        self.__class__.next_id += 1
        self.next_id = self.__class__.next_id
        self.name = name
        self.brand = brand
        self.weight = weight
        self.department = None

    def __str__(self):
        return f'id: {self.next_id} | name: {self.name} | brand: {self.brand} ' \
               f'| weight: {self.weight} | department: {self.department}'


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
scanner_1 = Scanner('Scanner Phaser 3020', 'Xerox', 5, 300)
xerox = Xerox('Xerox Phaser 5000', 'Xerox', weight=10, printing_technology='scanner', dpi=300)

warehouse.put(printer_1)
warehouse.put(printer_2)
warehouse.put(scanner_1)
warehouse.put(xerox)
warehouse.print_store()

printer = warehouse.get('Production office', Printer)
scanner = warehouse.get('Production office', Scanner)
print()
print(printer)
print(scanner)





