def basic_fuel(mass):
    return int(mass / 3) - 2


def super_plus_fuel(mass):
    min_fuel = 6
    if mass <= min_fuel:
        return 0
    else:
        f = basic_fuel(mass)
        return f + super_plus_fuel(f)


def fuel_needed_for_modules(input_file_name, fuel_func):
    with open(input_file_name, "r") as f:
        data = f.read().split("\n")
    return sum([fuel_func(int(module)) for module in data])


print(fuel_needed_for_modules("../resources/input-1.txt", basic_fuel))
print(fuel_needed_for_modules("../resources/input-1.txt", super_plus_fuel))
