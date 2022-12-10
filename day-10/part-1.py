with open("input.txt") as f:
    lines = f.read().split("\n")

x = 1
cycle = 1
result = 0

def record_cycle():
    global x
    global cycle
    global result

    if (cycle - 20) % 40 == 0:
        result += x * cycle

for line in lines:
    record_cycle()
    cycle += 1

    if line != "noop":
        record_cycle()
        cycle += 1
        x += int(line.split()[1])

print(result)
