from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path, mode="r") as fileRead:
        file = csv.DictReader(fileRead)
        lista = []
        for row in file:
            lista.append(row)

    return lista
