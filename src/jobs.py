import csv
from functools import lru_cache


@lru_cache
def read(path):
    with open(path) as file:
        return [
            row for row in csv.DictReader(file)
        ]
