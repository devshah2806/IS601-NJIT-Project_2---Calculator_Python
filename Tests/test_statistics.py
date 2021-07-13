import unittest

import statistics as pystats

from Statistics.Statistics import Statistics
from Statistics import Randomly as IntRandoms


class TestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.statistics = Statistics()
        self.int_randomData = IntRandoms.randoms(0, 30, 0, 30)

    def getUp(self) -> None:
        return self.int_randomData

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_decorator_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_mean(self):
        self.assertEqual(self.statistics.mean(self.int_randomData), pystats.mean(self.int_randomData))

    def test_median(self):
        self.assertEqual(self.statistics.median(self.int_randomData), pystats.median(self.int_randomData))

    def test_mode(self):
        self.assertEqual(self.statistics.mode(self.int_randomData), pystats.mode(self.int_randomData))

    def test_sd(self):
        self.assertEqual(self.statistics.sd(self.int_randomData), int(pystats.stdev(self.int_randomData)))

    