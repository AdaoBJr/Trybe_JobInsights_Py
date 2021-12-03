from src.jobs import read


# print(get_unique_industries("src/jobs.csv"))


def get_unique_job_types(path):
    auxJobs = read(path)
    job_type = set()
    for i in auxJobs:
        job_type.add(i['job_type'])
    return job_type


def filter_by_job_type(jobs, job_type):
    aux = []

    for item in jobs:
        if job_type in item.values():
            aux.append(item)

    return aux


def get_unique_industries(path):
    auxJobs = read(path)
    job_type = set()
    for i in auxJobs:
        if i['industry'] != '':
            job_type.add(i['industry'])
    return job_type


def filter_by_industry(jobs, industry):
    aux = []

    for item in jobs:
        if industry in item.values():
            aux.append(item)

    return aux


def get_max_salary(path):
    auxJobs = read(path)
    maior = 0
    for item in auxJobs:
        if item['max_salary'].isnumeric():
            aux = int(item['max_salary'])
            if aux >= maior:
                maior = aux
    return maior


def get_min_salary(path):
    auxJobs = read(path)
    menor = 99999999999999999999
    for item in auxJobs:
        if item['min_salary'].isnumeric():
            aux = int(item['min_salary'])
            if aux <= menor:
                menor = aux
    return menor


def matches_salary_range(job, salary):
    """Checks if a given salary is in the salary range of a given job

    Parametersd
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
