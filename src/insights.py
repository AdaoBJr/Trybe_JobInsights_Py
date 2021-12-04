from .jobs import read


def get_unique_job_types(path):
    unic_jobs = set()
    list_of_jobs = read(path)
    for job in list_of_jobs:
        if job['job_type'] != '':
            unic_jobs.add(job['job_type'])
    return unic_jobs


def filter_by_job_type(jobs, job_type):
    filtered_jobs = []
    for job in jobs:
        if job['job_type'] == job_type:
            filtered_jobs.append(job)
    return filtered_jobs


def get_unique_industries(path):
    unic_industries = set()
    list_of_jobs = read(path)
    for job in list_of_jobs:
        if job['industry'] != '':
            unic_industries.add(job['industry'])
    return unic_industries


def filter_by_industry(jobs, industry):
    filtered_industries = []
    for job in jobs:
        if job['industry'] == industry:
            filtered_industries.append(job)
    return filtered_industries


def get_max_salary(path):
    salaries = []
    list_of_jobs = read(path)
    for job in list_of_jobs:
        if (job['max_salary'] != 'invalid') and (job['max_salary'] != ''):
            salaries.append(int(job['max_salary']))

    return max(salaries)


def get_min_salary(path):
    salaries = []
    list_of_jobs = read(path)
    for job in list_of_jobs:
        if (job['min_salary'] != 'invalid') and (job['min_salary'] != ''):
            salaries.append(int(job['min_salary']))

    return min(salaries)


def matches_salary_range(job, salary):
    """try:
        if (salary > job['min_salary']) and (salary < job['max_salary']):
            return True
        else:
            return False
        job['min_salary']
        job['max_salary']
    except ValueError:
        if salary > job['max_salary']:
    Checks if a given salary is in the salary range of a given job

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
