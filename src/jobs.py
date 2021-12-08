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
        jobs_status_reader = csv.DictReader(file, delimiter=',', quotechar='"')
        list_rows = []
        for row in jobs_status_reader:
            list_rows.append(row)
        print(list_rows[0])
        return list_rows
