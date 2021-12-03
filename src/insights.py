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
    jobs_result = []

    for item in jobs:
        if item['industry'] == industry:
            jobs_result.append(item)
    return jobs_result


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
    if not('min_salary' in job.keys()):
        raise ValueError('min key not contain in jobs')

    if not('max_salary' in job.keys()):
        raise ValueError('max key not contain in jobs')

    if not(isinstance(job['min_salary'], int)):
        raise ValueError('min is not a integer')

    if not(isinstance(job['max_salary'], int)):
        raise ValueError('max is not a integer')

    if job['min_salary'] > job['max_salary']:
        raise ValueError('min value is greather than max value')

    if type(salary) != int:
        raise ValueError('salary is not a integer')

    if not(salary in range(int(job['min_salary']), int(job['max_salary']))):
        return False

    return True


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
