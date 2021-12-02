from .jobs import read


def get_unique_job_types(path):
    job_types = set()
    jobs_dict = read(path)
    for dict in jobs_dict:
        job_types.add(dict["job_type"])
    return list(job_types)


def filter_by_job_type(jobs, job_type):
    jobs_list = []
    for job in jobs:
        if job["job_type"] == job_type:
            jobs_list.append(job)
    return jobs_list


def get_unique_industries(path):
    industries = set()
    jobs_dict = read(path)
    for dict in jobs_dict:
        if dict["industry"] != "":
            industries.add(dict["industry"])
    return list(industries)


def filter_by_industry(jobs, industry):
    instrudies_list = []
    for job in jobs:
        if job["industry"] == industry:
            instrudies_list.append(job)
    return instrudies_list


def get_max_salary(path):
    max_salaries = set()
    jobs_list = read(path)
    for job in jobs_list:
        if job["max_salary"].isnumeric():
            max_salaries.add(int(job["max_salary"]))
    return max(list(max_salaries))


def get_min_salary(path):
    min_salaries = []
    jobs_list = read(path)
    for job in jobs_list:
        if job["min_salary"].isnumeric():
            min_salaries.append(int(job["min_salary"]))
    return min(min_salaries)


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
