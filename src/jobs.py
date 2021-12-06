from functools import lru_cache
import csv


# https://docs.python.org/pt-br/3/library/csv.html
# https://app.betrybe.com/course/computer-science/introducao-a-python/entrada-e-saida-de-dados/105dc022-72fa-425f-a452-29b3595bb64d/conteudos/9a69f5d2-dd9d-4831-bea0-bb2f7251cc3b/manipulando-arquivos-csv/acbfc282-4ea3-4391-aa85-77f9784efdd2?use_case=side_bar
@lru_cache
def read(path):
    with open(path) as file:
        dados = csv.DictReader(file)
        header, *data = dados
        return [header, *data]
