# import jobs
from src import jobs


def get_unique_job_types(path):
    jobs_list = jobs.read(path)
    types = set()
    for job in jobs_list:
        if job['job_type'] != "":
            types.add(job['job_type'])
    return types


def filter_by_job_type(jobs, job_type):
    return [job for job in jobs if job["job_type"] == job_type]


def get_unique_industries(path):
    jobs_list = jobs.read(path)
    industrys = set()
    for job in jobs_list:
        if job['industry'] != "":
            industrys.add(job["industry"])
    return industrys


def filter_by_industry(jobs, industry):
    return [job for job in jobs if job["industry"] == industry]


def get_max_salary(path):
    jobs_list = jobs.read(path)
    max_salarys = set()
    for job in jobs_list:
        if job['max_salary'] != '' and job['max_salary'].isnumeric():
            max_salarys.add(int(job['max_salary']))
    max_salary = max(max_salarys)
    return max_salary


def get_min_salary(path):
    jobs_list = jobs.read(path)
    min_salarys = set()
    for job in jobs_list:
        if job['min_salary'] != '' and job['min_salary'].isnumeric():
            min_salarys.add(int(job['min_salary']))
    min_salary = min(min_salarys)
    return min_salary


def matches_salary_range(job, salary):
    try:
        if type(salary) != int:
            raise ValueError(
                "Salary deve ser um inteiro"
            )
        if job["min_salary"] > job["max_salary"]:
            raise ValueError("Salario minimo deve ser menor que salario máximo")

        return job["min_salary"] <= salary <= job["max_salary"]

    except Exception:
        raise ValueError("Salary deve ser um inteiro")


def filter_by_salary_range(jobs, salary):
    salary_range = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                salary_range.append(job)
        except ValueError:
            pass
    return salary_range
