from math import floor


def mass_fuel_counter(filename):
    with open(filename) as inp:
        mass = [(floor(int(line.rstrip('\n')) / 3) - 2) for line in inp]
        mass_fuel = []
        for f_m in mass:
            "paliwo dla modułu to {}".format(f_m)
            f = []
            while f_m > 0:
                f.append(f_m)
                f_m = floor(int(f_m / 3)) - 2
                if f_m < 0: break
                "paliwo dla paliwa to {}".format(f_m)
            mass_fuel.append(sum(f))
        print(sum(mass_fuel))


mass_fuel_counter("fuel_input")
