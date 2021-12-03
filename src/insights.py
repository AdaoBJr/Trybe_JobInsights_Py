from src import jobs


def get_unique_job_types(path):
    all_jobs = jobs.read(path)
    job_types = []

    for job in all_jobs:
        if job["job_type"] not in job_types:
            job_types.append(job["job_type"])

    return job_types


def filter_by_job_type(jobs, job_type):
    jobs_filtered_by_type = []

    for job in jobs:
        if job["job_type"] == job_type:
            jobs_filtered_by_type.append(job)

    return jobs_filtered_by_type


def get_unique_industries(path):
    all_jobs = jobs.read(path)
    job_industries = []

    for job in all_jobs:
        if job["industry"] not in job_industries and job["industry"]:
            job_industries.append(job["industry"])

    return job_industries


def filter_by_industry(jobs, industry):
    jobs_filtered_by_industry = []

    for job in jobs:
        if job["industry"] == industry:
            jobs_filtered_by_industry.append(job)

    return jobs_filtered_by_industry


def get_max_salary(path):
    all_jobs = jobs.read(path)
    max_salary = 0

    for job in all_jobs:
        if (
            job["max_salary"].isnumeric()
            and int(job["max_salary"]) > max_salary
        ):
            max_salary = int(job["max_salary"])

    return max_salary


def get_min_salary(path):
    all_jobs = jobs.read(path)
    min_salary = 0

    for job in all_jobs:
        if job["min_salary"].isnumeric():
            min_salary = int(job["min_salary"])
            break

    for job in all_jobs:
        if (
            job["min_salary"].isnumeric()
            and int(job["min_salary"]) < min_salary
        ):
            min_salary = int(job["min_salary"])

    return min_salary


def matches_salary_range(job, salary):
    if (
        "min_salary" not in job
        or "max_salary" not in job
        or type(job["min_salary"]) != int
        and type(job["min_salary"]) != float
        or type(job["max_salary"]) != int
        and type(job["max_salary"]) != float
        or job["min_salary"] > job["max_salary"]
        or (type(salary) != int and type(salary) != float)
    ):
        raise ValueError

    is_in_range = False
    minimum = job["min_salary"]
    maximum = job["max_salary"]

    for each_in_min_max in list(range(minimum, maximum + 1)):
        if each_in_min_max == salary:
            is_in_range = True
    return is_in_range


def filter_by_salary_range(jobs, salary):
    jobs_filtered_by_salary = []

    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                jobs_filtered_by_salary.append(job)
        except ValueError:
            print("Valores inválidos foram inseridos")

    return jobs_filtered_by_salary
