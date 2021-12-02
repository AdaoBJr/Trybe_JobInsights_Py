from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path, 'r') as arquivo:
        arquivo_csv = csv.reader(arquivo, delimiter=',')
        for linha in arquivo_csv:
            return linha
