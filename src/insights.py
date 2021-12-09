from src.jobs import read


def get_unique_job_types(path):
    jobs = read(path)
    jobs_types = set()
    for job in jobs:
        jobs_types.add(job["job_type"])

    return jobs_types


def filter_by_job_type(jobs, job_type):
    filter_jobs_type = [job for job in jobs if job["job_type"] == job_type]
    return filter_jobs_type


def get_unique_industries(path):
    jobs = read(path)
    industry_type = set()
    for industry in jobs:
        if industry["industry"] != "":
            industry_type.add(industry["industry"])

    return industry_type


def filter_by_industry(jobs, industry):
    filter_industry_type = [job for job in jobs if job["industry"] == industry]
    return filter_industry_type


def get_max_salary(path):
    jobs = read(path)
    salary_jobs = set()
    for job in jobs:
        if job["max_salary"] != "" and job["max_salary"].isnumeric():
            salary_jobs.add(int(job["max_salary"]))

    return max(salary_jobs)


def get_min_salary(path):
    jobs = read(path)
    salary_jobs = set()
    for job in jobs:
        if job["min_salary"] != "" and job["min_salary"].isnumeric():
            salary_jobs.add(int(job["min_salary"]))

    return min(salary_jobs)


# Ajuda de Eder Paiva
def matches_salary_range(job, salary):
    try:
        if type(salary) != int:
            raise ValueError

        if job["min_salary"] > job["max_salary"]:
            raise ValueError

        return job["min_salary"] <= salary <= job["max_salary"]

    except Exception:
        raise ValueError


def filter_by_salary_range(jobs, salary):
    filter_salary = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                filter_salary.append(job)
        except ValueError:
            pass

    return filter_salary
