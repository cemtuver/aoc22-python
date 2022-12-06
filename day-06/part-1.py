with open("input.txt") as f:
    line = f.read()

left = 0
right = 3
marker = [line[i] for i in range(4)]

while len(set(marker)) < 4:
    marker.remove(line[left])
    left += 1
    right += 1
    marker.append(line[right])

print(right + 1)
