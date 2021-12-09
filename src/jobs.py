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
    with open(path, 'r', errors='ignore') as file:
        content = csv.DictReader(file, delimiter=",", quotechar='"')
        contentlist = [row for row in content]
    return contentlist


if __name__ == "__main__":
    read('src/jobs.csv')
