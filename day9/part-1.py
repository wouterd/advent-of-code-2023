import fileinput
import os

inputFile = os.path.dirname(__file__) + os.path.sep + 'input'

sum = 0
for ln in fileinput.input(inputFile):
    line = ln.strip()
    values = list(map(lambda x: int(x), line.split()))
    deltas = []
    curr = values
    while True:
        curr_deltas = []
        for i in range(1, len(curr)):
            curr_deltas.append(curr[i] - curr[i-1])
        deltas.append(curr_deltas)
        non_zero = next((x for x in curr_deltas if x != 0), None)
        if not non_zero:
            break
        curr = curr_deltas

    increment = 0
    for _ in range(0, len(deltas)):
        increment += deltas.pop().pop()

    next_value = values.pop() + increment
    sum += next_value

print(sum)
