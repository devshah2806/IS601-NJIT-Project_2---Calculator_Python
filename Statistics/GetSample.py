import random


def random_with_seed(r1, r2, r3):
    random.seed(r3)
    return random.randint(r1, r2)
