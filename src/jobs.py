from functools import lru_cache
import csv


@lru_cache
def read(path):
    jobs = []
    with open(path) as file:
        jobs_reade = csv.DictReader(file)
        for job in jobs_reade:
            jobs.append(job)

    return jobs


if __name__ == "__main__":
    print(read("src/jobs.csv"))

# https://docs.python.org/3/library/csv.html
