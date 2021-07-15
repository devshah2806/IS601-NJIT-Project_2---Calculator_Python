import numpy as np
import random


class RandomGenerator:
    @staticmethod
    def gen1(r1, r2, r3, r4, r5):
        random.seed(r3)
        np.random.seed(r3)
        if r5:
            return np.random.randint(r1, r2, size=r4)
        else:
            return [random.randint(r1, r2) for r in range(r4)]

    @staticmethod
    def gen2(r1, r2):
        random_list = []
        for i in range(r1, r2):
            random_list = random.randint(r1, r2)
        return random_list

    @staticmethod
    def gen3(r1, r2, r3, r4, r5):
        random.seed(r3)
        if r5:
            return [random.uniform(r1, r2) for i in range(r4)]
        else:
            return [round(random.uniform(r1, r2), 1) for i in range(r4)]

    @staticmethod
    def gen4(r1, r2):
        random_list1 = []
        for i in range(r1, r2):
            random_list1 = random.randint(r1, r2)
        return random_list1
