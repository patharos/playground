

p_input = [256310,732736]


def find_possible_passwords():
    # breakpoint()
    num_l = []
    for i in range(256310, 732736):
        num = ''
        for n in range(len(str(i))-1):
            if str(i)[n] <= str(i)[n+1]:
                num += str(i)[n]
        if len(num) == len(str(i))-1:
            if check_repetition(i) and give_all_rep(i):
                num_l.append(int(i))
                print(i)
    return len(num_l)


def check_repetition(n):
    for i in range(len(str(n))-1):
        if str(n)[i] == str(n)[i + 1]:
            return True


def give_all_rep(number):
    num_dict = {}
    for i in range(2, 10):
        if str(number).count(str(i)) > 1:
            num_dict[i] = str(number).count(str(i))
    for i in num_dict.keys() : 
        if num_dict[i] == 2:
            return True
    return False



print(find_possible_passwords())
