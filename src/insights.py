from src.jobs import read


def get_unique_job_types(path):
    data = read(path)
    # creates a set object
    unique_job_types = set()

    for job in data:
        unique_job_types.add(job["job_type"])

    return unique_job_types


def filter_by_job_type(jobs, job_type):
    job_types_list = []

    for job in jobs:
        if (job["job_type"] == job_type):
            job_types_list.append(job)

    return job_types_list


def get_unique_industries(path):
    data = read(path)
    unique_industries = set()

    for industry in data:
        # bool() returns true if a variable isn't empty
        if (bool(industry["industry"])):
            unique_industries.add(industry["industry"])

    return unique_industries


def filter_by_industry(jobs, industry):
    industry_list = []

    for job in jobs:
        if (job["industry"] == industry):
            industry_list.append(job)

    return industry_list


def get_max_salary(path):
    data = read(path)
    max_salary = 0

    for salary in data:
        # isnumreci() source: shorturl.at/alAGJ
        if (salary["max_salary"].isnumeric()
                # int() source: shorturl.at/djmA9
                and int(salary["max_salary"]) > max_salary):
            max_salary = int(salary["max_salary"])

    return max_salary


def get_min_salary(path):
    data = read(path)
    min_salary = 9999999999999999999

    for salary in data:
        if (salary["min_salary"].isnumeric()
                and int(salary["min_salary"]) < min_salary):
            min_salary = int(salary["min_salary"])

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
