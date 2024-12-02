def solve(data: str) -> str:
    records = sanitize(data)
    return str(sum(is_safe(record) for record in records))

def sanitize(data: str) -> list[list[int]]:
    records = []
    for line in data.split("\n"):
        if not line:
            break
        levels = []
        for number in line.split():
            levels.append(int(number))
        records.append(levels)
    return records

def is_safe(record: list[int]) -> bool:
    return is_ordered(record) and is_diif_1_to_3(record)

def is_ordered(record: list[int]) -> bool:
    return record == sorted(record) or record == sorted(record)[::-1]

def is_diif_1_to_3(record: list[int]) -> bool:
    return all(1 <= abs(lvl1 - lvl2) <= 3 for lvl1, lvl2 in zip(record[:-1], record[1:]))


filecontent = ""
with open("./2024/day02/input.txt") as file:
    filecontent = file.read()

result = solve(filecontent)
print(result)

with open("./2024/day02/result1.txt", "w") as file:
    file.write(str(result))
