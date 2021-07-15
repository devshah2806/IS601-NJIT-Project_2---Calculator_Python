import unittest

import statistics as pystats
from Statistics.Randomly import RandomGenerator
from Statistics.Statistics import Statistics


class TestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.statistics = Statistics()
        self.int_w_seed = RandomGenerator.gen1(0, 30, 0, 30, True)
        self.int_wo_seed = RandomGenerator.gen2(10, 30)
        self.dec_wo_seed = RandomGenerator.gen4(10, 30)
        self.dec_w_seed = RandomGenerator.gen3(10, 30, 2, 10, True)

    def getUp(self) -> None:
        return self.int_w_seed

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_decorator_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_mean(self):
        self.assertEqual(self.statistics.mean(self.int_w_seed), pystats.mean(self.int_w_seed))
        self.assertEqual(self.statistics.mean(self.dec_w_seed), int(pystats.mean(self.dec_w_seed)))

    def test_median(self):
        self.assertEqual(self.statistics.median(self.int_w_seed), pystats.median(self.int_w_seed))
        self.assertEqual(self.statistics.median(self.dec_w_seed), pystats.median(self.dec_w_seed))

    def test_mode(self):
        self.assertTrue(pystats.mode(self.int_w_seed.tolist()) in self.statistics.mode(self.int_w_seed.tolist()))

    def test_sd(self):
        self.assertEqual(self.statistics.sd(self.int_w_seed), int(pystats.stdev(self.int_w_seed)))
        self.assertEqual(self.statistics.sd(self.dec_w_seed), int(pystats.stdev(self.dec_w_seed)))

    def test_variance(self):
        self.assertEqual(self.statistics.variance(self.int_w_seed), pystats.variance(self.int_w_seed))
        self.assertEqual(self.statistics.variance(self.int_w_seed), pystats.variance(self.int_w_seed))
