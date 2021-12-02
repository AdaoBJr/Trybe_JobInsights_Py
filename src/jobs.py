from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path, 'r') as file:
        content = csv.reader(file, delimiter=',')
        content_list = []
        for row in content:
            content_list.append(dict(row))
        return content_list
