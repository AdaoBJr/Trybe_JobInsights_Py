from src.jobs import read


def get_unique_job_types(path):
    all_jobs = read(path)
    """Inicializando um conjunto com set()"""
    jobs = set()
    for job in all_jobs:
        jobs.add(job["job_type"])
    return jobs
    """
    faz um for em todos os  all_jobs e adiciona ao conjunto jobs
    todos os tipos de empregos(coluna job_types)
    """


def filter_by_job_type(jobs, job_type):
    job_filtered = [
        job for job in jobs
        if job["job_type"] == job_type
        ]
    return job_filtered


def get_unique_industries(path):
    all_jobs = read(path)
    jobs = set()
    for job in all_jobs:
        if job["industry"]:
            jobs.add(job["industry"])
    return jobs


def filter_by_industry(jobs, industry):
    """Cria uma lista e dentro dela ja faõ o for e filtro se o job
    é igual a industry
    """
    industry_filtered = [
        job for job in jobs
        if job["industry"] == industry
        ]
    return industry_filtered


def get_max_salary(path):
    all_jobs = read(path)
    max_salaries = set()
    for job in all_jobs:
        if(job["max_salary"] != '' and job["max_salary"].isnumeric()):
            max_salaries.add(int(job["max_salary"]))

    return max(max_salaries)


def get_min_salary(path):
    all_jobs = read(path)
    min_salaries = set()
    for job in all_jobs:
        if(job["min_salary"] != '' and job["min_salary"].isnumeric()):
            min_salaries.add(int(job["min_salary"]))

    return min(min_salaries)


def matches_salary_range(job, salary):
    """ if(
        type(salary) != int:
            raise ValueError("Salary deve ser um inteiro")
        or job["min_salary"] > job["max_salary"]:
            raise ValueError("Salario minimo deve ser menor
            que salario máximo")

    ):
    return job["min_salary"] <= salary <= job["max_salary"] """

    """ Requisito refatorado com ajuda do Renato Graça e Eder Paiva """
    try:
        if type(salary) != int:
            raise ValueError("Salary deve ser um inteiro")
        if job["min_salary"] > job["max_salary"]:
            raise ValueError("Salario min deve ser menor que salario máx")
        return job["min_salary"] <= salary <= job["max_salary"]
    except Exception:
        raise ValueError("Salary deve ser um inteiro")


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
