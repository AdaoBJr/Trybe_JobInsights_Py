from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open("jobs.csv") as jobs_file:
        jobs_list = csv.DictReader(jobs_file)
        print(jobs_list)
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
    return []
