"""AoC 2023 day 02 part 1"""

import re

ID_PATTERN = r"^Game (?P<id>\d+): "
MAX_CUBES = {"red": 12, "green": 13, "blue": 14}


def solve(data: str) -> int:
    return sum(check_game(line) for line in data.split("\n") if line)


def check_game(line: str):
    id = int(re.match(ID_PATTERN, line).group("id"))
    sets = line.split(": ")[1]
    if all(
        int(cube_data.split()[0]) <= MAX_CUBES[cube_data.split()[1]]
        for cube_data in re.split(r", |; ", sets)
    ):
        return id
    return 0


filecontent = ""
with open("./2023/day02/input.txt") as file:
    filecontent = file.read()

result = solve(filecontent)
print(result)

with open("./2023/day02/result1.txt", "w") as file:
    file.write(str(result))
