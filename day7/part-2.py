import fileinput
import os
from collections import defaultdict

inputFile = os.path.dirname(__file__) + os.path.sep + 'input'

def get_hand_type(h : str):
    hand = defaultdict(int)
    for char in h:
        hand[char] += 1
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

hand_type_order = ['five-kind', 'four-kind', 'full-house', 'three-kind', 'two-pairs', 'one-pair', 'high-card']

def get_hand_type_score(type: str):
    return hand_type_order.index(type)

card_order = 'AKQT98765432J'[::-1]

def get_hand_score(hand : str):
    mul = 1
    score = 0
    for card in hand[::-1]:
        loc = card_order.find(card)
        if loc == -1: 
            raise Exception("Unknown card! card = " + card)
        score += loc * mul
        mul *= 16
    return score

am_cards = 0
hands = defaultdict(list)
for l in fileinput.input(inputFile):
    line = l.strip().upper()
    am_cards += 1
    parts = line.split(' ')
    hand = parts[0]
    bid = int(parts[1])

    # Try every card for the joker(s)
    wild_type = min(get_hand_type_score(get_hand_type(hand.replace('J', c))) for c in '23456789TQKA')
    type = hand_type_order[wild_type]

    score = get_hand_score(hand)
    hands[type].append((score, bid))

for l in hands.values():
    l.sort(key = lambda x: x[0], reverse=True)

rank = am_cards
sum = 0
for key in hand_type_order:
    for hand in hands[key]:
        winnings = rank * hand[1]
        sum += winnings
        rank -= 1

print(sum)