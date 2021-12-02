from src.jobs import read

# from jobs import read


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

    job_types = [job["job_type"] for job in all_jobs if job["job_type"]]
    unique_job_type = list(set(job_types))

    return unique_job_type


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

    industries_types = [job["industry"] for job in all_jobs if job["industry"]]
    unique_industry_type = list(set(industries_types))
    return unique_industry_type


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
    max_salary = [
        int(job["max_salary"])
        for job in all_jobs
        if job["max_salary"].isnumeric()
    ]

    return max(max_salary)


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
    min_salary = [
        int(job["min_salary"])
        for job in all_jobs
        if job["min_salary"].isnumeric()
    ]
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

    min_salary = job.get("min_salary")
    max_salary = job.get("max_salary")

    if min_salary is None or max_salary is None:
        raise ValueError("Any empty field")
    if not type(min_salary) is int or not type(max_salary) is int:
        raise ValueError("Type must be integer")
    if min_salary > max_salary:
        raise ValueError("Max salary must be greater than min salary")
    if not type(salary) == int:
        raise ValueError("Salary type must be integer")

    if min_salary <= salary <= max_salary:
        return True
    else:
        return False


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
    if not type(salary) is int:
        return []
    
    salary_list = []
    for job in jobs:
        min_salary = job["min_salary"]
        max_salary = job["max_salary"]
        if (
            type(min_salary) is int
            and type(max_salary) is int
            and max_salary > min_salary
            and matches_salary_range(job, salary)
        ):
            salary_list.append(job)
    return salary_list
