from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path) as csv_file:
        csv_list = csv.DictReader(csv_file)
        return list(csv_list)
