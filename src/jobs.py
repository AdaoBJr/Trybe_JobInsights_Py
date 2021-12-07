from functools import lru_cache
import csv


@lru_cache
def read(path):
    lista = []
    with open(path) as file:
        data = csv.DictReader(file)
        for d in data:
            lista.append(d)

    return lista
