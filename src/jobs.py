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
    response = []
    with open(path, 'r') as file:
        jobs_reader = csv.reader(file, delimiter=",", quotechar='"')
        header, *data = jobs_reader
        for entry in data:
            job = {}
            for i in range(0, len(header)):
                job[header[i]] = entry[i]
            response.append(job)
    return response
