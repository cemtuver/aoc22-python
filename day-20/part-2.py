with open("input.txt") as f:
    lines = f.read().split("\n")

class Node:
    def __init__(self, number, prev, next, original_next):
        global lines

        self.number = number * 811589153
        self.rotate_number = abs(self.number) % (len(lines) - 1)
        self.prev = prev
        self.next = next
        self.original_next = original_next

numbers = list(map(int, lines))
head = Node(numbers[0], None, None, None)
current = head

for number in numbers[1:]:
    next = Node(number, current, None, None)
    current.next = next
    current.original_next = next
    current = next

current.next = head
head.prev = current

for _ in range(10):
    current = head

    while current:
        number = current.number
        rotate_number = current.rotate_number
        original_next = current.original_next

        if number != 0:
            current.prev.next = current.next
            current.next.prev = current.prev

            for _ in range(rotate_number):
                if number > 0:
                    current.prev = current.next
                    current.next = current.next.next
                else:
                    current.next = current.prev
                    current.prev = current.prev.prev

            current.prev.next = current
            current.next.prev = current   

        current = original_next    

zero = None
current = head

while not zero:
    if current.number == 0:
        zero = current
    
    current = current.next

n = 1
n_1000 = None
n_2000 = None
n_3000 = None

for n in range(1, 3001):
    if n == 1000:
        n_1000 = current
    elif n == 2000:
        n_2000 = current
    elif n == 3000:
        n_3000 = current

    current = current.next

print(sum([n_1000.number, n_2000.number, n_3000.number]))
