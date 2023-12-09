import fileinput
import os

inputFile = os.path.dirname(__file__) + os.path.sep + 'input'

sum = 0
for l in fileinput.input(inputFile):
    line = l.strip()
    values = list(map(lambda x: int(x), line.split()))
    deltas = []
    curr = values
    while True:
        curr_deltas = []
        for i in range(1,len(curr)):
            curr_deltas.append(curr[i] - curr[i-1])
        deltas.append(curr_deltas)
        non_zero = next((x for x in curr_deltas if x != 0), None)
        if not non_zero: break
        curr = curr_deltas

    decrease = 0
    for _ in range(0,len(deltas)):
        decrease = deltas.pop()[0] - decrease

    next_value = values[0] - decrease
    sum += next_value

print(sum)