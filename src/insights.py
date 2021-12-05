from src.jobs import read


def get_unique_job_types(path):
    list_jobs = read(path)
    jobs_type = set()
    for job in list_jobs:
        jobs_type.add(job["job_type"])
    return jobs_type


def filter_by_job_type(jobs, job_type):
    result = []
    for job in jobs:
        if job["job_type"] == job_type:
            result.append(job)
    return result


def get_unique_industries(path):
    list_jobs = read(path)
    jobs_industry = set()
    for job in list_jobs:
        if job["industry"] != '':
            jobs_industry.add(job["industry"])
    return jobs_industry


def filter_by_industry(jobs, industry):
    result = []
    for job in jobs:
        if job["industry"] == industry:
            result.append(job)
    return result


def get_max_salary(path):
    list_jobs = read(path)
    max_salary = 0
    for job in list_jobs:
        if job["max_salary"] != '' and job["max_salary"].isnumeric():
            if float(job["max_salary"]) > max_salary:
                max_salary = float(job["max_salary"])
    return max_salary


def get_min_salary(path):
    list_jobs = read(path)
    min_salary = get_max_salary(path)
    for job in list_jobs:
        if job["min_salary"] != '' and job["min_salary"].isnumeric():
            if float(job["min_salary"]) < min_salary:
                min_salary = float(job["min_salary"])
    return min_salary


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
