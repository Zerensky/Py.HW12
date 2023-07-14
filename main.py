from pathlib import Path

from student import Student
from factorial import Factorial
from generator import FactGenerator
from rectangle import Rectangle

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

        fg = FactGenerator(3)
        for i in fg:
            print(i)

        rect_1 = Rectangle(2, 5)
        # rect_2 = Rectangle(5, 10)
        # print(rect_2)
        print(rect_1.a)
        print(rect_1.b)
        # rect_1.a = -1
        rect_1.a = 10
        print(rect_1)
        # print(f'{rect.perimeter()= } {rect.area()= }')
        # print(f'{rect_1.perimeter()= } {rect_1.area()= }')
        # res_sum = rect_1 + rect_2
        # print(res_sum.a, res_sum.b)
        # res_sub = rect_1 - rect_2
        # print(res_sub.a, res_sub.b)
        help(rect_1)

        ber = Student("Березовский", "Виктор", "Викторович", Path('lessons.csv'))
        print(ber)
        ber.new_estimate("русский язык", 3)
        ber.new_estimate("химия", 5)
        ber.new_estimate("физика", 3)
        ber.new_estimate("физика", 4)
        ber.new_estimate("математика", 5)
        ber.new_estimate("русский язык", 5)
        ber.new_estimate("химия", 3)
        ber.new_estimate("физика", 5)
        ber.new_estimate("физика", 4)
        ber.new_estimate("математика", 4)
        ber.new_estimate("математика", 69, "тест")
        ber.new_estimate("математика", 99, "тест")
        ber.new_estimate("русский язык", 49, "тест")
        ber.new_estimate("русский язык", 100, "тест")
        ber.new_estimate("обществоведение", 78, "тест")
        ber.new_estimate("обществоведение", 74, "тест")
        ber.new_estimate("химия", 58, "тест")
        ber.new_estimate("химия", 95, "тест")
        print(ber)
        help(ber)