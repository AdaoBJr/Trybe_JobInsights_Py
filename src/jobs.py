from functools import lru_cache
import csv


@lru_cache
def read(path):
    jobs_dict = []
    with open(path) as file:
        jobs_reader = csv.DictReader(file)
        for dict in jobs_reader:
            jobs_dict.append(dict)
        return jobs_dict