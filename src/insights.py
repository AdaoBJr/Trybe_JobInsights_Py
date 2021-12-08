from src.jobs import read


def get_unique_job_types(path):
    list_of_dictionarie = read(path)
    empty_list = []
    for val in list_of_dictionarie:
        job_type = val["job_type"]
        if job_type in empty_list:
            continue
        elif job_type == '':
            continue
        else:
            empty_list.append(job_type)
    return empty_list


def filter_by_job_type(jobs, job_type):
    empty_list = []
    for val in jobs:
        if val['job_type'] == job_type:
            empty_list.append(val)
        else:
            continue
    return empty_list


def get_unique_industries(path):
    list_of_dictionarie = read(path)
    empty_list = []
    for val in list_of_dictionarie:
        industry = val["industry"]
        if industry in empty_list:
            continue
        elif industry == '':
            continue
        else:
            empty_list.append(industry)
    return empty_list


def filter_by_industry(jobs, industry):
    empty_list = []
    for val in jobs:
        if val['industry'] == industry:
            empty_list.append(val)
        else:
            continue
    return empty_list


def get_max_salary(path):
    list_of_dictionarie = read(path)
    max_salary = 0
    for val in list_of_dictionarie:
        max = val["max_salary"]
        if max == '' or max == 'invalid' or (int(max) < int(max_salary)):
            continue
        else:
            max_salary = max
    return int(max_salary)


def get_min_salary(path):
    list_of_dictionarie = read(path)
    min_salary = get_max_salary(path)
    for val in list_of_dictionarie:
        max = val["min_salary"]
        if max == '' or max == 'invalid' or (int(max) > int(min_salary)):
            continue
        else:
            min_salary = max
    return int(min_salary)


def matches_salary_range(job, salary):
    if 'min_salary' not in job or 'max_salary' not in job:
        raise ValueError('ValueError')
    if (type(job['min_salary']) != int or type(job['max_salary']) != int or
            type(salary) != int):
        raise ValueError('ValueError')
    if job['min_salary'] > job['max_salary']:
        raise ValueError('ValueError')

    return(job['min_salary'] <= salary <= job['max_salary'])


def filter_by_salary_range(jobs, salary):
    empty_list = []
    for val in jobs:
        try:
            if matches_salary_range(val, salary):
                empty_list.append(val)
        except ValueError:
            pass
    return empty_list
