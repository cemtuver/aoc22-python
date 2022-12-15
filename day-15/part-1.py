import time

with open("input.txt") as f:
    lines = f.read().replace("=", ",").replace(":", ",").split("\n")

class ScanResult:
    def __init__(self, sensor, beacon) -> None:
        self.sensor = sensor
        self.beacon = beacon
        self.distance = self._calcualte_distance(sensor, beacon)

    def __str__(self) -> str:
        return f"S: {self.sensor} B: {self.beacon} Dist: {self.distance}"

    def _calcualte_distance(self, sensor, beacon) -> int:
        return abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])

scan_results = []
for line in lines:
    _, sensor_x, _, sensor_y, _, beacon_x, _, beacon_y = line.split(",")
    scan_result = ScanResult((int(sensor_x), int(sensor_y)), (int(beacon_x), int(beacon_y)))
    scan_results.append(scan_result)

row = 2000000
covered_areas = set()
beacons_on_row = set()
for scan_result in scan_results:
    distance_to_row = abs(row - scan_result.sensor[1])
    scan_window_on_row = scan_result.distance - distance_to_row

    if scan_window_on_row < 0:
        continue

    for i in range(scan_window_on_row + 1):
        covered_areas.add((scan_result.sensor[0] + i, row))
        covered_areas.add((scan_result.sensor[0] - i, row))

    if scan_result.beacon[1] == row:
        beacons_on_row.add(scan_result.beacon)

print(len(covered_areas - beacons_on_row))
