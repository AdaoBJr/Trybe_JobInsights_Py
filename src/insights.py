from src.jobs import read


# print(get_unique_industries("src/jobs.csv"))


def get_unique_job_types(path):
    auxJobs = read(path)
    job_type = set()
    for i in auxJobs:
        job_type.add(i['job_type'])
    return job_type


def filter_by_job_type(jobs, job_type):
    aux = []

    for item in jobs:
        if job_type in item.values():
            aux.append(item)

    return aux


def get_unique_industries(path):
    auxJobs = read(path)
    job_type = set()
    for i in auxJobs:
        if i['industry'] != '':
            job_type.add(i['industry'])
    return job_type


def filter_by_industry(jobs, industry):
    aux = []

    for item in jobs:
        if industry in item.values():
            aux.append(item)

    return aux


def get_max_salary(path):
    auxJobs = read(path)
    maior = 0
    for item in auxJobs:
        if item['max_salary'].isnumeric():
            aux = int(item['max_salary'])
            if aux >= maior:
                maior = aux
    return maior


def get_min_salary(path):
    auxJobs = read(path)
    menor = 99999999999999999999
    for item in auxJobs:
        if item['min_salary'].isnumeric():
            aux = int(item['min_salary'])
            if aux <= menor:
                menor = aux
    return menor


def matches_salary_range(job, salary):
    if (
        "min_salary" not in job
        or "max_salary" not in job
        or not isinstance(job["min_salary"], int)
        or not isinstance(job["max_salary"], int)
        or job["min_salary"] > job["max_salary"]
    ):
        raise ValueError("")
    elif job["min_salary"] <= salary and salary <= job["max_salary"]:
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
