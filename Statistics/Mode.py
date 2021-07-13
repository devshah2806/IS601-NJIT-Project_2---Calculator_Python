from collections import Counter


def mode(mode_list):
    try:
        n = len(mode_list)

        data = Counter(mode_list)
        get_mode = dict(data)
        mode_l = [k for k, v in get_mode.items() if v == max(list(data.values()))]
        return mode_l

    except IndexError or ValueError:
        return None
