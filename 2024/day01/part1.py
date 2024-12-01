
def sanitize(data: str) -> tuple[list[int], list[int]]:
    left = []
    right = []

    for line in data.split("\n")[:-1]:
        [litem, ritem] = line.split()
        left.append(int(litem))
        right.append(int(ritem))
    
    return left, right

def solve(data: str) -> str:
    left, right = sanitize(data)
    left = sorted(left)
    right = sorted(right)

    result = 0
    for litem, ritem in zip(left, right):
        result += abs(litem - ritem)
    
    return str(result)


filecontent = ""
with open("./2024/day01/input.txt") as file:
    filecontent = file.read()

result = solve(filecontent)
print(result)

with open("./2024/day01/result1.txt", "w") as file:
    file.write(str(result))
