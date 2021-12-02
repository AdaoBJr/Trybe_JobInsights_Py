from .jobs import read


def get_unique_job_types(path):
    file = read(path)
    unique_job_type = set()
    for job in file:
        if job['job_type'] != '':
            unique_job_type.add(job['job_type'])

    # https://www.geeksforgeeks.org/python-convert-set-into-a-list/
    return list(unique_job_type)


def filter_by_job_type(jobs, job_type):
    result = []
    for job in jobs:
        if job['job_type'] == job_type:
            result.append(job)
    return result


def get_unique_industries(path):
    file = read(path)
    unique_industry = set()
    for job in file:
        if job['industry'] != '':
            unique_industry.add(job['industry'])

    return list(unique_industry)


def filter_by_industry(jobs, industry):
    result = []
    for job in jobs:
        if job['industry'] == industry:
            result.append(job)
    return result


def get_max_salary(path):
    file = read(path)
    biggest_salary = 0
    only_valid_salary = []
    for job in file:
        if job['max_salary'] != '' and job['max_salary'] != 'invalid':
            only_valid_salary.append(job['max_salary'])
    for salary in only_valid_salary:
        salary_in_number = int(salary)
        if salary_in_number > biggest_salary:
            biggest_salary = int(salary)
    return biggest_salary


def get_min_salary(path):
    file = read(path)
    only_valid_salary = []
    for job in file:
        if job['min_salary'] != '' and job['min_salary'] != 'invalid':
            only_valid_salary.append(job['min_salary'])

    lesser_salary = int(only_valid_salary[0])
    for salary in only_valid_salary:
        salary_in_number = int(salary)
        if salary_in_number < lesser_salary:
            lesser_salary = int(salary)
    return lesser_salary


def validate_max_and_mix_salary(job):
    if 'min_salary' not in job or 'max_salary' not in job:
        # https://rollbar.com/blog/throwing-exceptions-in-python/
        raise ValueError('Job needs "min_salary" and "max_salary" keys')

    if (
        not isinstance(job['min_salary'], int)
        or not isinstance(job['max_salary'], int)
    ):
        raise ValueError('Job keys and salary have to be a int')

    if job['min_salary'] > job['max_salary']:
        raise ValueError('Min. salary cannot be bigger than max. salary')


def matches_salary_range(job, salary):
    validate_max_and_mix_salary(job)
    if (not isinstance(salary, int)):
        raise ValueError('Job keys and salary have to be a int')

    if job['min_salary'] <= salary <= job['max_salary']:
        return True
    else:
        return False


def filter_by_salary_range(jobs, salary):
    works = []
    matched_salary = []
    for job in jobs:
        if (
            job['min_salary'] > -1
            and job['max_salary'] > -1
            and job['min_salary'] < job['max_salary']
            and isinstance(salary, int)
        ):
            works.append(job)

    for job in works:
        if matches_salary_range(job, salary):
            matched_salary.append(job)

    return matched_salary
