from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path) as csvFile:
        csvParsed = csv.reader(csvFile, delimiter=",")
        header, *data = csvParsed
        dictionaries = getDictsFromCsv(header, data)
        return dictionaries


def getDictsFromCsv(header, data):
    elements = []

    for rows in data:
        dictionarie = {}

        for idx, column in enumerate(header):
            dictionarie[column] = rows[idx]

        elements.append(dictionarie)

    return elements
