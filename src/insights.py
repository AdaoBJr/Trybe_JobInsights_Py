from src.jobs import read


def get_unique_job_types(path):
    read_jobs = read(path)
    return set(job["job_type"] for job in read_jobs)

    # jobs = set()
    # for job in read_jobs:
    #   jobs.add(job["job_type"])


def filter_by_job_type(jobs, job_type):
    return [job for job in jobs if job["job_type"] == job_type]
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
    read_jobs = read(path)
    return set(job["industry"] for job in read_jobs if job["industry"])
    # jobs = set()
    # for job in read_jobs:
    #   if job['industry']:
    #     jobs.add(job["industry"])


def filter_by_industry(jobs, industry):
    return [job for job in jobs if job["industry"] == industry]


def get_max_salary(path):
    read_jobs = read(path)
    list_max_salary = set(
        job["max_salary"] for job in read_jobs if job["max_salary"].isdigit())
    return max(int(salary) for salary in list_max_salary)


def get_min_salary(path):
    read_jobs = read(path)
    list_min_salary = set(
        job["min_salary"] for job in read_jobs if job["min_salary"].isdigit())
    return min(int(salary) for salary in list_min_salary)


def matches_salary_range(job, salary):
    if (
        "min_salary" not in job
        or "max_salary" not in job
        or type(job["min_salary"]) != int
        or type(job["max_salary"]) != int
        or type(salary) != int
        or job["min_salary"] > job["max_salary"]
    ):
        raise ValueError
    else:
        return int(job["min_salary"] <= int(salary) <= int(job["max_salary"]))


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
