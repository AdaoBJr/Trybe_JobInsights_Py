from src.jobs import read


def get_unique_job_types(path):
    lista = read(path)
    unique_list = []
    for item in lista:
        if item["job_type"] not in unique_list:
            unique_list.append(item["job_type"])

    return unique_list


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
    list_filtered = [job for job in jobs if job["job_type"] is job_type]
    return list_filtered


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
    lista = read(path)
    unique_list = []
    for item in lista:
        i = item["industry"]
        if i not in unique_list and i != "":
            unique_list.append(i)

    return unique_list


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
    list_filtered = [ind for ind in jobs if ind["industry"] is industry]
    return list_filtered


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
    lista = read(path)
    # set é um tipo de conjunto não ordenada e imutável. {'banana', 'maçã',...}
    maximum_salary = set()
    for item in lista:
        # O mpetodo isnumeric() retorna True se todos os caracteres da string
        # forem numéricos (0-9), caso contrário, False.
        # link: https://www.w3schools.com/python/ref_string_isnumeric.asp
        if item["max_salary"].isnumeric():
            maximum_salary.add(int(item["max_salary"]))
    # A funcção max() retorna o item com o valor mais alto em um iterável.
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
    lista = read(path)
    minimum_salary = set()
    for item in lista:
        if item["min_salary"].isnumeric():
            minimum_salary.add(int(item["min_salary"]))
    # A funcção min() retorna o item com o valor mais baixo em um iterável.
    return min(minimum_salary)


def verify_job_salary(job, salary):
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError("Invalid input")
    elif type(salary) != int:
        raise ValueError("Invalid input")
    elif type(job["min_salary"]) != int or type(job["max_salary"]) != int:
        raise ValueError("Invalid input")
    elif job["min_salary"] > job["max_salary"]:
        raise ValueError("Invalid input")


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
    verify_job_salary(job, salary)

    if job["min_salary"] <= salary <= job["max_salary"]:
        return True
    else:
        return False


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range(GO)
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
    my_jobs = []
    for job in jobs:
        if (
            type(salary) == int
            and type(job["min_salary"]) == int
            and type(job["max_salary"]) == int
        ):
            if (
                job["min_salary"] != ""
                and job["max_salary"] != ""
                and salary != ""
                and job["min_salary"] < job["max_salary"]
                and job["min_salary"] <= salary <= job["max_salary"]
            ):
                my_jobs.append(job)

    return my_jobs
