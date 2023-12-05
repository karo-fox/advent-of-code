"""AoC 2023 day 05 part 2"""

import re
from functools import partial

LINE_PATTERN = r"^(?P<destination_start>\d+) (?P<source_start>\d+) (?P<range_len>\d+)$"
SEEDS_PATTERN = r"^seeds:(?P<seeds>( \d+ \d+)+)$"
SEED_RANGE_PATTERN = r" (\d+) (\d+)"


def solve(data: str):
    segments = data.split("\n\n")
    seeds = get_seeds(segments[0])
    for segment in segments[1:]:
        seeds = map_seeds(seeds, segment)
    return get_min(seeds)


def get_seeds(data: str) -> [int]:
    result = []
    seeds = re.match(SEEDS_PATTERN, data).group("seeds")
    for seed_pair in re.findall(SEED_RANGE_PATTERN, seeds):
        start = int(seed_pair[0])
        range_len = int(seed_pair[1])
        result.append((start, range_len))
    return result


def map_seeds(seeds: [(int, int)], segment: str) -> [(int, int)]:
    result = []
    mapping = partial(source_to_destination, re.split(r":\n", segment)[1])
    for start, length in seeds:
        seed_list = [mapping(seed) for seed in range(start, start + length)]
        result.extend(get_ranges(seed_list))
    return result


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


def get_ranges(seeds: [int]) -> [(int, int)]:
    result = []
    seeds = sorted(seeds)
    idx = 0
    while idx < len(seeds):
        start = seeds[idx]
        range_len = 0
        inner_idx = idx + 1
        while inner_idx < len(seeds) and seeds[inner_idx] - 1 == seeds[idx]:
            range_len += 1
            inner_idx += 1
            idx += 1
        range_len += 1
        result.append((start, range_len))
        idx += 1
    return result
        


def get_min(seeds: [(int, int)]) -> int:
    return min(seed[0] for seed in seeds)


filecontent = ""
with open("./2023/day05/input.txt") as file:
    filecontent = file.read()

result = solve(filecontent)
print(result)

with open("./2023/day05/result2.txt", "w") as file:
    file.write(str(result))
