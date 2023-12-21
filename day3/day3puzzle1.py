from collections import defaultdict
from typing import Dict, Tuple

def isSymbol(ch: str) -> bool:
    if not (ch == '.' or '0' <= ch <= '9'):
        return True
    return False

def iterate1(line: str) -> list:
    res = []
    for j, ch in enumerate(line):
        if isSymbol(ch):
            pass
            #TO-DO - append for the square surrounding the symbol

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


