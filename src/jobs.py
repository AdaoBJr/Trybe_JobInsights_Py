from functools import lru_cache
import csv


@lru_cache
def read(path):
    """Reads a file from a given path and returns its contents

    Parameters
    ----------
    path : str
        Full path to file

    Returns
    -------
    list
        List of rows as dicts
    """
    with open(path) as file:
        csv_file = csv.DictReader(file, delimiter=",", quotechar='"')
        jobs = []
        for job in list(csv_file):
            jobs.append(job)
        return jobs


read("jobs.csv")
