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

def find_response(monkey):
    global jobs
    global responses

    if monkey in responses:
        return responses[monkey]

    left_operand, operation, right_operand = jobs[monkey].split()
    response = operations[operation](find_response(left_operand), find_response(right_operand))

    responses[monkey] = response
    return response

print(find_response("root"))
