from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path, 'r') as file:
        content = csv.DictReader(file, delimiter=',')
        content_list = []
        for row in content:
            content_list.append(row)
        return content_list
