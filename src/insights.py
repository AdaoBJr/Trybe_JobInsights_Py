from src.jobs import read


def get_unique_job_types(path):
    jobs = read(path)
    job_types = []
    for job in jobs:
        if job["job_type"] not in job_types:
            job_types.append(job["job_type"])
    return job_types


def filter_by_job_type(jobs, job_type):
    filter_job = []
    for element in jobs:
        if element["job_type"] == job_type:
            filter_job.append(element)
    return filter_job


def get_unique_industries(path):
    jobs = read(path)
    industries = []
    for element in jobs:
        if element["industry"] not in industries:
            industries.append(element["industry"])
    return industries


def filter_by_industry(jobs, industry):
    filter_industry = []
    for element in jobs:
        if element["job_type"] == industry:
            filter_industry.append(element)
    return filter_industry


def get_max_salary(path):
    jobs = read(path)
    max_salary = []
    for element in jobs:
        if element["max_salary"] != "invalid" and element["max_salary"] != "":
            max_salary.append(int(element["max_salary"]))
    return max(max_salary)


def get_min_salary(path):
    jobs = read(path)
    min_salary = []
    for element in jobs:
        if element["min_salary"] != "invalid" and element["min_salary"] != "":
            min_salary.append(int(element["min_salary"]))
    return min(min_salary)


def matches_salary_range(job, salary):

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
