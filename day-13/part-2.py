import functools

with open("input.txt") as f:
    lines = f.read().split("\n")

class Package:
    def __init__(self):
        self.parent = None

class Value(Package):
    def __init__(self, value):
        super(Value, self).__init__()
        self.value = value

    def __str__(self) -> str:
        return f"{self.value} "

class Container(Package):
    def __init__(self):
        super(Container, self).__init__()
        self.children = []

    def add_child(self, package: Package):
        package.parent = self
        self.children.append(package)

    def __str__(self) -> str:
        children_string = " ".join(map(str, self.children))
        return f"[{children_string}]"

def parse(input: str) -> Container:
    root = Container()
    current = root
    i = 1

    while i < len(input) - 1:
        char = input[i]

        if char == '[':
            child = Container()
            current.add_child(child)
            current = child
        elif char == ']':
            current = current.parent
        elif char.isnumeric():
            number = char
            while input[i + 1].isnumeric():
                number += input[i + 1]
                i += 1

            child = Value(int(number))
            current.add_child(child)
        else:
            pass

        i += 1

    return root

def ensure_container(package: Package) -> Container:
    if isinstance(package, Container):
        return package

    container = Container()
    container.add_child(package)
    
    return container

def compare(left: Container, right: Container) -> int:
    print(f"Comparing")
    print(f"  {left}")
    print(f"  {right}")
    for left_child, right_child in zip(left.children, right.children):
        if isinstance(left_child, Value) and isinstance(right_child, Value):
            if left_child.value < right_child.value:
                return -1
            elif left_child.value > right_child.value:
                return 1
        else:
            left_child_container = ensure_container(left_child)
            right_child_container = ensure_container(right_child)
            result = compare(left_child_container, right_child_container)

            if result != 0:
                return result

    if len(left.children) < len(right.children):
        return -1
    elif len(left.children) > len(right.children):
        return 1
    else:
        return 0

def find_insert_index(containers: list[Container], item: Container) -> int:
    i = 0
    
    while i < len(containers):
        if compare(item, containers[i]) <= 0:
            break
        i += 1

    return i + 1


containers = []
for line in lines:
    if line != "":
        containers.append(parse(line))

sorted_containers = sorted(containers, key=functools.cmp_to_key(compare))
divider_packet_2_index = find_insert_index(sorted_containers, parse("[[2]]"))
divider_packet_6_index = find_insert_index(sorted_containers, parse("[[6]]")) + 1

print(divider_packet_2_index * divider_packet_6_index)
