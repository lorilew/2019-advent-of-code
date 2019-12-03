
def generate_path(wire):
    input = wire.split(',')
    path = [(0, 0)]
    for instruction in input:
        direction = instruction[0]
        length = int(instruction[1:])
        current_x, current_y = path[-1]
        if direction == 'R':
            [path.append((current_x + i, current_y)) for i in range(1, length + 1)]
        elif direction == 'L':
            [path.append((current_x - i, current_y)) for i in range(1, length + 1)]
        elif direction == 'U':
            [path.append((current_x, current_y + i)) for i in range(1, length + 1)]
        elif direction == 'D':
            [path.append((current_x, current_y - i)) for i in range(1, length + 1)]
        else:
            raise Exception(f'Unknown input: {direction}')
    return path


def get_min_intersection(input_1, input_2):
        path_1 = generate_path(input_1)[1:]
        path_2 = generate_path(input_2)[1:]
        common = set(path_1).intersection(set(path_2))
        distances = [abs(x) + abs(y) for x, y in common]
        return min(distances)


def sol_3():
    with open('../resources/input_3.txt') as f:
        input_1 = f.readline()
        input_2 = f.readline()
        return get_min_intersection(input_1, input_2)


print(sol_3())
