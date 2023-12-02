"""AoC 2023 day 02 part 2"""

import re


def solve(data: str) -> int:
    return sum(process_game(line) for line in data.split("\n") if line)


def process_game(game: str):
    cubes = {"red": 0, "green": 0, "blue": 0}
    for cube_data in re.split(r", |; ", game.split(": ")[1]):
        number = int(cube_data.split()[0])
        color = cube_data.split()[1]
        if number > cubes[color]:
            cubes[color] = number
    return game_power(cubes)


def game_power(game: dict[str, int]) -> int:
    return game["red"] * game["green"] * game["blue"]


filecontent = ""
with open("./2023/day02/input.txt") as file:
    filecontent = file.read()

result = solve(filecontent)
print(result)

with open("./2023/day02/result2.txt", "w") as file:
    file.write(str(result))
