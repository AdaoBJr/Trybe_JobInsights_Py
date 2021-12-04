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
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    pass


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
