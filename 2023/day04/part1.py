"""AoC 2023 day 04 part 1"""

import re

NUMBER_PATTERN = r"\d+"


def solve(data: str):
    return sum(process_card(line) for line in data.split("\n") if line)


def process_card(card: str) -> int:
    numbers = card.split(": ")[1].split(" | ")
    winning_numbers = re.findall(NUMBER_PATTERN, numbers[0])
    my_numbers = re.findall(NUMBER_PATTERN, numbers[1])
    my_winning_numbers = [number for number in my_numbers if number in winning_numbers]
    if my_winning_numbers:
        return 2 ** (len(my_winning_numbers) - 1)
    return 0


filecontent = ""
with open("./2023/day04/input.txt") as file:
    filecontent = file.read()

result = solve(filecontent)
print(result)

with open("./2023/day04/result1.txt", "w") as file:
    file.write(str(result))
