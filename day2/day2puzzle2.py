from typing import Dict, List
import functools as fc

def parseDraw(draw: str) -> Dict:
    # example of draw: 6 red
    res = {}
    lst = draw.strip().split(' ')
    res['quantity'] = int(lst[0])
    res['color'] = lst[1]
    return res

def parseReveal(reveal: str) -> List[Dict]:
    # example of reveal: 6 red, 1 blue, 3 green
    draws = reveal.strip().split(',')
    res = list(map(parseDraw, draws))
    return res

# returns the list of draws
def parseRound(round: str) -> List[Dict]:
    # example of round: '6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'
    reveals = round.strip().split(';')
    res = []
    [res.extend(parseReveal(reveal)) for reveal in reveals]
    return res

# returns index of game
def parseGame(game: str) -> int:
    # example of game: 'Game 1'
    return int(game.split(' ')[1])

# returns the game dictionary
def parseLine(line: str) -> Dict:
    game = {}
    data = line.strip().split(':')
    game['gameNo'] = parseGame(data[0])
    game['draws'] = parseRound(data[1])
    return game

def handleGame(game: Dict) -> int:
    print(game)

# our main goal has two parts:
# 1. making a list of the dictionary:
# game = { 
#             gameNo : number_of_game,
#             draws: [
#                 {color : 'red',
#                  quantity : 6},
#                  {color : 'green',
#                  quantity : 6},
#                  {color : 'blue',
#                  quantity : 6}
#             ]
#         }

# 2. proccessing the games by the question (i.e finding the max for each)

if __name__ == '__main__':
    with open('/home/toker/advent-of-code/day2/day2puzzle1input.txt', 'r') as input_file:
        file = input_file.read()
        lines = file.split('\n')
        games = list(map(parseLine, lines))
        results = list(map(handleGame, games))
        sum = fc.reduce(lambda x,y: x + y, results)
        print(sum)