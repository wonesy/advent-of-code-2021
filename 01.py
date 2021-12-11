with open("input/01.txt", "r")  as f:
    lines = f.readlines()

increases = 0
for (i, line) in enumerate(lines):
    if i == 0:
        continue
    if int(lines[i-1]) < int(line):
        increases += 1
print(increases)