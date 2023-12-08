import fileinput
import os
from itertools import cycle
import math

inputFile = os.path.dirname(__file__) + os.path.sep + 'input'

state = 'nav'
nav = ''
points = {}
starts = []
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
            if point[2:3] == 'A': starts.append(point)
            continue

instructions = cycle(nav)

steps = []
for start in starts:
    loc = start
    count = 0
    while loc[2:3] != 'Z':
        loc = points[loc][next(instructions)]
        count += 1
    steps.append(count)

print(steps)
print(math.lcm(*steps))