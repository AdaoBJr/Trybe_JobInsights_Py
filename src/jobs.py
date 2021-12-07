from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path) as file:
        file_jobs = csv.DictReader(file, delimiter=",", quotechar='"')
        jobs = [line for line in file_jobs]

    return jobs
