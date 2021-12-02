from src.jobs import read


def get_unique_job_types(path):
    data = read(path)
    lista = set()
    for row in data:
        lista.add(row["job_type"])
    return lista


def filter_by_job_type(jobs, job_type):
    list_job = []
    for job in jobs:
        if job["job_type"] == job_type:
            list_job.append(job)
    return list_job


def get_unique_industries(path):
    data = read(path)
    lista = set()
    for row in data:
        if row["industry"]:
            lista.add(row["industry"])
    return lista


def filter_by_industry(jobs, industry):
    list_industry = []
    for job in jobs:
        if job["industry"] == industry:
            list_industry.append(job)
    return list_industry


def get_max_salary(path):
    data = read(path)

    max_salaries = []

    for salary in data:
        if salary["max_salary"].isnumeric():
            max_salaries.append(int(salary["max_salary"]))

    return max(max_salaries)


def get_min_salary(path):
    data = read(path)

    min_salaries = []

    for salary in data:
        if salary["min_salary"].isnumeric():
            min_salaries.append(int(salary["min_salary"]))
    return min(min_salaries)


def valid_key(job):
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError("doesn't exists")


def matches_salary_range(job, salary):
    valid_key(job)

    min_salary = job["min_salary"]
    max_salary = job["max_salary"]

    if not isinstance(min_salary, int) or not isinstance(max_salary, int):
        raise ValueError("aren't valid integers")
    if min_salary > max_salary:
        raise ValueError("is greather")
    if not isinstance(salary, int):
        raise ValueError("aaaaaaaa")

    if max_salary >= salary >= min_salary:
        return True
    else:
        return False


def filter_by_salary_range(jobs, salary):
    list_job = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                list_job.append(job)
        except ValueError:
            pass
    return list_job
