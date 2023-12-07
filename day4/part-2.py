import fileinput
import os
from collections import defaultdict

inputFile = os.path.dirname(__file__) + os.path.sep + 'input'

extra_cards = defaultdict(int)
card_num = 0
am_cards = 0
for line in fileinput.input(inputFile):
    colonPos = line.find(':')
    pipePos = line.find('|')
    wins = filter(lambda num: num != '', line[colonPos+1:pipePos].strip().split(' '))
    nums = filter(lambda num: num != '', line[pipePos+1:].strip().split(' '))
    winning_nums = len(set(wins).intersection(nums))
    if winning_nums > 0:
        for card in range(card_num + 1, card_num + 1 + winning_nums):
            this_cards = 1 + extra_cards[card_num]
            extra_cards[card] += this_cards
    am_cards += 1 + extra_cards[card_num]
    card_num += 1

print(am_cards)