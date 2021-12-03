import csv
from functools import lru_cache


@lru_cache
def read(path):
    # """Reads a file from a given path and returns its contents

    # Parameters
    # ----------
    # path : str
    #     Full path to file

    # Returns
    # -------
    # list
    #     List of rows as dicts
    # """
    with open(path) as file:
        dictionary = []
        list = csv.DictReader(file, delimiter=',', quotechar='"')
        for rows in list:
            dictionary.append(rows)
        return dictionary
