with open("input.txt") as f:
    lines = f.read().split("\n")

row = len(lines)
column = len(lines[0])
trees = [[lines[r][c] for c in range(column)] for r in range(row)]

max_score = 0
for r in range(row):
    for c in range(column):
        tree = trees[r][c]
        left_visible = 0
        right_visible = 0
        top_visible = 0
        bottom_visible = 0

        for left_c in reversed(range(c)):
            left_visible += 1
            if trees[r][left_c] >= tree:
                break

        for right_c in range(c + 1, column):
            right_visible += 1
            if trees[r][right_c] >= tree:
                break

        for top_r in reversed(range(r)):
            top_visible += 1
            if trees[top_r][c] >= tree:
                break

        for bottom_r in range(r + 1, row):
            bottom_visible += 1
            if trees[bottom_r][c] >= tree:
                break

        score = left_visible * right_visible * top_visible * bottom_visible
        max_score = max(max_score, score)

print(max_score)
