import re

with open("input.txt") as f:
    lines = f.read().split("\n")

board = lines[:-2]
board_size = max(map(len, board))
board = list(map(lambda line: str.ljust(line, board_size), board))
instructions = re.findall("\d+|[LR]", lines[-1])

position = (0, board[0].index('.'))
direction = (0, 1)
turns = {
    (0, 1): { "R": (1, 0), "L": (-1, 0) },
    (1, 0): { "R": (0, -1), "L": (0, 1) },
    (0, -1): { "R": (-1, 0), "L": (1, 0) },
    (-1, 0): { "R": (0, 1), "L": (0, -1) }
}
direction_grade = {
    (0, 1): 0,
    (1, 0): 1,
    (0, -1): 2,
    (-1, 0): 3
}

def find_next_position(position, direction):
    next_direction = direction
    next_position = (position[0] + direction[0], position[1] + direction[1])

    if 0 <= position[0] < 50 and 50 <= position[1] < 100:
        # 1
        if direction == (0, -1) and next_position[1] < 50:
            # -> 4
            next_direction = (0, 1)
            next_position = (149 - position[0], 0)
        elif direction == (-1, 0) and next_position[0] < 0:
            # -> 6
            next_direction = (0, 1)
            next_position = (100 + position[1], 0)
    elif 0 <= position[0] < 50 and 100 <= position[1] < 150:
        # 2
        if direction == (0, 1) and next_position[1] >= 150:
            # -> 5
            next_direction = (0, -1)
            next_position = (149 - position[0], 99)
        elif direction == (1, 0) and next_position[0] >= 50:
            # -> 3
            next_direction = (0, -1)
            next_position = (position[1] - 50, 99)
        elif direction == (-1, 0) and next_position[0] < 0:
            # -> 6
            next_direction = (-1, 0)
            next_position = (199, position[1] - 100)
    elif 50 <= position[0] < 100 and 50 <= position[1] < 100:
        # 3
        if direction == (0, 1) and next_position[1] >= 100:
            # -> 2
            next_direction = (-1, 0)
            next_position = (49, position[0] + 50)
        elif direction == (0, -1) and next_position[1] < 50:
            # -> 4
            next_direction = (1, 0)
            next_position = (100, position[0] - 50)
    elif 100 <= position[0] < 150 and 0 <= position[1] < 50:
        # 4
        if direction == (0, -1) and next_position[1] < 0:
            # -> 1
            next_direction = (0, 1)
            next_position = (149 - position[0], 50)
        elif direction == (-1, 0) and next_position[0] < 100:
            # -> 3
            next_direction = (0, 1)
            next_position = (50 + position[1], 50)
    elif 100 <= position[0] < 150 and 50 <= position[1] < 100:
        # 5
        if direction == (0, 1) and next_position[1] >= 100:
            # -> 2
            next_direction = (0, -1)
            next_position = (149 - position[0], 149)
        elif direction == (1, 0) and next_position[0] >= 150:
            # -> 6
            next_direction = (0, -1)
            next_position = (100 + position[1], 49)
    elif 150 <= position[0] < 200 and 0 <= position[1] < 50:
        # 6
        if direction == (0, 1) and next_position[1] >= 50:
            # -> 5
            next_direction = (-1, 0)
            next_position = (149, position[0] - 100)
        elif direction == (1, 0) and next_position[0] >= 200:
            # -> 2
            next_direction = (1, 0)
            next_position = (0, 100 + position[1])
        elif direction == (0, -1) and next_position[1] < 0:
            # -> 1
            next_direction = (1, 0)
            next_position = (0, position[0] - 100)

    return next_position, next_direction

for instruction in instructions:
    if not instruction.isnumeric():
        direction = turns[direction][instruction]
        continue
    
    step = int(instruction)
    for _ in range(step):
        next_position, next_direction = find_next_position(position, direction)

        if board[next_position[0]][next_position[1]] == "#":
            break

        position = next_position
        direction = next_direction

print(1000 * (position[0] + 1) + 4 * (position[1] + 1) + direction_grade[direction])
