with open("input.txt") as f:
    lines = f.read().split("\n")

row = len(lines)
column = len(lines[0])
trees = [[lines[r][c] for c in range(column)] for r in range(row)]

visible = 2 * row + 2 * (column - 2)
for r in range(1, row - 1):
    for c in range(1, column - 1):
        tree = trees[r][c]

        if (
            all(trees[r][left_c] < tree for left_c in range(c)) or
            all(trees[r][right_c] < tree for right_c in range(c + 1, column)) or
            all(trees[top_r][c] < tree for top_r in range(r)) or
            all(trees[bottom_r][c] < tree for bottom_r in range(r + 1, row))
        ):
            visible += 1

print(visible)
