import src.jobs


def get_unique_job_types(path):
    jobs_data = src.jobs.read(path)
    response = []
    for entry in jobs_data:
        job_type = entry['job_type']
        if job_type not in response:
            response.append(job_type)
    return response


def filter_by_job_type(jobs, job_type):
    response = []
    for entry in jobs:
        if job_type == entry['job_type']:
            response.append(entry)
    return response


def get_unique_industries(path):
    jobs_data = src.jobs.read(path)
    response = []
    for entry in jobs_data:
        industry = entry['industry']
        if industry != '' and industry not in response:
            response.append(industry)
    return response


def filter_by_industry(jobs, industry):
    response = []
    for entry in jobs:
        if industry == entry['industry']:
            response.append(entry)
    return response


def get_max_salary(path):
    jobs_data = src.jobs.read(path)
    response = 0
    for entry in jobs_data:
        salary = entry['max_salary']
        if salary.isnumeric() and int(salary) > response:
            response = int(salary)
    return response


def get_min_salary(path):
    jobs_data = src.jobs.read(path)
    response = 100000
    for entry in jobs_data:
        salary = entry['min_salary']
        if salary.isnumeric() and int(salary) < response:
            response = int(salary)
    return response


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

