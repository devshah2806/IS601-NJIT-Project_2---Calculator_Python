import unittest
from Calculator.Calculator import Calculator
from CsvReader.CsvReader import CsvReader


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_addition(self):
        additionFile = CsvReader('Tests/Data/addition.csv').data
        for row in additionFile:
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_subtraction(self):
        subtractionFile = CsvReader('Tests/Data/subtraction.csv').data
        for row in subtractionFile:
            self.assertEqual(self.calculator.subtract(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_multiplication(self):
        multiplicationFile = CsvReader('Tests/Data/multiplication.csv').data
        for row in multiplicationFile:
            self.assertEqual(self.calculator.multiply(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_division(self):
        divisionFile = CsvReader('Tests/Data/division.csv').data
        for row in divisionFile:
            self.assertEqual(self.calculator.divide(row['Value 1'], row['Value 2']), float(row['Result']))
            self.assertEqual(self.calculator.result, float(row['Result']))

    def test_square(self):
        squareFile = CsvReader('Tests/Data/square.csv').data
        for row in squareFile:
            self.assertEqual(self.calculator.square(row['Value 1']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_SquareRoot(self):
        square_rootFile = CsvReader('Tests/Data/square_root.csv').data
        for row in square_rootFile:
            self.assertEqual(self.calculator.SquareRoot(row['Value 1']), round(float(row['Result']), 8))
            self.assertEqual(self.calculator.result, round(float(row['Result']), 8))

    def tearDown(self) -> None:
        pass


if __name__ == '__main__':
    unittest.main()
