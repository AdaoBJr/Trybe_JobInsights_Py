from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path) as file:
        jobs_reader = csv.DictReader(file, delimiter=",", quotechar='"')
        header, *data = jobs_reader
    return [header, *data]
