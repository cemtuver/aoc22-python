import time

with open("input.txt") as f:
    jets = f.read()

jet_index = 0
rock_count = 0
rock_limit = 1000000000000
height = 0
chamber = set()
cycle_height = 0
states = {}
rock_producers = [
    lambda x, y: [(x, y), (x + 1, y), (x + 2, y), (x + 3, y)],
    lambda x, y: [(x + 1, y), (x, y + 1), (x + 1, y + 1), (x + 2, y + 1), (x + 1, y + 2)],
    lambda x, y: [(x, y), (x + 1, y), (x + 2, y), (x + 2, y + 1), (x + 2, y + 2)],
    lambda x, y: [(x, y), (x, y + 1), (x, y + 2), (x, y + 3)],
    lambda x, y: [(x, y), (x + 1, y), (x, y + 1), (x + 1, y + 1)]
]

class StateKey:
    def __init__(self, ys, rock_index, jet_index):
        self.hash_str = ",".join(map(str, ys))
        self.hash_str += f";{rock_index};{jet_index}"

    def __hash__(self) -> int:
        return self.hash_str.__hash__()

    def __eq__(self, __o: object) -> bool:
        return self.hash_str == __o.hash_str

    def __str__(self) -> str:
        return self.hash_str

class StateValue:
    def __init__(self, rock_count, height):
        self.rock_count = rock_count
        self.height = height

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

def check_for_cycle(rock_index):
    global chamber
    global cycle_height
    global rock_count
    global rock_limit
    global height

    max_ys = [-1 for _ in range(7)]
    for piece in chamber:
        max_ys[piece[0]] = max(max_ys[piece[0]], piece[1])

    min_y = min(max_ys)
    minified_ys = [y - min_y for y in max_ys]
    state_key = StateKey(minified_ys, rock_index, jet_index)

    if state_key not in states:
        states[state_key] = StateValue(rock_count, height)
    else:
        state_value = states[state_key]
        rocks_per_cycle = rock_count - state_value.rock_count
        rocks_remaining = rock_limit - rock_count
        cycle_height = (height - state_value.height) * (rocks_remaining // rocks_per_cycle)
        rock_count = rock_limit - (rocks_remaining % rocks_per_cycle)

while rock_count < rock_limit:
    rock_index = rock_count % len(rock_producers)
    rock_producer = rock_producers[rock_index]
    rock = rock_producer(2, height + 3)
    
    while True:
        # print_chamber(rock)
        rock = push_rock(rock)
        rock, is_resting = fall_rock(rock)

        if is_resting:
            add_to_chamber(rock)
            height = max(height, rock[-1][1] + 1)
            # print_chamber(rock)

            if cycle_height <= 0:
                check_for_cycle(rock_index)

            break

    rock_count += 1

print(cycle_height + height)
