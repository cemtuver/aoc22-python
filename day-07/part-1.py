with open("input.txt") as f:
    lines = f.read().split("\n")

tree = ["/"]
sizes = { "/": 0 }
for line in lines:
    if line.startswith("$ cd "):
        dir = line[5:]
        if dir == "..":
            tree.pop()
        else:
            full_path = f"{tree[-1]}/{dir}"
            tree.append(full_path)
            sizes[full_path] = 0
    elif line[0].isdigit():
        size = int(line.split(" ")[0])
        for dir in tree:
            sizes[dir] +=  size

total = sum(size for size in sizes.values() if size <= 100000)
print(total)
