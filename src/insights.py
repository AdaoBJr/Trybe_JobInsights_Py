from src.jobs import read


def get_unique_job_types(path):
    all_jobs = read(path)
    # pq não funciona?
    # print(set(job['job_type'] for job in all_jobs))
    # console.append(job['job_type'] for job in all_jobs)
    console = set()
    for job in all_jobs:
        console.add(job["job_type"])
    return console


def filter_by_job_type(jobs, job_type):
    list = []
    for job in jobs:
        if job["job_type"] == job_type:
            list.append(job)
    return list


def get_unique_industries(path):
    all_jobs = read(path)
    console = set()
    for job in all_jobs:
        if job["industry"]:
            console.add(job["industry"])
    return console


def filter_by_industry(jobs, industry):
    industries = []
    for job in jobs:
        if job["industry"] == industry:
            industries.append(job)
    return industries


def get_max_salary(path):
    all_jobs = read(path)
    max_salary = 0

    for job in all_jobs:
        if (
            job["max_salary"].isnumeric()
            and int(job["max_salary"]) > max_salary
        ):
            max_salary = int(job["max_salary"])
    return max_salary

    pass


def get_min_salary(path):
    all_jobs = read(path)
    min_salary = 90000

    for job in all_jobs:
        if (
            job["min_salary"].isnumeric()
            and int(job["min_salary"]) < min_salary
        ):
            min_salary = int(job["min_salary"])
    return min_salary
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
