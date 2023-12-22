import functools as fc 
from typing import Tuple, List, Dict

# calculates instances of next cards and returns how many instances of a card accure
def getQuantityOfCard(cards_dict_list: List, card_index: int) -> int:
    for index in range(card_index + 1, card_index + 1 + cards_dict_list[card_index]['matches']):
        if index <= len(cards_dict_list) - 1:
            cards_dict_list[index]['instances'] += cards_dict_list[card_index]['instances']
        else:
            break
    return cards_dict_list[card_index]['instances']

# build the cards' info dict
def proccessCard(card: Tuple[List, List]) -> Dict:
    [winning, my_nums] = card
    my_wins = [num for num in my_nums if num in winning]
    card_dict = { 'instances' : 1, 'matches' : len(my_wins)}
    return card_dict

# returns tuple of two lists - winning numbers and my numbers for each card 
def getResultOfLine(line: str) -> Tuple[List, List]:
    card = line.split(':')[1].strip()
    winning = list(filter(None, set(card.split('|')[0].strip().split(' '))))
    my_nums = list(filter(None, card.split('|')[1].strip().split(' ')))
    return (winning, my_nums)

if __name__ == '__main__':
    with open('day4puzzle1input.txt', 'r') as input_file:
        file = input_file.read()
        lines = file.split('\n')
        cards_lists = list(map(getResultOfLine, lines))
        cards_dict_list = list(map(proccessCard, cards_lists))
        instances = [getQuantityOfCard(cards_dict_list, index) for index in range(len(cards_dict_list))]
        sum = fc.reduce(lambda x,y: x + y, instances)
        print(sum)