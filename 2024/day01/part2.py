
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
    
    result = 0
    for item in left:
        result += item * right.count(item)
    
    return str(result)


filecontent = ""
with open("./2024/day01/input.txt") as file:
    filecontent = file.read()

result = solve(filecontent)
print(result)

with open("./2024/day01/result2.txt", "w") as file:
    file.write(str(result))
