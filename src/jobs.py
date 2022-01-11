from functools import lru_cache
from csv import DictReader


@lru_cache
def read(path):
    with open(path, mode="r") as jobs:
        return list(DictReader(jobs))  # list() returns a list
