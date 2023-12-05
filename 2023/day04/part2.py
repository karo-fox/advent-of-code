"""AoC 2023 day 04 part 2"""

import re

ID_PATTERN = r"^Card\s+(?P<id>\d+): "
NUMBER_PATTERN = r"\d+"


def solve(data: str):
    scratchcards = {}
    for line in data.split("\n"):
        if line:
            id, matching = process_card(line)
            scratchcards = add_scratchcards(id, matching, scratchcards)
    return sum(val for val in scratchcards.values())


def process_card(card: str) -> int:
    id = re.match(ID_PATTERN, card).group("id")
    numbers = card.split(": ")[1].split(" | ")
    winning_numbers = re.findall(NUMBER_PATTERN, numbers[0])
    my_numbers = re.findall(NUMBER_PATTERN, numbers[1])
    my_winning_numbers = [number for number in my_numbers if number in winning_numbers]
    return int(id), len(my_winning_numbers)


def add_scratchcards(
    id: int, matching_numbers: int, scratchcards: dict[str, int]
) -> dict[int, int]:
    scratchcards[id] = scratchcards.setdefault(id, 0) + 1
    for itr in range(matching_numbers):
        scratchcards[id + itr + 1] = scratchcards.setdefault(id + itr + 1, 0) + scratchcards[id]
    return scratchcards


filecontent = ""
with open("./2023/day04/input.txt") as file:
    filecontent = file.read()

result = solve(filecontent)
print(result)

with open("./2023/day04/result2.txt", "w") as file:
    file.write(str(result))
