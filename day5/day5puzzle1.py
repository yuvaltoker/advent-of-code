from typing import List, Dict

def getLocation(tables_dict: Dict, seed: int) -> int:
    ...

def mappingTables(tables: List) -> Dict:
    ...

if __name__ == '__main__':
    with open('sample.txt', 'r') as input_file:
        file = input_file.read()
        # split the file into tables
        tables = file.split('\n\n')
        # mapping the tables into dictionary
        tables_dict = mappingTables(tables)
        
        for seed in tables_dict['seeds']:
            seed_loc = getLocation(tables_dict, seed)

        print(tables)