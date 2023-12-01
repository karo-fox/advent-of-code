from aocd import submit


def calibration_value(line: str) -> int:
    digits = "".join(char for char in line if char.isdigit())
    return int(digits[0] + digits[-1])


def solve(data: str) -> int:
    return sum(calibration_value(line) for line in data.split())


filecontent = ""
with open("./2023/day01/input.txt") as file:
    filecontent = file.read()

result = solve(filecontent)
print(result)
submit(result, part='a', day=1, year=2023)
