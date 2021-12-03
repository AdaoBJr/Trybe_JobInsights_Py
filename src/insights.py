from src.jobs import read


def get_unique_job_types(path):
    jobs = read(path)
    job_types = []
    for job in jobs:
        if job["job_type"] not in job_types:
            job_types.append(job["job_type"])
    return job_types


def filter_by_job_type(jobs, job_type):
    jobs_filtered = []
    for job in jobs:
        if job["job_type"] == job_type:
            jobs_filtered.append(job)
    return jobs_filtered


def get_unique_industries(path):
    jobs = read(path)
    industry = set()
    for job in jobs:
        if job["industry"] != "":
            industry.add(job["industry"])
    return industry


def filter_by_industry(jobs, industry):
    industry_jobs = []
    for job in jobs:
        if job["industry"] == industry:
            industry_jobs.append(job)
    return industry_jobs


def get_max_salary(path):
    jobs = read(path)
    max_salary = []
    for job in jobs:
        if job["max_salary"] != "" and job["max_salary"] != "invalid":
            max_salary.append(int(job["max_salary"]))
    return max(max_salary)


def get_min_salary(path):
    jobs = read(path)
    min_salary = []
    for job in jobs:
        if job["min_salary"] != "" and job["min_salary"] != "invalid":
            min_salary.append(int(job["min_salary"]))
    return min(min_salary)
    pass


def matches_salary_range(job, salary):
    if (
        "min_salary" not in job
        or "max_salary" not in job
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
