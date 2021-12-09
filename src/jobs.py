import csv

from functools import lru_cache


@lru_cache
def read(path):
    with open(path) as file:
        return [key for key in csv.DictReader(file)]
