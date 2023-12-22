import functools as fc 

def getResultOfLine(line: str) -> int:
    card = line.split(':')[1].strip()
    winning = list(filter(None, set(card.split('|')[0].strip().split(' '))))
    my_nums = list(filter(None, card.split('|')[1].strip().split(' ')))
    my_wins = [num for num in my_nums if num in winning]
    res = int(pow(2, len(my_wins) - 1))
    print(f'{my_wins} - {res}\n\n')
    return res

if __name__ == '__main__':
    with open('day4puzzle1input.txt', 'r') as input_file:
        file = input_file.read()
        lines = file.split('\n')
        results = list(map(getResultOfLine, lines))
        sum = fc.reduce(lambda x,y: x + y, results)
        print(sum)