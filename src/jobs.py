from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path) as job_file:
        return list(csv.DictReader(job_file))


read("src/jobs.csv")
