import fileinput
import os
from itertools import cycle

inputFile = os.path.dirname(__file__) + os.path.sep + 'input'

state = 'nav'
nav = ''
points = {}
for l in fileinput.input(inputFile):
    line = l.strip()
    if line == '':
        state = 'points'
        continue
    match state:
        case 'nav': 
            nav = line
            continue
        case 'points':
            point = line[:3]
            l = line[7:10]
            r = line[12:15]
            points[point] = {'L': l, 'R': r}
            continue

instructions = cycle(nav)

loc = 'AAA'
steps = 0
while loc != 'ZZZ':
    instruction = next(instructions)
    loc = points[loc][instruction]
    print(loc)
    steps += 1

print(steps)