import src.jobs


def get_unique_job_types(path):
    new_data = src.jobs.read(path)
    list_unique_job_types = set()
    for new_job in new_data:
        list_unique_job_types.add(new_job["job_type"])
    return list_unique_job_types


def filter_by_job_type(jobs, job_type):
    list_jobs = []
    for new_job in jobs:
        if new_job["job_type"] == job_type:
            list_jobs.append(new_job)
    return list_jobs


def get_unique_industries(path):
    new_data = src.jobs.read(path)
    list_unique_industries = set()
    for industry in new_data:
        if industry["industry"] != "":
            list_unique_industries.add(industry["industry"])
    return list_unique_industries


def filter_by_industry(jobs, industry):
    list_industry = []
    for job_industry in jobs:
        if job_industry["industry"] == industry:
            list_industry.append(job_industry)
    return list_industry


def get_max_salary(path):
    new_data = src.jobs.read(path)
    list_max_salary = set()
    for salary in new_data:
        if salary["max_salary"].isnumeric():
            list_max_salary.add(int(salary["max_salary"]))
    return max(list_max_salary)


def get_min_salary(path):
    new_data = src.jobs.read(path)
    list_min_salary = set()
    for salary in new_data:
        if salary["min_salary"].isnumeric():
            list_min_salary.add(int(salary["min_salary"]))
    return min(list_min_salary)


def matches_salary_range(job, salary):
    if (
        "min_salary" not in job
        or "max_salary" not in job
        or type(job["min_salary"]) != int
        or type(job["max_salary"]) != int
        or type(salary) != int
        or job["min_salary"] > job["max_salary"]
    ):
        raise ValueError("Algo deu erro")

    elif job["min_salary"] <= salary <= job["max_salary"]:
        return True
    else:
        return False


def filter_by_salary_range(jobs, salary):
    new_jobs = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                new_jobs.append(job)
        except ValueError:
            print("Algo deu error")
    return new_jobs
