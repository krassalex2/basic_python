# Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число».
# Реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта. Для этого создаёте экземпляры класса (комплексные числа),
# выполните сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.


class ComplexNumber:

    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        real = self.real + other.real
        imaginary = self.imaginary + other.imaginary
        return ComplexNumber(real, imaginary)

    def __sub__(self, other):
        real = self.real - other.real
        imaginary = self.imaginary - other.imaginary
        return ComplexNumber(real, imaginary)

    def __mul__(self, other):
        real = self.real * other.real - self.imaginary * other.imaginary
        imaginary = self.real * other.imaginary + self.imaginary * other.real
        return ComplexNumber(real, imaginary)

    def __truediv__(self, other):
        real = (self.real * other.real + self.imaginary * other.imaginary) / (
                    self.imaginary ** 2 + other.imaginary ** 2)
        imaginary = (self.imaginary * self.real - self.real * other.imaginary) / (
                    self.imaginary ** 2 + other.imaginary ** 2)
        return ComplexNumber(real, imaginary)

    def __str__(self):
        return f'{self.real}{self.imaginary:+}i'

    def __repr__(self):
        return self.__str__()


complex_1 = ComplexNumber(1, -5)
complex_2 = ComplexNumber(5, 2)

print(f'{complex_1} + {complex_2} = {complex_1 + complex_2}')
print(f'{complex_1} - {complex_2} = {complex_1 - complex_2}')
print(f'{complex_1} * {complex_2} = {complex_1 * complex_2}')
print(f'{complex_1} / {complex_2} = {complex_1 / complex_2}')
