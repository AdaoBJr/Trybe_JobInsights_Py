from src.jobs import read


def get_unique_job_types(path):
    read_file = read(path)
    job_types = set()
    for job in read_file:
        job_types.add(job["job_type"])
    return job_types


def filter_by_job_type(jobs, job_type):
    return [job for job in jobs if job["job_type"] == job_type]


def get_unique_industries(path):
    read_file = read(path)
    industries = set()
    for industry in read_file:
        if industry["industry"] != "":
            industries.add(industry["industry"])
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
    return []


def get_max_salary(path):
    read_file = read(path)
    salary = 0
    for work in read_file:
        if work["max_salary"].isnumeric() and int(work["max_salary"]) > salary:
            salary = int(work["max_salary"])
    return salary


def get_min_salary(path):
    read_file = read(path)
    salary = []
    for work in read_file:
        if work["min_salary"] != "":
            try:
                salary.append(int(work["min_salary"]))
            except ValueError:
                pass
    return min(salary)


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
