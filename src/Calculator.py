import math
from CsvReader import CsvReader


def addition(a, b):
    a = int(a)
    b = int(b)
    c = a + b
    return c


def subtraction(a, b):
    a = int(a)
    b = int(b)
    c = b - a
    return c


def multiplication(a, b):
    a = int(a)
    b = int(b)
    c = a * b
    return c


def division(a, b):
    a = int(a)
    b = int(b)
    if b != 0:
        c = b / a
        return round(c, 9)
    else:
        return print('Denominator cannot be Zero')


def squares(a):
    a = int(a)
    c = a * a
    return c


def SquaresRoot(a):
    a = int(a)
    c = math.sqrt(a)
    return round(float(c), 8)


class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = multiplication(a, b)
        return self.result

    def divide(self, a, b):
        self.result = division(a, b)
        return self.result

    def square(self, a):
        self.result = squares(a)
        return self.result

    def SquareRoot(self, a):
        self.result = SquaresRoot(a)
        return self.result


class CSVStats(Calculator):
    data = []

    def __init__(self, data_file):
        self.data = CsvReader(data_file)
        pass
