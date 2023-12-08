import fileinput
import os
from collections import defaultdict

inputFile = os.path.dirname(__file__) + os.path.sep + 'input-example'

def get_hand_type(hand : dict):
    if len(hand.keys()) == 1:
        return 'five-kind'
    four = next((x for x in hand.values() if x == 4), None)
    if four: return 'four-kind'
    if len(hand.keys()) == 2:
        return 'full-house'
    three = next((x for x in hand.values() if x == 3), None)
    if three: return 'three-kind'
    pairs = list(filter(lambda x: x == 2, hand.values()))
    if len(pairs) == 2: return 'two-pairs'
    if len(pairs) == 1: return 'one-pair'
    return 'high-card'

card_order = '23456789TJQKA'
def get_hand_score(hand : str):
    mul = 1
    score = 0
    for card in reversed(hand):
        score += (card_order.find(card) + 1) * mul
        mul *= 16
    return score

am_cards = 0
hands = defaultdict(list)
for l in fileinput.input(inputFile):
    line = l.strip()
    am_cards += 1
    parts = line.split(' ')
    hand = parts[0]
    bid = int(parts[1])
    hand_cards = defaultdict(int)
    for char in hand:
        hand_cards[char] += 1
    type = get_hand_type(hand_cards)
    score = get_hand_score(hand)
    hands[type].append((score, bid))

for l in hands.values():
    l.sort(key = lambda x: x[0], reverse=True)

order = ['five-kind', 'four-kind', 'full-house', 'three-kind', 'two-pairs', 'one-pair', 'high-card']

rank = am_cards
sum = 0
for key in order:
    for hand in hands[key]:
        winnings = rank * hand[1]
        sum += winnings
        rank -= 1

print(sum)