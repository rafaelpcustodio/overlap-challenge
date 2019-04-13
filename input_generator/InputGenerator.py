class InputGenerator(object):

    def line_input_generator(self, position) -> list:
        fixed_line_range = 2
        list_to_return = []
        try:
            for index in range(fixed_line_range):
                value = int(input('{0}. Please provide your input from {1} coordinate: \n'.format(index + 1, position)))
                list_to_return.append(value)
            if list_to_return and len(list_to_return) == fixed_line_range:
                if self.validate_same_values(list_to_return):
                    raise ValueError()

            return list_to_return

        except ValueError:
            print("You must provide only different numbers in the same coordinate. It is not considered a line. "
                  "Moreover, chars, String and words are not valid inputs. Try again from the beginning.")
            exit(0)

    def validate_same_values(self, line) -> bool:
        if line[0] == line[1]:
            return True