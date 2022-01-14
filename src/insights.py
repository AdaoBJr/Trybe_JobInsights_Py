from src.jobs import read


def get_unique_job_types(path):
    data = read(path)
    job_types = list()

    for job in data:
        if job["job_type"] and job["job_type"] not in job_types:
            job_types.append(job["job_type"])

    return job_types


def filter_by_job_type(jobs, job_type):
    filtered_job = []
    for job in jobs:
        if job["job_type"] == job_type:
            filtered_job.append(job)

    return filtered_job


def get_unique_industries(path):
    data = read(path)
    industries = []
    for job in data:
        if job["industry"] and job["industry"] not in industries:
            industries.append(job["industry"])

    return industries


def filter_by_industry(jobs, industry):
    filtered_industry = []

    for job in jobs:
        if job["industry"] == industry:
            filtered_industry.append(job)

    return filtered_industry


def get_max_salary(path):
    data = read(path)
    salaries = []

    for job in data:
        if (
            job["max_salary"].isdigit()
            and int(job["max_salary"]) not in salaries
        ):
            salaries.append(int(job["max_salary"]))

    return max(salaries)


def get_min_salary(path):
    data = read(path)
    salaries = []

    for job in data:
        if (
            job["min_salary"].isdigit()
            and int(job["min_salary"]) not in salaries
        ):
            salaries.append(int(job["min_salary"]))

    return min(salaries)


def matches_salary_range(job, salary):
    if "min_salary" not in job.keys() or "max_salary" not in job.keys():
        raise ValueError("min_salary or max_salary doesn't exists")
    if (
        type(job["min_salary"]) != int
        or type(job["max_salary"]) != int
        or type(salary) != int
    ):
        raise ValueError("min_salary, max_salary or salary aren't integers")
    if job["min_salary"] > job["max_salary"]:
        raise ValueError("min_salary is greater than max_salary")
    if job["min_salary"] <= salary <= job["max_salary"]:
        return True
    else:
        return False


def filter_by_salary_range(jobs, salary):
    filtered_by_salary_range = []
    for job in jobs:
        if job["min_salary"] > job["max_salary"] or type(salary) != int:
            pass
        elif job["min_salary"] <= salary <= job["max_salary"]:
            filtered_by_salary_range.append(job)
    return filtered_by_salary_range
