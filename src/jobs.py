from functools import lru_cache
import csv


@lru_cache
def read(path):
    jobs = []
    with open(path, mode="r") as jobs_file:
        files_list = csv.DictReader(jobs_file)
        for f in files_list:
            jobs.append(f)
    return jobs
