from src.jobs import read

# from jobs import read


def get_column_unique(dict, name_column):
    return set(map(lambda job: job[name_column], dict))


def get_unique_job_types(path):
    return get_column_unique(read(path), "job_type")


def filter_by_job_type(jobs, job_type):
    jobs_filter = filter(lambda job: job["job_type"] == job_type, jobs)
    return list(jobs_filter)


def get_unique_industries(path):
    industries = get_column_unique(read(path), "industry")
    return list(filter(None, industries))


def filter_by_industry(jobs, industry):
    indrutries = filter(lambda job: job["industry"] == industry, jobs)
    return list(indrutries)


def get_max_salary(path):
    salaries = map(lambda job: job["max_salary"], read(path))
    salaries_str = filter(str.isdigit, salaries)
    salary_max = max(map(lambda salary: int(salary), salaries_str))
    return salary_max


def get_min_salary(path):
    salaries = map(lambda job: job["min_salary"], read(path))
    salaries_str = filter(str.isdigit, salaries)
    salary_min = min(map(lambda salary: int(salary), salaries_str))
    return salary_min


def validate_exist_column_job(salaries, job):
    if not all(salary in job for salary in salaries):
        raise ValueError


def validate_values_is_integer(values):
    if not all(isinstance(value, int) for value in values):
        raise ValueError


def validate_range_salary(job):
    if job["min_salary"] > job["max_salary"]:
        raise ValueError


def matches_salary_range(job, salary):
    validate_exist_column_job(["min_salary", "max_salary"], job)
    validate_values_is_integer([salary, job["min_salary"], job["max_salary"]])
    validate_range_salary(job)
    return job["min_salary"] <= salary <= job["max_salary"]


def filter_by_salary_range(jobs, salary):
    salaries = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                salaries.append(job)
        except ValueError:
            pass
    return salaries
