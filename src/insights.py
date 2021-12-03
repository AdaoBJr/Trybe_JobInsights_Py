from src.jobs import read


def get_unique_job_types(path):
    data = read(path)
    all_jobs = []
    for row in data:
        if row['job_type'] not in all_jobs:
            all_jobs.append(row['job_type'])

    return all_jobs


def filter_by_job_type(jobs, job_type):
    # return list(filter(lambda job: (job['job_type'] == job_type), jobs))
    return [job for job in jobs if job['job_type'] == job_type]


def get_unique_industries(path):
    data = read(path)
    all_industries = []
    for row in data:
        if row['industry'] not in all_industries and row['industry'] != '':
            all_industries.append(row['industry'])

    return all_industries


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
    data = read(path)
    max_salary = 0
    for row in data:
        try:
            max_salary_row = int(row['max_salary'])
            if(max_salary_row > max_salary):
                max_salary = max_salary_row
        except ValueError:
            continue

    return max_salary


def get_min_salary(path):
    data = read(path)
    min_salary = get_max_salary(path)
    for row in data:
        try:
            min_salary_row = int(row['min_salary'])
            if(min_salary_row < min_salary):
                min_salary = min_salary_row
        except ValueError:
            continue

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
