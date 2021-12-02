from functools import lru_cache
import csv


@lru_cache
def read(path):
    auxDict = []
    with open(path) as file:
        reader_jobs = csv.DictReader(file)
        for info in reader_jobs:
            auxDict.append(info)
    return auxDict
