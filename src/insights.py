from .jobs import read


def get_unique_job_types(path):
    jobs_type = []
    jobs_unique_types = []
    result_jobs = read(path)
    for jobs in result_jobs:
        if jobs["job_type"] != "":
            jobs_type.append(jobs["job_type"])
    for jobs_unique in jobs_type:
        if jobs_unique not in jobs_unique_types:
            jobs_unique_types.append(jobs_unique)
    return jobs_unique_types


def filter_by_job_type(jobs, job_type):
    filter_job_types = []
    for job in jobs:
        if job_type in job.values():
            filter_job_types.append(job)
    return filter_job_types


def get_unique_industries(path):
    result_industries = []
    unique_industries = []
    result_jobs = read(path)
    for jobs in result_jobs:
        if jobs["industry"] != "":
            result_industries.append(jobs["industry"])
    for industries in result_industries:
        if industries not in unique_industries:
            unique_industries.append(industries)
    return unique_industries


def filter_by_industry(jobs, industry):
    filter_job_industry = []
    for job in jobs:
        if industry in job.values():
            filter_job_industry.append(job)
    return filter_job_industry


def get_max_salary(path):
    salaries = []
    result_jobs = read(path)
    for jobs in result_jobs:
        if jobs["max_salary"] != "":
            if jobs["max_salary"].isdigit():
                salaries.append(int(jobs["max_salary"]))
    return max(salaries)


def get_min_salary(path):
    salaries = []
    result_jobs = read(path)
    for jobs in result_jobs:
        if jobs["min_salary"] != "":
            if jobs["min_salary"].isdigit():
                salaries.append(int(jobs["min_salary"]))
    return min(salaries)


def matches_salary_range(job, salary):
    if (
        "min_salary" not in job
        or "max_salary" not in job
        or type(job["min_salary"]) != int
        or type(job["max_salary"]) != int
        or type(salary) != int
        or job["min_salary"] > job["max_salary"]
    ):
        raise ValueError()
    elif salary >= job["min_salary"] and salary <= job["max_salary"]:
        return True
    else:
        return False


def filter_by_salary_range(jobs, salary):
    job_salary = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                job_salary.append(job)
        except ValueError:
            pass
    return job_salary
