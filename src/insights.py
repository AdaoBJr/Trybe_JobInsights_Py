import src.jobs


def get_unique_job_types(path):
    new_data = src.jobs.read(path)
    list_unique_job_types = set()
    for new_job in new_data:
        list_unique_job_types.add(new_job['job_type'])
    return list_unique_job_types

    # """Checks all different job types and returns a list of them

    # Must call `read`

    # Parameters
    # ----------
    # path : str
    #     Must be passed to `read`

    # Returns
    # -------
    # list
    #     List of unique job types
    # """


def filter_by_job_type(jobs, job_type):
    list_jobs = []  
    for new_job in jobs:
        if new_job['job_type'] == job_type:
            list_jobs.append(new_job)
    return list_jobs
    
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
    return []


def get_unique_industries(path):
    new_data = src.jobs.read(path)
    list_unique_industries = set()
    for industry in new_data:
        if industry['industry'] != "":
            list_unique_industries.add(industry['industry'])
    return list_unique_industries
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
    return []


def filter_by_industry(jobs, industry):
    list_industry = []  
    for job_industry in jobs:
        if job_industry['industry'] == industry:
            list_industry.append(job_industry)
    return list_industry
    
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
    return []


def get_max_salary(path):
    new_data = src.jobs.read(path)
    list_max_salary = set()
    for salary in new_data:
        if salary['max_salary'].isnumeric():
            list_max_salary.add(int(salary['max_salary']))
    return max(list_max_salary)
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
    new_data = src.jobs.read(path)
    list_min_salary = set()
    for salary in new_data:
        if salary['min_salary'].isnumeric():
            list_min_salary.add(int(salary['min_salary']))
    return min(list_min_salary)
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
