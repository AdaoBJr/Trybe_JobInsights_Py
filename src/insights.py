from src.jobs import read


def get_unique_job_types(path):
    dictJobs = read(path)
    types = set()
    for row in dictJobs:
        types.add(row["job_type"])
    return types


def filter_by_job_type(jobs, job_type):
    listaJobs = []
    for job in jobs:
        if job["job_type"] == job_type:
            listaJobs.append(job)
    return listaJobs


def get_unique_industries(path):
    dictJobs = read(path)
    industries = set()
    for row in dictJobs:
        if row["industry"]:
            industries.add(row["industry"])
    return industries


def filter_by_industry(jobs, industry):
    listIndustries = []
    for job in jobs:
        if job["industry"] == industry:
            listIndustries.append(job)

    return listIndustries


def get_max_salary(path):
    dictJobs = read(path)
    listSalary = []
    for row in dictJobs:
        if row["max_salary"].isnumeric():
            listSalary.append(int(row["max_salary"]))

    result = max(listSalary)
    return result


def get_min_salary(path):
    dictJobs = read(path)
    listSalary = []
    for row in dictJobs:
        if row["min_salary"].isnumeric():
            listSalary.append(int(row["min_salary"]))

    result = min(listSalary)
    return result


def matches_salary_range(job, salary):
    if "max_salary" not in job or "min_salary" not in job:
        raise ValueError()
    salary_test = isinstance(salary, int)
    max_test = isinstance(job["max_salary"], int)
    min_test = isinstance(job["min_salary"], int)
    if not salary_test or not max_test or not min_test:
        raise ValueError()
    elif job["max_salary"] < job["min_salary"]:
        raise ValueError()

    if job['min_salary'] <= salary <= job['max_salary']:
        return True
    return False


def filter_by_salary_range(jobs, salary):
    listaSalario = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                listaSalario.append(job)
        except ValueError:
            pass

    return listaSalario
