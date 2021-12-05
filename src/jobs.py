from functools import lru_cache
import csv


@lru_cache
def read(path):
    jobs = []
    with open(path) as file:
        jobs_read = csv.DictReader(file)
        for job in jobs_read:
            jobs.append(job)

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
    return jobs