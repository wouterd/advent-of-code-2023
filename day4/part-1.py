import fileinput
import os

inputFile = os.path.dirname(__file__) + os.path.sep + 'input'

sum = 0
for line in fileinput.input(inputFile):
    colonPos = line.find(':')
    pipePos = line.find('|')
    wins = filter(lambda num: num != '', line[colonPos+1:pipePos].strip().split(' '))
    nums = filter(lambda num: num != '', line[pipePos+1:].strip().split(' '))
    winning_nums = len(set(wins).intersection(nums))
    points = 0 if winning_nums == 0 else pow(2, winning_nums - 1)
    sum = sum + points

print(sum)