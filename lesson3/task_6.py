# Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделённых пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре.
# Нужно сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Используйте написанную ранее функцию int_func()

def int_func(word):
    """
    Принимает строку и преобразует первую букву в заглавную
    :param word: Входная строка
    :return: Возвращает входную строку с первой заглавной буквой
    """
    result = []
    for index, w in enumerate(word):
        w = chr(ord(w) - 32) if index == 0 and not is_title_func(w) else w
        result.append(w)
    return "".join(result)


def words_func(words):
    """
    Преобразует строку из слов, делая каждое слово с заглавной буквы
    :param words: Строка из слов
    :return: Возвращает строку с заглавными буквами в каждом слове
    """
    result = []
    words = words.split()
    for index, w in enumerate(words):
        result.append(int_func(w))
    return " ".join(result)


def is_title_func(char):
    """
    Проверяет, является ли уже буква заглавной
    :param char: Проверяемый символ
    :return: Возвращает True, если буква заглавная
    """
    rus = 'ЙЦУКЕНГШЩЗФЫВАПРОЛДЖЭЯЧСМИТЬБЮ'
    eng = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    return True if char in rus or char in eng else False


input_str = "добро пожаловать Иван!"
print(words_func(input_str))
