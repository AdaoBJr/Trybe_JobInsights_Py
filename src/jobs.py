from functools import lru_cache
import csv


@lru_cache
def read(path):
    headers = []
    with open(path, mode="r") as file:
        header_of_jobs = csv.DictReader(file)
        for row in header_of_jobs:
            headers.append(row)
    return headers
