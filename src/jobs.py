from functools import lru_cache
import csv

@lru_cache
def read(path):
    with open(path, encoding='utf-8') as file:
       data = []
       csvReader = csv.DictReader(file)
       for row in csvReader:
        data.append(row)
    
    return data