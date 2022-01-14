from src.jobs import read
# from jobs import read


def get_unique_job_types(path):

    job_list = read(path)
    job_types = set()
    for job in job_list:
        job_types.add(job["job_type"])
    return job_types


def filter_by_job_type(jobs, job_type):

    jobsFilter = []
    for job in jobs:
        if job["job_type"] == job_type:
            jobsFilter.append(job)
    return jobsFilter


def get_unique_industries(path):

    job_list = read(path)
    industries = set()
    for job in job_list:
        if job["industry"] != "":
            industries.add(job["industry"])
    return industries


def filter_by_industry(jobs, industry):

    industryFilter = []
    for job in jobs:
        if job["industry"] == industry:
            industryFilter.append(job)
    return industryFilter


def get_max_salary(path):

    job_list = read(path)
    # salaries = set()
    max_salary = 0
    for job in job_list:
        try:
            if job["max_salary"] != "" and int(job["max_salary"]) > max_salary:
                max_salary = int(job["max_salary"])
        except(ValueError):
            print(ValueError)

    return max_salary


def get_first_valid_salary(job_list):
    min_salary = 0
    for job in job_list:
        try:
            if job["min_salary"] != "":
                min_salary = int(job["min_salary"])
                break
        except(ValueError):
            print(ValueError)
    return min_salary


def get_min_salary(path):
    job_list = read(path)
    min_salary = get_first_valid_salary(job_list)
    for job in job_list:
        try:
            if job["min_salary"] != "" and int(job["min_salary"]) < min_salary:
                min_salary = int(job["min_salary"])
        except(ValueError):
            print(ValueError)

    return min_salary


def matches_salary_range(job, salary):
    if("min_salary" not in job or "max_salary" not in job):
        raise ValueError

    if(type(job["min_salary"]) != int or type(job["max_salary"]) != int):
        raise ValueError

    if(job["min_salary"] > job["max_salary"]):
        raise ValueError

    if(type(salary) != int):
        raise ValueError

    return job["min_salary"] <= salary <= job["max_salary"]


def filter_by_salary_range(jobs, salary):
    jobsFilter = []
    for job in jobs:
        try:
            if(matches_salary_range(job, salary) is False):
                continue
            jobsFilter.append(job)
        except(ValueError):
            continue
    return jobsFilter
