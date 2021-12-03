from src.jobs import read


def get_unique_job_types(path):
    data = read(path)
    all_jobs = []
    for row in data:
        if row['job_type'] not in all_jobs:
            all_jobs.append(row['job_type'])

    return all_jobs


def filter_by_job_type(jobs, job_type):
    # return list(filter(lambda job: (job['job_type'] == job_type), jobs))
    return [job for job in jobs if job['job_type'] == job_type]


def get_unique_industries(path):
    data = read(path)
    all_industries = []
    for row in data:
        if row['industry'] not in all_industries and row['industry'] != '':
            all_industries.append(row['industry'])

    return all_industries


def filter_by_industry(jobs, industry):
    return [job for job in jobs if job['industry'] == industry]


def get_max_salary(path):
    data = read(path)
    max_salary = 0
    for row in data:
        try:
            max_salary_row = int(row['max_salary'])
            if(max_salary_row > max_salary):
                max_salary = max_salary_row
        except ValueError:
            continue

    return max_salary


def get_min_salary(path):
    data = read(path)
    min_salary = get_max_salary(path)
    for row in data:
        try:
            min_salary_row = int(row['min_salary'])
            if(min_salary_row < min_salary):
                min_salary = min_salary_row
        except ValueError:
            continue

    return min_salary


def matches_salary_range(job, salary):
    if('min_salary' not in job or 'max_salary' not in job):
        raise ValueError('chave inexistente!')
    if(type(job['min_salary']) != int or type(job['max_salary']) != int):
        raise ValueError('min e max salary dever ser inteiros!')
    elif (job['min_salary'] > job['max_salary']):
        raise ValueError('Valor mínimo deve ser menor que valor máximo')

    return job['min_salary'] <= salary <= job['max_salary']


def filter_by_salary_range(jobs, salary):
    result = []
    for job in jobs:
        try:
            if(matches_salary_range(job, salary)):
                result.append(job)
        finally:
            continue

    return result
