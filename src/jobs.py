from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path) as file:
        return [index for index in csv.DictReader(file)]
