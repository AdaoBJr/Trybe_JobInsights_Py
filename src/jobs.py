from functools import lru_cache

import csv


@lru_cache
def read(path):
    jobsList=[]
    with open(path, 'r') as file:
        jobs = csv.DictReader(file)
        jobsList = list(jobs)
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
    return jobsList
