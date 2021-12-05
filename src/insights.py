from src.jobs import read


def get_unique_job_types(path):
    jobs = read(path)
    job_types = set()
    for job in jobs:
        job_types.add(job["job_type"])
    return job_types


def get_unique_industries(path):
    jobs = read(path)
    industries = set()
    for job in jobs:
        if job["industry"] != "":
            industries.add(job["industry"])
    return industries


def get_max_salary(path):
    jobs = read(path)
    max_salary = [int(job["max_salary"])
                  for job in jobs
                  if job["max_salary"] != ""
                  and job["max_salary"].isnumeric()]
    return max(max_salary)
# source func isNumeric() / max() ->
# https://acervolima.com/python-string-isnumeric-e-sua-aplicacao/
# https://acervolima.com/python-funcao-max/


def filter_by_job_type(jobs, job_type):
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


def filter_by_industry(jobs, industry):
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
    pass


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
