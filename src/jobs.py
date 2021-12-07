from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path, "r") as file:
        reader = csv.DictReader(file, delimiter=',')
        lines = []
        for line in reader:
            lines.append(line)

    print(lines)
    return lines
