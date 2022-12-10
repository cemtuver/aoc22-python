with open("input.txt") as f:
    lines = f.read().split("\n")

x = 1
cycle = 1
crt_position = 0
pixels: str = ""

def draw_crt():
    global x
    global crt_position
    global pixels

    pixels += "#" if x - 1 <= crt_position and x + 1 >= crt_position else " "
    crt_position += 1 if crt_position < 39 else -39

    if crt_position == 0:
        pixels += "\n"

for line in lines:
    draw_crt()
    cycle += 1

    if line != "noop":
        draw_crt()
        cycle += 1
        x += int(line.split()[1])

print(pixels)
