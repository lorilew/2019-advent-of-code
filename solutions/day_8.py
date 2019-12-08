BLACK = '0'
WHITE = '1'
TRANSPARENT = '2'


def generate_image_layers(input, width, height, include_zero_count=False):
    total_pix = width * height
    if len(input) % total_pix != 0:
        raise Exception('Incompplete image')

    layers = []
    index = 0
    while index < len(input):
        l = input[index:index+total_pix]
        if include_zero_count:
            zeros = l.count('0')
            layers += [(''.join(l), zeros)]
        else:
            layers += [''.join(l)]
        index += total_pix

    return layers


def sol_8_a(data, width, height):
    layers = generate_image_layers(data, width, height, True)
    sorted_by_zeros = sorted(layers, key=lambda tup: tup[1])
    the_fancy_layer = sorted_by_zeros[0][0]
    return the_fancy_layer.count('1') * the_fancy_layer.count('2')


def apply_mask(top, bottom):
    result = ''
    for i, p in enumerate(top):
        if p == BLACK or p == WHITE:
            result += p
        else:
            result += bottom[i]
    return result


def sol_8_b(data, width, height):
    layers = generate_image_layers(data, width, height)
    bottom = layers[-1]
    for i in reversed(range(1, len(layers))):
        bottom = apply_mask(layers[i - 1], bottom)
    return bottom

def print_result(image_data, width):
    index = 0
    image_data = image_data.replace('0', ' ')

    while index < len(image_data):
        print(image_data[index:index+width])
        index += width
