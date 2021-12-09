from src.jobs import read


def get_unique_job_types(path):
    jobs_data = read(path)
    types = set()
    for job in jobs_data:
        types.add(job["job_type"])
    return types


def filter_by_job_type(jobs, job_type):
    return [job for job in jobs if job["job_type"] == job_type]


def get_unique_industries(path):
    jobs_data = read(path)
    industries = set()
    for industry in jobs_data:
        if industry["industry"] != "":
            industries.add(industry["industry"])
    return industries


def filter_by_industry(jobs, industry):
    return [ind for ind in jobs if ind["industry"] == industry]


def get_max_salary(path):
    jobs_data = read(path)
    salary_info = set()
    for salary in jobs_data:
        if salary["max_salary"].isnumeric():
            salary_info.add(float(salary["max_salary"]))
    return max(salary_info)


def get_min_salary(path):
    jobs_data = read(path)
    salary_info = set()
    for salary in jobs_data:
        if salary["min_salary"].isnumeric():
            salary_info.add(float(salary["min_salary"]))
    return min(salary_info)


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
