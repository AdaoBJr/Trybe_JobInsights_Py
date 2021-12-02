from src.jobs import read


def get_unique_job_types(path):
    job_list = read(path)
    job_list_header = set()
    for job in job_list:
        job_list_header.add(job["job_type"])

    return job_list_header


def filter_by_job_type(jobs, job_type):
    filtered_jobs = [job for job in jobs if job["job_type"] == job_type]
    return filtered_jobs

# Assim que faz um filter


def get_unique_industries(path):
    industries_list = read(path)
    industry_list_header = set()
    for industry in industries_list:
        if industry["industry"] != '':
            industry_list_header.add(industry["industry"])

    return industry_list_header


def filter_by_industry(jobs, industry):
    filtered_jobs = [job for job in jobs if job["industry"] == industry]
    return filtered_jobs

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


def get_max_salary(path):
    job_list = read(path)
    job_salaries = set()
    for job in job_list:
        if job['max_salary'] != '' and job['max_salary'].isnumeric():
            job_salaries.add(int(job['max_salary']))

    maxsalary = max(job_salaries)

    return maxsalary


def get_min_salary(path):
    job_list = read(path)
    job_salaries = set()
    for job in job_list:
        if job['min_salary'] != '' and job['min_salary'].isnumeric():
            job_salaries.add(int(job['min_salary']))

    min_salary = min(job_salaries)

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
