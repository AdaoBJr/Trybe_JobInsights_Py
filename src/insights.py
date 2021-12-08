# from jobs import read
from src.jobs import read


def get_unique_job_types(path):
    jobs_list = read(path)
    job_types = set()
    job_types_list = []

    for job in jobs_list:
        job_types.add(job['job_type'])

    for job_type in job_types:
        if job_type != '':
            job_types_list.append(job_type)

    return job_types_list


def filter_by_job_type(jobs, job_type):
    job_types_list = []

    for job in jobs:
        if job['job_type'] == job_type:
            job_types_list.append(job)
    
    return job_types_list



def get_unique_industries(path):
    jobs_list = read(path)
    industry_types = set()
    industry_types_list = []

    for job in jobs_list:
        industry_types.add(job['industry'])

    for industry in industry_types:
        if industry != '':
            industry_types_list.append(industry)


    return industry_types_list


def filter_by_industry(jobs, industry):
    industry_list = []

    for job in jobs:
        if job['industry'] == industry:
            industry_list.append(job)
    
    return industry_list



def get_max_salary(path):
    jobs_list = read(path)
    salaries = set()

    for job in jobs_list:
        if job['max_salary'].isnumeric():
            salaries.add(int(job['max_salary']))
    
    return max(salaries)


def get_min_salary(path):

    jobs_list = read(path)
    salaries = set()

    for job in jobs_list:
        if job['min_salary'].isnumeric():
            salaries.add(int(job['min_salary']))
    
    return min(salaries)


def matches_salary_range(job, salary):
    if 'min_salary' not in job.keys():
        raise ValueError('min_salary does not exists')

    elif 'max_salary' not in job.keys():
        raise ValueError('max_salary does not exists')
    
    elif type(job['min_salary']) != int:
        raise ValueError('min_salary must to be a int number')

    elif type(job['max_salary']) != int:
        raise ValueError('max_salary must to be a int number')

    elif type(salary) != int:
        raise ValueError('salary must to be a int number')

    elif job['min_salary'] > job['max_salary']:
        raise ValueError('job["min_salary"] is greater than job["max_salary"]')

    
    return job['min_salary'] <= salary <= job['max_salary']


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    result = []

    for job in jobs:
        if (
            job['min_salary'] != ''
            and job['max_salary'] != ''
            and 'max_salary' in job.keys()
            and 'min_salary' in job.keys()
            and type(salary) == int
            and int(job['min_salary']) <= salary
            and int(job['max_salary']) >= salary
        ):
            result.append(job)
        

    return result

if __name__ == '__main__':
    jobs = read('src/jobs.csv')
    # job_teste = { 'min_salary': 3200, 'max_salary': 30000 }
    # teste = get_unique_job_types('src/jobs.csv')
    # teste = get_unique_industries('src/jobs.csv')
    teste = get_max_salary('src/jobs.csv')
    # teste = get_min_salary('src/jobs.csv')
    # teste = filter_by_job_type(jobs, 'FULL_TIME')
    # teste = filter_by_industry(jobs, 'Business Services')
    # teste = matches_salary_range(job_teste, 4900)
    # teste2 = type(ValueError('opa'))
    # teste = filter_by_salary_range(jobs, 50000)
    print(teste)