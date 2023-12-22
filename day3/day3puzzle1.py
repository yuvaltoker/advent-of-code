from collections import defaultdict
from typing import Dict, Tuple, List

def isSymbol(ch: str) -> bool:
    if not (ch == '.' or '0' <= ch <= '9'):
        return True
    return False

def getSurroundingPoints(i: int, j: int) -> List[int]:
    res = [(i - 1,col) for col in range(j-1, j+2)]
    res.extend([(i, j - 1),(i, j + 1)])
    res.extend([(i + 1, col) for col in range(j - 1, j + 2)])
    return res

def iterate1(line: str, row: int) -> List:
    res = []
    for j, ch in enumerate(line):
        if isSymbol(ch):
            res.extend(getSurroundingPoints(row, j))
    return res

def iterate2(symbols: Dict, line: str) -> int:
    pass

if __name__ == '__main__':
    with open('/home/toker/advent-of-code/day2/day3puzzle1input.txt', 'r') as input_file:
        file = input_file.read()
        lines = file.split('\n')
        symbols = {}
        for row, line in enumerate(lines):
            symbols[row] = iterate1(line)
        sum = 0
        for line in lines:
            sum += iterate2(symbols, line)
        print(sum)


