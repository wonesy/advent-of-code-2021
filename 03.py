from typing import List


with open("input/03.txt", "r")  as f:
    lines = f.readlines()

counts: List[int] = [0] * len(lines[0].strip())
print(f"Number of reports = {len(lines)}")

for line in lines:
    for (i,bit) in enumerate(line.strip()):
        counts[i] += int(bit.strip())

gamma = ""
epsilon = ""

for pos in counts:
    if pos <= len(lines) / 2:
        gamma += "0"
        epsilon += "1"
    else:
        gamma += "1"
        epsilon += "0"

print(gamma, int(gamma, 2))
print(epsilon, int(epsilon, 2))


print(int(gamma, 2) * int(epsilon, 2))

        
        