with open("input.txt") as f:
    lines = f.read().split("\n")
    lines.append("")

max_calories = []
current_calories = 0
for line in lines:
    if (line == ""):
        max_calories.append(current_calories)
        current_calories = 0
        continue

    current_calories += int(line)

max_calories.sort(reverse=True)
print(sum(max_calories[0:3]))