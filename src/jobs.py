from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path) as file:
        data_table = csv.DictReader(file, delimiter=",", quotechar='"')
        jobs = []
        for job in data_table:
            jobs.append(job)
        return jobs
