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

    jobs_dict_list = []

    with open(path) as file:
        jobs_reader = csv.DictReader(file, delimiter=",", quotechar='"')
        for row in jobs_reader:
            jobs_dict_list.append(row)
    return jobs_dict_list


if __name__ == '__main__':
    teste = read('src/jobs.csv')
    print(teste[3])
