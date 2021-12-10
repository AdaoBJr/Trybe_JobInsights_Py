from csv import DictReader
from functools import lru_cache


@lru_cache
def read(path):
    with open(path) as file:
        return list(DictReader(file))


if __name__ == '__main__':
    read('/jobs.csv')
