from functools import lru_cache
import csv


path = "src/jobs.csv"


@lru_cache
def read(path):
    with open(path) as file:
        teste = csv.DictReader(file)
        lista = []
        for index in teste:
            lista.append(index)
        return lista
