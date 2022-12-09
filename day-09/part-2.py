with open("input.txt") as f:
    lines = f.read().split("\n")

class Knot:
    def __init__(self):
        self.x = 0
        self.y = 0

    def move(self, direction):
        if (direction == "L"):
            self.x -= 1
        elif(direction == "U"):
            self.y += 1
        elif(direction == "R"):
            self.x += 1
        else:
            self.y -= 1

    def follow(self, other):
        if abs(other.x - self.x) <= 1 and abs(other.y - self.y) <= 1:
            return
        
        if other.x > self.x:
            self.x += 1
        elif other.x < self.x:
            self.x -= 1

        if other.y > self.y:
            self.y += 1
        elif other.y < self.y:
            self.y -= 1

knots = [Knot() for _ in range(10)]
visited = set()
for line in lines:
    direction, step = line.split()
    for _ in range(int(step)):
        knots[-1].move(direction)
        for i in reversed(range(9)):
            knots[i].follow(knots[i + 1])
        visited.add((knots[0].x, knots[0].y))

print(len(visited))
