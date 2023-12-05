"""AoC 2023 day 05 part 1"""

import re
from functools import partial

LINE_PATTERN = r"^(?P<destination_start>\d+) (?P<source_start>\d+) (?P<range_len>\d+)$"
SEEDS_PATTERN = r"^seeds:(?P<seeds>( \d+)+)$"


def solve(data: str):
    segments = data.split("\n\n")
    seeds = get_seeds(segments[0])
    for segment in segments[1:]:
        seeds = map_seeds(seeds, segment)
    return min(seeds)


def get_seeds(data: str) -> list[int]:
    seeds = re.match(SEEDS_PATTERN, data).group("seeds")
    return [int(seed) for seed in seeds.split()]


def map_seeds(seeds: list[int], segment: str) -> list[int]:
    mapping = partial(source_to_destination, re.split(r":\n", segment)[1])
    return [mapping(seed) for seed in seeds]


def source_to_destination(map_data: str, seed: int) -> int:
    for line in map_data.split("\n"):
        line_match = re.match(LINE_PATTERN, line)
        dest_start = int(line_match.group("destination_start"))
        src_start = int(line_match.group("source_start"))
        range_len = int(line_match.group("range_len"))
        match seed:
            case x if src_start <= x < src_start + range_len:
                return x - src_start + dest_start
    return seed


filecontent = ""
with open("./2023/day05/input.txt") as file:
    filecontent = file.read()

result = solve(filecontent)
print(result)

with open("./2023/day05/result1.txt", "w") as file:
    file.write(str(result))
