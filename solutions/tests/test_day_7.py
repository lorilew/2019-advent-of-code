import unittest

from solutions.day_7 import intcode_computer, sol_7


class MyTestCase(unittest.TestCase):
    def test_intcode_computer_multiple_input(self):
        input = [0, 1]
        data_str = "103,5,3,0,99"
        data, output = intcode_computer(data_str, input)
        self.assertEqual(output, [])
        self.assertEqual(data, "1,0,3,0,99")

    def test_sol_7_43210(self):
        data = "3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0"
        output = sol_7(data)
        self.assertEqual(([4, 3, 2, 1, 0], 43210), output)

    def test_sol_7_01234(self):
        data = (
            "3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0"
        )
        output = sol_7(data)
        self.assertEqual(([0, 1, 2, 3, 4], 54321), output)

    def test_sol_7_10432(self):
        data = "3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0"
        output = sol_7(data)
        self.assertEqual(([1, 0, 4, 3, 2], 65210), output)

    def test_sol_7_for_realz(self):
        with open('../../resources/input_7.txt', 'r') as f:
            data = f.read()
            output = sol_7(data)
            self.assertEqual(([], 0), output)


if __name__ == "__main__":
    unittest.main()
