from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path) as file:
        csv_file = csv.DictReader(file, delimiter=",", quotechar='"')
        jobs = []
        for job in csv_file:
            jobs.append(job)
        return jobs
