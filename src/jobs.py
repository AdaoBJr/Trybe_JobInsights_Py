from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path) as file:
        return [
            {key: value for key, value in row.items()}
            for row in csv.DictReader(file)
        ]
