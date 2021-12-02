from functools import lru_cache
import csv


@lru_cache
def read(path):
    jobs_dict = []
    with open(path) as file:
        reader = csv.DictReader(file)
        for job in reader:
            jobs_dict.append(job)
        return jobs_dict
