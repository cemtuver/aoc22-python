with open("input.txt") as f:
    lines = f.read().split("\n")

jobs = {}
responses = {}
operations = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x // y
}

for line in lines:
    monkey, job = line.split(": ")
    jobs[monkey] = job

    if job.isnumeric():
        responses[monkey] = int(job)

human_dependents = set()
human_dependents.add("humn")

def find_human_dependents(monkey):
    global jobs
    global responses
    global human_dependents

    if monkey in responses:
        return

    left_operand, _, right_operand = jobs[monkey].split()
    find_human_dependents(left_operand)
    find_human_dependents(right_operand)

    if left_operand in human_dependents or right_operand in human_dependents:
        human_dependents.add(monkey)

def find_response(monkey):
    global jobs
    global responses

    if monkey in responses:
        return responses[monkey]

    left_operand, operation, right_operand = jobs[monkey].split()
    response = operations[operation](find_response(left_operand), find_response(right_operand))

    responses[monkey] = response
    return response

def find_human_response(monkey, target):
    global human_dependents
    global operations

    if monkey == "humn":
        return target

    left_operand, operation, right_operand = jobs[monkey].split()

    if left_operand in human_dependents:
        left_target = 0
        right_response = find_response(right_operand)

        if operation == "+":
            left_target = target - right_response
        elif operation == "-":
            left_target = target + right_response
        elif operation == "*":
            left_target = target // right_response
        else:
            left_target = target * right_response

        return find_human_response(left_operand, left_target)        
    else:
        right_target = 0
        left_response = find_response(left_operand)

        if operation == "+":
            right_target = target - left_response
        elif operation == "-":
            right_target = left_response - target
        elif operation == "*":
            right_target = target // left_response
        else:
            right_target = left_response // target

        return find_human_response(right_operand, right_target)

target = 0
find_human_dependents("root")
left_operand, _, right_operand = jobs["root"].split()

if left_operand in human_dependents:
    print(find_human_response(left_operand, find_response(right_operand)))
else:
    print(find_human_response(right_operand, find_response(left_operand)))
