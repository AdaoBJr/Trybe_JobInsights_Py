from src.jobs import read
# https://csatlas.com/python-import-file-module/


def get_unique_job_types(path):
    all_jobs = read(path)
    all_types = []
    for types in all_jobs:
        all_types.append(types["job_type"])

    return list(set(all_types))


def filter_by_job_type(jobs, job_type):
    job = []

    for v in jobs:
        if job_type in v.values():
            job.append(v)

    return job


def get_unique_industries(path):
    all_jobs = read(path)
    all_industries = []
    for types in all_jobs:
        if types["industry"] != '':
            all_industries.append(types["industry"])

    return list(set(all_industries))


def filter_by_industry(jobs, industry):
    job = []

    for v in jobs:
        if industry in v.values():
            job.append(v)

    return job


def get_max_salary(path):
    all_jobs = read(path)
    salary = []
    for types in all_jobs:
        if types["max_salary"] != '' and types["max_salary"].isnumeric():
            i = int(types["max_salary"])
            salary.append(i)

    pass
    return max(salary)


def get_min_salary(path):
    all_jobs = read(path)
    salary = []
    for types in all_jobs:
        if types["min_salary"] != '' and types["min_salary"].isnumeric():
            i = int(types["min_salary"])
            salary.append(i)

    pass
    return min(salary)


def matches_salary_range(job, salary):

    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError
    if type(job["min_salary"]) != int or type(job["max_salary"]) != int:
        raise ValueError
    if job["min_salary"] > job["max_salary"]:
        raise ValueError
    if type(salary) != int:
        raise ValueError

    return job["min_salary"] <= salary <= job["max_salary"]


def filter_by_salary_range(jobs, salary):
    match_jobs = []

    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                match_jobs.append(job)
        except ValueError:
            ValueError

    return match_jobs
