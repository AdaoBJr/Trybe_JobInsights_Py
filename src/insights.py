from src.jobs import read


def get_unique_job_types(path):
    file = read(path)
    jobs_title = set()
    for job in file:
        jobs_title.add(job['job_type'])
    return list(jobs_title)


def filter_by_job_type(jobs, job_type):
    return [job for job in jobs if job["job_type"] == job_type]


def get_unique_industries(path):
    file = read(path)
    jobs_industries = set()
    for job in file:
        if len(job["industry"]) > 0:
            jobs_industries.add(job["industry"])
    return jobs_industries


def filter_by_industry(jobs, industry):
    filter_industrys = [job for job in jobs if job["industry"] == industry]
    return filter_industrys


def get_max_salary(path):
    file = read(path)
    max_salary_jobs = 0
    for job in file:
        if job["max_salary"].isnumeric():
            if float(job["max_salary"]) > max_salary_jobs:
                max_salary_jobs = int(job["max_salary"])
    return max_salary_jobs


def get_min_salary(path):
    file = read(path)
    min_salary_jobs = 100000000000
    for job in file:
        if job["min_salary"].isnumeric():
            if float(job["min_salary"]) < min_salary_jobs:
                min_salary_jobs = int(job["min_salary"])
    return min_salary_jobs


def matches_salary_range(job, salary):
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError("O salario não existe")
    elif (type(job["min_salary"]) == str or type(job["max_salary"]) == str or
          type(salary) == str):
        raise ValueError("O salario não é valido")
    elif job["max_salary"] < job["min_salary"]:
        raise ValueError("O salario maximo é menor que o minimo")
    elif job["min_salary"] <= salary <= job["max_salary"]:
        return True
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
