from itertools import permutations

POSITION = "0"
IMMEDIATE = "1"

opcode_lengths = {
    "99": 0,
    "01": 3,
    "02": 3,
    "03": 1,
    "04": 1,
    "05": 2,
    "06": 2,
    "07": 3,
    "08": 3,
}


def handle_opcode_08(data, index, modes):
    """ Less than """
    if get_by_mode(data, index + 1, modes[0]) == get_by_mode(data, index + 2, modes[1]):
        input_by_mode(data, modes[2], index + 3, 1)
    else:
        input_by_mode(data, modes[2], index + 3, 0)


def handle_opcode_07(data, index, modes):
    """ Less than """
    if get_by_mode(data, index + 1, modes[0]) < get_by_mode(data, index + 2, modes[1]):
        input_by_mode(data, modes[2], index + 3, 1)
    else:
        input_by_mode(data, modes[2], index + 3, 0)


def handle_opcode_06(data, index, modes):
    """ jump if false (is 0) """
    if get_by_mode(data, index + 1, modes[0]) == 0:
        return get_by_mode(data, index + 2, modes[1])
    else:
        return increment_index(index, "06")


def handle_opcode_05(data, index, modes):
    """ jump if true (not 0) """
    if get_by_mode(data, index + 1, modes[0]) != 0:
        return get_by_mode(data, index + 2, modes[1])
    else:
        return increment_index(index, "05")


def handle_opcode_04(data, index, modes, output):
    """ output """
    output += [get_by_mode(data, index + 1, modes[0])]
    return output


def handle_opcode_03(data, index, input, modes):
    """ input """
    input_by_mode(data, modes[0], index + 1, input)


def handle_opcode_02(data, index, modes):
    """ Multiplication z = x * y """
    value_1 = get_by_mode(data, index + 1, modes[0])
    value_2 = get_by_mode(data, index + 2, modes[1])
    input_by_mode(data, modes[2], index + 3, value_1 * value_2)


def handle_opcode_01(data, index, modes):
    """ Addition z = x + y """
    value_1 = get_by_mode(data, index + 1, modes[0])
    value_2 = get_by_mode(data, index + 2, modes[1])
    input_by_mode(data, modes[2], index + 3, value_1 + value_2)


def read_instruction(instruction):
    str_instruction = str(instruction)
    opcode = str_instruction[-2:].zfill(2)
    if len(str_instruction) <= 2:
        return opcode, "".zfill(opcode_lengths[opcode])
    else:
        modes = str_instruction[0:-2].zfill(opcode_lengths[opcode])[::-1]
        return opcode, modes


def get_by_mode(data, index, mode):
    if mode == POSITION:
        return data[data[index]]
    elif mode == IMMEDIATE:
        return data[index]
    else:
        raise ValueError(f"Mode not found: {mode}")


def input_by_mode(data, mode, index, value):
    if mode == POSITION:
        data[data[index]] = value
    elif mode == IMMEDIATE:
        data[index] = value
    else:
        raise ValueError(f"Mode not found: {mode}")


def increment_index(index, opcode):
    return index + opcode_lengths[opcode] + 1


def intcode_computer(data_str, input=[]):
    data = [int(i) for i in data_str.split(",")]
    index = 0
    output = []
    while index < len(data) - 1:
        opcode, modes = read_instruction(data[index])

        if opcode == "99":
            break
        elif opcode == "01":
            handle_opcode_01(data, index, modes)
            index = increment_index(index, opcode)
        elif opcode == "02":
            handle_opcode_02(data, index, modes)
            index = increment_index(index, opcode)
        elif opcode == "03":
            value = input.pop(0)
            handle_opcode_03(data, index, value, modes)
            index = increment_index(index, opcode)
        elif opcode == "04":
            output = handle_opcode_04(data, index, modes, output)
            index = increment_index(index, opcode)
        elif opcode == "05":
            index = handle_opcode_05(data, index, modes)
        elif opcode == "06":
            index = handle_opcode_06(data, index, modes)
        elif opcode == "07":
            handle_opcode_07(data, index, modes)
            index = increment_index(index, opcode)
        elif opcode == "08":
            handle_opcode_08(data, index, modes)
            index = increment_index(index, opcode)
        else:
            raise ValueError(f"Opcode not found: {opcode}")
    return ",".join([str(i) for i in data]), output[-1]


def sol_7(data):
    perms = permutations([0, 1, 2, 3, 4], 5)
    possible_outcomes = []
    for perm in perms:
        phase_settings = list(perm)
        output = 0
        for i in range(5):
            input = [int(phase_settings[i]), output]
            data, thing = intcode_computer(data, input)
            output = thing
        possible_outcomes += [(phase_settings, output)]
    sorted_possible_outcomes = sorted(possible_outcomes, key=lambda x: x[1])
    return sorted_possible_outcomes[-1]
