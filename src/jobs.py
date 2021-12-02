from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path) as file:
        read_file = csv.DictReader(file)
        list_job = []
        for new_job in read_file:
            list_job.append(new_job)
    return list_job

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
