import time

with open("input.txt") as f:
    lines = f.read().replace("=", ",").replace(":", ",").split("\n")

class ScanResult:
    def __init__(self, sensor, beacon) -> None:
        self.sensor = sensor
        self.beacon = beacon
        self.distance = self._calcualte_distance(beacon)

    def __str__(self) -> str:
        return f"S: {self.sensor} B: {self.beacon} Dist: {self.distance}"

    def _calcualte_distance(self, node) -> int:
        return abs(self.sensor[0] - node[0]) + abs(self.sensor[1] - node[1])

    def covers(self, node) -> bool:
        return self._calcualte_distance(node) <= self.distance

scan_results = []
for line in lines:
    _, sensor_x, _, sensor_y, _, beacon_x, _, beacon_y = line.split(",")
    scan_result = ScanResult((int(sensor_x), int(sensor_y)), (int(beacon_x), int(beacon_y)))
    scan_results.append(scan_result)

max_xy = 4000000
free_areas = []
for scan_result in scan_results:
    print(scan_result)
    free_area = set()
    free_x, free_y = scan_result.sensor[0], scan_result.sensor[1] - scan_result.distance - 1

    for _ in range(scan_result.distance + 1):
        if 0 <= free_x <= max_xy and 0 <= free_y <= max_xy:
            free_area.add((free_x, free_y))
        free_x -= 1
        free_y += 1

    for _ in range(scan_result.distance + 1):
        if 0 <= free_x <= max_xy and 0 <= free_y <= max_xy:
            free_area.add((free_x, free_y))
        free_x += 1
        free_y += 1

    for _ in range(scan_result.distance + 1):
        if 0 <= free_x <= max_xy and 0 <= free_y <= max_xy:
            free_area.add((free_x, free_y))
        free_x += 1
        free_y -= 1

    for _ in range(scan_result.distance + 1):
        if 0 <= free_x <= max_xy and 0 <= free_y <= max_xy:
            free_area.add((free_x, free_y))
        free_x -= 1
        free_y -= 1        

    free_areas.append(free_area)

found = False
found_point = (0, 0)
for free_area in free_areas:
    if found:
        break
    for point in free_area:
        if found:
            break
        
        found = True
        found_point = point

        for scan_result in scan_results:
            if scan_result.covers(point):
                found = False
                break

print(found_point[0] * max_xy + found_point[1])
