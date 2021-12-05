from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path) as file_csv:
        csv_reader = csv.DictReader(file_csv, delimiter=",", quotechar='"')
        return [line for line in csv_reader]
