from src.jobs import read


def get_unique_job_types(path):
    data = read(path)
    jobs_set = set()
    for jobs in data:
        jobs_set.add(jobs["job_type"])

    return list(jobs_set)


def filter_by_job_type(jobs, job_type):
    filtered_jobs = []
    for job in jobs:
        if job["job_type"] == job_type:
            filtered_jobs.append(job)

    return filtered_jobs


def get_unique_industries(path):
    data = read(path)
    industries_set = set()
    for industry in data:
        if industry["industry"] != '':
            industries_set.add(industry["industry"])

    return list(industries_set)


def filter_by_industry(jobs, industry):
    filtered_industry = []
    for ind in jobs:
        if ind["industry"] == industry:
            filtered_industry.append(ind)

    return filtered_industry


def get_max_salary(path):
    data = read(path)
    maximum = []
    for max_sal in data:
        if max_sal["max_salary"] != '' and max_sal["max_salary"] != 'invalid':
            salary = max_sal["max_salary"]
            maximum.append(int(salary))
    maximum.sort()
    return maximum[len(maximum) - 1]


def get_min_salary(path):
    data = read(path)
    minimun = []
    for min_sal in data:
        if min_sal["min_salary"] != '' and min_sal["min_salary"] != 'invalid':
            salary = min_sal["min_salary"]
            minimun.append(int(salary))
    minimun.sort()
    return minimun[0]


def matches_salary_range(job, salary):
    if (
        "min_salary" not in job or "max_salary" not in job
        or not isinstance(job["min_salary"], int)
        or not isinstance(job["max_salary"], int)
        or job["min_salary"] > job["max_salary"]
        or not isinstance(salary, int)
    ):
        raise ValueError("Job doesn't have a salary range")

    if salary >= job["min_salary"] and salary <= job["max_salary"]:
        return True
    else:
        return False


def filter_by_salary_range(jobs, salary):
    jobs_filtered = []

    for range in jobs:
        try:
            is_valid = matches_salary_range(range, salary)
            if is_valid:
                jobs_filtered.append(range)
        except ValueError:
            print("Erro")
    return jobs_filtered
