from functools import lru_cache

import csv


@lru_cache
def read(path):
    """https://acervolima.com/usando-o-modulo-csv-para-ler-os-dados-no-pandas/
    """
    with open(path) as file_csv:
        return list(csv.DictReader(file_csv))
        """vai abrir o arquivo do path
        e retorna a lista de dicionarios
        """


read("src/jobs.csv")
