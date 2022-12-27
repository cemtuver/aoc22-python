with open("input.txt") as f:
    lines = f.read().split("\n")

N = 0
E = 1
S = 2
W = 3
elves = set()
neighbour_producers = {
    N: (lambda r, c: [(r - 1, c - 1), (r - 1, c), (r - 1, c + 1)]),
    E: (lambda r, c: [(r - 1, c + 1), (r, c + 1), (r + 1, c + 1)]),
    S: (lambda r, c: [(r + 1, c + 1), (r + 1, c), (r + 1, c - 1)]),
    W: (lambda r, c: [(r + 1, c - 1), (r, c - 1), (r - 1, c - 1)])
}
neighbour_checks = [
    lambda neighbours, r, c: (r - 1, c) if neighbours[N] == 0 else None,
    lambda neighbours, r, c: (r + 1, c) if neighbours[S] == 0 else None,
    lambda neighbours, r, c: (r, c - 1) if neighbours[W] == 0 else None,
    lambda neighbours, r, c: (r, c + 1) if neighbours[E] == 0 else None,
]

for r, line in enumerate(lines):
    for c, char in enumerate(line):
        if char == "#":
            elves.add((r, c))

def get_neighbours(elf):
    r, c = elf
    neighbours = { N: 0b000, E: 0b000, S: 0b000, W: 0b000 }

    for key, neighbour_producer in neighbour_producers.items():
        neighbour_coordinates = neighbour_producer(r, c)

        for i, neighbour in enumerate(neighbour_coordinates):
            if neighbour in elves:
                neighbours[key] |= 1 << i

    return neighbours

def get_proposed_position(elf):
    r, c = elf
    neighbours = get_neighbours(elf)

    if all(map(lambda neighbour: neighbour == 0, neighbours.values())):
        return None

    for neighbour_check in neighbour_checks:
        neighbour_checks_result = neighbour_check(neighbours, r, c)

        if neighbour_checks_result is not None:
            return neighbour_checks_result

    return None

for i in range(10):
    proposed_positions = {}

    for elf in elves:
        proposed_position = get_proposed_position(elf)

        if proposed_position is None:
            continue

        if proposed_position not in proposed_positions:
            proposed_positions[proposed_position] = []

        proposed_positions[proposed_position].append(elf)

    for proposed_position, propsed_elves in proposed_positions.items():
        if len(propsed_elves) > 1:
            continue

        elves.remove(propsed_elves[0])
        elves.add(proposed_position)

    neighbour_checks = [*neighbour_checks[1:], neighbour_checks[0]]

top_left = None
bottom_right = None

for elf in elves:
    if top_left is None:
        top_left = elf
        bottom_right = elf
        continue

    top_left = (min(top_left[0], elf[0]), min(top_left[1], elf[1]))
    bottom_right = (max(bottom_right[0], elf[0]), max(bottom_right[1], elf[1]))

print((abs(top_left[0] - bottom_right[0]) + 1) * (abs(top_left[1] - bottom_right[1]) + 1) - len(elves))
