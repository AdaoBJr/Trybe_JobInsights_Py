from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path, 'r') as arquivo:
        arquivo_csv = csv.reader(arquivo, delimiter=',')
        array = []
        for linha in arquivo_csv:
            array.append(linha)
        return array


# if __name__ == '__main__':
#     print(read('src/jobs.csv'))
