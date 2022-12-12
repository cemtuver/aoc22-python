with open("input.txt") as f:
    lines = f.read().split("\n")

class InspectOperation:
    def __init__(self, operation_string):
        operation_tokens = operation_string.split()
        self.operation = operation_tokens[4]
        self.is_old_value_operand = operation_tokens[5] == "old"
        if not self.is_old_value_operand:
            self.operand = int(operation_tokens[5])
    
    def __str__(self):
        if self.is_old_value_operand:
            operand = "old"
        else:
            operand = f"{self.operand}"

        return f"new = old {self.operation} {operand}"

    def get_operand(self, old):
        if self.is_old_value_operand:
            return old
        else:
            return self.operand

    def inspect(self, old):
        operand = self.get_operand(old)

        if self.operation == "+":
            new = old + operand
        elif self.operation == "*":
            new = old * operand
        else:
            raise ValueError(f"No operation is defined with operation \"{self.operation}\"")
        return new

class TestOperation:
    def __init__(self, operation_string, true_target_string, false_target_string):
        self.operand = int(operation_string.split()[3])
        self.true_target = int(true_target_string.split()[5])
        self.false_target = int(false_target_string.split()[5])

    def __str__(self):
        return f"% {self.operand}: True -> {self.true_target} False -> {self.false_target}"

    def test(self, value):
        if value % self.operand == 0:
            return self.true_target
        else:
            return self.false_target

class Item:
    def __init__(self, worry_level):
        self.worry_level = worry_level

    def __str__(self):
        return f"{self.worry_level}"

class Monkey:
    def __init__(self, items_string, inspect_operation, test_operation):
        self.items = list(map(
            lambda worry_level: Item(int(worry_level)), 
            items_string.replace("  Starting items: ", "").split(", "))
        )
        self.inspect_operation = inspect_operation
        self.test_opeartion = test_operation
        self.inspected = 0

    def __str__(self): 
        items_string = ", ".join(map(str, self.items))
        inspect_operation_string = str(self.inspect_operation)
        test_opeartion_string = str(self.test_opeartion)

        return f"Items: {items_string}\nOperation: {inspect_operation_string}\nTest: {test_opeartion_string}\n Inspected: {self.inspected}"

    def __repr__(self) -> str:
        return self.__str__()

    def process(self, relief_factor):
        thrown_items = {}
        for item in self.items:
            item.worry_level = self.inspect_operation.inspect(item.worry_level)
            item.worry_level = item.worry_level % relief_factor
            thrown_items[item] = self.test_opeartion.test(item.worry_level)
            self.inspected += 1
        
        return thrown_items

class KeepAwayGame:
    def __init__(self, input):
        self.round = 0
        self.monkeys = []
        self.relief_factor = 1
        self.parse_input(input)

    def parse_input(self, input):
        for i in range(0, len(input), 7):
            monkey = Monkey(
                input[i + 1], 
                InspectOperation(input[i + 2]),
                TestOperation(
                    input[i + 3],
                    input[i + 4],
                    input[i + 5],
                )
            )
            self.monkeys.append(monkey)
            self.relief_factor *= monkey.test_opeartion.operand

    def print(self):
        print()
        print(f"After round {self.round}")
        for i in range(len(self.monkeys)):
            print(f"Monkey #{i}")
            print(self.monkeys[i])
            print()

    def process(self):
        print(f"Processing round {self.round}")
        for i in range(len(self.monkeys)):
            print(f"Processing Monkey #{i}")
            monkey = self.monkeys[i]
            thrown_items = monkey.process(self.relief_factor)
            for thrown_item in thrown_items.keys():
                target_monkey = thrown_items[thrown_item]
                print(f"{thrown_item} -> {target_monkey}")
                monkey.items.remove(thrown_item)
                self.monkeys[target_monkey].items.append(thrown_item)
        self.round += 1

keep_away_game = KeepAwayGame(lines)
keep_away_game.print()

for _ in range(10000):
    keep_away_game.process()
    keep_away_game.print()

most_active_monkeys = sorted(list(map(lambda monkey: monkey.inspected, keep_away_game.monkeys)))
print(most_active_monkeys[-1] * most_active_monkeys[-2])
