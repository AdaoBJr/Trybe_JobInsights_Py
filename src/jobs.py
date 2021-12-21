from functools import lru_cache
import csv
# Lê um arquivo de um determinado caminho e retorna seu conteúdo
# Parâmetros
# caminho : str
# Caminho completo para arquivar
# Retorna
#  lista
# Lista de linhas como dicts


@lru_cache
def read(path):
    """Reads a file from a given path and returns its contents
    Parameters
    ----------
    path : str
        Full path to file

    Returns
    -------
    list
        List of rows as dicts
    """
    with open(path) as file:
        path_file = csv.DictReader(file)
        list = []
        for row in path_file:
            list.append(row)

    return list
