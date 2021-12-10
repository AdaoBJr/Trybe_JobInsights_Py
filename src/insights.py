from src.jobs import read


def get_unique_job_types(path):
    jobs = read(path)
    job_types = []
    for job in jobs:
        if job["job_type"] not in job_types:
            job_types.append(job["job_type"])
    return job_types


def filter_by_job_type(jobs, job_type):
    filter_job = []
    for element in jobs:
        if element["job_type"] == job_type:
            filter_job.append(element)
    return filter_job


def get_unique_industries(path):
    jobs = read(path)
    industries = set()
    for element in jobs:
        if element["industry"] not in industries:
            industries.add(element["industry"])
    return industries


def filter_by_industry(jobs, industry):
    filter_industry = []
    for element in jobs:
        if element["job_type"] == industry:
            filter_industry.append(element)
    return filter_industry


def get_max_salary(path):
    jobs = read(path)
    max_salary = []
    for element in jobs:
        if element["max_salary"] != "invalid" and element["max_salary"] != "":
            max_salary.append(int(element["max_salary"]))
    return max(max_salary)


def get_min_salary(path):
    jobs = read(path)
    min_salary = []
    for element in jobs:
        if element["min_salary"] != "invalid" and element["min_salary"] != "":
            min_salary.append(int(element["min_salary"]))
    return min(min_salary)


def matches_salary_range(job, salary):
    if (
        "max_salary" not in job
        or "min_salary" not in job
        or type(job["max_salary"]) is not int
        or type(job["min_salary"]) is not int
        or job["min_salary"] > job["max_salary"]
        or type(salary) is not int
    ):
        raise ValueError("Not salary range")
    if salary >= job["min_salary"] and salary <= job["max_salary"]:
        return True
    else:
        return False


def filter_by_salary_range(jobs, salary):

    return []
