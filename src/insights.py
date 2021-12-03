from src.jobs import read


def get_unique_job_types(path):
    """Checks all different job types and returns a list of them.

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """
    get_jobs = read(path)
    job_types = set()
    for job in get_jobs:
        job_types.add(job["job_type"])
    return job_types


def filter_by_job_type(jobs, job_type):
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    job_list = []
    for job in jobs:
        if job["job_type"] == job_type:
            job_list.append(job)
    return job_list


def get_unique_industries(path):
    """Checks all different industries and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique industries
    """
    get_jobs = read(path)
    industries = set()
    for job in get_jobs:
        if job["industry"] != "":
            industries.add(job["industry"])
    return industries


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
    job_list = []
    for job in jobs:
        if job["industry"] == industry:
            job_list.append(job)
    return job_list


def get_max_salary(path):
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    get_jobs = read(path)
    get_higher_salaries = []
    for job in get_jobs:
        if job["max_salary"] != "":
            if job["max_salary"].isdigit():
                get_higher_salaries.append(int(job["max_salary"]))
    return max(get_higher_salaries)


def get_min_salary(path):
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    get_jobs = read(path)
    get_min_salaries = []
    for job in get_jobs:
        if job["min_salary"] != "":
            if job["min_salary"].isdigit():
                get_min_salaries.append(int(job["min_salary"]))
    return min(get_min_salaries)


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
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError("`job` must have `min_salary` and `max_salary` keys")
    elif (type(job["min_salary"]) == str or type(job["max_salary"]) == str or
          type(salary) != int):
        raise ValueError("`job` must have `min_salary` and `max_salary` as")
    elif job["max_salary"] < job["min_salary"]:
        raise ValueError("`job` must have `min_salary` less than `max_salary`")
    return job["min_salary"] <= salary <= job["max_salary"]


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
