import csv

# REFATORAR TODOS: Tentar resolver usando list/dict comprehension


def get_unique_job_types(path):
    result = []
    with open(path) as file:
        content = csv.DictReader(file, delimiter=",", quotechar='"')
        for row in content:
            result.append(row['job_type'])
    my_set = set(result)
    return list(my_set)


def filter_by_job_type(jobs, job_type):
    result = []
    for val in jobs:
        if(val['job_type'] == job_type):
            result.append(val)
    return result


def get_unique_industries(path):
    result = []
    with open(path) as file:
        content = csv.DictReader(file, delimiter=",", quotechar='"')
        for val in content:
            if(val['industry'] != ''):
                result.append(val['industry'])
    my_set = set(result)
    return list(my_set)


def filter_by_industry(jobs, industry):
    result = []
    for val in jobs:
        if(val['industry'] == industry):
            result.append(val)
    return result


def get_max_salary(path):
    result = []
    with open(path) as file:
        content = csv.DictReader(file, delimiter=",", quotechar='"')
        for val in content:
            if(val['max_salary'] != '' and val['max_salary'] != 'invalid'):
                result.append(int(val['max_salary']))
    return max(result)


def get_min_salary(path):
    result = []
    with open(path) as file:
        content = csv.DictReader(file, delimiter=",", quotechar='"')
        for val in content:
            if(val['min_salary'] != '' and val['min_salary'] != 'invalid'):
                result.append(int(val['min_salary']))
    return min(result)


def matches_salary_range(job, salary):
    min = job['min_salary'] if 'min_salary' in job else None
    max = job['max_salary'] if 'max_salary' in job else None

    if(type(max) != int
            or type(min) != int
            or type(salary) != int):
        raise ValueError
    elif(min > max):
        raise ValueError
    else:
        return True if min <= salary <= max else False


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
    return []
