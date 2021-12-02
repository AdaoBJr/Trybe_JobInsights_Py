from src import jobs


# req 2
def get_unique_job_types(path):
    all_jobs = jobs.read(path)
    unique_jobs = []
    for job in all_jobs:
        if job["job_type"] not in unique_jobs:
            unique_jobs.append(job["job_type"])
    return unique_jobs


# req 6
def filter_by_job_type(jobs, job_type):
    filter_jobs = []
    for job in jobs:
        if job["job_type"] == job_type:
            filter_jobs.append(job)
    return filter_jobs


# req 3
def get_unique_industries(path):
    all_jobs = jobs.read(path)
    unique_industries = []
    for job in all_jobs:
        if job["industry"] not in unique_industries and job["industry"] != '':
            unique_industries.append(job["industry"])
    return unique_industries


# req 7
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


# req 4
def get_max_salary(path):
    all_salary = jobs.read(path)
    max_salary = []
    for job in all_salary:
        if job["max_salary"] not in max_salary and job["max_salary"] != '':
            try:
                max_salary.append(int(job["max_salary"]))
            except ValueError:
                print("Invalid")
    return max(max_salary)


# req 5
def get_min_salary(path):
    all_salary = jobs.read(path)
    min_salary = []
    for job in all_salary:
        if job["min_salary"] not in min_salary and job["min_salary"] != '':
            try:
                min_salary.append(int(job["min_salary"]))
            except ValueError:
                print("Invalid")
    return min(min_salary)


# req 8
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


# req 9
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
