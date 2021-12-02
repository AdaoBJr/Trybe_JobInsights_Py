from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path) as file:
        data = csv.DictReader(file)
        lista = []
        for row in data:
            lista.append(row)
    return lista
