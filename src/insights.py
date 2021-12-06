from src.jobs import read


def get_unique_job_types(path):
    read_file = read(path)
    job_types = set()
    for job in read_file:
        job_types.add(job["job_type"])
    return job_types


def filter_by_job_type(jobs, job_type):
    return [job for job in jobs if job["job_type"] == job_type]


def get_unique_industries(path):
    read_file = read(path)
    industries = set()
    for industry in read_file:
        if industry["industry"] != "":
            industries.add(industry["industry"])
    return industries


def filter_by_industry(jobs, industry):
    return [job for job in jobs if job["industry"] == industry]


def get_max_salary(path):
    read_file = read(path)
    salary = 0
    for work in read_file:
        if work["max_salary"].isnumeric() and int(work["max_salary"]) > salary:
            salary = int(work["max_salary"])
    return salary


def get_min_salary(path):
    read_file = read(path)
    salary = []
    for work in read_file:
        if work["min_salary"] != "":
            try:
                salary.append(int(work["min_salary"]))
            except ValueError:
                pass
    return min(salary)


def matches_salary_range(job, salary):
    if not (
        "max_salary" not in job
        or "min_salary" not in job
        or type(job["min_salary"]) != int
        or type(job["max_salary"]) != int
        or type(salary) != int
        or job["min_salary"] > job["max_salary"]
    ):
        return job["min_salary"] <= salary <= job["max_salary"]
    raise ValueError


def filter_by_salary_range(jobs, salary):
    salary = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                salary.append(job)
        except ValueError:
            pass
    return salary
