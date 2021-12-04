from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path) as file:
        job_description = csv.reader(file, delimiter=",", quotechar='"')
        header, *data = job_description
        jobs = []
        for job in data:
            job_description = {}
            for idx, field in enumerate(header):
                job_description[field] = job[idx]
            jobs.append(job_description)
    return [jobs]
