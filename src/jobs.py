from functools import lru_cache
import csv


# https://docs.python.org/pt-br/3/library/csv.html
@lru_cache
def read(path):
    with open(path) as file:
        read_file = csv.DictReader(file)
        header, *data = read_file

    return [header, *data]
