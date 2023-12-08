import fileinput
import os

inputFile = os.path.dirname(__file__) + os.path.sep + 'input'

info = {}
for l in fileinput.input(inputFile):
    line = l.strip()
    parts = line.split(':')
    num = int(parts[1].replace(' ', ''))
    info[parts[0]] = num

print (info)

# The function is symmetrical, so we only need to search the first half for a solution which will be increasing
# Find the first highest hold by searching an increasingly smaller space
# left of the range are lower values, right of the range are higher values
def findFirstHighest(start : int, end : int, best_dest : int, time : int):
    lenght = end - start + 1
    middle = start + lenght // 2 - 1 + lenght % 2
    dist = middle * (time - middle)
    print((start,middle,end,dist))
    if dist > best_dest:
        # the solution is to the left
        if lenght > 2:
            # middle value can still be the solution
            return findFirstHighest(start, middle, best_dest, time)
        else:
            return middle
    else:
        # the solution is to the right
        if lenght > 2:
            # middle value is not the solution
            return findFirstHighest(middle + 1, end, best_dest, time)
        else:
            return None if lenght == 1 else end

time = info['Time'] 
best_distance = info['Distance']
hold = findFirstHighest(0, time // 2 + 1, best_distance, time)
ways = time + 1 - 2 * hold

print('hold for ' + str(hold) + ' seconds at a minimum')
print(ways)
