from src.jobs import read


def get_unique_job_types(path):
    array_of_jobs = read(path)
    job_types = set()

    for item in array_of_jobs:
        job_types.add(item['job_type'])
    return job_types


def filter_by_job_type(jobs, job_type):
    jobs_result = []

    for item in jobs:
        if item['job_type'] == job_type:
            jobs_result.append(item)

    return jobs_result


def get_unique_industries(path):
    array_of_jobs = read(path)
    industries = set()

    for item in array_of_jobs:
        if item['industry']:
            industries.add(item['industry'])
    return industries


def filter_by_industry(jobs, industry):
    print(industry)
    # jobs_result = []

    # for item in jobs:
    #     if item['industry'] == industry:
    #         jobs_result.append(item)

    # return jobs_result
    return []

def get_max_salary(path):
    array_of_jobs = read(path)
    salaries = []

    for item in array_of_jobs:
        if item['max_salary'].isnumeric():
            salaries.append(int(item['max_salary']))
    return (max(salaries))


def get_min_salary(path):
    array_of_jobs = read(path)
    salaries = []

    for item in array_of_jobs:
        if item['min_salary'].isnumeric():
            salaries.append(int(item['min_salary']))
    return (min(salaries))


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
