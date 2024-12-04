"""AoC 2024 day 04 part 1"""

import re

PATTERN = r"XMAS"


def solve(data: str) -> str:
    data = santatize(data)
    result = 0
    result += len(re.findall(PATTERN, rows(data.copy())))
    result += len(re.findall(PATTERN, rows(data.copy())[::-1]))
    result += len(re.findall(PATTERN, cols(data.copy())))
    result += len(re.findall(PATTERN, cols(data.copy())[::-1]))
    result += len(re.findall(PATTERN, diags_right(data.copy())))
    result += len(re.findall(PATTERN, diags_right(data.copy())[::-1]))
    result += len(re.findall(PATTERN, diags_left(data.copy())))
    result += len(re.findall(PATTERN, diags_left(data.copy())[::-1]))
    return str(result)


def santatize(data: str) -> list[str]:
    return data.strip().split("\n")


def rows(data: list[str]) -> str:
    return "\n".join(data)


def cols(data: list[str]) -> str:
    return "".join(
        "".join(line[idx] for line in data) + "\n" for idx in range(len(data[0]))
    )


def diags_right(data: list[str]) -> str:
    rows_num = len(data)
    for idx in range(len(data)):
        data[idx] = (rows_num - idx) * " " + data[idx] + idx * " "
    return cols(data)


def diags_left(data: list[str]) -> str:
    rows_num = len(data)
    for idx in range(len(data)):
        data[idx] = idx * " " + data[idx] + (rows_num - idx) * " "
    return cols(data)


filecontent = ""
with open("./2024/day04/input.txt") as file:
    filecontent = file.read()

result = solve(filecontent)
print(result)

with open("./2024/day04/result1.txt", "w") as file:
    file.write(str(result))
