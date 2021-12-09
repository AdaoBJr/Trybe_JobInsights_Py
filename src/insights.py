from src.jobs import read


def get_unique_job_types(path):
    read_jobs = read(path)
    types = set()
    for job in read_jobs:
        types.add(job["job_type"])
    return types


def filter_by_job_type(jobs, job_type):
    return [job for job in jobs if job["job_type"] == job_type]


def get_unique_industries(path):
    read_jobs = read(path)
    types = set()
    for industry in read_jobs:
        if industry["industry"] != "":
            types.add(industry["industry"])
    return types


def filter_by_industry(jobs, industry):
    return [job for job in jobs if job["industry"] == industry]


def get_max_salary(path):
    read_jobs = read(path)
    types = set()
    for salary in read_jobs:
        # https://www.w3schools.com/python/ref_string_isnumeric.asp
        if salary["max_salary"].isnumeric():
            types.add(int(salary["max_salary"]))
    # https://www.w3schools.com/python/ref_func_max.asp
    return max(types)


def get_min_salary(path):
    read_jobs = read(path)
    types = set()
    for salary in read_jobs:
        if salary["min_salary"].isnumeric():
            types.add(int(salary["min_salary"]))
    return min(types)


def matches_salary_range(job, salary):
    if (
        "min_salary" not in job
        or "max_salary" not in job
        or type(job["min_salary"]) != int
        or type(job["max_salary"]) != int
        or job["min_salary"] > job["max_salary"]
    ):
        raise ValueError
    return job["min_salary"] <= salary <= job["max_salary"]


def filter_by_salary_range(jobs, salary):
    filter_salary = []
    for job in jobs:
        try:
            if type(salary) == int and matches_salary_range(job, salary):
                filter_salary.append(job)
        except ValueError:
            pass
    return filter_salary
