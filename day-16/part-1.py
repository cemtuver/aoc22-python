with open("input.txt") as f:
    input = f.read()
    input = input.replace("Valve ", "")
    input = input.replace("has flow rate=", "")
    input = input.replace("; tunnels lead to valves", "")
    input = input.replace("; tunnel leads to valve", "")
    input = input.replace(", ", ",")
    lines = input.split("\n")

flows = {}
tunnels = {}
for line in lines:
    valve, flow_str, tunnels_str = line.split(" ")
    
    flows[valve] = int(flow_str)
    tunnels[valve] = tunnels_str.split(",")

class State:
    def __init__(self, valve, open_valves, time) -> None:
        open_valves_str = ";".join(open_valves)
        self.hash_str = f"{valve};{open_valves_str};{time}"

    def __hash__(self) -> int:
        return self.hash_str.__hash__()

    def __eq__(self, __o: object) -> bool:
        return self.hash_str == __o.hash_str

cache = {}
def dfs(current_valve, current_flow, open_valves, time):
    key = State(current_valve, open_valves, time)
    if key in cache:
        return cache[key]

    if time <= 0:
        return current_flow

    max_flow = 0

    if current_valve not in open_valves and flows[current_valve] > 0:
        next_open_valves = open_valves.copy()
        next_open_valves.append(current_valve)
        next_flow = current_flow + flows[current_valve] * (time - 1)
        max_flow = dfs(current_valve, next_flow, next_open_valves, time - 1)

    for tunnel in tunnels[current_valve]:
        max_flow = max(max_flow, dfs(tunnel, current_flow, open_valves.copy(), time - 1))

    cache[key] = max_flow
    return max_flow

print(dfs("AA", 0, [], 30))
