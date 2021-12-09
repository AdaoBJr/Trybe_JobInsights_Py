import src.jobs


def get_unique_job_types(path):
    all_jobs = src.jobs.read(path)
    job_types = []
    for job in all_jobs:
        if job["job_type"] not in job_types:
            job_types.append(job["job_type"])
    return job_types


def filter_by_job_type(jobs, job_type):
    filtered_jobs = []
    for job in jobs:
        if job["job_type"] == job_type:
            filtered_jobs.append(job)
    return filtered_jobs


def get_unique_industries(path):
    all_jobs = src.jobs.read(path)
    industry = set()
    for job in all_jobs:
        if job["industry"] != "":
            industry.add(job["industry"])
    return industry


def filter_by_industry(jobs, industry):
    filtered_industries = []
    for job in jobs:
        if job["industry"] == industry:
            filtered_industries.append(job)
    return filtered_industries


def get_max_salary(path):
    all_jobs = src.jobs.read(path)
    max_salary = []
    for job in all_jobs:
        if job["max_salary"] != "" and job["max_salary"] != "invalid":
            max_salary.append(int(job["max_salary"]))
    return max(max_salary)


def get_min_salary(path):
    all_jobs = src.jobs.read(path)
    min_salary = []
    for job in all_jobs:
        if job["min_salary"] != "" and job["min_salary"] != "invalid":
            min_salary.append(int(job["min_salary"]))
    return min(min_salary)


def matches_salary_range(job, salary):  # Agradecimento ao amigo Rafael Mathias
    if (
        "min_salary" not in job
        or "max_salary" not in job
        or not isinstance(job["min_salary"], int)
        or not isinstance(job["max_salary"], int)
        or job["min_salary"] > job["max_salary"]
        or not isinstance(salary, int)
    ):
        raise ValueError("Not salary range!")
    if salary >= job["min_salary"] and salary <= job["max_salary"]:
        return True
    else:
        return False


def filter_by_salary_range(jobs, salary):  # Agradecimento ao Rafael Mathias
    filtered_salary_range = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                filtered_salary_range.append(job)
        except ValueError:
            print("Not salary range!")
    return filtered_salary_range
