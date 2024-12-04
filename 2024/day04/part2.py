"""AoC 2024 day 04 part 2"""


def solve(data: str) -> str:
    data = santatize(data)
    row_len = len(data[0])
    col_len = len(data)
    result = 0
    while (coords := find_A(data)) != (-1, -1):
        row_idx, col_idx = coords
        data[row_idx] = data[row_idx][:col_idx] + "." + data[row_idx][col_idx + 1 :]
        if row_idx in (0, row_len - 1) or col_idx in (0, col_len - 1):
            continue
        if (
            (
                data[row_idx - 1][col_idx - 1] == "M"
                and data[row_idx + 1][col_idx + 1] == "S"
                and data[row_idx - 1][col_idx + 1] == "M"
                and data[row_idx + 1][col_idx - 1] == "S"
            )
            or (
                data[row_idx - 1][col_idx - 1] == "M"
                and data[row_idx + 1][col_idx + 1] == "S"
                and data[row_idx - 1][col_idx + 1] == "S"
                and data[row_idx + 1][col_idx - 1] == "M"
            )
            or (
                data[row_idx - 1][col_idx - 1] == "S"
                and data[row_idx + 1][col_idx + 1] == "M"
                and data[row_idx - 1][col_idx + 1] == "M"
                and data[row_idx + 1][col_idx - 1] == "S"
            )
            or (
                data[row_idx - 1][col_idx - 1] == "S"
                and data[row_idx + 1][col_idx + 1] == "M"
                and data[row_idx - 1][col_idx + 1] == "S"
                and data[row_idx + 1][col_idx - 1] == "M"
            )
        ):
            result += 1
    return str(result)


def santatize(data: str) -> list[str]:
    return data.strip().split("\n")


def find_A(data: list[str]) -> tuple[int, int]:
    for row_idx, row in enumerate(data):
        if (col_idx := row.find("A")) != -1:
            return (row_idx, col_idx)
    return (-1, -1)


filecontent = ""
with open("./2024/day04/input.txt") as file:
    filecontent = file.read()

result = solve(filecontent)
print(result)

with open("./2024/day04/result2.txt", "w") as file:
    file.write(str(result))
