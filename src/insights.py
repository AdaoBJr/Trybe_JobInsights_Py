from src.jobs import read


def get_unique_job_types(path):
    jobs = read(path)
    job_types = set()
    for job in jobs:
        job_types.add(job["job_type"])
    return job_types


def get_unique_industries(path):
    jobs = read(path)
    industries = set()
    for job in jobs:
        if job["industry"] != "":
            industries.add(job["industry"])
    return industries


def get_max_salary(path):
    jobs = read(path)
    max_salary = [int(job["max_salary"])
                  for job in jobs
                  if job["max_salary"] != ""
                  and job["max_salary"].isnumeric()]
    return max(max_salary)
# source func isNumeric() / max() ->
# https://acervolima.com/python-string-isnumeric-e-sua-aplicacao/
# https://acervolima.com/python-funcao-max/


def get_min_salary(path):
    jobs = read(path)
    min_salary = [int(job["min_salary"])
                  for job in jobs
                  if job["min_salary"] != ""
                  and job["min_salary"].isnumeric()]
    return min(min_salary)
# source func isNumeric() / min() ->
# https://acervolima.com/python-string-isnumeric-e-sua-aplicacao/
# https://acervolima.com/python-funcao-min/


def filter_by_job_type(jobs, job_type):
    filter_jobs = [job
                   for job in jobs
                   if job["job_type"] == job_type]
    return filter_jobs


def filter_by_industry(jobs, industry):
    filter_industry = [job
                       for job in jobs
                       if job["industry"] == industry]
    return filter_industry


def matches_salary_range(job, salary):
    min_salary = job.get("min_salary")
    max_salary = job.get("max_salary")

    if (
        type(salary) != int
        or type(min_salary) != int
        or type(max_salary) != int
        or min_salary > max_salary
    ):
        raise ValueError
    return min_salary <= salary <= max_salary


def filter_by_salary_range(jobs, salary):
    jobs_filter = []

    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                jobs_filter.append(job)
        except ValueError:
            pass
    return jobs_filter
