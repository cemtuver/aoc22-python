with open("input.txt") as f:
    lines = f.read().split("\n")

units = set()
bottom_y = 0
for line in lines:
    coordinates = line.split(" -> ")
    coordinates = list(map(lambda coordinate: list(map(int, coordinate.split(","))), coordinates))
    
    for i in range(len(coordinates) - 1):
        start_x, start_y = coordinates[i]
        end_x, end_y = coordinates[i + 1]

        if start_x == end_x:
            min_y = min(start_y, end_y)
            max_y = max(start_y, end_y) + 1

            for y in range(min_y, max_y):
                units.add((start_x, y))
                bottom_y = max(bottom_y, y)
        elif start_y == end_y:
            min_x = min(start_x, end_x)
            max_x = max(start_x, end_x) + 1
            bottom_y = max(bottom_y, start_y)

            for x in range(min_x, max_x):
                units.add((x, start_y))

iteration = 0
sand_source = (500, 0)
while True:
    x, y = sand_source
    unit_added = False

    while y < bottom_y:
        if (x, y + 1) not in units:
            x = x
            y = y + 1
            continue
        elif (x - 1, y + 1) not in units:
            x = x - 1
            y = y + 1
            continue
        elif (x + 1, y + 1) not in units:
            x = x + 1
            y = y + 1
            continue

        units.add((x, y))
        unit_added = True
        break

    if not unit_added:
        break
    
    iteration += 1

print(iteration)
