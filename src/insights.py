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
    if 'min_salary' not in job or 'max_salary' not in job:
        raise ValueError
    if not isinstance(salary, int) or not isinstance(job['min_salary'], int):
        raise ValueError
    if not isinstance(job['max_salary'], int):
        raise ValueError
    if job['min_salary'] > job['max_salary']:
        raise ValueError
    if job['min_salary'] <= salary <= job['max_salary']:
        return True
    else:
        return False


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

