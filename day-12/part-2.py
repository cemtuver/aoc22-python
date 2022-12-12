with open("input.txt") as f:
    lines = f.read().split("\n")

row_size = len(lines)
column_size = len(lines[0])
neighbour_diffs = [[-1, 0], [0, -1], [1, 0], [0, 1]]

class Node:
    def __init__(self, row, column):
        self.row = row
        self.column = column

    def __eq__(self, obj: object):
        return isinstance(obj, Node) and self.row == obj.row and self.column == obj.column

    def __hash__(self):
        return hash(f"{self.row}:{self.column}")

    def add(self, diff):
        return Node(self.row + diff[0], self.column + diff[1])

    def is_valid(self):
        global row_size
        global column_size
        return 0 <= self.row < row_size and 0 <= self.column < column_size

    def get_valid_neighbours(self):
        global neighbour_diffs
        
        valid_neighbours = []
        for neighbour_diff in neighbour_diffs:
            neighbour = self.add(neighbour_diff)
            if neighbour.is_valid():
                valid_neighbours.append(neighbour)
        
        return valid_neighbours

costs = [[float("inf") for _ in range(column_size)] for _ in range(row_size)]
heights = [[ord(lines[row][column]) for column in range(column_size)] for row in range(row_size)]
not_visiteds = set(Node(row, column) for column in range(column_size) for row in range(row_size))

end = Node(-1, -1)
for row in range(row_size):
    for column in range(column_size):
        height = heights[row][column]
        if height == ord('S'):
            heights[row][column] = ord('a')
        elif height == ord('E'):
            end = Node(row, column)
            heights[row][column] = ord('z')
            costs[row][column] = 0

current = Node(-1, -1)
while len(not_visiteds) > 0:
    min_cost = float("inf")
    for node in not_visiteds:
        cost = costs[node.row][node.column]
        if cost < min_cost:
            current = node
            min_cost = cost

    if heights[current.row][current.column] == ord('a'):
        break

    for neighbour in current.get_valid_neighbours():
        if (
            neighbour in not_visiteds and 
            heights[current.row][current.column] <= heights[neighbour.row][neighbour.column] + 1
        ):
            costs[neighbour.row][neighbour.column] = min(costs[neighbour.row][neighbour.column], costs[current.row][current.column] + 1)

    not_visiteds.remove(current)

print(costs[current.row][current.column])
