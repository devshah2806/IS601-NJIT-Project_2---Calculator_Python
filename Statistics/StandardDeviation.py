from Calculator.Addition import addition
from Calculator.Subtraction import subtraction
from Calculator.Division import division
from Calculator.SquaresRoot import SquaresRoot
from Calculator.Squares import squares
from Statistics.Mean import mean


def sd(a):
    try:
        total = 0
        Mean = mean(a)
        for val in a:
            total = addition(squares(subtraction(Mean, val)), total)
            result = SquaresRoot(division(len(a), total))
        return int(result)
    except ZeroDivisionError:

        print("Error: Cannot Divide by 0")

    except ValueError:

        print("Check your Data Input")
