from src.jobs import read


def get_unique_job_types(path):
    job_files = read(path)

    filtered_jobs = set()

    for job in job_files:
        filtered_jobs.add(job["job_type"])

    return filtered_jobs


def filter_by_job_type(jobs, job_type):
    filtered_jobs = []
    print(jobs)
    for job in jobs:
        if job["job_type"] == job_type:
            filtered_jobs.append(job)

    return filtered_jobs


def get_unique_industries(path):
    job_files = read(path)

    filtered_jobs = set()

    for job in job_files:
        if not job["industry"] == "":
            filtered_jobs.add(job["industry"])

    return filtered_jobs


def filter_by_industry(jobs, industry):
    filtered_jobs = []

    for job in jobs:
        if job["industry"] == industry:
            filtered_jobs.append(job)

    return filtered_jobs


def get_max_salary(path):
    jobs_files = read(path)

    max_salary = set()

    for job in jobs_files:
        if not (job["max_salary"] == "" or job["max_salary"] == "invalid"):
            max_salary.add(int(job["max_salary"]))

    return max(max_salary)


def get_min_salary(path):
    jobs_files = read(path)

    min_salary = set()

    for job in jobs_files:
        if not (job["min_salary"] == "" or job["min_salary"] == "invalid"):
            min_salary.add(int(job["min_salary"]))

    return min(min_salary)


def matches_salary_range(job, salary):
    if (
        "max_salary" not in job
        or "min_salary" not in job
        or type(job["min_salary"]) != int
        or type(job["max_salary"]) != int
        or job["min_salary"] > job["max_salary"]
        or type(salary) != int
    ):
        raise ValueError("Invalid input")

    if job["min_salary"] <= salary <= job["max_salary"]:
        return True

    return False


def filter_by_salary_range(jobs, salary):
    filtered_jobs = []

    for job in jobs:
        try:
            is_valid_salary = matches_salary_range(job, salary)
            if is_valid_salary is True:
                filtered_jobs.append(job)
        except ValueError:
            pass

    return filtered_jobs
