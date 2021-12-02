import csv
from functools import lru_cache


@lru_cache
def read(path):
    with open(path) as file:
        jobs = csv.DictReader(file, delimiter=",", quotechar='"')
        return [job for job in jobs]
