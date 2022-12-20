with open("input.txt") as f:
    input = f.read()
    input = input.replace("Valve ", "")
    input = input.replace("has flow rate=", "")
    input = input.replace("; tunnels lead to valves", "")
    input = input.replace("; tunnel leads to valve", "")
    input = input.replace(", ", ",")
    lines = input.split("\n")

valves = []
positive_valves = []
flows = {}
tunnels = {}

for line in lines:
    valve, flow_str, tunnels_str = line.split(" ")
    
    flows[valve] = int(flow_str)
    tunnels[valve] = tunnels_str.split(",")
    valves.append(valve)
    if flows[valve] > 0:
        positive_valves.append(valve)

distances = { valve_from: { valve_to: 0 if valve_from == valve_to else 99999 for valve_to in valves } for valve_from in valves }

for valve in valves:
    for tunnel in tunnels[valve]:
        distances[valve][tunnel] = 1

    for k in valves:
        for i in valves:
            for j in valves:
                distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])    

def dfs(current_valve, open_valves, time):
    result = []
    result.append(open_valves)

    for next_valve in positive_valves:
        if next_valve not in open_valves and distances[current_valve][next_valve] < time:
            next_open_valves = open_valves.copy()
            next_open_valves.append(next_valve)
            next_result = dfs(next_valve, next_open_valves, time - distances[current_valve][next_valve] - 1)
            result.extend(next_result)

    return result

time = 26
start_valve = "AA"
paths = dfs(start_valve, [], time)
path_flows = [0 for _ in paths]

for i, path in enumerate(paths):
    flow = 0
    remaining_time = time
    current_valve = start_valve

    for next_valve in path:
        remaining_time -= (distances[current_valve][next_valve] + 1)
        flow += flows[next_valve] * remaining_time
        current_valve = next_valve
    
    path_flows[i] = flow

max_flow = 0
paths = list(map(set, paths))

for i in range(len(paths)):
    for j in range(i + 1, len(paths)):
        if paths[i].isdisjoint(paths[j]):
            max_flow = max(max_flow, path_flows[i] + path_flows[j])

print(max_flow)
