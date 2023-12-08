import fileinput
import os

inputFile = os.path.dirname(__file__) + os.path.sep + 'input'

info = {}
for l in fileinput.input(inputFile):
    line = l.strip()
    parts = line.split(':')
    info[parts[0]] = list(map(lambda y: int(y), filter(lambda x: x.isdecimal(), parts[1].strip().split(' '))))

races = list(zip(info['Time'], info['Distance']))

total = 1
for time, best_distance in races:
    hold = 1
    # need to also try the middle option for odd total amounts
    while hold < time / 2 + time % 2:
        dist = hold * (time - hold)
        if dist > best_distance:
            ways = time + 1 - 2 * hold
            print(ways)
            total *= ways
            break
        hold += 1

print(total)