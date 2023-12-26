from typing import List, Dict

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
            seed_loc = getLocation()
        print(tables)