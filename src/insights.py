from src.jobs import read


def get_unique_job_types(path):
    content_list = read(path)
    job_types = set()
    for job in content_list:
        job_types.add(job["job_type"])
    return job_types


def filter_by_job_type(jobs, job_type):
    filtered_jobs = []
    for job in jobs:
        if job["job_type"] == job_type:
            filtered_jobs.append(job)
    return (filtered_jobs)


def get_unique_industries(path):
    content_list = read(path)
    industries = set()
    for job in content_list:
        if job["industry"] != "":
            industries.add(job["industry"])
    return industries


def filter_by_industry(jobs, industry):
    filtered_jobs = []
    for job in jobs:
        if job["industry"] == industry:
            filtered_jobs.append(job)
    return (filtered_jobs)


def get_max_salary(path):
    content_list = read(path)
    max_salary_selected = 0
    for job in content_list:
        if job["max_salary"] != "" and job["max_salary"].isdigit():
            if int(job["max_salary"]) > max_salary_selected:
                max_salary_selected = int(job["max_salary"])
    return max_salary_selected


def get_min_salary(path):
    content_list = read(path)
    min_salary_selected = get_max_salary(path)
    for job in content_list:
        if job["min_salary"] != "" and job["min_salary"].isdigit():
            if int(job["min_salary"]) < min_salary_selected:
                min_salary_selected = int(job["min_salary"])
    return min_salary_selected


def matches_salary_range(job, salary):
    if ("min_salary" or "max_salary") not in job:
        raise ValueError("Job does not have a salary range")
    elif type(job["min_salary"] or job["max_salary"] or salary) != int:
        raise ValueError("Job salary range or Salary is not an integer")
    elif job["min_salary"] > job["max_salary"]:
        raise ValueError("Job min_salary is greater than max_salary")

    if salary >= job["min_salary"] and salary <= job["max_salary"]:
        return True
    else:
        return False


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
