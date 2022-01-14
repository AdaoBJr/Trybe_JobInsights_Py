from functools import lru_cache
import csv


@lru_cache
def read(path):
    jobs_data = []
    with open(path) as file:
        jobs_items = csv.DictReader(file, delimiter=",", quotechar='"')
        jobs_data = list(jobs_items)

    return jobs_data
