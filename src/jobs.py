from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path) as file:
        list = csv.DictReader(file)
        header, *data = list
        return [header, *data]
