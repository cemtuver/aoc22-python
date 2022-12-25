import re
import math

with open("input.txt") as f:
    lines = f.read().split("\n")

ORE = 0
CLAY = 1
OBSIDIAN = 2
GEODE = 3
blueprints = []
total_geodes = 1
states = {}

class Blueprint:
    def __init__(self, id, robots, materials, robot_costs, max_costs):
        self.id = id
        self.robots = robots
        self.materials = materials
        self.robot_costs = robot_costs
        self.max_costs = max_costs

class StateKey:
    def __init__(self, robots, materials, times):
        self.tupple = tuple([*robots, *materials, times])

    def __hash__(self) -> int:
        return self.tupple.__hash__()

    def __eq__(self, __o: object) -> bool:
        return self.tupple == __o.tupple

    def __str__(self) -> str:
        return str(self.tupple) 

for line in lines[0:3]:
    id, ore_ore, clay_ore, obsidian_ore, obsidian_clay, geode_ore, geode_obsidian = map(int, re.findall("\d+", line))
    blueprint = Blueprint(
        id, 
        [1, 0, 0, 0], 
        [0, 0, 0, 0], 
        [
            [ore_ore, 0, 0, 0],
            [clay_ore, 0, 0, 0],
            [obsidian_ore, obsidian_clay, 0, 0],
            [geode_ore, 0, geode_obsidian, 0]
        ], 
        [
            max(ore_ore, clay_ore, obsidian_ore, geode_ore),
            obsidian_clay,
            geode_obsidian,
            0
        ]
    )

    blueprints.append(blueprint)

def dfs(blueprint: Blueprint, time):
    global states

    if time == 0:
        return blueprint.materials[GEODE]

    state_key = StateKey(blueprint.robots, blueprint.materials, time)

    if state_key in states:
        return states[state_key]

    max_geodes = blueprint.materials[GEODE] + (blueprint.robots[GEODE] * time)

    for i, robot_cost in enumerate(blueprint.robot_costs):
        should_build = i == GEODE or blueprint.robots[i] < blueprint.max_costs[i]

        if not should_build:
            continue

        required_additional_materials = [required - current for required, current in zip(robot_cost, blueprint.materials)]
        max_required_additional_material = max(required_additional_materials)
        new_materials = blueprint.materials.copy()
        new_robots = blueprint.robots.copy()

        if max_required_additional_material <= 0:
            new_robots[i] += 1
            for j, robot in enumerate(blueprint.robots):
                new_materials[j] += (robot - robot_cost[j])

            max_geodes = max(max_geodes, dfs(Blueprint(blueprint.id, new_robots, new_materials, blueprint.robot_costs, blueprint.max_costs), time - 1))            
        else:
            max_required_time = 0
            has_all_required_robots = True

            for j, required_additional_material in enumerate(required_additional_materials):
                if required_additional_material > 0:
                    if blueprint.robots[j] == 0:
                        has_all_required_robots = False
                        break

                    required_time = math.ceil(required_additional_material / blueprint.robots[j])
                    max_required_time = max(max_required_time, required_time + 1)

            if has_all_required_robots and max_required_time < time:
                new_robots[i] += 1
                for j, robot in enumerate(blueprint.robots):
                    new_materials[j] += robot * max_required_time - robot_cost[j]

                max_geodes = max(max_geodes, dfs(Blueprint(blueprint.id, new_robots, new_materials, blueprint.robot_costs, blueprint.max_costs), time - max_required_time))
        
    states[state_key] = max_geodes

    return max_geodes

for blueprint in blueprints:
    states.clear()
    total_geodes *= dfs(blueprint, 32)

print(total_geodes)
