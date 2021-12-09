import src.jobs


def get_unique_job_types(path):
    all_jobs = src.jobs.read(path)
    job_types = []
    for job in all_jobs:
        if job["job_type"] not in job_types:
            job_types.append(job["job_type"])
    return job_types


def filter_by_job_type(jobs, job_type):
    filtered_jobs = []
    for job in jobs:
        if job["job_type"] == job_type:
            filtered_jobs.append(job)
    return filtered_jobs


def get_unique_industries(path):
    all_jobs = src.jobs.read(path)
    industry = set()
    for job in all_jobs:
        if job["industry"] != "":
            industry.add(job["industry"])
    return industry


def filter_by_industry(jobs, industry):
    filtered_industries = []
    for job in jobs:
        if job["industry"] == industry:
            filtered_industries.append(job["industry"])
    return filtered_industries


def get_max_salary(path):
    all_jobs = src.jobs.read(path)
    max_salary = []
    for job in all_jobs:
        if job["max_salary"] != "" and job["max_salary"] != "invalid":
            max_salary.append(int(job["max_salary"]))
    return max(max_salary)


def get_min_salary(path):
    all_jobs = src.jobs.read(path)
    min_salary = []
    for job in all_jobs:
        if job["min_salary"] != "" and job["min_salary"] != "invalid":
            min_salary.append(int(job["min_salary"]))
    return min(min_salary)


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
