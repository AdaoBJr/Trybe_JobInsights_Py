from functools import lru_cache
import csv


@lru_cache
def read(path):
    list_dict = []
    with open(path) as file:
        read_file = csv.DictReader(file, delimiter=",", quotechar='"')
        for item in read_file:
            list_dict.append(item)
    return list_dict
