with open("input.txt") as f:
    jets = f.read()

jet_index = 0
rock_count = 0
height = 0
chamber = set()
rock_producers = [
    lambda x, y: [(x, y), (x + 1, y), (x + 2, y), (x + 3, y)],
    lambda x, y: [(x + 1, y), (x, y + 1), (x + 1, y + 1), (x + 2, y + 1), (x + 1, y + 2)],
    lambda x, y: [(x, y), (x + 1, y), (x + 2, y), (x + 2, y + 1), (x + 2, y + 2)],
    lambda x, y: [(x, y), (x, y + 1), (x, y + 2), (x, y + 3)],
    lambda x, y: [(x, y), (x + 1, y), (x, y + 1), (x + 1, y + 1)]
]

def push_rock_to_left(rock):
    global chamber

    for piece in rock:
        if piece[0] == 0 or (piece[0] - 1, piece[1]) in chamber:
            return rock

    return list(map(lambda piece: (piece[0] - 1, piece[1]), rock))

def push_rock_to_right(rock):
    global chamber

    for piece in rock:
        if piece[0] == 6 or (piece[0] + 1, piece[1]) in chamber:
            return rock

    return list(map(lambda piece: (piece[0] + 1, piece[1]), rock))

def push_rock(rock):
    global jets
    global jet_index

    jet = jets[jet_index]
    jet_index = jet_index + 1 if jet_index < len(jets) - 1 else 0

    if jet == ">":
        return push_rock_to_right(rock)
    else:
        return push_rock_to_left(rock)

def fall_rock(rock):
    global chamber

    for piece in rock:
        if piece[1] == 0 or (piece[0], piece[1] - 1) in chamber:
            return rock, True

    return list(map(lambda piece: (piece[0], piece[1] - 1), rock)), False

def add_to_chamber(rock):
    global chamber

    for piece in rock:
        chamber.add(piece)

def print_chamber(rock):
    global height
    global chamber

    print()
    for y in range(height + 5, -1, -1):
        line = "|"
        for x in range(7):
            line += "#" if ((x, y) in chamber or (x, y) in rock) else "."
        line += "|"
        print(line)
    print("=========")

while rock_count < 2022:
    rock_producer = rock_producers[rock_count % len(rock_producers)]
    rock = rock_producer(2, height + 3)
    
    while True:
        # print_chamber(rock)
        rock = push_rock(rock)
        rock, is_resting = fall_rock(rock)

        if is_resting:
            add_to_chamber(rock)
            height = max(height, rock[-1][1] + 1)
            # print_chamber(rock)
            break

    rock_count += 1

print(height)
