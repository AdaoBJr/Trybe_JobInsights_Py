from src.jobs import read


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
    data = read(path)
    jobs_set = set()
    for jobs in data:
        jobs_set.add(jobs["job_type"])

    return list(jobs_set)


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
    filtered_jobs = []
    for job in jobs:
        if job["job_type"] == job_type:
            filtered_jobs.append(job)

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
    data = read(path)
    industries_set = set()
    for industry in data:
        if industry["industry"] != '':
            industries_set.add(industry["industry"])

    return list(industries_set)


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
    filtered_industry = []
    for ind in jobs:
        if ind["industry"] == industry:
            filtered_industry.append(ind)

    return filtered_industry


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
    data = read(path)
    maximum = []
    for max_sal in data:
        if max_sal["max_salary"] != '' and max_sal["max_salary"] != 'invalid':
            salary = max_sal["max_salary"]
            maximum.append(int(salary))
    maximum.sort()
    return maximum[len(maximum) - 1]


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
    data = read(path)
    minimun = []
    for min_sal in data:
        if min_sal["min_salary"] != '' and min_sal["min_salary"] != 'invalid':
            salary = min_sal["min_salary"]
            minimun.append(int(salary))
    minimun.sort()
    return minimun[0]


def matches_salary_range(job, salary):
    if (
        "min_salary" not in job or "max_salary" not in job
        or not isinstance(job["min_salary"], int)
        or not isinstance(job["max_salary"], int)
        or job["min_salary"] > job["max_salary"]
        or not isinstance(job["min_salary"], int)
    ):
        raise ValueError("Job doesn't have a salary range")

    if salary >= job["min_salary"] and salary <= job["max_salary"]:
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
    return []
