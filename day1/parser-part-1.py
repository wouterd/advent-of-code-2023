import fileinput
import os

inputFile = os.path.dirname(__file__) + os.path.sep + 'input'

sum = 0
for line in fileinput.input(inputFile):
    first = ''
    last = ''
    for char in line:
        if char.isdecimal():
            first = char
            break
    for char in reversed(line):
        if char.isdecimal():
            last = char
            break
    sum = sum + int(first + last)

print('sum:' + str(sum))