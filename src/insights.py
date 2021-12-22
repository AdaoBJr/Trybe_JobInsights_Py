from src.jobs import read


def get_unique_job_types(path):
    """ Checks all different job types and returns a list of them
    Must call `read`
    Parameters
    ----------
    path : str
        Must be passed to `read`
    Returns
    -------
    list
        List of unique job types

    Verifica todos os diferentes tipos de trabalho e retorna uma lista deles
    Deve chamar `read`
    Parâmetros
    ----------
    caminho: str
        Deve ser passado para `read`
    Devoluções
    -------
    Lista
        Lista de tipos de trabalho exclusivos
    """
    list_job = read(path)
    unique_job_types = set()
    for job in list_job:
        if job["job_type"] != "":
            unique_job_types.add(job["job_type"])
    return unique_job_types


def filter_by_job_type(jobs, job_type):
    """Filters a list of jobs by job_type
    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter
    Returns
    -------
    list
        List of jobs with provided job_type
    """
    """Filtra uma lista de empregos por job_type
    Parâmetros
    ----------
    jobs: list
        Lista de empregos a serem filtrados
    job_type: str
        Tipo de trabalho para o filtro de lista
    Devoluções
    -------
    Lista
        Lista de empregos com job_type fornecido
    """
    list_job_type = []
    for job in jobs:
        if job["job_type"] == job_type:
            list_job_type.append(job)
    return list_job_type


def get_unique_industries(path):
    """Checks all different industries and returns a list of them
    Must call `read`
    Parameters
    ----------
    path : str
        Must be passed to `read`
    Returns
    -------
    list
        List of unique industries
    """
    """Verifica todas as diferentes indústrias e retorna uma lista deles
    Deve chamar de 'ler'
    Parâmetros
    caminho : str
    Deve ser passado para 'ler'
    Retorna
    lista
    Lista de indústrias únicas """
    list_industries = read(path)
    different_industries = set()
    for industry in list_industries:
        if industry["industry"] != "":
            different_industries.add(industry["industry"])
    return different_industries


def filter_by_industry(jobs, industry):
    """Filters a list of jobs by industry
    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter
    Returns
    -------
    list
        List of jobs with provided industry
    """
    """Filtra uma lista de empregos pela indústria
    Parâmetros
    empregos : lista
    Lista de empregos a serem filtrados
    indústria : str
    Indústria para o filtro de lista
    Retorna
    lista
    Lista de empregos com indústria fornecida """
    jobs_by_industry = []
    for industrie in jobs:
        if industrie["industry"] == industry:
            jobs_by_industry.append(industrie)
    return jobs_by_industry


def get_max_salary(path):
    """Get the maximum salary of all jobs
    Must call `read`
    Parameters
    ----------
    path : str
        Must be passed to `read`
    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    """Obter o salário máximo de todos os empregos
    Deve chamar de 'ler'
    Parâmetros
    caminho : str
    Deve ser passado para 'ler'
    Retorna
    int
    O salário máximo pago de todas as oportunidades de trabalho """
    list_salary = read(path)
    maximum_salary = set()
    for salary in list_salary:
        if salary["max_salary"] != "":
            try:
                maximum_salary.add(int(salary["max_salary"]))
            except ValueError:
                print("algo de errado aconteceu")
    return max(maximum_salary)


def get_min_salary(path):
    """Get the minimum salary of all jobs
    Must call `read`
    Parameters
    ----------
    path : str
        Must be passed to `read`
    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    """Obter o salário mínimo de todos os empregos
    Deve chamar de 'ler'
    Parâmetros
    caminho : str
    Deve ser passado para 'ler'
    Retorna
    int
    O salário mínimo pago de todas as oportunidades de trabalho """
    list_salary = read(path)
    minimum_salary = set()
    for salary in list_salary:
        if salary["min_salary"] != "":
            try:
                minimum_salary.add(int(salary["min_salary"]))
            except ValueError:
                print("algo de errado aconteceu")
    return min(minimum_salary)


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
    """
    Cheque se determinado salário está na faixa salarial de determinado trabalh
    Parâmetros
    trabalho : dict
    O trabalho com chaves 'min_salary' e 'max_salary'
    salário : int
    O salário para verificar se combina com a faixa salarial do trabalho
    Retorna
    Bool
    True se o salário está na faixa salarial do trabalho, False de outra forma
    Gera
    ValueError"""
    if (type(salary) != int):
        raise ValueError("`salary` isn't a valid integer")
    if("min_salary" not in job or "max_salary" not in job):
        raise ValueError("min_salary or max_salary doesn't exists")
    if (type(job["min_salary"]) != int or type(job["max_salary"]) != int):
        raise ValueError("min_salary or max_salary aren't valid integers")
    if (job["min_salary"]) > job["max_salary"]:
        raise ValueError("min_salary is greather than max_salary")
    return job["min_salary"] <= salary <= job["max_salary"]


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
    """Filtra uma lista de empregos por faixa salarial
    Parâmetros
    empregos : lista
    Os trabalhos a serem filtrados
    salário : int
    O salário a ser usado como filtro
    Retorna
    lista Empregos cuja faixa salarial contém 'salário'"""
    salary_range = []
    for salaries in jobs:
        try:
            if matches_salary_range(salaries, salary):
                salary_range.append(salaries)
        except ValueError:
            print("algo de errado aconteceu")
    return salary_range
