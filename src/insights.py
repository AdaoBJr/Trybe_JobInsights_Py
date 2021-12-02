from .jobs import read


def get_unique_job_types(path):
    job_types = set()
    jobs_dict = read(path)
    for dict in jobs_dict:
        job_types.add(dict["job_type"])
    return list(job_types)


def filter_by_job_type(jobs, job_type):
    jobs_list = []
    for job in jobs:
        if job["job_type"] == job_type:
            jobs_list.append(job)
    return jobs_list


def get_unique_industries(path):
    industries = set()
    jobs_dict = read(path)
    for dict in jobs_dict:
        if dict["industry"] != "":
            industries.add(dict["industry"])
    return list(industries)


def filter_by_industry(jobs, industry):
    instrudies_list = []
    for job in jobs:
        if job["industry"] == industry:
            instrudies_list.append(job)
    return instrudies_list


def get_max_salary(path):
    max_salaries = set()
    jobs_list = read(path)
    for job in jobs_list:
        if job["max_salary"].isnumeric():
            max_salaries.add(int(job["max_salary"]))
    return max(list(max_salaries))


def get_min_salary(path):
    min_salaries = []
    jobs_list = read(path)
    for job in jobs_list:
        if job["min_salary"].isnumeric():
            min_salaries.append(int(job["min_salary"]))
    return min(min_salaries)


def matches_salary_range(job, salary):
    if (
        "min_salary" not in job
        or "max_salary" not in job
        or not isinstance(job["min_salary"], int)
        or not isinstance(job["max_salary"], int)
        or job["min_salary"] > job["max_salary"]
        or not isinstance(salary, int)
    ):
        raise ValueError("Um ou vários inputs estão errados")

    if job["min_salary"] <= salary <= job["max_salary"]:
        return True
    else:
        return False


def filter_by_salary_range(jobs, salary):
    jobs_list = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                jobs_list.append(job)
        except ValueError:
            pass
    return jobs_list

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
