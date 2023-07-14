"""
Создайте класс-функцию, который считает факториал числа при вызове экземпляра. Экземпляр должен запоминать последние k
значений. Параметр k передаётся при создании экземпляра. Добавьте метод для просмотра ранее вызываемых чисел и их
факториалов.
"""
import json

"""
Доработаем задачу 1. Создайте менеджер контекста, который при выходе сохраняет значения в JSON файл.
"""


class Factorial:
    _content_dict = dict()

    def __init__(self, k: int):
        self.k = k
        self.save_list = list()

    def __call__(self, value):
        res = 1
        for item in range(2, value + 1):
            res *= item
        self.save_list.append(res)
        if len(self.save_list) > self.k:
            self.save_list.pop(0)
        return self.save_list[-1]

    def __str__(self):
        return f'list{self.save_list}'

    def __enter__(self):
        return self

    def mapper(self):
        for item, value in enumerate(self.save_list, start=self.k):
            self._content_dict[item] = value

    def __exit__(self, exc_type, exc_val, exc_tb):
        with open('json_res.json', 'w') as f:
            json.dump(self._content_dict, f, indent=4)


if __name__ == '__main__':
    with Factorial(5) as fact:
        for i in range(10):
            print(fact(i))
        # fact = Factorial(5)
        # print(fact(5))
        # print(fact(6))
        # print(fact(7))
        # print(fact(8))
        # print(fact(9))
        # print(fact(10))
        print(fact.mapper())
        print(fact)

"""
class Fact:
    def __init__(self, k: int):
        self.k = k
        self.save_list = list()

    def __call__(self, value):
        res = 1
        for i in range(2, value + 1):
            res *= i
        self.save_list.append(res)
        if len(self.save_list) > self.k:
            self.save_list.pop(0)
        return self.save_list[-1]

    def __str__(self):
        return f'{self.save_list}'

if __name__ == '__main__':
    fact = Fact(5)
    print(fact(5))
    print(fact(6))
    print(fact(7))
    print(fact(8))
    print(fact(9))
    print(fact(10))
    print(fact)
"""

"""
class Fact:
    _context_dict = dict()

    def __init__(self, k: int):
        self.k = k
        self.save_list = list()

    def __call__(self, value):
        res = 1
        for i in range(2, value + 1):
            res *= i
        self.save_list.append(res)
        if len(self.save_list) > self.k:
            self.save_list.pop(0)
        return self.save_list[-1]

    def __enter__(self):
        return self

    def mapper(self):
        for i, value in enumerate(self.save_list, start=1):
            self._context_dict[i] = value

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.mapper()
        with open('json_res.json', 'w') as f:
            json.dump(self._context_dict, f, indent=2)

    def __str__(self):
        return f'{self.save_list}'


if __name__ == '__main__':
    with Fact(5) as fact:
        # fact = Fact(5)
        print(fact(5))
        print(fact(6))
        print(fact(7))
        print(fact(8))
        print(fact(9))
        print(fact(10))
        print(fact)
        
"""