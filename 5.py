class ShipComputer:
    AMOUNT_OF_STEPS = {'01': 4,
                       '02': 4,
                       '03': 2,
                       '04': 2,
                       '07': 4,
                       '08': 4,
                       '99': 0}

    def __init__(self, input_filepath):
        with open(input_filepath) as fc:
            self.code_list = (fc.readline().rsplit(','))
        self.position = 0
        self.step = 0

    def __get_instruction_and_step(self):
        self.instruction = self.code_list[self.position]
        self.full_code = '{:0>{len}}'.format(str(self.instruction), len=5)
        if self.full_code[-2:] not in ['05', '06']:
            self.step = ShipComputer.AMOUNT_OF_STEPS[str(self.full_code[-2:])]

    def __perform_action(self):
        if self.full_code[-1] == '1':
            self.code_list[self.__get_proper_value(self.full_code, 3)] = int(self.code_list[self.__get_proper_value(self.full_code,  1)]) + \
                                                                                  int(self.code_list[self.__get_proper_value(self.full_code,  2)])
        elif self.full_code[-1] == '2':
            self.code_list[self.__get_proper_value(self.full_code, 3)] = int(self.code_list[self.__get_proper_value(self.full_code,  1)]) * \
                                                                                  int(self.code_list[self.__get_proper_value(self.full_code,  2)])
        elif self.full_code[-1] == '3':
            self.code_list[int(self.code_list[self.position+1])] = input("Give me the parameter!")
        elif self.full_code[-1] == '4':
            print("TEST CODE: {}".format(self.code_list[self.__get_proper_value(self.full_code,  1)]))
        elif self.full_code[-1] == '5':
            if int(self.code_list[self.__get_proper_value(self.full_code, 1)]) != 0:
                self.step = int(self.code_list[int(self.__get_proper_value(self.full_code, 2))]) - self.position
            else:
                self.step = 3
        elif self.full_code[-1] == '6':
            if int(self.code_list[self.__get_proper_value(self.full_code, 1)]) == 0:
                self.step = int(self.code_list[int(self.__get_proper_value(self.full_code, 2))]) - self.position
            else:
                self.step = 3
        elif self.full_code[-1] == '7':
            if self.code_list[self.__get_proper_value(self.full_code,  1)] < self.code_list[self.__get_proper_value(self.full_code, 2)]:
                self.code_list[self.__get_proper_value(self.full_code, 3)] = 1
            else:
                self.code_list[self.__get_proper_value(self.full_code, 3)] = 0
        elif self.full_code[-1] == '8':
            if self.code_list[self.__get_proper_value(self.full_code,  1)] == self.code_list[self.__get_proper_value(self.full_code, 2)]:
                self.code_list[self.__get_proper_value(self.full_code, 3)] = 1
            else:
                self.code_list[self.__get_proper_value(self.full_code, 3)] = 0
        else:
            return False
        self.position += self.step
        return self.code_list

    def __get_proper_value(self, code, param):
        if code[3-param] == '0':
            return int(self.code_list[self.position+param])
        elif code[3-int(param)] == '1':
            return self.position+param

    def run_computing(self):
        while self.position < len(self.code_list):
            self.__get_instruction_and_step()
            if not self.__perform_action():
                break
        print("Diagnostic code:{}".format(self.code_list[0]))


# dupa = ShipComputer("5_input")

dupa2 = ShipComputer("5_1_input.txt")
dupa2.run_computing()




