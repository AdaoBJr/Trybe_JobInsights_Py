import csv
from functools import lru_cache


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
    # Source: https://app.betrybe.com/course/computer-science
    # /introducao-a-python/entrada-e-saida-de-dados/105dc022-
    # 72fa-425f-a452-29b3595bb64d/conteudos/9a69f5d2-dd9d-483
    # 1-bea0-bb2f7251cc3b/manipulando-arquivos-csv/acbfc282-4
    # ea3-4391-aa85-77f9784efdd2?use_case=side_bar
    with open(path) as file:
        content = csv.reader(file, delimiter=",", quotechar='"')
        header, *data = content

    jobs_list = []
    for row in data:
        jobs_dict = {}
        # Source: https://www.educative.io/edpresso/how-to-get-th
        # e-length-of-a-list-in-python?utm_term=&utm_campaign=%5B
        # Test%5D+Dynamic+Verticals&utm_source=adwords&utm_medium
        # =ppc&hsa_acc=5451446008&hsa_cam=14045073269&hsa_grp=128
        # 822123241&hsa_ad=535845844735&hsa_src=g&hsa_tgt=dsa-139
        # 4252596758&hsa_kw=&hsa_mt=&hsa_net=adwords&hsa_ver=3
        # Source: https://app.betrybe.com/course/computer-science
        # /introducao-a-python/aprendendo-python/9c4e1d64-303d-49
        # 2d-82a4-998b2c0218b9/conteudos/217980af-0946-4b04-9cc4-
        # 5846af26ec27/tipos-de-dados-embutidos/bea4b2ef-aece-43f
        # e-9d9d-fa7d8c183088?use_case=side_bar
        for index in range(0, len(row)):
            jobs_dict[header[index]] = row[index]
        jobs_list.append(jobs_dict)

    return jobs_list


if __name__ == "__main__":
    read("src/jobs.csv")
