from src.jobs import read
# https://csatlas.com/python-import-file-module/


def get_unique_job_types(path):
    all_jobs = read(path)
    all_types = []
    for types in all_jobs:
        all_types.append(types["job_type"])

    return list(set(all_types))


def filter_by_job_type(jobs, job_type):
    job = []

    for v in jobs:
        if job_type in v.values():
            job.append(v)

    return job
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
   


def get_unique_industries(path):
    all_jobs = read(path)
    all_industries = []
    for types in all_jobs:
        if types["industry"] != '':
            all_industries.append(types["industry"])

    return list(set(all_industries))
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
    


def filter_by_industry(jobs, industry):
    job = []

    for v in jobs:
        if industry in v.values():
            job.append(v)

    return job
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
    


def get_max_salary(path):
    all_jobs = read(path)
    salary = []
    for types in all_jobs:
        if types["max_salary"] != '' and types["max_salary"].isnumeric():
            i = int(types["max_salary"])
            salary.append(i)

    pass
    return max(salary)
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
    pass


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
