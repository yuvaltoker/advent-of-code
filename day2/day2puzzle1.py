import functools as fc

def isValid(color: str, quantity: int) -> bool:
    bag = {'red' : 12, 'green' : 13, 'blue' : 14}
    if quantity <= bag[color]:
        return True
    return False

#TO-DO
def isPartValid(draw: str) -> bool:
    # example of draw: '1 red'
    parts = draw.strip().split(' ')
    return isValid(parts[1], int(parts[0]))

def isRoundValid(rounds: list[str]) -> bool:
    # example of round: '6 red, 1 blue, 3 green'
    parts = []
    for round in rounds:
        parts.extend(round.split(','))
    return all(list(map(isPartValid, parts)))

# returns index of game
def handleGame(game: str) -> int:
    return int(game.split(' ')[1])

# returns game No.x in case of valid game, else returns 0
def getResultOfLine(game: str) -> int:
    # example of line: 'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green' 
    data = game.split(':')
    game_number = handleGame(data[0])
    valid = isRoundValid(data[1].split(';'))
    if valid:
        return game_number
    return 0

if __name__ == '__main__':
    with open('day2puzzle1input.txt', 'r') as input_file:
        file = input_file.read()
        lines = file.split('\n')
        results = list(map(getResultOfLine, lines))
        sum = fc.reduce(lambda x,y: x + y, results)
        print(sum)