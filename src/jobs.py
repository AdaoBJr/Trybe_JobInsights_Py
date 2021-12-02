from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(f"{path}", "r") as fileRead:
        file = csv.reader(fileRead, delimiter=",", quotechar='""')
        header, *data = file

    print(header)

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
    return []
