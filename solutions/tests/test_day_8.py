import unittest

from solutions.day_8 import generate_image_layers, sol_8_a, sol_8_b, apply_mask, print_result


class MyTestCase(unittest.TestCase):
    def test_generate_image_layers(self):
        input = '123456789012'
        width = 3
        height = 2
        expected_layer_1 = '123456'
        expected_layer_2 = '789012'
        result = generate_image_layers(input, width, height)
        self.assertEqual(result, [expected_layer_1, expected_layer_2])

    def test_sol_8(self):
        with open('../../resources/input_8.txt', 'r') as f:
            data = f.read()
            result = sol_8_a(data, 25, 6)
            self.assertEqual(1862, result)

    def test_sol_8_b_mini(self):
        width = 2
        height = 2
        data = '0222112222120000'
        expected_outcome = '0110'
        result = sol_8_b(data, width, height)
        self.assertEqual(expected_outcome, result)

    def test_apply_mask(self):
        top = '1022'
        bottom = '0101'
        expected_result = '1001'
        result = apply_mask(top, bottom)
        self.assertEqual(expected_result, result)

    def test_sol_8_b(self):
        data = '10220101'
        width = 2
        height = 2
        expected_result = '1001'
        result = sol_8_b(data, width, height)
        self.assertEqual(expected_result, result)

    def test_sol_8_b_again(self):
        data = '0222112222120000'
        width = 2
        height = 2
        expected_result = '0110'
        result = sol_8_b(data, width, height)
        self.assertEqual(expected_result, result)

    def test_sol_8_b_proper(self):
        with open('../../resources/input_8.txt', 'r') as f:
            data = f.read()
            result = sol_8_b(data, 25, 6)
            # self.assertEqual(0, result)
            print_result(result, 25)

if __name__ == '__main__':
    unittest.main()
