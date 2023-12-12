"""AoC 2023 day 07 part 1"""

import re
from functools import cmp_to_key

HAND_PATTERN = r"(?P<hand>^\w{5}) (?P<bid>\d+)$"
CARDS = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]


def solve(data: str):
    hands = parse_data(data)
    hands = sorted(hands, key=cmp_to_key(cmp_hands), reverse=True)
    return sum(hands[idx][1] * (idx + 1) for idx in range(len(hands)))


def parse_data(data: str) -> [(str, int)]:
    return [
        ((mo := re.match(HAND_PATTERN, line)).group("hand"), int(mo.group("bid")))
        for line in data.split("\n")
        if line
    ]


def cmp_hands(h1: (str, int), h2: (str, int)) -> int:
    h1val = hand_value(h1)
    h2val = hand_value(h2)
    if h1val == h2val:
        return stronger_card(h1, h2)
    return h2val - h1val


def hand_value(hand: str) -> int:
    hand = "".join(sorted(list(hand[0])))
    if re.search(r"(.)\1{4}", hand):
        return 6
    if re.search(r"(.)\1{3}", hand):
        return 5
    if re.search(r"(.)\1{2}(.)\2", hand) or re.search(r"(.)\1(.)\2{2}", hand):
        return 4
    if re.search(r"(.)\1{2}", hand):
        return 3
    if re.search(r"(.)\1.?(.)\2", hand):
        return 2
    if re.search(r"(.)\1", hand):
        return 1
    return 0


def stronger_card(h1: (str, int), h2: (str, int)) -> int:
    for card1, card2 in zip(h1[0], h2[0]):
        if CARDS.index(card2) > CARDS.index(card1):
            return 1
        if CARDS.index(card2) < CARDS.index(card1):
            return -1
    return 0


filecontent = ""
with open("./2023/day07/input.txt") as file:
    filecontent = file.read()

result = solve(filecontent)
print(result)

with open("./2023/day07/result1.txt", "w") as file:
    file.write(str(result))
