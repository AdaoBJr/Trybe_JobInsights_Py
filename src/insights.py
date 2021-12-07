from .jobs import read


def get_unique_job_types(path):
    """Checks all different job types and returns a list of them

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
    all_jobs = read(path)
    job_types = set()
    for job in all_jobs:
        job_types.add(job["job_type"])
    return [
        *job_types,
    ]  # https://www.geeksforgeeks.org/python-convert-set-into-a-list/


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
    return [job for job in jobs if job["job_type"] == job_type]


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
    all_jobs = read(path)
    industries = set()
    for job in all_jobs:
        industries.add(job["industry"])
    industries_list = [
        *industries,
    ]
    return [ind for ind in industries_list if ind and ind is not None]


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
    return [job for job in jobs if job["industry"] == industry]


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
    all_jobs = read(path)
    salaries = []
    for job in all_jobs:
        try:
            salaries.append(int(job["max_salary"]))
        except ValueError:
            continue
    salaries.sort()
    return salaries[-1]


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
    all_jobs = read(path)
    salaries = []
    for job in all_jobs:
        try:
            salaries.append(int(job["min_salary"]))
        except ValueError:
            continue
    salaries.sort(reverse=True)
    return salaries[-1]


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
    try:
        if (
            type(job["min_salary"]) is int
            and type(job["max_salary"]) is int
            and type(salary) is int
        ):
            if job["min_salary"] <= salary and salary <= job["max_salary"]:
                return True
        return False
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")


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
    return [job for job in jobs if matches_salary_range(job, salary)]
