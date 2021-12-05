from src import jobs


def get_unique_job_types(path):
    job_type_list = []
    file_reader = jobs.read(path)
    for job in file_reader:
        # https://appdividend.com/2020/01/21/python-list-contains-how-to-check-if-item-exists-in-list/
        if job["job_type"] not in job_type_list:
            job_type_list.append(job["job_type"])

    return job_type_list


def filter_by_job_type(jobs, job_type):
    jobs_list = []
    for job in jobs:
        print(job)
        if job['job_type'] == job_type:
            jobs_list.append(job)
    return jobs_list


def get_unique_industries(path):
    job_industry_list = []
    file_reader = jobs.read(path)
    for job in file_reader:
        if job["industry"] not in job_industry_list and job["industry"] != '':
            job_industry_list.append(job["industry"])

    return job_industry_list


def filter_by_industry(jobs, industry):
    industry_list = []
    for job in jobs:
        if job['industry'] == industry:
            industry_list.append(job)
    return industry_list


def get_max_salary(path):
    max_salary = []
    file_reader = jobs.read(path)
    for job in file_reader:
        if job["max_salary"] != '' and job["max_salary"] != 'invalid':
            max_salary.append(int(job["max_salary"]))
    # https://www.w3schools.com/python/ref_func_max.asp
    return max(max_salary)


def get_min_salary(path):
    min_salary = []
    file_reader = jobs.read(path)
    for job in file_reader:
        if job["min_salary"] != '' and job["min_salary"] != 'invalid':
            min_salary.append(int(job["min_salary"]))
    # https://www.w3schools.com/python/ref_func_min.asp
    return min(min_salary)


def matches_salary_range(job, salary):
    if (
        "min_salary" not in job
        or "max_salary" not in job
        or type(job["min_salary"]) != int
        or type(job["max_salary"]) != int
        or job["min_salary"] > job["max_salary"]
        or type(salary) != int
    ):
        raise ValueError("Does not match the salary range")
        
    if salary >= job["min_salary"] and salary <= job["max_salary"]:
        return True
    else:
        return False


    raise ValueError(salary)


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
