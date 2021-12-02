from functools import lru_cache
import csv


@lru_cache
def read(path):
    dict_jobs = []
    with open(path) as file:
        reader_jobs = csv.DictReader(file)
        for dict in reader_jobs:
            dict_jobs.append(dict)
        return dict_jobs
