from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path) as file:
        job_insights_reader = csv.DictReader(
            file, delimiter=",", quotechar='"')
        job_insights = []
        for rows in job_insights_reader:
            job_insights.append(rows)
    return job_insights
