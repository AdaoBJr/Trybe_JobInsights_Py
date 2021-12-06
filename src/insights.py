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
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    pass


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []
