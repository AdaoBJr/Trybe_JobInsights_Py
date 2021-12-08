from src.jobs import read
# from jobs import read


def get_unique_job_types(path):
    job_types = set()
    read_path = read(path)
    for job in read_path:
        job_types.add(job["job_type"])

    return job_types


def filter_by_job_type(jobs, job_type):
    def condition(jobs):
        if jobs["job_type"] == job_type:
            return True
        else:
            return False

    job_filtered = list(filter(condition, jobs))

    return job_filtered


def get_unique_industries(path):
    industries = set()
    read_path = read(path)
    for industry in read_path:
        if industry["industry"] != '':
            industries.add(industry["industry"])

    return industries


def filter_by_industry(jobs, industry):
    def condition(jobs):
        if jobs["industry"] == industry:
            return True
        else:
            return False

    jobs_filtered = list(filter(condition, jobs))

    return jobs_filtered


def get_max_salary(path):
    read_path = read(path)
    salary_list = []
    for salary in read_path:
        if salary["max_salary"].isnumeric():
            convertInNumber = int(salary["max_salary"], base=10)
            salary_list.append(convertInNumber)

    highest_salary = max(salary_list)
    return highest_salary


def get_min_salary(path):
    read_path = read(path)
    salary_list = []
    for salary in read_path:
        if salary["min_salary"].isnumeric():
            salary_list.append(int(salary["min_salary"]))

    lowest_salary = min(salary_list)
    return lowest_salary


def matches_salary_range(job, salary):
    if (
        "min_salary" not in job
        or "max_salary" not in job
        or type(job["min_salary"]) != int
        or type(job["max_salary"]) != int
        or job["min_salary"] > job["max_salary"]
        or type(salary) != int
    ):
        raise ValueError("Invalid value")

    elif job["min_salary"] <= salary <= job["max_salary"]:
        return True
    else:
        return False


def filter_by_salary_range(jobs, salary):
    result = []
    for job in jobs:
        if (
            type(job["min_salary"]) == int
            and type(job["max_salary"]) == int
            and job["max_salary"] > job["min_salary"]
            and type(salary) == int
        ):
            if matches_salary_range(job, salary):
                result.append(job)

    return result
