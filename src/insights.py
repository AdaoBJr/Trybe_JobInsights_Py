from src.jobs import read


def get_unique_job_types(path):
    jobs_list = read(path)
    job_types = []
    for job in jobs_list:
        if not (job['job_type'] in job_types):
            job_types.append(job['job_type'])
    return job_types


def filter_by_job_type(jobs, job_type):
    job_list = []
    for job in jobs:
        if job['job_type'] == job_type:
            job_list.append(job)
    return job_list


def get_unique_industries(path):
    jobs_list = read(path)
    industries = []
    for job in jobs_list:
        if not (job['industry'] in industries) and job['industry']:
            industries.append(job['industry'])
    return industries


def filter_by_industry(jobs, industry):
    job_list = []
    for job in jobs:
        if job['industry'] == industry:
            job_list.append(job)
    return job_list


def get_max_salary(path):
    jobs_list = read(path)
    max_salary = 0
    for job in jobs_list:
        if job['max_salary'].isdigit():
            if (float(job['max_salary']) > max_salary):
                max_salary = float(job['max_salary'])
    return max_salary


def get_min_salary(path):
    jobs_list = read(path)
    min_salary = 999999
    for job in jobs_list:
        if job['min_salary'].isdigit():
            if (int(job['min_salary']) < min_salary):
                min_salary = int(job['min_salary'])
    return min_salary


def matches_salary_range(job, salary):
    if "max_salary" in job and "min_salary" in job:
        max_salary = job["max_salary"]
        min_salary = job["min_salary"]
        if not (type(salary) == int and
                type(min_salary) == int and
                type(max_salary) == int and
                min_salary < max_salary
                ):
            raise ValueError('Invalid arguments')
        elif (min_salary <= salary <= max_salary):
            return True
        return False
    raise ValueError('Invalid arguments')


def filter_by_salary_range(jobs, salary):
    job_options = []
    for job in jobs:
        try:
            valid_job = matches_salary_range(job, salary)
        except ValueError:
            continue
        else:
            if valid_job:
                job_options.append(job)
    return job_options
