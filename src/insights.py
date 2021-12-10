from src.jobs import read


def get_unique_job_types(path):
    all_jobs = read(path)
    unique_job_types = set()

    for jobs in all_jobs:
        unique_job_types.add(jobs['job_type'])

    return list(unique_job_types)


def filter_by_job_type(jobs, job_type):
    jobs_list = []
    for job in jobs:
        if job['job_type'] == job_type:
            jobs_list.append(job)
    return jobs_list


def get_unique_industries(path):
    all_jobs = read(path)
    job_industry_list = []
    for job in all_jobs:
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
    all_jobs = read(path)
    max_salary = []
    for job in all_jobs:
        if job["max_salary"] != '' and job["max_salary"] != 'invalid':
            max_salary.append(int(job["max_salary"]))
    return max(max_salary)


def get_min_salary(path):
    all_jobs = read(path)
    min_salary = []
    for job in all_jobs:
        if job["min_salary"] != '' and job["min_salary"] != 'invalid':
            min_salary.append(int(job["min_salary"]))
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


if __name__ == '__main__':
    print(get_unique_job_types('jobs.csv'))
