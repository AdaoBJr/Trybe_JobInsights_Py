from src.jobs import read


def get_unique_job_types(path):
    # Usando a func read criada no jobs
    file = read(path)
    # criando um array de elementos unicos
    jobs = set()
    # percorrendo o array e add ao Jobs tds os "job_types"
    for item in file:
        jobs.add(item["job_type"])
    # retornando jobs
    return jobs


def filter_by_job_type(jobs, job_type):
    # criando array de jobs
    job_list = []
    # percorrendo o array
    for job in jobs:
        # testando se o job_type recebido consta na lista de jobs
        if job_type == job["job_type"]:
            # add o Job do for na list de jobs
            job_list.append(job)
    return job_list


def get_unique_industries(path):
    # Usando a func read criada no jobs
    file = read(path)
    # criando um array de elementos unicos
    industries = set()
    # percorrendo o array e add ao industries tds os "indistry"
    for item in file:
        # testando se está vazio
        if item["industry"] != "":
            industries.add(item["industry"])
    # retornando industries
    return industries
    return []


def filter_by_industry(jobs, industry):
    # criando array de jobs
    job_list = []
    # percorrendo o array
    for job in jobs:
        # testando se a industry recebido consta na lista de jobs
        if industry == job["industry"]:
            # add o Job do for na list de jobs
            job_list.append(job)
    return job_list


def get_max_salary(path):
    # Usando a func read criada no jobs
    file = read(path)
    # criando variavel max salary
    max_salary = 0
    # percorrendo o array e testando se o valor de
    # item["max_salary"] é numerico e se é maior que que max_salary
    for item in file:
        if (
            item["max_salary"].isnumeric()
            and int(item["max_salary"]) > max_salary
        ):
            max_salary = int(item["max_salary"])
    return max_salary


def get_min_salary(path):
    # Usando a func read criada no jobs
    file = read(path)
    # criando variavel min salary com valor muito alto
    min_salary = 9999999999999
    # percorrendo o array e testando se o valor de
    # item["min_salary"] é numerico e se é menor que que min_salary
    for item in file:
        if (
            item["min_salary"].isnumeric()
            and int(item["min_salary"]) < min_salary
        ):
            min_salary = int(item["min_salary"])
    return min_salary


def matches_salary_range(job, salary):
    if (
        # testa se Jobs tem a chave "min_salary"
        "min_salary" not in job
        # testa se Jobs tem a chave "max_salary"
        or "max_salary" not in job
        # testa se max_salary e min_salary e salary saão inteiros
        or type(job["min_salary"]) != int
        or type(job["max_salary"]) != int
        or type(salary) != int
        # testa se min_salary é menor que max_salary
        or job["min_salary"] > job["max_salary"]
    ):
        # se algum dos tests acima der true, aparece o erro
        raise ValueError
        # retorna true pois o salario está dentro da faixa
    return job["min_salary"] <= salary <= job["max_salary"]


def filter_by_salary_range(jobs, salary):
    # cria array de filtered_salar
    filtered_salary = []
    # percorre o array jobs
    for job in jobs:
        try:
            # testa se o salario está no range
            if matches_salary_range(job, salary):
                filtered_salary.append(job)
        # levanta o erro
        except ValueError:
            pass
    return filtered_salary
