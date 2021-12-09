from src.jobs import read


def get_unique_job_types(path):
    jobs_data = read(path)
    types = set()
    for job in jobs_data:
        types.add(job["job_type"])
    return types


def filter_by_job_type(jobs, job_type):
    return [job for job in jobs if job["job_type"] == job_type]


def get_unique_industries(path):
    jobs_data = read(path)
    industries = set()
    for industry in jobs_data:
        if industry["industry"] != "":
            industries.add(industry["industry"])
    return industries


def filter_by_industry(jobs, industry):
    return [ind for ind in jobs if ind["industry"] == industry]


def get_max_salary(path):
    jobs_data = read(path)
    salary_info = set()
    for salary in jobs_data:
        if salary["max_salary"].isnumeric():
            salary_info.add(float(salary["max_salary"]))
    return max(salary_info)


def get_min_salary(path):
    jobs_data = read(path)
    salary_info = set()
    for salary in jobs_data:
        if salary["min_salary"].isnumeric():
            salary_info.add(float(salary["min_salary"]))
    return min(salary_info)


def matches_salary_range(job, salary):
    if (
        "min_salary" not in job
        or "max_salary" not in job
        or type(job["min_salary"]) != int
        or type(job["max_salary"]) != int
        or type(salary) != int
        or int(job["min_salary"]) > int(job["max_salary"])
    ):
        raise ValueError
    else:
        return int(job["min_salary"]) <= int(salary) <= int(job["max_salary"])


def filter_by_salary_range(jobs, salary):
    salaries_in_range = []
    for job_salary in jobs:
        try:
            if matches_salary_range(job_salary, salary):
                salaries_in_range.append(job_salary)
        except ValueError:
            pass
    return salaries_in_range
