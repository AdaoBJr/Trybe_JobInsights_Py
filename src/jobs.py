from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path, mode='r') as csv_file:
        csv_list = list(csv.DictReader(csv_file, delimiter=','))
    return csv_list
