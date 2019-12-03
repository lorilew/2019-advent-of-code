import unittest

from solutions.day_3 import get_min_intersection


class Day3testCase(unittest.TestCase):
    def test_sol_3(self):
        input_1 = 'R75,D30,R83,U83,L12,D49,R71,U7,L72'
        input_2 = 'U62,R66,U55,R34,D71,R55,D58,R83'
        expected_output = 159
        output = get_min_intersection(input_1, input_2)
        self.assertEqual(output, expected_output)

    def test_sol_3_again(self):
        input_1 = 'R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51'
        input_2 = 'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'
        expected_output = 135
        output = get_min_intersection(input_1, input_2)
        self.assertEqual(output, expected_output)