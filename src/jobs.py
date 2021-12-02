from functools import lru_cache
import csv


@lru_cache
def read(path):
    result = []
    with open(path, mode='r') as file:
        reader = csv.DictReader(file)
        for line in reader:
            result.append(line)
    return(result)
