with open("input.txt") as f:
    lines = f.read().split("\n")

total_priority = 0
i = 0
while i < len(lines):
    item_sets = map(set, lines[i:i+3])
    common_item = set.intersection(*item_sets).pop()
    total_priority += ord(common_item) - (96 if common_item.islower() else 38)
    i += 3

print(total_priority)
