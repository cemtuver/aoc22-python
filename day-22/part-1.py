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
    (-1, 0): 2
}

row_limits = []
column_limits = []

for r in range(len(board)):
    left = 0
    right = 0

    while board[r][left] == " ":
        left += 1
        right += 1

    while right < len(board[0]) and board[r][right] != " ":
        right += 1

    row_limits.append((left, right - 1))

for c in range(len(board[0])):
    top = 0
    bottom = 0

    while board[top][c] == " ":
        top += 1
        bottom += 1

    while bottom < len(board) and board[bottom][c] != " ":
        bottom += 1

    column_limits.append((top, bottom - 1))

def find_next_position(position, direction):
    next_position = (position[0] + direction[0], position[1] + direction[1])

    if direction[0] != 0:
        limits = column_limits[position[1]]

        if next_position[0] < limits[0]:
            next_position = (limits[1], next_position[1])
        elif next_position[0] > limits[1]:
            next_position = (limits[0], next_position[1])
    else:
        limits = row_limits[position[0]]

        if next_position[1] < limits[0]:
            next_position = (next_position[0], limits[1])
        elif next_position[1] > limits[1]:
            next_position = (next_position[0], limits[0])

    return next_position

for instruction in instructions:
    if not instruction.isnumeric():
        direction = turns[direction][instruction]
        continue
    
    step = int(instruction)
    for _ in range(step):
        next_position = find_next_position(position, direction)

        if board[next_position[0]][next_position[1]] == "#":
            break

        position = next_position

print(1000 * (position[0] + 1) + 4 * (position[1] + 1) + direction_grade[direction])
