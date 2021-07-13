import statistics


def variance(variance_list):
    try:
        result = statistics.variance(variance_list)
        return result

    except IndexError or ValueError:
        return None
