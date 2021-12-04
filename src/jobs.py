from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path, "r") as jobs_file:
        jobs_csv = csv.DictReader(jobs_file, delimiter=",")
        lines = []
        for line in jobs_csv:
            lines.append(line)
        return lines
