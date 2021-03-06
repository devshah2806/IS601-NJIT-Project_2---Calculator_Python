from Calculator.Division import division
from Calculator.Multiplication import multiplication
from Calculator.Squares import squares
from Calculator.SquaresRoot import SquaresRoot
from Calculator.Subtraction import subtraction
from CsvReader import CsvReader
from Calculator.Addition import addition


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
        super().__init__()
        self.data = CsvReader.CsvReader(data_file)
