from src.jobs import read

# from jobs import read


def get_unique_job_types(path):
    """Checks all different job types and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """

    list_jobs = read(path)
    list_types_jobs = set()  # cria a várial como um conjunto
    # list_types_jobs = []

    for job in list_jobs:
        list_types_jobs.add(job["job_type"])

    return list_types_jobs


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

    # compreensão de listas
    filter_list = [job for job in jobs if job["job_type"] == job_type]

    return filter_list


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
    list_jobs = read(path)
    list_types_industries = set()  # cria a várial como um conjunto
    # list_types_jobs = []

    for job in list_jobs:
        if job["industry"] != "":
            list_types_industries.add(job["industry"])

    return list_types_industries


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

    filter_list = [job for job in jobs if job["industry"] == industry]

    return filter_list


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
    list_jobs = read(path)
    list_salaries = []  # cria a várial como um conjunto
    # list_types_jobs = []

    for job in list_jobs:
        if job["max_salary"] != "" and job["max_salary"] != "invalid":
            list_salaries.append(int(job["max_salary"]))

    return max(list_salaries)


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
    list_jobs = read(path)
    list_salaries = []  # cria a várial como um conjunto
    # list_types_jobs = []

    for job in list_jobs:
        if job["min_salary"] != "" and job["min_salary"] != "invalid":
            list_salaries.append(int(job["min_salary"]))

    return min(list_salaries)


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
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError
    elif type(job["min_salary"]) != int or type(job["max_salary"]) != int:
        raise ValueError
    elif job["min_salary"] > job["max_salary"] or type(salary) != int:
        raise ValueError
    else:
        return (
            True if job["min_salary"] <= salary <= job["max_salary"] else False
        )


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
    list_salary = []

    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                list_salary.append(job)
        except ValueError:
            ValueError

    return list_salary
