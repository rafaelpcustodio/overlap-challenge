from overlap.Overlap import Overlap
from input_generator.InputGenerator import InputGenerator

if __name__ == '__main__':

    FIXED_LINE_RANGE = 2
    listToReturn = []

    line1 = InputGenerator.line_input_generator(InputGenerator(), 'first')
    line2 = InputGenerator.line_input_generator(InputGenerator(), 'second')
    result = Overlap.check_overlap_x_axis(Overlap(), line1, line2)



