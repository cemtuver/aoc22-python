import re

with open("input.txt") as f:
    lines = f.read().split("\n")

number_of_overlaps = 0
for line in lines:
    first_start, first_end, second_start, second_end = map(int, re.findall(r"\d+", line))

    if (first_start <= second_start and first_end >= second_end):
        number_of_overlaps += 1
    elif (second_start <= first_start and second_end >= first_end):
        number_of_overlaps += 1

print(number_of_overlaps)
