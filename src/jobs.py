from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path) as file:
        data_python = csv.reader(file)
        header, *data = data_python
    list = []
    for item in data:
        list.append(trans_dict(item, header))
    return list


def trans_dict(item, header):
    result = {header[idx]: itm for idx, itm in enumerate(item)}
    return result
