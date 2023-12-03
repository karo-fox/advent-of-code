"""AoC 2023 day 03 part 1"""


def solve(data: str) -> int:
    return sum(
        int(number[0]) for number in get_numbers(data) if is_engine_part(number, data)
    )


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


def is_engine_part(part: (str, int), schematic: str) -> bool:
    line_len = schematic.index("\n") + 1
    adjacent = [
        idx for idx in get_adjacent_idx(part, line_len) if 0 <= idx < len(schematic)
    ]
    result = any(is_symbol(schematic[idx]) for idx in adjacent)
    return result


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


def is_symbol(char: str):
    return not char.isdigit() and not char == "." and not char == "\n"


filecontent = ""
with open("./2023/day03/input.txt") as file:
    filecontent = file.read()

result = solve(filecontent)
print(result)

with open("./2023/day03/result1.txt", "w") as file:
    file.write(str(result))
