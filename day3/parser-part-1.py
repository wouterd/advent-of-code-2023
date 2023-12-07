import fileinput
import os

inputFile = os.path.dirname(__file__) + os.path.sep + 'input'

sum = 0
last_symbols = []
last_numbers = []
for line in fileinput.input(inputFile):
    symbols = list(filter(lambda idx: not line[idx].isdecimal() and not line[idx] in ['.','\n'], range(len(line))))
    i = 0
    numbers = []
    while (i < len(line)):
        if line[i].isdecimal():
            j = i
            while (j < len(line)):
                if j + 1 < len(line) and line[j + 1].isdecimal():
                    j = j + 1
                else:
                    numbers.append((i,j,int(line[i:j+1]),False))
                    i = j + 1
                    break
        else:
            i = i + 1
    
    # Find numbers adjecent to symbols in the same line
    for idx in range(len(numbers)):
        if numbers[idx][0] - 1 in symbols or numbers[idx][1] + 1 in symbols:
            numbers[idx] = numbers[idx][0:3] + (True,)

    # Find numbers adjecent to symbols in the last line
    for idx in range(len(numbers)):
        if list(filter(lambda i: i in last_symbols, range(numbers[idx][0] - 1, numbers[idx][1] + 2))):
            numbers[idx] = numbers[idx][0:3] + (True,)

    # Find numbers in the last line adjacent to symbols in this line
    for idx in range(len(last_numbers)):
        if list(filter(lambda i: i in symbols, range(last_numbers[idx][0] - 1, last_numbers[idx][1] + 2))):
            last_numbers[idx] = last_numbers[idx][0:3] + (True,)
    
    for num in list(map(lambda x: x[2], filter(lambda x: x[3], last_numbers))):
        sum = sum + num

    last_numbers = numbers
    last_symbols = symbols

for num in list(map(lambda x: x[2], filter(lambda x: x[3], last_numbers))):
    sum = sum + num

print(sum)