from src import jobs


def get_unique_job_types(path):
    jobs_list = jobs.read(path)
    types = set()
    for job in jobs_list:
        if job["job_type"] != "":
            types.add(job["job_type"])
    return types


def filter_by_job_type(jobs, job_type):
    jobs_type_list = []
    for job in jobs:
        if job["job_type"] == job_type:
            jobs_type_list.append(job)
    return jobs_type_list


def get_unique_industries(path):
    jobs_list = jobs.read(path)
    industries = set()
    for job in jobs_list:
        if job["industry"] != "":
            industries.add(job["industry"])
    return industries


def filter_by_industry(jobs, industry):
    industries_list = []
    for job in jobs:
        if job["industry"] == industry:
            industries_list.append(job)
    return industries_list


def get_max_salary(path):
    jobs_list = jobs.read(path)
    max_salaries = set()
    for job in jobs_list:
        if job["max_salary"] != "" and job["max_salary"].isnumeric():
            max_salaries.add(int(job["max_salary"]))
    max_salaries = max(max_salaries)
    return max_salaries


def get_min_salary(path):
    jobs_list = jobs.read(path)
    min_salaries = set()
    for job in jobs_list:
        if job["min_salary"] != "" and job["min_salary"].isnumeric():
            min_salaries.add(int(job["min_salary"]))
    min_salaries = min(min_salaries)
    return min_salaries


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
