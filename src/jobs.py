from functools import lru_cache
import csv


@lru_cache
def read(path):
    try:
        with open(path) as jobs:
            content = csv.DictReader(jobs, delimiter=',', quotechar='"')
            return [item for item in content]

    except FileNotFoundError:
        raise Exception("File not found")
