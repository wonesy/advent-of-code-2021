from dataclasses import dataclass
from typing import List
import sys

class Space:
    value: int
    marked: bool = False

    def __init__(self, value: int) -> None:
        self.value = value


@dataclass
class Board:
    spaces: List[Space]
    marks: List[bool]

    def __init__(self, spaces: List[str]) -> None:
        self.spaces = spaces
        self.marks = [False] * len(self.spaces)

    def mark(self, value: str):
        if value in self.spaces:
            # print(f"marking {value} @ {self.spaces.index(value)}")
            self.marks[self.spaces.index(value)] = True

    def sum_unmarked(self) -> int:
        sum = 0
        for (i, val) in enumerate(self.spaces):
            if not self.marks[i]:
                sum += int(val)
        return sum

    def is_winner(self) -> bool:
        # rows
        for i in range(5):
            # row
            start = 0 + (5*i)
            end = 5 + (5*i)

            if all(self.marks[start:end]):
                return True

            # col
            if all([
                self.marks[0+i], 
                self.marks[5+i], 
                self.marks[10+i], 
                self.marks[15+i], 
                self.marks[20+i]
            ]):
                return True

        return False

    def display(self) -> None:
        pass


boards = []
with open("input/04.txt", "r")  as f:
    draws = f.readline().strip().split(',')
    _ = f.readline()

    new_board = []
    for line in f:
        if line.strip() == "":
            boards.append(Board(new_board))
            new_board = []
            continue
        new_board.extend(list(filter(lambda x: x != '', line.strip().split(' '))))
    boards.append(Board(new_board))

for draw in draws:
    print(draw)
    for board in boards:
        board.mark(draw)

        if board.is_winner():
            sum = board.sum_unmarked()

            print("WINNER")
            print("DRAW", draw)
            print("SUM", sum)
            print(int(draw) * sum)
            sys.exit(0)

# print(boards)