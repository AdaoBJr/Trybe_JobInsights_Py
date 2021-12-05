from .jobs import read


def get_unique_job_types(path):
    jobs_type = []
    jobs_unique_types = []
    result_jobs = read(path)
    for jobs in result_jobs:
        if jobs["job_type"] != "":
            jobs_type.append(jobs["job_type"])
    for jobs_unique in jobs_type:
        if jobs_unique not in jobs_unique_types:
            jobs_unique_types.append(jobs_unique)
    return jobs_unique_types


def filter_by_job_type(jobs, job_type):
    filter_job_types = []
    for job in jobs:
        if job_type in job.values():
            filter_job_types.append(job)
    return filter_job_types


def get_unique_industries(path):
    result_industries = []
    unique_industries = []
    result_jobs = read(path)
    for jobs in result_jobs:
        if jobs["industry"] != "":
            result_industries.append(jobs["industry"])
    for industries in result_industries:
        if industries not in unique_industries:
            unique_industries.append(industries)
    return unique_industries


def filter_by_industry(jobs, industry):
    filter_job_industry = []
    for job in jobs:
        if industry in job.values():
            filter_job_industry.append(job)
    return filter_job_industry


def get_max_salary(path):
    salaries = []
    result_jobs = read(path)
    for jobs in result_jobs:
        if jobs["max_salary"] != "":
            if jobs["max_salary"].isdigit():
                salaries.append(int(jobs["max_salary"]))
    return max(salaries)


def get_min_salary(path):
    salaries = []
    result_jobs = read(path)
    for jobs in result_jobs:
        if jobs["min_salary"] != "":
            if jobs["min_salary"].isdigit():
                salaries.append(int(jobs["min_salary"]))
    return min(salaries)


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
