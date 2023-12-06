"""AoC 2023 day 06 part 2"""
from typing import Iterable
import re

LINE_PATTERN = r"^\w+:(?P<numbers>(\s+\d+)+)$"


def solve(data: str):
    data = data.split("\n")
    times = [
        elem
        for elem in re.split(r"\s+", re.match(LINE_PATTERN, data[0]).group("numbers"))
        if elem
    ]
    dists = [
        elem
        for elem in re.split(r"\s+", re.match(LINE_PATTERN, data[1]).group("numbers"))
        if elem
    ]
    return analyze_race((int("".join(times)), int("".join(dists))))


def analyze_race(race: (int, int)) -> int:
    results = [get_distance(race[0], push) for push in range(race[0] // 2 + 1)]
    counter = len([elem for elem in results if elem > race[1]])
    counter *= 2
    if race[0] % 2 == 0:
        counter -= 1
    return counter


def get_distance(total_time: int, push_time: int) -> int:
    return (total_time - push_time) * push_time


filecontent = ""
with open("./2023/day06/input.txt") as file:
    filecontent = file.read()

result = solve(filecontent)
print(result)

with open("./2023/day06/result2.txt", "w") as file:
    file.write(str(result))
