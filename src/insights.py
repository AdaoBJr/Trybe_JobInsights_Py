from .jobs import read

# ME AUXILIEI NO CÓDIGO DE RAPHAEL GUMIERI TURMA 10 - B


def get_unique_job_types(path):
    job_types = set()
    jobs_file = read(path)
    for job in jobs_file:
        job_types.add(job["job_type"])
    return job_types


def filter_by_job_type(jobs, job_type):
    filtered_list = list()
    for job in jobs:
        if job["job_type"] == job_type:
            filtered_list.append(job)
    return filtered_list


def get_unique_industries(path):
    industries_set = set()
    jobs_file = read(path)
    for job in jobs_file:
        if job["industry"] != "":
            industries_set.add(job["industry"])
    return industries_set


def filter_by_industry(jobs, industry):
    industries_list = list()
    for job in jobs:
        if job["industry"] == industry:
            industries_list.append(job)
    return industries_list


def get_max_salary(path):
    max_salaries = set()
    jobs_file = read(path)
    for job in jobs_file:
        if job["max_salary"].isnumeric():
            max_salaries.add(int(job["max_salary"]))
    return max(list(max_salaries))


def get_min_salary(path):
    min_salaries = list()
    jobs_file = read(path)
    for job in jobs_file:
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
        raise ValueError("Um ou vários inputs estão errados")

    if job["min_salary"] <= salary <= job["max_salary"]:
        return True
    else:
        return False


def filter_by_salary_range(jobs, salary):
    filtered_list = list()
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                filtered_list.append(job)
        except ValueError:
            pass
    return filtered_list
