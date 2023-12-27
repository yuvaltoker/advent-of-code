from typing import List, Dict, Tuple

def getNextId(table: List[List], cur_id: int) -> int:
    for row in table:
        if row[1] <= cur_id <= row[1] + row[2] - 1:
            return row[0] + (cur_id - row[1])
    return cur_id

# returns 'done' when finished
def getNextSubject(cur_subject: str) -> str:
    match cur_subject:
        case 'seed-to-soil map':
            return 'soil-to-fertilizer map'
        case 'soil-to-fertilizer map':
            return 'fertilizer-to-water map'
        case 'fertilizer-to-water map':
            return 'water-to-light map'
        case 'water-to-light map':
            return 'light-to-temperature map'
        case 'light-to-temperature map':
            return 'temperature-to-humidity map'
        case 'temperature-to-humidity map':
            return 'humidity-to-location map'
        case 'humidity-to-location map':
            return 'done'

def findNextId(tables_dict: Dict, cur_id: int, cur_subject: str) -> int:
    next_id = getNextId(tables_dict[cur_subject], cur_id)
    next_subject = getNextSubject(cur_subject)

    if next_subject == 'done':
        return next_id
    return findNextId(tables_dict, next_id, next_subject)


def getLocation(tables_dict: Dict, seed: int) -> int:
    return findNextId(tables_dict, seed, 'seed-to-soil map')

def getContent(table: str) -> Tuple:
    # example of table: 'seed-to-soil map:\n50 98 2\n52 50 48'
    table_name = table.split(':')[0]
    table_content = [[int(id) for id in part.strip().split(' ')] for part in table.split(':')[1].strip().split('\n')]

    return (table_name, table_content)

def mappingTables(tables: List) -> Dict:
    tables_dict = {}
    content = list(map(getContent, tables))
    for (subject, table) in content:
        tables_dict[subject] = table
    # fixing the seeds list of lists, where there is only on list in there
    tables_dict['seeds'] = tables_dict['seeds'][0]

    return tables_dict

def getMinLocationOfDuo(tables_dict: Dict, seed: int, seeds_range: int) -> int:
    min_loc = float('inf')
    for seed_No in range(seed, seed + seeds_range):
        min_loc = min(min_loc, getLocation(tables_dict, seed_No))
    return min_loc

if __name__ == '__main__':
    with open('day5puzzle1input.txt', 'r') as input_file:
        file = input_file.read()
        # split the file into tables
        tables = file.split('\n\n')
        # mapping the tables into dictionary
        tables_dict = mappingTables(tables)
        min_loc = min([getMinLocationOfDuo(tables_dict, seed, seeds_range) for seed, seeds_range in zip(tables_dict['seeds'][0::2], tables_dict['seeds'][1::2])])
        print(min_loc)