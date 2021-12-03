from .jobs import read


def get_unique_job_types(path):
    jobs_dict = read(path)
    job_types = set()
    for job in jobs_dict:
        job_types.add(job["job_type"])
    return list(job_types)


def filter_by_job_type(jobs, job_type):
    result = []
    for job in jobs:
        if job["job_type"] == job_type:
            result.append(job)
    return result


def get_unique_industries(path):
    jobs_dict = read(path)
    job_industries = set()
    for job in jobs_dict:
        if job["industry"] != "":
            job_industries.add(job["industry"])
    return list(job_industries)


def filter_by_industry(jobs, industry):
    result = []
    for job in jobs:
        if job["industry"] == industry:
            result.append(job)
    return result


def get_max_salary(path):
    jobs_dict = read(path)
    max_salaries = []
    for job in jobs_dict:
        if job["max_salary"].isnumeric():
            max_salaries.append(int(job["max_salary"]))
    return max(max_salaries)


def get_min_salary(path):
    jobs_dict = read(path)
    min_salaries = []
    for job in jobs_dict:
        if job["min_salary"].isnumeric():
            min_salaries.append(int(job["min_salary"]))
    return min(min_salaries)


def matches_salary_range(job, salary):
    if (
        "max_salary" not in job
        or "min_salary" not in job
        or type(job["max_salary"]) != int
        or type(job["min_salary"]) != int
        or type(salary) != int
        or job["min_salary"] > job["max_salary"]
    ):
        raise ValueError("Invalid input")

    if job["min_salary"] <= salary <= job["max_salary"]:
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
