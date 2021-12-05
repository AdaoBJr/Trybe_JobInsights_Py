from src.jobs import read
# from jobs import read


def get_unique_job_types(path):
    job_list = read(path)
    job_types = []
    for job in job_list:
        if job["job_type"] not in job_types:
            job_types.append(job["job_type"])
    return job_types


def filter_by_job_type(jobs, job_type):
    job_list = []
    for job in jobs:
        if job["job_type"] == job_type:
            job_list.append(job)
    return job_list


def get_unique_industries(path):
    job_list = read(path)
    industries = []
    for job in job_list:
        if job["industry"] not in industries and job["industry"] != "":
            industries.append(job["industry"])
    return industries


def filter_by_industry(jobs, industry):
    job_list = []
    for job in jobs:
        if job["industry"] == industry:
            job_list.append(job)
    return job_list


def get_max_salary(path):
    job_list = read(path)
    salary = []
    for job in job_list:
        if job["max_salary"] not in salary and job["max_salary"].isdigit():
            salary.append(int(job["max_salary"]))
    return max(salary)


def get_min_salary(path):
    job_list = read(path)
    salary = []
    for job in job_list:
        if job["min_salary"] not in salary and job["min_salary"].isdigit():
            salary.append(int(job["min_salary"]))
    return min(salary)


def matches_salary_range(job, salary):
    if (
        "min_salary" not in job
        or "max_salary" not in job
        or type(job["min_salary"]) is not int
        or type(job["max_salary"]) is not int
        or int(job["min_salary"]) > int(job["max_salary"])
    ):
        raise ValueError
    else:
        try:
            if (job["min_salary"]) <= salary <= (job["max_salary"]):
                return True
            else:
                return False
        except ValueError as err:
            return err


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
