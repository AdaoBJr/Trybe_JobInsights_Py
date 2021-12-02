from src.jobs import read


def get_unique_job_types(path):
    list = read(path)
    jobs = set()  # set of unique job types
    for job in list:
        jobs.add(job["job_type"])
    return jobs


def filter_by_job_type(jobs, job_type):
    list = []
    for job in jobs:
        if job["job_type"] == job_type:
            list.append(job)
    return list


def get_unique_industries(path):
    list = read(path)
    industries = set()  # set of unique industries
    for industry in list:
        if industry["industry"]:
            industries.add(industry["industry"])
    return industries


def filter_by_industry(jobs, industry):
    list = []
    for job in jobs:
        if job["industry"] == industry:
            list.append(job)
    return list


# https://docs.python.org/3/library/stdtypes.html#str.isnumeric


def get_max_salary(path):
    list = read(path)
    max_salary = 0
    for job in list:
        if (
            job["max_salary"].isnumeric()
            and int(job["max_salary"]) > max_salary
        ):
            max_salary = int(job["max_salary"])
    return max_salary


def get_min_salary(path):
    list = read(path)
    min_salary = 9999999999
    for job in list:
        if (
            job["min_salary"].isnumeric()
            and int(job["min_salary"]) < min_salary
        ):
            min_salary = int(job["min_salary"])
    return min_salary


# https://stackoverflow.com/questions/1602934/check-if-a-given-key-already-exists-in-a-dictionary


def matches_salary_range(job, salary):
    if (
        "min_salary" not in job
        or "max_salary" not in job
        or type(job["min_salary"]) != int
        or type(job["max_salary"]) != int
        or type(salary) != int
        or job["min_salary"] > job["max_salary"]
    ):
        raise ValueError
    return job["min_salary"] <= salary <= job["max_salary"]


def filter_by_salary_range(jobs, salary):
    list = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                list.append(job)
        except ValueError:
            pass
    return list
