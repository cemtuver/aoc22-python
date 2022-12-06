with open("input.txt") as f:
    line = f.read()

left = 0
right = 13
marker = [line[i] for i in range(14)]

while len(set(marker)) < 14:
    marker.remove(line[left])
    left += 1
    right += 1
    marker.append(line[right])

print(right + 1)
