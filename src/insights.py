from src.jobs import read


def get_unique_job_types(path):
    content = read(path)
    return {item["job_type"] for item in content}


def filter_by_job_type(jobs, job_type):
    return [job for job in jobs if job["job_type"] == job_type]


def get_unique_industries(path):
    content = read(path)
    return {item["industry"] for item in content if item['industry']}


def filter_by_industry(jobs, industry):
    return [job for job in jobs if job["industry"] == industry]


def get_max_salary(path):
    content = read(path)
    return max(
        [
            int(item["max_salary"])
            for item in content
            if item["max_salary"].isdigit()
        ]
    )


def get_min_salary(path):
    content = read(path)
    return min(
        [
            int(item["min_salary"])
            for item in content
            if item["min_salary"].isdigit()
        ]
    )


def matches_salary_range(job, salary):
    if (
        "min_salary" not in job
        or "max_salary" not in job
        or not str(job["min_salary"]).isdigit()
        or not str(job["max_salary"]).isdigit()
        or not isinstance(salary, int)
        or job["min_salary"] > job["max_salary"]
    ):
        raise ValueError

    if int(job["min_salary"]) <= int(salary) <= int(job["max_salary"]):
        return True

    return False


def filter_by_salary_range(jobs, salary):
    filter_range = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                filter_range.append(job)
        except ValueError:
            False

    return filter_range
