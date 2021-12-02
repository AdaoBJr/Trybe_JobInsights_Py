from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path) as jobs_file:
        jobs_content = csv.DictReader(jobs_file, delimiter=",", quotechar='"')
        result = []
        for row in jobs_content:
            result.append(row)

    return result
