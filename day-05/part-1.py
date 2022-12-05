import re

with open("input.txt") as f:
    lines = f.read().split("\n")

divider_index = lines.index("")
stack_count = (len(lines[0]) + 1) // 4
stacks = [[] for _ in range(stack_count)]

for line in lines[:divider_index - 1]:
    for stack_index in range(0, stack_count):
        crate = line[stack_index * 4 + 1]
        if crate != " ":
            stacks[stack_index].append(crate)

for stack in stacks:
    stack.reverse()

for line in lines[divider_index + 1:]:
    count, source, destionation = map(int, re.match(r"move (\d+) from (\d+) to (\d+)", line).groups())
    stacks[destionation - 1] = stacks[destionation - 1] + list(reversed(stacks[source - 1][-count:]))
    stacks[source - 1] = stacks[source - 1][:-count]

message = ""
for stack in stacks:
    if len(stack) > 0:
        message += stack.pop()

print(message)
