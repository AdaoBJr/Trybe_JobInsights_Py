from functools import lru_cache
import csv


# https://docs.python.org/pt-br/3/library/csv.html
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
        read_file = csv.DictReader(file)
        header, *data = read_file

    return [header, *data]
