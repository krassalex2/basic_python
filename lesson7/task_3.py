class Cell:

    def __init__(self, count_cell):
        self.count_cell = count_cell

    def __add__(self, other):
        return Cell(self.count_cell + other.count_cell)

    def __sub__(self, other):
        diff = self.count_cell - other.count_cell
        if diff < 0:
            return 'Ошибка вычитания!'
        return Cell(diff)

    def __mul__(self, other):
        return Cell(self.count_cell * other.count_cell)

    def __floordiv__(self, other):
        return Cell(self.count_cell // other.count_cell)

    def make_order(self, items_in_row):
        result = ''
        for _ in range(self.count_cell // items_in_row):
            result += f'{"*" * items_in_row}\n'
        result += "*" * (self.count_cell % items_in_row)
        return result


cell1 = Cell(10)
cell2 = Cell(5)

print(f'{(cell1 + cell2).make_order(3)}\n')
print(f'{(cell1 - cell2).make_order(4)}\n')
print(f'{(cell1 * cell2).make_order(10)}\n')
print(f'{(cell1 // cell2).make_order(3)}\n')
