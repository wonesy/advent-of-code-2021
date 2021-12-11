"""
    forward X increases the horizontal position by X units.
    down X increases the depth by X units.
    up X decreases the depth by X units.
"""

with open("input/02.txt", "r")  as f:
    directions = f.readlines()

def o(order: str) -> str:
    return order.strip().lower()

depth = 0
advance = 0
for dir in directions:
    _order, val = dir.split(' ')
    order = o(_order)

    if order == "forward":
        advance += int(val)

    if order == "up":
        depth -= int(val)

        if depth < 0:
            depth = 0

    if order == "down":
        depth += int(val)

print(f"Position {advance}")
print(f"Depth {depth}")

print(depth*advance)
    