from src.jobs import read


def get_unique_job_types(path):
    read_file = read(path)
    job_types = set()
    for job in read_file:
        job_types.add(job["job_type"])
    return job_types


def filter_by_job_type(jobs, job_type):
    return [job for job in jobs if job["job_type"] == job_type]


def get_unique_industries(path):
    read_file = read(path)
    industries_types = set()
    for industry in read_file:
        if industry["industry"] != "":
            industries_types.add(industry["industry"])
    return industries_types


def filter_by_industry(jobs, industry):
    return [job for job in jobs if job["industry"] == industry]


def get_max_salary(path):
    # https://docs.python.org/3/library/stdtypes.html#str.isnumeric
    read_file = read(path)
    max_salary = 0
    for job in read_file:
        if (
            job["max_salary"].isnumeric()
            and int(job["max_salary"]) > max_salary
        ):
            max_salary = int(job["max_salary"])
    return max_salary


def get_min_salary(path):
    # Ideia dada pelo Arlen - outra forma de fazer
    read_file = read(path)
    min_salary = []
    for job in read_file:
        if job["min_salary"] != "":
            try:
                min_salary.append(int(job["min_salary"]))
            except ValueError:
                pass
    return min(min_salary)


def matches_salary_range(job, salary):
    itsfalse = (
        "max_salary" not in job
        or "min_salary" not in job
        or type(job["min_salary"]) != int
        or type(job["max_salary"]) != int
        or type(salary) != int
        or job["min_salary"] > job["max_salary"]
    )
    if itsfalse:
        raise ValueError
    return job["min_salary"] <= salary <= job["max_salary"]


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
