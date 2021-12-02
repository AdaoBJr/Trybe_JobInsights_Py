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
    # for key in job:
    #     if type(job[key]) != int or job[key] < 0:
    #         raise ValueError
    # if 'min_salary' not in job or 'max_salary' not in job:
    #     raise ValueError
    # elif job['min_salary'] > job['max_salary']:
    #     raise ValueError
    # elif job['min_salary'] <= salary <= job['max_salary']:
    #     return True
    # else:
    #     return False

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
    pass
    """
    if 'min_salary' not in job or 'max_salary' not in job:
        raise ValueError
    min_sal = job['min_salary']
    max_sal = job['max_salary']
    if type(min_sal) != int or type(max_sal) != int or type(salary) != int:
        raise ValueError
    if min_sal > max_sal:
        raise ValueError
    if min_sal <= salary <= max_sal:
        return True
    return False


def filter_by_salary_range(jobs, salary):
    result = []
    for job in jobs:
        if new_filter(job, salary):
            result.append(job)
    return result


def new_filter(job, salary):
    if 'min_salary' not in job or 'max_salary' not in job:
        return False
    min_sal = job['min_salary']
    max_sal = job['max_salary']
    if type(min_sal) != int or type(max_sal) != int or type(salary) != int:
        return False
    if min_sal > max_sal:
        return False
    if min_sal <= salary <= max_sal:
        return True