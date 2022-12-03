with open("input.txt") as f:
    lines = f.read().split("\n")

total_priority = 0
for line in lines:
    first_compartment_items = set(line[:len(line)//2])
    second_compartment_items = set(line[len(line)//2:])
    common_item = set.intersection(first_compartment_items, second_compartment_items).pop()
    total_priority += ord(common_item) - (96 if common_item.islower() else 38)

print(total_priority)
