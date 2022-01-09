from src.jobs import read

def get_unique_job_types(path):
    read_file = read(path)
    unique_job_types = []
    for row in read_file:
        if row["job_type"] not in unique_job_types and row["job_type"] != "":
            unique_job_types.append(row["job_type"])
    return unique_job_types


def filter_by_job_type(jobs, job_type):
    job_type_filtered = []
    for row in jobs:
        if row["job_type"] == job_type:
            job_type_filtered.append(row)
    return job_type_filtered


def get_unique_industries(path):
    read_file = read(path)
    unique_industries = []
    for row in read_file:
        if row["industry"] not in unique_industries and row["industry"] != "":
            unique_industries.append(row["industry"])
    return unique_industries


def filter_by_industry(jobs, industry):
    industries_filtered = []
    for row in jobs:
        if row["industry"] == industry:
            industries_filtered.append(row)
    return industries_filtered


def get_max_salary(path):
    read_file = read(path)
    max_salary = []
    for row in read_file:
        if row["max_salary"] != "" and row["max_salary"].isdigit():
            max_salary.append(int(row["max_salary"]))
    return max(max_salary)


def get_min_salary(path):
    read_file = read(path)
    min_salary = []
    for row in read_file:
        if row["min_salary"] != "" and row["min_salary"].isdigit():
            min_salary.append(int(row["min_salary"]))
    return min(min_salary)


def matches_salary_range(job, salary):
    if type(salary) is not int:
        raise ValueError("Salary isn't a valid integer")
    if not ("min_salary" in job and "max_salary" in job):
        raise ValueError("min_salary or max_salary doesn't exists")
    if (
        type(job["min_salary"]) is not int
        or type(job["max_salary"]) is not int
    ):
        raise ValueError("min_salary or max_salary aren't valid integers")
    if job["min_salary"] > job["max_salary"]:
        raise ValueError("min_salary is greather than max_salary")

    return job["min_salary"] <= salary <= job["max_salary"]


def filter_by_salary_range(jobs, salary):
    salary_range = []
    for row in jobs:
        try:
            if matches_salary_range(row, salary):
                salary_range.append(row)
        except ValueError:
            pass

    return salary_range
