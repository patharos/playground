from math import floor


def fuel_counter(filename):
    with open(filename) as input:
        mass = sum([(floor(int(line.rstrip('\n'))/3)-2) for line in input])
        print(mass)



fuel_counter("fuel_input")