from src.jobs import read


def get_unique_job_types(path):
    list = read(path)
    jobs = set()  # set of unique job types
    for job in list:
        jobs.add(job["job_type"])
    return jobs


def filter_by_job_type(jobs, job_type):
    list = []
    for job in jobs:
        if job["job_type"] == job_type:
            list.append(job)
    return list


def get_unique_industries(path):
    list = read(path)
    industries = set()  # set of unique industries
    for industry in list:
        if industry["industry"]:
            industries.add(industry["industry"])
    return industries


def filter_by_industry(jobs, industry):
    list = []
    for job in jobs:
        if job["industry"] == industry:
            list.append(job)
    return list


def get_max_salary(path):
    list = read(path)
    max_salary = 0
    for job in list:
        if (
            job[
                "max_salary"
            ].isnumeric()  # https://docs.python.org/3/library/stdtypes.html#str.isnumeric
            and int(job["max_salary"]) > max_salary
        ):
            max_salary = int(job["max_salary"])
    return max_salary


def get_min_salary(path):
    list = read(path)
    min_salary = 9999999999
    for job in list:
        if (
            job[
                "min_salary"
            ].isnumeric()  # https://docs.python.org/3/library/stdtypes.html#str.isnumeric
            and int(job["min_salary"]) < min_salary
        ):
            min_salary = int(job["min_salary"])
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
