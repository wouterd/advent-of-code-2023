import fileinput
import os

inputFile = os.path.dirname(__file__) + os.path.sep + 'input'

def check_digit(line: str, idx: int):
    if line[idx].isdecimal():
        return line[idx]
    
    matchStr = line[idx:idx+5]
    if matchStr.startswith('one'):
        return '1'
    if matchStr.startswith('two'):
        return '2'
    if matchStr.startswith('three'):
        return '3'
    if matchStr.startswith('four'):
        return '4'
    if matchStr.startswith('five'):
        return '5'
    if matchStr.startswith('six'):
        return '6'
    if matchStr.startswith('seven'):
        return '7'
    if matchStr.startswith('eight'):
        return '8'
    if matchStr.startswith('nine'):
        return '9'
    
    return ''

sum = 0
for line in fileinput.input(inputFile):
    first = ''
    last = ''
    for idx in range(len(line)):
        result = check_digit(line, idx)
        if result != '':
            first = result
            break
    for idx in range(len(line)-1,-1,-1):
        result = check_digit(line, idx)
        if result != '':
            last = result
            break
    sum = sum + int(first + last)

print(sum)