"""AoC 2023 day 01 part 2"""

import re

PATTERN = re.compile(r"one|two|three|four|five|six|seven|eight|nine|\d")


def solve(data: str) -> int:
    return sum(calibration_value(line) for line in data.split())


def calibration_value(line: str) -> int:
    digits = find_digits(line)
    digits = convert_digits(digits)
    return int(digits[0] + digits[-1])


def find_digits(line: str) -> list[str]:
    digits = []
    while digit_match := re.search(PATTERN, line):
        digit = digit_match[0]
        digits.append(digit)
        prefix = line[: line.find(digit)]
        prefix += digit if digit.isdigit() else digit[:-1]
        line = line.removeprefix(prefix)
    return digits


def convert_digits(digits: str) -> str:
    return "".join(
        digit if digit.isdigit() else word_to_digit(digit) for digit in digits
    )


def word_to_digit(word: str) -> str:
    words = ("one", "two", "three", "four", "five", "six", "seven", "eight", "nine")
    return str(words.index(word) + 1)


filecontent = ""
with open("./2023/day01/input.txt") as file:
    filecontent = file.read()

result = solve(filecontent)
print(result)
