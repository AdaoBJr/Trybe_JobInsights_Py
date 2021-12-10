from .jobs import read


def get_unique_job_types(path):
    jobs_list = read(path)
    job_types_list = []

    for job in jobs_list:
        if job["job_type"] and job["job_type"] not in job_types_list:
            job_types_list.append(job["job_type"])

    return job_types_list


def filter_by_job_type(jobs, job_type):
    filtered_jobs = []

    for job in jobs:
        if job["job_type"] and job["job_type"] == job_type:
            filtered_jobs.append(job)

    return filtered_jobs


def get_unique_industries(path):
    jobs_list = read(path)
    industries_list = []

    for job in jobs_list:
        if job["industry"] and job["industry"] not in industries_list:
            industries_list.append(job["industry"])

    return industries_list


def filter_by_industry(jobs, industry):
    filtered_jobs = []

    for job in jobs:
        if job["industry"] and job["industry"] == industry:
            filtered_jobs.append(job)

    return filtered_jobs


def get_max_salary(path):
    jobs_list = read(path)
    max_salaries = []

    for job in jobs_list:
        if job["max_salary"].isnumeric():
            max_salaries.append(int(job["max_salary"]))

    return max(max_salaries)


def get_min_salary(path):
    jobs_list = read(path)
    min_salaries = []

    for job in jobs_list:
        if job["min_salary"].isnumeric():
            min_salaries.append(int(job["min_salary"]))

    return min(min_salaries)


def matches_salary_range(job, salary):
    if (
        "min_salary" not in job
        or "max_salary" not in job
        or not isinstance(job["min_salary"], int)
        or not isinstance(job["max_salary"], int)
        or job["min_salary"] > job["max_salary"]
        or not isinstance(salary, int)
    ):
        raise ValueError

    if job["min_salary"] <= salary <= job["max_salary"]:
        return True
    else:
        return False


def filter_by_salary_range(jobs, salary):
    filtered_jobs = []

    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                filtered_jobs.append(job)
        except ValueError:
            pass

    return filtered_jobs
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
