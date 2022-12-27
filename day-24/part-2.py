with open("input.txt") as f:
    lines = f.read().split("\n")

valley = [line[1:-1] for line in lines[1:-1]]
height = len(valley)
width = len(valley[0])
neighbours = lambda r, c: [(r, c), (r - 1, c), (r, c + 1), (r + 1, c), (r, c - 1)]
move_checks = [
    lambda r, c, time: valley[r][(c - time) % width] != ">",
    lambda r, c, time: valley[r][(c + time) % width] != "<",
    lambda r, c, time: valley[(r - time) % height][c] != "v",
    lambda r, c, time: valley[(r + time) % height][c] != "^"
]

def bfs(current_positions, source, destionation, time):
    if len(current_positions) == 0:
        current_positions.add(source)

    next_positions = set()

    for current_position in current_positions:
        for neigbour in neighbours(current_position[0], current_position[1]):
            if neigbour == destionation:
                return time

            r, c = neigbour

            if 0 <= r < height and 0 <= c < width:
                can_move = True

                for move_check in move_checks:
                    if not move_check(r, c, time):
                        can_move = False
                        break

                if can_move:
                    next_positions.add((r, c))

    return bfs(next_positions, source, destionation, time + 1)

first_time = bfs(set(), (-1, 0), (height, width - 1), 0)
back_time = bfs(set(), (height, width - 1), (-1, 0), first_time)
second_time = bfs(set(), (-1, 0), (height, width - 1), back_time)
print(second_time)
