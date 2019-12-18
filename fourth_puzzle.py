import itertools


def read_instructions(a, b):
    with open("code") as fc:
        code_list = (fc.readline().rsplit(','))
        code_list[1] = a
        code_list[2] = b
        for i in range(0, 145, 4):
            if int(code_list[i]) == 1:
                code_list[int(code_list[i+3])] = int(code_list[int(code_list[i+1])]) + int(code_list[int(code_list[i+2])])
            elif int(code_list[i]) == 2:
                code_list[int(code_list[i+3])] = int(code_list[int(code_list[i+1])]) * int(code_list[int(code_list[i+2])])
            elif int(code_list[i]) == 99:
                return code_list[0]
        return code_list[0]


def find_instructions():
    with open("code") as fc:
        for a, b in itertools.product(range(100), range(100)):
            if read_instructions(a, b) == 19690720:
                print(a)
                print(b)
                return 100*a+b
            else:
                continue


print(find_instructions())


