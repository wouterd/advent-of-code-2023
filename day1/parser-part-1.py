import fileinput
import os
from timeit import timeit

inputFile = os.path.dirname(__file__) + os.path.sep + 'input-example-1'

def get_sum():
    sum = 0
    for line in fileinput.input(inputFile):
        first = next(char for char in line if char.isdecimal())
        last = next(char for char in reversed(line) if char.isdecimal())
        sum += int(first + last)

    print('sum:' + str(sum))

print(timeit(get_sum, number=1))