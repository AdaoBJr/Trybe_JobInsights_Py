from .jobs import read


def get_unique_job_types(path):
    file = read(path)
    unique_job_type = set()
    for job in file:
        if job['job_type'] != '':
            unique_job_type.add(job['job_type'])

    # https://www.geeksforgeeks.org/python-convert-set-into-a-list/
    return list(unique_job_type)


def filter_by_job_type(jobs, job_type):
    result = []
    for job in jobs:
        if job['job_type'] == job_type:
            result.append(job)
    return result


def get_unique_industries(path):
    file = read(path)
    unique_industry = set()
    for job in file:
        if job['industry'] != '':
            unique_industry.add(job['industry'])

    return list(unique_industry)


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
    return []


def get_max_salary(path):
    file = read(path)
    biggest_salary = 0
    only_valid_salary = []
    for job in file:
        if job['max_salary'] != '' and job['max_salary'] != 'invalid':
            only_valid_salary.append(job['max_salary'])
    for salary in only_valid_salary:
        salary_in_number = int(salary)
        if salary_in_number > biggest_salary:
            biggest_salary = int(salary)
    return biggest_salary


def get_min_salary(path):
    file = read(path)
    only_valid_salary = []
    for job in file:
        if job['min_salary'] != '' and job['min_salary'] != 'invalid':
            only_valid_salary.append(job['min_salary'])

    lesser_salary = int(only_valid_salary[0])
    for salary in only_valid_salary:
        salary_in_number = int(salary)
        if salary_in_number < lesser_salary:
            lesser_salary = int(salary)
    return lesser_salary


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
