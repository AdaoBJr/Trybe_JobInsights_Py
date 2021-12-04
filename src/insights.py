from src.jobs import read
# from jobs import read


def get_column_unique(dict, name_column):
    return set(map(lambda job: job[name_column], dict))


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
    return get_column_unique(read(path), "job_type")


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
    jobs_filter = filter(lambda job: job["job_type"] == job_type, jobs)
    return list(jobs_filter)


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
    industries = get_column_unique(read(path), "industry")
    return list(filter(None, industries))


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
    indrutries = filter(lambda job: job["industry"] == industry, jobs)
    return list(indrutries)


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
    salaries = map(lambda job: job["max_salary"], read(path))
    salaries_str = filter(str.isdigit, salaries)
    salary_max = max(map(lambda salary: int(salary), salaries_str))
    return salary_max


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
    salaries = map(lambda job: job["min_salary"], read(path))
    salaries_str = filter(str.isdigit, salaries)
    salary_min = min(map(lambda salary: int(salary), salaries_str))
    return salary_min


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

    salaries_str = filter(
        lambda job: job["min_salary"].isnumeric()
        and job["max_salary"].isnumeric(),
        jobs,
    )

    salaries_filt = filter(
        lambda job: int(job["min_salary"]) <= salary <= int(job["max_salary"]),
        salaries_str,
    )

    return list(salaries_filt)
