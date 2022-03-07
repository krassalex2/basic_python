from abc import abstractmethod, ABC


class Clothes(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calculate(self):
        pass


class Coat(Clothes):

    def __init__(self, name, size):
        super().__init__(name)
        self.__size = size

    def __str__(self):
        return f'Пальто: {self.name}. Размер: {self.size}'

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value

    def calculate(self):
        return self.size / 6.5 + 0.5


class Suit(Clothes):

    def __init__(self, name, height):
        super().__init__(name)
        self.__height = height

    def __str__(self):
        return f'Костюм: {self.name}. Рост: {self.height}'

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    def calculate(self):
        return 2 * self.height + 0.3


coat = Coat("Пальто 1", 5)
print(coat)
print(f'Расход ткани: {coat.calculate():.2f}')

suit = Suit("Костюм 1", 10)
print(suit)
print(f'Расход ткани: {suit.calculate():.2f}')
