with open("input.txt") as f:
    lines = f.read().split("\n")
    lines.append("")

max_calories = 0
current_calories = 0
for line in lines:
    if (line == ""):
        max_calories = max(max_calories, current_calories)
        current_calories = 0
        continue

    current_calories += int(line)

print(max_calories)