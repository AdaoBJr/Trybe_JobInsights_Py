from functools import lru_cache
import csv


@lru_cache
def read(file_path):
    jobs = []
    with open(file_path) as file:
        jobs_reader = csv.DictReader(file, delimiter=",", quotechar='"')
        for job in jobs_reader:
            jobs.append(job)

    return jobs
