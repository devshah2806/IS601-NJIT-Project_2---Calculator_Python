from Calculator.Addition import addition
from Calculator.Division import division


def mean(mean_list):
    try:
        total = 0
        for num in mean_list:
            total = addition(total, num)
        return int(division(len(mean_list), total))
    except ZeroDivisionError:
        print("Error: Cannot Divide by 0")
    except ValueError:
        print("Check your Data Input")
