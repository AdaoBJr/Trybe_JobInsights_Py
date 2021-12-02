from src.jobs import read


def get_unique_job_types(path):
    file = read(path)
    jobs_title = set()
    for job in file:
        jobs_title.add(job['job_type'])
    return list(jobs_title)


def filter_by_job_type(jobs, job_type):
    return [job for job in jobs if job["job_type"] == job_type]


def get_unique_industries(path):
    file = read(path)
    jobs_industries = set()
    for job in file:
        if len(job["industry"]) > 0:
            jobs_industries.add(job["industry"])
    return jobs_industries


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
    file = read(path)
    max_salary_jobs = 0
    for job in file:
        if len(job["max_salary"]) > 0 and job["max_salary"] != "invalid":
            print(job["max_salary"], 'SALARIOS')
            if float(job["max_salary"]) > max_salary_jobs:
                max_salary_jobs = int(job["max_salary"])
    return max_salary_jobs


def get_min_salary(path):
    file = read(path)
    min_salary_jobs = 10000000000000
    for job in file:
        if len(job["min_salary"]) > 0 and job["min_salary"] != "invalid":
            if float(job["min_salary"]) < min_salary_jobs:
                min_salary_jobs = int(job["min_salary"])
    return min_salary_jobs


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
