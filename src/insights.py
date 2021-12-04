from src.jobs import read


def get_unique_job_types(path):
    dict_from_jobs = read(path)
    jobs_types = set()
    for job in dict_from_jobs:
        jobs_types.add(job["job_type"])
    return jobs_types


def filter_by_job_type(jobs, job_type):
    filter_job_type = []
    for job in jobs:
        if job["job_type"] == job_type:
            filter_job_type.append(job)
    return filter_job_type


def get_unique_industries(path):
    dict_from_jobs = read(path)
    list_of_industries = set()
    for industry in dict_from_jobs:
        if industry["industry"]:
            list_of_industries.add(industry["industry"])
    return list_of_industries


def filter_by_industry(jobs, industry):
    industries = []
    for job in jobs:
        if job["industry"] == industry:
            industries.append(job)
    return industries


def get_max_salary(path):
    dict_from_jobs = read(path)
    max_salary = 0
    for job in dict_from_jobs:
        if(
            job["max_salary"].isnumeric()
            and int(job["max_salary"]) > max_salary
        ):
            max_salary = int(job["max_salary"])
    return max_salary


def get_min_salary(path):
    dict_from_jobs = read(path)
    min_salary = []
    for job in dict_from_jobs:
        if job["min_salary"] != "" and job["min_salary"] != "invalid":
            min_salary.append(int(job["min_salary"]))
    return min(min_salary)


def matches_salary_range(job, salary):
    if (
        "min_salary" not in job
        or "max_salary" not in job
        or not isinstance(job["min_salary"], int)
        or not isinstance(job["max_salary"], int)
        or job["min_salary"] > job["max_salary"]
        or not isinstance(job["min_salary"], int)
        or not isinstance(salary, int)
    ):
        raise ValueError("Job doesn't have a salary range")
    if salary >= job["min_salary"] and salary <= job["max_salary"]:
        return True
    else:
        return False


def filter_by_salary_range(jobs, salary):
    filter_salary = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                filter_salary.append(job)
        except ValueError:
            pass
    return filter_salary


if __name__ == "__main__":
    print(get_unique_job_types("src/jobs.csv"))
    print(get_min_salary("src/jobs.csv"))
