def read_instructions():
    with open("code") as fc:
        code_list = (fc.readline().rsplit(','))
        for i in range(0, 145, 4):
            if int(code_list[i]) == 1:
                code_list[int(code_list[i+3])] = int(code_list[int(code_list[i+1])]) + int(code_list[int(code_list[i+2])])
            elif int(code_list[i]) == 2:
                code_list[int(code_list[i+3])] = int(code_list[int(code_list[i+1])]) * int(code_list[int(code_list[i+2])])
            elif int(code_list[i]) == 99:
                return code_list[0]
        return code_list[0]


print("Wartość elementu 0 to : {}".format(read_instructions()))
