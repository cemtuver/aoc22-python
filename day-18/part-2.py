with open("input.txt") as f:
    lines = f.read().split("\n")

area = 0
max_side = 0
droplets = set()
neighbours = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

for line in lines:
    x, y, z = list(map(int, line.split(",")))
    max_side = max(max_side, x, y, z)
    droplets.add((x, y, z))

visited = set()
to_visits = [(0, 0, 0)]

while len(to_visits) > 0:
    x, y, z = to_visits.pop()
  
    for dx, dy, dz in neighbours:
        nx, ny, nz = x + dx, y + dy, z + dz
        
        if (
            -1 <= nx <= max_side + 1 and 
            -1 <= ny <= max_side + 1 and
            -1 <= nz <= max_side + 1 and
            (nx, ny, nz) not in visited and 
            (nx, ny, nz) not in to_visits
        ):
            if (nx, ny, nz) in droplets:
                area += 1
            else:
                to_visits.append((nx, ny, nz))

    visited.add((x, y, z))

print(area)
