import unittest
import generators


class TestGenerator(unittest.TestCase):
    def _test_generator(self, params, expected_values):
        gen = generators.my_range(*params)

        for value in expected_values:
            self.assertEqual(next(gen), value)

        with self.assertRaises(StopIteration):
            next(gen)

    def test_generator(self):
        self._test_generator((3,), (0, 1, 2))

    def test_generator_start_stop(self):
        self._test_generator((3, 6), (3, 4, 5))

    def test_generator_start_stop_step(self):
        self._test_generator((0, 6, 2), (0, 2, 4))


if __name__ == '__main__':
    unittest.main()
