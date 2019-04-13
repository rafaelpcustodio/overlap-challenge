
class Overlap(object):

    FIXED_LINE_RANGE = 1
    POSITION_ZERO = 0

    def check_overlap_x_axis(self, first_line = [], second_line = []) -> bool:

        if not first_line or not second_line or len(first_line) > self.FIXED_LINE_RANGE + 1 or len(second_line) > self.FIXED_LINE_RANGE + 1:
            print('You probably passed at least one wrong input. You must pass 2 points with 2 values each. Try again. ')
            return False
            # both are ascending points

        if not self.validate_ascending_order(first_line):
            first_line = self.fix_inputs(first_line)

        if not self.validate_ascending_order(second_line):
            second_line = self.fix_inputs(second_line)

        if self.both_ascending_order(first_line, second_line):
            if not (first_line[self.FIXED_LINE_RANGE] < second_line[self.POSITION_ZERO]
                    or second_line[self.FIXED_LINE_RANGE] < first_line[self.POSITION_ZERO]):
                print('Lines overlap at x-axis')
                return True
        print('Lines does not overlap at x-axis')
        return False

    def both_ascending_order(self, line1=[], line2=[]) -> bool:
        return self.validate_ascending_order(line1) and self.validate_ascending_order(line2)

    # true if ascending values, false if descending
    def validate_ascending_order(self, line = []) -> bool:
        if line[0] < line[1]:
            return True
        return False

    # fixing descending input
    def fix_inputs(self, line = []) -> list:
        if line[0] > line[1]:
            value_to_pass = line[0]
            line[0] = line[1]
            line[1] = value_to_pass
        return line

    def execute_overlap(self, line1, line2) -> bool:
        return self.check_overlap_x_axis(line1, line2)