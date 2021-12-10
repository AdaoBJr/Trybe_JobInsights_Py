from src.jobs import read


def get_unique_job_types(path):
    file = read(path)
    array = set()

    for row in file:
        array.add(row["job_type"])

    return array


def filter_by_job_type(jobs, job_type):
    result = []

    for row in jobs:
        if row["job_type"] == job_type:
            result.append(row)

    return result


def get_unique_industries(path):
    file = read(path)
    industries = set()

    for row in file:
        if row["industry"] != '':
            industries.add(row["industry"])
    return industries


def filter_by_industry(jobs, industry):
    result = []

    for row in jobs:
        if row["industry"] == industry:
            result.append(row)

    return result


def get_max_salary(path):
    file = read(path)
    salaries = []

    for row in file:
        if row["max_salary"].isnumeric() and row["max_salary"] != '':
            salaries.append(int(row["max_salary"]))
    return max(salaries)


def get_min_salary(path):
    file = read(path)
    salaries = []

    for row in file:
        if row["min_salary"].isnumeric() and row["min_salary"] != '':
            salaries.append(int(row["min_salary"]))
    return min(salaries)


def matches_salary_range(job, salary):
    if ("min_salary" or "max_salary") not in job:
        raise ValueError
    elif (type(job["min_salary"]) == str or type(job["max_salary"]) == str or
          type(salary) != int):
        raise ValueError
    elif (job["min_salary"] > job["max_salary"]):
        raise ValueError
    return job["min_salary"] <= salary <= job["max_salary"]


def filter_by_salary_range(jobs, salary):
    result = []
    for row in jobs:
        try:
            if matches_salary_range(row, salary):
                result.append(row)
        except ValueError:
            print("A experiência é o nome que damos aos nossos erros.")
    return result
