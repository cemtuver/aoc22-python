with open("input.txt") as f:
    lines = f.read().split("\n")

area = 0
droplets = set()
neighbours = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

for line in lines:
    x, y, z = list(map(int, line.split(",")))
    droplets.add((x, y, z))

for x, y, z in droplets:    
    for dx, dy, dz in neighbours:
        if (x + dx, y + dy, z + dz) not in droplets:
            area += 1

print(area)
