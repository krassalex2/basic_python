# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде
# строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с
# декоратором @classmethod.
# Он должен извлекать число, месяц, год и преобразовывать их тип
# к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на
# реальных данных.


class Date:
    def __init__(self, date_str):
        self.date_str = date_str
        if not Date.validate(date_str):
            raise ValueError('Ошибка валидации даты. Объект не создан')
        self.__tuple_date = Date.parse(self.date_str)

    # В текущей реализации было бы достаточно @staticmethod, так как глобальные атрибуты классы не используются.
    # Для чтения даты использовать их не рационально, так как они общие для всех экземпляров класса.
    @classmethod
    def parse(cls, date_str):
        try:
            return tuple([int(item) for item in date_str.split('-')])
        except:
            raise ValueError('Не удалось разобрать дату.')

    @staticmethod
    def validate(input_date):

        tuple_date = Date.parse(input_date)

        if len(tuple_date) != 3:
            return False

        day, month, year = tuple_date

        # Валидация пока по упрощенной схеме
        if day < 1 or day > 31:
            return False
        if month < 1 or month > 12:
            return False
        if year < 1 or year > 9999:
            return False

        return True

    @property
    def day(self):
        return self.__tuple_date[0]

    @property
    def month(self):
        return self.__tuple_date[1]

    @property
    def year(self):
        return self.__tuple_date[2]

    def __str__(self):
        return f'{self.day}-{self.month}-{self.year}'


try:
    print('Проверка первой даты')
    date1 = Date('03-09-2022')
    print(date1)
except ValueError as ex:
    print(ex)
else:
    print('Успешно')


try:
    print('Проверка второй даты')
    date2 = Date('2022-09-03')
    print(date2)
except ValueError as ex:
    print(ex)
else:
    print('Успешно')



