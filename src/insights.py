from .jobs import read


def get_unique_job_types(path):
    unic_jobs = set()
    list_of_jobs = read(path)
    for job in list_of_jobs:
        if job['job_type'] != '':
            unic_jobs.add(job['job_type'])
    return unic_jobs


def filter_by_job_type(jobs, job_type):
    filtered_jobs = []
    for job in jobs:
        if job['job_type'] == job_type:
            filtered_jobs.append(job)
    return filtered_jobs


def get_unique_industries(path):
    unic_industries = set()
    list_of_jobs = read(path)
    for job in list_of_jobs:
        if job['industry'] != '':
            unic_industries.add(job['industry'])
    return unic_industries


def filter_by_industry(jobs, industry):
    filtered_industries = []
    for job in jobs:
        if job['industry'] == industry:
            filtered_industries.append(job)
    return filtered_industries


def get_max_salary(path):
    salaries = []
    list_of_jobs = read(path)
    for job in list_of_jobs:
        if (job['max_salary'] != 'invalid') and (job['max_salary'] != ''):
            salaries.append(int(job['max_salary']))

    return max(salaries)


def get_min_salary(path):
    salaries = []
    list_of_jobs = read(path)
    for job in list_of_jobs:
        if (job['min_salary'] != 'invalid') and (job['min_salary'] != ''):
            salaries.append(int(job['min_salary']))

    return min(salaries)


def matches_salary_range(job, salary):
    test_salary = (
        'min_salary' not in job
        or 'max_salary' not in job
        or type(job['min_salary']) != int
        or type(job['max_salary']) != int
        or type(salary) != int
        or job['min_salary'] > job['max_salary']
    )
    if test_salary:
        raise ValueError
    return job['min_salary'] <= salary <= job['max_salary']


def filter_by_salary_range(jobs, salary):
    jobs_filtered_by_salary = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                jobs_filtered_by_salary.append(job)
        except ValueError:
            pass
    return jobs_filtered_by_salary
