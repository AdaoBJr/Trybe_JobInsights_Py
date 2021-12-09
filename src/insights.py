from src import jobs


def get_unique_job_types(path):
    jobs_list = jobs.read(path)
    types = set()
    for job in jobs_list:
        if job["job_type"] != "":
            types.add(job["job_type"])
    return types


def filter_by_job_type(jobs, job_type):
    jobs_type_list = []
    for job in jobs:
        if job["job_type"] == job_type:
            jobs_type_list.append(job)
    return jobs_type_list


def get_unique_industries(path):
    jobs_list = jobs.read(path)
    industries = set()
    for job in jobs_list:
        if job["industry"] != "":
            industries.add(job["industry"])
    return industries


def filter_by_industry(jobs, industry):
    industries_list = []
    for job in jobs:
        if job["industry"] == industry:
            industries_list.append(job)
    return industries_list


def get_max_salary(path):
    jobs_list = jobs.read(path)
    max_salaries = set()
    for job in jobs_list:
        if job["max_salary"] != "" and job["max_salary"].isnumeric():
            max_salaries.add(int(job["max_salary"]))
    max_salaries = max(max_salaries)
    return max_salaries


def get_min_salary(path):
    jobs_list = jobs.read(path)
    min_salaries = set()
    for job in jobs_list:
        if job["min_salary"] != "" and job["min_salary"].isnumeric():
            min_salaries.add(int(job["min_salary"]))
    min_salaries = min(min_salaries)
    return min_salaries


def matches_salary_range(job, salary):
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError("The keys min_salary or max_salary doesn't exists")

    elif (type(job["min_salary"]) == str or type(job["max_salary"]) == str or
          type(salary) != int):
        raise ValueError("min_salary or max_salary aren't valid integers")

    elif job["max_salary"] < job["min_salary"]:
        raise ValueError("min_salary is greather than max_salary")

    return job["min_salary"] <= salary <= job["max_salary"]


def filter_by_salary_range(jobs, salary):
    jobs_salary_range_list = []

    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                jobs_salary_range_list.append(job)
        except ValueError:
            pass
    return jobs_salary_range_list
