from csv import DictReader
from functools import lru_cache


@lru_cache
def read(path):
    with open(path, mode="r") as jobs_file:
        return list(DictReader(jobs_file))
