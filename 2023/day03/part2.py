"""AoC 2023 day 03 part 2"""


def solve(data: str) -> int:
    return sum(gear[0] * gear[1] for gear in get_gears(get_numbers(data), data))


def get_numbers(schematic: str) -> [(str, int)]:
    numbers = []
    idx = 0
    while idx < len(schematic):
        if schematic[idx].isdigit():
            number = ""
            number_idx = idx
            while schematic[number_idx].isdigit():
                number += schematic[number_idx]
                number_idx += 1
            numbers.append((number, idx))
            idx = number_idx
            continue
        idx += 1
    return numbers


def get_gears(numbers: [(str, int)], schematic: str) -> [(int, int)]:
    line_len = schematic.index("\n") + 1
    asterisk_adjacent = {}
    for number in numbers:
        adjacent = [
            idx
            for idx in get_adjacent_idx(number, line_len)
            if 0 <= idx < len(schematic)
        ]
        for idx in adjacent:
            if schematic[idx] == "*":
                asterisk_adjacent.setdefault(idx, []).append(int(number[0]))
    gears = [
        (numbers[0], numbers[1])
        for numbers in asterisk_adjacent.values()
        if len(numbers) == 2
    ]
    return gears


def get_adjacent_idx(part: (str, int), line_len: int) -> [int]:
    idxs = []
    part_idx = part[1]
    part_len = len(part[0])
    idxs.append(part_idx - 1)
    idxs.append(part_idx + part_len)
    for itr in range(part_len + 2):
        idxs.append(part_idx - 1 + itr - line_len)
        idxs.append(part_idx - 1 + itr + line_len)
    return idxs


filecontent = ""
with open("./2023/day03/input.txt") as file:
    filecontent = file.read()

result = solve(filecontent)
print(result)

with open("./2023/day03/result2.txt", "w") as file:
    file.write(str(result))
