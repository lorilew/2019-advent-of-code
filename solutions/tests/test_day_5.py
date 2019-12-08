import unittest

from solutions.day_5 import (
    read_instruction,
    handle_opcode_01,
    handle_opcode_02,
    handle_opcode_03,
    handle_opcode_04,
    handle_opcode_05,
    handle_opcode_06,
    handle_opcode_07,
    handle_opcode_08,
    intcode_computer,
)


class Day5TestCase(unittest.TestCase):
    def test_read_instruction_opcode_01(self):
        instructions = 1
        expected_opcode = "01"
        expected_modes = "000"
        opcode, modes = read_instruction(instructions)
        self.assertEqual(opcode, expected_opcode)
        self.assertEqual(modes, expected_modes)

    def test_read_instruction_opcode_02(self):
        instructions = 102
        expected_opcode = "02"
        expected_modes = "100"
        opcode, modes = read_instruction(instructions)
        self.assertEqual(opcode, expected_opcode)
        self.assertEqual(modes, expected_modes)

    def test_read_instruction_opcode_03(self):
        instructions = 103
        expected_opcode = "03"
        expected_modes = "1"
        opcode, modes = read_instruction(instructions)
        self.assertEqual(opcode, expected_opcode)
        self.assertEqual(modes, expected_modes)

    def test_read_instruction_opcode_04(self):
        instructions = 4
        expected_opcode = "04"
        expected_modes = "0"
        opcode, modes = read_instruction(instructions)
        self.assertEqual(opcode, expected_opcode)
        self.assertEqual(modes, expected_modes)

    def test_handle_opcode_01_position(self):
        data = [1, 0, 0, 0, 99]
        index = 0
        modes = "000"
        expected_data = [2, 0, 0, 0, 99]
        handle_opcode_01(data, index, modes)
        self.assertEqual(expected_data, data)

    def test_handle_opcode_01_immediate(self):
        data = [1, 0, 0, 0, 99]
        index = 0
        modes = "001"
        expected_data = [1, 0, 0, 2, 99]
        handle_opcode_01(data, index, modes)
        self.assertEqual(expected_data, data)

    def test_handle_opcode_02_position(self):
        data = [2, 0, 0, 0, 99]
        index = 0
        modes = "000"
        expected_data = [4, 0, 0, 0, 99]
        handle_opcode_02(data, index, modes)
        self.assertEqual(expected_data, data)

    def test_handle_opcode_02_immediate(self):
        data = [2, 0, 0, 0, 99]
        index = 0
        modes = "001"
        expected_data = [2, 0, 0, 4, 99]
        handle_opcode_02(data, index, modes)
        self.assertEqual(expected_data, data)

    def test_handle_opcode_03_position(self):
        data = [3, 3, 0, 0, 99]
        index = 0
        input = 6
        modes = "0"
        expected_data = [3, 3, 0, 6, 99]
        handle_opcode_03(data, index, input, modes)
        self.assertEqual(expected_data, data)

    def test_handle_opcode_03_immediate(self):
        data = [3, 3, 0, 0, 99]
        index = 0
        input = 6
        modes = "1"
        expected_data = [3, 6, 0, 0, 99]
        handle_opcode_03(data, index, input, modes)
        self.assertEqual(expected_data, data)

    def test_handle_opcode_04_position(self):
        data = [4, 3, 0, 6, 99]
        index = 0
        modes = "0"
        expected_data = [4, 3, 0, 6, 99]
        output = []
        handle_opcode_04(data, index, modes, output)
        self.assertEqual(expected_data, data)
        self.assertEqual([6], output)

    def test_handle_opcode_04_immediate(self):
        data = [3, 3, 0, 6, 99]
        index = 0
        modes = "1"
        output = []
        expected_data = [3, 3, 0, 6, 99]
        handle_opcode_04(data, index, modes, output)
        self.assertEqual(expected_data, data)
        self.assertEqual([3], output)

    def test_handle_opcode_05_false_position(self):
        data = [5, 1, 2]
        index = 0
        modes = "00"
        result = handle_opcode_05(data, index, modes)
        self.assertEqual(result, 2)

    def test_handle_opcode_05_true_position(self):
        data = [5, 3, 2, 0]
        index = 0
        modes = "00"
        result = handle_opcode_05(data, index, modes)
        self.assertEqual(result, 3)

    def test_handle_opcode_05_false_immediate(self):
        data = [5, 3, 3, 0]
        index = 0
        modes = "11"
        result = handle_opcode_05(data, index, modes)
        self.assertEqual(result, 3)

    def test_handle_opcode_05_true_immediate(self):
        data = [5, 0, 2, 0]
        index = 0
        modes = "11"
        result = handle_opcode_05(data, index, modes)
        self.assertEqual(result, 3)

    def test_handle_opcode_06_false_position(self):
        data = [5, 1, 2, 99]
        index = 0
        modes = "00"
        result = handle_opcode_06(data, index, modes)
        self.assertEqual(result, 3)

    def test_handle_opcode_06_true_position(self):
        data = [5, 3, 2, 0]
        index = 0
        modes = "00"
        result = handle_opcode_06(data, index, modes)
        self.assertEqual(result, 2)

    def test_handle_opcode_06_false_immediate(self):
        data = [6, 3, 3, 0]
        index = 0
        modes = "11"
        result = handle_opcode_06(data, index, modes)
        self.assertEqual(result, 3)

    def test_handle_opcode_06_true_immediate(self):
        data = [6, 0, 3, 0]
        index = 0
        modes = "11"
        result = handle_opcode_06(data, index, modes)
        self.assertEqual(result, 3)

    def test_handle_opcode_07_less_than_position(self):
        data = [7, 1, 2, 0]
        index = 0
        modes = "000"
        expected_data = [1, 1, 2, 0]
        handle_opcode_07(data, index, modes)
        self.assertEqual(expected_data, data)

    def test_handle_opcode_07_more_than_position(self):
        data = [7, 0, 2, 0]
        index = 0
        modes = "000"
        expected_data = [0, 0, 2, 0]
        handle_opcode_07(data, index, modes)
        self.assertEqual(expected_data, data)

    def test_handle_opcode_07_less_than_immediate(self):
        data = [7, 1, 2, 7]
        index = 0
        modes = "111"
        expected_data = [7, 1, 2, 1]
        handle_opcode_07(data, index, modes)
        self.assertEqual(expected_data, data)

    def test_handle_opcode_07_more_than_immediate(self):
        data = [7, 2, 1, 7]
        index = 0
        modes = "111"
        expected_data = [7, 2, 1, 0]
        handle_opcode_07(data, index, modes)
        self.assertEqual(expected_data, data)

    def test_handle_opcode_08_equal_position(self):
        data = [7, 1, 1, 0]
        index = 0
        modes = "000"
        expected_data = [1, 1, 1, 0]
        handle_opcode_08(data, index, modes)
        self.assertEqual(expected_data, data)

    def test_handle_opcode_08_not_equal_position(self):
        data = [7, 0, 2, 0]
        index = 0
        modes = "000"
        expected_data = [0, 0, 2, 0]
        handle_opcode_08(data, index, modes)
        self.assertEqual(expected_data, data)

    def test_handle_opcode_08_equal_immediate(self):
        data = [7, 1, 1, 7]
        index = 0
        modes = "111"
        expected_data = [7, 1, 1, 1]
        handle_opcode_08(data, index, modes)
        self.assertEqual(expected_data, data)

    def test_handle_opcode_08_not_equal_immediate(self):
        data = [7, 2, 1, 7]
        index = 0
        modes = "111"
        expected_data = [7, 2, 1, 0]
        handle_opcode_08(data, index, modes)
        self.assertEqual(expected_data, data)

    def test_intcode_computer_position_equal_8_or_not(self):
        data = "3,9,8,9,10,9,4,9,99,-1,8"
        # INPUT == 8
        input = 8
        output = intcode_computer(data, input)
        self.assertEqual(output, 1)
        # INPUT != 8
        input = 1
        output = intcode_computer(data, input)
        self.assertEqual(output, 0)

    def test_intcode_computer_position_less_than_8_or_not(self):
        data = "3,9,7,9,10,9,4,9,99,-1,8"
        # INPUT < 8
        input = 1
        output = intcode_computer(data, input)
        self.assertEqual(output, 1)
        # INPUT > 8
        input = 8
        output = intcode_computer(data, input)
        self.assertEqual(output, 0)

    def test_intcode_computer_immediate_equal_to_8_or_not(self):
        data = "3,3,1108,-1,8,3,4,3,99"
        # INPUT == 8
        input = 8
        output = intcode_computer(data, input)
        self.assertEqual(output, 1)
        # INPUT != 8
        input = 1
        output = intcode_computer(data, input)
        self.assertEqual(output, 0)

    def test_intcode_computer_immediate_less_than_8_or_not(self):
        data = "3,3,1107,-1,8,3,4,3,99"
        # INPUT < 8
        input = 1
        output = intcode_computer(data, input)
        self.assertEqual(output, 1)
        # INPUT > 8
        input = 9
        output = intcode_computer(data, input)
        self.assertEqual(output, 0)

    def test_intcode_computer_input_less_than_8(self):
        data = (
            "3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1"
            "106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,"
            "1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99"
        )
        input = 1
        expected_output = 999
        output = intcode_computer(data, input)
        self.assertEqual(expected_output, output)

    def test_intcode_computer_input_equal_to_8(self):
        data = (
            "3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1"
            "106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,"
            "1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99"
        )
        input = 8
        expected_output = 1000
        output = intcode_computer(data, input)
        self.assertEqual(expected_output, output)

    def test_intcode_computer_input_more_than_8(self):
        data = (
            "3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1"
            "106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,"
            "1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99"
        )
        input = 10
        expected_output = 1001
        output = intcode_computer(data, input)
        self.assertEqual(expected_output, output)

    def test_solution_5(self):
        with open("../../resources/input_5_b.txt", "r") as f:
            data = f.read()
            input = 5
            output = intcode_computer(data, input)
            self.assertEqual(output, 0)


if __name__ == "__main__":
    unittest.main()
