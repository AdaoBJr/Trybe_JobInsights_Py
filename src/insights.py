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

    num_jobs = {}
    for row in read(path):
        if row["job_type"] not in num_jobs:
            num_jobs[row["job_type"]] = {"jobs": 0}
        else:
            num_jobs[row["job_type"]]["jobs"] += 1

    return num_jobs


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
    for row in jobs:
        if row["job_type"] == job_type:
            filtered_jobs.append(row)

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
    num_jobs_by_industry = {}
    for row in read(path):
        if row["industry"] not in num_jobs_by_industry and len(
            row["industry"]
        ):
            num_jobs_by_industry[row["industry"]] = {"jobs": 0}
        elif len(row["industry"]):
            num_jobs_by_industry[row["industry"]]["jobs"] += 1

    return num_jobs_by_industry


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
    filtered_jobs = []
    for row in jobs:
        if row["industry"] == industry:
            filtered_jobs.append(row)

    return filtered_jobs


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
    max_salary = 0

    for row in read(path):
        if row["max_salary"] == "invalid":
            pass
        elif (
            len(row["max_salary"]) > 0
            and int(row["max_salary"], 10) > max_salary
        ):
            max_salary = int(row["max_salary"], 10)

    return max_salary


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
    min_salary = 999999999999999

    for row in read(path):
        if row["min_salary"] == "invalid":
            pass
        elif (
            len(row["min_salary"]) > 0
            and int(row["min_salary"], 10) < min_salary
        ):
            min_salary = int(row["min_salary"], 10)

    return min_salary


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
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError

    elif (
        type(job["min_salary"]) is not int
        or type(job["max_salary"]) is not int
        or type(salary) is not int
    ):
        raise ValueError

    elif (job["min_salary"]) > (job["max_salary"] or salary < 0):
        raise ValueError

    else:
        return salary in range(job["min_salary"], job["max_salary"])


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
    filtered_jobs = []
    for row in jobs:
        try:
            if matches_salary_range(row, salary):
                filtered_jobs.append(row)
        except ValueError:
            pass

    return filtered_jobs


# print(matches_salary_range({"min_salary": 1000, "max_salary": 3000}, 2000))
