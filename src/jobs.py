from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path) as file:
        file_jobs = csv.DictReader(file)
        jobs = [row for row in file_jobs]

    return jobs
