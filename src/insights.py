from src.jobs import read
from src.validations import (
    valid_keys_in_job,
    valid_min_and_max_is_integer,
    valid_min_is_greather_than_max,
    valid_salary_is_an_integer,
)


def get_unique_job_types(path):
    array_of_jobs = read(path)
    job_types = set()

    for item in array_of_jobs:
        job_types.add(item["job_type"])
    return job_types


def filter_by_job_type(jobs, job_type):
    jobs_result = []

    for item in jobs:
        if item["job_type"] == job_type:
            jobs_result.append(item)
    return jobs_result


def get_unique_industries(path):
    array_of_jobs = read(path)
    industries = set()

    for item in array_of_jobs:
        if item["industry"]:
            industries.add(item["industry"])
    return industries


def filter_by_industry(jobs, industry):
    jobs_result = []

    for item in jobs:
        if item["industry"] == industry:
            jobs_result.append(item)
    return jobs_result


def get_max_salary(path):
    array_of_jobs = read(path)
    salaries = []

    for item in array_of_jobs:
        if item["max_salary"].isnumeric():
            salaries.append(int(item["max_salary"]))
    return max(salaries)


def get_min_salary(path):
    array_of_jobs = read(path)
    salaries = []

    for item in array_of_jobs:
        if item["min_salary"].isnumeric():
            salaries.append(int(item["min_salary"]))
    return min(salaries)


def matches_salary_range(job, salary):

    valid_keys_in_job(job)
    valid_min_and_max_is_integer(job)
    valid_min_is_greather_than_max(job)
    valid_salary_is_an_integer(salary)

    if not (salary in range(int(job["min_salary"]), int(job["max_salary"]))):
        return False

    return True


def filter_by_salary_range(jobs, salary):
    list_of_jobs = []

    for item in jobs:
        try:
            if matches_salary_range(item, salary):
                list_of_jobs.append(item)
        except ValueError:
            pass

    return list_of_jobs
