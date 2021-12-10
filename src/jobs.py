from functools import lru_cache
import csv


@lru_cache
def read(path):
    final_list = []

    with open(path) as csv_file:
        csv_data = csv.DictReader(csv_file)
        for line in csv_data:
            final_list.append(line)

    return final_list
