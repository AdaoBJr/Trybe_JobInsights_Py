from .jobs import read


def get_unique_job_types(path):
    unique_job_types = set()
    jobs = read(path)
    for dict in jobs:
        unique_job_types.add(dict["job_type"])
    return list(unique_job_types)


def filter_by_job_type(jobs, job_type):
    filtered_jobs = []
    for job in jobs:
        if job["job_type"] == job_type:
            filtered_jobs.append(job)
    return filtered_jobs


def get_unique_industries(path):
    unique_industries = set()
    jobs = read(path)
    for dict in jobs:
        if dict["industry"] != "":
            unique_industries.add(dict["industry"])
    return list(unique_industries)


def filter_by_industry(jobs, industry):
    filtered_jobs = []
    for job in jobs:
        if job["industry"] == industry:
            filtered_jobs.append(job)
    return filtered_jobs


def get_max_salary(path):
    max_salary_list = []
    jobs = read(path)
    for job in jobs:
        if job["max_salary"].isnumeric():
            max_salary_list.append(int(job["max_salary"]))
    return max(max_salary_list)


def get_min_salary(path):
    min_salary_list = []
    jobs = read(path)
    for job in jobs:
        if job["min_salary"].isnumeric():
            min_salary_list.append(int(job["min_salary"]))
    return min(min_salary_list)


def validate_min_and_max_salaries(job):
    if ("max_salary" not in job or "min_salary" not in job):
        raise ValueError("job doesn't have 'min_salary' or 'max_salary'")
    if (not isinstance(job["min_salary"], int)
            or not isinstance(job["max_salary"], int)):
        raise ValueError("'min_salary' or 'max_salary' aren't an integer")
    if (job["max_salary"] < job["min_salary"]):
        raise ValueError("'min_salary' is larger than 'max_salary'")


def validade_salary(salary):
    if not (isinstance(salary, int)):
        raise ValueError("'salary' is not an integer")


def matches_salary_range(job, salary):
    validate_min_and_max_salaries(job)
    validade_salary(salary)
    if (job["min_salary"] <= salary <= job["max_salary"]):
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
