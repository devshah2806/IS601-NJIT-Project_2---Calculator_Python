import statistics


def variance(variance_list):
    try:
        result = statistics.variance(variance_list)
        return result
    except ZeroDivisionError:

        print("Error: Cannot Divide by 0")

    except ValueError:

        print("Check your Data Input")
