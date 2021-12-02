from src import jobs


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
    """
    Material consultado sobre converter set para list
    https://favtutor.com/blogs/set-to-list-python
    https://www.geeksforgeeks.org/python-convert-set-into-a-list/
    """
    job_data = jobs.read(path)
    job_type_set = set()
    for job in job_data:
        job_type_set.add(job["job_type"])
    return sorted(job_type_set)


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
    """
    Material consultado sobre como verificar se um valor está na lista
    https://stackoverflow.com/a/7571665
    """
    filtered_jobs = [job
                     for job in jobs
                     if job["job_type"] in job_type]
    return filtered_jobs


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
    job_data = jobs.read(path)
    industries_set = {job["industry"]
                      for job in job_data
                      if job["industry"] != ""}
    return sorted(industries_set)


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
    return []


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
    """
    Material consultado sobre isnumeric; dica Henrique Zózimo
    https://docs.python.org/pt-br/3.8/library/stdtypes.html#str.isnumeric
    https://www.w3schools.com/python/ref_string_isnumeric.asp
    """
    job_data = jobs.read(path)
    maximum_salary = 0
    for job in job_data:
        if (job["max_salary"].isnumeric() and
           int(job["max_salary"]) > maximum_salary):
            maximum_salary = int(float(job["max_salary"]))
    return maximum_salary


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
    """
    Material consultado sobre o máximo inteiro no Python
    https://www.delftstack.com/howto/python/python-max-int/
    """
    job_data = jobs.read(path)
    minimum_salary = 2 ** 31 - 1
    for job in job_data:
        if (job["min_salary"].isnumeric() and
           int(job["min_salary"]) < minimum_salary):
            minimum_salary = int(float(job["min_salary"]))
    return minimum_salary


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
